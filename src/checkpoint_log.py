"""Recognise the first native pre-shell write separately on each MPI rank.

MPI preserves each rank's stream order, but not the ordering between ranks.
Consequently a rank's completion may arrive after the master's shell logs.
Only a completion following that same rank's first subset write is accepted.
"""
import re

START = re.compile(r'^\[(\d+)\] Writing subsetted mesh to time (\d+(?:\.\d+)?)\.$')
DONE = re.compile(r'^\[(\d+)\] Dumped mesh in = ')
OTHER_WRITE = re.compile(r'^\[(\d+)\] Writing .*mesh')


def pre_shell_checkpoint(text, ranks=(0, 1)):
    expected = {str(rank) for rank in ranks}
    started, completed = {}, set()
    # The last unterminated line may still be in flight.
    for line in text[:text.rfind('\n') + 1].splitlines():
        match = START.fullmatch(line)
        if match:
            rank, instance = match.groups()
            if rank not in expected:
                raise ValueError('Unexpected MPI rank in checkpoint log: ' + rank)
            if rank not in started:
                started[rank] = instance
            elif rank not in completed:
                raise ValueError('A second subset write preceded rank completion: ' + rank)
            continue
        match = DONE.match(line)
        if match:
            rank = match[1]
            if rank in started:
                completed.add(rank)
            if completed == expected:
                if len(set(started.values())) != 1:
                    raise ValueError('MPI checkpoint instances disagree: ' + repr(started))
                return {'subsetTime': next(iter(started.values())),
                        'stopMarker': [[rank, started[rank]] for rank in sorted(expected)]}
            continue
        match = OTHER_WRITE.match(line)
        if match and match[1] in started and match[1] not in completed:
            raise ValueError('Another mesh write preceded rank completion: ' + match[1])
    return None

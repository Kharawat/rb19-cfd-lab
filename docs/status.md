# Status and evidence boundaries

Snapshot date: **16 October 2026**. This file records a project status, not a live job monitor.

## Confirmed

- The detailed geometry and the three included studio renders already exist.
- The recorded final repaired-surface audit passed: closed/watertight, consistent winding, zero reported self-intersections, 2,114,416 triangles and 7 named patches.
- The recorded native Blender validation reopened the saved project and checked identities, patch counts, units, packed textures, and camera setup.
- A native mesh checkpoint containing **3,154,323 cells** was previously saved and verified.
- The 15:27–17:06 production attempt reached **4,892,045 cells in RAM**, then reduced the retained region to **3,382,439 cells**. Neither state was written as a new checkpoint. The host reserve guard stopped the run after **99 minutes 49 seconds** because Windows available RAM remained below 1 GiB for 15 seconds. No cgroup OOM or maximum-memory event occurred, and the owned job ended with no remaining processes.
- The post-stop audit passed at **23:35:51 Bangkok time on 16 October 2026**: live saved checkpoint hashes match the immutable 3,154,323-cell snapshot, and the canonical `0` state is unchanged. This fresh audit checked mesh files and small inputs. Full geometry identity remains a separate pre-run gate; the large geometry was not freshly rehashed by this audit.
- The audit now correctly links the archived previous log to its prior audit: the stage wrapper names an archived log with the next stage's timestamp. The earlier audit refusal came from an incorrect log-pairing check, not evidence of damaged mesh files. The corrected audit passed 26 isolated scenarios before inspecting the live checkpoint.
- A fresh continuation preflight was refused before service creation: the minimum available Windows RAM was 5.02 GiB against the stricter 6.5 GiB startup floor. A subsequent 25-second observation also fell from 6.93 to 5.03 GiB. No new mesher was launched by this continuation; all checkpoint markers remain preserved.

## Acceptance status

| Check | Status |
|---|---|
| Post-stop checkpoint audit | Passed; 3,154,323 remains the last verified saved cell count |
| Final castellation, snap, and layer completion | Not accepted as complete |
| Final topology/quality and narrow-passage coverage | Pending |
| Flow solver | Not started |
| Residual, mass-balance, force stability, and near-wall review | Not available |
| Grid sensitivity and comparison with external measurements | Not performed |

The public snapshot contains **no validated drag coefficient, downforce coefficient, pressure field, or velocity field**. A render, a closed triangulated surface, a large cell count, and a successful process exit each answer different questions; none establishes a validated aerodynamic result by itself.

## Acceptance path

1. Preserve the audited 3,154,323-cell checkpoint and its immutable snapshot.
2. Resume only from that verified saved state after a separately checked preparation and fresh Windows headroom of at least 6.5 GiB. Keep full geometry/input identity checks, finite RAM/swap limits, and the live 1 GiB/15-second host reserve guard intact. A brief rise in free RAM is not proof that later mesh stages will fit.
3. Complete mesh stages and inspect topology, quality, layer coverage, and critical slot passages.
4. Start the flow solver only after the mesh gate passes.
5. Assess residuals, conservation, force stability, near-wall resolution, and mesh sensitivity before interpreting coefficients.

The case's 50 m/s inlet, moving ground, rotating wheels, and assumed 1.5 m² reference area describe the intended setup. They do not imply that a production flow solution has been obtained.

Compact source-derived records are in [evidence/](../evidence/README.md). Large native checkpoints and full local logs are intentionally absent from the public snapshot.

# Compact technical evidence

These JSON files are selected public fields from local project reports. Personal paths, process IDs, cloud-account data, full logs, and large geometry/checkpoint payloads are excluded. Original small-report hashes are retained where useful for traceability; the omitted source reports are not independently reproducible from this repository alone.

| Record | What it supports |
|---|---|
| [model-provenance.json](model-provenance.json) | Original creator, source, CC BY 4.0, and recorded acquisition identity |
| [geometry-summary.json](geometry-summary.json) | Recorded surface checks, native-file reopening, and finite geometric clearance probes |
| [status.json](status.json) | Current rear-wing delivery, obsolete old-geometry checkpoint, and new volume-mesh requirement; solver not started |
| [workflow-tests.json](workflow-tests.json) | Compact summaries of existing lightweight local workflow tests |
| [public-example-tests.json](public-example-tests.json) | Tests rerun against the code included in this public snapshot |
| [asset-manifest.json](asset-manifest.json) | Original/public image hashes, metadata-only sanitation, byte identity of pixel-bearing PNG chunks, and attribution |

The geometry summary describes completed geometry validation. It does not certify the final fluid volume mesh, near-wall accuracy, convergence, or real-car aerodynamic performance. Finite clearance probes do not prove every passage is adequately resolved.

`status.json` and [docs/status.md](../docs/status.md) must be updated together when new checkpoint or solver evidence is accepted.

# Compact technical evidence

These JSON files are selected public fields from local project reports. Personal paths, process IDs, cloud-account data, full logs, and large geometry/checkpoint payloads are excluded. Original small-report hashes are retained where useful for traceability; the omitted source reports are not independently reproducible from this repository alone.

| Record | What it supports |
|---|---|
| [model-provenance.json](model-provenance.json) | Original creator, source, CC BY 4.0, and recorded acquisition identity |
| [underbody-summary.json](underbody-summary.json) | Current underbody-only union, native open-path probes and preserved DRS after the sidepod edits |
| [geometry-summary.json](geometry-summary.json) | Current individual wing-component checks, native DRS motion and finite slot-section measurements |
| [status.json](status.json) | Current DRS delivery, obsolete old geometry, and new whole-surface/volume-mesh requirements; solver not started |
| [workflow-tests.json](workflow-tests.json) | Compact summaries of existing lightweight local workflow tests |
| [public-example-tests.json](public-example-tests.json) | Tests rerun against the code included in this public snapshot |
| [asset-manifest.json](asset-manifest.json) | Original/public image hashes, metadata-only sanitation, byte identity of pixel-bearing PNG chunks, and attribution |

The wing geometry summary describes the preceding unchanged wing components. The underbody summary identifies the current native file and its new floor assembly. The current whole-car CFD surface has not been accepted. It does not certify the final fluid volume mesh, near-wall accuracy, convergence, or real-car aerodynamic performance. Finite clearance probes do not prove every passage is adequately resolved.

`status.json` and [docs/status.md](../docs/status.md) must be updated together when new checkpoint or solver evidence is accepted.

# Contributions

## Project credit

**Phoom & OpenAI Codex — co-design and development of the RB19 CFD Lab modifications and pipeline.**

Phoom set the project direction, fidelity goals, review priorities, local resource constraints, and publication intent. OpenAI Codex collaborated on reference research, implementation, geometry refinement scripts, validation tools, bounded execution, tests, and documentation. Project decisions and revisions developed through that collaboration.

This credit describes the work on this study. It is not a claim of authorship of the real RB19, the underlying third-party artist mesh, or OpenFOAM and Blender.

## Work represented here

| Area | Project contribution |
|---|---|
| Geometry | Scale/alignment, rear-wing physical section reconstruction, floor/diffuser refinements, and component organization |
| CFD surface | Closed-surface repair, solid union, junction repair, patch assignment, and recorded geometry identities |
| Workflow | OpenFOAM case preparation, staged meshing, checkpoint capture/promotion, cell-budget checks, and evidence gates |
| Resource control | Finite per-job RAM/swap limits and independent host-memory monitoring |
| Verification | Native-file reopening, surface/gap checks, transaction fixtures, MPI-log parser fixtures, and preservation of failed work |
| Presentation | Existing project renders, public technical summaries, explicit uncertainty, and source attribution |

## Upstream contributions

- **Redgrund:** original “Oracle Red Bull F1 Car RB19 2023” artist model, licensed CC BY 4.0.
- **MR-05-001/RB19:** the attributed public redistribution from which the working GLB was obtained. Its web-application license is distinct from the model license; its simulated telemetry is not used as CFD evidence.
- **Red Bull Racing:** the real RB19 car and its original engineering, which this project does not claim to reproduce exactly.
- **Blender, OpenFOAM, and geometry-processing libraries:** third-party tools used in the local workflow. Their source code and licenses are not replaced by this repository's code license.
- **Reference photographers and publishers:** visual references for visible features. Their photographs are linked in the engineering notes but are not redistributed in this repository.

The attribution record and source links are in [ATTRIBUTION.md](ATTRIBUTION.md).

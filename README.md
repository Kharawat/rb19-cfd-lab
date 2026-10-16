# RB19 CFD Lab

**Geometry refinement, verification, and a resource-bounded virtual wind tunnel — co-designed and developed by Phoom & OpenAI Codex.**

This project adapts an attributed RB19 artist model into a detailed Blender study and an OpenFOAM 14 workflow. It documents both the geometry work and the engineering needed to preserve progress on a memory-constrained workstation.

![Three-quarter studio render of the modified RB19 model](assets/hero.png)

*Project render of a modified model based on [Redgrund's “Oracle Red Bull F1 Car RB19 2023”](https://sketchfab.com/3d-models/oracle-red-bull-f1-car-rb19-2023-e4afe46f3aab4b23a418da06fc163821). Model-derived renders are shared under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Full credit and changes: [ATTRIBUTION.md](ATTRIBUTION.md).*

## What we built

- Reconstructed rear-wing sections with physical thickness, continuous camber, and a retained slot and spoon profile.
- Refined the floor-to-diffuser transition, diffuser roof, outer walls, and central spine using public photographs as visual references.
- Kept detailed display geometry and a repaired CFD surface separate, with recorded identities linking the native Blender project to the accepted surface.
- Built staged OpenFOAM meshing, per-job RAM/swap limits, host-memory monitoring, cell-budget checks, and native checkpoint handling.
- Added evidence gates so a saved surface, a saved volume mesh, and a completed flow solution are reported as distinct milestones.

## Current evidence

Snapshot: **16 October 2026**. See [status and acceptance criteria](docs/status.md) for the scope of each claim.

| Milestone | Confirmed status |
|---|---|
| Detailed geometry and existing studio renders | Available |
| Accepted repaired surface | Recorded closed-surface audit passed; 2,114,416 triangles across 7 patches |
| Native Blender file | Saved and reopened successfully in the recorded geometry validation |
| Last verified saved mesh checkpoint | **3,154,323 cells** |
| Later refinement progress | **4,892,045-cell peak**, then **3,382,439 cells after subsetting**, observed only in RAM; neither state was saved |
| Post-stop checkpoint audit | Passed at 23:35 Bangkok time; the saved 3,154,323-cell checkpoint still matches its immutable snapshot |
| Latest production attempt | Stopped after 99 minutes 49 seconds by the host RAM reserve guard; no OOM event |
| Accepted final volume mesh | Pending |
| Flow solver | **Not started** |
| Validated drag/downforce results | **Not available** |

These images show the modified model. They are not pressure contours, wind-tunnel measurements, or evidence of aerodynamic performance.

The next production launch requires at least 6.5 GiB of fresh Windows memory headroom. The finite RAM/swap limits and live 1 GiB reserve guard remain in place; transient cleanup gains do not establish that the full mesh will fit.

## Geometry details

| Diffuser reconstruction | Underfloor view |
|---|---|
| ![Close view of the reconstructed diffuser](assets/diffuser.png) | ![Underside view of the modified model](assets/underfloor.png) |

![Original and reconstructed rear-wing cross sections](assets/rear-wing-section-comparison.png)

The red profiles show the reconstructed sections; the grey profiles show the earlier artist surface. Thickness and unseen sections are modeling assumptions, not measurements of Red Bull team CAD. This study combines visible 2023 features and does not claim one exact race specification.

## Planned flow setup

The case is configured for a **50 m/s** inlet, moving ground, rotating-wheel wall conditions, and a steady external-aerodynamics workflow. The reference area is an **assumed 1.5 m² comparison convention**, not a measured frontal area. These are setup choices; solver execution and aerodynamic acceptance are still pending.

The current work prioritizes a recoverable, auditable mesh before any force-coefficient claim. [Engineering notes](docs/engineering.md) explain the geometry pipeline, checkpoint distinction, and acceptance gates.

## Explore the repository

- [Contribution and co-development credits](CONTRIBUTIONS.md)
- [Model provenance and licenses](ATTRIBUTION.md)
- [Current status and remaining checks](docs/status.md)
- [Compact technical evidence](evidence/README.md)
- [Runnable MPI checkpoint parser](src/checkpoint_log.py) and [its tests](tests/test_checkpoint_log.py)

Run the lightweight example with Python 3.10 or later; no Blender, OpenFOAM, or external packages are needed:

```bash
python -m unittest discover -s tests -v
```

This is a curated portfolio snapshot. The large native model, original asset bundle, volume-mesh checkpoints, full machine-specific controller, and third-party reference photographs are not distributed here. The included parser tests demonstrate one reusable part of the workflow; they do not run or validate CFD.

## Credits and scope

**Phoom & OpenAI Codex co-designed and developed the project-specific modifications, automation, validation, and presentation.** Redgrund created the base artist model. The real RB19 is a Red Bull Racing car; neither Phoom nor Codex designed the original race car or the original artist mesh.

This independent study is not official Red Bull CAD and is not affiliated with or endorsed by Red Bull Racing, Formula 1, the model creator, or the depicted sponsors. Marks remain with their respective owners. Code licensing and model-derived image licensing are separated in [LICENSES.md](LICENSES.md).

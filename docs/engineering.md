# Engineering notes

## Geometry to a CFD case

```mermaid
flowchart LR
    A[Attributed artist model] --> B[Photo-informed wings and native DRS]
    B --> C[Component and motion checks passed]
    C -. next .-> D[Export chosen DRS state and repair transitions]
    D --> E[Whole-car surface acceptance]
    E --> F[Fresh volume mesh and quality gates]
    F --> G[Flow solution and validation]
```

The current visible wings have independent component and motion checks. Retained transition surfaces need a fresh CFD export, union and repair. The older accepted seven-patch surface remains historical, not a representation of these new wings. Its patch scheme was body, frontWing, rearWing and four wheels, with the floor included in body.

## Physical reconstruction choices

The 18 October reconstruction uses four front elements per side, a rear spoon mainplane, rolled tips, an independent hinged flap, adapted endplates/swan-neck and two beam elements. Fourteen closed components passed independent topology/self-intersection checks. Native DRS motion was checked at 16 frames, rear slots at 39 sections per state and front slots at 54 sections. The preceding 17 October incidence correction is historical.

The DRS opening is approximately 18.545 degrees. The design uses a sampled 82 mm slot target below the 85 mm ceiling described in [FIA 2023 Technical Regulations, Issue 6, Article 3.10.10](https://www.fia.com/sites/default/files/fia_2023_formula_1_technical_regulations_-_issue_6_-_2023-04-25.pdf). This does not certify the entire model against FIA regulations. Profiles, thicknesses and unseen details remain assumptions; perspective photos cannot establish exact aerodynamic sections.

The diffuser work addresses the floor transition, roof, outer walls, and central spine. References span several 2023 events. They support visible shape features but do not establish a single exact race trim or hidden internal geometry.

Tyre contact treatment, sealed openings, and the absence of brake-cooling/exhaust mass flow are external-aerodynamics approximations. A closed surface is a meshing prerequisite, not a test of physical fidelity.

## Recoverable meshing under a memory budget

The local workflow uses explicit finite per-job memory and swap limits, Windows-host headroom checks, and stage-level stop conditions. Resource limits are chosen before launch; the controller does not silently expand an active job's allowance. Mesh-refinement forecasts and saved checkpoints help avoid discarding all progress after an interrupted stage.

MPI output order is especially important: one rank may finish writing after another rank has already printed the next refinement step. The included [checkpoint parser](../src/checkpoint_log.py) therefore matches each rank's first native subset write with that same rank's completion and requires a common saved time. It ignores an unterminated final log line.

The parser's result is only a log-level signal. Native mesh metadata, complete files for every rank, geometry/input identity, and the absence of active writers must be checked independently before a checkpoint is accepted. The public tests use small synthetic log fragments and never start a solver.

## Reference links

Photographs are linked for attribution and context; image files from these sources are not redistributed here.

- [Bahrain testing technical detail](https://www.motorsport.com/f1/news/f1-team-tech-2023-test-bahrain/10436662/) — Giorgio Piola / Motorsport Images; rear-wing shape reference.
- [Bahrain 2023 testing gallery](https://espanol.motorsport.com/f1/news/galeria-fotos-formula1-test-bahrein-2023/10435388/) — Motorsport Images; rear views.
- [Miami 2023 pitlane technical gallery](https://www.motorsport.com/f1/news/miami-gp-f1-technical-images-pitlane-explained/10465362/) — Giorgio Piola / Motorsport Images; diffuser reference.
- [Spain 2023 pitlane technical gallery](https://espanol.motorsport.com/f1/news/galeria-tecnica-detalles-f1-pitlane-espana/10476961/) — Giorgio Piola / Motorsport Images; diffuser reference.
- [Exposed RB19 floor after the Monaco incident](https://www.motorsport.com/f1/news/red-bull-f1-car-floor-exposed-williams/10482802/) — Motorsport Images; underfloor reference with perspective and damage limitations.

The primary artist model and its reuse terms are recorded in [ATTRIBUTION.md](../ATTRIBUTION.md).

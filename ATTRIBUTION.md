# Attribution and model provenance

## Original artist model

**“Oracle Red Bull F1 Car RB19 2023” by [Redgrund](https://sketchfab.com/redgrund)**

- Original model: https://sketchfab.com/3d-models/oracle-red-bull-f1-car-rb19-2023-e4afe46f3aab4b23a418da06fc163821
- License: **Creative Commons Attribution 4.0 International (CC BY 4.0)**
- License link: https://creativecommons.org/licenses/by/4.0/
- Legal code: https://creativecommons.org/licenses/by/4.0/legalcode.en

The model-derived renders in `assets/` are shared under **CC BY 4.0**. Credit Redgrund for the original model and Phoom & OpenAI Codex for this project's modifications and rendering. Preserve the source and license links and indicate further changes. These credits do not imply endorsement.

Suggested attribution:

> Based on “Oracle Red Bull F1 Car RB19 2023” by Redgrund, CC BY 4.0. Geometry adaptations and project renders co-designed and developed by Phoom & OpenAI Codex for RB19 CFD Lab. Original model and license: links above. Modified; not official team CAD.

## Acquisition record

The working GLB was obtained from the public, attributed redistribution at [MR-05-001/RB19](https://github.com/MR-05-001/RB19), pinned to commit `468c8db1ffc191554b3b1ab5925fe2bf358d8fa0`.

- [Pinned source asset](https://raw.githubusercontent.com/MR-05-001/RB19/468c8db1ffc191554b3b1ab5925fe2bf358d8fa0/RB19/rb19-model.glb)
- [Pinned attribution README](https://github.com/MR-05-001/RB19/blob/468c8db1ffc191554b3b1ab5925fe2bf358d8fa0/README.md)
- Recorded source size: 19,578,544 bytes
- Recorded source SHA-256: `13b4da1abf02feb72f7a5a91a30d2e6941923914eae64af81456ee359df18693`

The redistribution README and embedded GLB metadata identify Redgrund and CC BY 4.0. The creator's public [Sketchfab metadata](https://api.sketchfab.com/v3/models/e4afe46f3aab4b23a418da06fc163821) was checked again on 16 October 2026 and identified the same creator and license. A compact public record is in [evidence/model-provenance.json](evidence/model-provenance.json).

The redistributed GLB was compressed/optimized with glTF-Transform and Draco and may differ structurally from the creator's source mesh. The upstream website's MIT application license does not replace the model's CC BY 4.0 license. Its simulated telemetry and aerodynamic figures are not used in this project.

## Changes made in this study

Phoom & OpenAI Codex co-designed and developed these project-specific adaptations:

- Rescaled the artist model to an assumed nominal 2 m width, aligned it in metres, and separated editable components.
- Rebuilt four front-wing elements per side, a spoon mainplane, rolled tips, a moving flap and two beam elements on 18 October 2026. Adapted the attributed lower endplates and swan-neck; added a fixed-hinge DRS control, actuator, BYBIT/ORACLE markings and sampled motion checks. These are reconstruction assumptions, not measured team CAD.
- Refined the floor-to-diffuser transition, roof, outer walls, and central spine with photo-informed geometry.
- Previously derived a repaired solver surface using union and junction repair. That surface is now explicitly historical; current wings require a new state-specific export and union.
- Added studio lighting/cameras, project renders, validation reports, checkpoint handling, and a resource-bounded OpenFOAM workflow.

The current images and animation were rendered from the inspected native model on 18 October 2026. Public PNG copies remove text metadata only, preserving every pixel-bearing chunk. The GIF encodes actual native render frames. Model-derived media retain CC BY 4.0. Earlier images still present in Git history describe previous geometry, not current CFD acceptance.

## Real-car references and rights

The real RB19 is a Red Bull Racing car. This project does not claim ownership of its design, team CAD, livery, trademarks, or sponsor marks. Those rights remain with their respective owners. This independent educational portfolio does not imply affiliation or endorsement.

Third-party reference photographs were consulted locally and are not included. [Engineering notes](docs/engineering.md#reference-links) link to the publishers and credit the photographers. Unseen geometry and section thicknesses are assumptions; the model is not an exact or aerodynamically validated reconstruction of the real car.


### Underbody reconstruction, 18 October 2026

Phoom Kharawat and OpenAI Codex co-designed and developed a continuous
photo-informed floor/diffuser, six internal inlet fences, two floor-edge blades,
sidepod undercut/waist refinements, bounded lower-skin joins, native geometric
passage checks and an independently checked underbody-only STL union. Original
UVs and wing/DRS geometry are retained. Monaco, Spain and Hungary photographs
inform an explicitly mixed 2023 reconstruction with assumed dimensions. The
base model remains Redgrund's CC BY 4.0 work; Red Bull Racing designed the real
car. This attribution does not claim original authorship of either.

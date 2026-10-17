# Status and evidence boundaries

Snapshot: **18 October 2026**, a saved status rather than a live monitor.

## Continuous floor, diffuser and sidepod undercut

The current native file has a reconstructed continuous underfloor/diffuser,
six swept internal inlet vanes, two floor-edge blades and a deeper sidepod
undercut. A common displacement field preserves UV continuity across source
mesh islands. Newly cut lower-skin boundary vertices were joined to the new
floor within a bounded 65 mm search, with 1 mm penetration for subsequent union.
This is a new reconstruction, not a small-tolerance comparison to team CAD.

Nine new components pass watertightness, winding, positive-volume, degenerate-face
and self-intersection checks. Their union has 182,488 triangles and passes
OpenFOAM surfaceCheck for closure, illegal triangles and self-intersections.
Boolean-generated tiny triangles were cleaned with a 10 micrometre nominal
deviation setting; bidirectional vertex/centroid samples were below 30 micrometres.
This numerical cleanup is distinct from the larger intentional redesign.

Six native underfloor paths and two sidepod bypass paths do not intersect the
checked car triangles. Their smallest sampled solid distance is 25.56 mm.
The new floor does not cross the checked wheels, suspension or brake fins.
Packed textures and 16 DRS positions were checked after the body edits.
The floor-only acceptance does not validate the remaining artist-model shell,
body/wing transitions, volume mesh or aerodynamic solution.

[Reference assumptions](underbody-references.md) and
[current underbody evidence](../evidence/underbody-summary.json) describe the
mixed 2023 interpretation and exact native-file identity. Prior wing evidence
remains scoped to the unchanged wing components.

## Photo-informed wings and working DRS

The reconstruction uses four front-wing elements per side, a spoon-shaped rear mainplane, rolled outer tips, a separate moving flap, adapted lower endplates/swan-neck and two beam-wing elements. BYBIT faces forward/top with a gold I, and ORACLE faces rearward. Photographs guided layout and silhouette; they do not establish calibrated profiles, exact race trim, dimensions or hinge geometry.

The native file was reopened and checked independently. Fourteen new lofts have closed, consistently wound surfaces, positive volume, no zero-area faces and no self-intersection pairs. The initial rolled-tip audit exposed a folded coordinate mapping; the radial offset was corrected and the final geometry passed the same audit.

DRS rotates the flap approximately **18.545 degrees** about one fixed spanwise hinge. Sixteen sampled animation states returned to the same closed geometry, left fixed wing bodies stationary and showed no moving-flap crossings with the checked fixed bodies. Thirty-nine rear span sections per state gave **17.08–22.04 mm closed** and **66.38–81.99 mm open**. Fifty-four front sections found no adjacent-foil overlap and a sampled minimum slot of **7.18 mm**. These are discrete checks, not continuous/global clearance or complete FIA compliance proof.

## CFD surface and mesh

Retained body/floor joins, front nose/tip transition cuts and lower rear endplates need a fresh whole-car CFD export and union/repair for the selected DRS state. Passing individual new components does not establish a closed whole-car fluid boundary.

The previous **2,114,416-triangle** accepted surface belongs to the preceding wing revision. It remains historical inside the native project and is omitted from new exports. The **3,154,323-cell volume checkpoint** is older still. Neither is current acceptance evidence, and the old mesh must not be resumed against these wings.

No accepted volume mesh, solver run, pressure field, velocity field or validated drag/downforce coefficient exists for the current reconstruction. Previous memory-limited meshing attempts remain historical evidence only.

## Next acceptance gates

1. Select closed or open DRS and export that exact evaluated native state.
2. Repair/union retained transitions while preserving wing slots; verify the whole surface independently and with OpenFOAM.
3. Build fresh geometry identities, slot refinement boxes and a volume mesh under finite resource limits.
4. Inspect mesh quality, layers and actual passage resolution before the 50 m/s moving-ground/rotating-wheel case.
5. Assess residuals, mass conservation, force stability, near-wall resolution and mesh sensitivity.

The assumed 1.5 m² reference area is a comparison convention. Model renders and motion checks do not establish real-car aerodynamic performance.

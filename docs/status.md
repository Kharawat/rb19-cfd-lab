# Status and evidence boundaries

Snapshot: **18 October 2026**, a saved status rather than a live monitor.

## Photo-informed wings and working DRS

The reconstruction uses four front-wing elements per side, a spoon-shaped rear mainplane, rolled outer tips, a separate moving flap, adapted lower endplates/swan-neck and two beam-wing elements. BYBIT faces forward/top with a gold I, and ORACLE faces rearward. Photographs guided layout and silhouette; they do not establish calibrated profiles, exact race trim, dimensions or hinge geometry.

The native file was reopened and checked independently. Fourteen new lofts have closed, consistently wound surfaces, positive volume, no zero-area faces and no self-intersection pairs. The initial rolled-tip audit exposed a folded coordinate mapping; the radial offset was corrected and the final geometry passed the same audit.

DRS rotates the flap approximately **18.545 degrees** about one fixed spanwise hinge. Sixteen sampled animation states returned to the same closed geometry, left fixed wing bodies stationary and showed no moving-flap crossings with the checked fixed bodies. Thirty-nine rear span sections per state gave **17.08–22.04 mm closed** and **66.38–81.99 mm open**. Fifty-four front sections found no adjacent-foil overlap and a sampled minimum slot of **7.18 mm**. These are discrete checks, not continuous/global clearance or complete FIA compliance proof.

## CFD surface and mesh

Retained front nose/tip transition cuts and lower rear endplates need a fresh CFD export and union/repair for the selected DRS state. Passing individual new components does not establish a closed whole-car fluid boundary.

The previous **2,114,416-triangle** accepted surface belongs to the preceding wing revision. It remains historical inside the native project and is omitted from new exports. The **3,154,323-cell volume checkpoint** is older still. Neither is current acceptance evidence, and the old mesh must not be resumed against these wings.

No accepted volume mesh, solver run, pressure field, velocity field or validated drag/downforce coefficient exists for the current reconstruction. Previous memory-limited meshing attempts remain historical evidence only.

## Next acceptance gates

1. Select closed or open DRS and export that exact evaluated native state.
2. Repair/union retained transitions while preserving wing slots; verify the whole surface independently and with OpenFOAM.
3. Build fresh geometry identities, slot refinement boxes and a volume mesh under finite resource limits.
4. Inspect mesh quality, layers and actual passage resolution before the 50 m/s moving-ground/rotating-wheel case.
5. Assess residuals, mass conservation, force stability, near-wall resolution and mesh sensitivity.

The assumed 1.5 m² reference area is a comparison convention. Model renders and motion checks do not establish real-car aerodynamic performance.

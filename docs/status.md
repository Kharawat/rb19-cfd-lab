# Status and evidence boundaries

Snapshot: **17 October 2026**. This is a saved project status, not a live monitor.

## Rear-wing correction delivered

The earlier central flap chord was about 75.8 degrees from horizontal. The new central target is 45 degrees, easing to about 42 degrees outboard. The mainplane chord, rolled junctions and upper support were reshaped together; the upper trailing edge stays near X=5.280 m. These are modeling choices informed by public photographs, not measured team CAD or a verified race trim.

The visible and embedded CFD rear wing received the same continuous shape map. Independent checks found a closed, consistently wound surface with zero crossing/touching pairs and no holes. OpenFOAM initially flagged five numerical contacts on unchanged body areas; a bounded adjustment moved 35 body vertices by at most **0.010005 mm**. OpenFOAM then reported a closed surface, no illegal triangles and no self-intersections. Surface connectivity and patch labels stayed unchanged.

The final surface has **2,114,416 triangles, 1,054,066 welded vertices and 7 named patches**. Twelve rear-slot sections and 372 interior points passed, with sampled gaps of **6.364–15.598 mm**. Finite probes do not prove a full-span minimum or adequate fluid-mesh resolution. The final native file was reopened and all embedded CFD triangle buffers matched the checked arrays; textures remain packed.

## Volume mesh and solver

The **3,154,323-cell checkpoint belongs to the previous wing**. Preserve it as historical evidence; do not resume it against the new geometry. A short mesher attempt just after midnight was intentionally stopped for this correction and its owned process group is empty. No final volume mesh or flow solution exists for the corrected wing.

On the previous geometry, the 16 October 15:27–17:06 attempt reached 4,892,045 cells in RAM and later 3,382,439 after subsetting. Neither state was saved. The host RAM guard stopped it; the 23:35 audit confirmed the older saved checkpoint was intact. Those figures are historical, not results of the revised wing.

## Next acceptance gates

1. Build a new geometry contract and remeasure slot refinement boxes using the new surface identity.
2. Generate a fresh volume mesh under finite resource limits and live host-memory protection.
3. Check final topology, quality, layer coverage and actual narrow-passage resolution.
4. Run the 50 m/s moving-ground/rotating-wheel case only after the mesh passes.
5. Assess residuals, mass conservation, force stability, near-wall resolution and mesh sensitivity.

There are **no validated drag/downforce coefficients, pressure fields or velocity fields**. A surface check and a model render do not establish aerodynamic performance. The assumed 1.5 m² reference area remains a comparison convention.

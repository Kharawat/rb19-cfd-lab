# Status and evidence boundaries

Snapshot date: **16 October 2026**. This file records a project status, not a live job monitor.

## Confirmed

- The detailed geometry and the three included studio renders already exist.
- The recorded final repaired-surface audit passed: closed/watertight, consistent winding, zero reported self-intersections, 2,114,416 triangles and 7 named patches.
- The recorded native Blender validation reopened the saved project and checked identities, patch counts, units, packed textures, and camera setup.
- A native mesh checkpoint containing **3,154,323 cells** was previously saved and verified.
- A later meshing pass reached **4,498,036 cells in RAM**. The post-stop audit confirms that this larger state was not written as a new checkpoint.
- The post-stop audit passed at **15:23:48 Bangkok time on 16 October 2026**: live saved checkpoint hashes match the immutable 3,154,323-cell snapshot, and the canonical `0` state is unchanged. This fresh audit checked mesh files and small inputs. Full geometry identity remains a separate pre-run gate; the large geometry was not freshly rehashed by this audit.

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
2. Resume only from that accepted saved state, with the full geometry/input identity checks and finite resource limits intact.
3. Complete mesh stages and inspect topology, quality, layer coverage, and critical slot passages.
4. Start the flow solver only after the mesh gate passes.
5. Assess residuals, conservation, force stability, near-wall resolution, and mesh sensitivity before interpreting coefficients.

The case's 50 m/s inlet, moving ground, rotating wheels, and assumed 1.5 m² reference area describe the intended setup. They do not imply that a production flow solution has been obtained.

Compact source-derived records are in [evidence/](../evidence/README.md). Large native checkpoints and full local logs are intentionally absent from the public snapshot.

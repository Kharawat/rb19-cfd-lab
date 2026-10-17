# RB19 underbody reconstruction references — 18 October 2026

This study uses real 2023 photographs. It combines Monaco underfloor exposure,
Spain diffuser details and Hungary sidepod views; it is **not a replica of one
verified race specification**. No team CAD, measured sections or scanner data was
available. Photographs stay local as reference material and are not republished
with the portfolio.

| Local reference | Observed source | Use |
|---|---|---|
| monaco-underfloor.jpg | [RB19 discussion with actual crane photograph](https://www.f1technical.net/forum/viewtopic.php?p=1135968); original photographer not established | Broad tunnel roofs, centre keel, underside planform; damaged car, perspective limits |
| monaco-underside-rear.jpg | [Motorsport: exposed RB19 floor](https://www.motorsport.com/f1/news/red-bull-f1-car-floor-exposed-williams/10482802/) | Floor length and transition into diffuser; photo acquired at the observed Motorsport CDN URL |
| spain-diffuser-closeup.jpg | [Giorgio Piola / Motorsport, 2 June 2023](https://it.motorsport.com/f1/news/f1-red-bull-beam-wing-e-fondo-in-continua-evoluzione/10477046/) | Roof arch, rolled outer corner and relation to rear light/beam wing |
| rear-diffuser-mouth.jpg | [Autosport technical photographs](https://www.autosport.com/f1/news/the-best-tech-images-so-far-from-formula-1-2023/10471204/) | Open mouth, sidewall depth and tyre packaging |
| hungary-sidepod-inlet.jpg | [Autosport Hungary update, 21 July 2023](https://www.autosport.com/f1/news/red-bull-makes-five-key-changes-for-f1s-hungarian-gp/10497984/) | Inlet lip, visible undercut and floor shoulder |
| hungary-sidepod-undercut.jpg | [Motorsport Hungary sidepod photographs](https://es.motorsport.com/f1/news/cambios-pontones-red-bull-nuevos/10498120/) | Shoulder-to-coke-bottle contour and space above the floor |

Additional public introductory material:

- [Formula 1: RB19 floor, 13 June 2023](https://www.formula1.com/en/latest/article/tech-tuesday-the-secrets-behind-red-bulls-floor-design-and-how-it-differs-to.6J1SkUEvGWomlO9BJilUK4).
- [Formula 1: Hungary bodywork, 25 July 2023](https://www.formula1.com/en/latest/article/tech-tuesday-analysing-red-bulls-significant-bodywork-upgrade-brought-to.ksCBb342Gi6eW7FNyRrJb).
- [Formula 1: underfloor details, 14 November 2023](https://www.formula1.com/en/latest/article/tech-tuesday-the-technological-gift-that-keeps-on-giving-more-design-genius.2TkOtSyhf8cvMVb0LMFC8X).

Only publicly visible introductory text was used from sign-in-gated articles.

## Reconstruction decisions

- Replace the previous aft-only roof with a continuous inlet-to-throat-to-exit
  floor, shaped centre keel and integrated curved diffuser sidewalls.
- Use a smooth local rise to represent the photographed stepped diffuser roof;
  round the roof/wall transition and narrow the wall around the existing brake
  fins, preserving the wheels and suspension.
- Use three internal swept inlet fences per side with the original decorated
  outer fence, plus two floor-edge blades.
- Deepen the sidepod undercut with a smooth displacement field across all
  affected source mesh islands; retain UVs, BYBIT and the DRS system.
- Set nominal roof material thickness to 8 mm for a robust closed operand.
  This is a modeling choice, not a measured carbon laminate thickness.
- Keep original wheel positions and native ride-height origin. Exact race
  ride heights, rake, cooling ducts, hidden structure and boundary-layer setup
  remain unmeasured and require case-specific decisions before CFD.

## Evidence boundaries

Triangle closure, geometric passages and an underbody-only surfaceCheck do not
show fluid attachment, low turbulence, downforce or drag. No simulated streamlines
are drawn in the renderings. Full-car surface repair, a fresh volume mesh and
validated solver results remain required. Earlier mesh checkpoints are obsolete.

The original model is by Redgrund, CC BY 4.0. Phoom and OpenAI Codex co-designed
and developed these project modifications and validation. Red Bull Racing
designed the actual RB19.

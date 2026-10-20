"""Generate light/dark README hero banners for each product repository.

Usage: py -3.12 tools/make_banners.py <portfolio-root>
Writes <root>/<repo>/docs/assets/banner-{light,dark}.svg
"""

from __future__ import annotations

import sys
from pathlib import Path

W, H = 1280, 360
FONT = "Inter, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"

PRODUCTS = {
    "hr-policy-copilot": {
        "title": "HR Policy Copilot",
        "tagline": ["Ask HR policy questions.", "Get answers you can verify."],
        "chips": ["Hybrid RAG", "Versioned sources", "Exact citations"],
        "accent": "#0D9488",
        "accent2": "#5EEAD4",
        "motif": "documents",
    },
    "hiring-process-miner": {
        "title": "Hiring Process Miner",
        "tagline": ["Understand how hiring actually happens —", "from event logs to explainable insights."],
        "chips": ["Process discovery", "Bottlenecks", "Conformance"],
        "accent": "#7C3AED",
        "accent2": "#C4B5FD",
        "motif": "flow",
    },
    "workforce-optimizer": {
        "title": "Workforce Optimizer",
        "tagline": ["Constraint-based scheduling that", "explains every shift assignment."],
        "chips": ["OR-Tools CP-SAT", "Independent validator", "Explainable"],
        "accent": "#D97706",
        "accent2": "#FCD34D",
        "motif": "roster",
    },
    "fairhire-audit": {
        "title": "FairHire Audit",
        "tagline": ["Audit the model. Understand the trade-offs.", "Show your evidence."],
        "chips": ["Group metrics", "Confidence intervals", "Threshold lab"],
        "accent": "#2563EB",
        "accent2": "#93C5FD",
        "motif": "bars",
    },
    "skillgraph": {
        "title": "SkillGraph",
        "tagline": ["Map what you know.", "Discover where your skills can take you."],
        "chips": ["Knowledge graph", "Explainable paths", "Gap analysis"],
        "accent": "#C026D3",
        "accent2": "#F0ABFC",
        "motif": "graph",
    },
}

THEMES = {
    "light": {"bg1": "#FFFFFF", "bg2": "#F6F8FA", "fg": "#0F172A", "muted": "#475569", "line": "#E2E8F0", "card": "#FFFFFF"},
    "dark": {"bg1": "#0B1020", "bg2": "#111827", "fg": "#F8FAFC", "muted": "#94A3B8", "line": "#1F2937", "card": "#161E2E"},
}


def motif_documents(a: str, a2: str, t: dict) -> str:
    out = []
    for i, (dx, dy) in enumerate([(0, 30), (26, 14), (52, 0)]):
        x, y = 880 + dx, 70 + dy
        out.append(f'<rect x="{x}" y="{y}" width="230" height="250" rx="14" fill="{t["card"]}" stroke="{t["line"]}" stroke-width="2"/>')
        if i == 2:
            for j in range(7):
                w = [170, 140, 180, 120, 160, 100, 150][j]
                yy = y + 40 + j * 26
                fill = a if j == 3 else t["line"]
                op = "0.9" if j == 3 else "1"
                out.append(f'<rect x="{x + 28}" y="{yy}" width="{w}" height="10" rx="5" fill="{fill}" opacity="{op}"/>')
            out.append(f'<rect x="{x + 20}" y="{y + 108}" width="190" height="26" rx="6" fill="none" stroke="{a}" stroke-width="2.5"/>')
    out.append(f'<g transform="translate(1110 250)"><rect x="0" y="0" width="74" height="40" rx="20" fill="{a}"/>'
               f'<text x="37" y="27" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="700" fill="#FFFFFF">[1]</text></g>')
    out.append(f'<path d="M1110 270 C1080 270 1075 220 1062 206" fill="none" stroke="{a}" stroke-width="2.5" stroke-dasharray="5 5"/>')
    return "\n".join(out)


def motif_flow(a: str, a2: str, t: dict) -> str:
    nodes = [(880, 110), (980, 70), (980, 190), (1090, 130), (1190, 90), (1190, 240)]
    edges = [(0, 1, 6), (0, 2, 3), (1, 3, 5), (2, 3, 2), (3, 4, 4), (3, 5, 3), (2, 5, 1.5)]
    out = []
    for s, e, w in edges:
        (x1, y1), (x2, y2) = nodes[s], nodes[e]
        cx = (x1 + x2) / 2
        out.append(f'<path d="M{x1} {y1} C{cx} {y1} {cx} {y2} {x2} {y2}" fill="none" stroke="{a}" stroke-opacity="0.55" stroke-width="{w}"/>')
    for i, (x, y) in enumerate(nodes):
        hot = i == 3
        out.append(f'<circle cx="{x}" cy="{y}" r="{26 if hot else 20}" fill="{t["card"]}" stroke="{"#EF4444" if hot else a}" stroke-width="{4 if hot else 3}"/>')
        out.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{"#EF4444" if hot else a}"/>')
    out.append(f'<g transform="translate(1040 290)"><rect width="150" height="34" rx="17" fill="#EF4444" opacity="0.12"/>'
               f'<text x="75" y="23" text-anchor="middle" font-family="{FONT}" font-size="16" font-weight="600" fill="#EF4444">p90 wait ↑</text></g>')
    return "\n".join(out)


def motif_roster(a: str, a2: str, t: dict) -> str:
    out = []
    x0, y0, cw, rh = 870, 60, 50, 40
    for c in range(7):
        out.append(f'<rect x="{x0 + c * cw}" y="{y0}" width="{cw - 6}" height="{rh * 6 + 4}" rx="8" fill="{t["card"]}" stroke="{t["line"]}" stroke-width="1.5"/>')
    blocks = [(0, 0, 2), (1, 1, 2), (2, 0, 1), (3, 2, 3), (4, 1, 2), (5, 3, 2), (6, 0, 2), (0, 3, 2), (2, 2, 3), (4, 4, 2), (1, 4, 1), (6, 3, 2)]
    for i, (c, r, span) in enumerate(blocks):
        fill = a if i % 3 else a2
        out.append(f'<rect x="{x0 + c * cw + 5}" y="{y0 + 6 + r * rh}" width="{cw - 16}" height="{span * rh - 8}" rx="6" fill="{fill}" opacity="0.9"/>')
    out.append(f'<g transform="translate(1150 250)"><circle r="30" fill="#16A34A"/>'
               f'<path d="M-13 1 L-4 10 L14 -9" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></g>')
    return "\n".join(out)


def motif_bars(a: str, a2: str, t: dict) -> str:
    out = []
    base = 300
    out.append(f'<line x1="870" y1="{base}" x2="1220" y2="{base}" stroke="{t["line"]}" stroke-width="2"/>')
    groups = [(150, 120), (180, 95), (130, 150), (165, 110)]
    for g, (h1, h2) in enumerate(groups):
        x = 890 + g * 85
        for k, (h, col) in enumerate([(h1, a), (h2, a2)]):
            bx = x + k * 30
            out.append(f'<rect x="{bx}" y="{base - h}" width="24" height="{h}" rx="5" fill="{col}"/>')
            out.append(f'<line x1="{bx + 12}" y1="{base - h - 18}" x2="{bx + 12}" y2="{base - h + 14}" stroke="{t["fg"]}" stroke-width="2" opacity="0.6"/>')
            out.append(f'<line x1="{bx + 6}" y1="{base - h - 18}" x2="{bx + 18}" y2="{base - h - 18}" stroke="{t["fg"]}" stroke-width="2" opacity="0.6"/>')
    out.append(f'<line x1="870" y1="{base - 140}" x2="1220" y2="{base - 140}" stroke="{a}" stroke-width="2" stroke-dasharray="8 6"/>')
    return "\n".join(out)


def motif_graph(a: str, a2: str, t: dict) -> str:
    nodes = [(900, 180), (980, 90), (990, 260), (1070, 170), (1150, 80), (1160, 270), (1210, 175), (1060, 300), (1080, 60)]
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (3, 5), (4, 6), (5, 6), (2, 7), (1, 8), (8, 4), (7, 5)]
    path = {(0, 1), (1, 3), (3, 4), (4, 6)}
    out = []
    for s, e in edges:
        (x1, y1), (x2, y2) = nodes[s], nodes[e]
        on = (s, e) in path
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{a if on else t["muted"]}" stroke-opacity="{1 if on else 0.35}" stroke-width="{4 if on else 2}"/>')
    on_nodes = {0, 1, 3, 4, 6}
    for i, (x, y) in enumerate(nodes):
        on = i in on_nodes
        r = 18 if on else 12
        out.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{a if on else t["card"]}" stroke="{a if on else t["muted"]}" stroke-width="2.5"/>')
    out.append(f'<circle cx="1210" cy="175" r="28" fill="none" stroke="{a2}" stroke-width="3"/>')
    return "\n".join(out)


MOTIFS = {"documents": motif_documents, "flow": motif_flow, "roster": motif_roster, "bars": motif_bars, "graph": motif_graph}


def banner(p: dict, theme: str) -> str:
    t = THEMES[theme]
    a, a2 = p["accent"], p["accent2"]
    glow_op = "0.22" if theme == "dark" else "0.12"
    chips, cx = [], 80
    for c in p["chips"]:
        w = 22 + len(c) * 10
        chips.append(f'<rect x="{cx}" y="268" width="{w}" height="36" rx="18" fill="{a}" fill-opacity="0.12" stroke="{a}" stroke-opacity="0.45"/>'
                     f'<text x="{cx + w / 2}" y="292" text-anchor="middle" font-family="{FONT}" font-size="16" font-weight="600" fill="{a if theme == "light" else a2}">{c}</text>')
        cx += w + 12
    tag = "".join(
        f'<text x="80" y="{186 + i * 36}" font-family="{FONT}" font-size="28" fill="{t["muted"]}">{line}</text>'
        for i, line in enumerate(p["tagline"])
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{p["title"]}: {" ".join(p["tagline"])}">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{t["bg1"]}"/><stop offset="1" stop-color="{t["bg2"]}"/></linearGradient>
<radialGradient id="glow" cx="0.8" cy="0.4" r="0.6"><stop offset="0" stop-color="{a}" stop-opacity="{glow_op}"/><stop offset="1" stop-color="{a}" stop-opacity="0"/></radialGradient>
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{t["line"]}" stroke-width="1" opacity="0.6"/></pattern>
</defs>
<rect width="{W}" height="{H}" rx="24" fill="url(#bg)"/>
<rect width="{W}" height="{H}" rx="24" fill="url(#grid)" opacity="0.5"/>
<rect width="{W}" height="{H}" rx="24" fill="url(#glow)"/>
<rect x="0.75" y="0.75" width="{W - 1.5}" height="{H - 1.5}" rx="23.5" fill="none" stroke="{t["line"]}" stroke-width="1.5"/>
<rect x="80" y="62" width="44" height="6" rx="3" fill="{a}"/>
<text x="80" y="128" font-family="{FONT}" font-size="60" font-weight="800" letter-spacing="-1.5" fill="{t["fg"]}">{p["title"]}</text>
{tag}
{"".join(chips)}
{MOTIFS[p["motif"]](a, a2, t)}
</svg>
'''


def main() -> None:
    root = Path(sys.argv[1])
    for repo, p in PRODUCTS.items():
        out = root / repo / "docs" / "assets"
        out.mkdir(parents=True, exist_ok=True)
        for theme in THEMES:
            (out / f"banner-{theme}.svg").write_text(banner(p, theme), encoding="utf-8")
        print(f"{repo}: wrote banner-light.svg, banner-dark.svg")


if __name__ == "__main__":
    main()

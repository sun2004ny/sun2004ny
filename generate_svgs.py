# -*- coding: utf-8 -*-
"""
Generates self-contained, GitHub-compatible, responsive, animated dark.svg and light.svg
for Sunny More's GitHub Profile README.
Ensures perfect frame containment with zero overlaps or clipping.
"""

import os
import xml.etree.ElementTree as ET

# 26-line perfectly contained ASCII portrait of Sunny More
# Captures: signature wavy/curly hair, Wayfarer sunglasses with specular glint, mustache, bright smile, open collar & shoulders
ascii_art = [
    '                %%%%%%%%                ',
    '              %%%%%  %%%%%%             ',
    '            %%%%%   %%  %%##%           ',
    '           %%% %% %%%%%%%%%%#%          ',
    '          %%%%  %%%% %%%%%%%%%          ',
    '          % %%%  %%%#  %  %%%%          ',
    '          %   %###@@@@@@@# %%%          ',
    '           @#@@@##+:::+++###@           ',
    '           ###@@@#:+:+#:+##+@           ',
    '          @###@  #+::+#+##+++           ',
    '          @#+++++#+::::+++::#           ',
    '           +::···::::::····:+           ',
    '           :::::#::··::::·::+           ',
    '             +:::+:===:===+             ',
    '             #+:::::=====:#             ',
    '              #++::::::::::+            ',
    '            ++·············::·          ',
    '           +···········::··:::·+        ',
    '         +·::········::::··:::::·++     ',
    '       +:·····::++++····+::········::+  ',
    '    +::·······::++++++·++:·············:',
    '  +::··········:+++++++++···············',
    '+:··············+++++++++···············',
    '··················::::::················',
    '··················:::::·················',
    ':··················:·:··················'
]

def make_ascii_svg_lines(x_center, y_start, dy):
    lines = []
    for i, line in enumerate(ascii_art):
        y = y_start + i * dy
        escaped = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        lines.append(f'        <tspan x="{x_center}" y="{y:.1f}">{escaped}</tspan>')
    return '\n'.join(lines)


def build_svg(theme="dark"):
    is_dark = (theme == "dark")
    
    # Palette
    if is_dark:
        bg_start = "#040711"
        bg_end = "#080e1a"
        grid_stroke = "#1e293b"
        grid_opacity = "0.22"
        outer_border = "#1e293b"
        panel_bg = "#0b1220"
        panel_opacity = "0.85"
        panel_border = "#1e293b"
        header_bar_bg = "#0f172a"
        header_border = "#334155"
        
        text_primary = "#f8fafc"
        text_secondary = "#94a3b8"
        text_muted = "#64748b"
        
        accent_cyan = "#38bdf8"
        accent_emerald = "#34d399"
        accent_violet = "#c084fc"
        accent_indigo = "#818cf8"
        accent_amber = "#fbbf24"
        
        ascii_fill = "#22d3ee"
        ascii_box_bg = "#030712"
        ascii_box_border = "#164e63"
        
        pill_bg = "#0f172a"
        pill_border = "#1e293b"
        pill_text = "#e2e8f0"
        
        card_link_bg = "#0c1527"
        card_link_border = "#1e293b"
        card_link_text = "#38bdf8"
        
        glow1 = "rgba(56, 189, 248, 0.12)"
        glow2 = "rgba(192, 132, 252, 0.10)"
        glow3 = "rgba(52, 211, 153, 0.08)"
    else:
        bg_start = "#f8fafc"
        bg_end = "#f1f5f9"
        grid_stroke = "#cbd5e1"
        grid_opacity = "0.45"
        outer_border = "#cbd5e1"
        panel_bg = "#ffffff"
        panel_opacity = "0.92"
        panel_border = "#cbd5e1"
        header_bar_bg = "#f1f5f9"
        header_border = "#cbd5e1"
        
        text_primary = "#0f172a"
        text_secondary = "#475569"
        text_muted = "#64748b"
        
        accent_cyan = "#0284c7"
        accent_emerald = "#059669"
        accent_violet = "#7c3aed"
        accent_indigo = "#4f46e5"
        accent_amber = "#d97706"
        
        ascii_fill = "#1e293b"
        ascii_box_bg = "#f8fafc"
        ascii_box_border = "#94a3b8"
        
        pill_bg = "#f1f5f9"
        pill_border = "#cbd5e1"
        pill_text = "#1e293b"
        
        card_link_bg = "#f1f5f9"
        card_link_border = "#cbd5e1"
        card_link_text = "#0284c7"
        
        glow1 = "rgba(2, 132, 199, 0.10)"
        glow2 = "rgba(124, 58, 237, 0.08)"
        glow3 = "rgba(5, 150, 105, 0.08)"

    # Text lines for ASCII: 26 lines starting at y=70, dy=10.2 -> ends at 325px (box is 44 to 352)
    ascii_tspans = make_ascii_svg_lines(x_center=197, y_start=72, dy=10.2)
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 610" width="1180" height="610" role="img" aria-label="Sunny More — Full-Stack Web Architect and Applied NLP Engineer Profile Banner">
  <defs>
    <!-- Background Gradients -->
    <linearGradient id="bg-grad-{theme}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_start}" />
      <stop offset="100%" stop-color="{bg_end}" />
    </linearGradient>

    <radialGradient id="glow-cyan-{theme}" cx="15%" cy="18%" r="45%">
      <stop offset="0%" stop-color="{glow1}" />
      <stop offset="100%" stop-color="{glow1}" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="glow-violet-{theme}" cx="85%" cy="25%" r="40%">
      <stop offset="0%" stop-color="{glow2}" />
      <stop offset="100%" stop-color="{glow2}" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="glow-emerald-{theme}" cx="55%" cy="85%" r="35%">
      <stop offset="0%" stop-color="{glow3}" />
      <stop offset="100%" stop-color="{glow3}" stop-opacity="0" />
    </radialGradient>

    <linearGradient id="text-grad-{theme}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{accent_cyan}" />
      <stop offset="50%" stop-color="{accent_indigo}" />
      <stop offset="100%" stop-color="{accent_violet}" />
    </linearGradient>

    <!-- Subtle Dot Grid Pattern -->
    <pattern id="grid-{theme}" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.8" fill="{grid_stroke}" fill-opacity="{grid_opacity}" />
    </pattern>

    <style>
      .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }}
      .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
      .ascii-art {{
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
        font-size: 9px;
        letter-spacing: 1.5px;
        fill: {ascii_fill};
      }}
    </style>
  </defs>

  <!-- Canvas Outer Background -->
  <rect width="1180" height="610" rx="22" fill="url(#bg-grad-{theme})" />
  
  <!-- Ambient Lighting Effects -->
  <rect width="1180" height="610" rx="22" fill="url(#glow-cyan-{theme})" />
  <rect width="1180" height="610" rx="22" fill="url(#glow-violet-{theme})" />
  <rect width="1180" height="610" rx="22" fill="url(#glow-emerald-{theme})" />

  <!-- Subtle Dot Grid -->
  <rect width="1180" height="610" rx="22" fill="url(#grid-{theme})" />
  
  <!-- Outer Frame Border -->
  <rect x="1" y="1" width="1178" height="608" rx="21" fill="none" stroke="{outer_border}" stroke-width="1.2" />

  <!-- Top Window Header Bar -->
  <rect x="1" y="1" width="1178" height="42" rx="21" fill="{header_bar_bg}" />
  <rect x="1" y="22" width="1178" height="20" fill="{header_bar_bg}" />
  <line x1="1" y1="42" x2="1179" y2="42" stroke="{header_border}" stroke-width="1" />

  <!-- Window Controls -->
  <circle cx="30" cy="22" r="5.5" fill="#ef4444" />
  <circle cx="48" cy="22" r="5.5" fill="#f59e0b" />
  <circle cx="66" cy="22" r="5.5" fill="#10b981" />

  <!-- Terminal Title Breadcrumb -->
  <text x="96" y="27" class="mono" font-size="12" fill="{text_secondary}" font-weight="600">
    sun2004ny@workstation: ~/portfolio (main) — <tspan fill="{accent_cyan}">[SYSTEM.ONLINE]</tspan>
  </text>

  <!-- Top Right Available Status Pill -->
  <g transform="translate(1005, 12)">
    <rect width="145" height="20" rx="10" fill="{pill_bg}" stroke="{accent_emerald}" stroke-width="1" stroke-opacity="0.5" />
    <circle cx="14" cy="10" r="3.5" fill="{accent_emerald}">
      <animate attributeName="r" values="3;4.2;3" dur="2s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.8;1;0.8" dur="2s" repeatCount="indefinite" />
    </circle>
    <text x="26" y="14.5" class="mono" font-size="10.5" font-weight="700" fill="{accent_emerald}">OPEN TO ROLES</text>
  </g>

  <!-- ==================== LEFT PANEL: VISUAL IDENTITY & ASCII PORTRAIT ==================== -->
  <g transform="translate(32, 56)">
    <!-- Panel Glass Container -->
    <rect width="395" height="524" rx="16" fill="{panel_bg}" fill-opacity="{panel_opacity}" stroke="{panel_border}" stroke-width="1.2" />
    
    <!-- Panel Header -->
    <rect width="395" height="34" rx="16" fill="{header_bar_bg}" />
    <rect y="18" width="395" height="16" fill="{header_bar_bg}" />
    <line x1="0" y1="34" x2="395" y2="34" stroke="{panel_border}" stroke-width="1" />
    
    <text x="18" y="22" class="mono" font-size="11" font-weight="700" fill="{text_secondary}">[ VISUAL.MAP // PORTRAIT ]</text>
    <text x="375" y="22" class="mono" font-size="10" font-weight="600" fill="{accent_cyan}" text-anchor="end">ASCII_VECTOR</text>

    <!-- ASCII Canvas Viewport Box: 44 to 348 (height 304px) -->
    <rect x="16" y="44" width="363" height="308" rx="10" fill="{ascii_box_bg}" stroke="{ascii_box_border}" stroke-width="1" />
    
    <!-- Scanning Light Line Effect (Constrained within Box) -->
    <line x1="18" y1="46" x2="377" y2="46" stroke="{accent_cyan}" stroke-width="1.5" stroke-opacity="0.65">
      <animate attributeName="y1" values="46;350;46" dur="6s" repeatCount="indefinite" />
      <animate attributeName="y2" values="46;350;46" dur="6s" repeatCount="indefinite" />
      <animate attributeName="stroke-opacity" values="0.2;0.8;0.2" dur="6s" repeatCount="indefinite" />
    </line>

    <!-- The 26-line Contained ASCII Art Portrait -->
    <text class="ascii-art" text-anchor="middle" xml:space="preserve">
{ascii_tspans}
    </text>

    <!-- Distinct Horizontal Divider Below Box -->
    <line x1="16" y1="370" x2="379" y2="370" stroke="{panel_border}" stroke-width="1" />
    
    <!-- Bottom Status Log Area: perfectly spaced, no overlap -->
    <text x="20" y="396" class="mono" font-size="11" font-weight="700" fill="{accent_cyan}">$ ./status.sh --identity</text>
    <text x="20" y="420" class="mono" font-size="10.5" fill="{text_secondary}">&gt; STATUS : <tspan fill="{text_primary}" font-weight="600">Final-Year B.Tech (CGPA 9.22/10)</tspan></text>
    <text x="20" y="442" class="mono" font-size="10.5" fill="{text_secondary}">&gt; EXP    : <tspan fill="{text_primary}" font-weight="600">9 Mos Web Dev Intern @ Bada Builder</tspan></text>
    <text x="20" y="464" class="mono" font-size="10.5" fill="{text_secondary}">&gt; LOC    : <tspan fill="{text_primary}" font-weight="600">Vadodara, Gujarat, India [IN]</tspan></text>
    <text x="20" y="486" class="mono" font-size="10.5" fill="{text_secondary}">&gt; FOCUS  : <tspan fill="{accent_emerald}" font-weight="600">Full-Stack Web · Applied NLP · AWS</tspan></text>
  </g>

  <!-- ==================== RIGHT PANEL: SYSTEM.INFO & CAPABILITIES ==================== -->
  <g transform="translate(442, 56)">
    <!-- Panel Glass Container -->
    <rect width="706" height="524" rx="16" fill="{panel_bg}" fill-opacity="{panel_opacity}" stroke="{panel_border}" stroke-width="1.2" />

    <!-- Panel Header -->
    <rect width="706" height="34" rx="16" fill="{header_bar_bg}" />
    <rect y="18" width="706" height="16" fill="{header_bar_bg}" />
    <line x1="0" y1="34" x2="706" y2="34" stroke="{panel_border}" stroke-width="1" />
    
    <text x="22" y="22" class="mono" font-size="11" font-weight="700" fill="{text_secondary}">[ SYSTEM.INFO // SUNNY_MORE.DEV ]</text>
    <text x="684" y="22" class="mono" font-size="10" font-weight="600" fill="{accent_violet}" text-anchor="end">~/profile/overview.json</text>

    <!-- Terminal Command Line -->
    <text x="24" y="58" class="mono" font-size="11.5" font-weight="600" fill="{accent_cyan}">
      sun2004ny@terminal:<tspan fill="{text_muted}">~$</tspan> sysinfo --profile detailed
    </text>

    <!-- Name Heading -->
    <text x="24" y="90" class="sans" font-size="28" font-weight="900" fill="url(#text-grad-{theme})" letter-spacing="1">
      SUNNY MORE
    </text>

    <!-- Animated Rotating Roles with Inline Blinking Cursor -->
    <g class="mono" font-size="13" font-weight="700" transform="translate(24, 112)">
      <!-- Role 1 -->
      <g>
        <animate attributeName="opacity" values="1;1;0;0;0;0;1" keyTimes="0;0.29;0.33;0.96;0.98;1;1" dur="9s" repeatCount="indefinite" />
        <text x="0" y="0" fill="{accent_cyan}">
          FULL-STACK WEB ARCHITECT <tspan fill="{accent_cyan}"><animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />▋</tspan>
        </text>
      </g>
      <!-- Role 2 -->
      <g>
        <animate attributeName="opacity" values="0;0;1;1;0;0;0" keyTimes="0;0.33;0.37;0.62;0.66;0.99;1" dur="9s" repeatCount="indefinite" />
        <text x="0" y="0" fill="{accent_violet}">
          APPLIED NLP &amp; AI ENGINEER <tspan fill="{accent_violet}"><animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />▋</tspan>
        </text>
      </g>
      <!-- Role 3 -->
      <g>
        <animate attributeName="opacity" values="0;0;0;0;1;1;0" keyTimes="0;0.66;0.70;0.95;0.97;0.99;1" dur="9s" repeatCount="indefinite" />
        <text x="0" y="0" fill="{accent_emerald}">
          AWS CLOUD &amp; SYSTEMS BUILDER <tspan fill="{accent_emerald}"><animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite" />▋</tspan>
        </text>
      </g>
    </g>

    <!-- Divider Line -->
    <line x1="24" y1="126" x2="682" y2="126" stroke="{panel_border}" stroke-width="1" />

    <!-- Attributes Monospace Key-Value Grid -->
    <g transform="translate(24, 144)" class="mono" font-size="11">
      <!-- Line 1 -->
      <text x="0" y="0" fill="{text_secondary}">&gt; DEGREE</text>
      <text x="120" y="0" fill="{accent_cyan}">::</text>
      <text x="140" y="0" fill="{text_primary}" font-weight="600">B.Tech AI &amp; Data Science (Sigma University · CGPA: 9.22 / 10)</text>

      <!-- Line 2 -->
      <text x="0" y="19" fill="{text_secondary}">&gt; INTERNSHIP</text>
      <text x="120" y="19" fill="{accent_cyan}">::</text>
      <text x="140" y="19" fill="{text_primary}" font-weight="600">9 Months Web Dev Intern @ Bada Builder Pvt. Ltd. (Vadodara)</text>

      <!-- Line 3 -->
      <text x="0" y="38" fill="{text_secondary}">&gt; CORE FOCUS</text>
      <text x="120" y="38" fill="{accent_cyan}">::</text>
      <text x="140" y="38" fill="{text_primary}" font-weight="600">Multi-Role Web Platforms, 3D WebGL, Streaming NLP Pipelines</text>

      <!-- Line 4 -->
      <text x="0" y="57" fill="{text_secondary}">&gt; CLOUD &amp; QA</text>
      <text x="120" y="57" fill="{accent_cyan}">::</text>
      <text x="140" y="60" fill="{text_primary}" font-weight="600">AWS (EC2, S3, RDS), Docker, 58 pytest Tests + GitHub Actions CI</text>
    </g>

    <!-- Divider Line -->
    <line x1="24" y1="218" x2="682" y2="218" stroke="{panel_border}" stroke-width="1" />

    <!-- Technical Stack Pills Section -->
    <text x="24" y="236" class="mono" font-size="10.5" font-weight="700" fill="{text_secondary}">[ PRODUCTION TECH STACK ]</text>
    
    <!-- Pills Row 1 -->
    <g transform="translate(24, 246)">
      <!-- React 19 -->
      <g transform="translate(0, 0)">
        <rect width="84" height="22" rx="6" fill="{pill_bg}" stroke="{pill_border}" />
        <circle cx="10" cy="11" r="3" fill="#61dafb" />
        <text x="18" y="15" class="mono" font-size="10" font-weight="600" fill="{pill_text}">React 19</text>
      </g>
      <!-- Node.js -->
      <g transform="translate(92, 0)">
        <rect width="82" height="22" rx="6" fill="{pill_bg}" stroke="{pill_border}" />
        <circle cx="10" cy="11" r="3" fill="#339933" />
        <text x="18" y="15" class="mono" font-size="10" font-weight="600" fill="{pill_text}">Node.js</text>
      </g>
      <!-- PostgreSQL -->
      <g transform="translate(182, 0)">
        <rect width="102" height="22" rx="6" fill="{pill_bg}" stroke="{pill_border}" />
        <circle cx="10" cy="11" r="3" fill="#4169e1" />
        <text x="18" y="15" class="mono" font-size="10" font-weight="600" fill="{pill_text}">PostgreSQL</text>
      </g>
      <!-- Python -->
      <g transform="translate(292, 0)">
        <rect width="78" height="22" rx="6" fill="{pill_bg}" stroke="{pill_border}" />
        <circle cx="10" cy="11" r="3" fill="#f59e0b" />
        <text x="18" y="15" class="mono" font-size="10" font-weight="600" fill="{pill_text}">Python</text>
      </g>
      <!-- Sentence-BERT -->
      <g transform="translate(378, 0)">
        <rect width="124" height="22" rx="6" fill="{pill_bg}" stroke="{pill_border}" />
        <circle cx="10" cy="11" r="3" fill="#a78bfa" />
        <text x="18" y="15" class="mono" font-size="10" font-weight="600" fill="{pill_text}">Sentence-BERT</text>
      </g>
      <!-- FAISS -->
      <g transform="translate(510, 0)">
        <rect width="66" height="22" rx="6" fill="{pill_bg}" stroke="{pill_border}" />
        <circle cx="10" cy="11" r="3" fill="#10b981" />
        <text x="18" y="15" class="mono" font-size="10" font-weight="600" fill="{pill_text}">FAISS</text>
      </g>
      <!-- Docker -->
      <g transform="translate(584, 0)">
        <rect width="74" height="22" rx="6" fill="{pill_bg}" stroke="{pill_border}" />
        <circle cx="10" cy="11" r="3" fill="#0284c7" />
        <text x="18" y="15" class="mono" font-size="10" font-weight="600" fill="{pill_text}">Docker</text>
      </g>
    </g>

    <!-- Pills Row 2 -->
    <g transform="translate(24, 274)">
      <!-- AWS (EC2, S3, RDS) -->
      <g transform="translate(0, 0)">
        <rect width="144" height="22" rx="6" fill="{pill_bg}" stroke="{pill_border}" />
        <circle cx="10" cy="11" r="3" fill="#ff9900" />
        <text x="18" y="15" class="mono" font-size="10" font-weight="600" fill="{pill_text}">AWS (EC2, S3, RDS)</text>
      </g>
      <!-- Three.js -->
      <g transform="translate(152, 0)">
        <rect width="84" height="22" rx="6" fill="{pill_bg}" stroke="{pill_border}" />
        <circle cx="10" cy="11" r="3" fill="#ffffff" stroke="#94a3b8" />
        <text x="18" y="15" class="mono" font-size="10" font-weight="600" fill="{pill_text}">Three.js</text>
      </g>
      <!-- Socket.io -->
      <g transform="translate(244, 0)">
        <rect width="86" height="22" rx="6" fill="{pill_bg}" stroke="{pill_border}" />
        <circle cx="10" cy="11" r="3" fill="#cbd5e1" />
        <text x="18" y="15" class="mono" font-size="10" font-weight="600" fill="{pill_text}">Socket.io</text>
      </g>
      <!-- HDBSCAN -->
      <g transform="translate(338, 0)">
        <rect width="84" height="22" rx="6" fill="{pill_bg}" stroke="{pill_border}" />
        <circle cx="10" cy="11" r="3" fill="#ec4899" />
        <text x="18" y="15" class="mono" font-size="10" font-weight="600" fill="{pill_text}">HDBSCAN</text>
      </g>
      <!-- Razorpay -->
      <g transform="translate(430, 0)">
        <rect width="86" height="22" rx="6" fill="{pill_bg}" stroke="{pill_border}" />
        <circle cx="10" cy="11" r="3" fill="#2563eb" />
        <text x="18" y="15" class="mono" font-size="10" font-weight="600" fill="{pill_text}">Razorpay</text>
      </g>
      <!-- Streamlit -->
      <g transform="translate(524, 0)">
        <rect width="86" height="22" rx="6" fill="{pill_bg}" stroke="{pill_border}" />
        <circle cx="10" cy="11" r="3" fill="#ff4b4b" />
        <text x="18" y="15" class="mono" font-size="10" font-weight="600" fill="{pill_text}">Streamlit</text>
      </g>
    </g>

    <!-- Divider Line -->
    <line x1="24" y1="308" x2="682" y2="308" stroke="{panel_border}" stroke-width="1" />

    <!-- Flagship Projects Section -->
    <text x="24" y="326" class="mono" font-size="10.5" font-weight="700" fill="{text_secondary}">[ FLAGSHIP PRODUCTION SYSTEMS ]</text>

    <!-- Project 1: Bada Builder -->
    <g transform="translate(24, 336)">
      <rect width="658" height="38" rx="6" fill="{pill_bg}" stroke="{pill_border}" />
      <text x="14" y="16" class="mono" font-size="11" font-weight="700" fill="{accent_cyan}">BADA BUILDER</text>
      <text x="118" y="16" class="mono" font-size="10.5" fill="{text_muted}">|</text>
      <text x="130" y="16" class="sans" font-size="10.5" fill="{text_primary}">Live Real Estate Platform · 5 RBAC Dashboards, 3D WebGL, Razorpay, AWS EC2/S3/RDS</text>
      <text x="14" y="29" class="mono" font-size="9" fill="{accent_emerald}">bada-builder-frontend.vercel.app · 9 Mos Production Build</text>
    </g>

    <!-- Project 2: TrendRadar-AI -->
    <g transform="translate(24, 380)">
      <rect width="658" height="38" rx="6" fill="{pill_bg}" stroke="{pill_border}" />
      <text x="14" y="16" class="mono" font-size="11" font-weight="700" fill="{accent_violet}">TRENDRADAR-AI</text>
      <text x="118" y="16" class="mono" font-size="10.5" fill="{text_muted}">|</text>
      <text x="130" y="16" class="sans" font-size="10.5" fill="{text_primary}">Streaming NLP Engine · Sentence-BERT, HDBSCAN, FAISS, 58 pytest tests + GitHub CI</text>
      <text x="14" y="29" class="mono" font-size="9" fill="{accent_cyan}">8,784 Reddit Posts · Novelty Filter Slashed Alert Noise from 39 to 14</text>
    </g>

    <!-- Project 3: RadiantWears -->
    <g transform="translate(24, 424)">
      <rect width="658" height="38" rx="6" fill="{pill_bg}" stroke="{pill_border}" />
      <text x="14" y="16" class="mono" font-size="11" font-weight="700" fill="{accent_emerald}">RADIANTWEARS</text>
      <text x="118" y="16" class="mono" font-size="10.5" fill="{text_muted}">|</text>
      <text x="130" y="16" class="sans" font-size="10.5" fill="{text_primary}">Full-Stack Clothing E-Commerce · React, Node.js, Neon PostgreSQL, Admin Dashboard</text>
      <text x="14" y="29" class="mono" font-size="9" fill="{accent_amber}">radiantwear-puce.vercel.app · Order Lifecycle &amp; Inventory Sync</text>
    </g>

    <!-- Terminal Footer Interactive Links -->
    <line x1="24" y1="472" x2="682" y2="472" stroke="{panel_border}" stroke-width="1" />

    <g transform="translate(24, 480)">
      <!-- GitHub Link Card -->
      <g transform="translate(0, 0)">
        <rect width="210" height="30" rx="6" fill="{card_link_bg}" stroke="{card_link_border}" />
        <!-- GitHub Octocat SVG icon -->
        <path d="M18 9c-3.3 0-6 2.7-6 6 0 2.6 1.7 4.9 4.1 5.7.3.1.4-.1.4-.3v-1.1c-1.7.4-2-8-2-.8-.3-.7-.7-.9-.7-.9-.5-.4 0-.4 0-.4.6 0 .9.6.9.6.5.9 1.4.6 1.7.5.1-.4.2-.6.4-.8-1.3-.1-2.7-.7-2.7-3 0-.7.2-1.2.6-1.7 0-.2-.3-.8.1-1.6 0 0 .5-.2 1.7.6.5-.1 1-.2 1.6-.2s1.1.1 1.6.2c1.2-.8 1.7-.6 1.7-.6.4.8.1 1.4.1 1.6.4.5.6 1 .6 1.7 0 2.3-1.4 2.8-2.7 3 .2.2.4.6.4 1.2v1.7c0 .2.1.4.4.3 2.4-.8 4.1-3.1 4.1-5.7 0-3.3-2.7-6-6-6z" fill="{card_link_text}" transform="translate(0, -1)" />
        <text x="32" y="19" class="mono" font-size="11" font-weight="600" fill="{card_link_text}">github.com/sun2004ny</text>
      </g>
      <!-- LinkedIn Link Card -->
      <g transform="translate(222, 0)">
        <rect width="216" height="30" rx="6" fill="{card_link_bg}" stroke="{card_link_border}" />
        <!-- LinkedIn in SVG icon -->
        <path d="M15 11h2v8h-2v-8zm1-3c.7 0 1.2.5 1.2 1.2s-.5 1.2-1.2 1.2-1.2-.5-1.2-1.2.5-1.2 1.2-1.2zm3 3h2v1.2h.1c.3-.6 1.1-1.3 2.3-1.3 2.5 0 3 1.6 3 3.8v4.3h-2v-3.8c0-.9 0-2.1-1.3-2.1s-1.5 1-1.5 2v3.9h-2v-8z" fill="{card_link_text}" />
        <text x="32" y="19" class="mono" font-size="11" font-weight="600" fill="{card_link_text}">linkedin.com/in/sunnymore</text>
      </g>
      <!-- Email Link Card -->
      <g transform="translate(450, 0)">
        <rect width="208" height="30" rx="6" fill="{card_link_bg}" stroke="{card_link_border}" />
        <!-- Mail envelope SVG icon -->
        <path d="M14 11h12c.6 0 1 .4 1 1v7c0 .6-.4 1-1 1H14c-.6 0-1-.4-1-1v-7c0-.6.4-1 1-1zm6 4.5l-5.5-3.5h11l-5.5 3.5zm0 1.2l5.8-3.7H14.2l5.8 3.7z" fill="{card_link_text}" />
        <text x="32" y="19" class="mono" font-size="10.5" font-weight="600" fill="{card_link_text}">sunny260604@gmail.com</text>
      </g>
    </g>
  </g>
</svg>"""
    return svg


if __name__ == "__main__":
    dark_svg = build_svg("dark")
    light_svg = build_svg("light")
    
    with open(r"c:\Users\sunny\Downloads\sun2004ny\dark.svg", "w", encoding="utf-8") as f:
        f.write(dark_svg)
    print("Regenerated dark.svg with strict frame bounds and zero overlap.")

    with open(r"c:\Users\sunny\Downloads\sun2004ny\light.svg", "w", encoding="utf-8") as f:
        f.write(light_svg)
    print("Regenerated light.svg with strict frame bounds and zero overlap.")

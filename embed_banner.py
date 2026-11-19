# -*- coding: utf-8 -*-
import base64
import os
import xml.etree.ElementTree as ET

# Read hero-banner.jpg and encode to base64
banner_path = r"c:\Users\sunny\Downloads\sun2004ny\hero-banner.jpg"
with open(banner_path, "rb") as f:
    b64_data = base64.b64encode(f.read()).decode("utf-8")

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1024 506" width="1024" height="506" role="img" aria-label="Sunny More — Full-Stack Web Architect and Applied NLP Engineer Profile Banner">
  <defs>
    <!-- Laser Glow Gradient -->
    <linearGradient id="laser-glow" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="rgba(34, 211, 238, 0.45)" />
      <stop offset="100%" stop-color="rgba(34, 211, 238, 0)" />
    </linearGradient>
  </defs>

  <!-- High-Fidelity 3D Cyber-Scan Hero Banner -->
  <image href="data:image/jpeg;base64,{b64_data}" width="1024" height="506" />

  <!-- Live Animated Scanning Laser Overlay on the 3D Cyber Portrait -->
  <g>
    <!-- Radiant laser sweep wash -->
    <rect x="36" y="86" width="316" height="38" fill="url(#laser-glow)">
      <animate attributeName="y" values="86;338;86" dur="4s" repeatCount="indefinite" />
    </rect>
    <!-- Leading laser beam line -->
    <line x1="36" y1="86" x2="352" y2="86" stroke="#22d3ee" stroke-width="2.2" stroke-opacity="0.95">
      <animate attributeName="y1" values="86;376;86" dur="4s" repeatCount="indefinite" />
      <animate attributeName="y2" values="86;376;86" dur="4s" repeatCount="indefinite" />
    </line>
  </g>

  <!-- Live Pulsing Online Status Indicator -->
  <circle cx="866" cy="27" r="4" fill="#10b981">
    <animate attributeName="r" values="3.5;5;3.5" dur="2s" repeatCount="indefinite" />
    <animate attributeName="opacity" values="0.8;1;0.8" dur="2s" repeatCount="indefinite" />
  </circle>
</svg>"""

with open(r"c:\Users\sunny\Downloads\sun2004ny\dark.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("Updated dark.svg with embedded hero-banner.jpg and live scanning animations. Size:", len(svg_content))

# Verify XML
tree = ET.parse(r"c:\Users\sunny\Downloads\sun2004ny\dark.svg")
root = tree.getroot()
print("dark.svg XML valid! Root tag:", root.tag)

import os
import re

files = ['index.html', 'landmarks.html', 'regional-painting-styles.html']
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace root variables
    content = re.sub(
        r':root\s*\{[^\}]+\}',
        ':root{\n    --bg:#0f172a;\n    --panel:#1e293b;\n    --panel-2:#334155;\n    --line:#475569;\n    --gold:#38bdf8;\n    --gold-2:#7dd3fc;\n    --text:#f8fafc;\n    --muted:#94a3b8;\n    --radius:16px;\n  }',
        content
    )
    
    # Replace radial gradient colors to match new theme (sky blue and indigo instead of gold and blue)
    content = content.replace('rgba(224,180,92,.08)', 'rgba(56, 189, 248, .08)')
    content = content.replace('rgba(90,120,200,.07)', 'rgba(99, 102, 241, .07)')
    content = content.replace('rgba(90,140,220,.08)', 'rgba(99, 102, 241, .08)')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

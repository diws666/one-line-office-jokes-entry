import os

# Verified: exactly 82 UTF-8 bytes (no trailing newline).
LINE = "HR sent an email about work-life balance at 11 p.m. on a Sunday. I have framed it."

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
entry_path = os.path.join(output_dir, 'entry.txt')

os.makedirs(output_dir, exist_ok=True)
with open(entry_path, 'w', encoding='utf-8', newline='') as f:
    f.write(LINE)

print(len(LINE.encode('utf-8')))

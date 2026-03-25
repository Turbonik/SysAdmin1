#!/usr/bin/env python3
import subprocess
import os

STATE_FILE = os.path.expanduser("~/.login_monitor.state")
message_sender_script_path = os.path.expanduser("~/send_telegram.py")
result = subprocess.run(["last", "-w", "-n", "20"], capture_output=True, text=True)
lines = result.stdout.strip().split("\n")

if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        last_line = f.read().strip()
else:
    last_line = ""

if not last_line:
    with open(STATE_FILE, "w") as f:
        f.write(lines[0])
    exit(0)


new_lines = []
for line in lines:
    if line == last_line:
        break
    new_lines.append(line)

for line in reversed(new_lines):
    parts = line.split()
    
    if len(parts) < 8:
        continue

    login = parts[0]
    tail = parts[-7:]
 
    if "-" in tail:
        dash_index = tail.index("-")
        tail = tail[:dash_index]

    formatted = " ".join(tail)


    os.system(f"/usr/bin/env python3 {message_sender_script_path} {login} '{formatted}'")

with open(STATE_FILE, "w") as f:
    f.write(lines[0] + "\n")
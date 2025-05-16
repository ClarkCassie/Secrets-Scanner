import os
import re

#Folder selected for scanning:
FOLDER = "sandbox_codebase"

#Define regex of common secrets
patterns = [
  re.compile(r'API_KEY\s*=\s*[\'"]([A-Za-z0-9_\-]{20,})[\'"]'),
  re.compile(r'password\s*=\s*[\'"](.+?)[\'"]', re.IGNORECASE),
  re.compile(r'AWS_SECRET_ACCESS_KEY\s*=\s*[\'"]([A-Za-z0-9/+=]{40})[\'"]'),
]

def scan_file(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
      content = f.read()
      for pattern in patterns:
        for match in pattern.finditer(content):
          print(f"[!] Potential secret found in {file_path}: {match.group()}")


#Walk through files in the target folder
for root, _, files in os.walk(FOLDER):
  for file in files:
    if file.endswith((".py", ".env", ".txt")):
      scan_file(os.path.join(root, file))
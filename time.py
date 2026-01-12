#!/usr/bin/env python3
import sys

seconds = int(sys.argv[1])

hours = seconds // 3600
rest = seconds % 3600
minutes = rest // 60
secs = rest % 60

print(f"{hours}h{minutes}m{secs}s")

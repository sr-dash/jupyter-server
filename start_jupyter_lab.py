#!/usr/bin/env python3
import subprocess
import os
import socket
import time
import json
import re
from datetime import datetime

def find_free_port(start_port=8888, max_tries=50):
    """Find the next available port on the system."""
    port = start_port
    for _ in range(max_tries):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                return port
            except OSError:
                port += 1
    raise RuntimeError("No available ports found.")

def main():
    log_file_path = os.path.expanduser("/data/sdash/JupyterLabs/jupyter_lab.json")

    # Find a free port
    port = find_free_port()

    # Command to run JupyterLab
    cmd = [
        "jupyter", "lab",
        "--no-browser",
        f"--port={port}",
        "--ip=0.0.0.0"
    ]

    # Start the JupyterLab server
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    pid = process.pid
    start_time = datetime.now().isoformat()
    token = None

    # Read and parse output for the token
    output_lines = []
    for line in process.stdout:
        output_lines.append(line)
        token_match = re.search(r"token=([a-zA-Z0-9]+)", line)
        if token_match:
            token = token_match.group(1)
            break

    # Save log as JSON
    session_info = {
        "job_id": pid,
        "start_time": start_time,
        "port": port,
        "token": token,
        "url": f"http://localhost:{port}/?token={token}",
    }

    with open(log_file_path, "w") as f:
        json.dump(session_info, f, indent=4)

    print(f"JupyterLab started with PID {pid}")
    print(f"Session info written to {log_file_path}")

if __name__ == "__main__":
    main()

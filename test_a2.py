import subprocess
import re

def test_ping_google_dns():
    host = "8.8.8.8"
    command = ["ping", "-n", "5", host]

    completed = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=10,
    )

    # Extract packet loss percentage from stdout using regex
    # Windows ping output contains a line like: "Packets: Sent = 5, Received = 2, Lost = 3 (60% loss)"
    match = re.search(r"Lost = \d+ \((\d+)% loss\)", completed.stdout)
    if match:
        loss_percent = int(match.group(1))
    else:
        loss_percent = None  # fallback if parsing fails

    # Assert with tolerance (e.g., allow up to 20% loss)
    assert loss_percent is not None and loss_percent <= 20, (
        f"Ping to {host} failed: {loss_percent}% packet loss.\n"
        f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}"
    )

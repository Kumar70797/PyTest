import subprocess

def test_ping_google_dns():
    host = "4.5.6.7"
    command = ["ping", "-n", "1", host]

    completed = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=10,
    )

    assert completed.returncode == 0, (
        f"Ping to {host} failed with return code {completed.returncode}.\n"
        f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}"
    )

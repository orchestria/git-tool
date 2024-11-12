# /// script
# requires-python = "~=3.12"
# ///

import json
import subprocess
import sys


def run():
    args = sys.argv[-1]
    data = json.loads(args)

    if "working_dir" not in data:
        raise ValueError("working_dir not provided")

    cwd = data["working_dir"]

    command = ["git", "status"]

    res = subprocess.run(command, capture_output=True, text=True, check=True, cwd=cwd)

    status = {}
    if res.returncode:
        status["error"] = res.stderr
    else:
        status["output"] = res.stdout.splitlines()

    print(json.dumps(status))


if __name__ == "__main__":
    run()

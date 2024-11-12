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

    if "branch_name" not in data:
        raise ValueError("branch_name not provided")

    cwd = data["working_dir"]
    branch_name = data["branch_name"]

    command = ["git", "branch", branch_name]

    res = subprocess.run(command, capture_output=True, text=True, check=False, cwd=cwd)

    status = {}
    if res.returncode:
        status["error"] = res.stderr
    else:
        status["output"] = res.stdout.splitlines()

    print(json.dumps(status))


if __name__ == "__main__":
    run()

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

    if "target" not in data:
        raise ValueError("target not provided")

    cwd = data["working_dir"]

    # Branch or commit to checkout
    target = data["target"]

    # Optional: create new branch
    create_branch = data.get("create_branch", False)

    command = ["git", "checkout"]
    if create_branch:
        command.append("-b")
    command.append(target)

    res = subprocess.run(command, capture_output=True, text=True, check=False, cwd=cwd)

    status = {}
    if res.returncode:
        status["error"] = res.stderr
    else:
        status["output"] = res.stdout

    print(json.dumps(status))


if __name__ == "__main__":
    run()

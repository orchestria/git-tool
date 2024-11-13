# /// script
# requires-python = "~=3.12"
# ///

import json
import subprocess
import sys


def run():
    args = sys.argv[-1]
    data = json.loads(args)

    if "repository" not in data:
        raise ValueError("repository URL not provided")

    if "target_dir" not in data:
        raise ValueError("target_dir URL not provided")

    repository = data["repository"]
    target_dir = data["target_dir"]

    command = ["git", "clone", repository]
    if target_dir:
        command.append(target_dir)

    # If working_dir is provided, use it as the parent directory for cloning
    cwd = data.get("working_dir", None)

    res = subprocess.run(command, capture_output=True, text=True, check=True, cwd=cwd)

    status = {}
    if res.returncode:
        status["error"] = res.stderr
    else:
        status["status"] = "success"

    print(json.dumps(status))


if __name__ == "__main__":
    run()

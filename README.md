tools:

Basic tools collection to let an Agent interact with a Git repository.

## Usage

Add:

```
$ hatch run git_add.py '{{"working_dir": "/path/to/repo", "paths": ["file1.txt", "file2.py"]}}'
```

Checkout:

```
$ hatch run git_checkout.py '{{"working_dir": "/path/to/repo", "target": "feature-branch", "create_branch": true}}'
```

Clone:

```
$ hatch run git_clone.py '{{"repository": "https://github.com/user/repo.git", "target_dir": "local-folder"}}'
```

Commit:

```
$ hatch run git_commit.py '{{"working_dir": "/path/to/repo", "message": "Commit message"}}'
```

Create Branch:

```
$ hatch run git_create_branch.py '{{"working_dir": "/path/to/repo", "branch_name": "my-branch"}}'
```

Pull:

```
$ hatch run git_pull.py '{{"working_dir": "/path/to/repo", "remote": "my_remote"}}'
```

Push:

```
$ hatch run git_push.py '{{"working_dir": "/path/to/repo", "remote": "my_remote"}}'
```

Status:

```
$ hatch run git_status.py '{{"working_dir": "/path/to/repo"}}'
```

## License

The repo is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

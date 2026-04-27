# Autoresearch Tools

This folder contains support tools for running the autoresearch loop.

## Git Queue Worker

`git_queue_worker.ps1` is a host-side workaround for environments where Codex can edit normal files but cannot write to `.git`.

Run this from a normal PowerShell window in the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\autoresearch\tools\git_queue_worker.ps1
```

The worker watches:

```text
autoresearch/scratch/git_queue
```

Codex writes JSON jobs there. The worker stages the listed paths, commits them, optionally pushes, and moves completed jobs to:

```text
autoresearch/scratch/git_done
```

The queue and done folders are intentionally ignored by git.

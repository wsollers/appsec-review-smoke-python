# Changelog

All notable changes to this project are documented in this file. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- Smoke service with status, echo, lookup and config paths.
- Pinned dependency set in `requirements.txt` and `pyproject.toml`.

### Changed

- Builds with `python3 -m compileall -q .`.
- `tools/make-history.sh` reproduces the commit graph.

### Security

- 2026-02-10: Upgraded Jinja2 from 2.10 to 3.1.6 (CVE-2019-10906, GHSA-462w-v97r-4m45, sandbox escape through str.format).
- 2026-02-26: Fixed command injection in `archive` (CWE-78); the tarball is now built without a shell.
- 2026-03-14: Fixed path traversal in `read_report` (CWE-22); paths are canonicalised and confined to the report directory.

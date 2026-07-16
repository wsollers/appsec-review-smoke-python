# appsec-review-smoke-python

A deliberately vulnerable **smoke target** for [appsec-review](https://github.com/wsollers/appsec-review).
It exists so that a review of a tiny, fully understood Python program has one correct answer at
every stage. **Do not deploy, run against untrusted input, or reuse any of this code.**

The program is a toy Flask service: `smoke.service` dispatches API requests by path, and
`smoke.app` is the code-graph fixture service.

## Build

One package under `src/`, one manifest, no network, no generated code. The build is a byte-compile
of every module:

```sh
python3 -m compileall -q .
```

The build is expected to succeed in the appsec-review `python` build image (Python 3.12.3) as an
unprivileged user with networking disabled. `requirements.txt` pins the dependency set exactly;
nothing is installed by the build.

## History

`tools/make-history.sh` rebuilds this repository's commit graph from `tools/history/steps/` with
fixed authors and dates, so the history is reproducible and can be reviewed as code.

## License

MIT; see `LICENSE`.

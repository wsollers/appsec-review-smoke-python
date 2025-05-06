# appsec-review-smoke-python

A deliberately vulnerable **smoke target** for [appsec-review](https://github.com/wsollers/appsec-review).
It exists so that a review of a tiny, fully understood Python program has one correct answer at
every stage. **Do not deploy, run against untrusted input, or reuse any of this code.**

The program is a toy Flask service: `smoke.service` dispatches API requests by path, and
`smoke.app` is the code-graph fixture service.

## License

MIT; see `LICENSE`.

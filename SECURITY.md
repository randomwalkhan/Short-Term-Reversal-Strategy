# Security Policy

## Supported Versions

Security fixes are only maintained for the current public version of this repository.

| Version | Supported |
| --- | --- |
| `Reversal 3.2` | Yes |
| Earlier versions | No |

## Scope

This repository contains research code, backtests, visualizations, and a live paper-trading workflow.
It is not intended to store real-money brokerage credentials, exchange API secrets, or production trading infrastructure.

Please report the following privately:

- exposed API keys, tokens, passwords, or credentials
- accidental disclosure of personal data, local paths, or sensitive logs
- workflow bugs that materially misstate live paper-trading results
- dependency or script behavior that could allow unintended code execution or data access

## Reporting a Vulnerability

Please do **not** open a public GitHub issue for security-sensitive findings.

Instead, report the issue privately through GitHub by contacting the repository owner directly. Include:

- a short description of the issue
- affected file(s) or workflow(s)
- reproduction steps, if available
- potential impact

If the issue involves exposed credentials or sensitive data, please avoid pasting the full secret. A redacted sample is enough.

## Expected Response

Reasonable efforts will be made to:

- acknowledge the report
- validate whether the issue is real
- remove exposed secrets or sensitive material if applicable
- patch the repository when appropriate

There is no formal SLA for response time.

## Safe Handling Expectations

If you discover exposed credentials:

1. Do not use them.
2. Do not share them publicly.
3. Report them privately as soon as possible.

If the issue could affect current live paper-trading outputs, please mention that in your report so the affected logs or dashboards can be reviewed promptly.

# claude-api-fuzzing-bug-bounty-skill

A Claude Code skill for planning and conducting authorized API security testing, including structured input testing and vulnerability validation.

## Overview

This skill supports security assessment of REST, SOAP, and GraphQL APIs. It helps organize endpoint discovery, input variation, authorization checks, and evidence collection for bug bounty or approved penetration-testing engagements.

Testing must remain within the program's written scope and rules. The presence of a public endpoint does not imply permission to test it.

## Main Capabilities

- Inventory API endpoints and operations.
- Review API schemas and documentation.
- Identify authentication and authorization boundaries.
- Plan safe input variation and fuzzing.
- Review object-level access controls.
- Test validation and error handling.
- Identify potential injection and data exposure issues.
- Record reproducible evidence.
- Prioritize findings and remediation.
- Use local utilities to inspect API specifications.

## Installation

```bash
git clone https://github.com/Brajesh31/claude-api-fuzzing-bug-bounty-skill.git ~/.claude/skills/api-fuzzing-bug-bounty
```

## Usage

Invoke the skill for an authorized API assessment:

```text
/api-fuzzing-bug-bounty
```

Provide the program scope, target API, permitted test methods, rate limits, test accounts, and prohibited actions.

## Included Utility

The repository includes `json2paths.py`, a passive local OpenAPI/Swagger path inventory helper:

```bash
python3 json2paths.py swagger.json
```

YAML input may require PyYAML. This utility inspects a local specification and does not send requests or perform vulnerability testing.

## Recommended Workflow

1. Confirm authorization and scope.
2. Parse the API specification or inventory routes.
3. Identify methods, parameters, and authentication requirements.
4. Map object and function authorization boundaries.
5. Prepare safe, bounded test cases.
6. Execute only permitted tests.
7. Record request and response evidence with sensitive data removed.
8. Validate suspected issues.
9. Report impact and remediation.
10. Re-test fixes when authorized.

## Reporting Format

| Field | Description |
|---|---|
| Finding | Concise vulnerability description |
| Endpoint | Affected route or operation |
| Preconditions | Required role or state |
| Evidence | Sanitized request and response |
| Impact | Realistic consequence |
| Severity | Risk-based rating |
| Remediation | Specific defensive change |
| Retest | Verification outcome |

## Safety Checklist

- Testing is explicitly authorized.
- Target and methods are within scope.
- Rate limits and testing windows are respected.
- No unrelated data is accessed.
- Destructive actions are avoided unless explicitly permitted.
- Evidence is sanitized.
- Findings are reproducible.
- Stop conditions are followed.

## Repository Contents

- `SKILL.md`: Main API assessment workflow.
- `json2paths.py`: Passive API path inventory utility.
- `README.md`: Scope, process, and safety guidance.

## Practical Principle

A bug bounty finding must be reproducible and within program scope. Avoid aggressive testing that risks service availability or accesses data beyond the authorized target.

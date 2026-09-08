"""Cross-language pin of the harness's captureFingerprint (judge.ts).

The harness computes the capture fingerprint as
    createHash('sha256').update(JSON.stringify(capture.cases)).digest('hex')
(see evaluation/answer/judge.ts). Node's JSON.stringify is compact
(no spaces), non-ASCII characters are emitted raw (no \\uXXXX escaping),
and key order follows insertion order -- so the Python mirror below must
use separators=(",", ":"), ensure_ascii=False, and preserve the fixture's
key order. The EXPECTED hex was produced from
tests/fixtures/capture-fingerprint-pin.json by the inline tsx command
documented in the Task 6 brief; PR B's test re-pins the REAL TypeScript
function against the same hex.
"""

import hashlib
import json
from pathlib import Path

PIN = Path(__file__).parent / "fixtures" / "capture-fingerprint-pin.json"
EXPECTED = "298a04f89fac6d6539a5a6fb6ce6be4e6158e9543d9ecb2d3cc951b0593451e8"


def mirror(capture: dict) -> str:
    cases = capture["cases"]
    return hashlib.sha256(
        json.dumps(cases, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


def test_mirror_matches_harness_fingerprint():
    capture = json.loads(PIN.read_text(encoding="utf-8"))
    assert capture["schema"] == "answer-eval/capture@1"
    assert mirror(capture) == EXPECTED


def test_mirror_ignores_non_cases_fields():
    """Only capture.cases feeds the fingerprint -- provenance/preflight
    must not change it."""
    capture = json.loads(PIN.read_text(encoding="utf-8"))
    touched = json.loads(PIN.read_text(encoding="utf-8"))
    touched["provenance"]["timestamp"] = "2099-01-01T00:00:00Z"
    assert mirror(touched) == mirror(capture)

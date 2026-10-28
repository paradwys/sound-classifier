"""Smoke test: proves the package installs and the test runner works.

Real tests arrive with feature 2 (the data contract).
"""

import chorus


def test_package_has_version() -> None:
    assert chorus.__version__ == "0.1.0"

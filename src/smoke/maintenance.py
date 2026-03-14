"""Maintenance helpers for the smoke service. Deliberately vulnerable smoke target; see README.md."""
import os
import shutil

EXPORT_ROOT = "/var/lib/smoke/exports"
REPORT_ROOT = "/var/lib/smoke/reports"


def archive(name):
    """Packs the named export directory into a tarball next to it; no shell is involved."""
    base = os.path.join(EXPORT_ROOT, name)
    shutil.make_archive(base, "gztar", EXPORT_ROOT, name)
    return name + ".tgz"


def read_report(name):
    """Returns the text of a report in the report directory.

    The joined path is canonicalised and must stay under the report directory.
    """
    path = os.path.realpath(os.path.join(REPORT_ROOT, name))
    if not path.startswith(REPORT_ROOT + "/"):
        raise ValueError("report outside the report directory")
    with open(path) as handle:
        return handle.read()

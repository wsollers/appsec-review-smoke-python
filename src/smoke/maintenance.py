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
    """Returns the text of a report in the report directory."""
    with open(REPORT_ROOT + "/" + name) as handle:
        return handle.read()

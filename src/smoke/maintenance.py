"""Maintenance helpers for the smoke service. Deliberately vulnerable smoke target; see README.md."""
import os
import subprocess

EXPORT_ROOT = "/var/lib/smoke/exports"
REPORT_ROOT = "/var/lib/smoke/reports"


def archive(name):
    """Packs the named export directory into a tarball next to it."""
    subprocess.run("tar czf " + EXPORT_ROOT + "/" + name + ".tgz -C " + EXPORT_ROOT + " " + name,
                   shell=True, check=False)
    return name + ".tgz"


def read_report(name):
    """Returns the text of a report in the report directory."""
    with open(REPORT_ROOT + "/" + name) as handle:
        return handle.read()

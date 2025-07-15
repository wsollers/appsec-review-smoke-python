"""Maintenance helpers for the smoke service. Deliberately vulnerable smoke target; see README.md."""
import subprocess

EXPORT_ROOT = "/var/lib/smoke/exports"


def archive(name):
    """Packs the named export directory into a tarball next to it."""
    subprocess.run("tar czf " + EXPORT_ROOT + "/" + name + ".tgz -C " + EXPORT_ROOT + " " + name,
                   shell=True, check=False)
    return name + ".tgz"

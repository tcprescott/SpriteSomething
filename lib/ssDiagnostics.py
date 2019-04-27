import platform, sys, os, subprocess
import lib.constants as CONST
from datetime import datetime

def diagpad(str):
  return str.ljust(len("SpriteSomething Version") + 5,'.')

def output():
  lines = [
    "SpriteSomething Diagnostics",
    "===========================",
    diagpad("UTC Time") + str(datetime.utcnow())[:19],
    diagpad("SpriteSomething Version") + CONST.APP_VERSION,
    diagpad("Python Version") + platform.python_version()
  ]
  lines.append(diagpad("OS Version") + "%s %s" % (platform.system(), platform.release()))
  if hasattr(sys, "executable"):
    lines.append(diagpad("Executable") + sys.executable)
  lines.append(diagpad("Build Date") + platform.python_build()[1])
  lines.append(diagpad("Compiler") + platform.python_compiler())
  if hasattr(sys, "api_version"):
    lines.append(diagpad("Python API") + str(sys.api_version))
  if hasattr(os, "sep"):
    lines.append(diagpad("Filepath Separator") + os.sep)
  if hasattr(os, "pathsep"):
    lines.append(diagpad("Path Env Separator") + os.pathsep)
  lines.append("")
  lines.append("Packages")
  lines.append("--------")
  reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
  installed_packages = [r.decode() for r in reqs.split()]
  for pkg in installed_packages:
    pkg = pkg.split("==")
    lines.append(diagpad(pkg[0]) + pkg[1])
  return lines

if __name__ == "__main__":
    raise AssertionError(f"Called main() on utility library {__file__}")

# Trimmed lilac.py
#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  update_pkgver_and_pkgrel(_G.newver)
  run_cmd(['updpkgsums'])

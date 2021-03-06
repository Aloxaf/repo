# Trimmed lilac.py
#!/usr/bin/env python3

from lilaclib import *

#build_prefix = 'extra-x86_64'

def pre_build():
  pypi_pre_build(
    depends = ['python-six', 'libsass'],
    depends_setuptools = True,
    makedepends = ['gcc'],
    arch = ['x86_64'],
    provides = ['sassc']
  )

def post_build():
  pypi_post_build()
  update_aur_repo()

#if __name__ == '__main__':
#  single_main()

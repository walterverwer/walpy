### General utility functions module:

import os
from subprocess import getoutput

# Clone the Utility-Functions repository for integration, use subprocess:
getoutput('git clone -l -s git://github.com/walterverwer/Utility-Functions Utility-Functions')
os.chdir('Utility-Functions')

def r_import(modules):
  """
  Import R packages. If the desired packages are not installed it will
  automatically install them. Note that this function will act as a one time
  delay in running time, if modules need to be installed.

  Args:
      modules: list of the desired packages. The packages to be included should
      be as a string. E.g. modules = ['stargazer', 'tidyverse'].

  Returns:
      None
  """
  # Import rpy2's package module
  import rpy2.robjects.packages as rpackages

  # import R's utility package
  utils = rpackages.importr('utils')

  # select a mirror for R packages
  utils.chooseCRANmirror(ind=1) # select the first mirror in the list

  # R package names
  packnames = tuple(modules)

  # R vector of strings
  from rpy2.robjects.vectors import StrVector

  # Selectively install what needs to be install.
  # We are fancy, just because we can.
  names_to_install = [x for x in packnames if not rpackages.isinstalled(x)]
  if len(names_to_install) > 0:
      utils.install_packages(StrVector(names_to_install))
  
  return

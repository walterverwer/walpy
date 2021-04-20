# -*- coding: utf-8 -*-
"""walpy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12GceB64bo-uwVSQEX441fTlpK3D4fJOc

#Walter's Python - walpy
Welcome! In this notebook I have writen general (short) functions for every day use, which are written to a separate python script. For this reason every function can be imported from the repo separately. There is also a general file containing all functions. The primary usage would be in data science work, however the use cases could be more comprehensive.
"""

import os
from subprocess import getoutput
 
# Clone the Utility-Functions repository for integration, use subprocess:
getoutput('git clone -l -s git://github.com/walterverwer/walpy walpy')
os.chdir('walpy')

"""## Write and run (cell magic)
This function is a modification of the %%writefiles cell magic command. The original function only writes the cell to a (new) python script, while this function allows one to write and run the cell. This is useful when working in a notebook for developing functions, like this notebook!
"""

# Commented out IPython magic to ensure Python compatibility.
from IPython.core.magic import register_cell_magic

@register_cell_magic
def write_and_run(line, cell):
    """
    Write and run the cell. Use as follows: 
    
#     %%write_and_run script.py to overwrite existing scripts.
    
#     %%write_and_run -a script.py to append to the existing script.
    
    For both cases, if the script does not exist, then a new one is 
    created automatically.

    Args:
        line: ignore. See above.

        cell: ignore. See above.

    Returns:
        None
    """
    argz = line.split()
    file = argz[-1]
    mode = 'w'
    if len(argz) == 2 and argz[0] == '-a':
        mode = 'a'
    with open(file, mode) as f:
        f.write(cell)
    get_ipython().run_cell(cell)

    return

"""##R to Python installer and importer
When importing R packages while working in a Python environment can lead to some unnecessary code. In order to provide a as clean and close to importing Python packages, I have written this function that allows one to import a list of R packages. The package is flexible enough to also allow for manual imports. If one wants to manually import an R package, simply specify the package(s) to be installed manually and map the example below the following code cell to the individual's use case.
"""

# Commented out IPython magic to ensure Python compatibility.
# %%write_and_run r_importer.py
# def r_importer(modules, install_only=None, log=False):
#   """
#   Import and install R packages. If the desired packages are not installed it will
#   automatically install them. Note that this function will act as a one time
#   delay in running time, if modules need to be installed. Import R packages
#   manually as e.g. <stargazer =  rpy2.robjects.packages.importr('stargazer')>.
#   So, the same name used for installing, should be used to import the functions.
#   Important to note, this function imports the following modules from rpy2:
#   "rpy2.robjects.packages" and "rpy2.robjects.vectors".
#  
#   Args:
#       modules: list of the desired packages. The packages to be included should
#       be as a string. E.g. modules = ['stargazer', 'tidyverse'].
# 
#       install_only: default=None. list or string of packages to be installed 
#       only. Note, combinations are possible.
# 
#       log: default=False. Prints a log message if true, of the packages are
#       (succesfully) installed.
#  
#   Returns:
#       None
#   """
#   # Import rpy2's package module:
#   import rpy2.robjects.packages as rpackages
#  
#   # import R's utility package:
#   utils = rpackages.importr('utils')
#  
#   # R package names:
#   packnames = tuple(modules)
#  
#   # R vector of strings:
#   from rpy2.robjects.vectors import StrVector
#  
#   # Selectively install what needs to be install. Use CRAN cloud server:
#   names_to_install = [x for x in packnames if not rpackages.isinstalled(x)]
#   if len(names_to_install) > 0 and log == True:
#     utils.install_packages(StrVector(names_to_install),
#                             repos='https://cloud.r-project.org/')
#   else:
#     utils.install_packages(StrVector(names_to_install),
#                           repos='https://cloud.r-project.org/');
#   
#   # Make modules non-overlapping with install_only:
#   modules = set(modules) - set(install_only)
# 
#   # Import modules to be automatically imported
#   for module in modules:
#     rpackages.importr(module)
#   
#   # Print log message if true:
#   if log == True:
#     print('Successfully imported and/ or installed:', [i for i in modules])
# 
#   return

"""### Example

In order to manually import *sandwich* and *stargazer*, and automatically import *dplyr* and *tidyverse* run the following code. 

**Important**: in order to prevent cluttering in this document I have already installed the packages! Normally if log=True and one has not installed the packages, you will see the corresponding installation output of the rpy2 package.

"""

# First import the following rpy2 module for manual importing:
import rpy2.robjects.packages

# Modules to be installed:
modules = ['dplyr', 'tidyverse'] # This is correct!
modules = ['dplyr', 'tidyverse','sandwich', 'stargazer'] # This is also correct!
install_only = ['sandwich', 'stargazer'] # What to install only

# Run the R importer function
r_importer(modules, install_only, log=True) # log=True for demonstration

# Assign packages of the manual installs to the Python environment:
sandwich = rpy2.robjects.packages.importr('sandwich') 
stargazer =  rpy2.robjects.packages.importr('stargazer')
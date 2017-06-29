"""
Base __init__ for the quantum_python library

"""

import psi4
psi4.set_output_file("output.dat", False)

from .rhf import *
from .mp2 import *

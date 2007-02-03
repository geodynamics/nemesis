
from archimedes import use_merlin
use_merlin()

from merlin import setup, find_packages

setup(
    
    name = 'nemesis', 
    version = '1.0',

    zip_safe = False,
    packages = find_packages(),
    
    install_requires = [
    'pythia[mpi] >= 0.8.1.0, < 0.8.2a',
    ],

    author = 'Leif Strand',
    author_email = 'leif@geodynamics.org',
    description = """A Python interpreter which embeds MPI.""",
    license = 'BSD',
    url = 'http://www.geodynamics.org/cig/software/packages/cs/pythia/',

)

#!/usr/bin/env nemesis
# ======================================================================
#
# Brad T. Aagaard, U.S. Geological Survey
# Charles A. Williams, GNS Science
# Matthew G. Knepley, University of Chicago
#
# This code was developed as part of the Computational Infrastructure
# for Geodynamics (http://geodynamics.org).
#
# Copyright (c) 2010-2017 University of California, Davis
#
# See COPYING for license information.
#
# ======================================================================

"""Script to run test suite.

Code coverage is not reported because the code tested is actually
within the pyre.mpi module. Furthermore, Pyre runs MPI in a subprocess
which is not measured by coverage.
"""

import unittest
import sys


class TestApp(object):
    """Application to run tests.
    """

    def main(self):
        """
        Run the application.
        """
        sys.path.append("tests/mpi")
        
        success = unittest.TextTestRunner(verbosity=2).run(self._suite()).wasSuccessful()

        if not success:
            sys.exit(1)

    def _suite(self):
        """Setup the test suite.
        """
        import tests.mpi

        suite = unittest.TestSuite()

        test_cases = []
        for mod in [tests.mpi]:
            for test_case in mod.test_cases():
                suite.addTest(unittest.makeSuite(test_case))

        return suite


def configureSubcomponents(facility):
    """Configure subcomponents."""
    for component in facility.components():
        configureSubcomponents(component)
        component._configure()
    return


# ----------------------------------------------------------------------
if __name__ == '__main__':
    TestApp().main()


# End of file

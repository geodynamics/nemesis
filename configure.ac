dnl                                               -*- Autoconf -*-
dnl Process this file with autoconf to produce a configure script.
dnl

AC_PREREQ(2.59)
AC_INIT([nemesis], [2.0.0], [leif@geodynamics.org])
AC_CONFIG_AUX_DIR([./aux-config])
AC_CONFIG_SRCDIR([nemesis.c])
AC_CONFIG_HEADER([config.h])
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE([foreign])

# 'configure' options
AC_ARG_VAR(PYTHON, [Python interpreter])
AC_ARG_VAR(PYTHONPATH, [Python module search path])

# Checks for programs.
AC_PROG_CC([mpicc hcc mpcc mpcc_r mpxlc cmpicc gcc cc cl icc ecc pgcc xlc xlc_r])

# Check for Python.
AM_PATH_PYTHON([3.6])
CIT_PYTHON_CONFIG
CIT_CHECK_PYTHON_HEADER
CIT_CHECK_PYTHON_SHARED

# Check for pythia (which includes mpi).
CIT_PYTHON_MODULE([pythia],[0.9.0])

# Add pythia path to PYTHON_EGG_CPPFLAGS
eval p=`$PYTHON -c "import pythia; print(pythia.__""file__.replace('pythia/__init__.py',''))"`
PYTHON_EGG_CPPFLAGS="-I$p"
AC_SUBST(PYTHON_EGG_CPPFLAGS)

# Checks for libraries.
AC_SEARCH_LIBS([MPI_Init], [mpi mpich], [], [AC_MSG_ERROR([MPI library not found])])

# Checks for header files.
AC_CHECK_HEADER([mpi.h], [], [AC_MSG_ERROR([header 'mpi.h' not found])])

# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.

AC_CONFIG_FILES([Makefile])

AC_OUTPUT

dnl end of configure.ac

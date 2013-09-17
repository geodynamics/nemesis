## Process this file with automake to produce Makefile.in

ACLOCAL_AMFLAGS = -I ./m4

bin_PROGRAMS = nemesis mpinemesis

AM_CPPFLAGS = $(PYTHON_EGG_CPPFLAGS) $(PYTHON_CPPFLAGS)
AM_LDFLAGS = $(PYTHON_LDFLAGS)
LIBS = $(PYTHON_LIBS)

# nemesis (links MPI, but does not initialize it)
nemesis_SOURCES = nemesis.c

# mpinemesis (initializes MPI before starting Python)
mpinemesis_SOURCES = nemesis.c
mpinemesis_CFLAGS = -DUSE_MPI

install-data-hook:
	top_builddir=`$(am__cd) $(top_builddir) && pwd` && \
		cd $(top_srcdir) && \
		$(PYTHON) setup.py install --prefix=$(prefix)

EXTRA_DIST = setup.py

## end of Makefile.am

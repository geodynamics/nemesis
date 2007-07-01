## Process this file with automake to produce Makefile.in

ACLOCAL_AMFLAGS = -I ./m4

bin_PROGRAMS = nemesis mpinemesis

INCLUDES = \
	$(PYTHON_EGG_CPPFLAGS) \
	-I$(PYTHON_INCDIR)


# nemesis (links MPI, but does not initialize it)
nemesis_SOURCES = nemesis.c
nemesis$(EXEEXT): $(nemesis_OBJECTS) $(nemesis_DEPENDENCIES) 
	@rm -f nemesis$(EXEEXT)
	$(LINK) $(PYTHON_LDFLAGS) $(PYTHON_LINKFORSHARED) \
		$(nemesis_LDFLAGS) $(nemesis_OBJECTS) $(nemesis_LDADD) \
		$(PYTHON_EGG_LDFLAGS) \
		$(PYTHON_BLDLIBRARY) \
		$(PYTHON_LIBS) $(PYTHON_MODLIBS) $(PYTHON_SYSLIBS) \
		$(LIBS) \
		$(PYTHON_LDLAST)


# mpinemesis (initializes MPI before starting Python)
mpinemesis_SOURCES = nemesis.c
mpinemesis_CFLAGS = -DUSE_MPI
mpinemesis$(EXEEXT): $(mpinemesis_OBJECTS) $(mpinemesis_DEPENDENCIES) 
	@rm -f mpinemesis$(EXEEXT)
	$(LINK) $(PYTHON_LDFLAGS) $(PYTHON_LINKFORSHARED) \
		$(mpinemesis_LDFLAGS) $(mpinemesis_OBJECTS) $(mpinemesis_LDADD) \
		$(PYTHON_EGG_LDFLAGS) \
		$(PYTHON_BLDLIBRARY) \
		$(PYTHON_LIBS) $(PYTHON_MODLIBS) $(PYTHON_SYSLIBS) \
		$(LIBS) \
		$(PYTHON_LDLAST)


install-data-hook:
	top_builddir=`$(am__cd) $(top_builddir) && pwd` && \
		cd $(top_srcdir) && \
		$(PYTHON) setup.py install_deps -H None -f $$top_builddir/deps --prefix=$(prefix) && \
		$(PYTHON) setup.py egg_info -e $(pythondir)

EXTRA_DIST = setup.py

## end of Makefile.am

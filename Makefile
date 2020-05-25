# This file is part of mce-dev
#
# Copyright © 2005-2009 Nokia Corporation.
#
# Author: David Weinehall <david.weinehall@nokia.com>
# Modified by: Ilya Dogolazky, Tuomo Tanskanen

# ----------------------------------------------------------------------------
# TOP LEVEL TARGETS
# ----------------------------------------------------------------------------

.PHONY: build doc install clean distclean mostlyclean

build::

doc::

install::

mostlyclean::
	$(RM) *.bak *~
	$(RM) mce/include/*.bak mce/include/*~

clean:: mostlyclean

distclean:: clean

# ----------------------------------------------------------------------------
# INSTALL CONFIG
# ----------------------------------------------------------------------------

DESTDIR    ?= /tmp/test-mce-dev

PCDIR      ?= /usr/lib/pkgconfig
INCLUDEDIR := /usr/include/mce

INSTALL_DIR  := install -m 755 -d
INSTALL_DATA := install -m 644


# ----------------------------------------------------------------------------
# FILES TO BUILD / INSTALL
# ----------------------------------------------------------------------------

PCFILE  += mce.pc
INCLUDE_FILES += include/mce/dbus-names.h
INCLUDE_FILES += include/mce/mode-names.h

# ----------------------------------------------------------------------------
# DOCUMENTATION RULES
# ----------------------------------------------------------------------------

doc::	doc/doxygen.log

doc/doxygen.log: $(INCLUDE_FILES) Doxyfile
	mkdir -p doc
	doxygen 1> $@ # stdout=noise stderr=warnings

clean::
	$(RM) -rf doc

# ----------------------------------------------------------------------------
# INSTALL RULES
# ----------------------------------------------------------------------------

install::
	# package config files
	$(INSTALL_DIR) $(DESTDIR)$(PCDIR)
	$(INSTALL_DATA) $(PCFILE) $(DESTDIR)$(PCDIR)/
	# header files
	$(INSTALL_DIR) $(DESTDIR)$(INCLUDEDIR)
	$(INSTALL_DATA) $(INCLUDE_FILES) $(DESTDIR)$(INCLUDEDIR)

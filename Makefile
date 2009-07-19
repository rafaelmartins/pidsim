PREFIX=/usr
DESTDIR=/

PYTHON := $(shell which python)
PWD := $(shell pwd)

PKGNAME := $(shell $(PYTHON) $(PWD)/setup.py --name)
VERSION := $(shell $(PYTHON) $(PWD)/setup.py --version)

all: lib doc
	

lib: clean
	$(PYTHON) setup.py build

doc: clean-doc
	$(MAKE) -C doc

install: all
	$(PYTHON) setup.py install --prefix $(PREFIX) --root $(DESTDIR)

clean: clean-doc
	$(PYTHON) setup.py clean -a

clean-doc:
	$(MAKE) -C doc clean

distclean: clean
	rm -rf $(PWD)/$(PKGNAME)*

tmp-dir: distclean
	mkdir -p /tmp/$(PKGNAME)/files
	mkdir -p /tmp/$(PKGNAME)/dist
	mkdir -p /tmp/$(PKGNAME)/files/$(PKGNAME)-$(VERSION)
	cp -Rf * /tmp/$(PKGNAME)/files/$(PKGNAME)-$(VERSION)
	find /tmp/$(PKGNAME)/files/$(PKGNAME)-$(VERSION) -name *.pyc | xargs rm -rf	
	find /tmp/$(PKGNAME)/files/$(PKGNAME)-$(VERSION) -name .hg | xargs rm -rf

dist: tmp-dir
	cd /tmp/$(PKGNAME)/files && tar -cvjf /tmp/$(PKGNAME)/dist/$(PKGNAME)-$(VERSION).tar.bz2 $(PKGNAME)-$(VERSION)
	cp /tmp/$(PKGNAME)/dist/* $(PWD)
	rm -rf /tmp/$(PKGNAME)

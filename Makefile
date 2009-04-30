PYTHON=`which python`
PWD=`pwd`
PREFIX=/usr
DESTDIR=/
PKGNAME=python-controlsystems
VERSION=0.2

all: clean
	$(PYTHON) setup.py build

install: all
	$(PYTHON) setup.py install --prefix $(PREFIX) --root $(DESTDIR)

clean:
	$(PYTHON) setup.py clean
	rm -rf build/

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

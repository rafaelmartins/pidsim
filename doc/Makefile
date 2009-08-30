EPYDOC := $(shell which epydoc)
PWD := $(shell pwd)

PKGNAME := $(shell $(PYTHON) $(PWD)/../setup.py --name)
VERSION := $(shell $(PYTHON) $(PWD)/../setup.py --version)

PACKAGE := $(PKGNAME)-$(VERSION)

all: clean doc

clean:
	rm -rfv $(PACKAGE)-doc

distclean: clean
	rm -rfv *.tar.gz

doc: clean
	mkdir -p $(PWD)/$(PACKAGE)-doc/{pdf,html,temp}
	$(EPYDOC) --name="$(PACKAGE)" --html --no-frames -o $(PWD)/$(PACKAGE)-doc/html/ $(PWD)/../$(PKGNAME)
	$(EPYDOC) --name="$(PACKAGE)" --pdf -o $(PWD)/$(PACKAGE)-doc/temp/ $(PWD)/../$(PKGNAME)
	mkdir -p $(PWD)/$(PACKAGE)-doc/pdf
	mv $(PWD)/$(PACKAGE)-doc/temp/api.pdf $(PWD)/$(PACKAGE)-doc/pdf/$(PACKAGE).pdf
	rm -rfv $(PWD)/$(PACKAGE)-doc/temp

dist: distclean doc
	tar -cvzf $(PACKAGE)-doc.tar.gz $(PACKAGE)-doc

PACKAGE=controlsystems
NAME=Python Control Systems core package

all: clean doc

clean:
	rm -rfv html pdf

doc:
	epydoc --name="$(NAME)" --html --no-frames -o html/ ../src/$(PACKAGE)
	epydoc --name="$(NAME)" --pdf -o temp/ ../src/$(PACKAGE)
	mkdir -p pdf/
	mv temp/api.pdf pdf/$(PACKAGE).pdf
	rm -rfv temp

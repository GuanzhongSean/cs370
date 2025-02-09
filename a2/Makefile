all:
	rm -f a2.pdf A2Q1.pdf MassSpring.pdf *.zip
	pdflatex a2.tex
	jupyter nbconvert --to notebook --execute --clear-output --inplace A2Q1.ipynb
	jupyter nbconvert --to pdf A2Q1.ipynb
	jupyter nbconvert --to notebook --execute --clear-output --inplace MassSpring.ipynb
	jupyter nbconvert --to pdf MassSpring.ipynb
	zip a2pdf.zip a2.pdf A2Q1.pdf MassSpring.pdf
	zip a2code.zip a2.tex A2Q1.ipynb MassSpring.ipynb

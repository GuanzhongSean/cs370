all:
	rm -f a2.pdf A2Q1.pdf MassSpring.pdf *.zip
	pdflatex a2.tex
	jupyter nbconvert --to notebook --execute --clear-output --inplace A2Q1.ipynb
	jupyter nbconvert --to pdf A2Q1.ipynb
	# jupyter nbconvert --to notebook --execute --clear-output --inplace MassSpring.ipynb
	# jupyter nbconvert --to pdf MassSpring.ipynb
	zip a2pdf.zip a2.pdf A2Q1.pdf MassSpring.pdf -19j
	zip a2code.zip a2.tex A1A2Q1Q5.ipynb MassSpring.ipynb -19j

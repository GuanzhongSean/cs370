all:
	rm -f a1.pdf A1Q5.pdf A1Q6.pdf *.zip
	pdflatex a1.tex
	jupyter nbconvert --to notebook --execute --clear-output --inplace A1Q5.ipynb
	jupyter nbconvert --to pdf A1Q5.ipynb
	jupyter nbconvert --to notebook --execute --clear-output --inplace A1Q6.ipynb
	jupyter nbconvert --to pdf A1Q6.ipynb
	zip a1pdf.zip a1.pdf A1Q5.pdf A1Q6.pdf -19
	zip a1code.zip a1.tex A1Q5.ipynb q5c.png A1Q6.ipynb -19

all:
	rm -f a4.pdf A4Q5.pdf a4*.zip
	pdflatex a4.tex
	jupyter nbconvert --to notebook --execute --clear-output --inplace A4Q5.ipynb
	jupyter nbconvert --to pdf A4Q5.ipynb
	zip a4pdf.zip a4.pdf A4Q5.pdf
	zip a4code.zip a4.tex A4Q5.ipynb bbc.mat

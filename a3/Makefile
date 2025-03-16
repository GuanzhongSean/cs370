all:
	rm -f a3.pdf A3Q5.pdf A3Q6.pdf a3*.zip train_bird.wav
	pdflatex a3.tex
	unzip train_bird.wav.zip
	jupyter nbconvert --to notebook --execute --clear-output --inplace A3Q5.ipynb
	jupyter nbconvert --to pdf A3Q5.ipynb
	jupyter nbconvert --to notebook --execute --clear-output --inplace A3Q6.ipynb
	jupyter nbconvert --to pdf A3Q6.ipynb
	zip a3pdf.zip a3.pdf A3Q5.pdf A3Q6.pdf
	zip a3code.zip a3.tex A3Q5.ipynb A3Q6.ipynb operahall.png train_bird.wav

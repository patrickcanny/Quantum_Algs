make:
	killall TeXShop; latex *.tex; make clean; open *.dvi

clean:
	rm *.out *.log *.aux

edit:
	vi *.tex

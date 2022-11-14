now:
	make test

push:
	git add .
	git commit -a
	git push

test:
	python3 polarMath.py
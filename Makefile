venv-dir := venv

clean:
	find $ . -name '*.py[co]' -delete
	rm -rf $(venv-dir)

dev:
	python3 -m venv $(venv-dir); \
	$(venv-dir)/bin/pip install -r requirements.txt

test:
	$(venv-dir)/bin/py.test src/ --cov=src --cov-report term-missing

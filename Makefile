
.PHONY: compile
compile:
	sass --watch index.scss index.css

.PHONY: serve
serve:
	python3 -m http.server

.PHONY: all
all: compile serve

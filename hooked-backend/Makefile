# Variables
VENV_DIR := venv
PYTHON := python3
PIP := $(VENV_DIR)/bin/pip
FLASK_APP := run.py

# Targets
.PHONY: all setup run clean deps activate

all: setup

# Set up virtual environment and install dependencies
setup: $(VENV_DIR) deps

$(VENV_DIR):
	$(PYTHON) -m venv $(VENV_DIR)

deps: $(PIP)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

$(PIP):
	@echo "Virtual environment not found. Run 'make setup' first."

# Run the Flask app
run: $(VENV_DIR)
	$(VENV_DIR)/bin/flask run

# Activate virtual environment (informative, does not actually activate in the shell)
activate:
	@echo "Run 'source $(VENV_DIR)/bin/activate' to activate the virtual environment."

# Freeze dependencies to requirements.txt
freeze: $(VENV_DIR)
	$(PIP) freeze > requirements.txt

# Clean the project (remove virtual environment)
clean:
	rm -rf $(VENV_DIR)
	rm -rf __pycache__
	rm -rf *.pyc


# 		MAKEFILE README
# make setup 	- Creates venv
# make deps 	- Adds any new dependencies
# make run 		- Runs flask app
# make freeze 	- Updates requirements.txt with installed dependencies
# make clean 	- Removes venv and temp files
# make activate	- Gives command for sourcing venv
# dir and files ################################################################

game_dir             = ./game
venv_dir             = ./.venv

game                 = $(game_dir)/main.py
requirements_file    = $(game_dir)/requirements.txt

# colors #######################################################################

red                  = "\033[0;31m"
green                = "\033[0;32m"
yellow               = "\033[0;33m"
blue                 = "\033[0;34m"
magenta              = "\033[0;35m"
cyan                 = "\033[0;36m"
reset                = "\033[0m"

make_tag             = [$(magenta) MAKE $(reset)]

# commands #####################################################################

echo                 = echo -e $(make_tag)
python               = python3
pip                  = pip3
rm                   = rm -fr

.DEFAULT_GOAL := all

# rules ########################################################################

all: run-database run-game stop-database

run-game: requirements
	@$(echo) "Running game..."
	@$(python) $(game)

requirements:
	@$(echo) "Installing requirements..."
	@$(pip) install --requirement $(requirements_file)

run-database:
	@$(echo) "Running database..."
	@sudo docker-compose up --build --detach

stop-database:
	@$(echo) "Stopping database..."
	@sudo docker-compose down

# venv rules ###################################################################

create-venv:
	@$(echo) "Creating virtual environment..."
	@$(python) -m venv $(venv_dir)

remove-venv:
	@$(echo) "Removing virtual environment..."
	@$(rm) $(venv_dir)

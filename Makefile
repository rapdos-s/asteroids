# directory structure ##########################################################
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
game_tag             = [$(green) GAME $(reset)]
docker_tag             = [$(blue) DOCKER $(reset)]
database_tag         = [$(yellow) DATABASE $(reset)]
venv_tag             = [$(cyan) VENV $(reset)]

# commands #####################################################################
echo                 = echo -e $(make_tag)
docker               = sudo docker
docker-compose       = sudo docker-compose
make                 = make --no-print-directory
python               = python3
pip                  = pip3
rm                   = rm -fr

remove_output        = 2> /dev/null

# default goal #################################################################
.DEFAULT_GOAL := all

# basic rules ##################################################################
.PHONY: all clean fclean re

all:
	@$(echo) "Starting..."
	@$(make) docker_up_detach
	@$(make) game_run
	@$(echo) "All done."

clean:
	@$(echo) "Intermediate clean..."
	@$(make) docker_down
	@$(make) docker_container_stop
	@$(make) game_clean
	@$(echo) "Intermediate clean done."

fclean:
	@$(echo) "Full clean..."
	@$(make) clean
	@$(make) docker_fclean
	@$(make) venv_remove
	@$(echo) "Full clean done."

re:
	@$(echo) "Rebuilding..."
	@$(make) fclean
	@$(make) all
	@$(echo) "Rebuilding done."

# game rules ###################################################################
.PHONY: game_run install_game_requirements game_clean

game_run: install_game_requirements
	@$(echo) $(game_tag) "Running game..."
	@$(python) $(game)
	@$(echo) $(game_tag) "Game finished."

install_game_requirements:
	@$(echo) $(game_tag) "Installing requirements..."
	@$(pip) install --requirement $(requirements_file)
	@$(echo) $(game_tag) "Requirements installed."

game_clean:
	@$(echo) $(game_tag) "Cleaning game cache"
	@find $(game_dir) -type d -name __pycache__ | xargs $(rm)
	@$(echo) $(game_tag) "Game cache cleaned."

# docker rules #################################################################
.PHONY: docker_list docker_fclean
.PHONY: docker_container_list docker_container_stop docker_container_remove
.PHONY: docker_volume_list docker_volume_remove
.PHONY: docker_network_list docker_network_remove
.PHONY: docker_images_list docker_images_remove
.PHONY: docker_build docker_up docker_up_detach docker_down

docker_list: sudo
	@$(echo) $(docker_tag) "Listing all docker objects..."
	@$(make) docker_container_list
	@$(make) docker_volume_list
	@$(make) docker_network_list
	@$(make) docker_images_list
	@$(echo) $(docker_tag) "Docker objects listing done."

docker_fclean: sudo
	@$(echo) $(docker_tag) "Removing all docker objects..."
	@$(make) docker_container_remove
	@$(make) docker_volume_remove
	@$(make) docker_network_remove
	@$(make) docker_images_remove
	@$(echo) $(docker_tag) "Docker objects remove done."

docker_container_list: sudo
	@$(echo) $(docker_tag) "Listing containers..."
	@$(docker-compose) ps --all
	@$(echo) $(docker_tag) "Containers listing done."

docker_container_stop: sudo
	@$(echo) $(docker_tag) "Stopping all containers..."
	@$(docker-compose) stop
	@$(echo) $(docker_tag) "Containers stopped."

docker_container_remove: sudo
	@$(echo) $(docker_tag) "Removing all containers..."
	@$(docker) ps --all --quiet | \
		grep --quiet . && \
		$(docker) container rm --force $$($(docker) ps --all --quiet) || \
		$(echo) $(docker_tag) "No containers to remove."
	@$(echo) $(docker_tag) "Containers remove done."

docker_volume_list: sudo
	@$(echo) $(docker_tag) "Listing all volumes..."
	@$(docker) volume ls
	@$(echo) $(docker_tag) "Volumes listing done."

docker_volume_remove: sudo
	@$(echo) $(docker_tag) "Removing all volumes..."
	@$(docker) volume ls --quiet | \
		grep --quiet . && \
		$(docker) volume rm $$($(docker) volume ls --quiet) || \
		$(echo) $(docker_tag) "No volumes to remove."
	@$(echo) $(docker_tag) "Volumes remove done."

docker_network_list: sudo
	@$(echo) $(docker_tag) "Listing all networks..."
	@$(docker) network ls
	@$(echo) $(docker_tag) "Networks listing done."

docker_network_remove: sudo
	@$(echo) $(docker_tag) "Removing all networks..."
	@$(docker) network ls --format "{{.Name}}" | \
		grep --invert-match --extended-regexp "bridge|host|none" | \
		xargs $(docker) network rm --force $(remove_output) && \
		$(echo) $(docker_tag) "All networks removed." || \
		$(echo) $(docker_tag) "No networks to remove."
	@$(echo) $(docker_tag) "Networks remove done."

docker_images_list: sudo
	@$(echo) $(docker_tag) "Listing all images..."
	@$(docker) images
	@$(echo) $(docker_tag) "Images listing done."

docker_images_remove: sudo
	@$(echo) $(docker_tag) "Removing all images..."
	@$(docker) images --quiet | \
		grep --quiet . && \
		$(docker) rmi --force $$($(docker) images --quiet) || \
		$(echo) $(docker_tag) "No images to remove."
	@$(echo) $(docker_tag) "Images remove done."

docker_build: sudo
	@$(echo) $(docker_tag) "Building docker containers..."
	@$(docker-compose) build
	@$(echo) $(docker_tag) "Docker containers built."

docker_up: sudo docker_build
	@$(echo) $(docker_tag) "Starting docker containers..."
	@$(docker-compose) up
	@$(echo) $(docker_tag) "Docker containers started."

docker_up_detach: sudo docker_build
	@$(echo) $(docker_tag) "Starting docker containers..."
	@$(docker-compose) up --detach
	@$(echo) $(docker_tag) "Docker containers started."

docker_down: sudo
	@$(echo) $(docker_tag) "Stopping docker containers..."
	@$(docker-compose) down
	@$(echo) $(docker_tag) "Docker containers stopped."

# venv rules ###################################################################
.PHONY: venv_create venv_remove

venv_create:
	@$(echo) $(venv_tag) "Creating virtual environment..."
	@$(python) -m venv $(venv_dir)
	@$(echo) $(venv_tag) "Virtual environment created."

venv_remove:
	@$(echo) $(venv_tag) "Removing virtual environment..."
	@$(rm) $(venv_dir)
	@$(echo) $(venv_tag) "Virtual environment removed."

# tools rules ##################################################################
.PHONY: sudo lsof

sudo:
	@$(echo) "Requesting sudo..."
	@sudo true
	@$(echo) "Sudo granted."

lsof: sudo
	@$(echo) "Listing processes using port 5432..."
	@sudo lsof -i :5432 || true

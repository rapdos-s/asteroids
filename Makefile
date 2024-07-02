# directory structure ##########################################################
airbyte_dir          = ./airbyte
clickhouse_dir       = ./clickhouse
game_dir             = ./game
metabase_dir         = ./metabase
metabase_plugins_dir = $(metabase_dir)/metabase-plugins
postgres_dir         = ./postgres

airbyte_compose      = $(airbyte_dir)/docker-compose.yaml
clickhouse_compose   = $(clickhouse_dir)/docker-compose.yml
metabase_compose     = $(metabase_dir)/docker-compose.yml
postgres_compose     = $(postgres_dir)/docker-compose.yml

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
docker_tag           = [$(blue) DOCKER $(reset)]
database_tag         = [$(yellow) DATABASE $(reset)]

# commands #####################################################################
docker               = sudo docker
docker-compose       = sudo docker-compose
echo                 = /usr/bin/echo -e $(make_tag)
make                 = make --no-print-directory
pip                  = pip3
python               = python3
rm                   = rm -fr

remove_output        = 2> /dev/null
keep_on_error        = || true

# default goal #################################################################
.DEFAULT_GOAL        = all

# basic rules ##################################################################
.PHONY: all clean fclean re

all:
	@$(echo) "Starting..."
	@$(make) kill_postgres
	@$(make) create_network
	@$(make) docker_postgres_up_detach
	@$(make) docker_airbyte_up_detach
	@$(make) docker_clickhouse_up_detach
	@$(make) docker_metabase_up_detach
	@$(make) game_run
	@$(echo) "All done."

clean:
	@$(echo) "Intermediate clean..."
	@$(make) docker_container_stop
	@$(make) game_clean
	@$(echo) "Intermediate clean done."

fclean:
	@$(echo) "Full clean..."
	@$(make) clean
	@$(make) docker_fclean
	@$(make) kill_postgres
	@$(echo) "Full clean done."

re:
	@$(echo) "Rebuilding..."
	@$(make) fclean
	@$(make) all
	@$(echo) "Rebuilding done."

# docker rules #################################################################
.PHONY: docker_list docker_fclean
.PHONY: docker_container_list docker_container_stop docker_container_remove
.PHONY: docker_volume_list docker_volume_remove
.PHONY: docker_network_list docker_network_remove
.PHONY: docker_images_list docker_images_remove

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
	@$(docker) ps --all
	@$(echo) $(docker_tag) "Containers listing done."

docker_container_stop: sudo
	@$(echo) $(docker_tag) "Stopping all containers..."
	@if $(docker) ps --all --quiet | grep --quiet .; then \
		$(docker) stop $$($(docker) ps --all --quiet); \
		$(echo) $(docker_tag) "Containers stopped."; \
	else \
		$(echo) $(docker_tag) "No containers to stop."; \
	fi

docker_container_remove: sudo
	@$(echo) $(docker_tag) "Removing all containers..."
	@if $(docker) ps --all --quiet | grep --quiet .; then \
		$(docker) rm --force $$($(docker) ps --all --quiet); \
		$(echo) $(docker_tag) "Containers removed."; \
	else \
		$(echo) $(docker_tag) "No containers to remove."; \
	fi

docker_volume_list: sudo
	@$(echo) $(docker_tag) "Listing all volumes..."
	@$(docker) volume ls
	@$(echo) $(docker_tag) "Volumes listing done."

docker_volume_remove: sudo
	@$(echo) $(docker_tag) "Removing all volumes..."
	@if $(docker) volume ls --quiet | grep --quiet .; then \
		$(docker) volume rm --force $$($(docker) volume ls --quiet); \
		$(echo) $(docker_tag) "Volumes removed."; \
	else \
		$(echo) $(docker_tag) "No volumes to remove."; \
	fi

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
	@if $(docker) images --quiet | grep --quiet .; then \
		$(docker) rmi --force $$($(docker) images --quiet); \
		$(echo) $(docker_tag) "Images removed."; \
	else \
		$(echo) $(docker_tag) "No images to remove."; \
	fi

# postgres rules ###############################################################
.PHONY: docker_postgres_build docker_postgres_up docker_postgres_up_detach

docker_postgres_build: sudo
	@$(echo) $(docker_tag) "Building postgres container..."
	@$(docker-compose) --file $(postgres_compose) build
	@$(echo) $(docker_tag) "Postgres container built."

docker_postgres_up: sudo docker_postgres_build
	@$(echo) $(docker_tag) "Starting postgres container..."
	@$(docker-compose) --file $(postgres_compose) up
	@$(echo) $(docker_tag) "Postgres container started."

docker_postgres_up_detach: sudo docker_postgres_build
	@$(echo) $(docker_tag) "Starting postgres container in detached mode..."
	@$(docker-compose) --file $(postgres_compose) up --detach
	@$(echo) $(docker_tag) "Postgres container started."

docker_postgres_down: sudo
	@$(echo) $(docker_tag) "Stopping postgres container..."
	@$(docker-compose) --file $(postgres_compose) down
	@$(echo) $(docker_tag) "Postgres container stopped."

docker_postgres_stop: sudo
	@$(echo) $(docker_tag) "Stopping postgres container..."
	@$(docker-compose) --file $(postgres_compose) stop
	@$(echo) $(docker_tag) "Postgres container stopped."

# airbyte rules ################################################################
.PHONY: docker_airbyte_build docker_airbyte_up docker_airbyte_up_detach

docker_airbyte_build: sudo
	@$(echo) $(docker_tag) "Building airbyte container..."
	@$(docker-compose) --file $(airbyte_compose) build
	@$(echo) $(docker_tag) "Airbyte container built."

docker_airbyte_up: sudo docker_airbyte_build
	@$(echo) $(docker_tag) "Starting airbyte container..."
	@$(docker-compose) --file $(airbyte_compose) up
	@$(echo) $(docker_tag) "Airbyte container started."

docker_airbyte_up_detach: sudo docker_airbyte_build
	@$(echo) $(docker_tag) "Starting airbyte container in detached mode..."
	@$(docker-compose) --file $(airbyte_compose) up --detach
	@$(echo) $(docker_tag) "Airbyte container started."

docker_airbyte_down: sudo
	@$(echo) $(docker_tag) "Stopping airbyte container..."
	@$(docker-compose) --file $(airbyte_compose) down
	@$(echo) $(docker_tag) "Airbyte container stopped."

docker_airbyte_stop: sudo
	@$(echo) $(docker_tag) "Stopping airbyte container..."
	@$(docker-compose) --file $(airbyte_compose) stop
	@$(echo) $(docker_tag) "Airbyte container stopped."

# clickhouse rules #############################################################
.PHONY: docker_clickhouse_build docker_clickhouse_up docker_clickhouse_up_detach

docker_clickhouse_build: sudo
	@$(echo) $(docker_tag) "Building clickhouse container..."
	@$(docker-compose) --file $(clickhouse_compose) build
	@$(echo) $(docker_tag) "Clickhouse container built."

docker_clickhouse_up: sudo docker_clickhouse_build
	@$(echo) $(docker_tag) "Starting clickhouse container..."
	@$(docker-compose) --file $(clickhouse_compose) up
	@$(echo) $(docker_tag) "Clickhouse container started."

docker_clickhouse_up_detach: sudo docker_clickhouse_build
	@$(echo) $(docker_tag) "Starting clickhouse container in detached mode..."
	@$(docker-compose) --file $(clickhouse_compose) up --detach
	@$(echo) $(docker_tag) "Clickhouse container started."

docker_clickhouse_down: sudo
	@$(echo) $(docker_tag) "Stopping clickhouse container..."
	@$(docker-compose) --file $(clickhouse_compose) down
	@$(echo) $(docker_tag) "Clickhouse container stopped."

docker_clickhouse_stop: sudo
	@$(echo) $(docker_tag) "Stopping clickhouse container..."
	@$(docker-compose) --file $(clickhouse_compose) stop
	@$(echo) $(docker_tag) "Clickhouse container stopped."

# metabase rules ###############################################################
.PHONY: docker_metabase_build docker_metabase_up docker_metabase_up_detach

docker_metabase_build: sudo metabase_permissions
	@$(echo) $(docker_tag) "Building metabase container..."
	@$(docker-compose) --file $(metabase_compose) build
	@$(echo) $(docker_tag) "Metabase container built."

docker_metabase_up: sudo docker_metabase_build
	@$(echo) $(docker_tag) "Starting metabase container..."
	@$(docker-compose) --file $(metabase_compose) up
	@$(echo) $(docker_tag) "Metabase container started."

docker_metabase_up_detach: sudo docker_metabase_build
	@$(echo) $(docker_tag) "Starting metabase container in detached mode..."
	@$(docker-compose) --file $(metabase_compose) up --detach
	@$(echo) $(docker_tag) "Metabase container started."

docker_metabase_down: sudo
	@$(echo) $(docker_tag) "Stopping metabase container..."
	@$(docker-compose) --file $(metabase_compose) down
	@$(echo) $(docker_tag) "Metabase container stopped."

docker_metabase_stop: sudo
	@$(echo) $(docker_tag) "Stopping metabase container..."
	@$(docker-compose) --file $(metabase_compose) stop
	@$(echo) $(docker_tag) "Metabase container stopped."

metabase_permissions: sudo
	@$(echo) "Setting permissions..."
	@sudo chown -R 2000:2000 $(metabase_plugins_dir)
	@sudo chmod -R 777 $(metabase_plugins_dir)
	@$(echo) "Permissions set."

# game rules ###################################################################
.PHONY: game_run install_game_requirements game_clean

quick_run:
	@$(echo) "Starting..."
	@$(make) kill_postgres
	@$(make) create_network
	@$(make) docker_postgres_up_detach
	@$(make) game_run
	@$(echo) "All done."

game_run:
	@$(make) install_game_requirements
	@$(make) sleep
	@$(echo) $(game_tag) "Running game..."
	@$(python) $(game)
	@$(echo) $(game_tag) "Game finished."

install_game_requirements:
	@$(echo) $(game_tag) "Installing requirements..."
	@$(pip) install --quiet --requirement $(requirements_file)
	@$(echo) $(game_tag) "Requirements installed."

game_clean:
	@$(echo) $(game_tag) "Cleaning game cache"
	@find $(game_dir) -type d -name __pycache__ | xargs $(rm)
	@$(echo) $(game_tag) "Game cache cleaned."

# tools rules ##################################################################
.PHONY: sudo lsof kill_postgres sleep

sudo:
	@$(echo) "Requesting sudo..."
	@sudo true
	@$(echo) "Sudo granted."

lsof: sudo
	@$(echo) "Listing processes using port 5432..."
	@sudo lsof -i :5432 $(keep_on_error)
	@$(echo) "Processes listed."

kill_postgres: sudo
	@$(echo) "Killing postgres processes..."
	@sudo lsof -t -i:5432 | \
		grep --invert-match PID | \
		xargs --no-run-if-empty sudo kill -9
	@$(echo) "Postgres processes killed."

sleep:
	@/usr/bin/echo -n -e $(make_tag) "☕ Making coffee"
	@for i in {1..5}; do \
		/usr/bin/echo -n "."; \
		sleep 1; \
	done
	@/usr/bin/echo " Done!"

create_network:
	@$(echo) "Creating network..."
	@$(docker) network create services-network $(keep_on_error)
	@$(echo) "Network created."

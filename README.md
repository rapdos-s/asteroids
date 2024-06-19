## Mandatory
- [X] Control Spaceship
- [ ] Asteroids moves
- [ ] Collision Detection
- [ ] Score during gameplay
- [ ] Player Achievements
- [ ] Score list
- [ ] Store players score

## Bonus
- [ ] Sanityze inputs
- [ ] Flexibility (?)
- [ ] Persistence (?)

## Environment
- [X] venv

## Frontend: Python (Pygame)
- [X] Loop
  - [ ] Sistema de menu
    - [ ] Play
    - [ ] Leaderboard
    - [ ] Profile
    - [ ] Logout
    - [ ] Quit
  - [X] Especific fps
  - [X] Controls
    - [X] Rotation
    - [X] Impulse
    - [ ] Shoot
  - [ ] Main Menu
    - [ ] Play
    - [ ] Leaderboard

## Backend: Python (psycopg2)
  - [ ] Collision

## Database: PostgreSQL
- [ ] tables
  - [ ] players
    - [ ] id
    - [ ] player_name
  - [ ] leaderboard
    - [ ] id
    - [ ] player_id
    - [ ] score
    - [ ] date (timestamp)
  - [ ] score_history
    - [ ] id
    - [ ] player_id
    - [ ] score
    - [ ] date
  - [ ] achievements 
    - [ ] id
    - [ ] achievement_name
    - [ ] description
  - [ ] player_achievements
    - [ ] player_id
    - [ ] achievement_id
    - [ ] date_earned (timestamp)

- [ ] Documentar


## Running

Setup venv
```sh
python3 -m venv venv
```

Active venv
```sh
source venv/bin/activate
```

Install venv
```sh
pip3 install --requirement requirements.txt
```

Deactive venv
```sh
deactivate
```

Remove venv
```sh
rm -fr venv
```

Install database
```sh
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib -y
```

Enable and init Database
```sh
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

Check database service status
```sh
sudo systemctl status postgresql
```

Entering database
```sh
sudo -i -u postgres
```

# Acessar o PostgreSQL como superusuário
sudo -u postgres psql

Exiting Database
```sh
exit
```

CLosing database service
```sh
sudo systemctl stop postgresql
```

Criando novo banco de dados


# Criar um novo banco de dados
CREATE DATABASE db_asteroids;

# Criar um novo usuário com senha
CREATE USER marvin WITH ENCRYPTED PASSWORD 'F0rty_Tw0';

# Dar ao novo usuário permissões para o novo banco de dados
GRANT ALL PRIVILEGES ON DATABASE db_asteroids TO marvin;


Ideias para versão 2.0
Pausa
A velocidade dos asteroids aumenta conforme o tempo de jogo decorrido
Trocar macros de estados por enum

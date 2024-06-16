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
    - [ ] Highscore
    - [ ] Profile
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
  - [ ] high_scores
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

Ideias para versão 2.0
Pausa
Nave aparece do outro lado de forma mais orgânica

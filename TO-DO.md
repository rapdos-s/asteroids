## TO-DO
- [x] Limpar e organizar o .gitignore
- [ ] Configurar ambiente de banco de dados e jogo
  - [ ] Banco de dados: postgreeSQL: ???
  - [ ] Jogo: python: ???
- [ ] Criar usuário no database (marvin)
- [ ] Resolver bug de saída da tela
- [ ] Criar modal de conquistas
- [ ] CRUDs

- [ ] Criar arquivo config.py
- [ ] Store players score
- [ ] Score list
- [ ] Player Achievements

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
  - [ ] Equipe envolvida
  - [ ] Apresentação do projeto
  - [ ] Tecnologias usadas
  - [ ] Como rodar
  - [ ] Como jogar


## Requirements
psycopg2-binary
pygame
python-dotenv

## Perfis (Limite de 8 caracteres para o nome)
SAVE 01: KAREN    420000
SAVE 02: CAIO     42000
SAVE 03: TUCA     4200
SAVE 04: MARVIM   42

SAVE 05: FERNAO   123321
SAVE 06: FERNANDA 123213
SAVE 07: LUCAS    123231
SAVE 08: KIM      123313
SAVE 09: MARCEL   123123
SAVE 10: MAURICIO 123132

SAVE 11: DMOREIRA 0
SAVE 12: LUIZEDUA 0
SAVE 13: LUMEDEIR 0
SAVE 14: RAPDOS-S 0

## Conquistas:
???: Jogar 1 vez
???: 1000 Pontos
???: 10000 Pontos
???: 42000 Pontos
???: Destrua 10 asteroids
???: Destrua 100 asteroids
???: Destrua 1000 asteroids

## Anotações docker / database
sudo docker run --name "asteroid-database" -e POSTGRES_PASSWORD="F0rty_Tw0" -e POSTGRES_DB="db_asteroids" -p 9090:5432 -v data:/var/lib/postgresql/data -d postgres

sudo docker exec -it "asteroid-database" psql -U postgres -d "db_asteroids"

sudo docker stop "asteroid-database"
sudo docker rm "asteroid-database"
sudo docker volume rm data
sudo docker rmi postgres

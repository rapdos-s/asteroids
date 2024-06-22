<!-- Equipe envolvida ------------------------------------------------------ -->
<!-- Apresentação do projeto ----------------------------------------------- -->
<!-- Tecnologias usadas ---------------------------------------------------- -->
<!-- Como rodar ------------------------------------------------------------ -->
<!-- Como jogar ------------------------------------------------------------ -->


<!-- old ------------------------------------------------------------------- -->

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



## Jogo

Explicação básica do asteroids

### Controles
w ou seta apra cima impulsiona a nave
a ou seta para esquerda, gira em sentido anti-horário
d ou seta para direita, gira em sentido horário
Tecla 1 liga o debug

## Banco de dados
Colocar estrutura das tabelas
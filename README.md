# Asteroids

<!-- Apresentação do projeto ----------------------------------------------- -->
Este projeto visa recriar o clássico jogo Asteroids utilizando Python para o frontend e backend, e PostgreSQL para armazenamento de dados. Adicionalmente, será implementado um sistema ELT (Extract, Load, Transform) para manipulação e análise dos dados do jogo, utilizando Airbyte para coleta, ClickHouse para armazenamento e Metabase para visualização.

<!-- Tecnologias usadas ---------------------------------------------------- -->
- Docker
    - Objetivo: O Docker foi utilizado para facilitar a configuração e a execução de um ambiente consistente e isolado.
- Python
    - Objetivo: Implementar o frontend e backend do jogo Asteroids.
    - Biblioteca Utilizada: Pygame, que oferece funcionalidades para desenvolvimento de jogos em Python.
- Postrgres
    - Objetivo: Armazenar dados do jogo Asteroids Estrutura do Banco de Dados:
        - players: Informações sobre cada jogador.
        - Pontuações mais altas com timestamp.
        - score_history: Histórico de pontuações por jogador.
        - achievements: Diferentes conquistas disponíveis.
        - player_achievements: Registro de conquistas obtidas por cada jogador.
    - Uso de Psycopg2: Biblioteca Python para interação com o PostgreSQL.
- Airbyte
    - Função: Coletar dados do PostgreSQL do sistema Asteroids.
    - Configuração: Configurar Airbyte para extrair dados do PostgreSQL e carregar no ClickHouse.
- ClickHouse
    - Função: Armazenar os dados coletados pelo Airbyte.
    - Configuração: Configurar ClickHouse para receber dados do Airbyte e criar views para análise.
        - DBeaver: Utilize o DBeaver para facilitar a interação com o ClickHouse.
- Metabase
    - Função: Criar visualizações dos dados armazenados no ClickHouse.
    - Configuração: Configurar Metabase para se conectar ao ClickHouse e criar dashboards com visualizações dos dados.

<!-- Como rodar ------------------------------------------------------------ -->
### Como rodar?

#### O que precisa para rodar: 
- `make`: Gerencia os scripts para para execução dos containers e jogo;
- `docker`: Para executar as ferramentas de limpeza, listagem e remoção de containers;
- `docker-compose`: Para subir os containers;
- `python3`: Para rodar o jogo;
- `pip3`: Para instalar as dependências do jogo;
- `lsof`: Para verificar se a porta 5432 está ocupada;

Sabe o Make? É ele mesmo que roda essa bagaça, basta você digitar "make quick_run" no terminal (na raiz do repositório) que o jogo irá abrir.

<!-- Como jogar ------------------------------------------------------------ -->

### Como jogar?
**Setas** ou **WASD** é pra mover a nave.

**Espaço** pra atirar nos asteroids.

 - Destrua asteroids e sobreviva por bastante tempo para ganhar pontos e ficar entre os top 5 jogadores com maior pontuação!
 - Não seja atingido!

<!-- Futuras Implementações ------------------------------------------------ -->

### Ideias para versão 2.0
- Fazer com que o jogo pause;
- A velocidade dos asteroids aumenta conforme o tempo de jogo decorrido;
- Trocar macros de estados por enum;
- Melhorar as telas Profile e Leaderboard;
- Receber dano ao tocar nos asteroids ao invés de morrer instantaneamente.

<!-- Equipe envolvida ------------------------------------------------------ -->

## Quem é a equipe?

- Luiza Medeiros

- Raphael dos Santos

### Agradecimentos especiais

- Davi Moreira
- Luiz Eduardo
- Jchoi

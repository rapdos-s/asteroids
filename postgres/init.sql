-- Criação da tabela players
CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    player_name VARCHAR(100) NOT NULL
);

-- Criação da tabela leaderboard
CREATE TABLE leaderboard (
    id SERIAL PRIMARY KEY,
    player_id INT NOT NULL,
    score INT NOT NULL,
    date TIMESTAMP NOT NULL,
    FOREIGN KEY (player_id) REFERENCES players (id) ON DELETE CASCADE
);

-- Criação da tabela score_history
CREATE TABLE score_history (
    id SERIAL PRIMARY KEY,
    player_id INT NOT NULL,
    score INT NOT NULL,
    date TIMESTAMP NOT NULL,
    FOREIGN KEY (player_id) REFERENCES players (id) ON DELETE CASCADE
);

-- Criação da tabela achievements
CREATE TABLE achievements (
    id SERIAL PRIMARY KEY,
    achievement_name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL
);

-- Criação da tabela player_achievements
CREATE TABLE player_achievements (
    player_id INT NOT NULL,
    achievement_id INT NOT NULL,
    date_earned TIMESTAMP NOT NULL,
    PRIMARY KEY (player_id, achievement_id),
    FOREIGN KEY (player_id) REFERENCES players (id) ON DELETE CASCADE,
    FOREIGN KEY (achievement_id) REFERENCES achievements (id) ON DELETE CASCADE
);
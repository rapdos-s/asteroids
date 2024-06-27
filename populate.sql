-- players table
INSERT INTO players (player_name) VALUES ('MARVIN');
INSERT INTO players (player_name) VALUES ('KAREN');
INSERT INTO players (player_name) VALUES ('CAIO');
INSERT INTO players (player_name) VALUES ('TUCA');
INSERT INTO players (player_name) VALUES ('DENISE');
INSERT INTO players (player_name) VALUES ('FERNAO');
INSERT INTO players (player_name) VALUES ('FERNANDA');
INSERT INTO players (player_name) VALUES ('LUCAS');
INSERT INTO players (player_name) VALUES ('KIM');
INSERT INTO players (player_name) VALUES ('MARCEL');
INSERT INTO players (player_name) VALUES ('MAURICIO');

-- leaderboard table
INSERT INTO leaderboard (player_id, score, date) VALUES (1, 100, '2021-01-01 00:00:00');
INSERT INTO leaderboard (player_id, score, date) VALUES (2, 200, '2021-01-01 00:00:00');
INSERT INTO leaderboard (player_id, score, date) VALUES (3, 300, '2021-01-01 00:00:00');
INSERT INTO leaderboard (player_id, score, date) VALUES (4, 400, '2021-01-01 00:00:00');
INSERT INTO leaderboard (player_id, score, date) VALUES (5, 500, '2021-01-01 00:00:00');
INSERT INTO leaderboard (player_id, score, date) VALUES (6, 600, '2021-01-01 00:00:00');
INSERT INTO leaderboard (player_id, score, date) VALUES (7, 700, '2021-01-01 00:00:00');
INSERT INTO leaderboard (player_id, score, date) VALUES (8, 800, '2021-01-01 00:00:00');
INSERT INTO leaderboard (player_id, score, date) VALUES (9, 900, '2021-01-01 00:00:00');
INSERT INTO leaderboard (player_id, score, date) VALUES (10, 1000, '2021-01-01 00:00:00');

-- score_history table
INSERT INTO score_history (player_id, score, date) VALUES (1, 100, '2021-01-01 00:00:00');
INSERT INTO score_history (player_id, score, date) VALUES (2, 200, '2021-01-01 00:00:00');
INSERT INTO score_history (player_id, score, date) VALUES (3, 300, '2021-01-01 00:00:00');
INSERT INTO score_history (player_id, score, date) VALUES (4, 400, '2021-01-01 00:00:00');
INSERT INTO score_history (player_id, score, date) VALUES (5, 500, '2021-01-01 00:00:00');
INSERT INTO score_history (player_id, score, date) VALUES (6, 600, '2021-01-01 00:00:00');
INSERT INTO score_history (player_id, score, date) VALUES (7, 700, '2021-01-01 00:00:00');
INSERT INTO score_history (player_id, score, date) VALUES (8, 800, '2021-01-01 00:00:00');
INSERT INTO score_history (player_id, score, date) VALUES (9, 900, '2021-01-01 00:00:00');
INSERT INTO score_history (player_id, score, date) VALUES (10, 1000, '2021-01-01 00:00:00');

-- achievements table
INSERT INTO achievements (achievement_name, description) VALUES ('FIRST_SCORE', 'First score of the player');
INSERT INTO achievements (achievement_name, description) VALUES ('TOP_10', 'Player is in the top 10');
INSERT INTO achievements (achievement_name, description) VALUES ('TOP_5', 'Player is in the top 5');
INSERT INTO achievements (achievement_name, description) VALUES ('TOP_3', 'Player is in the top 3');
INSERT INTO achievements (achievement_name, description) VALUES ('TOP_1', 'Player is the top 1');

-- player_achievements table
INSERT INTO player_achievements (player_id, achievement_id, date_earned) VALUES (1, 1, '2021-01-01 00:00:00');
INSERT INTO player_achievements (player_id, achievement_id, date_earned) VALUES (2, 1, '2021-01-01 00:00:00');
INSERT INTO player_achievements (player_id, achievement_id, date_earned) VALUES (3, 1, '2021-01-01 00:00:00');
INSERT INTO player_achievements (player_id, achievement_id, date_earned) VALUES (4, 1, '2021-01-01 00:00:00');
INSERT INTO player_achievements (player_id, achievement_id, date_earned) VALUES (5, 1, '2021-01-01 00:00:00');
INSERT INTO player_achievements (player_id, achievement_id, date_earned) VALUES (6, 1, '2021-01-01 00:00:00');
INSERT INTO player_achievements (player_id, achievement_id, date_earned) VALUES (7, 1, '2021-01-01 00:00:00');
INSERT INTO player_achievements (player_id, achievement_id, date_earned) VALUES (8, 1, '2021-01-01 00:00:00');
INSERT INTO player_achievements (player_id, achievement_id, date_earned) VALUES (9, 1, '2021-01-01 00:00:00');
INSERT INTO player_achievements (player_id, achievement_id, date_earned) VALUES (10, 1, '2021-01-01 00:00:00');

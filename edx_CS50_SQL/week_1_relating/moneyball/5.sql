SELECT DISTINCT "teams"."name"
FROM "performances" JOIN "teams" ON "teams"."id" = "performances"."team_id"
JOIN "players" ON "players"."id" = "performances"."player_id"
WHERE "players"."first_name" = 'Satchel' AND "players"."last_name" = 'Paige';

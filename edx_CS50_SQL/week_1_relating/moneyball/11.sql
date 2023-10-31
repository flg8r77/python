SELECT "players"."first_name", "players"."last_name", "salaries"."salary"/"performances"."H" AS 'dollars per hit'
From "players"
JOIN "salaries" ON "players"."id" = "salaries"."player_id"
JOIN "performances" ON "performances"."player_id" = "players"."id" AND "salaries"."year" = "performances"."year"
WHERE "performances"."H" > 0 AND "performances"."year" = 2001
ORDER BY "dollars per hit" ASC, "players"."first_name", "players"."last_name" LIMIT 10;

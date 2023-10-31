SELECT "players"."first_name", "players"."last_name", "salaries"."salary"
FROM "players" JOIN "salaries" on "players"."id" = "salaries"."player_id"
WHERE "salaries"."year" = 2001
ORDER BY "salary" ASC, "first_name", "last_name", "players"."id"
LIMIT 50;

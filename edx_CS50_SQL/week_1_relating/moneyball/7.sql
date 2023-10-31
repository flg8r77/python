SELECT "first_name", "last_name"
FROM "players"
JOIN "salaries" on "players"."id" = "salaries"."player_id"
ORDER BY "salaries"."salary" DESC
LIMIT 1;

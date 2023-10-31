SELECT "year", "salary" FROM "salaries" JOIN "players" on "salaries"."player_id" = "players"."id"
WHERE "first_name" = 'Cal' AND "last_name" LIKE '%Ripken%'
ORDER BY "year" DESC;

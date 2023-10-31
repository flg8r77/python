SELECT "performances"."year", "performances"."HR" FROM
"performances" JOIN "players" on "performances"."player_id" = "players"."id"
WHERE "first_name" = "Ken" AND "last_name" LIKE '%Griffey%' AND "birth_year" = 1969
ORDER BY "year" DESC;

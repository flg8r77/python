SELECT "salary"
FROM "players"
JOIN "salaries" ON "players"."id" = "salaries"."player_id"
JOIN "performances" ON "players"."id" = "performances"."player_id"
WHERE "performances"."year" = 2001 AND "performances"."HR" = (
    SELECT MAX("performances"."HR") FROM "performances" WHERE "performances"."year" = 2001
) AND "salaries"."year" = 2001;

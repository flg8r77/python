SELECT "schools"."name", "expenditures"."per_pupil_expenditure", "graduation_rates"."graduated", "staff_evaluations"."unsatisfactory"
FROM "schools"
JOIN "expenditures" ON "schools"."district_id" = "expenditures"."district_id"
JOIN "graduation_rates" ON "schools"."id" = "graduation_rates"."school_id"
JOIN "staff_evaluations" ON "schools"."district_id" = "staff_evaluations"."district_id"
WHERE "graduated" < (
    SELECT AVG("graduated") FROM "graduation_rates"
)
AND "unsatisfactory" > (
    SELECT AVG("unsatisfactory") FROM "staff_evaluations"
)
ORDER BY "per_pupil_expenditure" DESC, "graduated" DESC
;

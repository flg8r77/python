SELECT "districts"."name", "expenditures"."per_pupil_expenditure", "staff_evaluations"."exemplary"
FROM "districts" JOIN "expenditures" on "districts"."id" = "expenditures"."district_id"
JOIN "staff_evaluations" on "districts"."id" = "staff_evaluations"."district_id"
WHERE "per_pupil_expenditure" > (
    SELECT AVG("per_pupil_expenditure") FROM "expenditures")
AND "exemplary" > (
    SELECT AVG("exemplary") FROM "staff_evaluations")
AND "districts"."type" != 'Charter District'
ORDER BY "exemplary" DESC, "per_pupil_expenditure" DESC;

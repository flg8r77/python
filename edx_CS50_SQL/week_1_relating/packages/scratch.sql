SELECT *, COUNT("address_id") AS "undisclosed deliveries" FROM "scans" WHERE "package_id" IN (
    SELECT "id" FROM "packages" WHERE "contents" = 'Undisclosed')
AND "action" = 'Drop'
GROUP BY "address_id"
ORDER BY "undisclosed deliveries" DESC;

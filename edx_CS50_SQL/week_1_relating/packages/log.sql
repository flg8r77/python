
-- *** The Lost Letter ***

-- Package Id based on FROM and TO address given, lets think of this as query1
-- Seems there is typo Finne vs Finni in the delivery address, so we use LIKE to capture the pattern instead
SELECT "id" FROM "packages" WHERE "from_address_id" = (
    SELECT "id" FROM "addresses" WHERE "address" = '900 Somerville Avenue')
AND "to_address_id" = (
    SELECT "id" FROM "addresses" WHERE "address" LIKE '%2 Fin%')
;
-- Now we can use the above query1 as a subquery, to query the scans table and see the address_id of where the lost letter got delivered
-- Lets call this query2
SELECT "address_id" FROM "scans" WHERE "package_id" = (
    SELECT "id" FROM "packages" WHERE "from_address_id" = (
        SELECT "id" FROM "addresses" WHERE "address" = '900 Somerville Avenue')
    AND "to_address_id" = (
        SELECT "id" FROM "addresses" WHERE "address" LIKE '%2 Fin%')
) AND "action" = 'Drop';

-- Finally we can use query2 as a nested query to look up info about the address where the missing package got delivered.
SELECT * FROM "addresses" WHERE "id" = (
    SELECT "address_id" FROM "scans" WHERE "package_id" = (
        SELECT "id" FROM "packages" WHERE "from_address_id" = (
            SELECT "id" FROM "addresses" WHERE "address" = '900 Somerville Avenue')
    AND "to_address_id" = (
        SELECT "id" FROM "addresses" WHERE "address" LIKE '%2 Fin%')
    ) AND "action" = 'Drop'
);


-- *** The Devious Delivery ***

-- We know this mystery package has no "FROM" address. So lets query the packages table for all packages with "from_address_id" set to NULL
-- We can also check the contents of all packages with no "From" address via this query
-- we will call this query1
SELECT * FROM "packages" WHERE "from_address_id" is NULL;
-- we can now use the above query1 as a subquery to lookup the delievery status in the scans table
-- we call this query2
SELECT * FROM "scans" WHERE "package_id" = (
    SELECT "id" FROM "packages" WHERE "from_address_id" is NULL
) AND "action" = 'Drop';
-- Finally we use query2 as a subquery to find from the addresses table where the package was delivered.
SELECT * from "addresses" WHERE "id" = (
    SELECT "address_id" FROM "scans" WHERE "package_id" = (
        SELECT "id" FROM "packages" WHERE "from_address_id" is NULL
        ) AND "action" = 'Drop'
);

-- *** The Forgotten Gift ***
-- Lets find out the package ID and contents first based on the "TO" and "From" address
SELECT * FROM "packages" WHERE "from_address_id" = (
    SELECT "id" FROM "addresses" WHERE "address" = '109 Tileston Street')
AND "to_address_id" = (
SELECT "id" FROM "addresses" WHERE "address" = '728 Maple Place');
-- Next lets find the status of this package ID in the scans table.
SELECT * FROM "scans" WHERE "package_id" = (
    SELECT "id" FROM "packages" WHERE "from_address_id" = (
        SELECT "id" FROM "addresses" WHERE "address" = '109 Tileston Street')
    AND "to_address_id" = (
        SELECT "id" FROM "addresses" WHERE "address" = '728 Maple Place')
);
-- We see that the package was delievered to address_id '9523' by dirver with id '11'
-- then later the package was picked up again from same address with id '9523' by driver with id '17'
-- So currently the package should be with driver with id '17'. Lets see who this driver is.
SELECT * FROM "drivers" WHERE "id" = 17;
-- we see from above query that driver "Mikel" has the package.

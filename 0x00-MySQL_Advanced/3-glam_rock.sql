-- ranking bands by longetivity
SELECT
    band_name,
    IFNULL(YEAR(split), 2022) - formed AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;


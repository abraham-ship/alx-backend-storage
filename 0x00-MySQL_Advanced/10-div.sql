CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS INT
BEGIN
    DECLARE result INT;

    -- Check if b is not equal to 0 to avoid division by zero
    IF b <> 0 THEN
        SET result = a / b;
    ELSE
        SET result = 0;
    END IF;

    RETURN result;
END;

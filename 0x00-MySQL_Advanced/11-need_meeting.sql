-- Create the view
CREATE VIEW need_meeting AS
SELECT
    u.name
FROM
    users u
LEFT JOIN
    corrections c ON u.id = c.user_id
WHERE
    c.score < 80
    AND (u.last_meeting IS NULL OR TIMESTAMPDIFF(MONTH, u.last_meeting, NOW()) > 1);


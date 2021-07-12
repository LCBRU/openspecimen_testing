-- SQLite
SELECT CURRENT_TIMESTAMP, COUNT(*) total, SUM(completed) completed, SUM(has_error) errors
FROM participant
;

-- SQLite
SELECT CURRENT_TIMESTAMP, COUNT(*) total, SUM(completed) completed
FROM collection_protocol
;

SELECT CURRENT_TIMESTAMP, SUM(has_error) total, SUM(COALESCE(has_error_checked, 0)) errors
FROM participant
;


-- SQLite
SELECT COUNT(*) total, SUM(completed) completed, SUM(has_error) errors
FROM participant
;

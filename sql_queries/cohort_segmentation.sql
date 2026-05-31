-- SQL Query: Running behavioral cohort analysis to prioritize product interventions
-- Segmenting users by active lifecycle status to track retention gaps

SELECT 
    lifecycle_segment,
    COUNT(DISTINCT user_id) AS total_distinct_users,
    COUNT(user_id) AS total_interactions_logged,
    ROUND(COUNT(user_id) * 1.0 / COUNT(DISTINCT user_id), 2) AS engagement_density_score
FROM user_activity_logs
GROUP BY lifecycle_segment
ORDER BY total_distinct_users DESC;
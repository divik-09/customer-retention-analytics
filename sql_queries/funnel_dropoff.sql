-- SQL Query: Tracking user behavior across acquisition and retention funnels
-- Identifies critical drop-off points driving key product conversion gaps

WITH FunnelStages AS (
    SELECT 
        user_id,
        COUNT(CASE WHEN funnel_stage = 'onboarding_start' THEN 1 END) as started_onboarding,
        COUNT(CASE WHEN funnel_stage = 'onboarding_complete' THEN 1 END) as completed_onboarding,
        COUNT(CASE WHEN funnel_stage = 'pricing_view' THEN 1 END) as viewed_pricing,
        COUNT(CASE WHEN funnel_stage = 'payment_success' THEN 1 END) as completed_payment
    FROM user_activity_logs
    GROUP BY user_id
)
SELECT 
    COUNT(CASE WHEN started_onboarding > 0 THEN 1 END) AS total_started_onboarding,
    COUNT(CASE WHEN completed_onboarding > 0 THEN 1 END) AS total_completed_onboarding,
    COUNT(CASE WHEN viewed_pricing > 0 THEN 1 END) AS total_viewed_pricing,
    COUNT(CASE WHEN completed_payment > 0 THEN 1 END) AS total_completed_payment,
    
    -- Drop-off Calculation Matrices
    ROUND((1.0 - (COUNT(CASE WHEN completed_onboarding > 0 THEN 1 END) * 1.0 / COUNT(CASE WHEN started_onboarding > 0 THEN 1 END))) * 100, 2) AS onboarding_dropoff_pct,
    ROUND((1.0 - (COUNT(CASE WHEN completed_payment > 0 THEN 1 END) * 1.0 / COUNT(CASE WHEN viewed_pricing > 0 THEN 1 END))) * 100, 2) AS pricing_to_payment_gap_pct
FROM FunnelStages;
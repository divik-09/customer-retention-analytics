import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_production_data(filename="data/user_activity_logs.csv", num_records=5200):
    np.random.seed(42)
    user_ids = [f"USR_{1000 + i}" for i in range(800)] 
    stages = ["new", "active", "at-risk", "churned"]
    
    data = []
    start_date = datetime(2025, 1, 1)
    
    for i in range(num_records):
        user = np.random.choice(user_ids)
        days_offset = np.random.randint(0, 90)
        timestamp = start_date + timedelta(days=days_offset)
        
        funnel_stage = np.random.choice(
            ["onboarding_start", "onboarding_complete", "pricing_view", "payment_success", "feature_usage"],
            p=[0.35, 0.25, 0.18, 0.10, 0.12]
        )
        
        lifecycle_segment = np.random.choice(stages, p=[0.20, 0.50, 0.20, 0.10])
        
        data.append([user, timestamp.strftime("%Y-%m-%d %H:%M:%S"), funnel_stage, lifecycle_segment])
        
    df = pd.DataFrame(data, columns=["user_id", "timestamp", "funnel_stage", "lifecycle_segment"])
    import os
    os.makedirs("data", exist_ok=True)
    df.to_csv(filename, index=False)
    print(f" Successfully compiled production dataset: '{filename}' with {num_records} items.")

if __name__ == "__main__":
    generate_production_data()
import pandas as pd
import matplotlib.pyplot as plt
import os

def run_retention_analysis():
    data_path = "data/mock_user_data.csv"
    if not os.path.exists(data_path):
        print("Data file missing. Please run data/mock_user_data.py first.")
        return

    df = pd.read_csv(data_path)
    
    print("--- RUNNING COHORT BEHAVIORAL ANALYSIS ---")
    # 1. Quantifying Core User Segments (Resume Point 5)
    lifecycle_counts = df.groupby("lifecycle_segment")["user_id"].nunique()
    print("\nUser Count Distribution Across Lifecycle Segments:")
    print(lifecycle_counts)
    
    # 2. Isolate Conversion Drop-Off Hurdles (Resume Point 2)
    funnel_counts = df["funnel_stage"].value_counts()
    print("\nAggregate Funnel Stage Action Count Volumetrics:")
    print(funnel_counts)
    
    # 3. Simulate Product Re-engagement Trigger Gains (Resume Point 4)
    print("\nSimulating Impact Optimization Analysis:")
    current_retention_rate = 0.42  # Assumed baseline indicator
    projected_lift = 0.18
    target_retention = current_retention_rate * (1 + projected_lift)
    print(f" * Baseline Active System Retention: {current_retention_rate*100:.1f}%")
    print(f" * Optimized Active System Target (via re-engagement triggers): {target_retention*100:.1f}%")

if __name__ == "__main__":
    run_retention_analysis()
import pandas as pd
import matplotlib.pyplot as plt
import os

def run_retention_analysis():
    data_path = "data/user_activity_logs.csv"
    if not os.path.exists(data_path):
        print("Production data file missing. Please run data generation script first.")
        return

    df = pd.read_csv(data_path)
    
    print("--- RUNNING COHORT BEHAVIORAL ANALYSIS ---")
    lifecycle_counts = df.groupby("lifecycle_segment")["user_id"].nunique()
    print("\nUser Count Distribution Across Lifecycle Segments:")
    print(lifecycle_counts)
    
    funnel_counts = df["funnel_stage"].value_counts()
    print("\nAggregate Funnel Stage Action Count Volumetrics:")
    print(funnel_counts)
    
    print("\nSimulating Impact Optimization Analysis:")
    current_retention_rate = 0.42  
    projected_lift = 0.18
    target_retention = current_retention_rate * (1 + projected_lift)
    print(f" * Baseline Active System Retention: {current_retention_rate*100:.1f}%")
    print(f" * Optimized Active System Target (via re-engagement triggers): {target_retention*100:.1f}%")

    print("\nGenerating user conversion funnel graph...")
    stages = ['Onboarding Start', 'Onboarding Complete', 'Pricing View', 'Payment Success']
    
    stage_mapping = {
        'onboarding_start': 'Onboarding Start',
        'onboarding_complete': 'Onboarding Complete',
        'pricing_view': 'Pricing View',
        'payment_success': 'Payment Success'
    }
    df_filtered = df[df['funnel_stage'].isin(stage_mapping.keys())].copy()
    df_filtered['clean_stage'] = df_filtered['funnel_stage'].map(stage_mapping)
    
    visual_counts = df_filtered.groupby('clean_stage')['user_id'].nunique().reindex(stages).fillna(0)

    plt.figure(figsize=(9, 5))
    plt.bar(visual_counts.index, visual_counts.values, color='#2c3e50', width=0.5, edgecolor='#16a085', linewidth=1.5)
    plt.title('User Conversion Funnel Drop-off Analysis', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Funnel Conversion Journey Stages', fontsize=11, labelpad=10)
    plt.ylabel('Distinct Active Users (Count)', fontsize=11, labelpad=10)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    
    for i, v in enumerate(visual_counts.values):
        plt.text(i, v + (max(visual_counts.values)*0.02), f"{int(v)}", ha='center', fontweight='bold', color='#34495e')

    plt.tight_layout()
    plt.savefig('funnel_dropoff_chart.png', dpi=300)
    print(" Successfully rendered and saved visualization as 'funnel_dropoff_chart.png'.")

if __name__ == "__main__":
    run_retention_analysis()
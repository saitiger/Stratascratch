import pandas as pd
thresholds = fraud_score.groupby('state')['fraud_score'].quantile(0.95).reset_index()
thresholds.columns = ['state', 'threshold']
fraud_score = pd.merge(fraud_score, thresholds, on='state')
top_5_percentile_df = fraud_score[fraud_score['fraud_score'] >= fraud_score['threshold']]
top_5_percentile_df[['policy_num', 'state', 'claim_cost', 'fraud_score']]

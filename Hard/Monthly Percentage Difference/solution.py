import pandas as pd

sf_transactions['year_month'] = sf_transactions['created_at'].dt.strftime('%Y-%m')
# sf_transactions['month'] = sf_transactions['created_at'].dt.strftime('%m')

final = sf_transactions.groupby(by='year_month')['value'].sum().reset_index()

final['revenue_diff_pct'] = round(final['value'].pct_change(periods=1)*100.0,2)

final[['year_month','revenue_diff_pct']]
# final['diff'] = final['value'].diff(periods=1)

# final

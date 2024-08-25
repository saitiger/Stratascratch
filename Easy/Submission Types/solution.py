import pandas as pd

type_counts = loans.groupby('user_id')['type'].value_counts().unstack(fill_value=0).reset_index()

filtered_users = type_counts[(type_counts['Refinance'] >= 1) & (type_counts['InSchool'] >= 1)]['user_id']

result_df = pd.DataFrame(filtered_users)

result_df

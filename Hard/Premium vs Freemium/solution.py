import pandas as pd
import numpy as np

df = ms_user_dimension.merge(ms_acc_dimension,on='acc_id')
merged = df.merge(ms_download_facts,on='user_id')

# res = merged.groupby([merged['date'].dt.date,'paying_customer'])['downloads'].sum().reset_index()

# res_no = res[res['paying_customer']=='no'].rename(columns={'downloads':'no'})[['date','no']]

# res_yes = res[res['paying_customer']=='yes'].rename(columns={'downloads':'yes'})[['date','yes']]

# final = res_no.merge(res_yes,on='date')

# final = final[final['no']>final['yes']]

res = pd.pivot_table(merged,index='date',values='downloads',columns='paying_customer',aggfunc=np.sum).reset_index()

res = res[res['no']>res['yes']]

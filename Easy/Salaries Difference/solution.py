import pandas as pd

merged = db_employee.merge(db_dept,left_on = 'department_id',right_on = 'id').rename(columns = {'id_x':'emp_id','id_y':'dept_id'})

merged = merged.loc[:, merged.columns != 'department_id']

eng_highest = merged[merged['department']=='engineering']['salary'].max()

mar_highest = merged[merged['department']=='marketing']['salary'].max()

abs(mar_highest - eng_highest)

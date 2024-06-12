import pandas as pd

worker.merge(title,left_on = 'worker_id',right_on = 'worker_ref_id').
nlargest(1,'salary',keep='all')['worker_title'].rename('best_paid_title')

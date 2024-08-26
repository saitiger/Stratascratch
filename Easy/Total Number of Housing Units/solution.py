import pandas as pd
result = housing_units_completed_us.groupby('year').apply(lambda x: x[['south', 'west', 'midwest', 'northeast']].sum().sum()).reset_index()
result

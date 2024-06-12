# Import your libraries
import pandas as pd

# Start writing code
email_counts = google_gmail_emails.groupby('from_user')['id'].count().reset_index().rename(columns = {'id':'total_emails'})
email_counts['rank'] = email_counts['total_emails'].rank(method = 'first',ascending = False)

email_counts.sort_values(by=['rank','from_user'],ascending = [True,True])

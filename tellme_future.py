from datetime import datetime

date = datetime(100000,1,1)
print(f'The party started on {date:%B, %d, %Y} and lasted a 10 days')


import pandas as pd
import webbrowser
from datetime import datetime, timedelta
from time import sleep

df_link = pd.read_csv('assets/Subject_Links.csv', index_col=0)
#webbrowser.open_new_tab(df['Links']['Subject_Name'])

df_sub = pd.read_csv('assets/Time_Table.csv', index_col='WeekDays')
#print(df_sub.info())

def handler(sub):
    
    if sub not in ('CLC', 'X'): 
        webbrowser.open_new_tab(df_link['Links'][sub])
        print(sub + 'class is started!!')
    #    if 'meet' in df_link['Links'][sub]:
            
    else:
        t = datetime.now().strftime('%H:%M:%S')
        print('No class at ' + t)

def wait_and_call(time, cb, sub):
        
    while datetime.now() < time:
        sleep(2)

    if datetime.now().strftime('%H') == time.strftime('%H'):
        cb(sub)

def main():
    
    Today_num = datetime.today().weekday()
    sub = df_sub.iloc[Today_num]
    today_time = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
    for subject in sub:
        wait_and_call(today_time, handler, subject)
        today_time += timedelta(hours=1)

if __name__ == '__main__':
    main()

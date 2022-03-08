import pandas as pd
import webbrowser
from datetime import datetime, timedelta
from time import sleep
from color import *

df_link = pd.read_csv('assets/Subject_Links.csv', index_col=0)

df_sub = pd.read_csv('assets/Time_Table.csv', index_col=False, header=None)
new_columns = df_sub.columns.values
new_columns[0] = 0
df_sub.columns = new_columns
df_sub = df_sub.set_index(0)
#print(df_sub.info())

def handler(sub):
    
#    if sub != 'X':
    if 'X' not in sub:

        if sub not in ('CLC', 'SE'): 
            webbrowser.open_new_tab(df_link['Links'][sub])
            print(sub + ' class is started!!')
        #   if 'meet' in df_link['Links'][sub]:
           
        else:
            print('[PANIC] YOU NEED TO JOIN "' + sub + '" CLASS MANUALLY !!!!')
    else:
        t = datetime.now().strftime('%H:%M:%S')
        print('No class at ' + t)

def wait_and_call(time, cb, sub):
       
    # Wait until class starts. 
    while datetime.now() < time:
        sleep(2)

    # If you're late for the class, and the class is still
    # going on then this 'if' condition helps to join class
    # immediately otherwise ignore.
    if datetime.now().strftime('%H') == time.strftime('%H'):
        cb(sub)#Starting class of that time

def main():
    Today_num = datetime.today().weekday()
    sub = df_sub.iloc[Today_num]
    print(Today_num)    
    # Initial starting time of today's meeting
    today_time = datetime.now().replace(hour=8, minute=0, second=0,
            microsecond=0)
    
    for subject in sub:
        wait_and_call(today_time, handler, subject)
        today_time += timedelta(hours=1)

if __name__ == '__main__':
    Start()
    main()
    End()

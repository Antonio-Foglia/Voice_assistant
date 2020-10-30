import requests
import pandas as pd
import bs4
from __output__ import say
from __input__ import inp
from __recognise__ import recognise

def serie_a(text):
    bs=bs4.BeautifulSoup(requests.get('https://www.skysports.com/serie-a-table').content,'lxml')
    tables=bs.find_all('table')
    df=pd.read_html(str(tables[0]))[0]
    df=df.set_index('Team').rename(columns={'#':'Pos'}).drop('Last 6',1)
    pos=int(df.loc['AC Milan'].Pos)
    pts=int(df.loc['AC Milan'].Pts)
    say(f'AC Milan are currently in position {pos} in the Serie A, with {pts} points.','en')
    say('Would you like to see the whole Serie A table?','en')
    fname=inp(3,'ques')
    ans = recognise(fname)
    if 'yes' in ans:
        print(f'##\n{df}\n##')
        return
    if 'no' in ans:
        return

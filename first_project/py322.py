# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:33:38 2021

@author: greg_desk
"""

def mysystemp ():
    """zeitstempel als string"""
    import time
    today = time.localtime()
    InternDatum = str(today.tm_year)+'-'+str(today.tm_mon)+'-'+str(today.tm_mday)
    InternZeit = str(today.tm_hour)+':'+str(today.tm_min)+':'+str(today.tm_sec)
    InternDatumsformat = InternDatum + 'T' + InternZeit
    return(InternDatumsformat)

print(mysystemp())
help(mysystemp)


autoren = ["Douglas Adams","Isaac Asimov", "Terry Pratchett", "Iain Banks"]
for name in autoren:
    print(name)

for i in range(1,11,2):
    print(i)
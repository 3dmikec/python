'''
PRINTS THE CURRENT DATE AND TIME
'''

import datetime

def curr_date_time():
    now = datetime.datetime.now()
    print('Current date and time:\n' + now.strftime("%Y-%m-%d %H:%M:%S"))

curr_date_time()

input("Press ENTER to exit")

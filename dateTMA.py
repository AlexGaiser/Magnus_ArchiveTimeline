#! python3

#this is the statement number to date conversion module
# it aims to convert statement numbers to actual dates.

import datetime
import re

#TMA statement dates are 7 digit numbers corresponding to dates in the format YYYDDMM

def convert(st_number):
    
    for i in str(st_number):
        print(i)
        if st_number[0] == '0':
            stdate = '2'+str(st_number)
        else:
            stdate = '1'+ str(st_number)
    print(stdate)
    realdate = datetime.datetime.strptime(str(stdate), "%Y%d%m").strftime("%m-%d-%Y")
    return(realdate)


convert('0100325')
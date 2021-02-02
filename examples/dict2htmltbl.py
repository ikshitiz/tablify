import sys
from tablify.parser.parse import pyobj

dict_example = {'Total_Matches': ['200', '127', '102'],\
    'Player Name': ['M.S Dhoni', 'Virendra Sehwag', 'Shikhar Dhawan'],\
    'Sixes': ['280.', '210', '126']}

pyobj = pyobj()
htmltext = pyobj.dictToHTMLTable(dict_example)
print(htmltext)


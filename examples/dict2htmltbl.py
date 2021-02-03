import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from tablify.parse import pyobj

dict_example = {'Total_Matches': ['200', '127', '102'],\
    'Player Name': ['M.S Dhoni', 'Virendra Sehwag', 'Shikhar Dhawan'],\
    'Sixes': ['280.', '210', '126']}

pyobj = pyobj()
htmltext = pyobj.dictToHTMLTable(dict_example)
print(htmltext)

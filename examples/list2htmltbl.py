import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from tablify.parse import pyobj

l_example = [['200', '127', '102'],\
    ['M.S Dhoni', 'Virendra Sehwag', 'Shikhar Dhawan'],\
        ['280.', '210', '126']]


col = ['Total_Matches','Player Name','Sixes']

pyobj = pyobj()
htmltext = pyobj.listOfListToHTMLTable(l_example, col)
print(htmltext)

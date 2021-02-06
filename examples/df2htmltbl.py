import sys
import os
import pandas as pd 

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from tablify.parse import pyobj


df_example = pd.DataFrame([[1,2,3],[3,4,5]], \
       columns=('first', 'second', 'third'), \
       index=('alpha', 'beta')) 

pyobj = pyobj()
htmltext = pyobj.dfToHTMLTable(df_example)
print(htmltext)

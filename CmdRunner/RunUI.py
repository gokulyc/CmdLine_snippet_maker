from PyQt5 import QtWidgets,uic

import json
from pprint import pprint

from os import getcwd 

print(getcwd())

with open(r'test123\CmdRunner\store.json') as f:
  config = json.load(f)
pprint(config['name'])

app=QtWidgets.QApplication([])

dlg=uic.loadUi(r'test123\CmdRunner\firstuinew.ui')

dlg.show()

app.exec()
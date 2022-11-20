from PyQt5.QtWidgets import QApplication
from smart import *
import json 

# notes = {
#     "Ласкаво просимо!": {
#         "text": "Це программа для створення заміток...",
#         "tegs": ["інструкція", "про программу"]
#     }
# }

# with open("notes.json", "w", encoding="utf-8") as file:
#     json.dump(notes, file)

app = QApplication([])

def show_note():
    t = win.listWidget_2.currentItem().text()
    win.textEdit.setText(notes[t]["text"])
    win.listWidget.clear()
    win.listWidget.addItems(notes[t]["tegs"])

with open("notes.json", "r", encoding="utf-8") as file:
    notes = json.load(file)
    
win = Ui_Form()
win.setupUi(win)
win.show()        
win.listWidget_2.addItems(notes.keys())
win.listWidget_2.itemClicked.connect(show_note)
app.exec_()
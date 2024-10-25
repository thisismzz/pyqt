from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


# class Window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(600,600)
#         options = ['c++' ,'python' ,'java' ,'php']
#         completer = QCompleter(options)
#         lineedit = QLineEdit()
#         lineedit.setCompleter(completer)
#         layout.addWidget(lineedit)
#         completer.setMaxVisibleItems(1)
#         completer.setCompletionMode(QCompleter.InlineCompletion)

# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#___________________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         global calendar
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(700,700)
#         calendar = QCalendarWidget()
#         layout.addChildWidget(calendar)
#         calendar.setGeometry(QRect(100,200,400,400))
#         button = QPushButton("button")
#         layout.addChildWidget(button)
#         button.setGeometry(QRect(50,40,80,80))
#         button.clicked.connect(self.on_click)

#     def on_click(self):
#         calendar.showNextYear()
#         print(calendar.selectedDate())
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())


#___________________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(600,600)
#         time = QTime()
#         time.setHMS(18,22,00)
#         timeedit = QTimeEdit()
#         timeedit.setTime(time)
#         layout.addWidget(timeedit)
#         timeedit.setMinimumTime(QTime(18,21,00))
#         timeedit.setMaximumTime(QTime(18,40,25))
#         dt = QDateTime().currentDateTime()
#         label = QLabel(dt.toString())
#         layout.addWidget(label)

        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#___________________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         global filedialog,colordialog,label,button,button2,button3
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(600,600)
#         dialog = QDialogButtonBox(QDialogButtonBox.Close | QDialogButtonBox.Ok)
#         layout.addChildWidget(dialog)
#         dialog.setGeometry(300,200,200,100)
#         filedialog = QFileDialog()
#         button = QPushButton("file dialog")
#         layout.addWidget(button)
#         button.clicked.connect(self.on_click)
#         button2 = QPushButton("File name")
#         layout.addWidget(button2)
#         button2.clicked.connect(self.on_click2)
#         filedialog.setAcceptMode(QFileDialog.AcceptOpen)
#         colordialog = QColorDialog()
#         button3 = QPushButton("color")
#         layout.addWidget(button3)
#         button3.clicked.connect(self.on_click3)
#         label = QLabel("label")
#         layout.addWidget(label)
        
#     def on_click(self):
#         global fname
#         fname = filedialog.getOpenFileName()
        
#     def on_click2(self):
#         print(fname)
#         label.setText(fname[0])
        
#     def on_click3(self):
#         color = QColorDialog.getColor()
#         if color.isValid():
#             print(color.name())
#             button.setStyleSheet("background-color:"+color.name()+';')
#             button2.setStyleSheet("background-color:"+color.name()+';')
#             button3.setStyleSheet("background-color:"+color.name()+';')
            
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#___________________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         global label
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         label = QLabel("python")
#         layout.addChildWidget(label)
#         label.setGeometry(QRect(50,50,400,300))
#         label.setFont(QFont("Arial",30))
#         button = QPushButton("Open Fonts")
#         layout.addWidget(button)
#         button.clicked.connect(self.on_click)
        
#     def on_click(self):
#         getfont,ok = QFontDialog().getFont()
#         if ok:
#             label.setFont(getfont)
#             print(getfont.toString())
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())

#___________________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         global fontcombobox
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         fontcombobox = QFontComboBox()
#         layout.addWidget(fontcombobox)
#         fontcombobox.currentFontChanged.connect(self.fontchanged)
        
#     def fontchanged(self):
#         font = fontcombobox.currentFont()
#         print("font: %s " %(font.family()))
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())


#___________________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         global listwidget,label
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(700,500)
#         button = QPushButton("show list")
#         layout.addWidget(button)
#         button.clicked.connect(self.buttonclicked)
#         label = QLabel("label")
#         layout.addWidget(label)
#         listwidget = QListWidget()
#         listwidget.insertItem(0,"python")
#         listwidget.insertItem(1,"c++")
#         listwidget.insertItem(2,"java")
#         listwidget.insertItem(3,"php")
#         listwidget.insertItem(4,"c")
#         layout.addWidget(listwidget)
#         listwidget.clicked.connect(self.listwidgetclicked)
#         listwidget.hide()
#         listwidget.sortItems(Qt.AscendingOrder)
        
#     def buttonclicked(self):
#         listwidget.show()
    
#     def listwidgetclicked(self):
#         item = listwidget.currentItem()
#         label.setText("Selected : "+ (item.text()) + " row : " + str(listwidget.currentRow()))

        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())


#___________________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         global tablewidget
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)
#         tablewidget = QTableWidget()
#         layout.addWidget(tablewidget)
#         tablewidget.setRowCount(4)
#         tablewidget.setColumnCount(3)
#         tablewidget.setColumnWidth(3,200)
#         tablewidget.setRowHeight(3,200)
#         button = QPushButton("Calculate")
#         layout.addWidget(button)
#         button.clicked.connect(self.on_click)
#         tablewidget.setShowGrid(False)
#         tablewidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        
    
#     def on_click(self):
#         s1 = tablewidget.item(0,0).text()
#         s2 = tablewidget.item(1,0).text()
#         s3 = tablewidget.item(2,0).text()
#         tablewidget.setItem(3,0,QTableWidgetItem(" sum : " + str(int(s1)+int(s2)+int(s3))))
#         tablewidget.setItem(3,1,QTableWidgetItem(" sum : " + str(-int(s1)-int(s2)-int(s3))))
#         tablewidget.setItem(3,2,QTableWidgetItem(" sum : " + str(int(s1)*int(s2)*int(s3))))
        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())


#___________________________________________

# class Window(QWidget):
    
#     def __init__(self):
#         QWidget.__init__(self)
#         layout = QGridLayout()
#         self.setLayout(layout)
#         self.resize(500,500)

        
# app = QApplication(sys.argv)
# screen = Window()
# screen.show()
# sys.exit(app.exec_())


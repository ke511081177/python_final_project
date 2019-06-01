

# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 11:57:06 2019

@author: Administrator
"""





import sys, os, random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QIcon, QPixmap



def ine():
    print("dfdfdfdffd")
        


class initialization_Button(QPushButton):

    
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setIcon(QIcon('icon.jpg'))
        self.setIconSize(QSize(200,200))
        self.clicked.connect(AppForm().add_Photo)
            
        
        




fileName_choose = ''



photo_space = QGroupBox("Grid layout")

layout = QGridLayout()
photo_space.setMinimumSize(600,400)
layout.setSpacing(10) 
layout.setColumnStretch(1, 10)

initialize_button = initialization_Button('')
layout.addWidget(initialize_button,0,0)


photo_column = 0
photo_row = -1


photo_space.setLayout(layout)







class Photo_Button(QPushButton):


    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        
        
        self.AppForm = self.parent()
        self.setIcon(QIcon(fileName_choose))
        self.setIconSize(QSize(200,200))

class Lower_Button(QPushButton):

    
    def __init__(self, title, parent=None):
        super().__init__(title, parent)



class file():
    def file1():
        print("232333")
            
class AppForm(QMainWindow):
    

    
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle('老闆來啦')
# =============================================================================
#         qss_file = open('style.qss').read()
#         self.setStyleSheet(qss_file)
# =============================================================================
        
        self.setGeometry(200,100,800,400)
        self.setAcceptDrops(True)
        self.create_menu()
        self.create_main_frame()
        
        



     
    def on_about(self):
        msg ="""
        
        加油。
        """
        QMessageBox.about(self, "簡介", msg.strip())
    
    def create_main_frame(self):
        self.main_frame = QWidget()






        finalbox = QVBoxLayout()

# =============================================================================
#         self.view = View(self)
# =============================================================================






        self.cb = QCheckBox('警告訊息')
        self.warning_word =QTextEdit()
        self.warning_word.setMaximumSize(400,40)
        
        self.choose_Button = QPushButton("選擇")   
        self.choose_Button.setCheckable(True)
        self.choose_Button.setMaximumSize(60,30)
        
        self.button =  QPushButton("choose") 
        upper_grid = QGridLayout()
       
        upper_grid.addWidget(photo_space,0,0,6,6)
        upper_grid.addWidget(self.cb,1,7)
        upper_grid.addWidget(self.warning_word,2,7)
        upper_grid.addWidget(self.choose_Button,4,7)
        upper_grid.addWidget(self.button,5,7)
        self.button.clicked.connect(self.add_button)
        
        


        lower_grid = QGridLayout()
        self.preset_button = Lower_Button('預設',self)
        self.cancel_button = Lower_Button('取消',self)
        self.ok_button = Lower_Button('儲存',self)
                
        
        lower_grid.setSpacing(4)
        lower_grid.addWidget(self.preset_button,1,0)
        lower_grid.addWidget(self.cancel_button,1,1)
        lower_grid.addWidget(self.ok_button,1,2)
        
        
        
        for w in [self.preset_button,self.cancel_button,self.ok_button]:
            w.setMaximumSize(60,30)
            lower_grid.setAlignment(w,Qt.AlignRight)
        
        finalbox.addLayout(upper_grid)
        finalbox.addLayout(lower_grid)
       
    
        self.main_frame.setLayout(finalbox)
        self.setCentralWidget(self.main_frame)
    
    def other_file(self):
    
        fileName_choose, filetype = QFileDialog.getSaveFileName(self,
                                    "")

        f = open(fileName_choose,'r')
        
        
    def add_Photo(self):

        global fileName_choose
        
       
        
        fileName_choose, filetype = QFileDialog.getSaveFileName(self,
                                    "新增圖片")

        f = open(fileName_choose,'r')
        self.add_button()

    def create_menu(self):        
        menu = self.menuBar().addMenu('檔案')
        new_action = menu.addAction('創建新檔')
        new_action.triggered.connect(self.add_Photo)

        
        about_action = self.menuBar().addAction('介紹')
        about_action.triggered.connect(self.on_about)
    
    def add_button(self):
        global photo_column
        global photo_row
        
        photo_row +=1
        
        if photo_row == 3:
            photo_row =0
            photo_column+=1
        
        print(photo_column)
        print(photo_row)
            
        self.button = Photo_Button('')
        
        self.button.setGeometry(50, 40, 200, 200)
        
        layout.addWidget(self.button,photo_column,photo_row)


# =============================================================================
#         self.button.show() 
# =============================================================================

def main():
    app = QApplication(sys.argv)
    form = AppForm()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

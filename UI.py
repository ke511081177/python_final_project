

import sys, os, random
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QIcon, QPixmap






class initialization_Button(QPushButton):
    
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setIcon(QIcon('icon.jpg'))
        self.setIconSize(QSize(200,200))
        self.clicked.connect(self.add_Photo)
            
        
    def add_Photo(self):

        global fileName_choose
        
        
        fileName_choose, filetype = QFileDialog.getSaveFileName(self,
                                    "新增圖片")

        if fileName_choose == "":

            print("\n取消存檔")
            return
        
        f = open(fileName_choose,'r')
        self.add_button()
        
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
        
        if photo_row == 2:
            layout.addWidget(initialize_button,photo_column+1,0)
        else:
            layout.addWidget(initialize_button,photo_column,photo_row+1)
        





fileName_choose = ''
sw_choose = ''


photo_space = QGroupBox("請輸入你要警示對象的圖片")

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
        qss_file = open('darkstyle.qss').read()
        self.setStyleSheet(qss_file)
        
        self.setGeometry(200,100,800,400)

        self.create_menu()
        self.create_main_frame()
        
        



     
    def on_about(self):
        msg ="""
        
        有一天有一個小朋友到了河邊玩

        傍晚卻還沒回家

        小孩的家人都很著急的想找他

        卻一直都找不到

        過了三年，大家都放棄了

        唯有奶奶每天還是會去河邊看看有沒有孩子的蹤影

        而這份感情也感動了湖中女神

        於是湖中女神決定幫助阿嬤

        湖中女神說：阿嬤，你掉了什麼嗎？

        阿嬤激動地說：我的金孫不見了，你有看到他嗎？

        湖中女神說：哎呀，你太貪心了唷。
        
        接著便離開了。
        """
        QMessageBox.about(self, "簡介", msg.strip())
    def a(self):
        print('sdsd')
        
    def create_main_frame(self):
        
        global actions
        
        self.main_frame = QWidget()


        cb = QCheckBox(self,text="警告訊息", checkable=True)

        finalbox = QVBoxLayout()


        
        toolbarBox = QToolBar('開啟程式~~~~~~~~~',self)
        toolbarBox.setFixedWidth(180)
        
        self.addToolBar(QtCore.Qt.LeftToolBarArea, toolbarBox)
        
        vscode_action = QtWidgets.QToolButton(self, text="VSCode", checkable=True)
        ppt_action = QtWidgets.QToolButton(self, text="PPt", checkable=True)
        word_action = QtWidgets.QToolButton(self, text="Word", checkable=True)
        excel_action = QtWidgets.QToolButton(self, text="Excel", checkable=True)
        other_action = QtWidgets.QToolButton(self, text="其他程式", checkable=True)
        
        other_action.toggled.connect(self.other_file)
        
        group = QtWidgets.QButtonGroup(self, exclusive=True)

        for button in (
            vscode_action,
            ppt_action,
            word_action,
            excel_action,
            other_action,
        ):
            toolbarBox.addWidget(button)
            group.addButton(button)

    


        group.addButton(cb)
        cb.stateChanged.connect(self.cb_check)

        
        self.warning_word =QTextEdit()
        self.warning_word.setMaximumSize(400,40)
        self.warning_word.setReadOnly(True)
        self.warning_word.setStyleSheet("background-color: gray")
        
        self.file_word = QTextEdit()
        self.file_word.setMaximumSize(400,80)
        self.file_word.setReadOnly(True)
        
        self.choose_Button = QPushButton("選擇")  
        self.choose_label = QLabel('開啟程式')
        self.choose_Button.setCheckable(True)
        self.choose_Button.setMaximumSize(60,30)
        


        

        upper_grid = QGridLayout()
        
        upper_grid.addWidget(photo_space,0,0,6,6)
        upper_grid.addWidget(cb,1,7)
        upper_grid.addWidget(self.warning_word,2,7)
        upper_grid.addWidget(self.choose_label,3,7)
        upper_grid.addWidget(self.file_word,4,7)
        upper_grid.addWidget(toolbarBox,5,7)
        

        


        lower_grid = QGridLayout()
        self.preset_button = Lower_Button('預設',self)
        self.cancel_button = Lower_Button('取消',self)
        self.ok_button = Lower_Button('儲存',self)
                
        
        lower_grid.setSpacing(0)
        lower_grid.addWidget(self.preset_button,1,20)
        lower_grid.addWidget(self.cancel_button,1,1)
        lower_grid.addWidget(self.ok_button,1,22)
        
        
        
        for w in [self.preset_button,self.cancel_button,self.ok_button]:
            w.setMaximumSize(60,30)
            lower_grid.setAlignment(w,Qt.AlignRight)
        
        finalbox.addLayout(upper_grid)
        finalbox.addLayout(lower_grid)
       
    
        self.main_frame.setLayout(finalbox)
        self.setCentralWidget(self.main_frame)
    

    
    def cb_check(self,a):
        
        print(a)
        if a == 2:
            self.warning_word.setReadOnly(False)
            self.warning_word.setStyleSheet("background-color: white")
            
# =============================================================================
#             for action in (
#             self.vscode_action,
#             self.ptt_action,
#             self.word_action,
#             self.excel_action,
#             self.other_action,
#         ):
#                 action.setCheckable(False)
# =============================================================================
        else:
            self.warning_word.setReadOnly(True)
            self.warning_word.setStyleSheet("background-color: gray")
# =============================================================================
#             for action in (
#             self.vscode_action,
#             self.ptt_action,
#             self.word_action,
#             self.excel_action,
#             self.other_action,
#         ):
#                 action.setCheckable(True)
# =============================================================================
        
        
    
    def other_file(self):
        
        sw_choose, sw_type = QFileDialog.getSaveFileName(self,
                                    "其他程式")

        f = open(sw_choose,'r')
        
        self.file_word.setText(sw_choose)

    def create_menu(self):        
     
        about_action = self.menuBar().addAction('介紹')
        about_action.triggered.connect(self.on_about)
    

def main():
    app = QApplication(sys.argv)
    form = AppForm()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

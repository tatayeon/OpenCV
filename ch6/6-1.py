from PyQt5.QtWidgets import *
import sys
import subprocess

class BeepSound(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.setWindowTitle('삑 소리 내기')  # 윈도우 이름과 위치 지정
        self.setGeometry(200, 200, 500, 100) # 위치와 사이즈 를 파라미터로 

        shortBeepButton = QPushButton('짧게 삑', self)  # 버튼 생성
        longBeepButton = QPushButton('길게 삑', self)  
        quitButton = QPushButton('나가기', self)
        self.label = QLabel('환영합니다!', self)
        
        shortBeepButton.setGeometry(10, 10, 100, 30)  # 버튼 위치와 크기 지정 윈도우 안에서의 위치를 잡는다.
        longBeepButton.setGeometry(110, 10, 100, 30)
        quitButton.setGeometry(210, 10, 100, 30)
        self.label.setGeometry(10, 40, 500, 70)
        
        shortBeepButton.clicked.connect(self.shortBeepFunction)  # 콜백 함수 지정
        longBeepButton.clicked.connect(self.longBeepFunction)
        quitButton.clicked.connect(self.quitFunction)
       
    def shortBeepFunction(self):
        self.label.setText('짧은 삑 소리를 내는 중입니다.')   
        self.beep(0.5)
        
    def longBeepFunction(self):
        self.label.setText('긴 삑 소리를 내는 중입니다.')        
        self.beep(3)
                
    def quitFunction(self):
        self.close()
    
    def beep(self, duration):
        # Use the `afplay` command on macOS to play a sound for the specified duration
        subprocess.call(['afplay', '/System/Library/Sounds/Ping.aiff'])
                
app = QApplication(sys.argv) 
win = BeepSound() 
win.show()
app.exec_()
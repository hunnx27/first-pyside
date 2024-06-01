from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
app = QApplication()
from main_ui import Ui_MainWindow
from qt_thread import WorkerThread
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.worker = WorkerThread()
        # 아이콘 설정
        icon = QIcon("tdcompany_logo.jpg")  # 아이콘 이미지 파일 경로
        self.setWindowIcon(icon)

    @Slot()
    def startGoogleIndex(self):
        print('strat')
        if not self.worker.isRunning():
            self.worker = WorkerThread()
            self.worker.start()

    @Slot()
    def stopGoogleIndex(self):
        print('stop')
        if self.worker.isRunning():
            self.worker.stop()
            self.worker.wait()
        
window = MainWindow()
window.show()

# Start the Event Loop!
app.exec()



# src/main.py
import sys
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow
from controllers.main_controller import MainController

def main():

    # QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    # QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    # QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    main_window = MainWindow()
    style = main_window.styleSheet()
    app.setStyleSheet(style)

    main_controller = MainController(main_window)

    main_window.showMaximized()

    sys.exit(app.exec())

if __name__ == "__main__":
    
    main()

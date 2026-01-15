# src/main.py
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow
from controllers.main_controller import MainController

def main():
    # QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)

    main_window = MainWindow()
    style = main_window.styleSheet()
    app.setStyleSheet(style)

    main_controller = MainController(main_window)

    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

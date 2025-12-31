# src/main.py
import sys
from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow
from controllers.main_controller import MainController

def main():
    app = QApplication(sys.argv)

    main_window = MainWindow()

    main_controller = MainController(main_window)

    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

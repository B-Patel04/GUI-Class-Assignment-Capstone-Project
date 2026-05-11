# main.py

import sys
from PySide6.QtWidgets import QApplication
from Controller import TemperatureController


def main():

    app = QApplication(sys.argv)

    window = TemperatureController()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
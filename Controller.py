# controller.py

from PySide6.QtWidgets import QMainWindow, QMessageBox
from view_ui import Ui_Root
from model import TemperatureModel


class TemperatureController(QMainWindow):

    def __init__(self):
        super().__init__()

        # Load UI
        self.ui = Ui_Root()
        self.ui.setupUi(self)

        # Model
        self.model = TemperatureModel()

        # Signals
        self.ui.btnConvert.clicked.connect(self.convert_temperature)
        self.ui.btnClear.clicked.connect(self.clear_form)
        self.ui.btnExit.clicked.connect(self.close)

        # Default state
        self.reset_form()

    def show_error(self, message):
        QMessageBox.critical(self, "Error", message)

    def reset_form(self):
        self.ui.entDegree.clear()
        self.ui.lblResult.setText("Result shows here")
        self.ui.radC2F.setChecked(True)
        self.ui.entDegree.setFocus()

    def clear_form(self):
        self.reset_form()

    def convert_temperature(self):

        text = self.ui.entDegree.text()

        valid, result = self.model.validate_input(text)

        if not valid:
            self.show_error(result)
            return

        value = result

        # C -> F
        if self.ui.radC2F.isChecked():

            fahrenheit = self.model.celsius_to_fahrenheit(value)

            self.ui.lblResult.setText(
                f"{value:.2f} °C = {fahrenheit:.2f} °F"
            )

        # F -> C
        else:

            celsius = self.model.fahrenheit_to_celsius(value)

            self.ui.lblResult.setText(
                f"{value:.2f} °F = {celsius:.2f} °C"
            )
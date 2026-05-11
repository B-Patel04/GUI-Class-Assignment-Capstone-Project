# Temperature Converter (MVC PySide6 App)

## Description

This is a simple desktop temperature converter built using **Python**, **PySide6**, and **Qt Designer**.

The application converts between:
- Celsius → Fahrenheit
- Fahrenheit → Celsius

This project is designed as a **proof of concept (PoC)** demonstrating the **Model–View–Controller (MVC)** architecture.

---

## MVC Architecture Overview

### Model
The Model handles all application logic:
- Temperature conversion formulas
- Input validation

File:
- `model.py`

---

### View
The View is created using **Qt Designer** and defines the GUI layout.

It includes:
- Input field (`entDegree`)
- Radio buttons for conversion type
- Output label (`lblResult`)
- Buttons (Convert, Clear, Exit)

Files:
- `view.ui`
- `view.py` (generated from UI file)

---

### Controller
The Controller connects the UI to the Model:
- Reads user input from the View
- Calls Model methods for calculations
- Updates the output label in the View
- Handles button clicks

File:
- `controller.py`

---

## How to Run

### 1. Install dependencies
```bash
pip install PySide6

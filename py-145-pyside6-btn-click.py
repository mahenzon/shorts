"""
Run in terminal:

pip install pyside6

save this file as main.py

run python main.py
"""
import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
)


class CounterWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.counter = 0

        self.setWindowTitle("Counter Example")
        self.setGeometry(400, 400, 300, 200)

        self.button = QPushButton("Click Me", self)
        self.button.clicked.connect(
            self.increment_counter
        )
        self.button.setGeometry(50, 50, 200, 50)

        self.label = QLabel("Counter: 0", self)
        self.label.setGeometry(50, 120, 200, 50)

    def increment_counter(self):
        self.counter += 1
        self.button.setText(
            f"Click Me ({self.counter})"
        )
        self.label.setText(
            f"Counter: {self.counter}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = CounterWindow()
    window.show()

    sys.exit(app.exec())

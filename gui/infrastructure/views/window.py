from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout,
    QComboBox, QLabel
)


class Window(QWidget):

    def __init__(self, controller):
        super().__init__(self)
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()

        self.controller = controller

        # Dropdown menu
        self.combo = QComboBox()
        self.combo.addItems(["Option 1", "Option 2", "Option 3"])
        self.combo.currentIndexChanged.connect(self.controller.on_selection_change)


        layout.addWidget(QLabel("Choose an option:"))
        layout.addWidget(self.combo)

        self.setLayout(layout)
        


    
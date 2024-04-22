from PyQt6.QtWidgets import  QPushButton, QComboBox
from PyQt6.QtCore import QSize

class ClickButton:

    def __init__(self, size_width, size_height):
        self.size_width = size_width
        self.size_height = size_height

    def adjust_size_to_percentage_bold_button(self):

        # Example widget
        boldButton = QPushButton("Bold")
        buttonStyle = """
                        QPushButton {
                            background-color: lightgrey;
                            font-size: 25px;
                            font-weight: bold;
                            color: black;
                            border: 5px solid grey;
                             }
                        QPushButton:pressed {
                             background-color: darkgrey;
                             border-style: inset;
                        }"""

        # Calculate size as a percentage of the parent widget's size
        widthPercentage = 0.1  # 10% of parent's width
        heightPercentage = 0.05  # 5% of parent's height

        # Calculate the absolute size based on percentage
        calculatedWidth = int(self.size_width * widthPercentage)
        calculatedHeight = int(self.size_height * heightPercentage)

        # Set the calculated size to the widget

        boldButton.setFixedSize(QSize(calculatedWidth, calculatedHeight))
        boldButton.setStyleSheet(buttonStyle)
        boldButton.clicked.connect(self.on_save_clicked)  # Connect to the save method

        return boldButton

    def adjust_size_to_percentage_kursiv_button(self):
        # Example widget
        kursivButton = QPushButton("Italic")
        buttonStyle = """
                           QPushButton {
                               background-color: lightgrey;
                               font-size: 25px;
                               font: italic;
                               color: black;
                               border: 5px solid grey;
                                }
                           QPushButton:pressed {
                                background-color: darkgrey;
                                border-style: inset;
                            }"""
        # Calculate size as a percentage of the parent widget's size

        widthPercentage = 0.1  # 10% of parent's width
        heightPercentage = 0.05  # 5% of parent's height

        # Calculate the absolute size based on percentage
        calculatedWidth = int(self.size_width * widthPercentage)
        calculatedHeight = int(self.size_height * heightPercentage)

        # Set the calculated size to the widget

        kursivButton.setFixedSize(QSize(calculatedWidth, calculatedHeight))
        kursivButton.setStyleSheet(buttonStyle)
        kursivButton.clicked.connect(self.on_save_clicked)  # Connect to the save method

        return kursivButton

    def adjust_size_to_percentage_underline_button(self):
        # Example widget
        underlineButton = QPushButton("Underline")
        buttonStyle = """
                           QPushButton {
                               background-color: lightgrey;
                               font-size: 25px;
                               font: italic;
                               color: black;
                               border: 5px solid grey;
                                }
                           QPushButton:pressed {
                                background-color: darkgrey;
                                border-style: inset;
                            }"""
        # Calculate size as a percentage of the parent widget's size

        widthPercentage = 0.1  # 10% of parent's width
        heightPercentage = 0.05  # 5% of parent's height

        # Calculate the absolute size based on percentage
        calculatedWidth = int(self.size_width * widthPercentage)
        calculatedHeight = int(self.size_height * heightPercentage)

        # Set the calculated size to the widget

        underlineButton.setFixedSize(QSize(calculatedWidth, calculatedHeight))
        underlineButton.setStyleSheet(buttonStyle)
        underlineButton.clicked.connect(self.on_save_clicked)  # Connect to the save method

        return underlineButton

    def adjust_size_to_percentage_dropdown(self):
        # Example widget
        sizeDropdown = QComboBox()

        # Calculate size as a percentage of the parent widget's size
        widthPercentage = 0.03  # 3% of parent's width
        heightPercentage = 0.05  # 5% of parent's height

        # Calculate the absolute size based on percentage
        calculatedWidth = int(self.size_width * widthPercentage)
        calculatedHeight = int(self.size_height * heightPercentage)

        # Set the calculated size to the widget
        sizeDropdown.setFixedSize(QSize(calculatedWidth, calculatedHeight))
        # Dropdown Text size
        sizeDropdown.addItems(["8", "10", "12", "14", "16", "18", "20", "22", "24", "26", "28", "30"])  # Example sizes
        # Adding a label for the size dropdown
        sizeDropdown.setStyleSheet("""
                                    QComboBox { background-color: lightgrey;
                                       font-size: 25px;
                                       color: black;
                                       border: 5px solid grey;
                                       }
                                     QComboBox:drop-down {
                                        subcontrol-origin: padding;
                                        subcontrol-position: top right;
                                        width: 15px;
                                        border-left-width: 5px;
                                        border-left-color: gray;
                                        border-left-style: solid; 
                                        border-top-right-radius: 5px; 
                                        border-bottom-right-radius: 5px;
                                        }""")
        return sizeDropdown

    @staticmethod
    def on_save_clicked():
        # Implement your save functionality here
        print("Save button clicked")

    @staticmethod
    def on_close_clicked(self):
        # Close here
        self.close()
import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget,
                             QVBoxLayout, QHBoxLayout, QLabel, QFrame, QComboBox)
from PyQt6.QtCore import QSize  # Import Qt for alignment and other constants


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a central widget and set it
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        # Create the main layout and assign it to the central widget
        mainLayout = QVBoxLayout()
        centralWidget.setLayout(mainLayout)

        # Create a frame for the title bar
        titleFrame = QFrame()
        titleFrame.setFrameShape(QFrame.Shape.Box)  # Set the frame shape
        titleFrame.setFrameShadow(QFrame.Shadow.Raised)  # Set the frame shadow
        titleFrame.setStyleSheet("background-color: #000000;")  # Set background color
        titleFrame.setMaximumHeight(30)  # Set maximum height for the title frame

        # Title bar layout inside the frame
        titleBarLayout = QHBoxLayout(titleFrame)  # Assign the layout directly to the frame
        titleBarLayout.setContentsMargins(5, 0, 5, 0)  # Add some padding around the layout

        # Save Button
        saveButton = QPushButton("Save")
        saveButton.setFixedSize(QSize(60, 20))
        saveButton.setStyleSheet("QPushButton { background-color: black; color: white; border: 2px solid white; }")
        saveButton.clicked.connect(self.onSaveClicked)  # Connect to the save method

        # Close Button
        closeButton = QPushButton("Exit")
        closeButton.setFixedSize(QSize(60, 20))
        closeButton.setStyleSheet("QPushButton { background-color: black; color: white; border: 2px solid white;}")
        closeButton.clicked.connect(self.onCloseClicked)

        titleLabel = QLabel("Notice Editor - Joël Müller - Version 0.1")
        titleLabel.setStyleSheet("font-size: 10px; color: #FFFFFF; font-weight: bold;")  # Adjusted font size

        # Add stretch on both sides of the label to center it in the layout
        # Layout setup
        titleBarLayout.addWidget(titleLabel)
        titleBarLayout.addStretch()
        titleBarLayout.addWidget(saveButton)  # Add Save button
        titleBarLayout.addWidget(closeButton)  # Add Close button

        # Add the title frame to the main layout
        mainLayout.addWidget(titleFrame)

        # First column
        firstColumn = QVBoxLayout()
        firstColumn.addWidget(QLabel("First Column Top"))
        firstColumn.addWidget(QLabel("First Column Bottom"))

        # Second column
        secondColumn = QVBoxLayout()
        buttonRowLayout = QHBoxLayout()
        buttonRowLayout.setSpacing(10)  # Set spacing between widgets in the layout to 0
        buttonRowLayout.setContentsMargins(5, 0, 5, 0)  # Set the layout's margins to 20

        # buttonRowLayout.addStretch(0)
        sizeLabel = QLabel("Textsize:")
        sizeLabel.setStyleSheet("font-size: 25px; color: #000000; background-color: lightgrey; border: 5px solid grey;")
        # Add Widgets
        buttonRowLayout.addWidget(self.adjustSizeToPercentageBoldButton())
        buttonRowLayout.addWidget(self.adjustSizeToPercentageKursivButton())
        buttonRowLayout.addWidget(self.adjustSizeToPercentageUnderlineButton())
        buttonRowLayout.addWidget(sizeLabel)
        buttonRowLayout.addWidget(self.adjustSizeToPercentageDropdown())

        secondColumn.addLayout(buttonRowLayout)

        secondColumn.addWidget(QLabel("Second Column Top"))
        secondColumn.addWidget(QLabel("Second Column Bottom"))

        # Layout for columns
        columnsLayout = QHBoxLayout()
        # Add first column to the columns layout
        columnsLayout.addLayout(firstColumn)

        #  Layout for seperator
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.VLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        separator.setLineWidth(10)
        separator.setFixedWidth(10)
        separator.setStyleSheet("QFrame { color: black; border: 10px solid black; }")

        # Add the separator to the layout
        columnsLayout.addWidget(separator)

        # Add second column to the columns layout
        columnsLayout.addLayout(secondColumn)

        # Add the columns layout below the taskbar layout
        mainLayout.addLayout(columnsLayout)

        # Show the window in full-screen mode
        self.showFullScreen()

    def adjustSizeToPercentageBoldButton(self):
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
        calculatedWidth = int(size_width * widthPercentage)
        calculatedHeight = int(size_height * heightPercentage)

        # Set the calculated size to the widget

        boldButton.setFixedSize(QSize(calculatedWidth, calculatedHeight))
        boldButton.setStyleSheet(buttonStyle)
        boldButton.clicked.connect(self.onSaveClicked)  # Connect to the save method

        return boldButton

    def adjustSizeToPercentageKursivButton(self):
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
        calculatedWidth = int(size_width * widthPercentage)
        calculatedHeight = int(size_height * heightPercentage)

        # Set the calculated size to the widget

        kursivButton.setFixedSize(QSize(calculatedWidth, calculatedHeight))
        kursivButton.setStyleSheet(buttonStyle)
        kursivButton.clicked.connect(self.onSaveClicked)  # Connect to the save method

        return kursivButton

    def adjustSizeToPercentageUnderlineButton(self):
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
        calculatedWidth = int(size_width * widthPercentage)
        calculatedHeight = int(size_height * heightPercentage)

        # Set the calculated size to the widget

        underlineButton.setFixedSize(QSize(calculatedWidth, calculatedHeight))
        underlineButton.setStyleSheet(buttonStyle)
        underlineButton.clicked.connect(self.onSaveClicked)  # Connect to the save method

        return underlineButton

    def adjustSizeToPercentageDropdown(self):
        # Example widget
        sizeDropdown = QComboBox()

        # Calculate size as a percentage of the parent widget's size
        widthPercentage = 0.03  # 3% of parent's width
        heightPercentage = 0.05  # 5% of parent's height

        # Calculate the absolute size based on percentage
        calculatedWidth = int(size_width * widthPercentage)
        calculatedHeight = int(size_height * heightPercentage)

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
    def onSaveClicked():
        # Implement your save functionality here
        print("Save button clicked")

    @staticmethod
    def onCloseClicked(self):
        # Close here
        self.close()


# Run the application
app = QApplication(sys.argv)
screen = app.primaryScreen()
size = screen.size()
size_width = size.width()
size_height = size.height()

window = MainWindow()
window.show()
app.exec()

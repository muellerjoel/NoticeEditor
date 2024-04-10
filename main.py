import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame,
                             QComboBox)
from PyQt6.QtCore import Qt, QSize  # Import Qt for alignment and other constants

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
        closeButton.setStyleSheet("QPushButton { background-color: black; color: white; border: 2px solid white; }")
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

        buttonRowLayout.addStretch(1)
        sizeLabel = QLabel("Textsize:")
        sizeLabel.setStyleSheet("font-size: 20px; color: #000000; font-weight: bold;")
                    #Add Widgets
        buttonRowLayout.addWidget(self.adjustSizeToPercentageBoldButton())
        buttonRowLayout.addWidget(self.adjustSizeToPercentageKursivButton())
        buttonRowLayout.addWidget(self.adjustSizeToPercentageUnderlineButton())
        buttonRowLayout.addWidget(sizeLabel)
        buttonRowLayout.addWidget(self.adjustSizeToPercentageDropwdown())

        secondColumn.addLayout(buttonRowLayout)


        secondColumn.addWidget(QLabel("Second Column Top"))
        secondColumn.addWidget(QLabel("Second Column Bottom"))

        # Layout for columns
        columnsLayout = QHBoxLayout()
        # Add columns to the columns layout
        columnsLayout.addLayout(firstColumn)
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
                            background-color: white;
                            font-size: 20px;
                            font-weight: bold;
                            color: black;
                            border: 5px solid black;
                        }"""

        # Calculate size as a percentage of the parent widget's size
        parentSize = self.size()  # Get the size of the parent widget
        widthPercentage = 0.5  # 50% of parent's width
        heightPercentage = 0.1  # 10% of parent's height

        # Calculate the absolute size based on percentage
        calculatedWidth = int(parentSize.width() * widthPercentage)
        calculatedHeight = int(parentSize.height() * heightPercentage)

        # Set the calculated size to the widget

        boldButton.setFixedSize(QSize(calculatedWidth, calculatedHeight))
        boldButton.setStyleSheet(buttonStyle)
        boldButton.clicked.connect(self.onSaveClicked)  # Connect to the save method

        return  boldButton


    def adjustSizeToPercentageKursivButton(self):
        # Example widget
        kursivButton = QPushButton("Kursiv")
        buttonStyle = """
                QPushButton {
                    background-color: white;
                    font-size: 20px;
                    font-weight: bold;
                    color: black;
                    border: 5px solid black;
                }
                """
        # Calculate size as a percentage of the parent widget's size
        parentSize = self.size()  # Get the size of the parent widget
        widthPercentage = 0.5  # 50% of parent's width
        heightPercentage = 0.1  # 10% of parent's height

        # Calculate the absolute size based on percentage
        calculatedWidth = int(parentSize.width() * widthPercentage)
        calculatedHeight = int(parentSize.height() * heightPercentage)

        # Set the calculated size to the widget

        kursivButton.setFixedSize(QSize(calculatedWidth, calculatedHeight))
        kursivButton.setStyleSheet(buttonStyle)
        kursivButton.clicked.connect(self.onSaveClicked)  # Connect to the save method

        return  kursivButton

    def adjustSizeToPercentageUnderlineButton(self):
        # Example widget
        underlineButton = QPushButton("Underline")
        buttonStyle = """
                QPushButton {
                    background-color: white;
                    font-size: 20px;
                    font-weight: bold;
                    color: black;
                    border: 5px solid black;
                }
                """

        # Calculate size as a percentage of the parent widget's size
        parentSize = self.size()  # Get the size of the parent widget
        widthPercentage = 0.5  # 50% of parent's width
        heightPercentage = 0.1  # 10% of parent's height

        # Calculate the absolute size based on percentage
        calculatedWidth = int(parentSize.width() * widthPercentage)
        calculatedHeight = int(parentSize.height() * heightPercentage)

        # Set the calculated size to the widget

        underlineButton.setFixedSize(QSize(calculatedWidth, calculatedHeight))
        underlineButton.setStyleSheet(buttonStyle)
        underlineButton.clicked.connect(self.onSaveClicked)  # Connect to the save method

        return underlineButton

    def adjustSizeToPercentageDropwdown(self):
        # Example widget
        sizeDropdown = QComboBox()
        buttonStyle = """
                   QPushButton {
                       background-color: white;
                       font-size: 20px;
                       font-weight: bold;
                       color: black;
                       border: 5px solid black;
                   }
                   """

        # Calculate size as a percentage of the parent widget's size
        parentSize = self.size()  # Get the size of the parent widget
        widthPercentage = 0.5  # 50% of parent's width
        heightPercentage = 0.1  # 10% of parent's height

        # Calculate the absolute size based on percentage
        calculatedWidth = int(parentSize.width() * widthPercentage)
        calculatedHeight = int(parentSize.height() * heightPercentage)

            # Set the calculated size to the widget

        sizeDropdown.setFixedSize(QSize(calculatedWidth, calculatedHeight))
        # Dropdown Text size
        sizeDropdown.addItems(["8", "10", "12", "14", "16", "18", "20", "22", "24", "26", "28", "30"])  # Example sizes
        # Adding a label for the size dropdown
        sizeDropdown.setStyleSheet(buttonStyle)

        return sizeDropdown

    def onSaveClicked(self):
        # Implement your save functionality here
        print("Save button clicked")

    def onCloseClicked(self):

    # Close here
        self.close()

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
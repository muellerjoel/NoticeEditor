import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame,  QSpacerItem, QSizePolicy
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

        # Left spacer
        leftSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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

        # Taskbar layout with buttons
        taskbarLayout = QHBoxLayout()
        taskbarLayout.addWidget(QPushButton("Button 1"))
        taskbarLayout.addWidget(QPushButton("Button 2"))

        # Add the taskbar layout below the title frame

        mainLayout.addLayout(taskbarLayout)

        # Layout for columns
        columnsLayout = QHBoxLayout()

        # First column
        firstColumn = QVBoxLayout()
        firstColumn.addWidget(QLabel("First Column Top"))
        firstColumn.addWidget(QLabel("First Column Bottom"))

        # Second column
        secondColumn = QVBoxLayout()
        secondColumn.addWidget(QLabel("Second Column Top"))
        secondColumn.addWidget(QLabel("Second Column Bottom"))

        # Add columns to the columns layout
        columnsLayout.addLayout(firstColumn)
        columnsLayout.addLayout(secondColumn)

        # Add the columns layout below the taskbar layout
        mainLayout.addLayout(columnsLayout)

        # Show the window in full-screen mode
        self.showFullScreen()

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
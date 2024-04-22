import sys
from PyQt6.QtCore import QSize  # Import Qt for alignment and other constants
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget,
                             QVBoxLayout, QHBoxLayout, QLabel, QFrame, QListWidget)
from iobox import IOBox
from notice_list import NoticeList
from buttons import ClickButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Notice Editor GUI")

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
        btn = ClickButton(size_width, size_height)
        saveButton = QPushButton("Save")
        saveButton.setFixedSize(QSize(60, 20))
        saveButton.setStyleSheet("QPushButton { background-color: black; color: white; border: 2px solid white; }")
        saveButton.clicked.connect(btn.on_save_clicked)  # Connect to the save method

        # Close Button
        closeButton = QPushButton("Exit")
        closeButton.setFixedSize(QSize(60, 20))
        closeButton.setStyleSheet("QPushButton { background-color: black; color: white; border: 2px solid white;}")
        closeButton.clicked.connect(btn.on_close_clicked)

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
        centralWidget.setLayout(firstColumn)
        # firstColumn.addWidget(QLabel("First Column Top"))
        # firstColumn.addWidget(QLabel("First Column Bottom"))

        # Second column
        secondColumn = QVBoxLayout()
        centralWidget.setLayout(secondColumn)
        buttonRowLayout = QHBoxLayout()
        buttonRowLayout.setSpacing(10)  # Set spacing between widgets in the layout to 0
        buttonRowLayout.setContentsMargins(5, 0, 5, 0)  # Set the layout's margins to 20

        # buttonRowLayout.addStretch(0)
        sizeLabel = QLabel("Textsize:")
        sizeLabel.setStyleSheet("font-size: 25px; color: #000000; background-color: lightgrey; border: 5px solid grey;")

        # List Widget
        self.list_widget = QListWidget()
        self.list_widget.addItem("Add a new notice by tap the add button")
        self.list_widget.setAlternatingRowColors(True)
        # Enable editing of the list items
        self.list_widget.setEditTriggers(QListWidget.EditTrigger.DoubleClicked)

        # Button layout
        button_layout = QHBoxLayout()
        nl = NoticeList()

        # Add button
        add_button = QPushButton("Add")
        add_button.clicked.connect(nl.add_item)
        button_layout.addWidget(add_button)

        # Delete button
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(nl.delete_item)
        button_layout.addWidget(delete_button)

        # Add widgets to the main layout
        io_box = IOBox(size_width, size_height)
        # Add Widgets
        buttonRowLayout.addWidget(btn.adjust_size_to_percentage_bold_button())
        buttonRowLayout.addWidget(btn.adjust_size_to_percentage_kursiv_button())
        buttonRowLayout.addWidget(btn.adjust_size_to_percentage_underline_button())
        buttonRowLayout.addWidget(sizeLabel)
        buttonRowLayout.addWidget(btn.adjust_size_to_percentage_dropdown())
        firstColumn.addWidget(self.list_widget)
        firstColumn.addLayout(button_layout)
        secondColumn.addLayout(buttonRowLayout)
        secondColumn.addWidget(io_box.adjust_size_to_percentage_iobox())

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


# Run the application
app = QApplication(sys.argv)
screen = app.primaryScreen()
size = screen.size()
size_width = size.width()
size_height = size.height()
window = MainWindow()
window.show()
app.exec()

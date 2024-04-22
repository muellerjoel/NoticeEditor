from PyQt6.QtWidgets import QLineEdit, QWidget
from PyQt6.QtCore import QSize


class IOBox:
    def __init__(self, size_width, size_height):
        self.size_width = size_width
        self.size_height = size_height
    def adjust_size_to_percentage_iobox(self):
        # Example widget
        io_box = QLineEdit()
        io_box.setMaxLength(100)


        # widget.setReadOnly(True) # uncomment this to make readonly

        io_box.returnPressed.connect(self.return_pressed)
        io_box.selectionChanged.connect(self.selection_changed)
        io_box.textChanged.connect(self.text_changed)
        io_box.textEdited.connect(self.text_edited)

        # Calculate size as a percentage of the parent widget's size
        widthPercentage = 0.8333  # 83.33% of parent's width (5/6)
        heightPercentage = 0.9  # 90% of parent's height

        # Calculate the absolute size based on percentage

        calculatedWidth = int(self.size_width * widthPercentage)
        calculatedHeight = int(self.size_height * heightPercentage)
        # Set the calculated size to the widget

        io_box.setFixedSize(QSize(calculatedWidth, calculatedHeight))
        io_box.setPlaceholderText("Enter your text")

        return io_box
    def return_pressed(self):
        print("Return pressed!")

    # self.secondColumn.addWidget(self.adjustSizeToPercentageIOBox().setPlaceholderText("BOOM"))

    def selection_changed(self):
        self.centralWidget = QWidget()
        print("Selection changed")
        print(self.centralWidget.selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)
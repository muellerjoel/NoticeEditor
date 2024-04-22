from PyQt6.QtWidgets import QPushButton, QHBoxLayout, QWidget, QListWidget, QListWidgetItem
from PyQt6.QtCore import Qt


class NoticeList:
    def __init__(self):
        self.centralWidget = None
        self.list_widget = None

    def notice_list(self):
        # List Widget
        self.centralWidget = QWidget()
        self.list_widget = QListWidget()
        self.list_widget.addItem("Add a new notice by tap the add button")
        self.list_widget.setAlternatingRowColors(True)
        # Enable editing of the list items
        self.list_widget.setEditTriggers(QListWidget.EditTrigger.DoubleClicked)

        # Button layout
        button_layout = QHBoxLayout()

        # Add button
        add_button = QPushButton("Add")
        add_button.clicked.connect(self.add_item)
        button_layout.addWidget(add_button)

        # Delete button
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.delete_item)
        button_layout.addWidget(delete_button)

        return self.list_widget

    def add_item(self):
        new_item = QListWidgetItem("New Item")
        new_item.setFlags(new_item.flags() | Qt.ItemFlag.ItemIsEditable)
        self.list_widget.addItem(new_item)
        self.list_widget.editItem(new_item)  # Automatically start editing the new item

    def delete_item(self):
        current_item = self.list_widget.currentItem()
        if current_item:
            row = self.list_widget.row(current_item)
            self.list_widget.takeItem(row)

    def return_pressed(self):
        print("Return pressed!")

    # self.secondColumn.addWidget(self.adjustSizeToPercentageIOBox().setPlaceholderText("BOOM"))

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)

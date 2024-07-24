import sys
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QFileDialog
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QButtonGroup, QRadioButton
import file_organizer  # 导入主逻辑模块


def code_to_message(code):
    if code == 0:
        return 'success!'
    elif code == -1:
        return 'unknown error!'
    elif code == 1:
        return 'empty source directory!'
    else:
        return 'empty message, hhh'


class PhotoOrganizer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Organizer")
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 单选按钮组
        radio_layout = QHBoxLayout()
        self.radio_group = QButtonGroup(self)
        self.radio_by_date = QRadioButton("按日期聚合")
        self.radio_by_month = QRadioButton("按月聚合")
        self.radio_by_date.setChecked(True)
        self.radio_group.addButton(self.radio_by_date)
        self.radio_group.addButton(self.radio_by_month)
        radio_layout.addWidget(self.radio_by_date)
        radio_layout.addWidget(self.radio_by_month)
        layout.addLayout(radio_layout)

        self.source_label = QLabel("Source Directory:")
        self.source_edit = QLineEdit()
        self.source_button = QPushButton("Select Source")
        self.source_button.clicked.connect(self.select_source)
        layout.addWidget(self.source_label)
        layout.addWidget(self.source_edit)
        layout.addWidget(self.source_button)

        self.target_label = QLabel("Target Directory:")
        self.target_edit = QLineEdit()
        self.target_button = QPushButton("Select Target")
        self.target_button.clicked.connect(self.select_target)
        layout.addWidget(self.target_label)
        layout.addWidget(self.target_edit)
        layout.addWidget(self.target_button)

        self.organize_button = QPushButton("Organize Files")
        self.organize_button.clicked.connect(self.organize)
        layout.addWidget(self.organize_button)

    def select_source(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Source Directory")
        self.source_edit.setText(directory)

    def select_target(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Target Directory")
        self.target_edit.setText(directory)

    def organize(self):
        group_type = self.get_selected_option()
        source_dir = self.source_edit.text()
        target_dir = self.target_edit.text()
        code = file_organizer.organize_files(source_dir, target_dir, group_type=group_type)
        self.show_message_box(code_to_message(code))

    def show_message_box(self, text, button=QMessageBox.StandardButton.Ok):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle('Information')
        msg_box.setText(text)
        msg_box.setStandardButtons(button)
        msg_box.exec()

    def get_selected_option(self):
        if self.radio_by_date.isChecked():
            return 1
        elif self.radio_by_month.isChecked():
            return 2


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhotoOrganizer()
    window.show()
    sys.exit(app.exec())
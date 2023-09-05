import sys
import os
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QProgressBar, QMessageBox
from PyQt6.QtGui import QIcon

from WorkerThread import WorkerThread

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()

        # Text zones and buttons
        self.textbox1 = QLineEdit()
        self.button1 = QPushButton("Select Folder")
        self.textbox2 = QLineEdit()
        self.button2 = QPushButton("Select Folder")

        # Button to call the function.
        self.button_function = QPushButton("Retrieve return values")

        # Progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.hide()

        # Icon
        self.logo_path = "Images/logo_pierrot.png"
        icon = QIcon(self.logo_path)

        # Link function to button.
        self.button1.clicked.connect(self.select_folder1)
        self.button2.clicked.connect(self.select_folder2)
        self.button_function.clicked.connect(self.calling_main_console)

        # Add elements to layout.
        layout.addWidget(QLabel("Project folder :"))

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.textbox1)
        hbox1.addWidget(self.button1)
        layout.addLayout(hbox1)

        layout.addWidget(QLabel("Folder containing the functions whose return values you are looking for :"))

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.textbox2)
        hbox2.addWidget(self.button2)
        layout.addLayout(hbox2)

        layout.addWidget(self.button_function)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)
        self.setWindowTitle("Pierrot")
        self.setWindowIcon(icon)
        QApplication.setStyle('Fusion')

        self.show()

    def select_folder1(self):
        folder = QFileDialog.getExistingDirectory(self, "Select File")
        self.textbox1.setText(folder)

    def select_folder2(self):
        folder = QFileDialog.getExistingDirectory(self, "Select File")
        self.textbox2.setText(folder)

    def calling_main_console(self):
        """
        Call the function that will create the excel.
        """
        scope_folder = self.textbox1.text()
        project_folder = self.textbox2.text()
        
        areOutputPathCorrect = self.checkInputPath(project_folder, scope_folder)
        
        if areOutputPathCorrect:
            output_file_path = self.chooseOutputFile()
            if output_file_path is not None:
                # If we are here, the two folders exists and the process can be done.
                # Disable the click on the buttons
                self.button1.setEnabled(False)
                self.button2.setEnabled(False)
                self.button_function.setEnabled(False)

                # Show the progress bar
                self.progress_bar.show()

                # Instanciation of the Worker thread.
                self.worker_thread = WorkerThread(project_folder, scope_folder, output_file_path)
                self.worker_thread.progress_updated.connect(self.update_progress_bar)
                self.worker_thread.work_finished.connect(self.on_work_finished)
                self.worker_thread.start()

    # If one of the path is incorreect, we have to set a dialog of error.
    # This dialog depends on which path is mispelled.
    def checkInputPath(self, project_folder: str, scope_folder: str) -> bool:
        if (not os.path.isdir(project_folder)) and (not os.path.isdir(scope_folder)):
            self.showDialog(QMessageBox.Icon.Critical,
                            "Warning",
                            "Both path are incorrect.")
            return False
        elif (not os.path.isdir(project_folder)):
            self.showDialog(QMessageBox.Icon.Critical,
                            "Warning",
                            "The path of the functions to retrieve is incorrect.")
            return False
        elif (not os.path.isdir(scope_folder)):
            self.showDialog(QMessageBox.Icon.Critical,
                            "Warning",
                            "The path of the project is incorrect.")
            return False
        
        # If this line is reached, it means that both path are correct.
        return True

    # Choose the output path / name of the output file
    def chooseOutputFile(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Output File", "", "Excel Files (*.xlsx);;All Files (*)")
        if file_path:
            return file_path
        else:
            self.showDialog(QMessageBox.Icon.Warning,
                            "Warning",
                            "You have to choose a path to save the output file.")
            return None
    
    # Show an error message on a dialog box
    def showDialog(self, warningLevel, title: str, text: str) -> None:
        dialog = QMessageBox()
        dialog.setWindowTitle(title)
        dialog.setText(text)
        dialog.setIcon(warningLevel)
        dialog.setWindowIcon(QIcon(self.logo_path))
        dialog.exec()

    # Function to update the progress of the bar
    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)

    # Function to hide the element at the end of the function.
    def on_work_finished(self):
        # Reinitialisation of the progress bar
        self.progress_bar.setValue(0)
        
        # Hidding the progress bar
        self.progress_bar.hide()
        
        # Allow the user to click on the buttons
        self.button1.setEnabled(True)
        self.button2.setEnabled(True)
        self.button_function.setEnabled(True)

        # Prevent the user that the work is done and opening the window explorer if he asks to.
        self.showDialog(QMessageBox.Icon.Information,
                        "Work completed",
                        "Pierrot just ended retrieving returned values.")

if __name__ == "__main__":
   app = QApplication(sys.argv)
   window = MyWidget()
   sys.exit(app.exec())
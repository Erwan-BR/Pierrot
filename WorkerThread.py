from PyQt6.QtCore import QThread, pyqtSignal

from create_excel import create_excel

class WorkerThread(QThread):
    """
    This class is for containing the work in a thread.
    It will avoid having a freezing page and allows to have a progress bar.
    """
    progress_updated = pyqtSignal(int)
    work_finished = pyqtSignal()

    def __init__(self, project_folder: str, scope_folder: str, output_file_path: str):
        super().__init__()
        self.project_folder = project_folder
        self.scope_folder = scope_folder
        self.output_file_path = output_file_path

    def run(self):
        create_excel(self.project_folder, self.scope_folder, self.update_progress, self.output_file_path)
        self.work_finished.emit()

    def update_progress(self, value):
        self.progress_updated.emit(value)

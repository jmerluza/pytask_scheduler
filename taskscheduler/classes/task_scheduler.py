import win32com.client
from taskscheduler.classes import NewTask

class TaskScheduler:
    def __init__(self):
        self.client = win32com.client.gencache.EnsureDispatch("Schedule.Service")
        self.client.Connect()
        self.root_folder = self.client.GetFolder("\\")

    def __find_folder(self, folder, folder_name: str) -> str:
        """Find and return the folder path from task scheduler."""
        folders = folder.GetFolders(0)
        for subfolder in folders:
            if subfolder.Name == folder_name:
                return subfolder.Path
            fpath = self.__find_folder(subfolder, folder_name)
            if fpath:
                return fpath
        return None

    def get_folder(self, folder_name: str|None=None):
        """Get the folder object.
        
        Parameters:
            folder_name (`str`): Folder name to look for.

        Returns:
            TaskFolder object.
        """

        if folder_name is None:
            return self.root_folder
        else:
            folder_path = self.__find_folder(self.root_folder, folder_name)
            if folder_path:
                folder = self.client.GetFolder(folder_path)
                return folder
            else:
                raise ValueError(f"Could not find {folder_name}")
    
    def create_task(
        self,
        folder_name: str,
        task_name: str
    ):
        folder = self.get_folder(folder_name)
        new_taskdef = self.client.NewTask(0)
        return NewTask(new_taskdef)

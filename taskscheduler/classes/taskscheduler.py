import win32com.client

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

    def get_folder(self, folder_name: str):
        """Get the folder com object based on folder name.
        
        Parameters:
            folder_name (`str`): Folder name to look for.

        Returns:
            task scheduler folder com object.
        """
        folder_path = self.__find_folder(self.root_folder, folder_name)
        if folder_path:
            folder = self.client.GetFolder(folder_path)
            return folder
        else:
            raise ValueError(f"Could not find {folder_name}")

"""This module covers the TaskFolder scripting object. 
https://learn.microsoft.com/en-us/windows/win32/taskschd/taskfolder"""

class TaskFolder:
    def __init__(self, folder_obj):
        self.folder = folder_obj
        self.subfolders = [f.Name for f in self.folder.GetFolders(0)]
        self.tasks = [t.Name for t in self.folder.GetTasks(0)]

    def info(self) -> dict:
        """Folder information stored in a hash table.
        
        Returns:
            Dictionary containing folder information.
        """
        return {
            "subfolders":self.subfolders,
            "tasks":self.tasks,
            "folder_name":self.folder.Name,
            "folder_path":self.folder.Path,
        }

    def create_folder(self, folder_name: str):
        """Creates a new subfolder.
        
        Parameters:
            folder_name (`str`): Name for the subfolder.

        Returns:
            TaskFolder object.
        """
        if folder_name in self.subfolders:
            raise ValueError(f"{folder_name} already exists!")
        else:
            new_folder = self.folder.CreateFolder(folder_name)
            return TaskFolder(new_folder)

    def delete_folder(self, folder_name: str):
        """Deletes the subfolder.

        Parameters:
            folder_name (`str`): Name for the subfolder.
        """
        if folder_name in self.subfolders:
            self.folder.DeleteFolder(folder_name)
        else:
            raise ValueError(f"{folder_name} does not exist!")

    def get_task(self, task_name: str):
        """Get the task object.
        
        Returns:
            RegisteredTask object.
        """
        if task_name in self.tasks:
            rtask = self.folder.GetTask(task_name)
        else:
            raise ValueError(f"{task_name} does not exist in this folder!")

        return rtask

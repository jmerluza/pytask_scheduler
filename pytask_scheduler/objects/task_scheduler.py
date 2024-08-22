from typing import Literal
from datetime import datetime
import win32com.client
from pytask_scheduler.objects import NewTask, TaskTrigger, TaskAction

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
        trigger_type: Literal["daily","weekly","monthly","monthlydow","one-time"],
        start_date: datetime.date,
        start_time: datetime.time,
        days_interval: int,
        weeks_interval: int,
        days_of_week: int, 
        days_of_month: int,
        months_of_year: int,
        weeks_of_month: int,
        action_type: Literal["exec","com-handler","email","show-message"],
        action_arg: str,
        action_file: str,
        action_working_dir: str,
        task_name: str,
        task_description: str,
        allow_demand_start: bool,
        start_when_available: bool,
        enabled: bool,
        hidden: bool,
        restart_interval: str,
        restart_count: int,
        execution_time_limit: str,
        multiple_instances: int
        
    ):
        """
        Creates a new task in a folder.
        1. Create task definition.
        2. Create task trigger.
        3. Create task action.
        4. Update task information.
        5. Update task settings.
        """
        folder = self.get_folder(folder_name)

        # create task def.
        new_taskdef = self.client.NewTask(0)

        # create new trigger.
        match trigger_type:
            case "daily":
                new_trigger = TaskTrigger(new_taskdef).create_daily_trigger(
                    start_date=start_date,
                    start_time=start_time,
                    days_interval=days_interval
                )

            case "weekly":
                new_trigger = TaskTrigger(new_taskdef).create_weekly_trigger(
                    start_date=start_date,
                    start_time=start_time,
                    weeks_interval=weeks_interval,
                    days_of_week=days_of_week
                )

            case "monthly":
                new_trigger = TaskTrigger(new_taskdef).create_monthly_trigger(
                    trigger_type="month",
                    start_date=start_date,
                    start_time=start_time,
                    days_of_month=days_of_month,
                    days_of_week=days_of_week,
                    months_of_year=months_of_year,
                    weeks_of_month=weeks_of_month
                )

            case "monthlydow":
                new_trigger = TaskTrigger(new_taskdef).create_monthly_trigger(
                    trigger_type="dow",
                    start_date=start_date,
                    start_time=start_time,
                    days_of_month=days_of_month,
                    days_of_week=days_of_week,
                    months_of_year=months_of_year,
                    weeks_of_month=weeks_of_month
                )

            case "one-time":
                new_trigger = TaskTrigger(new_taskdef).create_one_time_trigger(
                    start_date=start_date,
                    start_time=start_time
                )

        # create a new task action
        match action_type:
            case "exec":
                new_action = TaskAction(new_taskdef).create_execution_action(
                    argument=action_arg,
                    filepath=action_file,
                    working_dir=action_working_dir
                )
            case "com-handler":
                raise NotImplementedError("Create com handler action has not been implemented")
            case "email":
                raise NotImplementedError("Create send email action has not been implemented")
            case "show-message":
                raise NotImplementedError("Create show message action has not been implemented")
        
        # update task information
        new_taskdef.Name = task_name


        return NewTask(new_taskdef)

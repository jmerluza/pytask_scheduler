from typing import Literal
from datetime import datetime
import polars as pl
import win32com.client
from pytask_scheduler.objects import NewTask, TaskTrigger, TaskAction, TaskFolder
from pytask_scheduler.frames import TaskFrame

class TaskScheduler:
    def __init__(self):
        self.client = win32com.client.gencache.EnsureDispatch("Schedule.Service")
        self.client.Connect()
        self.root_folder = self.client.GetFolder("\\")
        self.folders = [f.Name for f in self.root_folder.GetFolders(0)]

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
            return TaskFolder(self.root_folder)
        else:
            folder_path = self.__find_folder(self.root_folder, folder_name)
            if folder_path:
                folder = self.client.GetFolder(folder_path)
                return TaskFolder(folder)
            else:
                raise ValueError(f"Could not find {folder_name}")

    def __list_tasks_info_in_folder(self, folder, folder_name: str, tasks_info_list: list):
        """Recursively list all tasks within folders."""

        # extract and append all the tasks info in the list.
        tasks = folder.tasks
        for t in tasks:
            tasks_info_list.append(folder.get_task(t).info())

        # walk through all subfolders and get the tasks info.
        subfolders = folder.subfolders
        for sf in subfolders:
            subfolder = self.get_folder(sf)
            self.__list_tasks_info_in_folder(
                subfolder,
                folder_name + "\\" + sf,
                tasks_info_list
            )

    def get_all_tasks(self) -> pl.DataFrame:
        """Method for extracting all the scheduled tasks."""
        root_folder = self.get_folder()
        tasks_info_list = []
        self.__list_tasks_info_in_folder(root_folder, "\\", tasks_info_list)
        df = pl.DataFrame(tasks_info_list)
        return TaskFrame(df)

    def create_task(
        self,
        folder_name: str,
        trigger_type: Literal["daily","weekly","monthly","monthlydow","one-time"],
        start_date: datetime.date,
        start_time: datetime.time,
        days_interval: int|None,
        weeks_interval: int|None,
        days_of_week: int|None,
        days_of_month: int|None,
        months_of_year: int|None,
        weeks_of_month: int|None,
        action_type: Literal["exec","com-handler","email","show-message"],
        action_arg: str|None,
        action_file: str,
        action_working_dir: str|None,
        task_name: str,
        task_description: str,
        allow_demand_start: bool|None,
        start_when_available: bool|None,
        enabled: bool|None,
        hidden: bool|None,
        restart_interval: str|None,
        restart_count: int|None,
        execution_time_limit: str|None,
        multiple_instances: int|None

    ):
        """Create a new task.

        Parameters:
            folder_name (`str`): Folder name in which the task will be registered to.
            trigger_type (`str`): `Literal["daily","weekly","monthly","monthlydow","one-time"]` \
                Indicates the type of trigger to create.
            start_date (`datetime.date`): Date when the trigger is activated.
            start_time (`datetime.time`): Time when the trigger is activated.
            days_interval (`int`): Required for a daily trigger. Sets the interval between the \
                days in the schedule. An interval of 1 produces a daily schedule, an interval \
                of 2 produces an every-other day schedule.
            weeks_interval (`int`): Required for a weekly trigger. Sets the interval between \
                the weeks in the schedule. An interval of 1 produces a weekly schedule, an \
                interval of 2 produces an every-other week schedule.
            days_of_week (`int`):
            days_of_month (`int`):
            months_of_year (`int`):
            weeks_of_month (`int`):
            action_type (`str`): Literal["exec","com-handler","email","show-message"],
            action_arg (`str`):
            action_file (`str`):
            action_working_dir (`str`):
            task_name (`str`):
            task_description (`str`):
            allow_demand_start (`bool`):
            start_when_available (`bool`):
            enabled (`bool`):
            hidden (`bool`):
            restart_interval (`str`):
            restart_count (`int`):
            execution_time_limit (`str`):
            multiple_instances (`int`):

        """
        folder = self.get_folder(folder_name)

        # create task def.
        new_taskdef = self.client.NewTask(0)

        # create new trigger.
        match trigger_type:
            case "daily":
                new_taskdef = TaskTrigger(new_taskdef).create_daily_trigger(
                    start_date=start_date,
                    start_time=start_time,
                    days_interval=days_interval
                )

            case "weekly":
                new_taskdef = TaskTrigger(new_taskdef).create_weekly_trigger(
                    start_date=start_date,
                    start_time=start_time,
                    weeks_interval=weeks_interval,
                    days_of_week=days_of_week
                )

            case "monthly":
                new_taskdef = TaskTrigger(new_taskdef).create_monthly_trigger(
                    trigger_type="month",
                    start_date=start_date,
                    start_time=start_time,
                    days_of_month=days_of_month,
                    days_of_week=days_of_week,
                    months_of_year=months_of_year,
                    weeks_of_month=weeks_of_month
                )

            case "monthlydow":
                new_taskdef = TaskTrigger(new_taskdef).create_monthly_trigger(
                    trigger_type="dow",
                    start_date=start_date,
                    start_time=start_time,
                    days_of_month=days_of_month,
                    days_of_week=days_of_week,
                    months_of_year=months_of_year,
                    weeks_of_month=weeks_of_month
                )

            case "one-time":
                new_taskdef = TaskTrigger(new_taskdef).create_one_time_trigger(
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

        # add task description
        new_taskdef.RegistrationInfo.Description = task_description

        # task settings
        new_taskdef.Settings.AllowDemandStart = allow_demand_start
        new_taskdef.Settings.StartWhenAvailable = start_when_available
        new_taskdef.Settings.Enabled = enabled
        new_taskdef.Settings.Hidden = hidden
        new_taskdef.Settings.RestartInterval = restart_interval
        new_taskdef.Settings.RestartCount = restart_count
        new_taskdef.Settings.ExecutionTimeLimit = execution_time_limit
        new_taskdef.Settings.MultipleInstances = multiple_instances

        folder.register_new_task(task_name,new_taskdef)
        return NewTask(new_taskdef)

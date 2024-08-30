import polars as pl
import win32com.client
from typing import Literal
from datetime import datetime
from pytask_scheduler import (
    TaskActionTypes,
    TaskTriggerTypes,
    TaskCreationTypes,
    TaskLogonTypes,
    TaskFrame
)

class TaskScheduler:
    """Task Scheduler object."""
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

class NewTask:
    """This object covers topics from the TaskDefinition scripting object.
    https://learn.microsoft.com/en-us/windows/win32/taskschd/taskdefinition
    """
    def __init__(self, taskdef_obj):
        self.taskdef = taskdef_obj

class RegisteredTask:
    """This object covers some of the api from the RegisteredTask scripting object.
        https://learn.microsoft.com/en-us/windows/win32/taskschd/registeredtask
    """
    def __init__(self, rtask_obj):
        self.rtask = rtask_obj
        self.taskdef = self.rtask.Definition
        self.reg_info = self.taskdef.RegistrationInfo

    def info(self) -> dict:
        """Information on registered task."""
        return {
            "name":self.rtask.Name,
            "enabled":self.rtask.Enabled,
            "task_state":self.rtask.State,
            "next_run_time":self.rtask.NextRunTime,
            "last_run_time":self.rtask.LastRunTime,
            "last_task_result":self.rtask.LastTaskResult,
            "number_of_missed_runs":self.rtask.NumberOfMissedRuns,
            "task_path":self.rtask.Path,
            "author":self.reg_info.Author,
            "registration_date":self.reg_info.Date,
            "task_description":self.reg_info.Description,
            "task_source":self.reg_info.Source
        }

    def update_registration_info(self, task_description: str):
        """Updates the registration info for a task.

        Parameter:
            task_description (`str`): Description of a task.
        
        Support:
            Only supports updating the task description.

        Returns:
            TaskDefinition object.
        """
        self.reg_info.Description = task_description
        return self.taskdef


class TaskAction:
    """This object covers topics from the Action scripting object.
    https://learn.microsoft.com/en-us/windows/win32/taskschd/action
    """
    def __init__(self, taskdef_obj):
        self.action = taskdef_obj.Actions

    def __set_action_type(self, action_type: int):
        self.action.Create(action_type)

    def create_execution_action(
        self,
        argument: str,
        filepath: str|None="",
        working_dir: str|None=""
    ):
        """Creates an action that executes a command-line operation. For example, \
            can execute a batch file script.
        https://learn.microsoft.com/en-us/windows/win32/taskschd/execaction

        Parameters:
            argument (`str`): Sets the arguments associated with the command-line operation.
            filepath (`str`): Sets the path to an executable file.
            working_dir (`str`): Sets the directory that contains either the executable file \
            or the files that are used by the executable file.
        """
        self.__set_action_type(TaskActionTypes.TASK_ACTION_EXEC)
        self.action.Path = filepath
        self.action.Arguments = argument
        self.action.WorkingDirectory = working_dir
        return self.action

    def create_com_handler_action(self):
        """Creates an action that fires a handler.
        https://learn.microsoft.com/en-us/windows/win32/taskschd/comhandleraction
        """
        raise NotImplementedError("Create com handle action has not been implemented")

    def create_send_email_action(self):
        """Creates an action that send an email message.
        https://learn.microsoft.com/en-us/windows/win32/taskschd/emailaction
        """
        raise NotImplementedError("Create send email action has not been implemented")

    def create_show_message_action(self):
        """Creates an action that shows a message box when a task is activated.
        https://learn.microsoft.com/en-us/windows/win32/taskschd/showmessageaction
        """
        raise NotImplementedError("Create show message action has not been implemented")

class TaskFolder:
    """This object covers the TaskFolder scripting object. 
        https://learn.microsoft.com/en-us/windows/win32/taskschd/taskfolder
    """

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
        """Get the task object by name.
        
        Returns:
            RegisteredTask object.
        """
        if task_name in self.tasks:
            rtask = self.folder.GetTask(task_name)
        else:
            raise ValueError(f"{task_name} does not exist in this folder!")

        return RegisteredTask(rtask)
    
    def register_new_task(
        self,
        task_name: str,
        new_taskdef
    ):
        self.folder.RegisterTaskDefinition(
            task_name,
            new_taskdef,
            TaskCreationTypes.TASK_CREATE_OR_UPDATE,
            "", # no username
            "", # no password
            TaskLogonTypes.TASK_LOGON_NONE
        )

    
class TaskSettings:
    """This object covers topics from the TaskSettings object.
        https://learn.microsoft.com/en-us/windows/win32/taskschd/tasksettings
    """

    def __init__(self, taskdef_obj):
        self.taskdef = taskdef_obj
        self.task_settings = self.taskdef.Settings

    def info(self) -> dict:
        """Get the settings of a task."""
        settings = {
            "AllowDemandStart": self.task_settings.AllowDemandStart,
            "StartWhenAvailable": self.task_settings.StartWhenAvailable,
            "Enabled": self.task_settings.Enabled,
            "Hidden": self.task_settings.Hidden,
            "RestartInterval": self.task_settings.RestartInterval,
            "RestartCount": self.task_settings.RestartCount,
            "ExecutionTimeLimit": self.task_settings.ExecutionTimeLimit,
            "MultipleInstances": self.task_settings.MultipleInstances
        }

        return settings

    def update_settings(
        self,
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
        Updates the settings of a task.
        
        Parameters:
            allow_demand_start (`bool`):
                Gets or sets a boolean value that indicates that the task can be started by using \
                either the run command of the context menu.

            start_when_available (`bool`):
                Gets or sets a boolean value that indicates that the task scheduler can start the \
                task at any time after its scheduled time has passed.

            enabled (`bool`):
                Gets or sets a boolean value that indicates that the task is enabled. The task can \
                be performed only when this setting is True.

            hidden (`bool`):
                Gets or sets a boolean value that indicates that the task will not be visible in \
                the UI. However, admins can override this setting through the use of a \
                'master switch' that makes all tasks visible in the UI.

            restart_interval (`str`):
                Gets or sets a value that specifies how long the task scheduler will \
                attempt to restart the task.

            restart_count (`int`): 
                Gets or sets the number of times that the task scheduler \
                will attempt to restart the task.

            execution_time_limit (`str`): 
                Gets or sets the amount of time allowed to complete the task.

            multiple_instances (`int`): 
                Gets or sets the policy that defines how the task scheduler deals with \
                multiple instances of the task. 
        
        """
        self.task_settings.AllowDemandStart = allow_demand_start
        self.task_settings.StartWhenAvailable = start_when_available
        self.task_settings.Enabled = enabled
        self.task_settings.Hidden = hidden
        self.task_settings.RestartInterval = restart_interval
        self.task_settings.RestartCount = restart_count
        self.task_settings.ExecutionTimeLimit = execution_time_limit
        self.task_settings.MultipleInstances = multiple_instances

        return self.taskdef
    
class TaskTrigger:
    """This module covers topics from the Trigger scripting objects.
        https://learn.microsoft.com/en-us/windows/win32/taskschd/trigger
    """
    def __init__(self, taskdef_obj):
        self.taskdef = taskdef_obj
        self.trigger = self.taskdef.Triggers

    def __set_start_boundary(self, start_date: datetime.date, start_time: datetime.time):
        self.trigger.StartBoundary = datetime.combine(start_date, start_time).isoformat()

    def __set_cadence(self, trigger_type: int):
        self.trigger.Create(trigger_type)

    def create_daily_trigger(
        self,
        start_date: datetime.date,
        start_time: datetime.time,
        days_interval: int
    ):
        """Starts a task based on a daily schedule. 
        https://learn.microsoft.com/en-us/windows/win32/taskschd/dailytrigger
        
        Parameters:
            start_date (`datetime.date`): Date when the trigger is activated.
            start_time (`datetime.time`): Time when the trigger is activated.
            days_interval (`int`): Sets the interval between the days in the schedule. \
                An interval of 1 produces a daily schedule, an interval of 2 produces an \
                every-other day schedule.
        """
        self.__set_cadence(TaskTriggerTypes.TASK_TRIGGER_DAILY)
        self.__set_start_boundary(start_date, start_time)
        self.trigger.DaysInterval = days_interval
        return self.taskdef

    def create_weekly_trigger(
        self,
        start_date: datetime.date,
        start_time: datetime.time,
        weeks_interval: int,
        days_of_week: int
    ):
        """Starts a task based on a weekly schedule. For example, the task starts at 8:00 AM \
            on a specific day of the week every week or every other week.
            https://learn.microsoft.com/en-us/windows/win32/taskschd/weeklytrigger

        Parameters:
            start_date (`datetime.date`): Date when the trigger is activated.
            start_time (`datetime.time`): Time when the trigger is activated.
            weeks_interval (`int`): Sets the interval between the weeks in the schedule. \
                An interval of 1 produces a weekly schedule, an interval of 2 produces an \
                every-other week schedule.
        """
        self.__set_cadence(TaskTriggerTypes.TASK_TRIGGER_WEEKLY)
        self.__set_start_boundary(start_date, start_time)
        self.trigger.WeeksInterval = weeks_interval
        self.trigger.DaysOfWeek = days_of_week
        return self.taskdef

    def create_monthly_trigger(
        self,
        trigger_type: Literal["month","dow"],
        start_date: datetime.date,
        start_time: datetime.time,
        days_of_month: int,
        days_of_week: int,
        months_of_year: int,
        weeks_of_month: int
    ):
        """Starts a task based on a monthly schedule or a monthly day-of-week schedule.
        https://learn.microsoft.com/en-us/windows/win32/taskschd/monthlytrigger
        
        Parameters:
            trigger_type (`Literal['month', 'dow']`): Type of monthly trigger.
            start_date (`datetime.date`): Date when the trigger is activated.
            start_time (`datetime.time`): Time when the trigger is activated.
            days_of_month (`int`): Sets the days of the month during which the task runs.
            days_of_week (`int`): Sets the days of the week during which the task runs. 
            months_of_year (`int`): Sets the months of the year during which the task runs.
            weeks_of_month (`int`): Sets the weeks of the month during which the task runs.
        
        Examples:
            The `month` trigger type can start a task on a specific day of specific months.
            The `dow` trigger type can start a task every first Thursday of specific months.
        
        """
        self.__set_start_boundary(start_date, start_time)
        match trigger_type:
            case "month":
                self.__set_cadence(TaskTriggerTypes.TASK_TRIGGER_MONTHLY)
                self.trigger.DaysOfMonth = days_of_month
                self.trigger.MonthsOfYear = months_of_year
            case "dow":
                self.__set_cadence(TaskTriggerTypes.TASK_TRIGGER_MONTHLYDOW)
                self.trigger.DaysOfWeek = days_of_week
                self.trigger.MonthsOfYear = months_of_year
                self.trigger.WeeksOfMonth = weeks_of_month
        return self.taskdef

    def create_one_time_trigger(
        self,
        start_date: datetime.date,
        start_time: datetime.time
    ):
        """Starts a task at as specific date and time.
        https://learn.microsoft.com/en-us/windows/win32/taskschd/timetrigger

        Parameters:
            start_date (`datetime.date`): Date when the trigger is activated.
            start_time (`datetime.time`): Time when the trigger is activated.
        """
        self.__set_cadence(TaskTriggerTypes.TASK_TRIGGER_TIME)
        self.__set_start_boundary(start_date, start_time)
        return self.taskdef
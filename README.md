# 📅 pytask_scheduler
A python wrapper for the win32com task scheduler client and it's scripting objects. The motivation for building this came from my 9-5 where I use Task Scheduler for scheduling data pipelines to execute after hours. This project was primarily built for my personal and professional use but would like to share it to others who also share the same love-hate relationship with Task Scheduler.

# ❗ Getting Started

## Installation
Install this repo by entering this command in the terminal.
```console
pip install git+https://github.com/jmerluza/pytask_scheduler
```
Or this command for upgrading.
```console
pip install git+https://github.com/jmerluza/pytask_scheduler --upgrade
```

## Connect to Task Scheduler Client
You can initialize the connection to the Task Scheduler client object like so:

```python
from pytask_scheduler import TaskScheduler
ts = TaskScheduler()
```

Compared to the original win32com API.
```python
import win32com.client
client = win32com.client.gencache.EnsureDispatch("Schedule.Service")
client.Connect()
```

## Attributes
- `client` attribute returns the schedule.service com object from win32com.
- `root_folder` attribute return the root folder object.
- `folders` attribute returns the list of the subfolder names from the root folder. 
    ```python
    ts.folders
    >>> ['GoogleSystem',
        'Jalen_Tasks',
        'Microsoft']
    ```

## Methods
- `get_folder` method returns the `TaskFolder` object based on the folder name.
- `get_all_tasks` method returns the `TaskDataFrame` object containing all the tasks scheduled within task scheduler.
- `create_task` method creates and schedules a new task in task scheduler.

# 📇 Task Event Logs
A cool feature that is available in this api is to extract the task event history logs in the form of a dataframe. This feature requires **read-only access** to the Task Scheduler Event Log file. To get access to this file you can do so by following the steps below assuming you have admin permissions.

> ## 🚧 Warning
> In a professional setting, you may need to contact your IT desk to give you read access permission. For personal use, you should be able to give yourself read-only access to this file.

1. Navigate to the log folder --> `C:\Windows\System32\winevt\Logs`.
2. Locate file --> `Microsoft-Windows-TaskScheduler%4Operational.evtx`.
3. Right click on file and click `properties`.
4. Go to `security` tab.
5. Click `Edit...` to edit permissions.
6. Click `Add...`.
7. Click `Advanced...`.
8. Click `Find Now`.
9. Select your user account and click `OK`.
10. Check off `Read` only.
11. Once read access has been granted, you can test this by executing the `get_task_scheduler_history` function. 

# pytask_scheduler
A python wrapper for the win32com task scheduler client and it's scripting objects. This was built for personal use and my professional use at my 9-5, plus I thought this would be a fun side project to do. Let's get started!

# Installation
Install this repo by entering this command in the terminal.
```console
pip install git+https://github.com/jmerluza/pytask_scheduler
```

# Getting Started
You can instantiate the Task Scheduler client object like so:

```python
from pytask_scheduler import TaskScheduler
ts = TaskScheduler()
```

## Attributes

|Attribute|Description|
|---|---|
|`client`|The schedule.service com object from win32com.|
|`root_folder`|Root folder object.|
|`folders`|List of the subfolder names from the root folder.|

The below is an example of using the folders `attribute`.
```python
ts.folders
>>> ['Agent Activation Runtime',
    'GoogleSystem',
    'Jalen_Tasks',
    'Microsoft',
    'Norton 360',
    'Norton Security',
    'Norton Security with Backup',
    'Oem',
    'Remediation']
```

## Methods
|Method|Description|
|---|---|
|`get_folder`|Gets and returns the task folder based on folder name.|
|`get_all_tasks`|Gets and returns the list of all tasks.|
|`create_task`|Creates a new task.|

The below is an example of using the `get_all_tasks` method.
```python
tasks_data = ts.get_all_tasks()
print(tasks_data.head())
>>> shape: (5, 12)
    ┌────────────┬─────────┬───────────┬───────────┬───┬───────────┬───────────┬───────────┬───────────┐
    │ name       ┆ enabled ┆ task_stat ┆ next_run_ ┆ … ┆ author    ┆ registrat ┆ task_desc ┆ task_sour │
    │ ---        ┆ ---     ┆ e         ┆ time      ┆   ┆ ---       ┆ ion_date  ┆ ription   ┆ ce        │
    │ str        ┆ bool    ┆ ---       ┆ ---       ┆   ┆ str       ┆ ---       ┆ ---       ┆ ---       │
    │            ┆         ┆ i64       ┆ datetime[ ┆   ┆           ┆ str       ┆ str       ┆ str       │
    │            ┆         ┆           ┆ μs, UTC]  ┆   ┆           ┆           ┆           ┆           │
    ╞════════════╪═════════╪═══════════╪═══════════╪═══╪═══════════╪═══════════╪═══════════╪═══════════╡
    │ ACCBackgro ┆ true    ┆ 4         ┆ 1899-12-3 ┆ … ┆           ┆           ┆ Acer Care ┆           │
    │ undApplica ┆         ┆           ┆ 0         ┆   ┆           ┆           ┆ Center    ┆           │
    │ tion       ┆         ┆           ┆ 00:00:00  ┆   ┆           ┆           ┆ backgroun ┆           │
    │            ┆         ┆           ┆ UTC       ┆   ┆           ┆           ┆ d ap…     ┆           │
    │ Acer       ┆ true    ┆ 3         ┆ 1899-12-3 ┆ … ┆           ┆           ┆ Acer Coll ┆           │
    │ Collection ┆         ┆           ┆ 0         ┆   ┆           ┆           ┆ ection    ┆           │
    │ Applicatio ┆         ┆           ┆ 00:00:00  ┆   ┆           ┆           ┆ applicati ┆           │
    │ n          ┆         ┆           ┆ UTC       ┆   ┆           ┆           ┆ on        ┆           │
    │ Acer       ┆ true    ┆ 4         ┆ 1899-12-3 ┆ … ┆           ┆           ┆ Acer Coll ┆           │
    │ Collection ┆         ┆           ┆ 0         ┆   ┆           ┆           ┆ ection    ┆           │
    │ Monitor    ┆         ┆           ┆ 00:00:00  ┆   ┆           ┆           ┆ Monitor   ┆           │
    │ Applic…    ┆         ┆           ┆ UTC       ┆   ┆           ┆           ┆ applic…   ┆           │
    │ AcerCloud  ┆ true    ┆ 3         ┆ 1899-12-3 ┆ … ┆           ┆           ┆ Global    ┆           │
    │            ┆         ┆           ┆ 0         ┆   ┆           ┆           ┆ registrat ┆           │
    │            ┆         ┆           ┆ 00:00:00  ┆   ┆           ┆           ┆ ion       ┆           │
    │            ┆         ┆           ┆ UTC       ┆   ┆           ┆           ┆           ┆           │
    │ Adobe-Genu ┆ true    ┆ 3         ┆ 2024-08-3 ┆ … ┆ Adobe     ┆           ┆           ┆           │
    │ ine-Softwa ┆         ┆           ┆ 1         ┆   ┆ Systems   ┆           ┆           ┆           │
    │ re-Integri ┆         ┆           ┆ 21:17:00  ┆   ┆ Inc.      ┆           ┆           ┆           │
    │ …          ┆         ┆           ┆ UTC       ┆   ┆           ┆           ┆           ┆           │
    └────────────┴─────────┴───────────┴───────────┴───┴───────────┴───────────┴───────────┴───────────┘
```


## Getting a task history
The task history feature requires read-only access to the Task Scheduler Event Log file. To get read-only access you can do so by following these steps:
1. Navigate to the log folder --> `C:\Windows\System32\winevt\Logs`.
2. Locate file --> `Microsoft-Windows-TaskScheduler%4Operational.evtx`.
3. Right click on file and click `properties`.
4. Go to `security` tab.
5. Click `Edit...` to edit permissions.

> 🚧 Warning
>
> In a professional setting, you may need to contact your IT desk to give you read access permission. For personal use, you should be able to give yourself read-only access to this file.

6. Click `Add...`.
7. Click `Advanced...`.
8. Click `Find Now`.
9. Select your user account and click `OK`.
10. Check off `Read` only.
11. Once read access has been granted, you can test this by executing the `get_task_scheduler_history` function. 

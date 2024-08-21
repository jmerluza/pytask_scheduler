"""This module covers topics from the TaskSettings object.
https://learn.microsoft.com/en-us/windows/win32/taskschd/tasksettings
"""

class TaskSettings:
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
        restart_interval: bool,
        restart_count: bool,
        execution_time_limit: bool,
        multiple_instances: bool
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

            restart_interval (`bool`):
                Gets or sets a value that specifies how long the task scheduler will \
                attempt to restart the task.

            restart_count (`bool`): 
                Gets or sets the number of times that the task scheduler \
                will attempt to restart the task.

            execution_time_limit (`bool`): 
                Gets or sets the amount of time allowed to complete the task.

            multiple_instances (`bool`): 
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
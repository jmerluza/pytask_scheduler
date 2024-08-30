"""This module is for the TasksFrame object."""
import polars as pl
from pytask_scheduler.constants import TaskValueDefinitions

class TaskFrame(pl.DataFrame):
    def __init__(self, data: pl.DataFrame):
        super().__init__(data)
        self.df = data

    def stats(self) -> pl.DataFrame:
        """Get statistics on all the tasks."""
        stats_schema = {
            "task_total":self.total_number_of_tasks(),
            "missed_runs_total":self.total_number_of_missed_runs(),
            "unknown_state_total":self.total_number_of_tasks_by_state(0),
            "disabled_state_total":self.total_number_of_tasks_by_state(1),
            "queued_state_total":self.total_number_of_tasks_by_state(2),
            "ready_state_total":self.total_number_of_tasks_by_state(3),
            "running_state_total":self.total_number_of_tasks_by_state(4)
        }

        return pl.DataFrame(stats_schema)

    def total_number_of_tasks(self):
        """Counts the total number of tasks."""
        return self.df.shape[0]

    def total_number_of_missed_runs(self):
        """Counts the total number of missed runs."""
        return self.df["number_of_missed_runs"].sum()

    def total_number_of_tasks_by_state(self, state: int):
        """Counts the total number of tasks by state."""
        return self.df.filter(pl.col("task_state")==state).shape[0]
    

"""This module is for the TasksFrame object."""

import polars as pl

class TaskFrame(pl.DataFrame):
    def __init__(self, data: pl.DataFrame):
        super().__init__(data)
        self.df = data

    def stats(self):
        """Get statistics on all the tasks."""
        task_total = self.df.shape[0]
        missed_runs_total = self.df.shape[0]

    def total_number_of_tasks(self):
        """Counts the total number of tasks."""
        return self.df.shape[0]

    def total_number_of_missed_runs(self):
        """Counts the total number of missed runs."""
        return self.df["missed_runs"].sum()

    def total_number_of_tasks_by_state(self, state: str):
        """Counts the total number of tasks by state."""
        return self.df.filter(pl.col("state")==state).shape[0]
    
    def filter_author_and_task_name(self, author: str, folder_name: str|None=None):
        """Filters the task frame by author and task name."""
        if folder_name:
            df = self.df.filter(
                (pl.col("author").str.contains(author)) &
                (pl.col("folder_name")==folder_name)
            )
        else:
            df = self.df
        return TaskFrame(df)

import polars as pl
import xml.etree.ElementTree as ET
from Evtx.Evtx import Evtx
from pytask_scheduler import EventIDs, EventLogType

def get_task_scheduler_history() -> pl.DataFrame:
    """Get the task scheduler event histories."""
    evt_fpath = r"C:\Windows\System32\winevt\Logs\Microsoft-Windows-TaskScheduler%4Operational.evtx"
    event_data = []
    with Evtx(evt_fpath) as t:
        for event_record in [r.xml() for r in list(t.records())]:
            root = ET.fromstring(event_record)

            # extracts the event data from the xml string.
            event_data.append(
                {
                    "event_created_time":root[0][7].attrib.get("SystemTime"),
                    "event_level":root[0][3].text,
                    "event_id":root[0][1].text,
                    "task_name":root[1][0].text
                }
            )

    df = pl.DataFrame(event_data)

    df = df.with_columns(
        pl.col("event_id").replace(EventIDs.DESCRIPTIONS).alias("event_id_description"),
        pl.col("event_level").replace(EventLogType.DESCRIPTIONS).alias("event_log_description")
    )

    return df

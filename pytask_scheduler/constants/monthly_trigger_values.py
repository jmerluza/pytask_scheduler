"""https://learn.microsoft.com/en-us/windows/win32/taskschd/monthlytrigger-daysofmonth"""
from dataclasses import dataclass

@dataclass
class MonthlyTriggerValues:
    DAYS_OF_MONTH = {
        1:1,
        2:2,
        3:4,
        4:8,
        5:16,
        6:32,
        7:64,
        8:128,
        9:256,
        10:512,
        11:1024,
        12:2048,
        13:4096,
        14:8192,
        15:16384,
        16:32768,
        17:65536,
        18:131072,
        19:262144,
        20:524288,
        21:1048576,
        22:2097152,
        23:4194304,
        24:8388608,
        25:16777216,
        26:33554432,
        27:67108864,
        28:134217728,
        29:268435456,
        30:536870912,
        31:1073741824,
        "Last":2147483648
    }

    MONTHS_OF_YEAR = {
        "January":1,
        "February":2,
        "March":4,
        "April":8,
        "May":16,
        "June":32,
        "July":64,
        "August":128,
        "September":256,
        "October":512,
        "November":1024,
        "December":2048
    }

    DAYS_OF_WEEK = {
        "Sunday":1,
        "Monday":2,
        "Tuesday":4,
        "Wednesday":8,
        "Thursday":16,
        "Friday":32,
        "Saturday":64
    }

    WEEKS_OF_MONTH = {
        "First week of the month":1,
        "Second week of the month":2,
        "Third week of the month":4,
        "Fourth week of the month":8
    }
from datetime import date
from enum import Enum
from typing import Optional
from pydantic import BaseModel


class GroupingEnum(str, Enum):
    weekly = 'weekly'
    bi_weekly = 'bi-weekly'
    monthly = 'monthly'


class TimelineTypeEnum(str, Enum):
    cumulative = 'cumulative'
    usual = 'usual'


class TimelineRequest(BaseModel):
    startDate: date
    endDate: date
    grouping: Optional[GroupingEnum]
    timelineType: Optional[TimelineTypeEnum]
    asin: Optional[int] = None
    brand: Optional[str] = None
    source: Optional[str] = None
    stars: Optional[int] = None


def validate_timeline_request(request) -> TimelineRequest:
    return TimelineRequest(
        startDate=request.args.get('startDate'),
        endDate=request.args.get('endDate'),
        grouping=request.args.get('Grouping'),
        timelineType=request.args.get('Type'),
        asin=request.args.get('asin'),
        brand=request.args.get('brand'),
        source=request.args.get('source'),
        stars=request.args.get('stars'),
    )

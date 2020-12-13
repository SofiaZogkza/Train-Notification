from __future__ import annotations
from dataclasses import dataclass, asdict, field
from typing import Dict, Any, List, AnyStr, Optional

@dataclass
class JourneyResponse:
    earlierRef: str
    laterRef: str
    journeys: List[Journey]
    realtimeDataFrom: int

    def __post_init__(self):
        # Instead of dictionaries , transform a dictionary to List of (leg)objects.
        temp_list = []
        for item in self.journeys:
            journey = item
            if isinstance(item, dict):  # If item is type of dictionary, convert to leg object.
                journey = Journey(**item)
            temp_list.append(journey)
        self.journeys = temp_list

@dataclass
class Journey:
    type: str
    legs: List[Leg]
    refreshToken: str
    cycle: Dict[AnyStr, Any]
    remarks: Any = None

    def __post_init__(self):
        # Instead of dictionaries , transform a dictionary to List of (leg)objects.
        temp_list = []
        for item in self.legs:
            leg = item
            if isinstance(item, dict):  # If item is type of dictionary, convert to leg object.
                leg = Leg(**item)
            temp_list.append(leg)
        self.legs = temp_list


@dataclass
class Leg:
    origin: Dict[Any, Any]
    destination: Destination  # dictionary {}
    departure: str
    plannedDeparture: str
    departureDelay: str
    arrival: str
    plannedArrival: str
    arrivalDelay: int
    reachable: Optional[bool] = None
    tripId: Optional[str] = None
    line: Optional[Dict[Any, Any]] = None
    direction: Optional[str] = None
    arrivalPlatform: Optional[str] = None
    plannedArrivalPlatform: Optional[str] = None
    departurePlatform: Optional[str] = None
    plannedDeparturePlatform: Optional[str] = None
    cycle: Dict[Any, Any] = None
    public: Optional[bool] = None
    walking: Optional[bool] = None
    distance: Optional[int] = None
    alternatives: Any = None

    # Transform to object.
    def __post_init__(self):
        # If it is dictionary -> convert it to object.
        if isinstance(self.destination, dict):
            self.destination = Destination(**self.destination)

@dataclass
class Destination:
    type: str
    id: str
    name: str
    location: Dict[AnyStr, Any]
    products: Dict[AnyStr, Any]
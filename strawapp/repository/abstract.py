from abc import ABC, abstractmethod
from typing import List

from strawapp.entities import OpenPosition, Person, Sponsor, Talk


class AbstractPeopleRepository(ABC):

    @staticmethod
    @abstractmethod
    def get_people(filter) -> List[Person]:
        ...

    @staticmethod
    @abstractmethod
    def get_people_by_interest(interest: str) -> List[Person]:
        ...

    @staticmethod
    @abstractmethod
    def get_people_open_to_proposals() -> List[Person]:
        ...


class AbstractTalksRepository(ABC):

    @staticmethod
    @abstractmethod
    def get_talks() -> List[Talk]:
        ...

    @staticmethod
    @abstractmethod
    def get_next_talks() -> List[Talk]:
        ...

    @staticmethod
    @abstractmethod
    def get_talks_by_year(year: str) -> List[Talk]:
        ...

    @staticmethod
    @abstractmethod
    def get_talks_by_topic(topic: str) -> List[Talk]:
        ...


class AbstractRepository(AbstractPeopleRepository, AbstractTalksRepository, ABC):

    @staticmethod
    @abstractmethod
    def get_sponsors() -> List[Sponsor]:
        ...

    @staticmethod
    @abstractmethod
    def get_open_opportunities() -> List[OpenPosition]:
        ...


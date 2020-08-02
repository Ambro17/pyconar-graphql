from dataclasses import dataclass
import dataclasses
from typing import List, Optional
from enum import Enum
import strawberry
from strawberry.field import field


Link = str


@strawberry.interface
class Person:
    name: str
    email: str
    interests: List[str]
    open_to_job_offers: bool

    def interested_in(self, topic):
        interests = [i.lower() for i in self.interests] or []
        return topic.lower() in interests


@strawberry.type
class Speaker(Person):
    job: str 
    # company: str
    # talk: 'Talk'


@strawberry.type
class Visitor(Person):
    resume_link: str = ''
    # github_profile


Attendee = strawberry.union("Attendee", (Speaker, Visitor))


@strawberry.enum
class Topic(Enum):
    PYTHON = 'Python'
    REST = 'Rest'
    DIVERSITY = 'Diversity'


@strawberry.enum
class NerdearlaEdition(Enum):
    _2017 = '2017'
    _2018 = '2018'
    _2019 = '2019'


@strawberry.type
class Talk:
    name: str
    topic: Topic
    description: str
    year: int
    speaker: Person


@strawberry.type
class OpenPosition:
    title: str
    url: Link
    company: str


@strawberry.type
class Company:
    name: str
    description: str
    website: Link
    open_positions: List[OpenPosition]
    technologies: List[str]


@strawberry.enum
class SponsorType(Enum):
    EXABYTE = 'EXABYTE'
    PETABYTE = 'PETABYTE'
    TERABYTE = 'TERABYTE'


@strawberry.type
class Sponsor:
    company: Company
    category: SponsorType

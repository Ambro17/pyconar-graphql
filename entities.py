from typing import List
from enum import Enum
import strawberry


Link = str


@strawberry.interface
class Person:
    name: str
    surname: str
    email: str


class Speaker(Person):
    job: str 
    company: str
    talk: 'Talk'


class Attendee(Person):
    interests: str
    looking_for_job: bool
    resume_link: str


@strawberry.enum
class Topic(Enum):
    PYTHON = 'Python'
    DIVERSITY = 'Diversity'


@strawberry.enum
class NerdearlaEdition(Enum):
    _2017 = '2017'
    _2018 = '2018'
    _2019 = '2019'


@strawberry.type
class Talk:
    name: str
    description: str
    speaker: Person
    topic: Topic
    tags: List[str]
    youtube_link: Link


@strawberry.type
class OpenPosition:
    title: str
    url: Link


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

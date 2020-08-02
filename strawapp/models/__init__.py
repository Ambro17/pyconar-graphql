from typing import List
from enum import Enum


class Person:
    name: str
    email: str
    interests: List[str]
    open_to_job_offers: bool

    def interested_in(self, topic):
        interests = [i.lower() for i in self.interests] or []
        return topic.lower() in interests


class Speaker(Person):
    job: str 
    # company: str
    # talk: 'Talk'


class Visitor(Person):
    resume_link: str = ''
    # github_profile



class Topic(Enum):
    PYTHON = 'Python'
    REST = 'Rest'
    DIVERSITY = 'Diversity'


class Edition(Enum):
    _2017 = '2017'
    _2018 = '2018'
    _2019 = '2019'
    _2020 = '2020'


class Talk:
    name: str
    topic: Topic
    description: str
    year: Edition
    speaker: Person


class OpenPosition:
    title: str
    url: str
    company: str


class Company:
    name: str
    description: str
    website: str
    open_positions: List[OpenPosition]
    technologies: List[str]


class SponsorType(Enum):
    EXABYTE = 'EXABYTE'
    PETABYTE = 'PETABYTE'
    TERABYTE = 'TERABYTE'


class Sponsor:
    company: Company
    category: SponsorType

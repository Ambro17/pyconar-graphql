from typing import List, Optional
from enum import Enum
import strawberry


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
    talk: Optional['Talk'] = None


@strawberry.type
class Visitor(Person):
    resume_link: str = ''
    github_profile: str = ''


@strawberry.enum
class Topic(Enum):
    PYTHON = 'Python'
    REST = 'Rest'
    DIVERSITY = 'Diversity'


@strawberry.type
class Talk:
    name: str
    topic: Topic
    description: str
    year: str
    speaker: Speaker


@strawberry.type
class OpenPosition:
    title: str
    url: Link
    company: 'Company'


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

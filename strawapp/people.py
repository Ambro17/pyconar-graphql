import strawberry
from .entities import Person, Speaker, Visitor
from typing import List


SPEAKERS = [
    Speaker(
        name='Carla',
        email='carla@mail.com',
        job='Evil Inc',
        interests=['Python'],
        open_to_job_offers=False,
    ),
    Speaker(
        name='Lucia',
        email='lu@mail.com',
        job='Some Inc.',
        interests=['Python', 'Ruby'],
        open_to_job_offers=False,
    ),
]


VISITORS = [
    Visitor(
        name='Juan',
        email='me@mail.com',
        interests=['Python', 'GraphQL', 'API Design'],
        open_to_job_offers=True,
    ),
    Visitor(
        name='Sofía',
        email='sofi@mail.com',
        interests=['Java'],
        open_to_job_offers=True,
    ),
]

ATTENDEES = SPEAKERS + VISITORS


@strawberry.input
class PeopleFilter:
    seniority: str
    language: str
    salary_range: str


def get_people(filter: PeopleFilter = None) -> List[Person]:
    return ATTENDEES


def get_people_by_interest(interest: str) -> List[Person]:
    return [
        person for person in ATTENDEES
        if person.interested_in(interest)
    ]


def get_people_open_to_proposals() -> List[Person]:
    return [
        person for person in ATTENDEES
        if person.open_to_job_offers
    ]

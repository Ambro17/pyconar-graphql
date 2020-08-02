import strawberry
from entities import Attendee, Person, Speaker, Visitor
from typing import KeysView, Union, List


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


def get_people(filter: PeopleFilter = None) -> List[Attendee]:
    return ATTENDEES


def get_people_by_interest(keyword: str) -> List[Person]:
    return [
        person for person in ATTENDEES
        if person.interested_in(keyword)
    ]


def get_people_open_to_proposals() -> List[Person]:
    return [
        person for person in ATTENDEES
        if person.looking_for_a_job
    ]
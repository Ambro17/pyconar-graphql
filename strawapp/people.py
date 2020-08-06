import random
import requests
import strawberry
from typing import List
from enum import Enum

from .entities import Person, Speaker, Visitor


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
        open_to_job_offers=True,
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


@strawberry.enum
class Seniority(Enum):
    SENIOR = 'Sr'
    SEMI_SENIOR = 'Ssr'
    JUNIOR = 'Jr'


@strawberry.input
class PeopleFilter:
    interested_in: List[str]
    open_to_job_offers: bool
    seniority: Seniority


def get_people(filter: PeopleFilter = None) -> List[Person]:
    try:
        resp = requests.get('https://jsonplaceholder.typicode.com/users', timeout=2)
    except requests.Timeout:
        return []

    if resp.status_code != 200 or not resp.json():
        return []

    return [
        Visitor(
            name=p['name'],
            email=p['email'],
            interests=p['company']['bs'].split(),
            open_to_job_offers=random.choice([True, False])           
        )
        for p in resp.json()
    ]


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

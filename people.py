from entities import Attendee, Person, Speaker, Visitor
from typing import KeysView, Union, List


SPEAKERS = [
    Speaker(
        name='Carla',
        email='carla@mail.com',
        job='Evil Inc',
        interests=['Python'],
    ),
    Speaker(
        name='Lucia',
        email='lu@mail.com',
        job='Some Inc.',
        interests=['Python', 'Ruby'],
    ),
]


VISITORS = [
    Visitor(
        name='Juan',
        email='me@mail.com',
        interests=['Python', 'GraphQL', 'API Design'],
        looking_for_a_job=True,
    ),
    Visitor(
        name='Sofía',
        email='sofi@mail.com',
        interests=['Java'],
        looking_for_a_job=False,
    ),
]

ATTENDEES = SPEAKERS + VISITORS


def get_people(name: str) -> List[Attendee]:
    return ATTENDEES


def get_people_by_interest(keyword: str) -> List[Person]:
    return [
        person for person in ATTENDEES
        if person.interested_in(keyword)
    ]
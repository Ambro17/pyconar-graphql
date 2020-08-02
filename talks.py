import itertools
from typing import List
from entities import Talk, Speaker, Topic


TALKS = {
    '2019': [
        Talk(
            name='How to GraphQL',
            topic=Topic.PYTHON,
            description='We will learn how to graphql',
            year=2019,
            speaker=Speaker(
                name='Nahuel',
                email='me@mail.com',
                job='Sinapsis',
                interests=[],
                open_to_job_offers=True,
            ),
        )
    ],
    '2020': [
        Talk(
            name='How to REST',
            topic=Topic.REST,
            description='We will learn how to REST',
            year=2020,
            speaker=Speaker(
                name='Juan',
                email='jp@mail.com',
                job='Self Employed',
                interests=[],
                open_to_job_offers=True,
            ),
        )
    ]
}


def _unwrap_list(list_of_iterables) -> List:
    return list(itertools.chain.from_iterable(list_of_iterables))


def get_talks() -> List[Talk]:
    return _unwrap_list(TALKS.values())


def get_talks_by_year(year: str) -> List[Talk]:
    return TALKS.get(year, [])


def get_talks_by_topic(topic: str) -> List[Talk]:
    return [
        talk
        for talk in _unwrap_list(TALKS.values())
        if topic.lower() in talk.topic.value.lower()
    ]

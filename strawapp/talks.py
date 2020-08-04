import datetime
import itertools
from typing import List
from .entities import Edition, Talk, Speaker, Topic


a_speaker = Speaker(
    name='Nahuel',
    email='me@mail.com',
    job='Sinapsis',
    interests=[],
    open_to_job_offers=True,
    talk=None
)
a_talk = Talk(
    name='How to GraphQL',
    topic=Topic.PYTHON,
    description='We will learn how to graphql',
    year=Edition._2019.value,
    speaker=a_speaker
)
a_speaker.talk = a_talk


TALKS = {
    '2019': [a_talk],
    '2020': [
        Talk(
            name='How to REST',
            topic=Topic.REST,
            description='We will learn how to REST',
            year=Edition._2020.value,
            speaker=Speaker(
                name='Juan',
                email='jp@mail.com',
                job='Self Employed',
                interests=[],
                open_to_job_offers=True,
            ),
        ),
        Talk(
            name='How to Postgres',
            topic=Topic.DIVERSITY,
            description='We will learn how to Postgres',
            year=Edition._2020.value,
            speaker=Speaker(
                name='John',
                email='john@mail.com',
                job='Avianca',
                interests=[],
                open_to_job_offers=True,
            ),
        ),
    ]
}


def _unwrap_list(list_of_iterables) -> List:
    return list(itertools.chain.from_iterable(list_of_iterables))


def get_talks() -> List[Talk]:
    return _unwrap_list(TALKS.values())


def get_next_talks() -> List[Talk]:
    year = str(datetime.datetime.utcnow().year)
    next_talks = TALKS.get(year, [])
    return next_talks


def get_talks_by_year(year: str) -> List[Talk]:
    return TALKS.get(year, [])


def get_talks_by_topic(topic: str) -> List[Talk]:
    return [
        talk
        for talk in _unwrap_list(TALKS.values())
        if topic.lower() in talk.topic.value.lower()
    ]

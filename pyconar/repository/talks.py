import itertools
import json
import random
import string
from datetime import datetime
from typing import List

from pyconar.domain import Speaker, Talk, Topic
from pyconar.repository.abstract import AbstractTalksRepository


def random_name():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(5))


def random_interest():
    return random.choice(['Python', 'Programming', 'API', 'GraphQL'])


class TalksRepository(AbstractTalksRepository):
    def __init__(self, file) -> None:
        self.talks = self._load_talks_from_file(file)

    def _load_talks_from_file(self, file):
        with open(file, 'r') as f:
            talks_by_year = json.load(f)

        talks = {
            year: [
                Talk(
                    name=talk['title'],
                    description=talk['desc'],
                    topic=Topic.PYTHON,
                    year=year,
                    speaker=Speaker(
                        name=talk['speaker'],
                        email=f'{random_name()}@mail.com',
                        job='PyconAr',
                        interests=[random_interest()],
                        open_to_job_offers=random.choice([True, False]),
                        talk=None
                    ),
                )
                for talk in talks
            ]
            for year, talks in talks_by_year.items()
        }

        for talk in self._unwrap_list(talks.values()):
            # Backreference talk from each speaker
            talk.speaker.talk = talk

        return talks

    @staticmethod
    def _unwrap_list(list_of_iterables) -> List:
        return list(itertools.chain.from_iterable(list_of_iterables))


    def get_talks(self) -> List[Talk]:
        return self._unwrap_list(self.talks.values())


    def get_next_talks(self) -> List[Talk]:
        year = str(datetime.utcnow().year)
        next_talks = self.talks.get(year, [])
        return next_talks


    def get_talks_by_year(self, year: str) -> List[Talk]:
        return self.talks.get(year, [])


    def get_talks_by_topic(self, topic: str) -> List[Talk]:
        return [
            talk
            for talk in self._unwrap_list(self.talks.values())
            if topic.lower() in talk.topic.value.lower()
        ]

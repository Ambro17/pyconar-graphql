import itertools
import json
import random
import string
from datetime import datetime, timedelta
from typing import List

from dateutil.parser import parse
import humanize

from pyconar.domain import ScheduleInfo, Speaker, Talk, Topic, UpcomingTalk
from pyconar.repository.abstract import AbstractTalksRepository


def random_name():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(5))


def random_interest():
    return random.choice(['Python', 'Programming', 'API', 'GraphQL'])


class TalksRepository(AbstractTalksRepository):
    def __init__(self, file, schedule) -> None:
        self.talks: List[Talk] = self._load_talks_from_file(file)
        self.schedule: List[UpcomingTalk] = self._load_schedule_from_file(schedule)

    def _load_schedule_from_file(self, schedule) -> List[UpcomingTalk]:
        with open(schedule, 'r') as f:
            schedule_2020 = json.load(f)
        # [u'bio', u'title', u'speaker', u'schedule', u'desc']
        """
        class UpcomingTalk:
            name: str
            description: str
            schedule: ScheduleInfo
            speaker: Speaker
        """
        up_talks = [
            UpcomingTalk(
                name=talk['title'],
                description=talk['desc'],
                topic=Topic.PYTHON,
                year=str(datetime.now().year),
                schedule=ScheduleInfo(
                    when=talk['schedule']['time'],
                    start=talk['schedule']['start'],
                    end=talk['schedule']['end'],
                    starting_in=(
                        humanize.precisedelta(
                            datetime.now() - parse(talk['schedule']['time']),
                            format='%0.f')
                    ),
                ),
                speaker=Speaker(
                    name=talk['speaker'],
                    email=f'{random_name()}@mail.com',
                    bio=talk.get('bio',''),
                    job='PyconAr Inc.',
                    interests=[random_interest()],
                    open_to_job_offers=random.choice([True, False]),
                    talk=None
                ),
            ) 
            for talk in schedule_2020
        ]

        for talk in up_talks:
            # Backreference talk from each speaker
            talk.speaker.talk = talk


        return up_talks

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
                        bio=talk.get('bio',''),
                        job='PyconAr Inc.',
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


    def get_next_talks(self) -> List[UpcomingTalk]:
        # Get now
        # Filter those that already happend
        # Return those in the future
        now = datetime.now()

        next_talks = []
        for talk in self.schedule:
            talk_date = parse(talk.schedule.start)
            if talk_date < now:
                continue

            talk.schedule.starting_in = humanize.precisedelta(
                now - talk_date,
                format='%0.f'
            )
            next_talks.append(talk)

        return next_talks


    def get_talks_by_year(self, year: str) -> List[Talk]:
        return self.talks.get(year, [])


    def get_talks_by_topic(self, topic: str) -> List[Talk]:
        return [
            talk
            for talk in self._unwrap_list(self.talks.values())
            if topic.lower() in talk.topic.value.lower()
        ]

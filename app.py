from typing import List, Optional, Union
import strawberry
from strawberry import field

from sponsors import Sponsor, get_sponsors
from talks import Talk, get_talks, get_talks_by_topic, get_talks_by_year
from people import get_people, get_people_by_interest
from entities import OpenPosition, Person, Speaker, Visitor


@strawberry.type
class Query:
    sponsors: List[Sponsor] = field(resolver=get_sponsors)

    searchPeople: List[Person] = field(resolver=get_people)
    searchPeopleByInterest: List[Person] = field(resolver=get_people_by_interest)
    searchPeopleLookingForAJob: List[Person] = field(resolver=get_people_by_interest)


    searchJobOportunities: List[OpenPosition] = field(resolver=get_sponsors)


    talks: List[Talk] = field(resolver=get_talks)
    talksByYear: List[Talk] = field(resolver=get_talks_by_year)
    talksByTopic: List[Talk] = field(resolver=get_talks_by_topic)


schema = strawberry.Schema(query=Query, types=[Speaker, Visitor])

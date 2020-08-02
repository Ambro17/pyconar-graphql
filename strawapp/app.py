from typing import List
import strawberry
from strawberry import field

from .sponsors import Sponsor, get_open_opportunities, get_sponsors
from .talks import Talk, get_next_talks, get_talks, get_talks_by_topic, get_talks_by_year
from .people import get_people, get_people_by_interest, get_people_open_to_proposals

from .models.strawberry import OpenPosition, Person, Speaker, Visitor # Works now, is it worth it tho?
# from .entities import OpenPosition, Person, Speaker, Visitor  # WORKS


@strawberry.type
class Query:
    sponsors: List[Sponsor] = field(resolver=get_sponsors)

    searchPeople: List[Person] = field(resolver=get_people)
    searchPeopleByInterest: List[Person] = field(resolver=get_people_by_interest)
    searchPeopleOpenToHiring: List[Person] = field(resolver=get_people_open_to_proposals)

    searchJobOportunities: List[OpenPosition] = field(resolver=get_open_opportunities)

    talks: List[Talk] = field(resolver=get_talks)
    nextTalks: List[Talk] = field(resolver=get_next_talks, description="Talks which are about to start")
    talksByYear: List[Talk] = field(resolver=get_talks_by_year)
    talksByTopic: List[Talk] = field(resolver=get_talks_by_topic)


schema = strawberry.Schema(query=Query, types=[Speaker, Visitor])

with open('strawapp/dump.gql', 'w+') as f: 
    f.write(schema.as_str())

from typing import List
import strawberry
from strawberry import field

from strawapp.sponsors import Sponsor, get_open_opportunities, get_sponsors
from strawapp.talks import talks_repo
from strawapp.people import people_repo
from strawapp.domain import OpenPosition, Person, Speaker, Visitor, Talk


@strawberry.type
class Query:
    sponsors: List[Sponsor] = field(resolver=get_sponsors)

    findPeople: List[Person] = field(resolver=people_repo.get_people)
    findPeopleByInterest: List[Person] = field(resolver=people_repo.get_people_by_interest)
    findPeopleOpenToHiring: List[Person] = field(resolver=people_repo.get_people_open_to_proposals)

    findJobOportunities: List[OpenPosition] = field(resolver=get_open_opportunities)

    talks: List[Talk] = field(resolver=talks_repo.get_talks)
    nextTalks: List[Talk] = field(resolver=talks_repo.get_next_talks,
                                  description="Talks which are about to start")
    talksByYear: List[Talk] = field(resolver=talks_repo.get_talks_by_year)
    talksByTopic: List[Talk] = field(resolver=talks_repo.get_talks_by_topic)


schema = strawberry.Schema(query=Query, types=[Speaker, Visitor])

with open('strawapp/schema.gql', 'w+') as f:
    f.write(schema.as_str())

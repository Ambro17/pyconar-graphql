from typing import List

import strawberry
from strawberry import field

from pyconar.sponsors import Sponsor, get_open_opportunities, get_sponsors
from pyconar.talks import talks_repo
from pyconar.people import people_repo
from pyconar.domain import OpenPosition, Person, Speaker, Topic, Visitor, Talk
from pyconar.mutations import Mutation

@strawberry.type
class Query:
    sponsors: List[Sponsor] = field(resolver=get_sponsors)

    findPeople: List[Person] = field(resolver=people_repo.get_people)
    findPeopleOpenToHiring: List[Person] = field(resolver=people_repo.get_people_open_to_proposals)

    findOpenPositions: List[OpenPosition] = field(resolver=get_open_opportunities)

    allTalks: List[Talk] = field(resolver=talks_repo.get_talks)
    nextTalks: List[Talk] = field(resolver=talks_repo.get_next_talks,
                                  description="Talks which are about to start")
    talksByYear: List[Talk] = field(resolver=talks_repo.get_talks_by_year)


schema = strawberry.Schema(query=Query, mutation=Mutation, types=[Speaker, Visitor])


with open('pyconar/schema.gql', 'w+') as f:
    f.write(schema.as_str())

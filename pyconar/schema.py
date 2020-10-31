from typing import List
from datetime import datetime

import strawberry
from strawberry import field

from pyconar.resolvers.sponsors import Sponsor, get_open_opportunities, get_sponsors
from pyconar.resolvers.talks import talks_repo
from pyconar.resolvers.people import people_repo
from pyconar.domain import OpenPosition, Person, Speaker, UpcomingTalk, Visitor, Talk
from pyconar.mutations import Mutation


@strawberry.type
class Query:
    sponsors: List[Sponsor] = field(resolver=get_sponsors, description="Get info about current pyconar sponsors")

    findPeople: List[Person] = field(resolver=people_repo.get_people, 
                                     description="Find people that match the given filters")
    findPeopleInterestedIn: List[Person] = field(resolver=people_repo.get_people_by_interest,
                                                 description="Find people interested in the given technology")
    findPeopleOpenToHiring: List[Person] = field(resolver=people_repo.get_people_open_to_proposals,
                                                 description="Find who is open to receive job offers")

    findOpenPositions: List[OpenPosition] = field(resolver=get_open_opportunities,
                                                  description="Find who is hiring and for what jobs")

    nextTalks: List[UpcomingTalk] = field(resolver=talks_repo.get_next_talks,
                                          description=f"Talks ocurring on PyconAr `{datetime.utcnow().year}`")
    allTalks: List[Talk] = field(resolver=talks_repo.get_talks, description="All talks from `2018`, `2019` and `2020`")
    talksByYear: List[Talk] = field(resolver=talks_repo.get_talks_by_year,
                                    description="Talks given on specified `year`. One of `[2018, 2019, 2020]`")


schema = strawberry.Schema(query=Query, mutation=Mutation, types=[Speaker, Visitor])


with open('pyconar/schema.gql', 'w+') as f:
    f.write(schema.as_str())

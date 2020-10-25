from typing import List
from datetime import datetime

import strawberry
from strawberry import field

from pyconar.sponsors import Sponsor, get_open_opportunities, get_sponsors
from pyconar.talks import talks_repo
from pyconar.people import people_repo
from pyconar.domain import OpenPosition, Person, Speaker, Topic, Visitor, Talk
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

    talks: List[Talk] = field(resolver=talks_repo.get_next_talks,
                              description=f"Talks ocurring on PyconAr `{datetime.utcnow().year}`")
    talksByYear: List[Talk] = field(resolver=talks_repo.get_talks_by_year,
                                    description="Talks given on specified `year`. One of `[2018, 2019, 2020]`")


schema = strawberry.Schema(query=Query, mutation=Mutation, types=[Speaker, Visitor])


with open('pyconar/schema.gql', 'w+') as f:
    f.write(schema.as_str())

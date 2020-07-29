from typing import List, Optional
import strawberry
from strawberry import field
from entities import ( 
    Sponsor,
    SponsorType,
    Company,
    OpenPosition,
)


def get_sponsors() -> List[Sponsor]:
    evil_corp = Company(
        name='Evil Inc.',
        description='Lorem',
        website='www.evil.inc',
        open_positions=[
            OpenPosition(
                title='Python Dev',
                link='www.carrers.com',
            )
        ],
        technologies=['Python', 'React', 'GraphQL'],
    )
    return [
        Sponsor(
           company=evil_corp,
           category=SponsorType.EXABYTE,
        )
    ]


@strawberry.type
class Query:
    sponsors: List[Sponsor] = field(resolver=get_sponsors)


schema = strawberry.Schema(query=Query)
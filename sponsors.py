from entities import ( 
    Sponsor,
    SponsorType,
    Company,
    OpenPosition,
)
from typing import List


def get_sponsors() -> List[Sponsor]:
    evil_corp = Company(
        name='Evil Inc.',
        description='Lorem',
        website='www.evil.inc',
        open_positions=[
            OpenPosition(
                title='Python Dev',
                url='www.carrers.com',
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


def get_open_opportunities(): List[OpenPosition]
    pass

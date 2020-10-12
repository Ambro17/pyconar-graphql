from strawapp.domain import Company, Sponsor, OpenPosition, SponsorType
from typing import List
from strawapp.db.database import Sponsorship

CATEGORIES = {
    1: SponsorType.DIAMANTE,
    2: SponsorType.ORO,
}

def get_sponsors() -> List[Sponsor]:
    return [
        Sponsor(
            company=Company(
                name=s.company.name,
                tagline=s.company.tagline,
                website=s.company.website,
                technologies=s.company.technologies.split(','),
                open_positions=s.company.open_positions
            ),
            category=CATEGORIES[s.category]
        )
        for s in Sponsorship.select()
    ]


def get_open_opportunities() -> List[OpenPosition]:
    return [
        s.company.open_positions
        for s in Sponsorship.select()
    ]

from strawapp.domain import Company, Sponsor, OpenPosition, SponsorType
from typing import List
from strawapp.db.database import Sponsorship, OpenPosition as Job

CATEGORIES = {
    1: SponsorType.DIAMANTE,
    2: SponsorType.ORO,
}

def to_company(company):
    return Company(
        name=company.name,
        tagline=company.tagline,
        website=company.website,
        technologies=company.technologies.split(','),
        open_positions=company.open_positions
    )

def get_sponsors() -> List[Sponsor]:
    return [
        Sponsor(
            company=to_company(s.company),
            category=CATEGORIES[s.category]
        )
        for s in Sponsorship.select()
    ]


def get_open_opportunities() -> List[OpenPosition]:
    return [
        OpenPosition(
           company=to_company(job.company),
           title=job.title,
           url=job.url,
        )
        for job in Job.select()
    ]

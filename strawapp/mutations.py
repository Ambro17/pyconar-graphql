from enum import Enum
from typing import List
import strawberry
from strawapp.domain import Company, Sponsor, SponsorType, Talk, OpenPosition
from dataclasses import field


@strawberry.input
class CompanyInput:
    name: str
    website: str
    tagline: str = ''
    technologies: List[str] = field(default_factory=list)


@strawberry.enum
class SponsorTypeInput(Enum):
    DIAMANTE: str = 'Diamante'
    ORO: str = 'Oro'
    PLATA: str = 'Plata'
    BRONCE: str = 'Bronce'


@strawberry.type
class Mutation:

    @strawberry.input
    class AddNewSponsorInput:
        company: CompanyInput
        category: SponsorTypeInput


    @strawberry.mutation
    def add_new_sponsor(self, input: AddNewSponsorInput) -> Sponsor:
        # Add to json
        # Add error handling with useful messages
        import pdb; pdb.set_trace()
        return Sponsor(**input.__dict__)
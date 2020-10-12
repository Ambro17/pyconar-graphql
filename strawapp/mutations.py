from peewee import DoesNotExist
from typing import List, Optional
import strawberry
from strawapp.domain import Company
from strawapp.db.database import Company as CompanyModel, OpenPosition as OpenPositionModel
from dataclasses import field


@strawberry.input
class CompanyInput:
    name: str
    website: str
    tagline: str = ''
    technologies: List[str] = field(default_factory=list)

@strawberry.type
class CompanyOutput:
    company: Company
    actions: List[str]

@strawberry.input
class AddCompanyInput:
    company: CompanyInput


@strawberry.input
class OpenPositionInput:
    title: str
    url: str

@strawberry.input
class AddOpenPositionInput:
    company_name: str
    position: OpenPositionInput

@strawberry.type
class AddOpenPositionOutput:
    company: Company


@strawberry.type
class Mutation:

    @strawberry.mutation
    def add_new_company(self, input: AddCompanyInput) -> CompanyOutput:
        # Add to json
        # Add error handling with useful messages
        company = input.company
        new_company = CompanyModel.create(
            name=company.name,
            website=company.website,
            tagline=company.tagline,
            technologies=','.join(company.technologies)
        )
        def to_graphql(c):
            """Map database model to graphql model. Side-Effect of decoupling them.."""
            c.technologies = c.technologies.split(',') if c.technologies else []
            return c

        return CompanyOutput(
            company=to_graphql(new_company),
            actions=['addOpenPosition']
        )
    
    @strawberry.mutation
    def add_open_position(self, input: AddOpenPositionInput) -> AddOpenPositionOutput:
        name = input.company_name
        position = input.position
        try:
            company = CompanyModel.get(CompanyModel.name==name)
        except DoesNotExist:
            raise ValueError('Company name does not exist')
        
        OpenPositionModel(company=company, title=position.title, url=position.url).save()
        return AddOpenPositionOutput(
            company=company
        )

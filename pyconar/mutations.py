import os
from strawberry.permission import BasePermission
from peewee import DoesNotExist
from typing import List
import strawberry
from pyconar.domain import Company
from pyconar.db.database import Company as CompanyModel, OpenPosition as OpenPositionModel
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
class AddOpenPositionCreated:
    company: Company

@strawberry.type
class AddOpenPositionFailed:
    error: str


AddOpenPositionOutput = strawberry.union("AddOpenPositionOutput", (AddOpenPositionCreated, AddOpenPositionFailed))


class MutationsEnabled(BasePermission):
    message = "You are not authorized"

    def has_permission(self, source, info, **kwargs):
        return os.getenv('MUTATIONS_ENABLED', False)


@strawberry.type
class Mutation:

    @strawberry.mutation(permission_classes=[MutationsEnabled])
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
    
    @strawberry.mutation(permission_classes=[MutationsEnabled])
    def add_open_position(self, input: AddOpenPositionInput) -> AddOpenPositionOutput:
        name = input.company_name
        position = input.position
        try:
            company = CompanyModel.get(CompanyModel.name==name)
        except DoesNotExist:
            return AddOpenPositionFailed(
                error='Company name does not exist'
            )
        
        OpenPositionModel(company=company, title=position.title, url=position.url).save()
        return AddOpenPositionCreated(
            company=company
        )

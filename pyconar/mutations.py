import os
from strawberry.permission import BasePermission
from peewee import DoesNotExist
from typing import List
import strawberry
from pyconar.domain import Company
from pyconar.db.database import Company as CompanyModel, OpenPosition as OpenPositionModel


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
    suggestion: str = "Fix the error and retry"


AddOpenPositionResult = strawberry.union("AddOpenPositionResult", (AddOpenPositionCreated, AddOpenPositionFailed),
                                         description="Union of possible outcomes when adding a position to a company")


class MutationsEnabled(BasePermission):
    message = "You are not authorized"

    def has_permission(self, source, info, **kwargs):
        return os.getenv('MUTATIONS_ENABLED', False)


ADD_OPEN_POSITION_EXAMPLE = """
```
mutation AgregarBusqueda {
  addOpenPosition(input: {
      companyName: "CompanyName", 
      position: {title: "Architect", url: "www.url.com"}
    }) {
    __typename  # Field to discriminate successfull results from failed ones
    ... on AddOpenPositionCreated {
      # The position was added successfully
      company {
        name
        openPositions {
          title
          url
        }
      }
    }
    ... on AddOpenPositionFailed {
      # There was an error adding the position
      error
      suggestion
    }

  }
}
```
""".strip()

@strawberry.type
class Mutation:
   
    @strawberry.mutation(
        permission_classes=[MutationsEnabled], 
        description=f"Add a new open positions for the given company. Example:\n{ADD_OPEN_POSITION_EXAMPLE}"
    )
    def add_open_position(self, input: AddOpenPositionInput) -> AddOpenPositionResult:
        name = input.company_name
        position = input.position
        try:
            company = CompanyModel.get(CompanyModel.name==name)
        except DoesNotExist:
            return AddOpenPositionFailed(
                error='Company name does not exist',
                suggestion='Please review any possible typos and retry with a valid company name'
            )
        
        OpenPositionModel(company=company, title=position.title, url=position.url).save()
        return AddOpenPositionCreated(
            company=company
        )

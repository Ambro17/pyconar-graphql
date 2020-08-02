"""Map plain dataclasses to strawberry types"""
from . import (
    Company as _Company,
    Edition as _Edition,
    OpenPosition as _OpenPosition,
    Person as _Person,
    Speaker as _Speaker,
    Sponsor as _Sponsor,
    SponsorType as _SponsorType,
    Talk as _Talk,
    Topic as _Topic,
    Visitor as _Visitor,
)

import strawberry


Company = strawberry.type(_Company)
Edition = strawberry.type(_Edition)
OpenPosition = strawberry.type(_OpenPosition)

Person = strawberry.interface(_Person)
Speaker = strawberry.type(_Speaker)
Sponsor = strawberry.type(_Sponsor)

SponsorType = strawberry.type(_SponsorType)
Talk = strawberry.type(_Talk)
Topic = strawberry.type(_Topic)
Visitor = strawberry.type(_Visitor)
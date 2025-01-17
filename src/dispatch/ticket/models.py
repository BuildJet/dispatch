from pydantic import validator

from typing import Optional

from sqlalchemy import Column, Integer, ForeignKey

from dispatch.database.core import Base
from dispatch.messaging.strings import INCIDENT_TICKET_DESCRIPTION
from dispatch.models import DispatchBase, ResourceMixin


class Ticket(Base, ResourceMixin):
    id = Column(Integer, primary_key=True)
    incident_id = Column(Integer, ForeignKey("incident.id", ondelete="CASCADE"))


# Pydantic models...
class TicketBase(DispatchBase):
    resource_id: Optional[str]
    resource_type: Optional[str]
    weblink: Optional[str]


class TicketCreate(TicketBase):
    pass


class TicketUpdate(TicketBase):
    pass


class TicketRead(TicketBase):
    description: Optional[str]

    @validator("description", pre=True, always=True)
    def set_description(cls, v):
        """Sets the description"""
        return INCIDENT_TICKET_DESCRIPTION


class TicketNested(TicketBase):
    id: int

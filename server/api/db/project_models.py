# external imports
import pytz
import datetime as dt
from pydantic import Field
from typing import Optional

# internal imports
from api.db.base_models import Serialization
from api.db.pydantic_objectid import PydanticObjectId

class Project(Serialization):
    id: Optional[PydanticObjectId] = Field(alias='_id', default=None)
    user_id: Optional[PydanticObjectId] = Field(default=None)
    name: str
    organization: Optional[str] = Field(default=None)
    created_at: dt.datetime = Field(default_factory=lambda: dt.datetime.now(tz=pytz.timezone('Asia/Kolkata')))
    updated_at: Optional[dt.datetime] = Field(default=None)

    def set_updated_at(self):
        self.updated_at = dt.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
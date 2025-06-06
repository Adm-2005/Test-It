# external imports
import pytz
import datetime as dt
from pydantic import Field
from typing import Optional, List

# internal imports
from api.db.base_models import Serialization
from api.db.pydantic_objectid import PydanticObjectId

class Session(Serialization):
    id: Optional[PydanticObjectId] = Field(alias='_id', default=None)
    proj_id: Optional[PydanticObjectId] = Field(default=None)
    name: str 
    scope: str
    context: Optional[str] = Field(default='')
    input_images: Optional[List[str]] = Field(default=None) # list contains paths to image files
    input_code: Optional[str] = Field(default='')
    generated_response: Optional[str] = Field(default='')
    created_at: dt.datetime = Field(default_factory=lambda: dt.datetime.now(tz=pytz.timezone('Asia/Kolkata')))
    updated_at: Optional[dt.datetime] = Field(default=None)

    def set_updated_at(self):
        self.updated_at = dt.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
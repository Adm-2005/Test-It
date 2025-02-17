# external imports
from pydantic import Field
from typing import Optional

# internal imports
from api.db.base_models import Serialization
from api.db.pydantic_objectid import PydanticObjectId

class Session(Serialization):
    id: Optional[PydanticObjectId] = Field(alias='_id', default=None)
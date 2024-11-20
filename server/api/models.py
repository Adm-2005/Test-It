import torch
import datetime
from pydantic import BaseModel, Field
from typing import Optional, Dict, List
from fastapi.encoders import jsonable_encoder
from ..utils.objectId import PydanticObjectId
from werkzeug.security import check_password_hash, generate_password_hash

class Session(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias='_id')
    project_id: Optional[PydanticObjectId] = Field(None)
    name: str
    scope: str
    context: Optional[str]
    inputImages: Optional[List[str]] = Field(default_factory=list)
    inputCode: Optional[str]
    output: Optional[str]
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now(tz=datetime.timezone.utc))
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now(tz=datetime.timezone.utc))

    def set_image(self, images: List[torch.Tensor]):
        """
        Converts the tensors in the list into flattened lists and then stores them as string.
        """
        for image in images:
            flattened_image = image.flatten().tolist()
            self.inputImages.append(flattened_image)

    def get_image_tensor(self) -> torch.Tensor:
        data = []
        for image in self.inputImages:
            data.append(torch.Tensor(image))
        return data

    def to_json(self):
        return jsonable_encoder(self)
    
    def to_bson(self):
        data = self.model_dump(by_alias=True)
        if data.get('_id') is None:
            data.pop('_id', None)

        return data

class Project(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias='_id')
    user_id: Optional[PydanticObjectId] = Field(None)
    project_name: str
    organization: Optional[str]
    sessions: Optional[List[PydanticObjectId]] = Field(default_factory=list)
    created_at: datetime.datetime = Field(datetime.datetime.now(tz=datetime.timezone.utc)) 
    updated_at: datetime.datetime = Field(datetime.datetime.now(tz=datetime.timezone.utc))

    def to_json(self):
        return jsonable_encoder(self)
    
    def to_bson(self):
        data = self.model_dump(by_alias=True)
        if data.get('_id') is None:
            data.pop('_id', None)

        return data

class User(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias='_id')
    full_name: str
    email: str
    username: str
    hashed_password: str
    projects: Optional[List[PydanticObjectId]] = Field(default_factory=list)

    def set_password(self, password: str):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.hashed_password, password)

    def to_json(self):
        return jsonable_encoder(self)
    
    def to_bson(self):
        data = self.model_dump(by_alias=True)
        if data.get('_id') is None:
            data.pop('_id', None)

        return data
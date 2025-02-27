from pydantic import BaseModel
from typing import List, Optional
from datetime import date, datetime


class VisitorFilter(BaseModel):
    limit: Optional[int] = None
    page: Optional[int] = None
    search: Optional[str] = None

class Face (BaseModel):
    image : Optional[str] = None
    trx_id : Optional[str] = None

class IdentifyVisitor(BaseModel):
    image : str
    client_name:Optional[str] = None

class CreateNewVisitor(BaseModel):
    username: Optional[str] = None
    full_name: str
    nik : str
    born_date: date
    email: str
    address:str
    company_name :str
    # faces : Optional[List[Face]] = None
    image : Optional[str] = None
    client_name:Optional[str] = None


class GetVisitor(BaseModel):
    username:str
    nik:str

class IdentifyVisitorFace(BaseModel):
    facegallery_id:str
    image: Optional[str] = None
    trx_id:Optional[str] = None

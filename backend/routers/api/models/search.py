# pylint: disable=line-too-long
from enum import Enum
from typing import Union
import pydantic

class DocType(str, Enum):
    IR_MATERIAL = 'ir_material'
    OTHER = 'other'


class SearchCompany(pydantic.BaseModel):
    edinet_code: Union[str, list[str], None] = None
    security_code: Union[str, None] = None
    company_name: Union[str, None] = None
    company_address: Union[str, None] = None
    industry: Union[str, None] = None

class SearchDocument(pydantic.BaseModel):
    type: Union[DocType, None] = None
    file_name: Union[str, None] = None
    content: str = None
    company_edinet_code: Union[str, list[str], None] = pydantic.Field(alias="company.edinet_code")
    company_security_code: Union[str, None] = pydantic.Field(alias="company.security_code")
    company_company_name: Union[str, None] = pydantic.Field(alias="company.company_name")
    company_company_address: Union[str, None] = pydantic.Field(alias="company.company_address")
    company_industry: Union[str, None] = pydantic.Field(alias="company.industry")


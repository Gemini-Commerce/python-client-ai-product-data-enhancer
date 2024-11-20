# coding: utf-8

"""
    aiproductdataenhancer/service.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from aiproductdataenhancer.models.aiproductdataenhancer_generate_product_data_request_product_information import AiproductdataenhancerGenerateProductDataRequestProductInformation
from aiproductdataenhancer.models.aiproductdataenhancer_language_code import AiproductdataenhancerLanguageCode
from aiproductdataenhancer.models.generate_product_data_request_product_data_to_generate import GenerateProductDataRequestProductDataToGenerate
from typing import Optional, Set
from typing_extensions import Self

class AiproductdataenhancerGenerateProductDataRequest(BaseModel):
    """
    AiproductdataenhancerGenerateProductDataRequest
    """ # noqa: E501
    tenant_id: Optional[StrictStr] = Field(default=None, alias="tenantId")
    language_code: Optional[AiproductdataenhancerLanguageCode] = Field(default=AiproductdataenhancerLanguageCode.UNKNOWN, alias="languageCode")
    product_information: Optional[List[AiproductdataenhancerGenerateProductDataRequestProductInformation]] = Field(default=None, alias="productInformation")
    product_data_to_generate: Optional[List[GenerateProductDataRequestProductDataToGenerate]] = Field(default=None, alias="productDataToGenerate")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["tenantId", "languageCode", "productInformation", "productDataToGenerate"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AiproductdataenhancerGenerateProductDataRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in product_information (list)
        _items = []
        if self.product_information:
            for _item_product_information in self.product_information:
                if _item_product_information:
                    _items.append(_item_product_information.to_dict())
            _dict['productInformation'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in product_data_to_generate (list)
        _items = []
        if self.product_data_to_generate:
            for _item_product_data_to_generate in self.product_data_to_generate:
                if _item_product_data_to_generate:
                    _items.append(_item_product_data_to_generate.to_dict())
            _dict['productDataToGenerate'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiproductdataenhancerGenerateProductDataRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "languageCode": obj.get("languageCode") if obj.get("languageCode") is not None else AiproductdataenhancerLanguageCode.UNKNOWN,
            "productInformation": [AiproductdataenhancerGenerateProductDataRequestProductInformation.from_dict(_item) for _item in obj["productInformation"]] if obj.get("productInformation") is not None else None,
            "productDataToGenerate": [GenerateProductDataRequestProductDataToGenerate.from_dict(_item) for _item in obj["productDataToGenerate"]] if obj.get("productDataToGenerate") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


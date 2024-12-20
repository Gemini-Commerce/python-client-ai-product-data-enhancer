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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from aiproductdataenhancer.models.aiproductdataenhancer_language_code import AiproductdataenhancerLanguageCode
from aiproductdataenhancer.models.aiproductdataenhancer_product_data_to_fill import AiproductdataenhancerProductDataToFill
from aiproductdataenhancer.models.aiproductdataenhancer_product_information import AiproductdataenhancerProductInformation
from typing import Optional, Set
from typing_extensions import Self

class AiproductdataenhancerFillProductDataRequest(BaseModel):
    """
    AiproductdataenhancerFillProductDataRequest
    """ # noqa: E501
    tenant_id: Optional[StrictStr] = Field(default=None, alias="tenantId")
    language_code: Optional[AiproductdataenhancerLanguageCode] = Field(default=AiproductdataenhancerLanguageCode.UNKNOWN, alias="languageCode")
    product_information: Optional[AiproductdataenhancerProductInformation] = Field(default=None, alias="productInformation")
    product_data_to_fill: Optional[List[AiproductdataenhancerProductDataToFill]] = Field(default=None, alias="productDataToFill")
    domains_to_include: Optional[List[StrictStr]] = Field(default=None, alias="domainsToInclude")
    domains_to_exclude: Optional[List[StrictStr]] = Field(default=None, alias="domainsToExclude")
    extract_images: Optional[StrictBool] = Field(default=None, alias="extractImages")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["tenantId", "languageCode", "productInformation", "productDataToFill", "domainsToInclude", "domainsToExclude", "extractImages"]

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
        """Create an instance of AiproductdataenhancerFillProductDataRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of product_information
        if self.product_information:
            _dict['productInformation'] = self.product_information.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in product_data_to_fill (list)
        _items = []
        if self.product_data_to_fill:
            for _item_product_data_to_fill in self.product_data_to_fill:
                if _item_product_data_to_fill:
                    _items.append(_item_product_data_to_fill.to_dict())
            _dict['productDataToFill'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiproductdataenhancerFillProductDataRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "languageCode": obj.get("languageCode") if obj.get("languageCode") is not None else AiproductdataenhancerLanguageCode.UNKNOWN,
            "productInformation": AiproductdataenhancerProductInformation.from_dict(obj["productInformation"]) if obj.get("productInformation") is not None else None,
            "productDataToFill": [AiproductdataenhancerProductDataToFill.from_dict(_item) for _item in obj["productDataToFill"]] if obj.get("productDataToFill") is not None else None,
            "domainsToInclude": obj.get("domainsToInclude"),
            "domainsToExclude": obj.get("domainsToExclude"),
            "extractImages": obj.get("extractImages")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj



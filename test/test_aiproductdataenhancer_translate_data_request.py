# coding: utf-8

"""
    aiproductdataenhancer/service.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from aiproductdataenhancer.models.aiproductdataenhancer_translate_data_request import AiproductdataenhancerTranslateDataRequest

class TestAiproductdataenhancerTranslateDataRequest(unittest.TestCase):
    """AiproductdataenhancerTranslateDataRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AiproductdataenhancerTranslateDataRequest:
        """Test AiproductdataenhancerTranslateDataRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AiproductdataenhancerTranslateDataRequest`
        """
        model = AiproductdataenhancerTranslateDataRequest()
        if include_optional:
            return AiproductdataenhancerTranslateDataRequest(
                tenant_id = '',
                target_language = 'LANGUAGE_CODE_UNKNOWN',
                source_language = 'LANGUAGE_CODE_UNKNOWN',
                data_to_translate = [
                    aiproductdataenhancer.models.aiproductdataenhancer_data_to_translate.aiproductdataenhancerDataToTranslate(
                        name = '', 
                        value = '', )
                    ]
            )
        else:
            return AiproductdataenhancerTranslateDataRequest(
        )
        """

    def testAiproductdataenhancerTranslateDataRequest(self):
        """Test AiproductdataenhancerTranslateDataRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

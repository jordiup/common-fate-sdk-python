# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import jhc_cf_sdk_test
from jhc_cf_sdk_test.paths.api_v1_admin_providersetups_providersetup_id_steps_step_index_complete import put  # noqa: E501
from jhc_cf_sdk_test import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1AdminProvidersetupsProvidersetupIdStepsStepIndexComplete(ApiTestMixin, unittest.TestCase):
    """
    ApiV1AdminProvidersetupsProvidersetupIdStepsStepIndexComplete unit test stubs
        Update the completion status for a Provider setup step  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()

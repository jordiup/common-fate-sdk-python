# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import jhc_cf_sdk_test
from jhc_cf_sdk_test.paths.api_v1_admin_access_rules_rule_id_archive import post  # noqa: E501
from jhc_cf_sdk_test import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1AdminAccessRulesRuleIdArchive(ApiTestMixin, unittest.TestCase):
    """
    ApiV1AdminAccessRulesRuleIdArchive unit test stubs
        Archive Access Rule  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()

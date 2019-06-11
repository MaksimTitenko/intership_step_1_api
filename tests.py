import re
import unittest

from main import get_api_url, get_params
from task import kufar_parser


class TestParseMethod(unittest.TestCase):
    def setUp(self) -> None:
        self.api_url = get_api_url()
        self.params = get_params()
        self.links = kufar_parser(self.api_url, self.params)

    def test_parser_response_instance(self) -> None:
        self.assertIsInstance(self.links, list)

    def test_parser_response_link_instances(self) -> None:
        for link in self.links:
            self.assertIsInstance(link, str)

    def test_parser_response_valid_link(self) -> None:
        for link in self.links:
            result = re.search(r'https://re\.kufar\.by/vi/[0-9]+', link)
            self.assertIsNotNone(result.group(0))

    def test_parser_different_links(self):
        links = set(self.links)
        self.assertTrue(len(links) > 1)


if __name__ == '__main__':
    unittest.main()

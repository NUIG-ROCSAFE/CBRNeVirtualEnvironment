import os
import utils
import unittest
import elastic_utils

from elasticsearch import Elasticsearch
from sop_server import app


class SopTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.es = Elasticsearch()
        self.db_conn, self.sop_location, self.pdf_loc, self.index_name = utils.get_config('main.ini')
        self.search_terms = 'headache'

    def test_ini(self):
        self.assertTrue(os.path.exists(self.db_conn))
        self.assertTrue(os.path.exists(self.sop_location))
        self.assertTrue(os.path.exists(self.pdf_loc))

    def test_search(self):
        headache_rankings = elastic_utils.compute_ranking(self.es, self.index_name, "text", self.search_terms)
        self.assertDictEqual({'0': 0.0, '5': 0.0, '2': 0.0, '4': 0.0, '1': 0.45428392, '3': 0.0}, headache_rankings)

    def test_flask(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()

import utils
import elastic_utils
import sys
from elasticsearch import Elasticsearch


def main():
    es = Elasticsearch()

    db_conn, _, _, index_name = utils.get_config('./main.ini')

    # get the search terms to rank
    # TODO maybe move arg parsing to its own fn
    search_terms = sys.argv[1:]
    print("searching for terms: ", search_terms)
    search_terms = [search_term.strip() for search_term in search_terms]
    # first add synonyms to elasticsearch
    elastic_utils.add_synoyms()
    sop_rankings_dict = elastic_utils.compute_ranking(es, index_name, "text", search_terms[0])
    print('res: ', sop_rankings_dict)
    elastic_utils.insert_rank(sop_rankings_dict, search_terms, db_conn)
    print(sop_rankings_dict)


if __name__ == '__main__':
    main()

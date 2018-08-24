import utils
import elastic_utils
import sys
import insert_records
from elasticsearch import Elasticsearch


def main():
    es = Elasticsearch()
    db_conn, _, _, index_name = utils.get_config('./main.ini')

    search_terms = sys.argv[1:]
    if len(search_terms) == 0:
        print("Error: Include search terms in script parameters e.g. headache, pulmonary...")
        exit(-1)

    insert_records.insert(es, index_name)
    print("searching for terms: ", search_terms)
    search_terms = [search_term.strip() for search_term in search_terms]

    sop_rankings_dict = elastic_utils.compute_ranking(es, index_name, "text", search_terms)
    elastic_utils.insert_rank(sop_rankings_dict, search_terms, db_conn)
    print(sop_rankings_dict)


if __name__ == '__main__':
    main()

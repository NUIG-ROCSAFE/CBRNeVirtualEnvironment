import sqlite3
from datetime import datetime


def insert_rank(sop_rankings_dict, search_terms, db_conn):
    """Insets new rankings into DB based on search terms"""
    db_conn = sqlite3.connect(db_conn)
    n = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur = db_conn.cursor()

    for i, score in sop_rankings_dict.items():
        sql = '''insert into Rank(Date, Rank, SOPID, SearchTerms) values (?,?,?,?)'''
        params = (str(n), score, i, str(search_terms))
        cur.execute(sql, params)
        db_conn.commit()
    db_conn.close()


def format_synonyms(synonym_dict):
    """Takes a synonym dict and formats it to be written with elasticsearch"""
    synonym_list = []
    for word, synonyms in sorted(synonym_dict.items()):
        for synonym in synonyms:
            pair = "\t\t\t\t\t\t\"%s,%s\"" % (word.strip(), synonym.strip())
            synonym_list.append(pair)
    return synonym_list


def return_query(es, index_name, field, search_name):
    res = es.search(index=index_name, body={"query": {"match": {field: str(search_name)}}})
    sop_dict = res['hits']['hits']
    for sop in sop_dict:
        yield sop['_id'], sop['_score']


def return_all(es, index_name):
    print("return_all: index_name = " + index_name)
    res = es.search(index=index_name, body={"query": {"match_all": {}}})
    sop_dict = res['hits']['hits']
    for sop in sop_dict:
        yield sop['_id'], 0.0


def compute_ranking(es, index_name, field, search_name):
    res = {}
    for i, score in return_all(es, index_name):
        res[i] = score

    for i, score in return_query(es, index_name, field, search_name):
        res[i] = score

    return res


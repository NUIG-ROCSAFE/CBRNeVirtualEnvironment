import json
import sqlite3
import os
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
    res = es.search(index=index_name, body={"query": {"match": {field: search_name}}})
    sop_dict = res['hits']['hits']
    for sop in sop_dict:
        yield sop['_id'], sop['_score']


def return_all(es, index_name):
    print("return_all: index_name = " + index_name)
    res = es.search(index=index_name, body={"query": {"match_all": {}}})
    sop_dict = res['hits']['hits']
    for sop in sop_dict:
        yield sop['_id'], 0.0
    print("Finish return_all")


def compute_ranking(es, index_name, field, search_name):
    res = {}
    for i, score in return_all(es, index_name):
        res[i] = score

    for i, score in return_query(es, index_name, field, search_name):
        res[i] = score
    print('compute ranking res: ', res)

    return res


def add_synoyms():
    synonym_dict = json.loads(open("../Synonyms/synonyms.json", 'r').read())
    synonym_list = format_synonyms(synonym_dict)
    s = ",\n"
    synoyms = s.join(synonym_list)

    doc = "PUT /index/sops"
    doc += "{ "
    doc += "  \"settings\": {\n"
    doc += "      \"analysis\": {\n"
    doc += "          \"filter\": {\n"
    doc += "              \"CBRNE_filter\": {\n"
    doc += "                  \"type\": \"synonym\",\n"
    doc += "                  \"synonyms\": [ \n"

    doc += synoyms
    doc += "         }\n"
    doc += "      },\n"
    doc += "      \"analyzer\":{\n"
    doc += "          \"tokenizer\": \"standard\",\n"
    doc += "          \"CBRNE\":{\n"
    doc += "          \"filter\": [\n"
    doc += "              \"lowercase\",\n"
    doc += "              \"CBRNE_filter\"\n"
    doc += "          ]\n"
    doc += "      }\n"
    doc += "  }\n"
    doc += "}\n}\n}"


def return_sops(soplocation):
    for f in os.listdir(soplocation):
        yield "%s%s" % (soplocation, f), f



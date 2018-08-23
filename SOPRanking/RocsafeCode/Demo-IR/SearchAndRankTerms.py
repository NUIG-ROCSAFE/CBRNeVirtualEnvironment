from datetime import datetime
import time
from elasticsearch import Elasticsearch
import os, sqlite3, json, pickle, flask
import ConfigParser, sys


def ConfigSectionMap(section, Config):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


def get_config():
    inilocation = "./main.ini"
    Config = ConfigParser.ConfigParser()
    Config.read(inilocation)

    section = "sqlite"
    config_dict = None

    try:
        config_dict = ConfigSectionMap(section, Config)
    except:
        print("Can't find ini file: %s" % (inilocation))
        exit()

    location = config_dict["dblocation"]
    soplocation = config_dict["soplocation"]
    indexName = config_dict["indexname"]

    if not os.path.isfile(location):
        strError = "File %s does not exist" % (location)
        returnMessage(strError)
        exit()

    if not os.path.isdir(soplocation):
        strError = "Directory %s does not exist" % (soplocation)
        returnMessage(strError)
        exit()

    if not indexName:
        strError = "indexName not set"
        returnMessage(strError)
        exit()

    return config_dict


def insertRank(sop_rankings_dict, searchTerms, dbconn):
    n = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur = dbconn.cursor()

    for i, score in sop_rankings_dict.items():
        sql = '''insert into Rank(Date, Rank, SOPID, SearchTerms) values (?,?,?,?)'''
        params = (str(n), score, i, str(searchTerms))
        cur.execute(sql, params)
        dbconn.commit()
    dbconn.close()


def format_synonyms(synonym_dict):
    """takes a synonym dict and formats it to be written with elasticsearch"""
    synonym_list = []
    for word, synonyms in sorted(synonym_dict.items()):
        for synonym in synonyms:
            pair = "\t\t\t\t\t\t\"%s,%s\"" % (word.strip(), synonym.strip())
            synonym_list.append(pair)
    return synonym_list

def returndoc():
    for flocation, title in returnSOPS():
        title = title[0:-4]
        text = returntext(flocation)
        doc = {
            'title': title,
            'text': text,
        }
        yield doc


def returnQuery(es, indexName, field, searchTerm):
    res = es.search(index=indexName, body={"query": {"match": {field: searchTerm}}})
    d = res['hits']['hits']
    for dx in d:
        yield dx['_id'], dx['_score']


def returnAll(es, indexName):
    print("returnAll: indexName=" + indexName)
    res = es.search(index=indexName, body={"query": {"match_all": {}}})
    print("Results Returned")
    print("RESULT : " + str(res))
    d = res['hits']['hits']
    print('d', d)
    print("SELECT HITS : " + str(d))
    for dx in d:
        yield dx['_id'], 0.0
    print("Finish returnAll")


def computeRanking(es, indexName, field, searchTerm):
    res = {}
    # try:
    for i, score in returnAll(es, indexName):
        res[i] = score

    for i, score in returnQuery(es, indexName, field, searchTerm):
        res[i] = score
    print('compute ranking res: ', res)
    # except:
    # strError = "Elastic Search is Down"
    # returnMessage(strError)
    # exit()

    return res


def returnSynoyms(d):
    l = []
    for word, synonyms in sorted(d.items()):
        try:
            print(word, ':', synonyms.split(','), ',')
        except Exception as e:
            print([], ',')
        for synonym in synonyms.split(","):
            pair = "\t\t\t\t\t\t\"%s,%s\"" % (word.strip(), synonym.strip())
            l.append(pair)
    return l


def addSynonyms():
    synonym_dict = json.loads(open("../Synonyms/synonyms.json", 'r').read())
    synonym_list = format_synonyms(synonym_dict)
    s = ",\n"
    syns = s.join(synonym_list)

    doc = "PUT /index/sops"
    doc += "{ "
    doc += "  \"settings\": {\n"
    doc += "      \"analysis\": {\n"
    doc += "          \"filter\": {\n"
    doc += "              \"CBRNE_filter\": {\n"
    doc += "                  \"type\": \"synonym\",\n"
    doc += "                  \"synonyms\": [ \n"

    doc += syns
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


def returnSOPS(soplocation):
    for f in os.listdir(soplocation):
        yield "%s%s" % (soplocation, f), f


def insertSOP(dbconn, soplocation):
    cur = dbconn.cursor()
    xid = 0
    for location, name in returnSOPS(soplocation):
        text = returntext(location)
        name = name[0:-4]

        sql = '''insert into SOP(ID, Title, Text) values (?,?,?)'''
        text = text.decode("utf-8")
        params = (xid, name, text)
        cur.execute(sql, params)
        dbconn.commit()

        xid += 1
    dbconn.close()


def returntext(flocation):
    inhandle = open(flocation, "r")
    text = ""
    for line in inhandle:
        text += " " + line
    inhandle.close()
    return text


def main():
    es = Elasticsearch()

    config_dict = get_config()
    dbconn = sqlite3.connect(config_dict["dblocation"])
    soplocation = config_dict["soplocation"]
    indexName = config_dict["indexname"]

    # get the search terms to rank
    search_terms = sys.argv[1:]
    print("searching for terms: ", search_terms)
    search_terms = [search_term.strip() for search_term in search_terms]
    # first add synonyms to elasticsearch
    addSynonyms()
    sop_rankings_dict = computeRanking(es, indexName, "text", search_terms[0])
    print('res: ', sop_rankings_dict)
    insertRank(sop_rankings_dict, search_terms, dbconn)
    print(sop_rankings_dict)


if __name__ == '__main__':
    main()
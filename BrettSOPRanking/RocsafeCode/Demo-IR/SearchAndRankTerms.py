from datetime import datetime
import time
from elasticsearch import Elasticsearch
import os, sqlite3, datetime, json, pickle,flask
import configparser,sys


def ConfigSectionMap(section,Config):
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
    Config = configparser.ConfigParser()
    Config.read(inilocation)
   
    section = "sqlite"
    config_dict = None

    try:
        config_dict = ConfigSectionMap(section,Config)
    except:
        print("Can't find ini file: %s" % (inilocation))
        exit()

    location = config_dict["dblocation"]
    soplocation = config_dict["soplocation"]
    indexName = config_dict["indexname"]

    if not os.path.isfile(location):
        strError ="File %s does not exist" % (location)
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
	
def insertRank(res, searchTerms, dbconn):
    
    n= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur = conn.cursor()

    for i, score in res.items():
        
        sql = '''insert into Rank(Date, Rank, SOPID, SearchTerms) values (?,?,?,?)'''
        params = (str(n),score,i, searchTerms)
        cur.execute(sql, params)
        conn.commit()
    conn.close()


def format_synonyms(synonym_dict):
	'''takes a synonym dict and formats it to be written with elasticsearch'''
	synonym_list = []
    for word, synonyms in sorted(synonym_dict.items()):
        for synonym in synonyms.split(","):
            pair ="\t\t\t\t\t\t\"%s,%s\"" %(word.strip(), synonym.strip())
            synonym_list.append(pair)
    return synonym_list
	
def addSynonyms():
    synonym_dict = json.loads(open("../Synonyms/synonyms.json",'r'))
    synonym_list = format_synonyms(d)
    s =",\n"
    syns = s.join(l)


    doc = "PUT /index/sops"
    doc+="{ "
    doc+="  \"settings\": {\n"
    doc+="      \"analysis\": {\n"
    doc+="          \"filter\": {\n"
    doc+="              \"CBRNE_filter\": {\n"
    doc+="                  \"type\": \"synonym\",\n"
    doc+="                  \"synonyms\": [ \n"

    doc+=syns
    doc+="         }\n"
    doc+="      },\n"
    doc+="      \"analyzer\":{\n"
    doc+="          \"tokenizer\": \"standard\",\n"
    doc+="          \"CBRNE\":{\n"
    doc+="          \"filter\": [\n"
    doc+="              \"lowercase\",\n"
    doc+="              \"CBRNE_filter\"\n"
    doc+="          ]\n"
    doc+="      }\n"
    doc+="  }\n"
    doc+="}\n}\n}"
	
def returnSOPS(soplocation):
    for f in os.listdir(soplocation):
        yield "%s%s" % (soplocation,f),f
		
def insertSOP(dbconn, soplocation):  
    cur = dbconn.cursor()
    xid = 0
    for location,name in returnSOPS(soplocation):
        text = returntext(location)
        name = name[0:-4]
        
        sql = '''insert into SOP(ID, Title, Text) values (?,?,?)'''
        text = text.decode("utf-8")
        params = (xid,name,text)
        cur.execute(sql, params)
        conn.commit()

        xid+=1
    conn.close()
	
def returntext(flocation):
    inhandle = open(flocation,"r")
    text = ""
    for line in inhandle:
        text+=" "+line
    inhandle.close()
    return text
	
def main():
	config_dict = get_config()
	dbconn = sqlite3.connect(config_dict["dblocation"])
	soplocation = config_dict["soplocation"]
    indexName = config_dict["indexname"]
	
	#get the search terms to rank
	search_terms = sys.argv[1:]
	print("searching for terms: ", search_terms)
	search_terms = [search_term.strip() for search_term in search_terms]
	es = Elasticsearch()
	#first add synonyms to elasticsearch
	addSynonyms()
	field = "text"
	res = computeRanking("text", searchTerm)
	print('res: ', res)
	insertRank(res, search_terms)
	#insertRank(res)
	print(line)
	print(res)
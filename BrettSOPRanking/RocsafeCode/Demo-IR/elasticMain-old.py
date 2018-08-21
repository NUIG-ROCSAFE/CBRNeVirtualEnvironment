from datetime import datetime
import time
from elasticsearch import Elasticsearch
import os, sqlite3, datetime, json, pickle,flask
import configparser,sys

global es
global indexName
global location
global soplocation
es = Elasticsearch()

# import logging
# import sys
# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


#json functions
def returnMessage(strMsg, error=True):
    if error:
        error = {"error":strMsg}
        print(json.dumps(error))
    else:
        message = {"message":strMsg}
        print(json.dumps(strMsg))



#read ini-file
def setGlobalVariables():

    global location
    global soplocation
    global indexName
    
    inilocation = "main.ini"
    Config = configparser.ConfigParser()
    Config.read(inilocation)
   
    section = "sqlite"
    keys = None

    try:
        keys = ConfigSectionMap(section,Config)
    except:
        print("Can't find ini file: %s" % (inilocation))
        exit()

    location = keys["dblocation"]
    soplocation = keys["soplocation"]
    indexName = keys["indexname"]

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


    
def ConfigSectionMap(section,Config):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


#SQLite Functions
def returnRank():
    global location 
    conn = sqlite3.connect(location)      
    cur = conn.cursor()
    sql = "SELECT SOP.Title, rank.rank from rank,SOP where rank.sopid = SOP.id "
    sql+= " and date in (select max(date) FROM Rank) order by rank desc"
    cur.execute(sql)
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

    
def insertRank(res):
    global location
    conn = sqlite3.connect(location)
    n= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur = conn.cursor()

    for i, score in res.items():
        
        sql = '''insert into Rank(Date, Rank, SOPID) values (?,?,?)'''
        params = (str(n),score,i)
        cur.execute(sql, params)
        conn.commit()
    conn.close()


def insertSOP():
    global location
  
    conn = sqlite3.connect(location)
    cur = conn.cursor()
    xid = 0
    for location,name in returnSOPS():
        text = returntext(location)
        name = name[0:-4]
        
        sql = '''insert into SOP(ID, Title, Text) values (?,?,?)'''
        text = text.decode()
        params = (xid,name,text)
        cur.execute(sql, params)
        conn.commit()

        xid+=1
    conn.close()
        

def returnSOPS():
    global soplocation
    for f in os.listdir(soplocation):
        yield "%s%s" % (soplocation,f),f


def returntext(flocation):
    inhandle = open(flocation,"r")
    text = ""
    for line in inhandle:
        text+=" "+line
    inhandle.close()
    return text


#ElasticSearch Functions

def returndoc():
    for flocation, title in returnSOPS():
        title = title[0:-4]
        text =  returntext(flocation)
        doc = {
    'title': title,
    'text': text,
    }
        yield doc
        

def returnQuery(field,searchTerm):
    res =es.search(index=indexName, body={"query": {"match": {field:searchTerm}}})    
    d = res['hits']['hits']        
    for dx in d:
        yield dx['_id'],dx['_score']

def returnAll():
    print("returnAll: indexName="+indexName) 
    res =es.search(index=indexName, body={"query": {"match_all": {}}})
    print("Results Returned")
    #print("RESULT : "+str(res))    
    d = res['hits']['hits']   
    #print("sELECT hITS : "+str(d))	
    for dx in d:
        yield dx['_id'],0.0
    print("Finish returnAll")	
        
def computeRanking(field,searchTerm):
    res = {}
    try:
        for i, score in returnAll():
            res[i]=score
            

        for i, score in returnQuery(field,searchTerm):
            res[i] = score
    except:
        strError = "Elastic Search is Down"
        returnMessage(strError)
        exit()

    return res



def returnSynoyms(d):
    l = []
    for word, synonyms in d.items():
        for synonym in synonyms.split(","):
            pair ="\t\t\t\t\t\t\"%s,%s\"" %(word.strip(), synonym.strip())
            l.append(pair)
    return l


def addSynonyms():
    d = pickle.load(open("synonyms.pck"))
    l = returnSynoyms(d)
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

    
    
            
#default search term
field = "text"
#searchTerm =""
#if len(sys.argv)==1:
#    searchTerm ="chlorine, mustard gas"
#else:
#    searchTerm = sys.argv[1]

inhandle = open("terms.txt")
for line in inhandle:
	searchTerm = line.strip()
	setGlobalVariables()
	#addSynonyms()
	res = computeRanking(field,searchTerm)
	insertRank(res)
	print(line)
	time.sleep(10)
# #strMsg = "Action Completed"
# #returnMessage(strMsg, False)


# def main():
	# search_terms = sys.argv[1:]
	# print("searching for terms: ", search_terms)
	# for line in search_terms:
		# searchTerm = line.strip()
	# setGlobalVariables()
	# addSynonyms()
	# res = computeRanking(field, search_terms)
	# insertRank(res, search_terms)
	# print(line)
	
# if __name__ == '__main__':
	# main()





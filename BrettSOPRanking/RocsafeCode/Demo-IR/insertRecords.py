from elasticsearch import Elasticsearch
import os

es = Elasticsearch()

def insertSOP(title, text, idno):
    doc = {
    'title': title,
    'text': text
    }
    
    res = es.index(index="sops", doc_type='sop', id=idno, body=doc)



#insert SOP into 
location ="text/"
for counter,title in enumerate(os.listdir(location)):
    fileLocation ="%s%s" % (location, title)
    print ("Reading file: "+fileLocation)
    text = open(fileLocation,encoding="UTF8").read()
    print ("Inserting SOP: "+title)
    insertSOP(title, text, counter)

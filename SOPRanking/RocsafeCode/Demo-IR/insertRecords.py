from elasticsearch import Elasticsearch
import os

INDEX_NAME = 'sops'
es = Elasticsearch()


def insertSOP(title, text, idno):
    doc = {
        'title': title,
        'text': text
    }

    res = es.index(index="sops", doc_type='sop', id=idno, body=doc)


def insert():
    # insert SOP into
    location = "text/"
    response = es.indices.create(index=INDEX_NAME)
    for counter, title in enumerate(os.listdir(location)):
        fileLocation = "%s%s" % (location, title)
        print ("Reading file: " + fileLocation)
        # text = open(fileLocation,encoding="UTF8").read()
        text = open(fileLocation).read()
        print ("Inserting SOP: " + title)
        insertSOP(title, text, counter)

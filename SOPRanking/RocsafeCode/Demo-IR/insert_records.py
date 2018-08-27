import os

from elasticsearch import RequestError


def insert_sop(es, index_name, title, text, idno):
    doc = {
        'title': title,
        'text': text
    }

    es.index(index=index_name, doc_type='sop', id=idno, body=doc)


def insert(es, index_name):
    # insert SOP into
    location = "./text/"
    try:
        es.indices.create(index=index_name)
    except RequestError:
        print("Index %s exists, continuing" % index_name)

    for counter, title in enumerate(os.listdir(location)):
        file_loc = "%s%s" % (location, title)
        print("Reading file: " + file_loc)
        text = open(file_loc, encoding='utf-8').read()
        print("Inserting SOP: " + title)
        insert_sop(es, index_name, title, text, counter)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string,itertools
import urllib2, codecs
import requests
from lxml import html
from time import sleep
from random import randint
from selenium import webdriver
from pyvirtualdisplay import Display
import time, re, pickle
from selenium import webdriver
from random import randint

location = "http://opencbrne.jrc.ec.europa.eu/page/%d?fchar=%s"
urlLocation = "http://opencbrne.jrc.ec.europa.eu/page/%d"


def returnChars():
    chars = string.ascii_uppercase[:26]
    for char in chars:
        yield char

def returnNumbers():
    for n in itertools.count():
        yield n


def returnURL():
    for c in returnChars():
        for n in returnNumbers():
            url = location %(n,c)
            yield url



def readFile():
    location = "CBRNEURLS.txt"
    for l in open(location):
        if not l.strip():
            continue
        yield l

def returnSynonym(text):
    anchors = ["see:","see also:"]

    if not text:
        return ""
    
    for anchor in anchors:
        if anchor not in text.lower():
            continue
     
        index = text.lower().index(anchor)
        index+=len(anchor)+1
        return text[index:].strip()
    return ""
    
def dumpText(outhandle, name, text):
    name = name.strip()
    text = text.strip()
    text = text.encode('utf-8', 'ignore').decode('utf-8')
    dumpText = "%s\n%s\n%s\n\n\n" % (name,text, "End Record")
    outhandle.write(dumpText)


def scrapeSite():
    d = {}
    outhandle = codecs.open("PlainTextDumpCBRNE.txt","w","utf-8")
    browser = webdriver.Edge("C:/Users/Brett/Downloads/Edge/MicrosoftWebDriver.exe")
    timeout = -1
    for url in readFile():
        if url.strip() != "http://opencbrne.jrc.ec.europa.eu/page/7996" and timeout == -1:
            print url
            continue


        print url
        timeout = randint(7, 40)
        browser.get(url)
        time.sleep(timeout)
        
        name = None
       
        for a in browser.find_elements_by_xpath("//*[@id]"):
            if str(a.get_attribute("id")).strip() != "cbrn_aj_title" and \
             str(a.get_attribute("id")).strip() != "cbrn_aj_content":
                continue

            if str(a.get_attribute("id")).strip() == "cbrn_aj_title":
                name = a.text
                d[name] = None

            elif str(a.get_attribute("id")).strip() == "cbrn_aj_content":
                synonym = returnSynonym(a.text)
                d[name] = synonym
                dumpText(outhandle, name, a.text)
                
    pickle.dump(d,open("synonyms.pck","wb"))
    outhandle.close()   
    browser.quit
                
        


def processPages():
  
    #location = "http://opencbrne.jrc.ec.europa.eu/page/%d"
    location = "http://opencbrne.jrc.ec.europa.eu/page/0?fchar=%s"
    browser = webdriver.Edge("C:/Users/Brett/Downloads/Edge/MicrosoftWebDriver.exe")
    outhandle = open("CBRNEURLS.txt","w")
    for w in returnChars():
        url = location %(w)
        browser.get(url)
        time.sleep(10)
        for a in browser.find_elements_by_xpath("//*[@id]"):

            if str(a.get_attribute("id")).strip() != "cbrn_aj_index":
                continue
            
            for n in a.find_elements_by_xpath(".//a"):
                
            
                try:

                    #print n.text.encode('ascii', 'ignore').decode('ascii')
                    #print n.tag_name
                    #print n.get_attribute("id")
                    #print n.get_attribute("name")
                    outhandle.write(n.get_attribute("href"))
                    outhandle.write("\n")
            #print str(a.get_attribute("id")).strip() == "cbrn_aj_index"
        
        #if str(a.get_attribute("id")).strip() == "cbrn_aj_index":
        #    print a.text.encode('ascii', 'ignore').decode('ascii')
         #   print a.tag_name    
        
                except:
                    continue
    #print a.id
        #break
    browser.quit
    outhandle.close()


def extractSynonyms():
    d = {}
    locations = ["PlainTextDumpCBRNE.txt.2","PlainTextDumpCBRNE.txt.1","PlainTextDumpCBRNE.txt"]
    for location in locations:
        ihandle = codecs.open (location,"r","utf-8")
        text = ihandle.read()
        ihandle.close()

        records = text.split("End Record")
        for record in records:
            lines = record.split("\n")
            synonym = returnSynonym(lines[-2])
            if not synonym:
                continue
            d[lines[3].strip().lower()] = synonym.lower()
    for i,t in d.items():
        print i,"  ",t 
    pickle.dump(d,open("synonyms.pck","wb"))
        
extractSynonyms()

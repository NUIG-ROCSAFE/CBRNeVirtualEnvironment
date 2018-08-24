from flask import Flask
from flask import make_response
import ConfigParser, sys, os
import sqlite3

app = Flask(__name__)

global location
global soplocation
global sopPDFlocation


def ConfigSectionMap(section, Config):
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


def returnMessage(strText):
    print(strText)


def setGlobalVariables():
    global location
    global soplocation
    global indexName
    global sopPDFlocation

    inilocation = "main.ini"
    Config = ConfigParser.ConfigParser()
    Config.read(inilocation)

    section = "sqlite"
    keys = None

    try:
        keys = ConfigSectionMap(section, Config)
    except:
        print("Can't find ini file: %s" % (inilocation))
        exit()

    location = keys["dblocation"]
    soplocation = keys["soplocation"]
    sopPDFlocation = keys["soppdflocation"]

    if not os.path.isfile(location):
        strError = "File %s does not exist" % (location)
        returnMessage(strError)
        exit()

    if not os.path.isdir(soplocation):
        strError = "Directory %s does not exist" % (soplocation)
        returnMessage(strError)
        exit()

    if not os.path.isdir(sopPDFlocation):
        strError = "Directory %s does not exist" % (sopPDFlocation)
        returnMessage(strError)
        exit()


def returnLink(title):
    linkText = "View " + title + " PDF"
    print(title)
    # location ="\'file://C:/Users/Brett/Documents/NUIG/text/%s.%s\'" % (title,"txt")
    link_location = "\'http://127.0.0.1:5000/%s\'" % (title)
    link = "<a href=" + link_location + " target=\"_blank\">%s</a>"
    link = link % (linkText)
    return link


def returnRank():
    global location
    conn = sqlite3.connect(location)
    cur = conn.cursor()
    sql = '''SELECT SOP.Title, rank.rank, rank.date, rank.SearchTerms from rank,SOP where rank.sopid = SOP.id 
	and date in (select max(date) FROM Rank) order by rank.rank desc'''
    # sql+= "  order by rank.rank desc"
    cur.execute(sql)
    rows = cur.fetchall()
    print(rows)

    doc = "<html> \n"
    doc += "<head> <title> SOP Ranking </title> \n "

    # doc+= "<script type=\'text/javascript\'>"
    # doc+="function sleep(delay) { \n"
    # doc+="var start = new Date().getTime(); \n"
    # doc+="while (new Date().getTime() < start + delay); \n"
    # doc+="  } \n"
    # doc+=" </script> \n"

    doc += " <style> \n"
    doc += " table { \n"
    doc += " border-collapse: collapse; \n"
    doc += " width: 100%; \n"
    doc += " } \n"
    doc += "th, td { \n"
    doc += " text-align: left; \n"
    doc += " padding: 8px; \ncolor: #00075f;\n"
    doc += " } \n"
    doc += " tr:nth-child(even) {background: #ffffff} \n"
    doc += " tr:nth-child(odd) {background: #d9eff9} \n"
    doc += " th { \n"
    doc += " background: #3c8dbc; \n"
    doc += " color: white; \n"
    doc += " } \n"
    doc += " </style> \n"
    # doc+=" </head> \n"
    # onload='sleep(50000); location.reload();')
    doc += "</head> \n"
    doc += "<body> <table> \n"
    doc += "<tr>\n <th> Standard Operating Procedure Title</th>\n <th> Score </th>\n <th> Search Terms </th>\n <th> Date Computed </th>\n <th> Link </th>\n </tr>\n"

    for row in rows:
        link = returnLink(row[0])
        doc += "<tr>\n"
        doc = "%s\n<td>%s</td>\n<td>%s</td>\n<td>%s</td>\n<td>%s</td>\n<td>%s</td>" % (
            doc, row[0], row[1], row[3], row[2], link)
        doc += "</tr>\n"

    doc += "</table> "
    # doc+=" <Button onclick='location.reload()'> Refresh </Button> "
    doc += " </body> </html> "
    return doc


@app.route('/')
def returnSOPS():
    setGlobalVariables()
    return returnRank()


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def printText(path):
    global sopPDFlocation

    if "attack" not in path:
        return ""

    location = "%s%s.pdf" % (sopPDFlocation, path)
    inhandle = open(location, "rb")
    binary_pdf = inhandle.read()
    inhandle.close()

    response = make_response(binary_pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = \
        'inline; filename=%s.pdf' % 'path'
    return response


def main():
    # runs in port 5000 by default
    app.run()


if __name__ == "__main__":
    # runs in port 5000 by default
    main()

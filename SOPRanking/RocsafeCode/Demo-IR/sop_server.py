import sqlite3
import utils

from flask import Flask
from flask import make_response

app = Flask(__name__)


def return_link(title, pdf_loc):
    link_text = "View " + title + " PDF"
    print(title)
    link_location = "\'http://127.0.0.1:5000/%s\'" % (pdf_loc + title)
    link = "<a href=" + link_location + " target=\"_blank\">%s</a>" % link_text
    return link


def return_rank(db_loc, pdf_loc):
    conn = sqlite3.connect(db_loc)
    cur = conn.cursor()
    sql = '''SELECT SOP.Title, rank.rank, rank.date, rank.SearchTerms from rank,SOP where rank.sopid = SOP.id 
    and date in (select max(date) FROM Rank) order by rank.rank desc'''
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
    doc += "<tr>\n <th> Standard Operating Procedure Title</th>\n <th> Score </th>\n <th> Search Terms </th>\n " \
           "<th> Date Computed </th>\n <th> Link </th>\n </tr>\n"

    for row in rows:
        link = return_link(row[0], pdf_loc)
        doc += "<tr>\n"
        doc = "%s\n<td>%s</td>\n<td>%s</td>\n<td>%s</td>\n<td>%s</td>\n<td>%s</td>" % (
            doc, row[0], row[1], row[3], row[2], link)
        doc += "</tr>\n"

    doc += "</table> "
    # doc+=" <Button onclick='location.reload()'> Refresh </Button> "
    doc += " </body> </html> "
    return doc


@app.route('/')
def return_sops():
    db_conn, _, pdf_loc, _ = utils.get_config('main.ini')
    return return_rank(db_conn, pdf_loc)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def print_text(path):
    if "attack" not in path:
        return ""

    file_location = "%s.pdf" % path
    pdf_file = open(file_location, "rb")
    binary_pdf = pdf_file .read()
    pdf_file.close()

    response = make_response(binary_pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = \
        'inline; filename=%s.pdf' % 'path'
    return response


def main():
    # runs in port 5000 by default
    app.run()


if __name__ == '__main__':
    main()

import configparser
import os


def config_selection_map(section, config):
    config_dict = {}
    options = config.options(section)
    for option in options:
        try:
            config_dict[option] = config.get(section, option)
            if config_dict[option] == -1:
                print("skip: %s" % option)
        except Exception as e:
            print("exception on %s!" % option)
            print(e)
            config_dict[option] = None
    return config_dict


def get_config(ini_loc):
    """
    Reads config file 'main.ini' and returns config values
    Sample config file:
        [sqlite]
        dblocation: ./dbs/sops.db
        soplocation: ./text/
        sopPDFlocation: ./pdf/
        indexname: sops
    """

    config = configparser.ConfigParser()
    config.read(ini_loc)

    section = "sqlite"
    config_dict = None

    try:
        config_dict = config_selection_map(section, config)
    except configparser.NoSectionError:
        print("Can't find section \'%s\' file: %s" % (section, ini_loc))
        exit(-1)

    db_conn = config_dict["dblocation"]
    sop_location = config_dict["soplocation"]
    pdf_loc = config_dict["soppdflocation"]
    index_name = config_dict["indexname"]

    if not os.path.isfile(db_conn):
        db_err = "DB file: %s does not exist" % db_conn
        print(db_err)
        exit(-1)

    if not os.path.isdir(sop_location):
        sop_err = "SOP text file location: %s does not exist" % sop_location
        print(sop_err)
        exit(-1)

    if not os.path.isdir(pdf_loc):
        pdf_err = "Directory %s does not exist" % pdf_loc
        print (pdf_err)
        exit(-1)

    if not index_name:
        index_err = "Index name is not set in %s" % ini_loc
        print(index_err)
        exit(-1)

    return db_conn, sop_location, pdf_loc, index_name

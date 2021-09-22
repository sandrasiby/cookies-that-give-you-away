from extract_cookie_ids import extract_persistent_ids_from_dbs, extract_common_id_cookies
import pickle
import os

def extract_id_cookies(db1, db2):
    """ 
    Compares two databases and returns the id cookie domain, name
    pairs as a dict
    """
    print("Pulling cookies from db1")
    cookies_db1 = extract_persistent_ids_from_dbs([db1], num_days = 90)
    print("Pulling cookies from db2")
    cookies_db2 = extract_persistent_ids_from_dbs([db2], num_days = 90)
    print("Extracting common ids")
    id_cookies = extract_common_id_cookies([cookies_db1, cookies_db2])
    return id_cookies

if __name__=='__main__':
    
    db1 = '../data/crawl-data-us1.sqlite'
    db2 = '../data/crawl-data-us2.sqlite'

    #db1 = '../data/crawl-data-.sqlite'
    #db2 = '../data/crawl-data-cookies2.sqlite'
    id_cookies = extract_id_cookies(db1, db2)
    c_list = []
    for k, v in id_cookies.items():
        c_list += v
    #print(len(c_list), len(set(c_list)), len(id_cookies))
    pickle.dump(id_cookies, open(os.path.join(os.path.dirname(__file__),'../data/id_cookies_delim.p'),'wb'))

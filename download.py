import requests
import re
import sys
import os


def checkAndMkDir():
    curpath = os.getcwd()
    wpath = os.path.join(curpath, 'tdoc')
    if not os.path.exists(wpath) or os.path.isfile(wpath):
        os.mkdir(wpath)


def downloadOneFile(f_list, name):
    f_name = name + ".zip"
    url = f_list + f_name
    r = requests.get(url)
    #print "code:" + str(r.status_code)
    if r.status_code == 200:
        path = sys.path[0] + '/tdoc/' + f_name
        with open(path, 'wb') as code:
            code.write(r.content)
        return 0
    elif r.status_code == 404:
        return 1
    else:
        return 2


def readfilelist():
    name_lst = []
    with open('list.txt', 'r') as name:
        for ff_name in name.readlines():
            pattern = "R[\d]-[\d]{4,8}"
            rs = re.findall(pattern, ff_name)
            if len(rs):
                name_lst.append(rs[0])
            else:
                print "NO names found!"
    return name_lst


def main():
    prefix_url = 'http://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_92/Docs/'
    names = readfilelist()
    checkAndMkDir()
    for name in names:
        rs = downloadOneFile(prefix_url, name)
        if 0 == rs:
            print name + " downloaded!"
        elif 1 == rs:
            print("File Not found!")
        else:
            print("Error!")


if __name__ == "__main__":
    main()

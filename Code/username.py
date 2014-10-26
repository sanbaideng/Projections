#coding=utf8
'''
Created on 2014年10月26日

@author: Administrator
收集用户名称
'''
import urllib
import urllib2
from bs4 import BeautifulSoup
import MySQLdb
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def create_username(username):
    conn=None
    #assert isinstance(conn, MySQLdb.connection)
    try:
        conn=MySQLdb.connect(host="127.0.0.1",
                   user="rrrrr",
                   passwd="ssssss",
                   db="abc",
                   port=3306,charset='utf8')
        
        cur=conn.cursor()
        #cur.execute("select * from username")
        cur.execute("select id from username where username=%s",[username]);
        one=cur.fetchone()
        if one is None:
            print "入库："+str(username)
            cur.execute("insert into username (username,isused) values (%s,%s)",[username,0])
            conn.commit()
        else:
            print "已经存在"+username
        conn.close()
    except MySQLdb.Error,e:
        conn.rollback()
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
def getHtml(url):
    icount=0
    while icount<10:
            try:        
                html=urllib2.urlopen(url,timeout=5).read()
                return html
            except Exception,e:
                time.sleep(1)
                icount=icount+1
if __name__ == '__main__':    
    forums=["http://bbs.tianya.cn/list-free-1.shtml","http://bbs.tianya.cn/list-law-1.shtml","http://bbs.tianya.cn/list-university-1.shtml","http://bbs.tianya.cn/list-828-1.shtml","http://bbs.tianya.cn/list-develop-1.shtml","http://bbs.tianya.cn/list-837-1.shtml","http://bbs.tianya.cn/list-culture-1.shtml","http://bbs.tianya.cn/list-665-1.shtml","http://bbs.tianya.cn/list-feeling-1.shtml","http://bbs.tianya.cn/list-no11-1.shtml","http://bbs.tianya.cn/list-play-1.shtml","http://bbs.tianya.cn/list-no05-1.shtml","http://bbs.tianya.cn/list-no01-1.shtml","http://bbs.tianya.cn/list-books-1.shtml","http://bbs.tianya.cn/list-no16-1.shtml","http://bbs.tianya.cn/list-poem-1.shtml","http://bbs.tianya.cn/list-no02-1.shtml","http://bbs.tianya.cn/list-16-1.shtml","http://bbs.tianya.cn/list-house-1.shtml","http://bbs.tianya.cn/list-stocks-1.shtml","http://bbs.tianya.cn/list-no22-1.shtml","http://bbs.tianya.cn/list-no20-1.shtml","http://bbs.tianya.cn/list-enterprise-1.shtml","http://bbs.tianya.cn/list-cars-1.shtml","http://bbs.tianya.cn/list-itinfo-1.shtml","http://bbs.tianya.cn/list-516-1.shtml","http://bbs.tianya.cn/list-numtechnoloy-1.shtml","http://bbs.tianya.cn/list-no06-1.shtml","http://bbs.tianya.cn/list-news-1.shtml","http://bbs.tianya.cn/list-worldlook-1.shtml","http://bbs.tianya.cn/list-333-1.shtml","http://bbs.tianya.cn/list-1089-1.shtml","http://bbs.tianya.cn/list-fans-1.shtml","http://bbs.tianya.cn/list-basketball-1.shtml","http://bbs.tianya.cn/list-travel-1.shtml","http://bbs.tianya.cn/list-1138-1.shtml","http://bbs.tianya.cn/list-96-1.shtml","http://bbs.tianya.cn/list-768-1.shtml","http://bbs.tianya.cn/list-98-1.shtml","http://bbs.tianya.cn/list-outseachina-1.shtml","http://bbs.tianya.cn/list-100-1.shtml","http://bbs.tianya.cn/list-spirit-1.shtml","http://bbs.tianya.cn/list-934-1.shtml","http://bbs.tianya.cn/list-motss-1.shtml","http://bbs.tianya.cn/list-water-1.shtml","http://bbs.tianya.cn/list-funinfo-1.shtml","http://bbs.tianya.cn/list-1095-1.shtml","http://bbs.tianya.cn/list-tianyamyself-1.shtml","http://bbs.tianya.cn/list-filmtv-1.shtml","http://bbs.tianya.cn/list-music-1.shtml","http://bbs.tianya.cn/list-14-1.shtml","http://bbs.tianya.cn/list-no04-1.shtml","http://bbs.tianya.cn/list-english-1.shtml","http://bbs.tianya.cn/list-lookout-1.shtml","http://bbs.tianya.cn/list-1013-1.shtml","http://bbs.tianya.cn/list-137-1.shtml","http://bbs.tianya.cn/list-810-1.shtml","http://bbs.tianya.cn/list-24-1.shtml","http://bbs.tianya.cn/list-409-1.shtml","http://bbs.tianya.cn/list-172-1.shtml","http://bbs.tianya.cn/list-410-1.shtml","http://bbs.tianya.cn/list-168-1.shtml","http://bbs.tianya.cn/list-174-1.shtml","http://bbs.tianya.cn/list-31-1.shtml","http://bbs.tianya.cn/list-411-1.shtml","http://bbs.tianya.cn/list-666-1.shtml","http://bbs.tianya.cn/list-113-1.shtml","http://bbs.tianya.cn/list-780-1.shtml","http://bbs.tianya.cn/list-210-1.shtml","http://bbs.tianya.cn/list-420-1.shtml","http://bbs.tianya.cn/list-943-1.shtml","http://bbs.tianya.cn/list-647-1.shtml","http://bbs.tianya.cn/list-157-1.shtml","http://bbs.tianya.cn/list-help-1.shtml","http://bbs.tianya.cn/list-972-1.shtml","http://bbs.tianya.cn/list-838-1.shtml","http://bbs.tianya.cn/list-22-1.shtml","http://bbs.tianya.cn/list-consumer-1.shtml","http://bbs.tianya.cn/list-1131-1.shtml","http://bbs.tianya.cn/list-67-1.shtml","http://bbs.tianya.cn/list-106-1.shtml","http://bbs.tianya.cn/list-66-1.shtml","http://bbs.tianya.cn/list-241-1.shtml","http://bbs.tianya.cn/list-139-1.shtml","http://bbs.tianya.cn/list-160-1.shtml","http://bbs.tianya.cn/list-187-1.shtml","http://bbs.tianya.cn/list-486-1.shtml","http://bbs.tianya.cn/list-218-1.shtml","http://bbs.tianya.cn/list-364-1.shtml","http://bbs.tianya.cn/list-390-1.shtml","http://bbs.tianya.cn/list-901-1.shtml","http://bbs.tianya.cn/list-1005-1.shtml","http://bbs.tianya.cn/list-shortmessage-1.shtml","http://bbs.tianya.cn/list-no124-1.shtml","http://bbs.tianya.cn/list-23-1.shtml","http://bbs.tianya.cn/list-no17-1.shtml","http://bbs.tianya.cn/list-169-1.shtml","http://bbs.tianya.cn/list-762-1.shtml","http://bbs.tianya.cn/list-150-1.shtml","http://bbs.tianya.cn/list-737-1.shtml","http://bbs.tianya.cn/list-911-1.shtml","http://bbs.tianya.cn/list-738-1.shtml","http://bbs.tianya.cn/list-912-1.shtml","http://bbs.tianya.cn/list-767-1.shtml","http://bbs.tianya.cn/list-201-1.shtml","http://bbs.tianya.cn/list-49-1.shtml","http://bbs.tianya.cn/list-149-1.shtml","http://bbs.tianya.cn/list-75-1.shtml","http://bbs.tianya.cn/list-151-1.shtml","http://bbs.tianya.cn/list-805-1.shtml","http://bbs.tianya.cn/list-358-1.shtml","http://bbs.tianya.cn/list-43-1.shtml","http://bbs.tianya.cn/list-766-1.shtml","http://bbs.tianya.cn/list-female-1.shtml","http://bbs.tianya.cn/list-99-1.shtml","http://bbs.tianya.cn/list-oldgirl-1.shtml","http://bbs.tianya.cn/list-166-1.shtml","http://bbs.tianya.cn/list-363-1.shtml","http://bbs.tianya.cn/list-84-1.shtml","http://bbs.tianya.cn/list-607-1.shtml","http://bbs.tianya.cn/list-1090-1.shtml","http://bbs.tianya.cn/list-108-1.shtml","http://bbs.tianya.cn/list-924-1.shtml","http://bbs.tianya.cn/list-71-1.shtml","http://bbs.tianya.cn/list-524-1.shtml","http://bbs.tianya.cn/list-105-1.shtml","http://bbs.tianya.cn/list-177-1.shtml","http://bbs.tianya.cn/list-3d-1.shtml","http://bbs.tianya.cn/list-funstribe-1.shtml","http://bbs.tianya.cn/list-tianyaphoto-1.shtml","http://bbs.tianya.cn/list-indepfilm-1.shtml","http://bbs.tianya.cn/list-384-1.shtml","http://bbs.tianya.cn/list-200-1.shtml","http://bbs.tianya.cn/list-38-1.shtml","http://bbs.tianya.cn/list-138-1.shtml","http://bbs.tianya.cn/list-705-1.shtml","http://bbs.tianya.cn/list-641-1.shtml","http://bbs.tianya.cn/list-no100-1.shtml","http://bbs.tianya.cn/list-967-1.shtml","http://bbs.tianya.cn/list-20-1.shtml","http://bbs.tianya.cn/list-107-1.shtml","http://bbs.tianya.cn/list-103-1.shtml","http://bbs.tianya.cn/list-29-1.shtml","http://bbs.tianya.cn/list-131-1.shtml","http://bbs.tianya.cn/list-192-1.shtml","http://bbs.tianya.cn/list-944-1.shtml","http://bbs.tianya.cn/list-743-1.shtml","http://bbs.tianya.cn/list-sport-1.shtml","http://bbs.tianya.cn/list-fansunion-1.shtml","http://bbs.tianya.cn/list-it-1.shtml","http://bbs.tianya.cn/list-numtechnoloy-1.shtml","http://bbs.tianya.cn/list-343-1.shtml","http://bbs.tianya.cn/list-102-1.shtml","http://bbs.tianya.cn/list-243-1.shtml","http://bbs.tianya.cn/list-185-1.shtml","http://bbs.tianya.cn/list-952-1.shtml","http://bbs.tianya.cn/list-1021-1.shtml","http://bbs.tianya.cn/list-923-1.shtml","http://bbs.tianya.cn/list-927-1.shtml","http://bbs.tianya.cn/list-778-1.shtml","http://bbs.tianya.cn/list-883-1.shtml","http://bbs.tianya.cn/list-1123-1.shtml","http://bbs.tianya.cn/list-1135-1.shtml","http://bbs.tianya.cn/list-1144-1.shtml","http://bbs.tianya.cn/list-985-1.shtml","http://bbs.tianya.cn/list-991-1.shtml","http://bbs.tianya.cn/list-986-1.shtml","http://bbs.tianya.cn/list-1030-1.shtml","http://bbs.tianya.cn/list-998-1.shtml","http://bbs.tianya.cn/list-1004-1.shtml","http://bbs.tianya.cn/list-1035-1.shtml","http://bbs.tianya.cn/list-1097-1.shtml","http://bbs.tianya.cn/list-1105-1.shtml","http://bbs.tianya.cn/list-1122-1.shtml","http://bbs.tianya.cn/list-1127-1.shtml","http://bbs.tianya.cn/list-1133-1.shtml","http://bbs.tianya.cn/list-1140-1.shtml","http://bbs.tianya.cn/list-1143-1.shtml"]
    icount=0
    for furl in forums:        
        listHtml=getHtml(furl)
        while True:
            soup=BeautifulSoup(listHtml)
            lstAuthors= soup.find_all("a", attrs={"class":"author"})
            for lstAuthor in lstAuthors:                
                create_username(lstAuthor.text)
                icount=icount+1
            nextUrl=soup.find("a", attrs={"rel":"nofollow"},text="下一页")["href"]
            if nextUrl is not None:
                nextUrl="http://bbs.tianya.cn"+nextUrl
                print "开始采集："+nextUrl
                listHtml=getHtml(nextUrl)
            else:
                break
        print furl+"已经处理完成"

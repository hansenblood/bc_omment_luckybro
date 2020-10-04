import requests
import random

def getHTMLurl(url,kvs):
    try:
        r = requests.get(url,headers= kvs)
        print('connect_code:')
        print(r.status_code)
        r.encoding = r.apparent_encoding
        return r.json()
    except:
        print('false')

def uPeople(html_js,infoLists):
    #去重
    kunum = 0
    cap = {}
    for peo in html_js['data']['replies']:
        key = peo['member']['mid']
        val = str(kunum)
        cap.update({key:val})
        kunum = kunum + 1
    del cap['345236483']#排除up
#    print(cap)
    cap_2 = {v:k for k,v in cap.items()}
#    print(cap_2)
#列表变为整数
    unum = random.sample(cap_2.keys(),1)
    unum2 =int( ''.join(unum))
    uinfo = html_js['data']['replies'][unum2]
    infoLists.append(uinfo['member']['mid'])
    infoLists.append(uinfo['member']['uname'])
    infoLists.append(uinfo['content']['message'])
    infoLists.append(str('https://space.bilibili.com/'+uinfo['member']['mid']))

def main():
    url = 'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=1&oid=626859816&sort=2&_=1599540944670'
    # 请求头信息
    kv = {
        'Host': 'api.bilibili.com',
    }
    html = getHTMLurl(url,kv)
    infoList = []
    uPeople(html,infoList)
    print('中奖者个人id:  ' +infoList[0]+'\n'
          '昵称:          ' + infoList[1] + '\n'
          '评论:          ' + infoList[2] + '\n'
          '个人空间:      ' + infoList[3] + '\n'
         )

if __name__ == '__main__':
    main()
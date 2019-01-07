from bs4 import BeautifulSoup as BS
from requests import get

def OpenHtml(param):
    html = get(param)
    bs_obj = BS(html.content, 'html.parser')
    return bs_obj

def LastNum(bs_obj):
    num = bs_obj.find(class_ = "last near")['href'].split('=')[-1]
    return num

def FindMoves(param, num):
    for page in range(1,int(num)):
        bs_obj_page = OpenHtml(param +"&p=" + str(page))
        all_son = bs_obj_page.find_all(class_="item")
        IfMoves(all_son)

def IfMoves(all_son):
    for son in all_son:
        if son.find(class_="cate").get_text() != "人物":
            print(son.find(class_="name"))

if __name__ == "__main__":
    param = "http://www.taiyingshi.com/search/?kw=a"
    FindMoves(param, LastNum(OpenHtml(param)))
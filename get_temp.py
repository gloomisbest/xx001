#coding:UTF-8
import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def change_weekday(date):
    week_jp = ['(日)', '(月)', '(火)', '(水)', '(木)', '(金)', '(土)']
    week_cn = ['星期天', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
    a = date[-3:]
    b = week_jp.index(a)
    c = week_cn[b]
    date_ch = date.replace(a,c)
    return date_ch

url = 'https://weather.yahoo.co.jp/weather/jp/17/5610.html'
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
req = urllib2.Request(url, headers=head)
response = urllib2.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, 'lxml')
soup_texts = soup.find('div', class_='forecastCity')
#print soup_texts
date = soup_texts.find('div',class_='date today').h3.getText()
date_c = change_weekday(date)
#print date_c
weather = soup_texts.find('dd',class_='txt').getText()
temp_h = soup_texts.find('span',class_='high').em.getText()
temp_l = soup_texts.find('span',class_='low').em.getText()
text = '早上好！今天是%s,天气%s,最高温度%s摄氏度,最低温度%s摄氏度'%(date_c, weather, temp_h, temp_l)
print text

url = u'http://tts.baidu.com/text2audio?idx=1&tex={0}&cuid=baidu_speech_' \
      u'demo&cod=2&lan=zh&ctp=1&pdt=1&spd=4&per=0&vol=5&pit=5'.format(text)

print url



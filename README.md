
# **Python Jingjue 荊訣**

## **1. 導讀**︰
北京大學收藏的西漢竹書內有《荊訣》一篇，共記載了十六卦，卦名以干支命名，包括甲、乙、丙、丁、戊、己、壬、癸、子、丑、寅、卯、辰、巳、午、未。《

荊訣》內記載︰"鑽龜告筮，不如荊訣。若陰若陽，若短若長。所蔔毋方，所占毋良，必察以明。卅筭以蔔其事，若吉若凶，唯筭所從。左手持書，右手操筭，必東面。用卅筭分，以為三分，其上分橫，中分從縱，下分橫。四四而除之，不盈者勿除。"卅筭指三十根算籌，把算籌分成上、中、下三份，每份除四取餘數，上中下之餘數值集合就成卦。本系統引用卦辭文字內容參考自 子居著的〈北大簡《荊訣》解析〉(http://xianqin.byethost10.com/2015/12/28/309)。

"Jingjue" is an ancient chinese divination method which is similar as Ichingshifa found from a bunch of bamboo slips relics from Xihan dynasty collected by Peking University, consisting of sixteen Gua("卦"). Similar as ichingshifa, Jingjue is about 30 stalks to do divination. The stalks will be seperated into 3 bunches and the remainders of these three bunches taken out to form Gua("卦").

![alt text](https://github.com/kentang2017/jingjue/blob/master/data/pic.png?raw=true)


## **2. 安裝套件**

```python
	pip install jingjue
```

## **3. 起課方式**
```python
	from jingjue import jingjue
	jingjue.qigua()
	
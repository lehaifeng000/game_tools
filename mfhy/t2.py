# 种花、一键操作、施肥、收花

import requests
import math
import threading
import time


from  concurrent.futures import ThreadPoolExecutor

# 会话id，每隔一段时间失效
sid="254402_f09461313a3a6c0652fe"

huapen_ids=["6b9248de75","c202a7edad","6eae7f0fd4","d8772d5842","e5603823c3","dc5dabf6b1","ab9b6b6313","52e25821ff","8ae0da7ddf","9be5d687e4","b060ffc85e","ac05124225","b15ed48d85","b76957dc32"]
# huapen_ids=[
#     # "6b9248de75","c202a7edad","6eae7f0fd4","d8772d5842","e5603823c3","dc5dabf6b1","ab9b6b6313","52e25821ff","8ae0da7ddf","9be5d687e4","b060ffc85e","ac05124225","b15ed48d85",
#     "b76957dc32"
#     ]

shuipen_ids=["cf0271f4b6","46c12fe2fc","6a9f39d967","8e58e23c80","b7dc6c311e","70da7f669a","a61fd41593"]
huafei_list=[
    [10,"2y80538cb6"],
    [3,"83i75384ov"],
    [1,"xcz5538f3k"],
    [0.5,"8131538r4p"]
]

# 时间削减
time_sub=0.116


# 种子记录
'''
茑萝松 rd98755xgh    13小时48分
'''
seed_dict={
    "rd98755xgh":{
        "name":"茑萝松",
        "huapen":True,
        "time":13.8
    },
    "3zd4855vju":{
        "name":"半边莲（水生）",
        "huapen":False,
        "time":20
    },
    "au99075c2o":{
        "name":"星星之火（水生）",
        "huapen":False,
        "time":5
    },
    "zhq83759ld":{
        "name":"心花怒放",
        "huapen":True,
        "time":5.84
    },
    "f4e53376n9":{
       "name":"萍逢草(水生)",
        "huapen":False,
        "time":2 
    },
    "44r7155qrr":{
        "name":"绣球",
        "huapen":True,
        "time":14.1 
    },
    "3io4755b55":{
        "name":"堇花兰",
        "huapen":True,
        "time":16
    }
}

headers={
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/113.0.0.0"
}

def caozuo():
    res=requests.get("http://47.108.60.249:9998/mfhy/pot/okdooper.asp?sid="+sid, headers=headers)
    pass

# 一键播种
def yjbz(seedid):
    res=requests.get("http://47.108.60.249:9998/mfhy/pot/prepOkSeed.asp?sid="+sid+"&seedId="+seed_id, headers=headers)
    res2=requests.get("http://47.108.60.249:9998/mfhy/pot/okSow.asp?sid="+sid, headers=headers)

# 施肥
def sf(potid,hfid='8131538r4p'):
    s=time.time()
    res=requests.get("http://47.108.60.249:9998/mfhy/pot/urgeProd.asp?sid="+sid+"&potId="+potid+"&toolId="+hfid, headers=headers)
    print(time.time()-s)
    # print("1")
    
    pass

def sf_tx(potid,cost):
    t=cost
    while t>0:
        if t>=10:
            sf(potid,huafei_list[0][1])
            t-=10
            pass
        elif t>=3:
            sf(potid,huafei_list[1][1])
            t-=3
            pass
        elif t>=1:
            sf(potid,huafei_list[2][1])
            t-=1
            pass
        else:
            sf(potid,huafei_list[3][1])
            t-=0.5
            pass

epoch=100

seed_id="3io4755b55"
huafei_tanxin=True
sf_time=seed_dict[seed_id]["time"]*(1-time_sub)
sf_num= math.ceil(sf_time/0.5)
pot_list= huapen_ids if seed_dict[seed_id]["huapen"] else shuipen_ids
for ep in range(epoch):
    # 播种
    yjbz(seed_id)
    # 一键操作
    caozuo()
    # 施肥
    for potid in pot_list:
        # with ThreadPoolExecutor(max_workers=sf_num) as executor:
        #     executor.map(sf,potid)
        # t_list=[]
        start=time.time()
        if huafei_tanxin:
            sf_tx(potid,sf_time)
        else:
            # 小化肥
            for hfn in range(sf_num):
                sf(potid)

        print(time.time()-start)
        pass
        # for ti in t_list:
        #     ti.join()
        
    # 一键操作收获

    caozuo()
    print(ep)


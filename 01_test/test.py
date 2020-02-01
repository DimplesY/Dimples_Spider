import requests
import json
import datetime


city = ["北京","上海","深圳","重庆"]
citys = ["北京市","上海市","深圳市","重庆市"]

def getProvince():

    Province = input("请输入需要查询的省：")
    while Province=="":
        Province = input("请输入需要查询的省：")

    if len(Province)==2 and Province not in city:
        return Province+"省"

    if Province in city and len(Province)==2:
        return Province+"市"


def getData():
    baseUrl = "https://lab.isaaclin.cn/nCoV/api/area"
    province = getProvince()
    payload = {"latest":1,"province":province}

    req = requests.get(baseUrl,params=payload)
    return json.loads(req.content.decode())["results"][0],json.loads(req.content.decode())["results"][0]["cities"],province

def main():
    dataP,dataC,province = getData()
    upTime = str(dataP["updateTime"])[:10]

    print("=====最新数据=====")
    # print("更新时间:",datetime.datetime.utcfromtimestamp(int(upTime)).strftime("%Y-%m-%d %H:%M:%S"))
    print("查询地点:",dataP["provinceName"])
    print("确诊人数:",dataP["confirmedCount"])
    print("治愈人数:",dataP["curedCount"])
    print("死亡人数:",dataP["deadCount"])
    if province not in citys:
        ct = input("请输入该省份具体城市：")
        for i in range(len(dataC)):
            if dataC[i]["cityName"] == ct:
                print(ct+"市,最新情况如下：")
                print("确诊人数:", dataC[i]["confirmedCount"])
                print("治愈人数:", dataC[i]["curedCount"])
                print("死亡人数:", dataC[i]["deadCount"])


if __name__ == '__main__':
    main()
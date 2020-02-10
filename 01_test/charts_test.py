import requests
import json
from pyecharts import options as opts
from pyecharts.charts import Map

# 腾讯数据源
url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
res = json.loads(requests.get(url).json()["data"])
datas = res["areaTree"][0]["children"]
# 全国数据做副标题
china_total = "确诊:{} 疑似:{} 治愈:{} 死亡:{} 更新日期:{}".format(res["chinaTotal"]["confirm"],
                                                       res["chinaTotal"]["suspect"], res["chinaTotal"]["heal"],
                                                       res["chinaTotal"]["dead"], res["lastUpdateTime"])
provinces = []
confirm_value = []

# 遍历获取各省份数据
for data in datas:
    provinces.append(data["name"])
    confirm_value.append(data["total"]["confirm"])

# 链式调用
cmap = (
    Map(init_opts=opts.InitOpts(width="1000px", height="700px", page_title="新型冠状病毒疫情地图"))

    # 在地图中插入数据，使用中国地图，隐藏标记
    .add("确诊", [list(z) for z in zip(provinces, confirm_value)], "china", is_map_symbol_show=False)

    # 设置坐标属性，显示省份名
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=True)
    )

    # 设置全局属性
    .set_global_opts(
        # 分段型数据，自定义分段
        visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=[
            {"min": 1000, "color": "#70161d"},
            {"min": 500, "max": 1000, "color": "#cb2a2f"},
            {"min": 100, "max": 500, "color": "#e55a4e"},
            {"min": 10, "max": 100, "color": "#f59e83"},
            {"min": 1, "max": 10, "color": "#fdebcf"}
        ]),
        # 标题
        title_opts=opts.TitleOpts(title="全国新型冠状病毒疫情地图", subtitle=china_total, pos_left="center", pos_top="10px"),
        # 不显示图例
        legend_opts=opts.LegendOpts(is_show=False),
        # 提示框
        tooltip_opts=opts.TooltipOpts(trigger_on="click", formatter='省份:{b}<br/>{a}:{c}')
    )
)

# 在 html 中渲染图表
cmap.render()
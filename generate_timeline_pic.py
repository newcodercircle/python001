import numpy as np
import pandas as pd
from pyecharts.charts import Bar, Timeline
from pyecharts import options as opt

# 载入数据
data = pd.read_csv("./分省月度数据.csv", encoding="gbk")
# 清洗数据
data.dropna(axis=1, how="all", inplace=True)
data.fillna(value=0, inplace=True)
data.set_index("地区", inplace=True)


colors = [
    "#000075",
    "#a9a9a9",
    "#ffffff",
    "#000000",
    "#037ef3",
    "#f85a40",
    "#00c16e",
    "#7552cc",
    "#0cb9c1",
    "#f48924",
    "#ffc845",
    "#e6194B",
    "#3cb44b",
    "#ffe119",
    "#4363d8",
    "#f58231",
    "#911eb4",
    "#42d4f4",
    "#52565e",
    "#caccd1",
    "#49a942",
    "#f032e6",
    "#bfef45",
    "#fabed4",
    "#469990",
    "#dcbeff",
    "#9A6324",
    "#fffac8",
    "#800000",
    "#aaffc3",
    "#808000",
    "#ffd8b1",
]

timeline = Timeline(init_opts=opt.InitOpts(page_title="2003-2023房地产施工面积趋势变化图"))
# 画图
for c in data.columns[::-1]:
    data_column = data[[c]]
    data_column.sort_values(by=c, inplace=True)
    x_data = data_column.index.values.tolist()
    y_data = data_column[c].values.tolist()
    y_data_items = [
        opt.BarItem(
            name=x_data[i],
            value=y_data[i],
            itemstyle_opts=opt.ItemStyleOpts(color=colors[i]),
        )
        for i in range(len(y_data))
    ]
    bar = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis(
            series_name=c,
            y_axis=y_data_items,
            label_opts=opt.LabelOpts(position="right"),
        )
        .reversal_axis()
    )
    timeline.add(bar, time_point=c)

timeline.add_schema(is_auto_play=True, play_interval=1000)
timeline.render("result.html")

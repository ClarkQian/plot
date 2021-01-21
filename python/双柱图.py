import matplotlib.pyplot as plt
import matplotlib
# 设置中文字体和负号正常显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

label_list = ['中国', '印度尼西亚', '越南', '印度','美国', "德国"]    # 横坐标刻度显示值
num_list1 = [79.83, 2.84, 1.57, 18.56,13.28, 2.9]      # 纵坐标值1
num_list2 = [81.67, 3.41, 2.07, 18.62,11.34, 2.3]      # 纵坐标值2
x = range(len(num_list1))
"""
绘制条形图
left:长条形中点横坐标
height:长条形高度
width:长条形宽度，默认值0.8
label:为后面设置legend准备
"""
rects1 = plt.bar(left=x, height=num_list1, width=0.4, alpha=0.7, color='#b2b2ff', label="2018年煤炭消费总量")
rects2 = plt.bar(left=[i + 0.4 for i in x], height=num_list2, width=0.4, color='#f4b183',alpha=0.8, label="2019年煤炭消费总量")
plt.ylim(0, 90)     # y轴取值范围
# plt.ylabel("数量")
"""
设置x轴刻度显示值
参数一：中点坐标
参数二：显示值
"""
plt.xticks([index + 0.2 for index in x], label_list)
# plt.xlabel("年份")
# plt.title("某某公司")
plt.legend()     # 设置题注
# 编辑文本
for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
plt.savefig('res2.png')
plt.show()

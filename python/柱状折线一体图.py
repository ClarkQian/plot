# # -*- coding:utf-8 -*-
# import matplotlib
# import matplotlib.pyplot as plt
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
# # 构建数据
# x = [x_ for x_ in range(2009, 2020)]
# y = [480,505,515,525,535,545,545,555,565,575,580]
# # 绘图
# plt.bar(x=x, height=y, label='书库大全', color='steelblue', alpha=0.8)
# # 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
# # for x1, yy in zip(x, y):
# #     plt.text(x1, yy + 1, str(yy), ha='center', va='bottom', fontsize=20, rotation=0)
# # 设置标题
# # plt.title("80小说网活跃度")
# # 为两条坐标轴设置名称
# plt.xlabel("年份")
# plt.ylabel("一次性能源消费量/EJ")
#
#
# # 显示图例
# plt.legend()
# # 画折线图
# # x_ = [None,460,]
# plt.plot(x, y, "r", ms=10, label="消费量增速")
# plt.xticks(rotation=45)
# plt.legend(loc="upper left")
# plt.savefig("a.jpg")
# plt.show()


#python 画柱状图折线图
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
from matplotlib.font_manager import FontProperties
# font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
a = [480,505,515,525,535,545,545,555,565,575,580]
# a=[1228.3,3.38,63.8,0.07,0.16,6.74,1896.18]  #数据
# b=[0.12,-12.44,1.82,16.67,6.67,-6.52,4.04]
b=[4.5,2.4,1.3,2.0,0.9,0.7,1.3,1.8,3.0,1.3]
# l=[i for i in range(11)]
l_a = [x for x in range(2009,2020)]
l_b = [x for x in range(2010,2020)]
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

fmt='%.0f%%'
yticks = mtick.FormatStrFormatter(fmt)  #设置百分比形式的坐标轴

# lx=[u'粮食',u'棉花',u'油料',u'麻类',u'糖料',u'烤烟',u'蔬菜']
lx = ["%s年"%x for x in range(2009,2020)]


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.bar(l_a,a,alpha = 0.3, color = 'blue',width=0.3,label=u'一次能源消费量')
ax1.legend(loc=2,fontsize=10)
ax1.set_ylim([0,650])
ax1.set_ylabel("一次能源消费量/EJ")
# lines = ax1.plot(l_b, b,'or-',label=u'消费量增速');

ax2 = ax1.twinx()
plt.plot(l_b, b,'or-',label=u'消费量增速');
ax2.yaxis.set_major_formatter(yticks)

ax2.legend(loc="upper right",fontsize=9)
ax2.set_ylim([0,6]);
ax2.set_ylabel('消费量增速');
# plt.legend(prop={'family':'SimHei','size':8})  #设置中文



# plt.legend(prop={'family':'SimHei','size':8},loc="upper left")
# ax1 = fig.add_subplot(111)
# lines = ax1.plot(l_b, b,'or-',label=u'消费量增速');
# ax1.yaxis.set_major_formatter(yticks)
# # for i,(_x,_y) in enumerate(zip(l,b)):
# #     plt.text(_x,_y,b[i],color='black',fontsize=10,)  #将数值显示在图形上
# # print(ax1.lines.remove())
#
#
# ax1.legend(loc=2)
# ax1.set_ylim([0,6]);
# ax1.set_ylabel('消费量增速');
# plt.legend(prop={'family':'SimHei','size':8})  #设置中文
#
# ax2 = ax1.twinx() # this is the important function
# plt.bar(l_a,a,alpha=0.3,color='blue',width=0.3,label=u'一次能源消费量')
# ax2.legend(loc=2)
# ax2.set_ylim([0, 650])  #设置y轴取值范围
# ax2.set_ylabel('一次能源消费量/EJ');
# # plt.legend(prop={'family':'SimHei','size':8},loc="upper left")

#绑定底脚坐标
plt.xticks(l_a,lx)
plt.savefig("res.png")
plt.show()

# fig = plt.figure()
# ax2 = fig.add_subplot(111)
# ax1 = ax2.twinx() # this is the important function
# ax2.plot(l, b,'or-',label=u'消费量增速');
# ax2.yaxis.set_major_formatter(yticks)
# for i,(_x,_y) in enumerate(zip(l,b)):
#     plt.text(_x,_y,b[i],color='black',fontsize=10,)  #将数值显示在图形上
# # ax2.legend(loc=2)
# ax1.set_ylim([0, 6]);
# ax1.set_ylabel('增长率');
# # plt.legend(prop={'family':'SimHei','size':8})  #设置中文
#
# # ax2 = ax1.twinx() # this is the important function
# plt.bar(l,a,alpha=0.3,color='blue',label=u'一次能源消费量')
# # ax1.legend(loc=2)
# #add later
# # ax1.legend(loc="best")
# # ax2.legend(loc="best")
# # ax1.set_ylim([0, 600])  #设置y轴取值范围
# # plt.legend(prop={'family':'SimHei','size':8},loc="upper left")
# # plt.xticks(l,lx)
# plt.xlabel("年份")
# plt.show()

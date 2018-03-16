# -*- coding: utf-8 -*-

# @Author  : Skye
# @Time    : 2018/1/9 10:39
# @desc    :

import requests
import webbrowser
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def open_webbrowser(question):
    webbrowser.open('https://baidu.com/s?wd=' + question)




def output(choices, counts):
    counts = list(map(int, counts))
    #print(choices, counts)

    # 最可能的答案
    index_max = counts.index(max(counts))

    # 最不可能的答案
    index_min = counts.index(min(counts))

    if index_max == index_min:
        print("\033[1;31m此方法失效！\033[0m")
        return

    for i in range(len(choices)):
        if i == index_max:
            # 绿色为计数最高的答案
            print("\033[1;32m{0:^10} {1:^10}\033[0m".format(choices[i], counts[i]))
        elif i == index_min:
            # 红色为计数最低的答案
            print("\033[0;31m{0:^10}{1:^10}\033[0m".format(choices[i], counts[i]))
        else:
            print("{0:^10} {1:^10}".format(choices[i], counts[i]))


def run_algorithm(al_num, question, choices):
    if al_num == 0:
        open_webbrowser(question)
    elif al_num == 1:
        open_webbrowser_count(question, choices)
    elif al_num == 2:
        count_base(question, choices)

if __name__ == '__main__':
    question = '新装修的房子通常哪种化学物质含量会比较高?'
    choices = ['甲醛', '苯', '甲醇']
    run_algorithm(1, question, choices)



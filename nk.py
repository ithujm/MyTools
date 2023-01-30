# -*- coding = utf-8 -*-
# @Time: 2023/1/31 1:26
# @Author:hjm
# @File：nk.py
# @Software: PyCharm

import sys


def func(s):
    s_lst = s.split()
    num = s_lst[-1]
    s_txt = s_lst[0].split("\\")[-1][-16:]
    return "{} {}".format(s_txt, num)


def run(lines):
    tmp = []
    tmp_d = {}
    for line in lines:
        txt = func(line)
        if txt not in tmp:
            tmp.append(txt)
            tmp_d[txt] = 1
        else:
            tmp_d[txt] += 1
    for txt in tmp[-8:]:
        print("{} {}".format(txt, tmp_d[txt]))


if __name__ == '__main__':
    lines = sys.stdin.readlines()

    run(lines)

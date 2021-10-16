# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ========================================================
# @Author: Ryuchen
# @Time: 2021/05/06-10:35
# @Site: https://ryuchen.github.io
# @Contact: chenhaom1993@hotmail.com
# @Copyright: Copyright (C) 2019-2020 NER.
# ========================================================
"""
...
DocString Here
...
"""
import os


def merge_corpus():
    current_path = os.getcwd()
    g = os.walk(current_path)

    corpus = []

    for path, dir_list, file_list in g:
        for file_name in file_list:
            if ".txt" in file_name:
                corpus.append(os.path.join(path, file_name))

    contents = ""
    for item in corpus:
        with open(item, "r") as obj:
            lines = obj.readlines()
            for line in lines:
                if line != '\n':
                    line = line.strip('\n')
                    contents += line + " "

    contents = contents.split(" ")

    lines = []
    for item in contents:
        if item != "/O":
            lines.append(item)

    with open(os.path.join(current_path, "data.csv"), "w") as obj:
        for item in lines:
            if len(item) >= 1:
                if item == "。/O":
                    obj.write(f'{item.replace("/", " ")}\n\n')
                elif item == "/ O":
                    obj.write(f'{item}\n')
                else:
                    obj.write(f'{item.replace("/", " ")}\n')


if __name__ == '__main__':
    merge_corpus()

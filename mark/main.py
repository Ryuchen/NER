#!/usr/bin/python
# -*- coding: utf-8 -*-
# ===================================================================================
# File Name      : main.py
# Author         : chenlianghua
# Modified Time  : 2021/4/3
# Description    : put you description here
# ===================================================================================
import os
import jieba
import jieba.posseg as pseg

try:
    jieba.enable_paddle()
except Exception as e:
    print(e)


def do_jieba(file_path):
    tag_map = {
        'nr': 'PER',
        'ns': 'LOC',
        'nt': 'ORG',
        't': 'TIME'
    }

    output_lines = []

    print('start======={0}======='.format(file_path))
    with open(file_path) as file_reader:
        for line in file_reader:
            line = line.strip()
            if not line:
                continue
            print("==> input: ", line)
            jieba_output = pseg.cut(line)

            my_output = []
            for word, flag in jieba_output:
                for i, char in enumerate(word):
                    if flag not in tag_map:
                        my_output.append('{0}/O'.format(char))
                    else:
                        if i == 0:
                            my_output.append('{0}/B-{1}'.format(char, tag_map.get(flag)))
                        else:
                            my_output.append('{0}/I-{1}'.format(char, tag_map.get(flag)))

            print("==> output: ")
            print(' '.join(my_output))
            output_lines.append(' '.join(my_output))
    print('end======={0}======='.format(file_path))
    return output_lines


def main():
    dir_path = './data/input'
    output_dir = './data/output'

    for item in os.listdir(dir_path):
        if not item.endswith('.txt'):
            continue

        file_path = os.path.join(dir_path, item)
        output_lines = do_jieba(file_path)

        output_filepath = os.path.join(output_dir, item)
        if os.path.exists(output_filepath):
            os.unlink(output_filepath)

        with open(output_filepath, 'w+') as write_handler:
            write_handler.write('\n\n\n\n'.join(output_lines))


if __name__ == '__main__':
    main()

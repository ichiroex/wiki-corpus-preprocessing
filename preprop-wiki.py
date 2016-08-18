# -*- coding: utf-8 -*-

import sys
import re

def remove_brackets(sentences, delimiter=" "):

    sentences_without_brackets = []
    pattern = r"[\(\[].+?[\]\)]|\{\{.+?\}\}"
    for sen in sentences:
        sen = sen.replace("（", "(").replace("）", ")") + " " + delimiter
        for m in re.findall(pattern, sen):
            sen = sen.replace(m, "") # remove string including brackets
        sentences_without_brackets.append(sen)

    return sentences_without_brackets

def split_line(line, delimiter):
    pattern = r"「.+?」"
    for m in re.findall(pattern, line):
        tmp_m = m.replace(delimiter, "")
        line = line.replace(m, tmp_m)

    return line.split(delimiter)[:-1]

def main():

    delimiter = "。"

    # 標準入力を一行ずつ読み込み
    for line in sys.stdin:

        b_sentences = split_line(line, delimiter) # before
        a_sentences = remove_brackets(b_sentences, delimiter=delimiter) # after

        for a in a_sentences:
            if len(a) > 40 and len(a) < 800:
                print a

if __name__ == '__main__':
    main()

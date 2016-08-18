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

def main():

    delimiter = "。"

    # 標準入力を一行ずつ読み込み
    for line in sys.stdin:

        b_sentences = line.split(delimiter)[:-1] # before
        a_sentences = remove_brackets(b_sentences, delimiter=delimiter) # after

        for a in a_sentences:
            if len(a) > 40 and len(a) < 800:
                print a

if __name__ == '__main__':
    main()

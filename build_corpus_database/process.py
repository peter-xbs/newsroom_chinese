# _*_ coding:utf-8 _*_

import os
import json
import copy
from newsroom.analyze import Fragments

src_dir = '/Users/peter_sun/PycharmProjects/TextSummary/corpus'
tgt = os.path.join(src_dir, '平安科技新闻语料库.corpus')
with open('template.json') as f:
    template_dic = json.load(f)

# QHG
src = os.path.join(src_dir, 'QHG_corpus.txt')
with open(tgt, 'a', encoding='utf-8') as fo:
    with open(src, encoding='utf-8') as f:
        for line in f:
            line_dic = copy.deepcopy(template_dic)
            line_list = line.strip().split('\t\t')
            if len(line_list) != 2:
                print(line)
                continue
            text, summary = line_list
            fragments = Fragments(summary, text)
            coverage = fragments.coverage()
            density = fragments.density()
            compression = fragments.compression()
            text_len = len(text)
            summary_len = len(summary)
            dataset_src = "头条QHG"

            line_dic["text"], line_dic["summary"], line_dic["title"] = text, summary, summary
            line_dic["coverage"], line_dic["density"] = coverage, density
            line_dic["compression"], line_dic["text_len"] = compression, text_len
            line_dic["dataset_src"], line_dic["summary_len"] = dataset_src, summary_len

            new_line = json.dumps(line_dic, ensure_ascii=False)+'\n'
            fo.write(new_line)



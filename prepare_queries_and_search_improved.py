
from bs4 import BeautifulSoup
from pyserini.search import SimpleSearcher
import pandas as pd

import os, json

param_1_tests = [0.6]
param_2_tests = [0.5]
param_3_tests = [5, 7, 10]
param_4_tests = [5, 7, 10]
param_5_tests = [0.5625, 0.625, 0.75, 0.5]

use_rm3 = True

for param_1 in param_1_tests:
    for param_2 in param_2_tests:
        for param_3 in param_3_tests:
            for param_4 in param_4_tests:
                for param_5 in param_5_tests:

                    queries_path = "resources/queries.xml"
                    indexes_path = "indexes/FSP95_json"
                    output_path = f"outputs/run_FSP95_json_improved_bm25_{param_1}_{param_2}_rm3_{use_rm3}_{param_3}_{param_4}_{param_5}.txt"

                    # Load queries file
                    with open(f"{queries_path}", encoding="utf-8") as fp:
                        soup = BeautifulSoup(fp)
                            
                    nums = (soup.find_all("num"))
                    pttitles = (soup.find_all("pt-title"))
                    ptdescs = (soup.find_all("pt-desc"))
                    ptnarrs = (soup.find_all("pt-narr"))

                    searcher = SimpleSearcher(indexes_path)
                    searcher.set_language('ptbr')
                    searcher.set_bm25(param_1, param_2)
                    if use_rm3:
                        searcher.set_rm3(param_3, param_4, param_5)

                    lines = []

                    for num, pttitle in zip(nums, pttitles):
                        hits = searcher.search(pttitle.text, k=100)
                        print(pttitle.text)

                        for i in range(len(hits)):
                            #print(f'{i+1:2} {hits[i].docid:4} {hits[i].score:.5f}')
                            lines.append([num.text, "Q0", hits[i].docid, i, f"""{hits[i].score:.6f}""", "jonas"])

                    os.makedirs("outputs", exist_ok=True)

                    with open(output_path, "w+"):
                        pd.DataFrame(lines).to_csv(output_path, sep="\t", index=False, header=False)

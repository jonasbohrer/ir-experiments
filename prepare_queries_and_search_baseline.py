
from bs4 import BeautifulSoup
from pyserini.search import SimpleSearcher
import pandas as pd

import os, json

queries_path = "resources/queries.xml"
indexes_path = "indexes/FSP95_json"
output_path = "outputs/run_FSP95_json_baseline.txt"

# Load queries file
with open(f"{queries_path}", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp)
        
nums = (soup.find_all("num"))
pttitles = (soup.find_all("pt-title"))
ptdescs = (soup.find_all("pt-desc"))
ptnarrs = (soup.find_all("pt-narr"))

searcher = SimpleSearcher(indexes_path)
searcher.set_language('ptbr')

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


import json
import os

import pandas as pd
from bs4 import BeautifulSoup

queries_path = "resources\queries.xml"
output_path = ""

# Load queries file
with open(f"{queries_path}", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp)

# Save to correct queries format (tsv)
nums = (soup.find_all("num"))
pttitles = (soup.find_all("pt-title"))
ptdescs = (soup.find_all("pt-desc"))
ptnarrs = (soup.find_all("pt-narr"))

queries_output = [[num.text, pttitle.text] for num, pttitle in zip(nums, pttitles)]

pd.DataFrame(queries_output).to_csv("resources/queries.tsv", sep="\t", index=False, header=False)

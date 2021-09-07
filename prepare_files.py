import json
import os

from bs4 import BeautifulSoup

doc_base_path = "resources\FSP95"
output_path = f"{doc_base_path}_json"

for doc_path in os.listdir(doc_base_path):

    # Load file
    with open(f"{doc_base_path}\{doc_path}", encoding="latin1") as fp:
        soup = BeautifulSoup(fp, "html.parser")

    # Get data and transform it to pyserini format
    docids = (soup.find_all("docid"))
    dates = (soup.find_all("date"))
    categories = (soup.find_all("category"))
    texts = (soup.find_all("text"))

    pyserini_json_format = [{"id": docid.text, "contents": text.text} for docid, text in zip(docids, texts)]

    # Save to json
    os.makedirs(f"{output_path}", exist_ok=True)

    with open(f"""{output_path}\{doc_path.replace("sgml", "json")}""", "w+", encoding="utf-8") as f:
        json.dump(pyserini_json_format, f, ensure_ascii=False, indent=2)

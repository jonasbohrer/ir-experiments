Requirements:

- Have JAVA SDK (13+) installed .
    - Make sure you have your JAVA SDK path set to the environment variables JAVA_HOME and PATH (e.g. "C:\Program Files\Java\jdk-\<version\>\bin"),
    - as well as \<JAVA SDK path + "\server"> (e.g. "C:\Program Files\Java\jdk-\<version\>\bin\server") in the PATH.
- Create an empty python 3.7 conda environment.
- Run `pip install pyserini`.
- Place the dataset directory in `/resources/<dataset_name>` with SGML files.
- Place the queries .xml file in `/resources/queries.xml`.

Execution:

1. access the base path of the repo: `cd <your_git_path/ir-experiments>`

2. run: `python prepare_files.py` and verify that a `resources/<file_name>_json` directory has been generated with a json collection version of the original document collection.

3. run: `python -m pyserini.index -collection JsonCollection -generator DefaultLuceneDocumentGenerator -language ptbr -threads 1 -input resources/FSP95_json -index indexes/FSP95_json -storePositions -storeDocvectors -storeRaw` and verify that a `indexes/<file_name>_json` indexes directory has been generated.

4. run: `python prepare_queries_and_search_baseline.py` and verify the output file in `outputs/<filename>.txt`.

5. run: `python prepare_queries_and_search_improved.py` and verify the output file in `outputs/<filename>.txt` (change the parameters in the code to perform the intended tests).

import spacy
import pandas as pd
import os
import json

if __name__ == "__main__":
    # nlp = spacy.load('en_core_web_md')
    config_path = os.path.dirname(os.path.dirname(__file__))

    with open(os.path.join(config_path, "config", "default.json"), "r") as jf:
        config = json.load(jf)

    data_path = os.path.join(os.path.expanduser('~'), config["path"], config["data"]["input"])

    df_metadata = pd.read_csv(os.path.join(data_path, 'ted_main.csv'))

    df_transcripts = pd.read_csv(data_path, 'transcripts.csv')

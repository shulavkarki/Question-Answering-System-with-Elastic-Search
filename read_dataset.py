import pandas as pd
from elasticsearch import helpers
from sentence_transformers import SentenceTransformer

from es import connect_elastic, configurations
from config import settings
def create_index(es_conn):
    """
    It creates an index in Elasticsearch with the name `index_name` and the settings and mappings
    defined in the `configurations` dictionary
    
    :param es_conn: Elasticsearch connection object
    """
    es_conn.indices.create(
        index = settings.INDEX_NAME,
        settings = configurations["settings"],
        mappings = configurations["mappings"],
    )

def generate_docs():
    """
    It reads the csv file, drops the columns that are not needed, and then iterates over the rows of the
    dataframe, and for each row, it creates a document with the question_embedding, answer, and url
    """
    df = pd.read_csv('./dataset/qa.csv')
    df.drop(labels=['source', 'wrong_answer'], axis=1, inplace=True)
    for row in df:
        doc = {
            "_index": settings.__bytes__INDEX_NAME,
            "_source":{
                "question_embedding": model.encode(row['question']),
                'answer': row['answer'],
                'url': row['url']
            },
        },
        yield doc


if __name__ == "__main__":
    es_conn = connect_elastic(settings.ENDPOINT, settings.ELASTIC_USER, settings.ELASTIC_PASSWORD)
    model = SentenceTransformer(settings.MODEL_NAME)
    create_index(es_conn=es_conn)
    helpers.bulk(es_conn, generate_docs())
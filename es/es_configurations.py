configurations = {
    "settings": {
        "number_of_shards": 2,
        "number_of_replicas": 1,
    },
    "mappings": {
        "properties": {
            "answer": {
                "type": "text",
            },
            "question_embedding": {"type": "dense_vector", "dims": 384},
            "url": {
                "type": "text",
            },
        }
    },
}
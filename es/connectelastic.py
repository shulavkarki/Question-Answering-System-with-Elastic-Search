from elasticsearch import Elasticsearch


def connect_elastic(endpoint: str, user: str, password: str):
    """
    It connects to the Elasticsearch cluster.
    :param endpoint: The URL of the Elasticsearch cluster
    :param user: The username of the Elasticsearch user
    :param password: the password for the elasticsearch user
    :return: the es variable.
    """
    global es
    es = Elasticsearch(endpoint, http_auth=(user, password), timeout=300)
    #  send_get_body_as='POST'
    if es.ping():
        print(f"Elastic-search connection established.")
    else:
        print("Elasticsearch Connection Failed.")
    return es
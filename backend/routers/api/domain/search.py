import json
from common.elasticsearch.client import ElasticSearchClient

from core.texts.vectorize import USE_vectorize

client = ElasticSearchClient()
client.debug = False

QUERY_TYPE = {
    "edinet_code": "term",
    "company.edinet_code": "term",
    "security_code": "term",
    "company.security_code": "term",
    "content": "match_phrase",
}


def get_query(field, value):
    query_type = QUERY_TYPE.get(field, "match")
    if query_type == "term" and isinstance(value, list):
        query_type = "terms"
    return {
        query_type: {
            field: value,
        },
    }


def search_value(index, fields, order_by=None, **kwargs):
    if not fields:
        return []
    search_config = {
        "query": {
            "bool": {
                "must": list(map(lambda args: get_query(*args), fields.items())),
            },
        },
        "aggs": {
            "total": {
                "cardinality": {
                    "field": "company.edinet_code",
                    "precision_threshold": 10000
                }
            }
        },
    }
    if order_by:
        search_config["sort"] = [{ order_by : "asc" }, "_score"]
    for key, value in kwargs.items():
        search_config[key] = value
    res = client.search(index, search_config).json()
    hits = res.get("hits", {})
    if index == "company":
        total = hits.get("total", {}).get("value", 0)
    else:
        total = res.get("aggregations", {}).get("total", {}).get("value", 0)
    hits = hits.get("hits", [])

    return {
        "pagination": {
            "total": total,
            "from": kwargs.get("from", 0),
            "count": len(hits),
        },
        "data": hits,
    }


def search_knn(index, field, value, fields={}, k=50, num_candidates=100, **kwargs):
    if not value:
        return []
    search_config = {
        "knn": {
            "field": field,
            "k": k,
            "num_candidates": num_candidates,
            "query_vector": USE_vectorize([value])[0],
        },
        "aggs": {
            "total": {
                "cardinality": {
                    "field": "company.edinet_code",
                    "precision_threshold": 10000
                }
            }
        },
    }
    for key, value in kwargs.items():
        search_config[key] = value

    if fields:
        search_config["query"] = {
            "bool": {
                "must": list(map(lambda args: get_query(*args), fields.items())),
            },
        }
        print(json.dumps(search_config["query"], indent=2))

    res = client.search(index, search_config).json()
    hits = res.get("hits", {})
    total = res.get("aggregations", {}).get("total", {}).get("value", 0)
    hits = hits.get("hits", [])

    return {
        "pagination": {
            "total": total,
            "from": kwargs.get("from", 0),
            "count": len(hits),
        },
        "data": hits,
    }


def search(index, order_by=None, **kwargs):
    search_config = {
        "query": {
            "match_all": {}
        },
    }
    if order_by:
        search_config["sort"] = [{ order_by : "asc" }, "_score"]
    for key, value in kwargs.items():
        search_config[key] = value

    res = client.search(index, search_config).json()
    hits = res.get("hits", {})
    total = hits.get("total", {}).get("value", 0)
    hits = hits.get("hits", [])

    return {
        "pagination": {
            "total": total,
            "from": kwargs.get("from", 0),
            "count": len(hits),
        },
        "data": hits,
    }

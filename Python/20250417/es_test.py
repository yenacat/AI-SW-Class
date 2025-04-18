from elasticsearch import Elasticsearch


ELASTIC_ID = "elastic"
ELASTIC_PASSWORD = "r*ZZhHhoRZ*lH0F4ZumN"

client = Elasticsearch(
    "https://localhost:9200",
    ca_certs="C:/Users/UserK/Downloads/es9/elasticsearch/config/certs/http_ca.crt",
    basic_auth=(ELASTIC_ID, ELASTIC_PASSWORD),
)

# client.indices.create(index="my_index")

# client.indices.delete(index="my_index")

# client.index(
#     index="my_index2",
#     id="my_document_id",
#     document={
#         "field1": "value1",
#         "field2": "value2",
#     },
# )

result = client.get(index="my_index2", id="my_document_id")

print(result)

result = client.search(index="my_index2", query={"match": {"field1": "value1"}})

print(result)

client.update(
    index="my_index2",
    id="my_document_id",
    doc={"field1": "new_value1", "new_field": "new_value2"},
)

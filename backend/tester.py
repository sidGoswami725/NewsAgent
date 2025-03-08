from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(
    "https://9fb474a7f57d4bfbbd9e05246ff0b8ec.asia-south1.gcp.elastic-cloud.com:443",
    basic_auth=("elastic", "6lWF4jG8mE5IUnOSc66kmSo1"),
    verify_certs=False  # Disable SSL verification for debugging
)

# Fetch a sample document
response = es.search(index="news-articles", body={"query": {"match_all": {}}}, size=1)
if response['hits']['hits']:
    article = response['hits']['hits'][0]['_source']
    print("Sample Article:", article)
    print("Image URL:", article.get('image_url', 'No image URL found'))
else:
    print("No articles found in the index.")
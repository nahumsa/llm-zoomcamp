from searching import es_query

question = "How do I execute a command in a running docker container?"
filter_course = "machine-learning-zoomcamp"
print(
    es_query(question, filter_course=filter_course)["hits"][2]["_source"][  # type: ignore
        "question"
    ],
)

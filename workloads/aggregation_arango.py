import time


def aggregation_benchmark_arango(db):

    query = """
    RETURN LENGTH(User)
    """

    start = time.perf_counter()

    db.execute(query)

    end = time.perf_counter()

    return (end - start) * 1000
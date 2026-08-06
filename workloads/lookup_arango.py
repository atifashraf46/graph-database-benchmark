import time


def lookup_benchmark_arango(db, user_id):
    query = """
    FOR u IN User
        FILTER u.id == @id
        RETURN u
    """

    start = time.perf_counter()

    db.execute(query, {"id": user_id})

    end = time.perf_counter()

    return (end - start) * 1000
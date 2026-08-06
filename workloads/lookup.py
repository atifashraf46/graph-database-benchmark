import time


def lookup_benchmark(db, user_id):
    """
    Executes a lookup query and returns the execution time in milliseconds.
    """

    query = """
    MATCH (u:User {id:$id})
    RETURN u
    """

    start = time.perf_counter()

    db.execute(query, {"id": user_id})

    end = time.perf_counter()

    return (end - start) * 1000
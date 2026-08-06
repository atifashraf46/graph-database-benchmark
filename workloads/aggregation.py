import time


def aggregation_benchmark(db):
    """
    Executes an aggregation query and returns the execution time in milliseconds.
    """

    query = """
    MATCH (u:User)
    RETURN count(u) AS totalUsers
    """

    start = time.perf_counter()

    db.execute(query)

    end = time.perf_counter()

    return (end - start) * 1000
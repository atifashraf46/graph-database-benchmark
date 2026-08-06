import time


def traversal_benchmark_arango(db, user_id, hops=1):

    query = f"""
    WITH User

    FOR v IN 1..{hops}
        OUTBOUND CONCAT("User/", @id)
        Friend
        RETURN v
    """

    start = time.perf_counter()

    db.execute(query, {"id": user_id})

    end = time.perf_counter()

    return (end - start) * 1000
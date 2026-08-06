import time


def traversal_benchmark(db, user_id, hops=1):
    """
    Executes traversal queries of different hop depths.
    Returns execution time in milliseconds.
    """

    if hops == 1:
        query = """
        MATCH (u:User {id:$id})-[:FRIEND]->(friend)
        RETURN friend
        """

    elif hops == 2:
        query = """
        MATCH (u:User {id:$id})-[:FRIEND]->()-[:FRIEND]->(friend)
        RETURN friend
        """

    elif hops == 3:
        query = """
        MATCH (u:User {id:$id})-[:FRIEND]->()-[:FRIEND]->()-[:FRIEND]->(friend)
        RETURN friend
        """

    else:
        raise ValueError("Hop count must be 1, 2, or 3")

    start = time.perf_counter()

    db.execute(query, {"id": user_id})

    end = time.perf_counter()

    return (end - start) * 1000
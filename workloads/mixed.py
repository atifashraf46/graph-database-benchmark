import time


def mixed_benchmark(db, user_id):
    """
    Executes a mixed workload consisting of lookup,
    traversal and aggregation.
    Returns execution time in milliseconds.
    """

    start = time.perf_counter()

    # Lookup
    db.execute(
        """
        MATCH (u:User {id:$id})
        RETURN u
        """,
        {"id": user_id},
    )

    # Traversal
    db.execute(
        """
        MATCH (u:User {id:$id})-[:FRIEND]->(friend)
        RETURN friend
        """,
        {"id": user_id},
    )

    # Aggregation
    db.execute(
        """
        MATCH (u:User)
        RETURN count(u)
        """
    )

    end = time.perf_counter()

    return (end - start) * 1000
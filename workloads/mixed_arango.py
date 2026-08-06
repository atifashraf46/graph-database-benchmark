import time


def mixed_benchmark_arango(db, user_id):

    start = time.perf_counter()

    db.execute("""
    FOR u IN User
        FILTER u.id == @id
        RETURN u
    """, {"id": user_id})

    db.execute("""
    WITH User

    FOR v IN 1..1
        OUTBOUND CONCAT("User/", @id)
        Friend
        RETURN v
    """, {"id": user_id})

    db.execute("""
    RETURN LENGTH(User)
    """)

    end = time.perf_counter()

    return (end - start) * 1000
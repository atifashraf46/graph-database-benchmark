import time

from config import DATABASES

from databases.neo4j import Neo4jDB
from databases.cognodb import CognoDB
from databases.memgraph import MemgraphDB
from databases.arangodb import ArangoDB

# Cypher workloads
from workloads.lookup import lookup_benchmark
from workloads.traversal import traversal_benchmark
from workloads.aggregation import aggregation_benchmark
from workloads.mixed import mixed_benchmark

# ArangoDB workloads
from workloads.lookup_arango import lookup_benchmark_arango
from workloads.traversal_arango import traversal_benchmark_arango
from workloads.aggregation_arango import aggregation_benchmark_arango
from workloads.mixed_arango import mixed_benchmark_arango

from utils.statistics import calculate_statistics
from utils.csv_writer import save_results

results = []


def run_multiple_times(func, *args, iterations=10):
    times = []

    for _ in range(iterations):
        t = func(*args)
        times.append(t)

    return calculate_statistics(times)


def benchmark_connection(name, db):
    print(f"\n{name} Connection Test")

    start = time.perf_counter()
    db.connect()
    end = time.perf_counter()

    print(f"Connection Time: {(end-start)*1000:.2f} ms")


def print_stats(name, workload, stats):
    print(f"\n{name} {workload} Benchmark")
    print(f"Runs      : {stats['runs']}")
    print(f"Average   : {stats['average']:.2f} ms")
    print(f"Minimum   : {stats['minimum']:.2f} ms")
    print(f"Maximum   : {stats['maximum']:.2f} ms")
    print(f"Median    : {stats['median']:.2f} ms")

    results.append([
        name,
        workload,
        stats["runs"],
        f"{stats['average']:.2f}",
        f"{stats['minimum']:.2f}",
        f"{stats['maximum']:.2f}",
        f"{stats['median']:.2f}",
    ])


def run_database(name, db):

    benchmark_connection(name, db)

    if name == "ArangoDB":

        print_stats(
            name,
            "Lookup",
            run_multiple_times(lookup_benchmark_arango, db, "1")
        )

        print_stats(
            name,
            "Traversal",
            run_multiple_times(traversal_benchmark_arango, db, "1")
        )

        print_stats(
            name,
            "Aggregation",
            run_multiple_times(aggregation_benchmark_arango, db)
        )

        print_stats(
            name,
            "Mixed",
            run_multiple_times(mixed_benchmark_arango, db, "1")
        )

    else:

        print_stats(
            name,
            "Lookup",
            run_multiple_times(lookup_benchmark, db, "1")
        )

        print_stats(
            name,
            "Traversal",
            run_multiple_times(traversal_benchmark, db, "1")
        )

        print_stats(
            name,
            "Aggregation",
            run_multiple_times(aggregation_benchmark, db)
        )

        print_stats(
            name,
            "Mixed",
            run_multiple_times(mixed_benchmark, db, "1")
        )

    db.close()


def main():

    neo4j = Neo4jDB(
        DATABASES["Neo4j"]["uri"],
        DATABASES["Neo4j"]["user"],
        DATABASES["Neo4j"]["password"],
    )

    cognodb = CognoDB(
        DATABASES["CognoDB"]["uri"],
        DATABASES["CognoDB"]["user"],
        DATABASES["CognoDB"]["password"],
    )

    memgraph = MemgraphDB(
        DATABASES["Memgraph"]["uri"],
        DATABASES["Memgraph"]["user"],
        DATABASES["Memgraph"]["password"],
    )

    arangodb = ArangoDB(
        DATABASES["ArangoDB"]["uri"],
        DATABASES["ArangoDB"]["user"],
        DATABASES["ArangoDB"]["password"],
    )

    run_database("Neo4j", neo4j)
    run_database("CognoDB", cognodb)
    run_database("Memgraph", memgraph)
    run_database("ArangoDB", arangodb)

    save_results(results)


if __name__ == "__main__":
    main()
import time

from config import DATABASES
from databases.neo4j import Neo4jDB
from databases.cognodb import CognoDB

from workloads.lookup import lookup_benchmark
from workloads.traversal import traversal_benchmark
from workloads.aggregation import aggregation_benchmark
from workloads.mixed import mixed_benchmark

from utils.statistics import calculate_statistics
from utils.csv_writer import save_results


results = []


def run_multiple_times(benchmark_function, *args, iterations=10):
    times = []

    for _ in range(iterations):
        execution_time = benchmark_function(*args)
        times.append(execution_time)

    return calculate_statistics(times)


def benchmark_connection(name, db):
    print(f"\n{name} Connection Test")

    start = time.perf_counter()
    db.connect()
    end = time.perf_counter()

    print(f"Connection Time: {(end-start)*1000:.2f} ms")


def benchmark_lookup(name, db):
    print(f"\n{name} Lookup Benchmark")

    stats = run_multiple_times(lookup_benchmark, db, "1")

    print(f"Runs      : {stats['runs']}")
    print(f"Average   : {stats['average']:.2f} ms")
    print(f"Minimum   : {stats['minimum']:.2f} ms")
    print(f"Maximum   : {stats['maximum']:.2f} ms")
    print(f"Median    : {stats['median']:.2f} ms")

    results.append([
        name,
        "Lookup",
        stats["runs"],
        f"{stats['average']:.2f}",
        f"{stats['minimum']:.2f}",
        f"{stats['maximum']:.2f}",
        f"{stats['median']:.2f}"
    ])


def benchmark_traversal(name, db):
    print(f"\n{name} Traversal Benchmark")

    stats = run_multiple_times(traversal_benchmark, db, "1")

    print(f"Runs      : {stats['runs']}")
    print(f"Average   : {stats['average']:.2f} ms")
    print(f"Minimum   : {stats['minimum']:.2f} ms")
    print(f"Maximum   : {stats['maximum']:.2f} ms")
    print(f"Median    : {stats['median']:.2f} ms")

    results.append([
        name,
        "Traversal",
        stats["runs"],
        f"{stats['average']:.2f}",
        f"{stats['minimum']:.2f}",
        f"{stats['maximum']:.2f}",
        f"{stats['median']:.2f}"
    ])


def benchmark_aggregation(name, db):
    print(f"\n{name} Aggregation Benchmark")

    stats = run_multiple_times(aggregation_benchmark, db)

    print(f"Runs      : {stats['runs']}")
    print(f"Average   : {stats['average']:.2f} ms")
    print(f"Minimum   : {stats['minimum']:.2f} ms")
    print(f"Maximum   : {stats['maximum']:.2f} ms")
    print(f"Median    : {stats['median']:.2f} ms")

    results.append([
        name,
        "Aggregation",
        stats["runs"],
        f"{stats['average']:.2f}",
        f"{stats['minimum']:.2f}",
        f"{stats['maximum']:.2f}",
        f"{stats['median']:.2f}"
    ])


def benchmark_mixed(name, db):
    print(f"\n{name} Mixed Benchmark")

    stats = run_multiple_times(mixed_benchmark, db, "1")

    print(f"Runs      : {stats['runs']}")
    print(f"Average   : {stats['average']:.2f} ms")
    print(f"Minimum   : {stats['minimum']:.2f} ms")
    print(f"Maximum   : {stats['maximum']:.2f} ms")
    print(f"Median    : {stats['median']:.2f} ms")

    results.append([
        name,
        "Mixed",
        stats["runs"],
        f"{stats['average']:.2f}",
        f"{stats['minimum']:.2f}",
        f"{stats['maximum']:.2f}",
        f"{stats['median']:.2f}"
    ])


def run_database(name, db):
    benchmark_connection(name, db)
    benchmark_lookup(name, db)
    benchmark_traversal(name, db)
    benchmark_aggregation(name, db)
    benchmark_mixed(name, db)
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

    run_database("Neo4j", neo4j)
    run_database("CognoDB", cognodb)

    save_results(results)


if __name__ == "__main__":
    main()
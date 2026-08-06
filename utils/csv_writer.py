import csv
import os


def save_results(results):
    """
    Save benchmark results into a CSV file.
    """

    os.makedirs("results", exist_ok=True)

    with open("results/benchmark_results.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Database",
            "Benchmark",
            "Runs",
            "Average(ms)",
            "Minimum(ms)",
            "Maximum(ms)",
            "Median(ms)",
            "P50(ms)",
            "P95(ms)"
        ])

        for row in results:
            writer.writerow(row)

    print("\nResults saved to results/benchmark_results.csv")
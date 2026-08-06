import csv
import os


class BenchmarkMetrics:

    def __init__(self):
        self.results = []

    def add_result(
        self,
        database,
        workload,
        latency,
        throughput,
        success=True,
    ):

        self.results.append(
            {
                "database": database,
                "workload": workload,
                "latency_ms": round(latency * 1000, 3),
                "throughput_qps": round(throughput, 3),
                "success": success,
            }
        )

    def save(self, filename):

        os.makedirs("results", exist_ok=True)

        with open(
            f"results/{filename}",
            "w",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "database",
                    "workload",
                    "latency_ms",
                    "throughput_qps",
                    "success",
                ],
            )

            writer.writeheader()

            writer.writerows(self.results)
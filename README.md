# Graph Database Cloud Benchmark

## Overview

This project benchmarks managed graph databases using a common dataset and identical workloads. The goal is to evaluate the performance of different cloud graph database platforms under the same benchmarking methodology.

This project was developed as part of the WEXA AI Graph Database Cloud Benchmark Assignment.

---

## Databases Compared

- CognoDB Cloud
- Neo4j AuraDB

> The project is designed with a modular architecture, making it easy to extend support for additional graph databases such as Memgraph, FalkorDB, and ArangoDB.

---

## Benchmark Workloads

The benchmark suite measures the following workloads:

### Connection Benchmark
- Database connection latency

### Lookup Benchmark
- Point lookup queries

### Traversal Benchmark
- Graph traversal queries

### Aggregation Benchmark
- Count and aggregation queries

### Mixed Workload Benchmark
- Combined read/write operations

---

## Project Structure

```
graph-database-benchmark/
│
├── databases/
├── dataset/
├── loaders/
├── utils/
├── workloads/
├── benchmark.py
├── config.py
├── requirements.txt
└── README.md
```

---

## Dataset

The benchmark uses a sampled subset of the SNAP Pokec social network dataset.

The complete dataset is intentionally not included in this repository because of GitHub file size limitations.

Sample dataset files are included for testing.

---

## Installation

Clone the repository

```bash
git clone https://github.com/atifashraf46/graph-database-benchmark.git
```

Move into the project

```bash
cd graph-database-benchmark
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file containing your database credentials.

Example:

```
NEO4J_URI=
NEO4J_USER=
NEO4J_PASSWORD=

COGNODB_URI=
COGNODB_USER=
COGNODB_PASSWORD=
```

Do not commit credentials to GitHub.

---

## Running the Benchmark

Run

```bash
python benchmark.py
```

Benchmark results are exported to

```
results/benchmark_results.csv
```

---

## Methodology

- Same benchmark code used for every database
- Same dataset
- Same query workloads
- Multiple benchmark iterations
- Execution time measured in milliseconds
- Statistics include:
  - Average
  - Minimum
  - Maximum
  - Median

---

## Technologies Used

- Python 3
- Neo4j Python Driver
- Cypher Query Language
- CSV
- Git
- GitHub

---

## Current Results

The benchmark currently reports:

- Connection Time
- Lookup Time
- Traversal Time
- Aggregation Time
- Mixed Workload Time

Results are automatically exported as CSV.

---

## Future Improvements

- Add Memgraph Cloud
- Add FalkorDB
- Add ArangoDB
- Support larger benchmark datasets
- Concurrent client benchmarking
- Performance charts
- p50/p95 latency reporting
- Resource utilization monitoring

---

## Notes

This benchmark is intended for educational and evaluation purposes. Results may vary depending on network latency, cloud region, database tier, and system resources.

---

## Author

**Mohammad Atif Hussain**

WEXA AI Graph Database Benchmark Assignment

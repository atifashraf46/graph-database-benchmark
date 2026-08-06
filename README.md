# Graph Database Benchmark Framework

A modular benchmarking framework developed to evaluate the performance of multiple graph database systems using a common dataset and standardized workloads.

This project benchmarks graph databases by measuring execution time for common graph operations such as node lookup, graph traversal, aggregation, and mixed workloads. Results are collected automatically and exported as CSV files for comparison and analysis.

---

## Supported Graph Databases

The framework currently supports the following graph databases:

- Neo4j
- CognoDB
- Memgraph
- ArangoDB

Each database is implemented through a common interface, making the framework easily extensible for additional graph databases.

---

## Project Structure

```
graph-benchmark-clean/
│
├── databases/
│   ├── base.py
│   ├── neo4j.py
│   ├── cognodb.py
│   ├── memgraph.py
│   └── arangodb.py
│
├── loaders/
│   ├── load_dataset.py
│   ├── import_neo4j.py
│   ├── import_memgraph.py
│   ├── import_cognodb.py
│   └── import_arangodb.py
│
├── workloads/
│   ├── lookup.py
│   ├── traversal.py
│   ├── aggregation.py
│   ├── mixed.py
│   ├── lookup_arango.py
│   ├── traversal_arango.py
│   ├── aggregation_arango.py
│   └── mixed_arango.py
│
├── dataset/
│
├── results/
│
├── benchmark.py
├── config.py
├── requirements.txt
└── README.md
```

---

## Features

- Modular benchmark architecture
- Support for multiple graph databases
- Common benchmark interface
- Automated dataset loading
- Automated benchmark execution
- CSV result generation
- Easily extensible database adapters

---

## Benchmark Workloads

The framework evaluates each database using four workloads.

### 1. Lookup Benchmark

Measures the execution time required to retrieve a user node by its ID.

Example:

```
MATCH (u:User {id:$id})
RETURN u
```

---

### 2. Traversal Benchmark

Measures the execution time required to traverse friendship relationships from a starting user.

---

### 3. Aggregation Benchmark

Measures the performance of aggregate operations such as counting all user nodes.

---

### 4. Mixed Benchmark

Executes a combination of:

- Lookup
- Traversal
- Aggregation

This simulates a more realistic workload.

---

## Dataset

The framework imports user profiles and friendship relationships into each supported graph database.

Dataset files include:

- User profiles
- User relationships

The same dataset format is used across all databases to ensure consistent benchmarking.

---

## Technologies Used

- Python 3
- Neo4j Python Driver
- ArangoDB Python Driver
- Memgraph
- CognoDB
- CSV
- Git
- GitHub

---

## Installation

Clone the repository.

```bash
git clone https://github.com/atifashraf46/graph-database-benchmark.git
```

Move into the project directory.

```bash
cd graph-database-benchmark
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file containing your database credentials.

Example:

```env
NEO4J_URI=
NEO4J_USER=
NEO4J_PASSWORD=

COGNODB_URI=
COGNODB_USER=
COGNODB_PASSWORD=

MEMGRAPH_URI=
MEMGRAPH_USER=
MEMGRAPH_PASSWORD=

ARANGO_URI=
ARANGO_USER=
ARANGO_PASSWORD=
```

---

## Loading Data

Import the dataset into each database before running benchmarks.

Example:

```bash
python -m loaders.import_neo4j
```

Similarly:

```
python -m loaders.import_memgraph

python -m loaders.import_cognodb

python -m loaders.import_arangodb
```

---

## Running Benchmarks

Execute:

```bash
python benchmark.py
```

The benchmark automatically executes:

- Connection Benchmark
- Lookup Benchmark
- Traversal Benchmark
- Aggregation Benchmark
- Mixed Benchmark

for every supported database.

---

## Results

Benchmark results are automatically exported to:

```
results/benchmark_results.csv
```

Each workload records:

- Number of runs
- Average execution time
- Minimum execution time
- Maximum execution time
- Median execution time

---

## Current Benchmark Results

The project has been successfully benchmarked on:

- Neo4j
- CognoDB
- Memgraph
- ArangoDB

Each database was tested using the same benchmark framework and identical workloads.

---

## Design

The framework follows an adapter-based architecture.

Each database inherits from a common `BaseDatabase` interface.

This design allows new graph databases to be integrated with minimal code changes while keeping benchmark logic independent from database-specific implementations.

---

## Future Improvements

Possible enhancements include:

- Additional graph database support
- Larger benchmark datasets
- Advanced latency metrics
- Benchmark visualizations
- Performance analysis dashboards

---

## Author

**Mohammad Atif Hussain**

B.Tech Computer Science (Artificial Intelligence & Machine Learning)

GitHub:
https://github.com/atifashraf46

---

## License

This project was developed for educational and benchmarking purposes.

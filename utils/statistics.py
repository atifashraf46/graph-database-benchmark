import statistics


def percentile(data, percent):
    """
    Calculate percentile using linear interpolation.
    """

    if not data:
        return 0

    data = sorted(data)

    k = (len(data) - 1) * (percent / 100)

    f = int(k)
    c = min(f + 1, len(data) - 1)

    if f == c:
        return data[f]

    return data[f] + (k - f) * (data[c] - data[f])


def calculate_statistics(times):
    """
    Calculate benchmark statistics.
    """

    if len(times) == 0:
        return None

    return {
        "runs": len(times),
        "average": statistics.mean(times),
        "minimum": min(times),
        "maximum": max(times),
        "median": statistics.median(times),
        "p50": percentile(times, 50),
        "p95": percentile(times, 95),
    }
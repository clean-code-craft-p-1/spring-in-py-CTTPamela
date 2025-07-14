
def calculateStats(numbers):
    if not numbers:
        return {}
    return {
        "avg": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }

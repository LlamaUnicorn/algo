import time
import statistics


def timer(func):
    """
    Timer decorator.

    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        times = []  # List to store the execution times
        num_runs = 100  # Number of times the function will be run

        for _ in range(num_runs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            times.append((end - start) * 1000)  # Convert to milliseconds

        # Remove the minimum and maximum times
        times.remove(min(times))
        times.remove(max(times))

        # Calculate the average time
        avg_time = statistics.mean(times)

        print(f"{func.__name__} average execution time over {num_runs - 2} runs: {avg_time:.5f} milliseconds")

        return result

    return wrapper

import time
import datetime
import sys


def ft_tqdm(lst):
    """
    A generator function to mimic tqdm behavior with a
    progress bar and iteration counter.

    Parameters:
    - lst: An iterable to iterate over.

    Yields:
    - The elements of the iterable with a progress bar and iteration counter.
    """
    total = len(lst)
    start_time = time.time()
    for i, item in enumerate(lst, 1):
        progress = i / total * 100
        elapsed_time = time.time() - start_time
        speed = i / elapsed_time if elapsed_time > 0 else 0
        bar_length = 50
        filled_length = int(bar_length * progress / 100)
        bar = "█" * filled_length + "-" * (bar_length - filled_length)
        eta = (total - i) / speed if speed > 0 else 0
        eta_formatted = str(datetime.timedelta(seconds=int(eta)))
        sys.stdout.write(
            f"\r{progress:.0f}% |{bar}| {i}/{total} "
            f"[{eta_formatted}, {speed:.2f} it/s]"
        )
        yield item
    print()

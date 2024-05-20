import time


def format_date() -> tuple:
    return (
        time.time(),
        "{:.2e}".format(time.time()),
        time.strftime("%b %d %Y", time.localtime(time.time())),
    )


if __name__ == "__main__":
    seconds_since_epoch, scientific_notation, current_date = format_date()
    print(
        f"Seconds since January 1, 1970: {seconds_since_epoch:,.4f}\
            or {scientific_notation} in scientific notation$"
    )
    print(current_date + "$")

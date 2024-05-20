def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    re = []
    for x, y in zip(weight, height):
        re.append(x / y**2)

    return re


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    re = []
    for x in bmi:
        if x <= limit:
            re.append(False)
            continue
        re.append(True)

    return re

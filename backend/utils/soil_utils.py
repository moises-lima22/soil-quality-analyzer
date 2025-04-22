def is_ideal_range(
    value, min_val=None, max_val=None, greater_than=None, less_than=None
):
    if min_val is not None and max_val is not None:
        return min_val <= value <= max_val
    if greater_than is not None:
        return value > greater_than
    if less_than is not None:
        return value < less_than
    return False


def evaluate_soil(sample):
    criteria = {
        "ph": is_ideal_range(sample["ph"], 5.5, 7.0),
        "nitrogen": is_ideal_range(sample["nitrogen"], greater_than=20),
        "phosphorus": is_ideal_range(sample["phosphorus"], greater_than=15),
        "potassium": is_ideal_range(sample["potassium"], greater_than=100),
        "compaction": is_ideal_range(sample["compaction"], less_than=1.4),
    }

    score = sum(criteria.values())
    status = "Apto" if score >= 4 else "Inapto"

    return {"sample": sample, "criteria": criteria, "score": score, "status": status}

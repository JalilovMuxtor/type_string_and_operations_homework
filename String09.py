def main(x1,x2,x3):
    """
    Given three integers, x1, x2, and x3, return the "[x1, x2, x3]" string.
    Args:
        x1: int
        x2: int
        x3: int
    Returns:
        str: return answer.
    """
    return f"[{x1},{x2},{x3}]"
    return "[%d, %d, %d]" % (x1, x2, x3)
print(main(3,2,1))
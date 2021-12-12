def triangle(a, b, c):
    """
    This function checks whether a triangle can be formed from the given sides a, b and c.
    :param a, b, c: The lengths of the sides of the triangle.
    :return: Returns True if given sides form a triangle and False otherwise.
    """
    # Determine the longest side - first element in the list:
    sides_table = sorted([a, b, c], key=None, reverse=True)
    # Check if the triangle can be made:
    if sides_table[0] < sides_table[1] + sides_table[2]:
        return True
    return False


if __name__ == '__main__':
    print(triangle(22, 21, 20))

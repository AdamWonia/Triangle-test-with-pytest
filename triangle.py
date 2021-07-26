def triangle(a, b, c):
    """
    Funkcja sprawdza, czy z podanych boków, można
    utworzyć trójkąt
    :param a: bok trójkąta
    :param b: bok trójkąta
    :param c: bok trójkąta
    :return: zwraca True, jeżeli można, False jeżeli nie można
    """
    # Determine the longest side - first element in list:
    sides_table = sorted([a, b, c], key=None, reverse=True)

    # Check if the triangle can be made:
    if sides_table[0] < sides_table[1] + sides_table[2]:
        return True
    return False


if __name__ == '__main__':
    triangle(22, 21, 20)

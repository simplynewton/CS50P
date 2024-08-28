from Done.Week_5_Unit_Test.calculator import square

def test_square():
    assert square(2) == 4
    assert square(6) == 9 # pytest finds
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0



# def main(): do corner cases
#     test_square()

# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")

# def test_square():
#     if square(2) !=4:
#         print("2 squared was not 4")
#     if square(3) !=9:
#         print("3 squared was not 9:)

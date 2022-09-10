import argparse


def find_sum(a: int, b: int) -> int:
    """This function calculates the sum of two numbers.

    Args:
        a (int): First Number
        b (int): Second Number

    Returns:
        int: Sum
    """
    return a+b


if __name__ == "__main__":

    # parse command line args
    parser = argparse.ArgumentParser(description="Find Sum")

    # system/input/output
    parser.add_argument('--num1', type=int, default=1, help="first number")
    parser.add_argument('--num2', type=int, default=1, help="second number")

    # Execute the parse_args() method
    args = parser.parse_args()

    s = find_sum(args.num1, args.num2)
    print(f'The sum is : {s}')

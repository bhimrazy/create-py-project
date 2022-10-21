import argparse

if __name__ == "__main__":

    # parse command line args
    parser = argparse.ArgumentParser(description="ML/DL App")

    # system/input/output
    parser.add_argument('--task', type=str, help="Tasks are: train | test")

    # Execute the parse_args() method
    args = parser.parse_args()

    if args.task == "train":
        print("Taining...")
    elif args.task == "test":
        print("Testing...")
    else:
        print("Invalid task")

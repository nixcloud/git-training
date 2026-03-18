# Global variable controlling computation range
COMPUTE_LIMIT = 5

def main():
    # Validate global variable
    if not isinstance(COMPUTE_LIMIT, int) or COMPUTE_LIMIT < 0:
        print("Failure: COMPUTE_LIMIT must be a non-negative integer")
        exit(1)

    # Perform computation dependent on global variable
    result = sum(i * i for i in range(COMPUTE_LIMIT))

    # Print success message
    print("Success")

    # Exit with code 0
    exit(0)

if __name__ == "__main__":
    main()

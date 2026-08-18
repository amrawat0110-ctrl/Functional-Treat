# Project: Functional Treat - Data Analyzer and Transformer Program

# Global variable to store dataset summary/status across operations
global_dataset = []


def display_data_summary(*args):
    """
    Displays summary statistics of the dataset using built-in functions.
    Demonstrates built-in functions (len, min, max, sum) and *args.
    """
    if not global_dataset:
        print("No data available! Please input data first.")
        return

    total_elements = len(global_dataset)
    min_val = min(global_dataset)
    max_val = max(global_dataset)
    sum_vals = sum(global_dataset)
    avg_val = sum_vals / total_elements

    print("\nData Summary:")
    print(f"- Total elements: {total_elements}")
    print(f"- Minimum value: {min_val}")
    print(f"- Maximum value: {max_val}")
    print(f"- Sum of all values: {sum_vals}")
    print(f"- Average value: {avg_val:.2f}")


def calculate_factorial(n):
    """
    Calculates the factorial of a given non-negative integer using recursion.
    """
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)


def get_dataset_stats(**kwargs):
    """
    Calculates and returns multiple dataset statistics.
    Demonstrates returning multiple values and accepting **kwargs for metadata display.
    """
    if not global_dataset:
        return None, None, None, None

    min_val = min(global_dataset)
    max_val = max(global_dataset)
    sum_vals = sum(global_dataset)
    avg_val = sum_vals / len(global_dataset)

    # Returning multiple values as a tuple
    return min_val, max_val, sum_vals, avg_val


def main_menu():
    """
    Main function providing menu interaction and calling appropriate functions.
    """
    global global_dataset

    print("Welcome to the Data Analyzer and Transformer Program")

    while True:
        print("\nMain Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")

        choice = input("Please enter your choice: ").strip()

        if choice == "1":
            print("\nPlease enter your choice: 1")
            user_input = input(
                "\nEnter data for a 1D array (separated by spaces):\n"
            )
            global_dataset = [int(x) for x in user_input.split()]
            print("\nData has been stored successfully!")

        elif choice == "2":
            print("\nPlease enter your choice: 2")
            display_data_summary()

        elif choice == "3":
            print("\nPlease enter your choice: 3")
            num = int(
                input("\nEnter a number to calculate its factorial: ")
            )
            result = calculate_factorial(num)
            print(f"\nFactorial of {num} is: {result}")

        elif choice == "4":
            print("\nPlease enter your choice: 4")
            threshold = int(
                input(
                    "\nEnter a threshold value to filter out data above this value:\n"
                )
            )

            # Applying Lambda Function with filter()
            filtered_data = list(
                filter(lambda x: x >= threshold, global_dataset)
            )

            formatted_output = ", ".join(map(str, filtered_data))
            print(f"\nFiltered Data (values >= {threshold}):")
            print(formatted_output)

        elif choice == "5":
            print("\nPlease enter your choice: 5")
            print("\nChoose sorting option:")
            print("1. Ascending")
            print("2. Descending")

            sort_choice = input("\nEnter your choice: ").strip()

            if sort_choice == "1":
                # In-place sorting using sort()
                sorted_list = sorted(global_dataset)
                print("\nSorted Data in Ascending Order:")
                print(", ".join(map(str, sorted_list)))
            elif sort_choice == "2":
                sorted_list = sorted(global_dataset, reverse=True)
                print("\nSorted Data in Descending Order:")
                print(", ".join(map(str, sorted_list)))

        elif choice == "6":
            print("\nPlease enter your choice: 6")
            min_v, max_v, sum_v, avg_v = get_dataset_stats()

            if min_v is not None:
                print("\nDataset Statistics:")
                print(f"- Minimum value: {min_v}")
                print(f"- Maximum value: {max_v}")
                print(f"- Sum of all values: {sum_v}")
                print(f"- Average value: {avg_v:.2f}")

        elif choice == "7":
            print("\nPlease enter your choice: 7")
            print(
                "\nThank you for using the Data Analyzer and Transformer Program. Goodbye!"
            )
            break
        else:
            print("\nInvalid choice. Please choose an option between 1 and 7.")


if __name__ == "__main__":
    main_menu()



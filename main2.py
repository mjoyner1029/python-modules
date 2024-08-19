# main2.py
import text_utils as tu

def main():
    """Main function to demonstrate string manipulation using text_utils module."""
    sample_string = "hello world"

    reversed_string = tu.reverse_string(sample_string)
    capitalized_string = tu.capitalize_string(sample_string)

    print(f"Original String: {sample_string}")
    print(f"Reversed String: {reversed_string}")
    print(f"Capitalized String: {capitalized_string}")

if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""File Processor Script.

Reads a user-specified text file, converts its content to lowercase,
and writes the modified content to a new file.
Handles common I/O errors gracefully.
"""


def process_file():
    """Process the file input by the user."""
    filename = input("Enter the filename to read from (e.g., input.txt): ")

    try:
        with open(filename, 'r', encoding='utf-8') as infile:
            content = infile.read()

        modified_content = content.lower()
        output_filename = f"modified_{filename}"

        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(modified_content)

        print(f"✅ File processed successfully. Output saved to '{output_filename}'.")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except IOError:
        print("❌ Error: Could not read or write to the file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


if __name__ == "__main__":
    process_file()

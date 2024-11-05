#!/usr/bin/env python3

import sys
import os


def main():
    # Check if the number of arguments is less than 2
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    # Assign the arguments to variables
    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Convert Markdown to HTML (dummy implementation)
    with open(markdown_file, 'r') as md_file:
        markdown_content = md_file.read()

    html_content = markdown_content  # This is a placeholder for actual conversion logic

    # Write the HTML content to the output file
    with open(output_file, 'w') as out_file:
        out_file.write(html_content)

    # If all checks pass, print nothing and exit with status 0
    sys.exit(0)


if __name__ == "__main__":
    main()

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


def extract_epub_text(epub_path, output_path):
    # Load the EPUB file
    book = epub.read_epub(epub_path)

    # Initialize an empty list to hold the text content
    full_text = []

    # Iterate through each item in the EPUB
    for item in book.get_items():
        # We're only interested in documents of type 'text'
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            # Parse the item's content with BeautifulSoup
            soup = BeautifulSoup(item.get_body_content(), "html.parser")

            # Extract the text and append it to the list
            full_text.append(soup.get_text())

    # Join all the extracted text into a single string
    text_content = "\n".join(full_text)

    # Write the extracted text to the output file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text_content)


# get the filename from command line
if __name__ == "__main__":
    import sys

    epub_path = sys.argv[1]
    output_path = sys.argv[2]
    # epub_path and output_path should be mandatory, if any of them is missing, it will raise an error
    if not epub_path or not output_path:
        raise ValueError("epub_path and output_path are mandatory")

    extract_epub_text(epub_path, output_path)

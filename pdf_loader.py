# pdf_loader.py
import fitz  # PyMuPDF
import io


def load_pdf(file) -> str:
    """
    Load and extract text from a PDF file or file-like object.

    Args:
        file: A file-like object (e.g., from Streamlit) or path to the PDF file.

    Returns:
        List[str]: A list of strings, each representing a segment of text extracted from the PDF.
    """
    text = ""

    # If the file is a file-like object (such as from Streamlit), we handle it differently
    if isinstance(file, io.BytesIO):
        pdf_document = fitz.open(stream=file.read(), filetype="pdf")
    else:
        # If it's a file path, just open it
        pdf_document = fitz.open(file)

    # Iterate through each page and extract text
    for page in pdf_document:
        text += page.get_text() + "\n"  # Add a newline for separation

    pdf_document.close()

    # Split the text into segments (you can adjust the splitting logic as needed)
    return text.split('\n')  # Return a list of text segments

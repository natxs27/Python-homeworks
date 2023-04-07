import os

def find_pdf_size(top):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(top):
        for filename in filenames:
            if filename.endswith('.pdf'):
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
    return total_size

# Example usage:
pdf_size = find_pdf_size('.')
print(f"Total size of PDF files in current directory: {pdf_size} bytes.")

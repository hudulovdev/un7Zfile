import py7zr

def extract_7z(file_path, output_dir):
    with py7zr.SevenZipFile(file_path, mode='r') as archive:
        archive.extractall(path=output_dir)

# Example usage:
file_path = 'archive.7z'
output_dir = 'extracted_files'

extract_7z(file_path, output_dir)

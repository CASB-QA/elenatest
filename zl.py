import zlib  # A compression / decompression library
filename = '.git/objects/ff/0d56a803ad61b6ab8e89a290bedee0114848bc'
compressed_contents = open(filename, 'rb').read()
decompressed_contents = zlib.decompress(compressed_contents)
print(decompressed_contents)


# import gzip
# with gzip.open('./compressed_file.gz', 'rb') as f:
#     file_content = f.read()
# print(file_content)

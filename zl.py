import zlib  # A compression / decompression library
filename = '.git/objects/pack/pack-6d3fb0a6e8c5b3e78b33375e19faf131f23a7f9f.idx'
compressed_contents = open(filename, 'rb').read()
decompressed_contents = zlib.decompress(compressed_contents)
print(decompressed_contents)


# import gzip
# with gzip.open('./compressed_file.gz', 'rb') as f:
#     file_content = f.read()
# print(file_content)

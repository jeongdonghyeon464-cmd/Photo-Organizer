from metadata import MetadataReader

reader = MetadataReader()

files = [
    r"test_data\IMG_0913.JPG",
    r"test_data\IMG_0193.JPG",
]

for file in files:
    print("=" * 50)
    print(file)

    result = reader.get_date(file)

    print(result)
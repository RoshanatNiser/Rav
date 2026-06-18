from spectral_data_file_reader import *

import os

dir_path = r"C:\Users\ro\Downloads\Ravita\data"
all_files = []

for root, dirs, files in os.walk(dir_path):
    for file in files:
        # Join the root directory with the filename to get the full absolute path
        full_path = os.path.join(root, file)
        all_files.append(full_path)

if not all_files:
    raise FileNotFoundError(f"No files found in {dir_path}")

print(all_files[0])

for i in range(0, len(all_files)):
    r = parse_spectral_file(all_files[i])
    plot_spectral_data(r)
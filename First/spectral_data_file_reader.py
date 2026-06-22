import os
import json
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import matplotlib.pyplot as plt


def parse_spectral_file(
    file_path, output_dict="C:\\Users\\ro\\Downloads\\Ravita\\data base"
):
    """Parses a single spectral file, converts it into a structured nested dictionary,

    and saves it as a JSON file with a matching name in the output directory.
    """
    spectral_dict = {
        "meta data": {},
        "data": {"wavelength": [], "reflectance": []},
    }

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        is_data_section = False
        unstructured_meta_count = 1

        for line in file:
            line_str = line.strip()
            if not line_str:
                continue

            parts = line_str.split()
            if len(parts) == 2:
                try:
                    wavelength = float(parts[0])
                    reflectance = float(parts[1])
                    spectral_dict["data"]["wavelength"].append(wavelength)
                    spectral_dict["data"]["reflectance"].append(reflectance)
                    is_data_section = True
                    continue
                except ValueError:
                    pass

            if not is_data_section:
                if ":" in line_str:
                    key, value = line_str.split(":", 1)
                    spectral_dict["meta data"][key.strip()] = value.strip()
                elif "=" in line_str and not (
                    "xmin" in line_str and "xmax" in line_str
                ):
                    key, value = line_str.split("=", 1)
                    spectral_dict["meta data"][key.strip()] = value.strip()
                else:
                    spectral_dict["meta data"][
                        f"info_line_{unstructured_meta_count}"
                    ] = line_str
                    unstructured_meta_count += 1

    # --- Saving to JSON with a similar name ---
    # Ensure the output directory exists
    os.makedirs(output_dict, exist_ok=True)

    # Extract the original file name without its extension (e.g., 'sample.txt' -> 'sample')
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    # Construct the full output path for the JSON file
    json_file_name = f"{base_name}.json"
    output_path = os.path.join(output_dict, json_file_name)

    # Save the dictionary as a formatted JSON file
    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(spectral_dict, json_file, indent=4)

    print(f"Successfully saved JSON to: {output_path}")

    return spectral_dict


def plot_spectral_data(
    spectral_dict,
    output_dict="C:\\Users\\ro\\Downloads\\Ravita\\spectrum_plots",
):
    """
    Takes the spectral dictionary (as returned by parse_spectral_file) and
    plots Wavelength vs Reflectance, saving the figure to output_dict.
    """
    # Extract data from the dictionary lists
    wavelengths = spectral_dict["data"]["wavelength"]
    reflectances = spectral_dict["data"]["reflectance"]

    # Try to extract the organism name from metadata for a dynamic plot title
    organism_name = spectral_dict["meta data"].get("info_line_1", "Agrococcus sp.")

    # Generate the plot using subplots to avoid layout truncation
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the spectral line
    ax.plot(wavelengths, reflectances, color="teal", linewidth=1.5, label="Reflectance Curve")

    # Add title and labels with appropriate formatting
    ax.set_title(f"Reflectance Spectrum of {organism_name}", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel(r"Wavelength ($\text{nm}$)", fontsize=12)
    ax.set_ylabel("Reflectance", fontsize=12)

    # Aesthetic enhancements
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend(loc="upper right")

    # Adjust layout to prevent label cropping
    plt.tight_layout()

    # Ensure the output directory exists
    os.makedirs(output_dict, exist_ok=True)

    # Sanitize the organism name so it's safe to use as a filename, then
    # build the full path (savefig has no "path" kwarg, so this must be
    # done manually) and add the .png extension.
    safe_name = re.sub(r'[\\/:*?"<>|]', "_", organism_name).strip()
    output_path = os.path.join(output_dict, f"{safe_name}.png")

    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Plot successfully saved to {output_path}")


'''
# --- Execution Pipeline ---
if __name__ == "__main__":
    # Step 1: Download target text files into 'data/' using specific pattern filtering
    download_spectral_files()

    # Step 2: Extract, build dictionaries, and serialize database profiles into 'data base/'
    process_and_create_database()


# step 3: Graph the data using the hand-off dictionary
plot_spectral_data(spectral_data, output_filename="agrococcus_spectrum.png")

'''

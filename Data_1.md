# McMurdo Dry Valleys LTER — Microbial Mats & Mosses Database

**File:** `mcm_5500_database.json`  
**Package ID:** knb-lter-mcm.5500.3  
**Built:** 2026-06-22  
**Contact:** im@mcmlter.org

---

## What This Is

This JSON database contains spectral and biological measurements of microbial mats and mosses collected across **Fryxell Basin, Taylor Valley, Antarctica** during the 2018–2019 field season. It was assembled from the McMurdo Dry Valleys Long-Term Ecological Research (MCM LTER) program, one of the longest-running ecological monitoring efforts in Antarctica.

The data captures how different mat communities — cyanobacterial mats, mosses, and mixed assemblages — reflect light and what pigments and biomass they contain. This kind of data is used to study how Antarctic microbial communities survive extreme cold, desiccation, and UV exposure, and to develop remote sensing methods that can map these communities from satellites or aircraft.

**Sampling sites** span nine streams in the Fryxell Basin:

- Bowles Creek
- Canada Stream
- Commonwealth Stream
- Crescent Stream
- Huey Creek
- Lost Seal Stream
- McKnight Creek
- Relict Channel
- Von Guerard Stream

**Mat types** sampled include: black, green, orange, red, tan, moss, and mixed assemblages (e.g. `moss/black`, `black/red/orange`).

**Moisture conditions** at time of collection: `dry`, `saturated`, `inundated`.

---

## Database Structure

The file is a single JSON object with two top-level keys:

```
mcm_5500_database.json
├── metadata        ← dataset-level info (title, creators, dates)
└── tables          ← the 6 data tables
    ├── dt1_sample_metadata
    ├── dt2_biomass
    ├── dt3_hplc_per_area
    ├── dt4_hplc_per_mass
    ├── dt5_spectral_vis
    └── dt6_spectral_swir
```

Each table object contains:

| Field | Description |
|---|---|
| `description` | Plain-language summary of the table |
| `source_url` | Original EDI repository URL |
| `row_count` | Number of records |
| `column_count` | Number of fields |
| `columns` | Ordered list of field names |
| `numeric_summary` | Descriptive stats (count, mean, std, min, max) for numeric fields |
| `records` | Array of row objects — one dict per sample |

Missing values are stored as `null`. Dates are ISO 8601 strings (e.g. `"2018-12-08T00:00:00"`).

The **`unique_id`** field (e.g. `LSS_20181208_P1_SP01_M_dry`) encodes site, date, plot, subplot, mat type, and moisture condition — it is the primary key that links records across tables.

---

## Table Reference

### `dt1_sample_metadata` — 370 rows

The master sample log. Every collected sample appears here with its full spatial and contextual metadata.

Key fields:

| Field | Description |
|---|---|
| `unique_id` | Primary key, links to all other tables |
| `date_collected` | ISO date of field collection |
| `stream_name` | Named stream or channel |
| `site_id` | Station code (e.g. `LSS`, `CAN`) |
| `plot_id` | Plot within site (e.g. `P1`, `P2`) |
| `subplot_id` | Subplot within plot |
| `mat_type` | Visual mat classification |
| `moisture_content` | `dry`, `saturated`, or `inundated` |
| `latitude` / `longitude` | Decimal degrees (WGS84) |
| `data_type` | `bio` (biological) or `spectral` |
| `sample_type` | Whether sample was archived, filtered, etc. |
| `spectral_id` | Links to spectral tables (dt5/dt6) |

---

### `dt2_biomass` — 225 rows

Biomass measurements from physical lab analysis of mat cores.

| Field | Unit | Mean | Range |
|---|---|---|---|
| `afdm_mg_cm2` | mg ash-free dry mass / cm² | 31.9 | 1.7 – 198.9 |
| `chl_a` | µg chlorophyll-a / cm² | 10.0 | 0.0 – 50.3 |

Ash-free dry mass (AFDM) is a measure of total organic matter. Chlorophyll-a indicates photosynthetic biomass.

---

### `dt3_hplc_per_area` — 56 rows

Pigment concentrations measured by High-Performance Liquid Chromatography (HPLC), expressed per unit **area** (µg/cm²). Provides a community-level snapshot of pigment composition.

Contains 22 individual pigments including:

| Pigment | Column | Ecological significance |
|---|---|---|
| Chlorophyll-a | `chla_440nm_ug_cm2` | Primary photosynthetic pigment |
| Chlorophyll-b | `chlb_440nm_ug_cm2` | Green algae and mosses |
| Total chlorophyll | `chltot_440nm_ug_cm2` | Sum of all chlorophylls |
| Scytonemin | `scy_388nm_ug_cm2` | UV-protective pigment in cyanobacteria |
| Scytonemin (reduced) | `scyred_388nm_ug_cm2` | Reduced form of scytonemin |
| Fucoxanthin | `fuco_440nm_ug_cm2` | Diatom indicator |
| Zeaxanthin | `zeaxan_440nm_ug_cm2` | Cyanobacteria photoprotection |
| Myxoxanthophyll | `myxo_440nm_ug_cm2` | Cyanobacteria-specific carotenoid |

All pigment columns follow the naming pattern: `{pigment}_{detection_wavelength}nm_ug_cm2`.

---

### `dt4_hplc_per_mass` — 56 rows

Identical pigment measurements to dt3, but expressed per unit **dry mass** (µg/g). Use this table when comparing across samples with different mat thicknesses or densities. Column names follow the pattern `{pigment}_{wavelength}nm_ug_g`.

---

### `dt5_spectral_vis` — 453,861 rows

Hyperspectral reflectance in the **visible and near-infrared range (350–2500 nm)**. Each sample has hundreds of band measurements, one row per band. This is the largest table by far.

| Field | Description |
|---|---|
| `spectral_id` | Instrument scan identifier |
| `band_nm` | Wavelength in nanometers |
| `reflectance` | Fraction of incident light reflected (0–1) |

To reconstruct a full spectrum for one sample, filter by `unique_id` or `spectral_id` and sort by `band_nm`.

---

### `dt6_spectral_swir` — 1,688 rows

Multispectral reflectance in the **shortwave infrared range (0.427–0.908 µm)**. Fewer bands than dt5, measured with a different instrument. Band wavelengths are in micrometers (`band_um`).

---

## How to Use

### Load in Python

```python
import json

with open("mcm_5500_database.json") as f:
    db = json.load(f)

# Access a table's records
records = db["tables"]["dt2_biomass"]["records"]

# Convert to a pandas DataFrame
import pandas as pd
df = pd.DataFrame(records)
```

### Join tables by unique_id

```python
meta = pd.DataFrame(db["tables"]["dt1_sample_metadata"]["records"])
biomass = pd.DataFrame(db["tables"]["dt2_biomass"]["records"])

merged = biomass.merge(meta[["unique_id", "latitude", "longitude", "stream_name"]],
                       on="unique_id", how="left")
```

### Reconstruct a reflectance spectrum

```python
vis = pd.DataFrame(db["tables"]["dt5_spectral_vis"]["records"])

# Get one spectrum
spectrum = vis[vis["unique_id"] == "CAN_20181212_P1_A_dry_81"].sort_values("band_nm")

import matplotlib.pyplot as plt
plt.plot(spectrum["band_nm"], spectrum["reflectance"])
plt.xlabel("Wavelength (nm)")
plt.ylabel("Reflectance")
plt.title("Visible spectrum — Canada Stream, moss/black mat")
plt.show()
```

### Filter by mat type and moisture

```python
df = pd.DataFrame(db["tables"]["dt1_sample_metadata"]["records"])

# Dry moss samples only
dry_moss = df[(df["mat_type"] == "moss") & (df["moisture_content"] == "dry")]
```

### Load in JavaScript / Node.js

```javascript
const fs = require("fs");
const db = JSON.parse(fs.readFileSync("mcm_5500_database.json", "utf8"));

const records = db.tables.dt2_biomass.records;
const highBiomass = records.filter(r => r.afdm_mg_cm2 > 50);
```

---

## Key Relationships Between Tables

```
dt1_sample_metadata  ──── unique_id ────►  dt2_biomass
                     ──── unique_id ────►  dt3_hplc_per_area
                     ──── unique_id ────►  dt4_hplc_per_mass
                     ──── unique_id ────►  dt5_spectral_vis
                     ──── unique_id ────►  dt6_spectral_swir

dt3_hplc_per_area    ──── sample_id ────►  dt2_biomass
dt4_hplc_per_mass    ──── sample_id ────►  dt2_biomass
```

The `unique_id` is human-readable and encodes sampling context:
`{SITE}_{DATE}_{PLOT}_{SUBPLOT}_{MAT_ID}_{MOISTURE}`

Example: `LSS_20181208_P1_SP01_M_dry` = Lost Seal Stream, 2018-12-08, Plot 1, Subplot 01, mat M, dry.

---

## Creators

Schuyler Borges, Lee Stanish, Sarah Power, Mark Salvatore, John "Jeb" Barrett, Eric Sokol, M. Davis

**Program:** McMurdo Dry Valleys Long-Term Ecological Research (MCM LTER)  
**Original data repository:** https://pasta.edirepository.org  
**Package ID:** knb-lter-mcm.5500.3
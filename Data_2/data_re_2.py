"""
McMurdo Dry Valleys LTER - Microbial Mats & Mosses Database Builder
Dataset: knb-lter-mcm.5500.3
Fryxell Basin, Taylor Valley, Antarctica (2018-2019)

Fetches all 6 data tables from the EDI repository and saves them
as a structured JSON database file.

Output: mcm_5500_database.json
"""

import numpy as np
import pandas as pd
import json
import sys
from datetime import datetime

# ── URLs ──────────────────────────────────────────────────────────────────────
TABLES = {
    "dt1_sample_metadata": {
        "url": "http://pasta.lternet.edu/package/data/eml/knb-lter-mcm/5500/3/103cfd6d96e9c7e411d7630de4b839da",
        "description": "Sample collection metadata (location, mat type, IDs)",
        "columns": [
            "dataset_code", "unique_id", "date_collected", "time_collected",
            "stream_name", "site_id", "plot_id", "subplot_id", "mat_type",
            "mat_id", "moisture_content", "data_type", "latitude", "longitude",
            "sample_name", "sample_id", "sample_type", "number_of_cores",
            "spectral_id", "photo_id", "sample_description",
            "filtering_remarks", "freezer_remarks"
        ],
        "numeric_cols": [],
        "date_cols": ["date_collected", "time_collected"],
    },
    "dt2_biomass": {
        "url": "http://pasta.lternet.edu/package/data/eml/knb-lter-mcm/5500/3/ee60d7ffb4334af076e1f1cdce4dba77",
        "description": "Biomass measurements: ash-free dry mass (AFDM) and chlorophyll-a",
        "columns": [
            "dataset_code", "unique_id", "sample_id", "date_collected",
            "stream_name", "site_id", "plot_id", "subplot_id", "mat_type",
            "moisture_content", "afdm_mg_cm2", "chl_a", "biomass_remarks"
        ],
        "numeric_cols": ["afdm_mg_cm2", "chl_a"],
        "date_cols": ["date_collected"],
    },
    "dt3_hplc_per_area": {
        "url": "http://pasta.lternet.edu/package/data/eml/knb-lter-mcm/5500/3/c147dc5c157f2d1310dd3341c3f25cd8",
        "description": "HPLC pigment concentrations per unit area (ug/cm²)",
        "columns": [
            "dataset_code", "unique_id", "sample_id", "date_collected",
            "stream_name", "plot_id", "subplot_id", "mat_type", "moisture_content",
            "allo_440nm_ug_cm2", "anthera_440nm_ug_cm2", "beta_440nm_ug_cm2",
            "butan_440nm_ug_cm2", "cantha_440nm_ug_cm2", "chla_440nm_ug_cm2",
            "chlb_440nm_ug_cm2", "chlc1c2_440nm_ug_cm2", "chlda_440nm_ug_cm2",
            "chltot_440nm_ug_cm2", "diadin_440nm_ug_cm2", "diato_440nm_ug_cm2",
            "echine_440nm_ug_cm2", "fuco_440nm_ug_cm2", "gyroxan_440nm_ug_cm2",
            "hexan_440nm_ug_cm2", "lutein_440nm_ug_cm2", "myxo_440nm_ug_cm2",
            "neoxan_440nm_ug_cm2", "scy_388nm_ug_cm2", "scyred_388nm_ug_cm2",
            "viola_440nm_ug_cm2", "zeaxan_440nm_ug_cm2",
            "hplc_file_id", "hplc_remarks"
        ],
        "numeric_cols": [
            "allo_440nm_ug_cm2", "anthera_440nm_ug_cm2", "beta_440nm_ug_cm2",
            "butan_440nm_ug_cm2", "cantha_440nm_ug_cm2", "chla_440nm_ug_cm2",
            "chlb_440nm_ug_cm2", "chlc1c2_440nm_ug_cm2", "chlda_440nm_ug_cm2",
            "chltot_440nm_ug_cm2", "diadin_440nm_ug_cm2", "diato_440nm_ug_cm2",
            "echine_440nm_ug_cm2", "fuco_440nm_ug_cm2", "gyroxan_440nm_ug_cm2",
            "hexan_440nm_ug_cm2", "lutein_440nm_ug_cm2", "myxo_440nm_ug_cm2",
            "neoxan_440nm_ug_cm2", "scy_388nm_ug_cm2", "scyred_388nm_ug_cm2",
            "viola_440nm_ug_cm2", "zeaxan_440nm_ug_cm2"
        ],
        "date_cols": ["date_collected"],
    },
    "dt4_hplc_per_mass": {
        "url": "http://pasta.lternet.edu/package/data/eml/knb-lter-mcm/5500/3/7540e93df6403cae41f13a2954f2fa4f",
        "description": "HPLC pigment concentrations per unit mass (ug/g dry weight)",
        "columns": [
            "dataset_code", "unique_id", "sample_id", "date_collected",
            "stream_name", "plot_id", "subplot_id", "mat_type", "moisture_content",
            "allo_440nm_ug_g", "anthera_440nm_ug_g", "beta_440nm_ug_g",
            "butan_440nm_ug_g", "cantha_440nm_ug_g", "chla_440nm_ug_g",
            "chlb_440nm_ug_g", "chlc1c2_440nm_ug_g", "chlda_440nm_ug_g",
            "chltot_440nm_ug_g", "diadin_440nm_ug_g", "diato_440nm_ug_g",
            "echine_440nm_ug_g", "fuco_440nm_ug_g", "gyroxan_440nm_ug_g",
            "hexan_440nm_ug_g", "lutein_440nm_ug_g", "myxo_440nm_ug_g",
            "neoxan_440nm_ug_g", "scy_388nm_ug_g", "scyred_388nm_ug_g",
            "viola_440nm_ug_g", "zeaxan_440nm_ug_g",
            "hplc_file_id", "hplc_remarks"
        ],
        "numeric_cols": [
            "allo_440nm_ug_g", "anthera_440nm_ug_g", "beta_440nm_ug_g",
            "butan_440nm_ug_g", "cantha_440nm_ug_g", "chla_440nm_ug_g",
            "chlb_440nm_ug_g", "chlc1c2_440nm_ug_g", "chlda_440nm_ug_g",
            "chltot_440nm_ug_g", "diadin_440nm_ug_g", "diato_440nm_ug_g",
            "echine_440nm_ug_g", "fuco_440nm_ug_g", "gyroxan_440nm_ug_g",
            "hexan_440nm_ug_g", "lutein_440nm_ug_g", "myxo_440nm_ug_g",
            "neoxan_440nm_ug_g", "scy_388nm_ug_g", "scyred_388nm_ug_g",
            "viola_440nm_ug_g", "zeaxan_440nm_ug_g"
        ],
        "date_cols": ["date_collected"],
    },
    "dt5_spectral_vis": {
        "url": "http://pasta.lternet.edu/package/data/eml/knb-lter-mcm/5500/3/d23786fa1139cc2222262575d4c9382e",
        "description": "Visible spectral reflectance (band in nanometers)",
        "columns": [
            "dataset_code", "unique_id", "spectral_id", "date_collected",
            "stream_name", "plot_id", "subplot_id", "mat_type",
            "moisture_content", "band_nm", "reflectance"
        ],
        "numeric_cols": ["band_nm"],
        "date_cols": ["date_collected"],
    },
    "dt6_spectral_swir": {
        "url": "http://pasta.lternet.edu/package/data/eml/knb-lter-mcm/5500/3/f56637013d430419b448de22dcde119b",
        "description": "Shortwave infrared spectral reflectance (band in micrometers)",
        "columns": [
            "dataset_code", "unique_id", "spectral_id", "date_collected",
            "stream_name", "plot_id", "subplot_id", "mat_type",
            "moisture_content", "band_um", "reflectance"
        ],
        "numeric_cols": ["band_um"],
        "date_cols": ["date_collected"],
    },
}


def safe_val(v):
    """Convert numpy / NaN values to JSON-safe Python types."""
    if v is None:
        return None
    if isinstance(v, float) and np.isnan(v):
        return None
    if isinstance(v, (np.integer,)):
        return int(v)
    if isinstance(v, (np.floating,)):
        return float(v)
    if isinstance(v, pd.Timestamp):
        return v.isoformat() if not pd.isnull(v) else None
    return v


def compute_summary(df, numeric_cols):
    """Return basic descriptive stats for numeric columns."""
    summary = {}
    for col in numeric_cols:
        if col in df.columns:
            s = df[col].dropna()
            summary[col] = {
                "count": int(s.count()),
                "mean":  round(float(s.mean()), 6) if len(s) else None,
                "std":   round(float(s.std()),  6) if len(s) else None,
                "min":   round(float(s.min()),  6) if len(s) else None,
                "max":   round(float(s.max()),  6) if len(s) else None,
            }
    return summary


def fetch_table(name, meta):
    print(f"  Fetching {name} ...", end=" ", flush=True)
    df = pd.read_csv(
        meta["url"],
        storage_options={"User-Agent": "EDI_CodeGen"},
        skiprows=1,
        sep=",",
        quotechar='"',
        names=meta["columns"],
        parse_dates=meta["date_cols"],
    )

    # Coerce numeric columns
    for col in meta["numeric_cols"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    print(f"{len(df):,} rows, {len(df.columns)} cols")
    return df


def df_to_records(df):
    """Convert DataFrame rows to a list of clean dicts."""
    records = []
    for row in df.itertuples(index=False):
        record = {col: safe_val(getattr(row, col)) for col in df.columns}
        records.append(record)
    return records


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print("=" * 60)
    print("McMurdo Dry Valleys LTER — Database Builder")
    print("Dataset: knb-lter-mcm.5500.3")
    print("=" * 60)

    database = {
        "metadata": {
            "package_id":   "knb-lter-mcm.5500.3",
            "title":        "Spectral and biological characteristics of microbial mats and mosses across Fryxell Basin, Taylor Valley, Antarctica (2018-2019)",
            "creators":     ["Schuyler Borges", "Lee Stanish", "Sarah Power",
                             "Mark Salvatore", "John 'Jeb' Barrett",
                             "Eric Sokol", "M. Davis"],
            "contact":      "im@mcmlter.org",
            "catalog_url":  "https://pasta.edirepository.org",
            "built_at":     datetime.utcnow().isoformat() + "Z",
        },
        "tables": {}
    }

    for name, meta in TABLES.items():
        try:
            df = fetch_table(name, meta)
            records = df_to_records(df)
            summary = compute_summary(df, meta["numeric_cols"])

            database["tables"][name] = {
                "description":   meta["description"],
                "source_url":    meta["url"],
                "row_count":     len(df),
                "column_count":  len(df.columns),
                "columns":       list(df.columns),
                "numeric_summary": summary,
                "records":       records,
            }

        except Exception as e:
            print(f"  ERROR fetching {name}: {e}", file=sys.stderr)
            database["tables"][name] = {
                "description": meta["description"],
                "source_url":  meta["url"],
                "error":       str(e),
                "records":     [],
            }

    # ── Write JSON ────────────────────────────────────────────────────────────
    out_path = "mcm_5500_database.json"
    print(f"\nWriting database to {out_path} ...", end=" ", flush=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(database, f, indent=2, ensure_ascii=False, default=str)
    print("done.")

    # ── Quick summary ─────────────────────────────────────────────────────────
    print("\n── Summary ──────────────────────────────────────────────")
    total_rows = sum(
        t.get("row_count", 0) for t in database["tables"].values()
    )
    for tname, tdata in database["tables"].items():
        status = f"{tdata.get('row_count', 0):>7,} rows" if "row_count" in tdata else "  FAILED"
        print(f"  {tname:<30} {status}")
    print(f"\n  Total records across all tables: {total_rows:,}")
    print(f"  Output file: {out_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()
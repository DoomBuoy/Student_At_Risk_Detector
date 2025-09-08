from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from student_at_risk_detector.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


# ...existing code...
@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    # Ensure RAW_DATA_DIR exists
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Download the dataset from Google Drive and save to RAW_DATA_DIR
    import gdown
    url = "https://drive.google.com/uc?id=18Yo5NWxoY5R4w2sWeNE0jLZ5Ey19P77W"
    output_file = RAW_DATA_DIR / "dataset.csv"
    logger.info(f"Downloading dataset from {url} to {output_file}...")
    gdown.download(url, str(output_file), quiet=False)
    logger.success("Download complete. File saved to raw data directory.")
# ...existing code...

if __name__ == "__main__":
    app()

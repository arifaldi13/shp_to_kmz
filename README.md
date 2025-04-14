# Shapefile to KMZ Web Converter

A simple web application built with Python and Flask that allows users to convert ESRI Shapefiles (`.shp`, `.shx`, `.dbf`) into a downloadable KMZ file suitable for use in Google Earth or Google Maps.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

*   **Web-based Interface:** Easy-to-use web UI for file upload (supports drag & drop and file selection).
*   **Shapefile Component Handling:** Accepts the essential `.shp`, `.shx`, and `.dbf` files required for processing.
*   **Core Conversion:** Uses the powerful `GeoPandas` library to read Shapefile geometry and attributes.
*   **KMZ Generation:** Employs the `SimpleKML` library to create structured KML data (points, lines, polygons) including attributes.
*   **KMZ Packaging:** Automatically saves the KML data into a compressed `.kmz` file.
*   **Direct Download:** Provides the generated KMZ file for download directly in the browser.
*   **Automatic Cleanup:** Removes temporary uploaded files and the generated output file from the server after the request.

## Requirements

*   **Python:** Version 3.7+ recommended.
*   **pip:** Python package installer (usually comes with Python).
*   **Required Python Libraries:** See `requirements.txt` file. Key libraries include:
    *   `Flask`
    *   `GeoPandas`
    *   `simplekml`
*   **External Dependencies (for GeoPandas):** GeoPandas relies on libraries like GDAL, Fiona, Shapely, etc. Installation can sometimes be complex depending on your operating system.
    *   **Recommendation:** Using a package manager like `conda` (especially via Miniconda or Anaconda) is often the easiest way to install GeoPandas and its dependencies correctly:
        ```bash
        conda create -n shp2kmz_env -c conda-forge python=3.9 geopandas simplekml flask
        conda activate shp2kmz_env
        ```

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/arifaldi13/shp_to_kmz.git
    cd shp_to_kmz
    ```

2.  **Create and activate a virtual environment (Recommended):**
    *   **Using `venv` (standard Python):**
        ```bash
        python -m venv venv
        # On Windows:
        .\venv\Scripts\activate
        # On macOS/Linux:
        source venv/bin/activate
        ```
    *   **Using `conda` (if you followed the conda recommendation above):**
        ```bash
        conda activate shp2kmz_env
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Skip this step if you used the `conda create` command above, as it installed the packages already).*

## Usage

1.  **Run the Flask application:**
    ```bash
    python app.py
    ```

2.  **Access the web interface:**
    Open your web browser and navigate to: `http://127.0.0.1:5000` (or the address provided in the terminal output).

3.  **Upload files:**
    *   Drag and drop your `.shp`, `.shx`, and `.dbf` files onto the designated area, OR
    *   Click the "Select Files" button and choose the required `.shp`, `.shx`, and `.dbf` files.

4.  **Convert:**
    Click the "Convert to KMZ" button.

5.  **Download:**
    If the conversion is successful, your browser will automatically prompt you to download the `output.kmz` file. Status messages will appear on the web page.

**Note:** The application runs with `debug=True` by default in `app.py`. This is helpful for development but should be turned off (`debug=False`) for any production deployment.

## Project Structure
```
.
├── app.py             # Main Flask application script
├── shptokmz.py        # Shapefile to KMZ conversion logic
├── requirements.txt   # Python package dependencies
├── templates/
│   └── index.html     # HTML template for the web interface
├── uploads/           # Temporary folder for uploaded files (created automatically)
├── outputs/           # Temporary folder for generated KMZ (created automatically)
├── .gitignore         # Specifies intentionally untracked files for Git
└── README.md          # This file
```

## License

This project is licensed under the MIT License - see the `LICENSE` file (you should create one!) for details. If you haven't added a `LICENSE` file, you can state: "This project is open source under the MIT License."

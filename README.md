# Manga Download

This project is designed to help users download manga efficiently. It provides tools and scripts to automate the process of fetching manga chapters from supported sources.

## Features

- Download manga chapters in bulk.
- Supports multiple manga sources.
- Easy-to-use interface.
- Customizable download settings.

## Requirements

- Python 3.7 or higher
- Required libraries (install via `requirements.txt`):
    - `requests`
    - `beautifulsoup4`
    - `lxml`

## Installation

1. Clone the repository:
     ```bash
     git clone https://github.com/Igboke/manga-donwloader.git
     ```
2. Navigate to the project directory:
     ```bash
     cd manga-downloader
     ```
3. Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

## Usage

```bash
command_line_downloader.py [-h] [--output OUTPUT] [--start-page START_PAGE] manga chapter
```

positional arguments:
  manga                 The name of the manga (e.g., "boruto_two_blue_vortex"). Get the name from mangafreak
  chapter               The chapter number to download (e.g., 20).

options:
  -h, --help            show help message
  --output OUTPUT, -o OUTPUT
                        Directory to save the downloaded chapter images. (default: .)
  --start-page START_PAGE, -s START_PAGE
                        The page number to start downloading from. (default: 1)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License



## Disclaimer

This tool is intended for personal use only. Ensure you comply with copyright laws and the terms of service of the manga sources you use.
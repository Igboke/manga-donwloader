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

- manga                 The name of the manga (e.g., "boruto_two_blue_vortex"). Get the name from mangafreak

- chapter               The chapter number to download (e.g., 20).

options:

- -h, --help            show help message
- --output OUTPUT, -o OUTPUT Directory to save the downloaded chapter images. (default: .)
- --start-page START_PAGE, -s START_PAGE The page number to start downloading from. (default: 1)

---

## Check for New Chapters

Use `check_new_chapter.py` to quickly check if a new chapter is available:

```bash
python check_new_chapter.py [-h] [--output OUTPUT] [--download] [--check-chapter CHECK_CHAPTER] manga
```

### Arguments

| Argument | Description |
|----------|-------------|
| `manga` | The name of the manga (e.g., `kingdom`, `kagura_bachi`) |
| `-o`, `--output` | Directory where chapters are saved (used to find last chapter). Default: `.` |
| `-d`, `--download` | Automatically download the new chapter if available |
| `-c`, `--check-chapter` | Manually specify which chapter to check (overrides auto-detection) |

### Examples

```bash
# Check if a new Kingdom chapter exists
python check_new_chapter.py kingdom -o kingdom_manga

# Check and auto-download if available
python check_new_chapter.py kagura_bachi -o kagura_bachi --download

# Manually check a specific chapter number
python check_new_chapter.py boruto_two_blue_vortex -c 25
```

### How It Works

1. Scans the output directory for existing chapter folders (e.g., `kingdom_chapter_650`)
2. Determines the highest chapter number you have
3. Makes a HEAD request to check if `last_chapter + 1` exists
4. Reports whether a new chapter is available (with exit code 0 if yes, 1 if no)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License



## Disclaimer

This tool is intended for personal use only. Ensure you comply with copyright laws and the terms of service of the manga sources you use.
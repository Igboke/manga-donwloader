import requests
import time
import random
import argparse
import os

def download_chapter(manga_name, chapter_num, output_dir=".", start_page=1):
    """
    Downloads a specified manga chapter page by page until a 404 is encountered.

    Args:
        manga_name (str): The name of the manga (used in the URL and filenames).
        chapter_num (int): The chapter number to download.
        output_dir (str): The directory to save the downloaded images. Defaults to current directory.
        start_page (int): The page number to start downloading from. Defaults to 1.
    """
    print(f"Attempting to download {manga_name} Chapter {chapter_num} starting from page {start_page}...")

    # Create the output directory if it doesn't exist
    chapter_dir = os.path.join(output_dir, f"{manga_name}_chapter_{chapter_num}")
    os.makedirs(chapter_dir, exist_ok=True)
    print(f"Saving images to: {chapter_dir}")


    # Loop through pages, starting from start_page
    for i in range(start_page, start_page + 200): # Try up to 200 pages
        page_num = str(i)
        base_url = f"https://images.mangafreak.me/mangas/{manga_name}/{manga_name}_{chapter_num}/{manga_name}_{chapter_num}_{page_num}.jpg"

        print(f"Checking URL: {base_url}")

        # Add a delay before making the request
        sleep_duration = random.uniform(1, 3)
        time.sleep(sleep_duration)

        try:
            # Using stream=True for memory efficiency when downloading images
            response = requests.get(base_url, stream=True)

            if response.status_code == 200:
                # Construct the local filename
                local_filename = os.path.join(chapter_dir, f"{manga_name}_{chapter_num}_{page_num}.jpg")
                print(f"Downloading page {page_num} to {local_filename}")

                # Write the image content to a local file in binary mode ('wb')
                with open(local_filename, "wb") as file:
                    for chunk in response.iter_content(1024):
                        if chunk:
                            file.write(chunk)
            elif response.status_code == 404:
                 print(f"Received 404 for page {page_num}. Assuming end of chapter.")
                 response.close()
                 break
            else:
                print(f"Failed to download image {base_url}. Status code: {response.status_code}")
                break

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while requesting {base_url}: {e}")
            break


    print(f"Finished attempting to download Chapter {chapter_num} of {manga_name}.")


def parse_chapters(chapter_arg):
    """
    Parses a chapter string which can be a single number, a comma-separated list,
    or a range (e.g., "1-5", "1,3,5", "1-3,5").
    Returns a sorted list of unique chapter numbers.
    """
    chapters = set()
    parts = chapter_arg.split(',')
    for part in parts:
        part = part.strip()
        if '-' in part:
            try:
                start, end = map(int, part.split('-'))
                chapters.update(range(start, end + 1))
            except ValueError:
                print(f"Warning: Invalid range format '{part}'. Skipping.")
        else:
            try:
                chapters.add(int(part))
            except ValueError:
                print(f"Warning: Invalid chapter number '{part}'. Skipping.")
    return sorted(list(chapters))

# 2. Setup argparse and call the main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Download manga chapters page by page from a specific site.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter # Shows default values in help
    )

    # Add arguments
    parser.add_argument(
        'manga',
        type=str,
        help='The name of the manga (e.g., "boruto_two_blue_vortex").'
    )

    parser.add_argument(
        'chapter',
        type=str, # Expect a string for the chapter range/list
        help='The chapter number(s) to download. Can be a single number (e.g., "20"), a range (e.g., "11-20"), or a list (e.g., "1,2,5").'
    )

    parser.add_argument(
        '--output', '-o',
        type=str,
        default='.', # Default to the current directory
        help='Directory to save the downloaded chapter images.'
    )

    parser.add_argument(
        '--start-page', '-s',
        type=int,
        default=1, # Default to starting from page 1
        help='The page number to start downloading from.'
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Parse the chapter argument into a list of integers
    chapters_to_download = parse_chapters(args.chapter)

    if not chapters_to_download:
        print("No valid chapters found to download.")
    else:
        print(f"Scheduled to download chapters: {chapters_to_download}")
        # Iterate over the parsed chapters and download each one
        for chapter_num in chapters_to_download:
            download_chapter(args.manga, chapter_num, args.output, args.start_page)
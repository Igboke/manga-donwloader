#!/usr/bin/env python3
"""
Check if a new manga chapter is available by looking at the last downloaded chapter
and checking if the next one exists on the server.
"""

import requests
import argparse
import os
import re
import sys

# Import the download function from the existing downloader
from command_line_downloader import download_chapter


def get_last_downloaded_chapter(manga_name, output_dir="."):
    """
    Scans the output directory for existing chapter folders and returns
    the highest chapter number found.
    
    Args:
        manga_name (str): The name of the manga.
        output_dir (str): The directory to scan for chapter folders.
    
    Returns:
        int or None: The highest chapter number found, or None if no chapters exist.
    """
    pattern = re.compile(rf"^{re.escape(manga_name)}_chapter_(\d+)$")
    
    max_chapter = None
    
    try:
        for item in os.listdir(output_dir):
            item_path = os.path.join(output_dir, item)
            if os.path.isdir(item_path):
                match = pattern.match(item)
                if match:
                    chapter_num = int(match.group(1))
                    if max_chapter is None or chapter_num > max_chapter:
                        max_chapter = chapter_num
    except FileNotFoundError:
        print(f"Warning: Output directory '{output_dir}' not found.")
        return None
    
    return max_chapter


def check_chapter_exists(manga_name, chapter_num):
    """
    Check if a specific chapter exists by making a HEAD request to the first page.
    
    Args:
        manga_name (str): The name of the manga.
        chapter_num (int): The chapter number to check.
    
    Returns:
        bool: True if the chapter exists, False otherwise.
    """
    # Check the first page of the chapter
    url = f"https://images.mangafreak.me/mangas/{manga_name}/{manga_name}_{chapter_num}/{manga_name}_{chapter_num}_1.jpg"
    
    try:
        # Use HEAD request - faster as it only fetches headers
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error checking chapter: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Check if a new manga chapter is available.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        'manga',
        type=str,
        help='The name of the manga (e.g., "boruto_two_blue_vortex").'
    )
    
    parser.add_argument(
        '--output', '-o',
        type=str,
        default='.',
        help='Directory where chapters are saved (used to find the last chapter).'
    )
    
    parser.add_argument(
        '--download', '-d',
        action='store_true',
        help='Automatically download the new chapter if available.'
    )
    
    parser.add_argument(
        '--check-chapter', '-c',
        type=int,
        default=None,
        help='Manually specify which chapter to check (overrides auto-detection).'
    )
    
    args = parser.parse_args()
    
    manga_name = args.manga
    output_dir = args.output
    
    # Determine which chapter to check
    if args.check_chapter is not None:
        next_chapter = args.check_chapter
        print(f"Manually checking chapter {next_chapter} for '{manga_name}'...")
    else:
        # Find the last downloaded chapter
        last_chapter = get_last_downloaded_chapter(manga_name, output_dir)
        
        if last_chapter is None:
            print(f"No existing chapters found for '{manga_name}' in '{output_dir}'.")
            print("Use --check-chapter to manually specify which chapter to check.")
            sys.exit(1)
        
        next_chapter = last_chapter + 1
        print(f"Last downloaded chapter: {last_chapter}")
        print(f"Checking if chapter {next_chapter} exists...")
    
    # Check if the next chapter exists
    exists = check_chapter_exists(manga_name, next_chapter)
    
    if exists:
        print(f"\n✅ NEW CHAPTER AVAILABLE! Chapter {next_chapter} is out!")
        
        if args.download:
            print(f"\nStarting download of chapter {next_chapter}...")
            download_chapter(manga_name, next_chapter, output_dir)
        else:
            print(f"\nRun the following to download:")
            print(f"  python command_line_downloader.py {manga_name} {next_chapter} -o {output_dir}")
        
        sys.exit(0)
    else:
        print(f"\n❌ Chapter {next_chapter} is not available yet.")
        sys.exit(1)


if __name__ == "__main__":
    main()

# Image Organizer

A simple Python script that automatically organizes image files by separating RAW and JPEG files into their respective folders.

## Features

- Automatically creates separate folders for RAW and JPEG images
- Supports multiple RAW formats (CR2, NEF, ARW, RW2, ORF)
- Supports JPEG formats (JPG, JPEG)
- Simple command-line interface

## Supported File Types

### RAW Formats
- `.cr2` (Canon)
- `.nef` (Nikon)
- `.arw` (Sony)
- `.rw2` (Panasonic)
- `.orf` (Olympus)

### JPEG Formats
- `.jpg`
- `.jpeg`

## Requirements

- Python 3.x

## Installation

1. Clone this repository or download the `image-organizer.py` file
2. No additional dependencies required - the script uses only Python standard library

## Usage

1. Run the script using Python:
   ```bash
   python image-organizer.py
   ```
2. When prompted, enter the full path to the directory containing your images:
   ```
   Enter the path to your images directory: C:/Users/bikal1000/Pictures/SheyPhoksundo2024
   # or on Mac/Linux
   Enter the path to your images directory: /home/bikal1000/Pictures/SheyPhoksundo2024
   ```
3. The script will:
   - Create two subdirectories: `raw` and `jpeg`
   - Move all RAW files to the `raw` folder
   - Move all JPEG files to the `jpeg` folder
   - Print the status of each moved file

## Directory Structure

After running the script, your directory will be organized as follows:
## Directory Structure

After running the script, your directory will be organized as follows:

```
your-directory/
├── raw/
│   ├── image1.cr2
│   └── image2.nef
└── jpeg/
    ├── image1.jpg
    └── image2.jpeg
```

## Note

- The script will only process files in the specified directory (not subdirectories)
- Existing files with the same name in destination folders may be overwritten
- Non-image files will be left in place

## License

This project is open source and available under the MIT License.

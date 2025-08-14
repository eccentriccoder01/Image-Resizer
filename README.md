# Image Resizer Tool

A Python script that automates batch image resizing and format conversion using PIL/Pillow.

## Features

- **Batch Processing**: Resize all images in a folder at once
- **Format Conversion**: Convert between different image formats (JPEG, PNG, WEBP, BMP, TIFF)
- **Flexible Sizing**: Customize width and height for resized images
- **Error Handling**: Robust error handling with detailed feedback
- **Multiple Format Support**: Supports JPG, JPEG, PNG, BMP, TIFF, WEBP, GIF
- **Command Line Interface**: Easy to use with command line arguments

## Requirements

- Python 3.6+
- Pillow (PIL Fork)

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd image-resizer-tool
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Resize all images in a folder to 800x600 pixels:

```bash
python image_resizer.py input_folder output_folder
```

### Custom Dimensions

Resize images to custom dimensions:

```bash
python image_resizer.py input_folder output_folder --width 1920 --height 1080
```

### Format Conversion

Resize and convert all images to PNG format:

```bash
python image_resizer.py input_folder output_folder --format PNG
```

### Combined Example

Resize to 500x500 and convert to JPEG:

```bash
python image_resizer.py photos resized_photos --width 500 --height 500 --format JPEG
```

## Command Line Arguments

- `input_folder`: Path to the folder containing images to resize
- `output_folder`: Path where resized images will be saved
- `--width`: Target width in pixels (default: 800)
- `--height`: Target height in pixels (default: 600)
- `--format`: Convert to specified format (JPEG, PNG, WEBP, BMP, TIFF)

## Supported Image Formats

**Input formats:**
- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff)
- WEBP (.webp)
- GIF (.gif)

**Output formats:**
- JPEG
- PNG
- WEBP
- BMP
- TIFF

## How It Works

1. **Directory Reading**: Uses `os` module to read all files in the input directory
2. **Image Processing**: Uses `PIL.Image` to open, resize, and save images
3. **Format Handling**: Automatically handles format conversions and color mode adjustments
4. **Error Management**: Uses try-except blocks to handle corrupted or unsupported files
5. **Batch Processing**: Processes all valid image files in the specified directory

## Key Concepts Demonstrated

- **File Handling**: Reading directories and managing file paths with `os` module
- **Image Processing**: Using PIL/Pillow for image manipulation
- **Error Handling**: Implementing robust error handling for file operations
- **Command Line Interface**: Using `argparse` for user-friendly CLI
- **Batch Operations**: Processing multiple files efficiently

## Example Output

```
Image Resizer Tool
Input folder: ./photos
Output folder: ./resized_photos
Target size: 800x600
--------------------------------------------------
Processing: IMG_001.jpg (Original size: (4032, 3024))
✓ Saved: IMG_001.jpg (New size: 800x600)
Processing: IMG_002.png (Original size: (1920, 1080))
✓ Saved: IMG_002.png (New size: 800x600)
Processing: corrupted.jpg (Original size: Unknown)
✗ Error processing corrupted.jpg: cannot identify image file

--- Processing Complete ---
Images processed successfully: 2
Errors encountered: 1
Output folder: ./resized_photos
```

## Error Handling

The script includes comprehensive error handling for:

- Invalid input directories
- Corrupted image files
- Unsupported file formats
- Permission issues
- Memory limitations

## Potential Extensions

This tool can be extended to include:

- **GUI Interface**: Add a graphical user interface using tkinter or PyQt
- **Preview Mode**: Show before/after previews
- **Aspect Ratio Preservation**: Option to maintain original aspect ratios
- **Batch Watermarking**: Add watermarks to processed images
- **Progress Bar**: Visual progress indicator for large batches
- **Image Optimization**: Compress images while resizing
- **Metadata Preservation**: Keep EXIF data from original images

## Technical Details

- **Resampling Algorithm**: Uses `Image.Resampling.LANCZOS` for high-quality resizing
- **Color Mode Handling**: Automatically converts RGBA to RGB for JPEG compatibility
- **Memory Efficient**: Uses context managers (`with` statements) for proper resource management
- **Cross-platform**: Works on Windows, macOS, and Linux

## License

This project is open source and available under the MIT License.
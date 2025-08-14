import os
from PIL import Image
import argparse

def resize_images(input_folder, output_folder, width=800, height=600, format_convert=None):
    """
    Resize and optionally convert all images in a folder
    
    Args:
        input_folder (str): Path to folder containing images
        output_folder (str): Path to folder where resized images will be saved
        width (int): Target width for resized images
        height (int): Target height for resized images
        format_convert (str): Target format (e.g., 'PNG', 'JPEG', 'WEBP')
    """
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output directory: {output_folder}")
    
    # Supported image formats
    supported_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp', '.gif'}
    
    # Counter for processed images
    processed_count = 0
    error_count = 0
    
    # Process all files in input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        
        # Skip if not a file
        if not os.path.isfile(file_path):
            continue
            
        # Check if file has supported image extension
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext not in supported_formats:
            continue
            
        try:
            # Open the image
            with Image.open(file_path) as img:
                print(f"Processing: {filename} (Original size: {img.size})")
                
                # Resize the image
                resized_img = img.resize((width, height), Image.Resampling.LANCZOS)
                
                # Determine output filename and format
                if format_convert:
                    # Change format
                    base_name = os.path.splitext(filename)[0]
                    if format_convert.upper() == 'JPEG':
                        output_filename = f"{base_name}.jpg"
                        # Convert RGBA to RGB for JPEG
                        if resized_img.mode in ('RGBA', 'LA', 'P'):
                            resized_img = resized_img.convert('RGB')
                    else:
                        output_filename = f"{base_name}.{format_convert.lower()}"
                else:
                    # Keep original format
                    output_filename = filename
                    format_convert = img.format
                
                # Save the resized image
                output_path = os.path.join(output_folder, output_filename)
                resized_img.save(output_path, format=format_convert.upper() if format_convert else None)
                
                print(f"✓ Saved: {output_filename} (New size: {width}x{height})")
                processed_count += 1
                
        except Exception as e:
            print(f"✗ Error processing {filename}: {str(e)}")
            error_count += 1
    
    # Summary
    print(f"\n--- Processing Complete ---")
    print(f"Images processed successfully: {processed_count}")
    print(f"Errors encountered: {error_count}")
    print(f"Output folder: {output_folder}")

def main():
    parser = argparse.ArgumentParser(description='Batch resize and convert images')
    parser.add_argument('input_folder', help='Path to input folder containing images')
    parser.add_argument('output_folder', help='Path to output folder for resized images')
    parser.add_argument('--width', type=int, default=800, help='Target width (default: 800)')
    parser.add_argument('--height', type=int, default=600, help='Target height (default: 600)')
    parser.add_argument('--format', choices=['JPEG', 'PNG', 'WEBP', 'BMP', 'TIFF'], 
                       help='Convert to specified format')
    
    args = parser.parse_args()
    
    # Validate input folder
    if not os.path.exists(args.input_folder):
        print(f"Error: Input folder '{args.input_folder}' does not exist!")
        return
    
    if not os.path.isdir(args.input_folder):
        print(f"Error: '{args.input_folder}' is not a directory!")
        return
    
    # Start processing
    print(f"Image Resizer Tool")
    print(f"Input folder: {args.input_folder}")
    print(f"Output folder: {args.output_folder}")
    print(f"Target size: {args.width}x{args.height}")
    if args.format:
        print(f"Convert to: {args.format}")
    print("-" * 50)
    
    resize_images(
        input_folder=args.input_folder,
        output_folder=args.output_folder,
        width=args.width,
        height=args.height,
        format_convert=args.format
    )

if __name__ == "__main__":
    main()

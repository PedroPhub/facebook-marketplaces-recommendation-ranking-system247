from PIL import Image
from pathlib import Path
import os


def clean_image_data(images_directory: str) -> None:
    """
    Extract and returns dataframe from S3
    
    Keyword arguments:
        'address': str -- Address to extract data from;
    
    Returns:
        'products_df': pd.dataframe -- DataFrame from S3 address;
    """
    destination_dir = Path("cleaned_images")
    # Creates destination folder if doesn't exist
    try:
        destination_dir.mkdir(parents=True)
    except FileExistsError:
        pass
    
    dirs = os.listdir(images_directory)
    final_size = 512 # Define size 512x512

    for index, item in enumerate(dirs):
        image = Image.open(f'images/{item}')
        filepath, extension = os.path.splitext(image.filename) # Get file path of each file
        filename = filepath.split("/")[-1] # Get filename from file path to use in .save()
        resized_image = resize_image(final_size, image)
        # Save new resized image with original name in destination directory
        resized_image.save(f'{destination_dir}\/{filename}{extension}')

def resize_image(final_size: int, image: Image) -> Image:
    size = image.size
    ratio = float(final_size) / max(size)
    new_image_size = tuple([int(x*ratio) for x in size])
    image = image.resize(new_image_size, Image.Resampling.LANCZOS)
    new_image = Image.new("RGB", (final_size, final_size))
    new_image.paste(image, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
    return new_image
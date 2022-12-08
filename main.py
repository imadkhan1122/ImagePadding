from padding import resize_images

# =============================================================================
# change both the paths according to your need
# =============================================================================
Excel_path = 'big rock 2 images.xlsx'
Des_path = 'Original_images/'
padd_path = 'PaddedImages/'

resize_images(Des_path, padd_path, Excel_path)

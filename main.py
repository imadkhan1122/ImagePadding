from padding import resize_images

# =============================================================================
# change both the paths according to your need
# =============================================================================
Excel_path = 'sent for work images.xlsx'
Des_path = 'data/Comm/'
padd_path = 'PaddedImages/'

resize_images(Des_path, padd_path, Excel_path)
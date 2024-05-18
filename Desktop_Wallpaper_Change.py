import ctypes
import time

def set_wallpaper(count, delay, *image_paths):
  """
  Changes the desktop wallpaper on Windows systems.

  Args:
      count: Number of times to switch between wallpapers.
      delay: Time (in seconds) to display each wallpaper.
      *image_paths: Variable arguments representing paths to image files.
  """

  for _ in range(count):
    for path in image_paths:
      image = ctypes.c_wchar_p(path)
      ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 0)
      time.sleep(delay)

# Example usage (replace with your image paths)
# Replace '\' with '\\' to avoid errors.
image_paths = [
  "C:\\Users\\username\\Pictures\\Wallpaper1.jpg",
  "C:\\Users\\username\\Pictures\\Wallpaper2.png"
]
set_wallpaper(10, 5, *image_paths)  # Change 10 times, 5 seconds each

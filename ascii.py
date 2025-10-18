from PIL import Image

def ask():
    while True:
        path = input("Enter the path to an image: ").strip('"').replace("\\", "/")
        try:
            image = Image.open(path)
            return image
        except FileNotFoundError:
            print("The file path does not exist. Try again.")
        except OSError:
            print("The file could not be opened. Make sure it's a valid image.")
        except Exception as e:
            print(f"Unexpected error: {e}")

image = ask()

ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

width, height = image.size
aspect_ratio = height / width
new_width = 100
new_height = int(aspect_ratio * new_width * 0.55) 
resized = image.resize((new_width, new_height))

gray = resized.convert("L")

pixels = gray.getdata()
chars = "".join(ascii_chars[pixel // 25] for pixel in pixels)

ascii_image = "\n".join(chars[i:i + new_width] for i in range(0, len(chars), new_width))

print(ascii_image)

# C:/User/Ezra/Downloads/smileyface.png
# Image Steganography

This Python script allows you to hide a secret message inside an image and later extract it using a password. It uses **LSB (Least Significant Bit)** steganography to encode the message in the pixel values of an image.

## Features

- 🛡️ **Hide Message**: Conceal a text message inside an image with a password for protection.
- 🔍 **Extract Message**: Retrieve the hidden message by providing the correct password.
- 🔐 **Password Protection**: Only users with the correct password can decode the hidden message.
- 🖼️ **Lossless Output**: Outputs images in PNG format to prevent quality loss.

## Requirements

Ensure you have Python installed along with the following packages:

```bash
pip install opencv-python numpy
```

## Usage

Run the script and follow the prompts.

```bash
python image_steganography.py
```

### 1. Hide a Message

1. ➡️ Choose option **1** to hide a message.
2. 📝 Provide the following inputs:
   - 📷 Path to the cover image.
   - 💬 Secret message to hide.
   - 🔒 Password for protection.
   - 📁 Output path for the stego image.

Example:
```
Do you want to (1) Hide or (2) Extract a message? 1
Enter the path of the cover image: kaish1.jpg
Enter the secret message: hii I'm kaish and this is a hidden message.
Enter a password to protect the message: 1234
Enter the output image path: msg image.png
```

### 2. Extract a Message

1. ⬅️ Choose option **2** to extract a message.
2. 📝 Provide the following inputs:
   - 📷 Path to the image containing the hidden message.
   - 🔑 Password to extract the message.

Example:
```
Do you want to (1) Hide or (2) Extract a message? 2
Enter the path of the image with hidden message: msg image.png
Enter the password to extract the message: 1234
Extracted Message: hii I'm kaish and this is a hidden message.
```

## How It Works

1. 🛠️ **Hiding Process:**
   - 📊 The message and password are combined using a `::` delimiter.
   - 🔢 Converted to a binary format and embedded into the least significant bits of the image pixels.
   - 🚩 A unique delimiter (`1111111111111110`) marks the end of the message.

2. 🔍 **Extraction Process:**
   - 🧾 The script reads the least significant bits from the image.
   - 📥 Retrieves the encoded message until the delimiter is found.
   - ✅ Validates the password and outputs the message if correct.

## Limitations

- ⚠️ Ensure the image has enough capacity to hold the message.
- 📌 Works best with uncompressed formats like PNG.

## License

📄 This project is licensed under the MIT License. Feel free to use and modify it!


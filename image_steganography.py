import cv2
import numpy as np

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    chars = [binary[i:i + 8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars if len(char) == 8 and int(char, 2) != 0)

def hide_message(image_path, message, password, output_path):
    # Read image in BGR format
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Unable to load image.")
        return

    # Combine message and password, followed by a delimiter
    binary_message = text_to_binary(message + "::" + password) + '1111111111111110'

    message_index = 0
    for row in image:
        for pixel in row:
            for channel in range(3):
                if message_index < len(binary_message):
                    pixel[channel] = (pixel[channel] & 0xFE) | int(binary_message[message_index])
                    message_index += 1

    # Save the image as a lossless PNG
    cv2.imwrite(output_path, image)
    print(f"Message hidden successfully in {output_path}")

def extract_message(image_path, password):
    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Unable to load image.")
        return ""

    binary_message = ''

    # Extract LSB from each pixel
    for row in image:
        for pixel in row:
            for channel in range(3):
                binary_message += str(pixel[channel] & 1)

    # Define delimiter
    delimiter = '1111111111111110'

    if delimiter in binary_message:
        binary_message = binary_message[:binary_message.index(delimiter)]
        decoded_message = binary_to_text(binary_message)

        # Check for password
        if "::" in decoded_message:
            secret_message, stored_password = decoded_message.rsplit("::", 1)

            if stored_password == password:
                return secret_message
            else:
                print("Error: Incorrect password.")
                return ""

    print("Error: No hidden message found.")
    return ""

if __name__ == "__main__":
    choice = input("Do you want to (1) Hide or (2) Extract a message? ")

    if choice == '1':
        image_path = input("Enter the path of the cover image: ")
        message = input("Enter the secret message: ")
        password = input("Enter a password to protect the message: ")
        output_path = input("Enter the output image path: ")
        hide_message(image_path, message, password, output_path)

    elif choice == '2':
        image_path = input("Enter the path of the image with hidden message: ")
        password = input("Enter the password to extract the message: ")
        hidden_message = extract_message(image_path, password)
        if hidden_message:
            print("Extracted Message:", hidden_message)

    else:
        print("Invalid choice!")

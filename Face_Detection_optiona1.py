import face_recognition
import PIL.Image
import PIL.ImageDraw


def load_image(image_path: str):
    """Load an image file into a numpy array."""
    return face_recognition.load_image_file(image_path)


def find_faces(image):
    """Find all face locations in the image."""
    return face_recognition.face_locations(image)


def draw_faces(image, face_locations, box_color="red", box_width=3):
    """Draw bounding boxes around detected faces and return the PIL image."""
    pil_image = PIL.Image.fromarray(image)
    draw_handle = PIL.ImageDraw.Draw(pil_image)

    for face_location in face_locations:
        top, right, bottom, left = face_location
        print(f"A face is located at Top: {top}, Left: {left}, Bottom: {bottom}, Right: {right}")
        draw_handle.rectangle([(left, top), (right, bottom)], outline=box_color, width=box_width)

    return pil_image


def detect_faces(image_path: str):
    """Main workflow: load image, detect faces, draw boxes, and display result."""
    # Step 1: Load image
    image = load_image(image_path)

    # Step 2: Find faces
    face_locations = find_faces(image)
    print(f"Found {len(face_locations)} face(s) in this picture.")

    # Step 3: Draw boxes
    pil_image = draw_faces(image, face_locations)

    # Step 4: Show result
    pil_image.show()


def main():
    """Program entry point."""
    # Replace 'your_image.jpg' with the path to your actual image file
    image_file = "Images/group image.jpg"
    detect_faces(image_file)


if __name__ == "__main__":
    main()
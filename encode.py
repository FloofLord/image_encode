import base64

def main():
    with open("/Users/val/Desktop/Santa.jpg","rb") as reader:
        # Read the whole image
        image_file = reader.read(-1)
        image = base64.b64encode(image_file)
    
    # Convert image to a utf-8 string
    image  = image.decode("utf-8")
    # Insert the base64 encoded string into a html img tag
    image = f'<img src="data:image/jpg;base64,{image}"'
    
    with open("index.html", "w") as writer:
        writer.write(image)




if __name__ =="__main__":
    main()

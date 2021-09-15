import base64

def main():
    with open("/Users/val/Desktop/Santa.jpg","rb") as reader:
        # Read the whole image
        image_file = reader.read(-1)
        image = base64.b64encode(image_file)
        #print(image)
        #<image src="data:image/jpg;base64,
        image  = image.decode("utf-8")
        image = f'<img src="data:image/jpg;base64,{image}"'
        print(image)
        file  =  open("encoded.txt","w")
        file.write(image)
        file.close()




if __name__ =="__main__":
    main()

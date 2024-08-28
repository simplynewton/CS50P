def main():
    ext = str(input("File Name: ")).lower().replace(" ", "")

    if ext.endswith("gif"):
        print("image/gif", end="")

    elif ext.endswith("jpg"):
        print("image/jpeg", end="")

    elif ext.endswith("jpeg"):
        print("image/jpeg", end="")

    elif ext.endswith("png"):
        print("image/png", end="")

    elif ext.endswith("pdf"):
        print("application/pdf", end="")

    elif ext.endswith("txt"):
        print("text/plain", end="")

    elif ext.endswith("zip"):
        print("application/zip", end="")

    else:
        print("application/octet-stream" , end="")

main()

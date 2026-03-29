
import zipfile


with zipfile.ZipFile("myfiles.zip", "w") as z:
    z.write("sample1.txt")

print("File zipped successfully!")
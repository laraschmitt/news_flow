import tarfile

# open tarfile
tar = tarfile.open("<PATH>", "r")

# print contents
for member in tar.getmembers():
    i = i + 1
    f = tar.extractfile(member)
    if f != None:
        print(f)
    if i == 7:
        break


tar.close()

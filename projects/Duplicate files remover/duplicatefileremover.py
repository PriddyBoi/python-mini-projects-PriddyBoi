import hashlib
import os

# Returns the hash string of the given file name
def hashFile(filename):
    # For large files, if we read it all together it can lead to memory overflow, So we take a blocksize to read at a time
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(filename, 'rb') as file:
        # Reads the particular blocksize from file
        buf = file.read(BLOCKSIZE)
        while(len(buf) > 0):
            hasher.update(buf)
            buf = file.read(BLOCKSIZE)
    return hasher.hexdigest()


if __name__ == "__main__":
    # Dictionary to store the hash and filename
    hashMap = {}

    # List to store deleted files
    deletedFiles = []
    
    # Specify the directory path to search for duplicate files
    directory = 'C:/Users/jacob/Downloads/test'
    
    # Generate the file list from the specified directory
    filelist = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    for f in filelist:
        key = hashFile(f)
        # If key already exists, it deletes the file
        if key in hashMap.keys():
            deletedFiles.append(f)
            os.remove(f)  # Corrected line
        else:
            hashMap[key] = f
    
    if len(deletedFiles) != 0:
        print('Deleted Files')
        for i in deletedFiles:
            print(i)
    else:
        print('No duplicate files found')

def filename(f):
    ext = []
    for i in range(len(f)):
        l = f[i].rfind(".")
        if(l==-1):
            ext.append("")
        else:
            ext.append(f[i][l:])
    return ext
f = ["text.txt","hello.pdf","itsjpeg.jpg","nullfile","multiple.dote.dot"]
ext = filename(f)
print(ext)

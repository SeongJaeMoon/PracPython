import urllib.request as req
import io, sys, gzip, os.path

savepath = "./mnist"
BASE_URL = "http://yann.lecun.com/exdb/mnist"
files = [
    "train-labels-idx1-ubyte.gz",
    "t10k-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz",
    "train-images-idx3-ubyte"
]

# 다운로드
if not os.path.exists(savepath): os.mkdir(savepath)
for f in files:
    url = BASE_URL + "/" + f
    loc = savepath + "/" + f
    print("download:", url)
    if not os.path.exists(loc):
        req.urlretrieve(url, loc)

# GZip 압축 해제
for f in files:
    gz_file = savepath + "/" + f
    raw_file = savepath + "/" + f.replace(".gz", "")
    print("gzip:", f)
    with gzip.open(gz_file, "rb") as fp:
        body = fp.read()
        with open(raw_file, "wb") as w:
            w.write(body)
print("Finished")               

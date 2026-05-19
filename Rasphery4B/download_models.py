import urllib.request

print("Downloading model (~30MB)...")
urllib.request.urlretrieve(
    "https://github.com/onnx/models/raw/main/validated/vision/classification/mobilenet/model/mobilenetv2-12.onnx",
    "mobilenet_v2.onnx"
)

print("Downloading labels...")
urllib.request.urlretrieve(
    "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt",
    "imagenet_labels.txt"
)

print("All done!")
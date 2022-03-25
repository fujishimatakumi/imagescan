import sys
import ImageScan

args = sys.argv

if len(args) == 1:
    sys.exit("prease args filepath")

filepath = args[1]

iScan = ImageScan.ImageScan()
result = iScan.ScanImageGrayScale(filepath)
print(result)
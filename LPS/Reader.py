import cv2
import zbar

class DetectQRcode():

    def detectQR(self, image):
        scanner = zbar.ImageScanner()

        scanner.parse_config('enable')

        gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY, dstCn=0)
        pil = image.fromarray(gray)
        width , high = pil.size
        raw = pil.tostring()
        image = zbar.Image(width, height, 'Y800', raw)

        scanner.scan(image)
        for symbol in image:
            loc = symbol.location
            x = (loc[0][0]+loc[2][0])/2
            y = (loc[0][1]+loc[2][1])/2
            if symbol.data == "None":
                return "Drone bevindt zich buiten het raster"
            else:
                return symbol.data

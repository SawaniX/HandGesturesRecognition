import cv2


class Rozpoznawanie:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)

    def __del__(self):
        self.cam.release()

    def stream(self):
        while True:
            success, image = self.cam.read()
            if not success:
                raise Exception("Cannot read frame!")
            ret, jpeg = cv2.imencode('.jpg', image)
            bytes_img = jpeg.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + bytes_img + b'\r\n')
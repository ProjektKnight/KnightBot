import pyqrcode

s = "www .sahil.com"
url = pyqrcode.create(s)
url.svg("gameplay.svg", scale=10)
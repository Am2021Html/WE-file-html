#pip install captcha

from captcha.image import ImageCaptcha

cap = ImageCaptcha(width=280, width=90)
c_text = "Im NoT a RoBOt"
data = cap.generate(c_text)
cap.write(c_text, "ADA.png"

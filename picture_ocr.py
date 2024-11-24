import cv2
import pytesseract

def ocr_opencv(image_path):
    # 读取图片并转换为灰度图
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 对图片进行 OCR 识别
    text = pytesseract.image_to_string(gray, lang="chi_sim+eng")
    return text

if __name__ == "__main__":


    
    image_path = r"C:\Users\admin\Desktop\kk.png"  # 替换为你的图片路径
    print("识别结果：")
    print(ocr_opencv(image_path))

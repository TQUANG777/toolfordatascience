import cv2
import numpy as np
import matplotlib.pyplot as plt

# Check OpenCV version
print("OpenCV version:", cv2.__version__)

# Simple test to see if the library loads correctly
img = cv2.imread(r"C:\Users\Hi\OneDrive\Pictures\wallpaper-4k-hinh-nen-4k-hinh-anh-ve-vu-tru-cuc-dep_101311485.jpg")  # Replace with an actual image path
if img is None:
    print("Image not loaded correctly!")
else:
    print("OpenCV is installed and working correctly!")
    height, width = img.shape[:2]
    new_width = int(width * 0.4)
    new_height = int(height * 0.4)
    resized_img = cv2.resize(img, (new_width, new_height))

    # Hiển thị ảnh đã thay đổi kích thước
    cv2.imshow('Picture',resized_img)

    #hold the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    '''RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #Displaying image using plt.imshow() method
    plt.imshow(RGB_img)

    # hold the window
    plt.waitforbuttonpress()
    plt.close('all')'''

import cv2
import numpy as np
import requests
from io import BytesIO

# Hàm tải ảnh từ URL và chuyển đổi thành ảnh OpenCV
def load_image_from_url(url):
    # Gửi yêu cầu tải ảnh
    response = requests.get(url)
    # Chuyển đổi dữ liệu ảnh thành mảng NumPy
    img_array = np.asarray(bytearray(response.content), dtype=np.uint8)
    # Đọc ảnh từ mảng NumPy
    image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return image

# URL của các ảnh
url1 = 'https://media.geeksforgeeks.org/wp-content/uploads/1-500x250-3.jpg'
url2 = 'https://media.geeksforgeeks.org/wp-content/uploads/2-500x250-2.jpg'

# Tải ảnh từ URL
image1 = load_image_from_url(url1)
image2 = load_image_from_url(url2)

# Kiểm tra xem ảnh đã được tải thành công hay chưa
if image1 is None or image2 is None:
    print("Không thể tải ảnh từ URL!")
else:
    # Áp dụng phép cộng trọng số lên hai ảnh
    weightedSum = cv2.addWeighted(image1, 1, image2, 0.5, 0)

    # Hiển thị ảnh kết quả
    cv2.imshow('Weighted Image', weightedSum)

    # Đóng cửa sổ khi nhấn phím ESC
    if cv2.waitKey(0) & 0xFF == 27:
        cv2.destroyAllWindows()


'''3. So sánh sự khác biệt giữa cộng và trừ
Cộng:
Kết quả sẽ sáng hơn, vì các giá trị pixel được cộng lại với nhau.
Có thể làm cho các chi tiết màu sắc của ảnh trở nên nổi bật và sáng hơn.
Có thể xảy ra hiện tượng bão hòa màu (trên 255) nếu giá trị pixel vượt quá giới hạn.
Trừ:
Kết quả sẽ tối hơn, vì các giá trị pixel của ảnh thứ hai bị trừ từ ảnh đầu tiên.
Phép trừ có thể làm nổi bật các sự thay đổi, vì những vùng có sự khác biệt giữa hai ảnh sẽ trở nên tối hơn hoặc "biến mất" (khi một pixel của ảnh thứ hai lớn hơn ảnh đầu tiên, giá trị bị cắt về 0).
Không có giá trị âm trong kết quả, nên nó không thể tạo ra các pixel "đen" (có giá trị âm).
4. Ứng dụng của cộng và trừ trong xử lý ảnh:
Cộng ảnh:

Thường được sử dụng để tăng cường màu sắc, tạo hiệu ứng sáng, hoặc kết hợp thông tin từ hai ảnh lại với nhau (ví dụ: ghép ảnh, phơi sáng).
Ví dụ: Tăng cường chi tiết sáng trong một bức ảnh hoặc tạo hiệu ứng ánh sáng rực rỡ.
Trừ ảnh:

Phép trừ hữu ích trong việc phát hiện sự thay đổi hoặc phân tích sự khác biệt giữa hai ảnh (ví dụ: trong phát hiện chuyển động hoặc phân tích sự thay đổi trong các hình ảnh).
Ví dụ: Phát hiện sự khác biệt giữa ảnh chụp hai lần tại các thời điểm khác nhau.
Tóm tắt:
Phép cộng tăng độ sáng của ảnh và có thể tạo ra ảnh rực rỡ hơn.
Phép trừ làm giảm độ sáng của ảnh và có thể giúp phát hiện sự khác biệt giữa các ảnh.
Hy vọng bạn đã hiểu rõ sự khác biệt giữa phép cộng và phép trừ trong xử lý ảnh!'''

# opencv(Computer Vision)

import cv2
print(cv2.__version__)

img1 = cv2.imread('./ani.jpg') # 이미지 불러오기
print(type(img1))
cv2.imshow('image test', img1)
cv2.waitKey() # 이미지 띄어두기(무한루프)
cv2.destroyAllWindows() # 종료버튼 누를 때 창 닫기

cv2.imwrite('ani2.jpeg', img1) # 이미지를 다른 이름으로 저장
cv2.imwrite('ani3.jpeg', img1, [cv2.IMWRITE_JPEG_QUALITY, 10]) 
# 이미지를 다른 이름으로 저장하며 사진의 퀄리티를 바꾼다

# 이미지 크기 조절
img2 = cv2.resize(img1, (300, 100), interpolation=cv2.INTER_AREA)
cv2.imwrite('ani4.jpg', img2)
# basic-cv：OpenCV 基础图像处理实验

## 简介
用 OpenCV 完成图像读取、灰度化、高斯模糊、Canny 边缘检测的完整流程。

## 环境
- Python 3.12
- opencv-python 4.13

安装依赖：
pip install opencv-python

## 运行
python3 basic_cv.py --input input.jpg

## 输出
output/01_original.jpg   原图
output/02_gray.jpg       灰度图
output/03_blurred.jpg    高斯模糊
output/04_edges.jpg      Canny 边缘检测

## 说明
- 高斯模糊作用：降噪，避免噪点被误识别为边缘
- Canny 双阈值：低于50丢弃，高于150确认为边缘，中间看连通性


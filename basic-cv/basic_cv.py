import cv2
import argparse
import os

def process(input_path, output_dir="output"):
    img = cv2.imread(input_path)
    if img is None:
        print(f"读取失败，请检查路径：{input_path}")
        return

    os.makedirs(output_dir, exist_ok=True)

    cv2.imwrite(f"{output_dir}/01_original.jpg", img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"{output_dir}/02_gray.jpg", gray)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imwrite(f"{output_dir}/03_blurred.jpg", blurred)

    edges = cv2.Canny(blurred, threshold1=50, threshold2=150)
    cv2.imwrite(f"{output_dir}/04_edges.jpg", edges)

    print("完成！结果保存在 output/ 文件夹")
    print(f"  原图尺寸：{img.shape[1]} x {img.shape[0]}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="input.jpg")
    args = parser.parse_args()
    process(args.input)

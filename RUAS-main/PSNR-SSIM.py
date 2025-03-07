import os
import cv2
from skimage.metrics import structural_similarity as ssim
import numpy as np


def calculate_psnr(img1, img2):
    return cv2.PSNR(img1, img2)


def calculate_ssim(img1, img2):
    # Convert images to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    return ssim(gray1, gray2)


def compare_images(folder1, folder2):
    images1 = sorted(os.listdir(folder1))
    images2 = sorted(os.listdir(folder2))

    if len(images1) != len(images2):
        print("两个文件夹中的文件数量不匹配！")
        return

    psnr_values = []
    ssim_values = []

    for img_name1, img_name2 in zip(images1, images2):
        img_path1 = os.path.join(folder1, img_name1)
        img_path2 = os.path.join(folder2, img_name2)

        img1 = cv2.imread(img_path1)
        img2 = cv2.imread(img_path2)

        if img1 is None or img2 is None:
            print(f"无法读取图像 {img_name1} 或 {img_name2}。")
            continue

        psnr_value = calculate_psnr(img1, img2)
        ssim_value = calculate_ssim(img1, img2)

        psnr_values.append(psnr_value)
        ssim_values.append(ssim_value)

        print(f"{img_name1} & {img_name2}: PSNR = {psnr_value}, SSIM = {ssim_value}")

    # Calculate average PSNR and SSIM
    avg_psnr = np.mean(psnr_values) if psnr_values else float('nan')
    avg_ssim = np.mean(ssim_values) if ssim_values else float('nan')

    print(f"平均 PSNR: {avg_psnr}")
    print(f"平均 SSIM: {avg_ssim}")

    return avg_psnr, avg_ssim


# 使用你的文件夹路径
folder1 = 'G:/Datasets/CPSLLE/Test/target'
folder2 = './result'

compare_images(folder1, folder2)
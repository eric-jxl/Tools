import os
import hashlib
import imagehash
from PIL import Image


def get_file_hash(file_path, is_image=False):
    """计算文件的哈希值（图片使用感知哈希，其他文件使用 SHA-256）"""
    try:
        if is_image:
            with Image.open(file_path) as img:
                return str(imagehash.phash(img))  # 感知哈希（pHash）
        else:
            hasher = hashlib.sha256()
            with open(file_path, "rb") as f:
                while chunk := f.read(8192):  # 逐块读取，适用于大文件
                    hasher.update(chunk)
            return hasher.hexdigest()
    except Exception as e:
        print(f"无法处理 {file_path}，错误: {e}")
        return None


def find_duplicates(folder_path):
    """查找并收集重复文件"""
    hashes = {}  # 存储 {哈希值: 文件路径}
    duplicates = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            ext = file.lower().split('.')[-1]

            # 判断是否为图片
            is_image = ext in ('png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp')

            file_hash = get_file_hash(file_path, is_image)
            if file_hash:
                if file_hash in hashes:
                    duplicates.append(file_path)  # 记录重复项
                else:
                    hashes[file_hash] = file_path

    return duplicates


def remove_duplicates(duplicates):
    """删除重复文件"""
    for dup in duplicates:
        print(f"删除重复文件: {dup}")
        os.remove(dup)


if __name__ == "__main__":
    FOLDER_PATH = "/Users/eric/Downloads/Downloads/哔哩哔哩壁纸"
    duplicates = find_duplicates(FOLDER_PATH)
    if duplicates:
        remove_duplicates(duplicates)
        print(f"已删除 {len(duplicates)} 个重复文件！")
    else:
        print("未发现重复文件！")

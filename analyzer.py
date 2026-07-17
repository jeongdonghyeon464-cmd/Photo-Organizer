import os

IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".bmp",
    ".gif", ".tiff", ".webp", ".heic", 
    ".dng", ".raw", ".cr2", ".cr3", 
    ".nef", ".arw", ".orf", ".rw2"
}

VIDEO_EXTENSIONS = {
    ".mp4", ".mov", ".avi",
    ".mkv", ".mts", ".m4v", ".3gp"
}


def format_size(size):
    """Byte → 사람이 보기 쉬운 단위"""

    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size:.2f} PB"


def analyze_folder(folder_path):

    result = {
        "total": 0,
        "images": 0,
        "videos": 0,
        "others": 0,
        "size": 0,
        "other_files": []
    }

    for root, dirs, files in os.walk(folder_path):

        for file in files:

            result["total"] += 1

            full_path = os.path.join(root, file)

            try:
                size = os.path.getsize(full_path)
                result["size"] += size

            except Exception:
                pass

            ext = os.path.splitext(file)[1].lower()

            if ext in IMAGE_EXTENSIONS:
                result["images"] += 1

            elif ext in VIDEO_EXTENSIONS:
                result["videos"] += 1

            else:
                result["others"] += 1
                result["other_files"].append(full_path)

    result["size_str"] = format_size(result["size"])

    return result
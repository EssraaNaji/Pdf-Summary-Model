import os

def get_file_size(path):
    """الحصول على حجم الملف بصيغة مقروءة"""
    size = os.path.getsize(path)
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} GB"

def validate_pdf(path):
    """التحقق من صحة ملف PDF"""
    if not path.endswith(".pdf"):
        raise ValueError("الملف يجب أن يكون بصيغة PDF")
    if not os.path.exists(path):
        raise FileNotFoundError("الملف غير موجود")
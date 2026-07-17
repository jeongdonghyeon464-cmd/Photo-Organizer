from pathlib import Path
from datetime import datetime

from PIL import Image
from PIL.ExifTags import TAGS


class MetadataReader:

    def __init__(self):
        pass

    def get_exif_date(self, file_path):

        try:
            image = Image.open(file_path)

            exif = image.getexif()

            if not exif:
                return None

            for tag_id, value in exif.items():

                tag = TAGS.get(tag_id, tag_id)

                if tag in (
                        "DateTimeOriginal",
                        "DateTimeDigitized",
                        "DateTime",
                    ):

                    return datetime.strptime(
                        value,
                        "%Y:%m:%d %H:%M:%S"
                    )

        except Exception:
            pass

        return None

    def get_date(self, file_path):

        path = Path(file_path)

        # 1. EXIF 먼저 확인
        exif_date = self.get_exif_date(file_path)

        if exif_date:
            return {
                "date": exif_date,
                "source": "EXIF"
            }

        # 2. EXIF 없으면 생성일 사용
        created = datetime.fromtimestamp(path.stat().st_ctime)

        return {
            "date": created,
            "source": "Creation Date"
        }
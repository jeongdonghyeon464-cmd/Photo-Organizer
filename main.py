import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText


class PhotoOrganizer:

    def __init__(self):

        self.root = ttk.Window(themename="flatly")
        self.root.title("Photo Organizer v0.1")
        self.root.geometry("850x700")

        self.source_path = ttk.StringVar()
        self.output_path = ttk.StringVar()

        self.create_widgets()

        self.root.mainloop()

    def create_widgets(self):

        ########################################
        # 제목
        ########################################

        ttk.Label(
            self.root,
            text="📷 Photo Organizer",
            font=("맑은 고딕", 20, "bold")
        ).pack(pady=10)

        ########################################
        # 원본 폴더
        ########################################

        frame1 = ttk.LabelFrame(self.root, text="원본 폴더")
        frame1.pack(fill=X, padx=15, pady=5)

        ttk.Entry(
            frame1,
            textvariable=self.source_path
        ).pack(side=LEFT, fill=X, expand=True, padx=5, pady=5)

        ttk.Button(
            frame1,
            text="찾아보기",
            bootstyle=PRIMARY,
            command=self.select_source
        ).pack(side=RIGHT, padx=5)

        ########################################
        # 출력 폴더
        ########################################

        frame2 = ttk.LabelFrame(self.root, text="출력 폴더")
        frame2.pack(fill=X, padx=15, pady=5)

        ttk.Entry(
            frame2,
            textvariable=self.output_path
        ).pack(side=LEFT, fill=X, expand=True, padx=5, pady=5)

        ttk.Button(
            frame2,
            text="찾아보기",
            bootstyle=PRIMARY,
            command=self.select_output
        ).pack(side=RIGHT, padx=5)

        ########################################
        # 옵션
        ########################################

        option = ttk.LabelFrame(self.root, text="옵션")
        option.pack(fill=X, padx=15, pady=10)

        ttk.Checkbutton(
            option,
            text="EXIF 우선 사용"
        ).pack(anchor=W)

        ttk.Checkbutton(
            option,
            text="EXIF가 없으면 생성일 사용"
        ).pack(anchor=W)

        ttk.Checkbutton(
            option,
            text="중복 파일 건너뛰기"
        ).pack(anchor=W)

        ########################################
        # 예상 결과
        ########################################

        preview = ttk.LabelFrame(self.root, text="예상 결과")
        preview.pack(fill=X, padx=15, pady=10)

        self.preview_label = ttk.Label(
            preview,
            text="원본 폴더를 선택하세요."
        )

        self.preview_label.pack(anchor=W, padx=10, pady=10)

        ########################################
        # 진행률
        ########################################

        progress = ttk.LabelFrame(self.root, text="진행률")
        progress.pack(fill=X, padx=15, pady=10)

        self.progress = ttk.Progressbar(
            progress,
            length=700,
            mode="determinate"
        )

        self.progress.pack(padx=10, pady=10)

        self.current_file = ttk.Label(
            progress,
            text="현재 파일 : -"
        )

        self.current_file.pack(anchor=W, padx=10)

        ########################################
        # 로그
        ########################################

        log_frame = ttk.LabelFrame(self.root, text="로그")

        log_frame.pack(fill=BOTH, expand=True, padx=15, pady=10)

        self.log = ScrolledText(
            log_frame,
            height=10
        )

        self.log.pack(fill=BOTH, expand=True)

        ########################################
        # 시작 버튼
        ########################################

        ttk.Button(
            self.root,
            text="정리 시작",
            bootstyle=SUCCESS,
            command=self.start
        ).pack(fill=X, padx=15, pady=15)

    ########################################

    def select_source(self):

        folder = filedialog.askdirectory()

        if folder:
            self.source_path.set(folder)
            self.preview_label.config(
                text=f"원본 폴더\n\n{folder}"
            )

    ########################################

    def select_output(self):

        folder = filedialog.askdirectory()

        if folder:
            self.output_path.set(folder)

    ########################################

    def start(self):

        self.log.insert("end", "Photo Organizer 시작\n")

        self.log.insert("end", "아직 구현되지 않았습니다.\n")

        self.log.see("end")


if __name__ == "__main__":
    PhotoOrganizer()
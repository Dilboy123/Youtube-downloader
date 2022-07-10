from pytube import YouTube


class Details(YouTube):
    def __init__(self, link):
        super().__init__(link)
        YouTube(link)

    def get_details(self):
        ys = self.streams.get_highest_resolution()
        return ys

    def download_video(self):
        print("Downloading...")
        download = self.get_details().download('.')
        print("Download Completed!!")
        return download



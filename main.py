import tkinter
from tkinter import Message, filedialog
from tkinter import messagebox
from tkinter import ttk
from pathlib import Path
import os
from src.message_factroy import MessageFactory as MF
import youtube_dl
"""
やること
レイアウト調整
Enter でADDしたい
ADDしたらEntry内の文字消えてほしい
最後exeにする
"""


# start class
class Application(tkinter.Frame):
    # start init
    def __init__(self, root):
        """
        Parameters
        ----------
        borderwidth : 境界線の太さ
        relief : 境界線の種類
        pack : 位置を設定、配置
        P_* : 表示用変数
        D_* : 説明用変数
        ----------
        """
        super().__init__(root, width=380, height=280,
                         borderwidth=1, relief='groove')

        # start variable
        self.file_tyep_list = ['mp3', 'mp4', 'wav']
        self.url_list = []
        self.savePath = os.getcwd()
        # end variable

        self.root = root
        self.pack()
        # サイズ調整用
        self.pack_propagate(0)
        self.createWidgets()

    # end init

    # start createWidgets
    def createWidgets(self):
        # start quit_btn
        quit_btn = tkinter.Button(self)
        quit_btn['text'] = MF.P_Close
        quit_btn['command'] = self.root.destroy
        quit_btn.pack(side='bottom')
        # end quit_btn

        # start message
        reception_label = tkinter.Label(self)
        reception_label['text'] = MF.P_D_reception_message
        reception_label.pack()
        # end message

        # start URL_reception
        self.URL_reception = tkinter.Entry(self)
        self.URL_reception['width'] = 100
        self.URL_reception.pack()
        # end URL_reception

        # start add_url_btn
        add_url_btn = tkinter.Button(self)
        add_url_btn['text'] = MF.P_Add
        add_url_btn['command'] = self.addURL
        add_url_btn.pack()
        # end add_url_btn

        # start delete_url_btn
        delete_url_btn = tkinter.Button(self)
        delete_url_btn['text'] = MF.P_Delete
        delete_url_btn['command'] = self.deleteURL
        delete_url_btn.pack()
        # end delete_url_btn

        # start add_url_check_list
        self.add_url_check_list = tkinter.Message(self)
        self.add_url_check_list['width'] = 300
        self.add_url_check_list['text'] = os.getcwd()
        self.add_url_check_list.pack()
        # end add_url_check_list

        # start submit_btn
        submit_btn = tkinter.Button(self)
        submit_btn['text'] = MF.P_Run
        submit_btn['command'] = self.downloadVideo
        submit_btn.pack(side='bottom')
        # end submit_btn

        # start added link message
        self.P_add_url = tkinter.Message(self, width=380)
        self.P_add_url.pack()
        # end added link message

        # start select_dir
        select_dir = tkinter.Button(self)
        select_dir['text'] = MF.P_Reference
        select_dir['command'] = self.dirDialogClicked
        select_dir.pack(side='right')
        # end select_dir

        # start select_file_type
        # どのラジオボタンが押されたかを知るためのもの
        self.selected_radio = tkinter.StringVar()
        mp3_radio = tkinter.Radiobutton(
            self, text=self.file_tyep_list[0], value=self.file_tyep_list[0], variable=self.selected_radio)
        mp4_radio = tkinter.Radiobutton(
            self, text=self.file_tyep_list[1], value=self.file_tyep_list[1], variable=self.selected_radio)
        wav_radio = tkinter.Radiobutton(
            self, text=self.file_tyep_list[2], value=self.file_tyep_list[2], variable=self.selected_radio)
        mp3_radio.pack()
        mp4_radio.pack()
        wav_radio.pack()
        # end select_file_type

        # start help use botton
        help_use = tkinter.Button(self)
        help_use['text'] = MF.P_Help
        help_use['command'] = self.discriptionUseApp
        help_use.pack()
        # end help use botton
    # end createWidgets

    # フォルダ選択用関数
    def dirDialogClicked(self):
        self.savePath = filedialog.askdirectory(initialdir=self.savePath)
        self.add_url_check_list['text'] = self.savePath
    # end def

    # URL先の動画をDLする
    def downloadVideo(self):
        # file_type = self.file_type_combobox.get()
        file_type = self.selected_radio.get()
        ydl_opts = self.createYoutubeDLOpt(file_type=file_type)
        ydl_opts['outtmpl'] = f"{self.savePath}/%(title)s%(ext)s"
        # start if
        if not self.url_list:
            self.addURL()
        # end if
        # start for
        for url in self.url_list:
            """有効なURLかどうか調べる必要あり(関数で作成)"""
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        # end for
    # end def

    # youtube-dl options set
    def createYoutubeDLOpt(self, file_type):
        ydl_opts = {
            'outtmpl': "",
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        # start if
        if file_type == 'mp4':
            ydl_opts = {}
        else:
            # start if
            if file_type in self.file_tyep_list:
                ydl_opts['preferredcodec'] = file_type
            # とりあえずこうしてる（多分tryとか使うべき）default=mp4 or webm
            else:
                ydl_opts = {}
            # end if
        # end if
        return ydl_opts
    # end def

    # 使い方
    def discriptionUseApp(self):
        P_text = MF.P_D_combobox
        P_text += '\n' + MF.P_D_discriptionUseApp
        messagebox.showinfo('使い方', P_text)
    # end def

    # ダウンロードするURLを追加
    def addURL(self):
        url = self.URL_reception.get()
        # start if 同じurlがないとき
        if url not in self.url_list:
            # Entryの値を0文字目から最後の文字まで削除
            self.URL_reception.delete(0, tkinter.END)
            self.url_list.append(url)
            self.P_add_url['text'] += url + "\n"
        else:
            messagebox.showwarning('Warning !!!', MF.P_W_add_URL)
        # end if
    # end def

    # ダウンロードするURLを削除
    def deleteURL(self):
        # start if
        if self.url_list:
            self.url_list.pop()
            # start if
            if not self.url_list:
                self.P_add_url['text'] = ''
            else:
                self.P_add_url['text'] = "".join(
                    [url+'\n' for url in self.url_list])
            # end if
        else:
            messagebox.showerror('*** Error ***', MF.P_E_delete_URL)
        # end if
    # end def
# end class


if __name__ == '__main__':
    root = tkinter.Tk()
    # window name
    root.title(MF.P_Title)
    # window size
    root.geometry('600x500')
    # applicationクラスのオブジェクトの作成
    app = Application(root=root)
    # アプリが動く
    app.mainloop()

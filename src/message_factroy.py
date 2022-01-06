"""
creater : ryoum 
version : 1.0.0
"""


class MessageFactory():
    """
    Parameter
    ----------
    P_* : 表示用変数
    _D_* : 説明用変数
    _W_* : 警告用変数
    _E_* : エラー用変数
    """
    # start Button Message
    P_Title = 'Youtube Downloader'
    P_Add = 'Add'
    P_Delete = 'Delete'
    P_Reference = '参照'
    P_Help = 'Help'
    P_Run = '実行'
    P_Close = '閉じる'
    # end Button Message

    # start Discription Message
    P_D_combobox = "各拡張子について\n音声\n.mp3, .wav\n動画\n.mp4"
    P_D_discriptionUseApp = "aaaaa"
    P_D_reception_message = 'YoutubeのURL'
    # end Discription Message

    # start Warning Message
    P_W_add_URL = "同じURLが既に追加されています\nWarning: The same URL already exists."
    # end Warning Message

    # start Error Message
    P_E_delete_URL = "URLないよ！\nNot exist URL."
# end class

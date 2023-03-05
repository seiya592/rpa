import cv2
import os
from PIL import ImageGrab
import tkinter as tk

def ss():
    TkRoot = tk.Tk()
    ImageGrab.grab().save('IMG/screenshot.bmp')                 # スクリーンショット
    img = cv2.imread('IMG/screenshot.bmp', cv2.IMREAD_COLOR)    # RGBで読み込み
    window_name = 'img'                                         # ssを画面に出力するときの表示名
    imgBoxHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)             # HSVに変換

    #debug
    cv2.imwrite('IMG/output.bmp', imgBoxHsv)        # HSVデータを出力

    def onMouse(event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            crop_img = imgBoxHsv[[y], [x]]
            H_val = crop_img.T[0].flatten().mean()
            S_val = crop_img.T[1].flatten().mean()
            V_val = crop_img.T[2].flatten().mean()
            print("H: {}, S: {}, V: {}".format(H_val, S_val, V_val))

    def my_makedirs(path):
        if not os.path.isdir(path):
            os.makedirs(path)

    # dirpath= "./IMG"
    # my_makedirs(dirpath)

    # 画像最大化処理
    # cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    # cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # ディスプレイサイズ取得
    # display_width = TkRoot.winfo_screenwidth()
    # display_height = TkRoot.winfo_screenheight()
    #
    # print(f'{display_width} {display_height}')

    # height, width, ch = img.shape
    # resize_frame = cv2.resize(img, dsize=(int(display_height / height * width), display_height))

    # フレームをリサイズ
    # img2 = cv2.resize(img, (display_width, display_height))
    # cv2.imshow(window_name, img2)  # RGB画像を画面上に表示

    cv2.imshow(window_name, img)                # 画像表示
    # cv2.imshow(window_name, imgBoxHsv)
    cv2.setMouseCallback(window_name, onMouse)  # クリックするとその位置のHSVを取得
    cv2.waitKey(0)                              # キーを押下するまで画像表示
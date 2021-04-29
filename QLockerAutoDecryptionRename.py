"""
程式名稱: QNAP批次修改被壓縮的亂碼檔名視窗化程式
註解: QLockerAutoDecryptionRename
作者: scku208
副本建立日期: 29/04/2021
影片: https://youtu.be/-e43DFQu0gY
部落格: https://www.ku88.xyz/?p=1142
"""

import os
import py7zr
import PySimpleGUI as sg

sg.theme('Dark Blue 3')

file_list_column = [
    [
        sg.Text("解壓縮根目錄：", size=(12, 1)),
        sg.In(size=(50, 1), key="-FOLDER-"),
        sg.FolderBrowse(button_text='選擇根目錄資料夾')
    ],
    [
        sg.Text("解壓縮密碼：", size=(12, 1)),
        sg.Input(size=(50, 1), key="-PASSWORD-"),
        
    ],
    [sg.Button('開始解壓縮', size=(12, 1))],
    [
        sg.Output(
            size=(100, 20)
        )
    ],
]

layout = [
    [
        sg.Column(file_list_column),
    ]
]

window = sg.Window("QNAP批次修改被壓縮的亂碼檔名視窗化程式 by scku208", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "開始解壓縮":
        STOP = False
        for r_, d_, files in os.walk(values['-FOLDER-']):
            for f_ in files:
                if f_.endswith('.7z'):
                    print(f'解壓縮… {os.path.join(r_, f_)}', end='')
                    correct_name = f_.rsplit('.', 1)[0]
                    archive = py7zr.SevenZipFile(
                        os.path.join(r_, f_), mode='r',
                        password=values['-PASSWORD-'])
                    wrong_name = archive.getnames()[0]
                    try:
                        archive.extractall(path=os.path.join(r_))
                        archive.close()
                    except (py7zr.exceptions.CrcError, py7zr.exceptions.Bad7zFile) as e:
                        print('解壓失敗?!，是不是打錯密碼?!')
                        STOP = True
                        break
                    if os.path.exists(os.path.join(r_, correct_name)):
                        print('解壓後檔案已存在，略過')
                    else:
                        os.rename(
                            os.path.join(r_, wrong_name),
                            os.path.join(r_, correct_name)
                            )
                        print(' 且改名成功!!')
                if STOP:
                    break
            if STOP:
                break

window.close()

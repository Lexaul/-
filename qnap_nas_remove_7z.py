"""
程式名稱: QNAP批次刪除解壓縮後的7z檔案視窗化程式
註解: qnap_nas_remove_7z
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
        sg.Text("根目錄：", size=(12, 1)),
        sg.In(size=(30, 1), key="-FOLDER-"),
        sg.FolderBrowse(button_text='選擇資料夾')
    ],
    [sg.Button('開始刪除', size=(12, 1)),
     sg.Checkbox(
        '我清楚知道此程式的用途是與刪除檔案有關,\n'
        '對使用此程式造成的任何結果與開發者無關。\n'
        '同時，開發者真的無法負責檔案(與其正確名稱)的消失\n'
        '本程式強迫產出刪除檔案的路徑記錄於所選之根目錄下,\n'
        '名稱為「qnap_nas_remove_7z_log.txt」,以備不時之需(文件為UTF-8編碼)。',
        default=False, text_color='red',
        key="-I Know-")],
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

window = sg.Window("QNAP批次刪除解壓縮後的7z檔案視窗化程式 by scku208", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "開始刪除":
        if values["-I Know-"] != True:
            print(f'**若要執行「開始刪除」，請勾選(也代表同意)程式中對風險的說明**')
            continue
        else:
            if values['-FOLDER-'] == '':
                print(f'**請務必選取根目錄資料夾，以免造成遺憾**')
                continue
            else:
                f_out = open(
                    os.path.join(values['-FOLDER-'], 'qnap_nas_remove_7z_log.txt'),
                    'w',
                    encoding='utf-8'
                    )
                delete_file_count = 0
                for r_, d_, files in os.walk(values['-FOLDER-']):
                    for f_ in files:
                        correct_name = f_.rsplit('.', 1)[0]
                        if f_.endswith('.7z') and os.path.exists(os.path.join(r_, correct_name)):
                            print(f'發現檔案 {os.path.join(r_, correct_name)} 的存在,')
                            print(f'所以將檔案 {os.path.join(r_, f_)} 刪除...', end='')

                            os.remove(os.path.join(r_, f_))
                            f_out.write(os.path.join(r_, f_)+'\n')
                            print(' 刪除成功!!')
                            delete_file_count += 1
                f_out.close()

        print(f'執行結束!! 共移除{delete_file_count}個檔案')

window.close()

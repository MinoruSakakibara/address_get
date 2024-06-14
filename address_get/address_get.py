import PySimpleGUI as sg
import requests

layout = [[sg.Text('郵便番号：'),
           sg.InputText(key = '-NUMBER1-', size = (10, 3)),
           sg.Text('-'),
           sg.InputText(key = '-NUMBER2-', size = (10, 3))],
          [sg.Text('住所：', size = (5, 5)),
           sg.Text(key = '-ADDRESS-', size = (20, 5))],
          [sg.Button('実行', key = '-SUBMIT-')]]

window = sg.Window('住所取得アプリ', layout, size = (300, 150))

while True:
    event, values = window.read()
    
    if event == '-SUBMIT-' and len(values['-NUMBER1-']) < 3:
        sg.popup("左欄は3桁で入力してください。")
        continue
    
    if event == '-SUBMIT-' and len(values['-NUMBER1-']) >= 4:
        sg.popup("左欄は3桁で入力してください。")
        continue
    
    if event == '-SUBMIT-' and len(values['-NUMBER2-']) < 4:
        sg.popup("右欄は4桁で入力してください。")
        continue
        
    if event == '-SUBMIT-' and len(values['-NUMBER2-']) >= 5:
        sg.popup("右欄は4桁で入力してください。")
        continue
        
    if event == '-SUBMIT-':
        num1 = values['-NUMBER1-']
        num2 = values['-NUMBER2-']
        URL = 'https://zipcloud.ibsnet.co.jp/api/search'
        res = requests.get(f'{URL}?zipcode={num1}{num2}')
        res_json = res.json()
        if res_json['status'] == 200:
            result = res_json['results'][0]
            adr1 = result['address1']
            adr2 = result['address2']
            adr3 = result['address3']
            window['-ADDRESS-'].update(f'{adr1}{adr2}{adr3}')
        else:
            window['-ADDRESS-'].update('住所の取得に失敗しました')
    
    if event == sg.WIN_CLOSED:
        break
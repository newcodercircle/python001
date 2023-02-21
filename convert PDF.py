import os
import PySimpleGUI as sg
from pathlib import Path
from pdf2docx import parse as pdf2docx_parse


def parse(files):
    for i, f in enumerate(files):
        path = Path(os.path.dirname(f)).joinpath("output")
        # 防止文件名中出现多个.
        file_name = os.path.basename(f)[::-1].split(".", maxsplit=1)[-1][::-1]
        path.mkdir(parents=True, exist_ok=True)
        target = path.joinpath(f"{file_name}.docx")
        sg.OneLineProgressMeter('转换中', i + 1, len(files), key='-METER-')
        pdf2docx_parse(f, str(target))
    sg.popup('完成!查看output文件夹', '文件数:%s' % (i + 1))


def make_window():
    layouts = [[sg.Input(key='_FILES_'), sg.FilesBrowse("浏览", file_types=(("pdf", "*.pdf"),))],
               [sg.OK("开始转换"), sg.Cancel("取消")]]
    return sg.Window("批量ppdf转word", layout=layouts)


if __name__ == '__main__':
    main_window = make_window()
    while True:
        event, values = main_window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == "取消":
            main_window["_FILES_"].update(value="")
        if event == "开始转换":
            files = main_window["_FILES_"].get().split(";")
            if files:
                parse(files)

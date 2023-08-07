# coding: utf-8

import flet as ft
import ybc_face


async def main(page: ft.Page):
    async def left_choose_file_action(e):
        await left_file_picker.pick_files_async(
            allow_multiple=False,
            file_type=ft.FilePickerFileType.IMAGE,
        )

    async def left_pick_file_result(e):
        if not e.files:
            return
        url = e.files[0].path
        left_pic_show_area.src = url
        await left_pic_show_area.update_async()
        left_result_area.value = ybc_face.info_all(url)
        await left_result_area.update_async()

    async def right_choose_file_action(e):
        await right_file_picker.pick_files_async(
            allow_multiple=False,
            file_type=ft.FilePickerFileType.IMAGE,
        )

    async def right_pick_file_result(e):
        if not e.files:
            return
        url = e.files[0].path
        right_pic_show_area.src = url
        await right_pic_show_area.update_async()
        right_result_area.value = ybc_face.info_all(url)
        await right_result_area.update_async()

    page.title = "颜值PK器"
    page.window_width = 800
    page.window_height = 600
    left_choose_file_btn = ft.ElevatedButton("选择文件", on_click=left_choose_file_action)
    left_file_picker = ft.FilePicker(on_result=left_pick_file_result)
    left_result_area = ft.Text("")
    left_pic_show_area = ft.Image(src="0000")

    right_choose_file_btn = ft.ElevatedButton("选择文件", on_click=right_choose_file_action)
    right_file_picker = ft.FilePicker(on_result=right_pick_file_result)
    right_result_area = ft.Text("")
    right_pic_show_area = ft.Image(src="0000")
    page.overlay.extend([left_file_picker, right_file_picker])
    await page.add_async(
        ft.Row(
            [
                ft.Column(
                    [left_choose_file_btn, left_result_area, left_pic_show_area],
                    expand=1,
                ),
                ft.VerticalDivider(),
                ft.Column(
                    [right_choose_file_btn, right_result_area, right_pic_show_area],
                    expand=1,
                ),
            ],
            expand=1,
        )
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.FLET_APP)

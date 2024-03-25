import flet as ft

# flet 若使用 .ipynb 會出現 RuntimeError: asyncio.run() cannot be called from a running event loop
# 因此需使用 .py

def remove_outliers(num_remove, data_original):
    removed_data = []
    data = []
    
    data = data_original.copy()
    for i in range(num_remove*2):
        if i < num_remove:
            max_value = max(data)
            removed_data.append(max_value)
            data.remove(max_value)
        else:
            min_value = min(data)
            removed_data.append(min_value)
            data.remove(min_value)

    return sorted(data), sorted(removed_data)

def main(page: ft.Page):
    global start_station, end_station

    # GUI的排版
    page.title = "Remove Outliers GUI"
    page.window_width = 700
    page.window_height = 600
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.background_color = '#FFFFFF'  # 將背景顏色設定為白色
    
    data_original = []

    # 按鈕的function
    def append_click(e):
        # 可以透過 number_textfield.value 取得值
        # data_original.append(number) 將數字一個一個加進去list中
        # list_text.value 更改顯示的內容
        # page.update() 更新GUI畫面
        # *****請完成這部分*****
        number = int(number_textfield.value)
        data_original.append(number)
        list_text.value = 'This list is ' + str(data_original)
        page.update()

    def result_click(e):
        # 可以使用下面寫好的function傳出的變數繼續完成
        data, removed_data = remove_outliers(int(remove_textfield.value), data_original)
        # original_data_text.value 更改顯示的內容
        # data_text.value 更改顯示的內容
        # removed_data_text.value 更改顯示的內容
        # page.update() 更新GUI畫面
        # *****請完成這部分*****
        original_data_text.value = "The original data: " + str(data_original)
        data_text.value = "The data with the outliers removed: " + str(data)
        removed_data_text.value = "The outliers: " + str(removed_data)
        page.update()

    # ------建立物件------
    
    # for number view
    remove_textfield = ft.TextField(label="Number to remove", width=300, text_size=18)
    number_textfield = ft.TextField(label="Input number to list", width=300, text_size=18)

    append_button = ft.ElevatedButton(text=f"Append the number to list", width=300, on_click=append_click)
    list_text = ft.Text("", size=18)
    
    # for result view
    result_button = ft.ElevatedButton(text=f"Run the function", width=300, on_click=result_click)

    original_data_text = ft.Text("", size=18)
    data_text = ft.Text("", size=18)
    removed_data_text = ft.Text("", size=18)

    # ------將物件進行排版------
    page.add(
        # 把物件照順序放進版面...
        remove_textfield,
        number_textfield,
        append_button,
        list_text,
        result_button,
        original_data_text,
        data_text,
        removed_data_text
    )

ft.app(target=main)
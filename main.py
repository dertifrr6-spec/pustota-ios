import flet as ft
import os
import datetime

def main(page: ft.Page):
    page.title = "ПУСТОТА"
    page.theme_mode = "dark"
    
    # Секретный пароль
    SECRET_PASSWORD = "mamatop1122999666464"
    
    # Контроллер записи для iOS/Android
    audio_recorder = ft.AudioRecorder()
    page.overlay.append(audio_recorder)

    status_text = ft.Text("Готов к записи", size=16)

    def on_record_click(e):
        if not audio_recorder.is_recording():
            # На iPhone файлы лучше сохранять в спец. папку приложения
            file_name = f"rec_{datetime.datetime.now().strftime('%H%M%S')}.wav"
            # Для мобилок путь определяется автоматически
            audio_recorder.start_recording(os.path.join(os.getcwd(), file_name))
            mic_btn.icon_color = "red"
            status_text.value = "Идет запись..."
        else:
            audio_recorder.stop_recording()
            mic_btn.icon_color = "blue"
            status_text.value = "Запись сохранена"
        page.update()

    mic_btn = ft.IconButton(
        icon=ft.Icons.MIC_ROUNDED,
        icon_size=100,
        icon_color="blue",
        on_click=on_record_click
    )

    page.add(
        ft.AppBar(title=ft.Text("ПУСТОТА"), bgcolor="surfacevariant"),
        ft.Column([
            mic_btn,
            status_text,
            ft.FilledButton("Посмотреть архив", icon=ft.Icons.FOLDER_OPEN)
        ], alignment="center", horizontal_alignment="center")
    )


ft.app(main) 

from kivy_reloader.app import App
import trio
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.utils import rgba


class MyApp(App):
    def build(self):
        box = FloatLayout()

        # === ФОН ===
        with box.canvas.before:
            Color(0.95, 0.95, 0.95, 1)  # Светло-серый фон
            self.rect = Rectangle(size=Window.size, pos=box.pos)
            box.bind(size=self._update_rect, pos=self._update_rect)

        # === БЛОК 1: ХИТ и вес без упаковки ===

        # Главный заголовок
        Header = Label(
            text='ХИТ',
            font_size=72,
            size_hint=(1, 0.15),
            pos_hint={'center_x': 0.5, 'top': 1},
            color=rgba('#2C3E50'),  # Темно-синий
            bold=True
        )
        box.add_widget(Header)

        # Подзаголовок блока 1
        header_1 = Label(
            text="Вес продукции без упаковки",
            font_size=24,
            size_hint=(1, 0.08),
            pos_hint={'center_x': 0.5, 'top': 0.85},
            color=rgba('#34495E'),  # Серо-синий
            bold=True
        )
        box.add_widget(header_1)

        # Ввод количества деталей
        col_d = TextInput(
            hint_text='Количество деталей',
            multiline=False,
            size_hint=(0.28, 0.06),
            pos_hint={'x': 0.05, 'top': 0.75},
            input_filter='int',
            background_color=(1, 1, 1, 1),
            foreground_color=(0.1, 0.1, 0.1, 1),
            cursor_color=rgba('#3498DB'),  # Ярко-синий
            font_size=18,
            padding=[10, 12]
        )
        self.col_d = col_d
        box.add_widget(col_d)

        # Ввод веса одной детали
        ves_d = TextInput(
            hint_text='Вес детали (г)',
            multiline=False,
            size_hint=(0.28, 0.06),
            pos_hint={'x': 0.36, 'top': 0.75},
            input_filter='float',
            background_color=(1, 1, 1, 1),
            foreground_color=(0.1, 0.1, 0.1, 1),
            cursor_color=rgba('#3498DB'),
            font_size=18,
            padding=[10, 12]
        )
        self.ves_d = ves_d
        box.add_widget(ves_d)

        # Кнопка расчета блока 1
        button1 = Button(
            text="=",
            size_hint=(0.1, 0.06),
            pos_hint={'x': 0.67, 'top': 0.75},
            background_color=rgba('#9B59B6'),
            background_normal='',
            color=(1, 1, 1, 1),
            font_size=24,
            bold=True
        )
        box.add_widget(button1)
        self.button1 = button1

        # Результат блока 1
        self.ves_d_label = Label(
            text='Вес без упаковки: 0 г',
            font_size=20,
            size_hint=(0.9, 0.06),
            pos_hint={'center_x': 0.5, 'top': 0.66},
            color=rgba('#27AE60'),  # Зеленый
            bold=True,
            halign='center',
            valign='middle'
        )
        self.ves_d_label.bind(size=self.ves_d_label.setter('text_size'))
        box.add_widget(self.ves_d_label)

        # === РАЗДЕЛИТЕЛЬ 1 ===
        with box.canvas.after:
            Color(0.8, 0.8, 0.8, 1)
            Rectangle(pos=(50, Window.height * 0.58), size=(Window.width - 100, 2))

        # === БЛОК 2: Вес с упаковкой ===

        # Подзаголовок блока 2
        label2 = Label(
            text="Вес продукции с упаковкой",
            font_size=24,
            size_hint=(1, 0.08),
            pos_hint={'center_x': 0.5, 'top': 0.55},
            color=rgba('#34495E'),
            bold=True
        )
        box.add_widget(label2)

        # Вес без упаковки
        d_1 = TextInput(
            hint_text='Вес без уп.',
            multiline=False,
            size_hint=(0.2, 0.05),
            pos_hint={'x': 0.08, 'top': 0.48},
            input_filter='int',
            background_color=(1, 1, 1, 1),
            foreground_color=(0.1, 0.1, 0.1, 1),
            cursor_color=rgba('#E67E22'),  # Оранжевый
            font_size=16,
            padding=[8, 10]
        )
        self.d_1 = d_1

        # Вес пакета
        d_2 = TextInput(
            hint_text='Пакет',
            multiline=False,
            size_hint=(0.2, 0.05),
            pos_hint={'x': 0.32, 'top': 0.48},
            input_filter='int',
            background_color=(1, 1, 1, 1),
            foreground_color=(0.1, 0.1, 0.1, 1),
            cursor_color=rgba('#E67E22'),
            font_size=16,
            padding=[8, 10]
        )
        self.d_2 = d_2

        # Вес коробки
        d_3 = TextInput(
            hint_text='Коробка',
            multiline=False,
            size_hint=(0.2, 0.05),
            pos_hint={'x': 0.56, 'top': 0.48},
            input_filter='int',
            background_color=(1, 1, 1, 1),
            foreground_color=(0.1, 0.1, 0.1, 1),
            cursor_color=rgba('#E67E22'),
            font_size=16,
            padding=[8, 10]
        )
        self.d_3 = d_3

        box.add_widget(d_1)
        box.add_widget(d_2)
        box.add_widget(d_3)

        # Кнопка расчета блока 2
        btn2 = Button(
            text="=",
            size_hint=(0.1, 0.05),
            pos_hint={'x': 0.8, 'top': 0.48},
            background_color=rgba('#9B59B6'),
            background_normal='',
            color=(1, 1, 1, 1),
            font_size=24,
            bold=True
        )

        # Результат блока 2
        self.label3 = Label(
            text="Вес с упаковкой: 0 г",
            font_size=20,
            size_hint=(0.9, 0.06),
            pos_hint={'center_x': 0.5, 'top': 0.4},
            color=rgba('#27AE60'),
            bold=True,
            halign='center',
            valign='middle'
        )
        self.label3.bind(size=self.label3.setter('text_size'))

        box.add_widget(btn2)
        box.add_widget(self.label3)

        # === РАЗДЕЛИТЕЛЬ 2 ===
        with box.canvas.after:
            Color(0.8, 0.8, 0.8, 1)
            Rectangle(pos=(50, Window.height * 0.22), size=(Window.width - 105, 2))

        # === БЛОК 3: Количество деталей в коробке ===

        # Подзаголовок блока 3
        header_2 = Label(
            text="Детали в коробке",
            font_size=24,
            size_hint=(1, 0.08),
            pos_hint={'center_x': 0.5, 'top': 0.32},
            color=rgba('#34495E'),
            bold=True
        )
        box.add_widget(header_2)

        # Вес без упаковки
        f_1 = TextInput(
            hint_text='Вес без уп.',
            multiline=False,
            size_hint=(0.2, 0.04),
            pos_hint={'x': 0.05, 'top': 0.26},
            input_filter='int',
            background_color=(1, 1, 1, 1),
            foreground_color=(0.1, 0.1, 0.1, 1),
            cursor_color=rgba('#9B59B6'),  # Фиолетовый
            font_size=14,
            padding=[5, 8]
        )
        self.f_1 = f_1

        # Вес пакета
        f_2 = TextInput(
            hint_text='Пакет',
            multiline=False,
            size_hint=(0.2, 0.04),
            pos_hint={'x': 0.27, 'top': 0.26},
            input_filter='int',
            background_color=(1, 1, 1, 1),
            foreground_color=(0.1, 0.1, 0.1, 1),
            cursor_color=rgba('#9B59B6'),
            font_size=14,
            padding=[5, 8]
        )
        self.f_2 = f_2

        # Вес коробки
        f_3 = TextInput(
            hint_text='Коробка',
            multiline=False,
            size_hint=(0.2, 0.04),
            pos_hint={'x': 0.49, 'top': 0.26},
            input_filter='int',
            background_color=(1, 1, 1, 1),
            foreground_color=(0.1, 0.1, 0.1, 1),
            cursor_color=rgba('#9B59B6'),
            font_size=14,
            padding=[5, 8]
        )
        self.f_3 = f_3

        # Вес детали
        f_4 = TextInput(
            hint_text='Вес детали',
            multiline=False,
            size_hint=(0.2, 0.04),
            pos_hint={'x': 0.71, 'top': 0.26},
            input_filter='float',
            background_color=(1, 1, 1, 1),
            foreground_color=(0.1, 0.1, 0.1, 1),
            cursor_color=rgba('#9B59B6'),
            font_size=14,
            padding=[5, 8]
        )
        self.f_4 = f_4

        # Кнопка расчета блока 3
        btn3 = Button(
            text="Рассчитать",
            size_hint=(0.25, 0.04),
            pos_hint={'x': 0.375, 'top': 0.2},
            background_color=rgba('#9B59B6'),
            background_normal='',
            color=(1, 1, 1, 1),
            font_size=16,
            bold=True
        )

        # Результат блока 3
        self.label4 = Label(
            text="Кол-во деталей: 0",
            font_size=20,
            size_hint=(0.9, 0.06),
            pos_hint={'center_x': 0.5, 'top': 0.14},
            color=rgba('#27AE60'),
            bold=True,
            halign='center',
            valign='middle'
        )
        self.label4.bind(size=self.label4.setter('text_size'))

        # Добавляем все виджеты блока 3
        box.add_widget(f_1)
        box.add_widget(f_2)
        box.add_widget(f_3)
        box.add_widget(f_4)
        box.add_widget(btn3)
        box.add_widget(self.label4)

        # === ФУНКЦИИ РАСЧЕТА ===

        # Функция для блока 1
        def count_final_mas_besup(instance):
            try:
                a = int(int(self.col_d.text) * float(self.ves_d.text))
                self.ves_d_label.text = f'Вес без упаковки: {a} г'
                # Автоматически подставляем в первое поле блока 2
                self.d_1.text = str(a)
            except ValueError:
                self.ves_d_label.text = 'Ошибка ввода!'

        button1.bind(on_press=count_final_mas_besup)

        # Функция для блока 2
        def count_final_mass(instance):
            try:
                a = int(self.d_1.text) + int(self.d_2.text) + int(self.d_3.text)
                self.label3.text = f'Вес с упаковкой: {a} г'
            except ValueError:
                self.label3.text = 'Ошибка ввода!'

        btn2.bind(on_press=count_final_mass)

        # Функция для блока 3
        def count_col_d(instance):
            try:
                a = int((int(self.f_1.text) - int(self.f_2.text) - int(self.f_3.text)) / float(self.f_4.text))
                self.label4.text = f'Кол-во деталей: {a}'
            except ValueError:
                self.label4.text = 'Ошибка ввода!'

        btn3.bind(on_press=count_col_d)

        return box

    def _update_rect(self, instance, value):
        """Обновление фона при изменении размера окна"""
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == "__main__":
    my_app = MyApp()
    Window.size = (450, 850)  # Оптимальный размер для мобильного
    trio.run(my_app.async_run, 'trio')
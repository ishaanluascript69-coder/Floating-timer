from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

class FloatingTimerWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(FloatingTimerWidget, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        
        self.seconds = 0
        self.is_running = False
        
        self.label = Label(text="00:00", font_size='20sp', bold=True)
        self.add_widget(self.label)
        
        self.btn_play = Button(text="▶", size_hint=(None, None), size=(60, 40))
        self.btn_play.bind(on_press=self.toggle_timer)
        self.add_widget(self.btn_play)
        
        self.btn_reset = Button(text="↺", size_hint=(None, None), size=(60, 40))
        self.btn_reset.bind(on_press=self.reset_timer)
        self.add_widget(self.btn_reset)

    def update_timer(self, dt):
        if self.is_running:
            self.seconds += 1
            mins = self.seconds // 60
            secs = self.seconds % 60
            self.label.text = f"{mins:02d}:{secs:02d}"

    def toggle_timer(self, instance):
        if not self.is_running:
            self.is_running = True
            self.btn_play.text = "⏸"
            Clock.schedule_interval(self.update_timer, 1)
        else:
            self.is_running = False
            self.btn_play.text = "▶"
            Clock.unschedule(self.update_timer)

    def reset_timer(self, instance):
        self.is_running = False
        Clock.unschedule(self.update_timer)
        self.seconds = 0
        self.label.text = "00:00"
        self.btn_play.text = "▶"

class FloatingTimerApp(App):
    def build(self):
        return FloatingTimerWidget()

if __name__ == '__main__':
    FloatingTimerApp().run()

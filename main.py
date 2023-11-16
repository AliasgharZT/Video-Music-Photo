from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.filemanager import MDFileManager
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader
from kivy.clock import Clock


Builder.load_file('style.kv')

class Style(MDAnchorLayout):
    address_file=None
    video=ObjectProperty()
    music_image=ObjectProperty()
    photo=ObjectProperty()
    time_music=ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.f=MDFileManager(
            exit_manager=self.close_filemanager,
            icon_selection_button='play',
            select_path=self.get_address,
            size_hint=(0.6,0.7),
            preview=True,
        )

    def get_address(self,path):
        self.address_file=path

    def show_filemanager(self):
        self.f.ext = ['.mp4',".mp3",'.jpg']
        self.f.selection_button.on_press=self.play_file
        self.f.show_disks()

    def close_filemanager(self,*args):
        self.f.close()

    def play_file(self):
        a=self.address_file
        if a!=None:
            if a[-3::]=='mp4':
                self.video.source=a 
                self.f.close()
            elif a[-3::]=='mp3':
                self.music=SoundLoader.load(a)
                self.f.close()
            elif a[-3::]=='jpg':
                self.photo.source=a
                self.f.close()
            else:pass 

    def _play(self):
        try:
            self.music.play()
            Clock.schedule_interval(self.chage_time_music,1) 
        except:pass 
    def _pause(self):
        try:
            self.music.stop()
            Clock.unschedule(self.chage_time_music)
            self.time_music.value=0
        except:pass 

    def chage_time_music(self,*args):
        self.time_music.value+=1

class MainApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style='Dark'

        return Style()

MainApp().run()
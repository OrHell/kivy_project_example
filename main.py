import glob,os
import shutil
import zipfile##Импорт архивации
from kivy.app import App##Импорт киви
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config##Импорт изменения окошка
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.progressbar import ProgressBar
#from kivy.core.window import Window
#Window.clearcolor = (1, 1, 0, 20)

Config.set('graphics','resizeble','0');##Изминения чтобы окошко не двигалось
Config.set('graphics','width','480');##Изминения ширина
Config.set('graphics','height','240');##Изминение высоты


class BoxApp(App):
	def build(self):
		al = AnchorLayout()
		bl = BoxLayout(orientation= 'vertical')
		self.lbl = Label(text = "")
		self.pb = ProgressBar(value = 0,max = 100)
		bl.add_widget(self.lbl)
		bl.add_widget(self.pb)
		
		bl.add_widget(Button(text = "Создать Папки", on_press = self.btn_press))
		bl.add_widget(Button(text = "Отсортировать картинки", on_press = self.btn_press_jpg))
		bl.add_widget(Button(text = "Сожмать питона", on_press = self.btn_press))
		al.add_widget(bl)
		return al

	def btn_press(self,instance):
		path = 'C:\\'
		projectname = 'sort'
		folders = \
		['png',
		'jpg',
		'py']

		fullPath = os.path.join(path , projectname)
		if not os.path.exists(fullPath):
			os.mkdir(fullPath)
		for f in folders:
			folder = os.path.join(fullPath, f)
			
			if not os.path.exists(folder):
				os.mkdir(folder)

		self.lbl.text = ('Папки созданы :3')
		self.pb.value = 100

	

	def btn_press_jpg(self,instance):
		fantasy_zip = zipfile.ZipFile('C:/sort/jpg/jpg.zip', 'w')
 
		for folder, subfolders, files in os.walk('C:/Users/Mentall/Desktop/'):
 
		    for file in files:
		        if file.endswith('.txt'):
		            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file),file), compress_type = zipfile.ZIP_DEFLATED)
		 		
		 
		fantasy_zip.close()



		for files in os.listdir("C:/Users/Mentall/Desktop"):
			if files.endswith(".txt"):
				os.remove(os.path.join("C:/Users/Mentall/Desktop",files))
		

		self.lbl.text = ('Архив готов :3')
		self.pb.value = 100

			


		


if __name__ == "__main__":##
	 BoxApp().run()##
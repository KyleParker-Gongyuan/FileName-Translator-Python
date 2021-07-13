#python 3.9.6

from json import load
import os

from os import listdir, stat, truncate

from googletrans import Translator 

# the main google trans didn't work for me

# pip install googletrans==3.1.0a0 OR pip install googletrans==4.0.0-rc1


import time

from tkinter import *

from googletrans.constants import LANGUAGES

import webbrowser

#? random note: The maximum character limit on a single text is 15k (shouldn't cause a problem	)

LangsetFrom = 'auto'
LangsetTo = 'en'

addOgWord = "Example: 你好 -> Hello (你好)"
wordOnly = "Example: 你好 -> Hello"

delOn = "ON"
delOff = "OFF"
delSwitch = False

TransStarted = "Translation ended"
TranslateError = "sorry that language code does not exist goto:"
LangURL = "https://cloud.google.com/translate/docs/languages"

translator = Translator()


OGword = False


def main():
	main_window = Tk()
	
	main_window.geometry("280x130")	

	main_window.title('Python FileName Translator (Py FnT)')
	from_lang_txt = StringVar()
	to_lang_txt = StringVar()

	def clickTrans():#late
		
		LangsetFrom = from_lang_txt.get().lower()
		LangsetTo = to_lang_txt.get().lower()
		
		if len(from_lang_txt.get()) == 0:
			LangsetFrom = "auto"
		
		if len(to_lang_txt.get()) == 0:
			LangsetTo = "en"



		if LangsetFrom not in LANGUAGES and LangsetFrom != "auto" or LangsetTo not in LANGUAGES:
			error_Window = Toplevel()

			error_Window.title('py FnT Error')
			error_Window.geometry("280x40")
			error_Window.resizable(False,False)

			workingText = Label(error_Window, text=TranslateError)

			workingText.pack()
			workingText.place(x=30,y=0)

			urlonly = Label(error_Window, text=LangURL, fg="blue", cursor="hand2")
			urlonly.pack()
			urlonly.place(x=0, y=20)

			urlonly.bind("<Button-1>", lambda e: callback(LangURL))

		else:
			MainTranslator()
		

	def delaySet():
		global delSwitch
		delSwitch = not delSwitch

		if delSwitch == True:
			delayLab.configure(text="Delay for (300+) files: "+ delOn)
			
		else:
			delayLab.configure(text="Delay for (300+) files:"+ delOff)

	def clickChangeName():
		global OGword
		OGword = not OGword
		
		if OGword == True:
			exampleWord.configure(text=addOgWord)
			exampleWord.place(x=80, y=90)
		else:
			exampleWord.configure(text=wordOnly)
			exampleWord.place(x=90, y=90)

	

	
	ez1 = Label(main_window, text="from lang")
	ez1.pack()
	ez1.place(x=0, y=0)

	ez1 = Label(main_window, text="to lang")
	ez1.pack()
	ez1.place(x=10, y=30)

	


	from_lang_E = Entry(main_window,textvariable=from_lang_txt, width=15)
	
	to_lang_E = Entry(main_window,textvariable=to_lang_txt, width=15)

	ez1 = Label(main_window, text="(if none auto detect)")
	ez1.pack()
	ez1.place(x=150, y=0)
	ez1 = Label(main_window, text="(if none auto english)")
	ez1.pack()
	ez1.place(x=150, y=30)

	startBut = Button(main_window, text="TRANSLATE", width= 10,command = clickTrans)
	
	exampleWord = Label(main_window,text=wordOnly)

	
	changeNamebutt = Button(main_window,text= "Trans Output",width=10, command=clickChangeName)

	secdelay=Button(main_window,text= "1secDelay",width=10, command=delaySet)


	delayLab = Label(main_window, text="Delay for (300+) files: "+ delOff)
	def callback(url):
		webbrowser.open(url)


	delayLab.pack()
	delayLab.place(x=85, y=110)

	secdelay.pack()
	secdelay.place(x=190, y=60)







	
	startBut.pack()
	startBut.place(x=10, y=60)
	
	changeNamebutt.pack()
	changeNamebutt.place(x=100, y=60)

	exampleWord.pack()
	exampleWord.place(x=90, y=90)

	from_lang_E.pack()
	from_lang_E.place(x= 60,y=0)
	to_lang_E.pack()
	to_lang_E.place(x= 60,y=30)

	

	main_window.resizable(False, False) 

	main_window.mainloop()

def MainTranslator():


	for files in os.listdir():
		
		file_name, file_ext = os.path.splitext(files)
		result = translator.translate(file_name, dest= LangsetTo, src = LangsetFrom)
		
		
		if OGword == True:				
			os.rename(files,result.text + "(" + file_name + ")" + file_ext)

		else:
			os.rename(files,result.text + file_ext)


		if delSwitch:
			time.sleep(1) # to many request on the same ip to fast this fixes it

		
	exit()





if __name__ == '__main__':
	main()
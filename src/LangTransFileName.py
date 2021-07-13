#python 3.9.6

from json import load
import os

from os import listdir, stat, truncate

from googletrans import Translator 

# pip install googletrans==3.1.0a0

# the main google trans didn't work for me

from tkinter import *

from googletrans.constants import LANGUAGES

import webbrowser

#? random note: The maximum character limit on a single text is 15k (shouldn't cause a problem	)

LangsetFrom = 'auto'
LangsetTo = 'en'

addOgWord = "Example: 你好 -> Hello (你好)"
wordOnly = "Example: 你好 -> Hello"

TransStarted = "Translation ended"
TranslateError = "sorry that language code does not exist goto:"
LangURL = "https://cloud.google.com/translate/docs/languages"

translator = Translator()

OGword = False

nameOfFile = __file__
def main():
	main_window = Tk()
		
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
			workingText.configure(text=TranslateError)
			workingText.place(x=30,y=150)

			urlonly.configure( text=LangURL, fg="blue", cursor="hand2")
			urlonly.bind("<Button-1>", lambda e: callback(LangURL))
	

		else:
			workingText.configure(text=TransStarted)
			workingText.place(x=90,y=150)

			urlonly.configure(text="", fg=None, cursor=None)
		
			MainTranslator()
		

	def clickChangeName():
		global OGword
		OGword = not OGword
		
		if OGword == True:
			exampleWord.configure(text=addOgWord)
		else:
			exampleWord.configure(text=wordOnly)

	main_window.geometry("300x300")

	
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

	
	changeNamebutt = Button(main_window,text= "orignal txt",width=10, command=clickChangeName)

	workingText = Label(main_window, text="waiting")

	def callback(url):
		webbrowser.open(url)


	urlonly = Label(main_window)
	urlonly.pack()
	urlonly.place(x=10, y=170)


	workingText.pack()
	workingText.place(x=110, y=150)



	
	startBut.pack()
	startBut.place(x=110, y=60)
	
	exampleWord.pack()
	exampleWord.place(x=110, y=130)

	changeNamebutt.pack()
	changeNamebutt.place(x=110, y=100)

	from_lang_E.pack()
	from_lang_E.place(x= 60,y=0)
	to_lang_E.pack()
	to_lang_E.place(x= 60,y=30)

	


	main_window.mainloop()

def MainTranslator():


	for files in os.listdir():
		
		file_name, file_ext = os.path.splitext(files)
		result = translator.translate(file_name, dest= LangsetTo, src = LangsetFrom)
		
		
		if OGword == True:				
			os.rename(files,result.text + "(" + file_name + ")" + file_ext)

		else:
			os.rename(files,result.text + file_ext)

		
	exit()





if __name__ == '__main__':
	main()
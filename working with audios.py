# Imports
import tkinter
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests
from multiprocessing.pool import ThreadPool as Pool
from multiprocessing import cpu_count
import time
import os.path
from glob import glob
from pydub import AudioSegment
from prettytable import PrettyTable


class MainWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Data cuncurrency Project")
        
        # Create buttons
        button1 = tkinter.Button(self, text="Download files without Multiprocessing pool",
                                         command=self.on_button1_click, padx=10, pady=20)
        button2 = tkinter.Button(self, text="Download files with Multiprocessing pool",
                                         command=self.on_button2_click, padx=10, pady=20)
        button3 = tkinter.Button(self, text="Scrap audio file information to text file",
                                         command=self.on_button3_click, padx=10, pady=20)
        
        # Add buttons to main window
        button1.pack()
        button2.pack()
        button3.pack()
        
    def on_button1_click(self):
         # download one file
        def download(link):
            f = link.split('/')
            p = len(f)
            name = f[p-1]
            url = link
            directory = './output/'
            filepath = os.path.join(directory, name)
            if ".wav" in url:
                response = requests.get(link)
                with open(filepath, "wb") as file:
                    file.write(response.content)
            else:
                pass
        # get page links
        def get_home_urls(a):
            headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
            }
            url = a
            page = requests.get(url)
            html = page.text
            soup = BeautifulSoup(html, "html.parser")
            urls = []
            links = soup.find_all('a', class_="buttons btn_green right")
            for link in links:
                urls.append(link['href'])
            return urls

        # download all files without multiprocessing
        def no_mpPool(url):
            t = time.time()
            for i in url:
                links = get_home_urls(i) 
                for url in links:
                    download(url)
            print(time.time() - t)

        def runNOMP():
            link = ['https://wav-sounds.com/cartoon-wav-sounds/',
                'https://wav-sounds.com/cartoon-wav-sounds-page2/',
                'https://wav-sounds.com/cartoon-wav-sounds-page3/',
                'https://wav-sounds.com/bender-futurama-wav-sounds/',
                'https://wav-sounds.com/e-mail-wav-sounds/',
                'https://wav-sounds.com/e-mail-wav-sounds-page2/',
                'https://wav-sounds.com/funny-wav-sounds/',
                'https://wav-sounds.com/funny-wav-sounds-page2/',
                'https://wav-sounds.com/movie-wav-sounds/',
                'https://wav-sounds.com/movie-wav-sounds-page2/',
                'https://wav-sounds.com/parody-wav-sounds/',
                'https://wav-sounds.com/parody-wav-sounds-page2/',
                'https://wav-sounds.com/various-wav-sounds/',
                'https://wav-sounds.com/various-wav-sounds-page2/',
                'https://wav-sounds.com/vehicle-wav-sounds/',
                'https://wav-sounds.com/vehicle-wav-sounds-page2/',
                'https://wav-sounds.com/answering-machine-wav-sounds/',
                'https://wav-sounds.com/answering-machine-wav-sounds-page2/',
                'https://wav-sounds.com/']
            no_mpPool(link)
            
        runNOMP()
        messagebox.showinfo(title="Download files without Multiprocessing", message="Files finished are downloading")
        
    def on_button2_click(self):
        def download(link):
            f = link.split('/')
            p = len(f)
            name = f[p-1]
            url = link
            directory = './output/'
            filepath = os.path.join(directory, name)
            if ".wav" in url:
                response = requests.get(link)
                with open(filepath, "wb") as file:
                    file.write(response.content)
            else:
                pass
        # get page links
        def get_home_urls(a):
            headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
            }
            url = a
            page = requests.get(url)
            html = page.text
            soup = BeautifulSoup(html, "html.parser")
            urls = []
            links = soup.find_all('a', class_="buttons btn_green right")
            for link in links:
                urls.append(link['href'])
            return urls

        # download all file with multiprocessing
        def using_mpPool(url):
            t = time.time()
            for i in url:
                links = get_home_urls(i)
                tim = []
                with Pool(cpu_count()) as pool:
                    tim.append(pool.map(download, links))
            print(time.time() - t)

        def runMP():
            link = ['https://wav-sounds.com/cartoon-wav-sounds/',
                    'https://wav-sounds.com/cartoon-wav-sounds-page2/',
                    'https://wav-sounds.com/cartoon-wav-sounds-page3/',
                    'https://wav-sounds.com/bender-futurama-wav-sounds/',
                    'https://wav-sounds.com/e-mail-wav-sounds/',
                    'https://wav-sounds.com/e-mail-wav-sounds-page2/',
                    'https://wav-sounds.com/funny-wav-sounds/',
                    'https://wav-sounds.com/funny-wav-sounds-page2/',
                    'https://wav-sounds.com/movie-wav-sounds/',
                    'https://wav-sounds.com/movie-wav-sounds-page2/',
                    'https://wav-sounds.com/parody-wav-sounds/',
                    'https://wav-sounds.com/parody-wav-sounds-page2/',
                    'https://wav-sounds.com/various-wav-sounds/',
                    'https://wav-sounds.com/various-wav-sounds-page2/',
                    'https://wav-sounds.com/vehicle-wav-sounds/',
                    'https://wav-sounds.com/vehicle-wav-sounds-page2/',
                    'https://wav-sounds.com/answering-machine-wav-sounds/',
                    'https://wav-sounds.com/answering-machine-wav-sounds-page2/',
                    'https://wav-sounds.com/']

            using_mpPool(link)
        runMP()
        messagebox.showinfo(title="Download files with Multiprocessing", message="Files are finished downloading")
        
    def on_button3_click(self):
        def writeToTextFile():
            audiofile = glob('./output/*.wav')
            table = PrettyTable()
            i=0
            table.field_names = ['Audio name', 'Frame rate', 'Channels', 'Bytes per sample', 'Maximum amplitude', 'length of audio file']
            for audio in audiofile:
                try: 
                    wav_file = AudioSegment.from_file(file = audio, format = "wav")
                    name = audio.split('\\')[1][:-4]
                    table.add_row([name,wav_file.frame_rate,wav_file.channels,wav_file.sample_width,wav_file.max,len(wav_file) ])
                except FileNotFoundError:
                    pass
            table.align = 'l'
            with open("./output/results.txt", "w") as file:
                file.write(table.get_string())
        writeToTextFile()
        messagebox.showinfo(title="Audio scraping", message="Audio files have been scraped to text file")

# Create and start main window
window = MainWindow()
window.geometry("300x250")
window.geometry("400x250+500+250") 
window.mainloop()
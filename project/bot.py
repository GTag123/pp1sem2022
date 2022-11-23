import datetime
import os
import random
import requests
import pyttsx3
import speech_recognition as sr
from datetime import date
from fuzzywuzzy import fuzz
from time import sleep
import sys

opts = {
    'names': ('илья', 'помощник', 'ассистент'),
    'tbr': ('скажи', 'вруби', 'намути', 'сколько', 'какой', 'какое', 'какая', 'добавь', 'поставь', 'посчитай', 'мне'),
    'cmds': {
        'greeting': ('привет', 'привет друг', 'здравствуйте', 'приветик', 'добрый день', 'хай', 'приветствую', 'здравствуй'),
        'create_task': ('создай задачу', 'сделай заметку'),
        'dating': ('сегодня число', 'число'),
        'timing': ('который час', 'времени', 'время'),
        'weekday': ('сегодня день недели', 'день недели'),
        'timer': ('таймер', 'засеки время'),
        'weather': ('какая погода ', 'погода'),
        'factorial': ('факториал', 'факториал'),
        'playMusic': ('музыку', 'музон', 'музяка', 'трек'),
        'yesorno': ('да или нет', 'нет или да'),
        'support1': ('мне страшно', 'я волнуюсь', 'скоро сессия'),
        'support2': ('я устал', 'мне надоело делать лабораторные работы'),
        'support3': ('Что делать если я не могу посчитать факториал'),
        'support4': ('что будет если я не справлюсь с учебой'),
        'support5': ('учеба важна в жизни', 'учеба играет роль в жизни'),
        'timetable': ('расписание', 'пары'),
        'end': ('пока', 'до свидания', 'до встречи')
    }
}

'Создать заметку, Число\Время\День недели, Поставить таймер, Погода, Факториал, проиграть музыку, Оказать поддержку, сказать расписание'


class Bot:
    def __init__(self, commonui, error=False):
        self.ui = commonui
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

        with self.m as source:
            self.r.adjust_for_ambient_noise(source)

        self.speak_engine = pyttsx3.init()

        if (error):
            self.speak('Бот перезапущен из-за ошибки')
            self.speak('Я снова приветствую вас')
        else:
            self.speak('Бот запущен')
            self.speak('Я приветствую вас')

    def callback(self):

        #if text -> execute
        #else voice recognize...



        try:
            with self.m as mic:
                self.r.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = self.r.listen(source=mic)
                voice = self.r.recognize_google(audio_data=audio, language='ru-RU').lower()
            print('Распознано: ' + voice)

            if voice.startswith(opts['names']): # основная фун-ия обработки
                cmd = voice

                for x in opts['names']:
                    cmd = cmd.replace(x, "").strip()

                for x in opts['tbr']:
                    cmd = cmd.replace(x, "").strip()

                cmd = self.recognize_cmd(cmd)
                self.execute_cmd(cmd['cmd'])

            else:
                return voice

        except sr.UnknownValueError:
            print('Голос не распознан!')


    def listenEN(self):
        try:
            with self.m as mic:
                self.r.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = self.r.listen(source=mic)
                return self.r.recognize_google(audio_data=audio, language='en-EN').lower()
        except sr.UnknownValueError:
            pass


    def recognize_cmd(self,cmd):
        RC = {'cmd': '', 'percent': 0}
        for c, v in opts['cmds'].items():

            for x in v:
                vrt = fuzz.ratio(cmd, x)
                if vrt > RC['percent']:
                    RC['cmd'] = c
                    RC['percent'] = vrt

        return RC


    def execute_cmd(self, cmd):
        if cmd == 'greeting':
            self.greeting()
        elif cmd == 'create_task':
            self.create_task()
        elif cmd == 'dating':
            self.dating()
        elif cmd == 'timing':
            self.timing()
        elif cmd == 'weekday':
            self.weekday()
        elif cmd == 'timer':
            self.timer()
        elif cmd == 'weather':
            self.weather()
        elif cmd == 'factorial':
            self.factorial()
        elif cmd == 'playMusic':
            self.playMusic()
        elif cmd == 'yesorno':
            self.yesorno()
        elif cmd == 'support1':
            self.support1()
        elif cmd == 'support2':
            self.support2()
        elif cmd == 'support3':
            self.support3()
        elif cmd == 'support4':
            self.support4()
        elif cmd == 'support5':
            self.support5()
        elif cmd == 'timetable':
            self.timetable()
        elif cmd == 'end':
            self.speak('рад помочь, до свидания')
        else:
            self.unclear()


    def speak(self, speech):

        # изменение текста окна
        self.ui.changeBotText(speech)

        self.speak_engine.say(speech)
        self.speak_engine.runAndWait()
        self.speak_engine.stop()


    def greeting(self):
        self.speak('Приветствую вас')


    def create_task(self):
        self.speak('Что добавим в список дел?')
        task = self.callback()
        with open('todo-list.txt', 'a') as file:
            file.write(f'{task}\n')
        self.speak(f'Задача "{task}" успешно добавлена')


    def dating(self):
        today = date.today()
        self.speak(f'Сегодня {today}')


    def timing(self):
        dt = datetime.datetime.now()
        today = dt.time()
        correct = {0: '00', 1: '01', 2: '02', 3: '03', 4: '04', 5: '05', 6: '06', 7: '07', 8: '08', 9: '09'}
        hours = today.hour
        minutes = today.minute
        seconds = today.second
        if today.hour < 10:
            hours = correct[today.hour]
        if today.minute < 10:
            minutes = correct[today.minute]
        if today.second < 10:
            seconds = correct[today.second]
        self.speak(f'Сейчас {hours}:{minutes}:{seconds}')



    def weekday(self):
        dt = datetime.datetime.now()
        wd = {0: 'понедельник', 1: 'вторник', 2: 'среда', 3: 'четверг', 4: 'пятница', 5: 'суббота', 6: 'воскресенье'}
        today = wd[dt.weekday()]
        self.speak(f'Сегодня {today}')


    def timer(self):
        self.speak('На сколько секунд поставить таймер?')
        seconds = self.callback()
        try:
            s = int(seconds)
            self.speak('Время пошло!!!')
            sleep(s / 2)
            if s > 5:
                self.speak('Осталась половина')
            sleep((s / 2) - 1)
            os.system(r'C:\Users\napap\source\repos\PythonApplication1\PythonApplication1\1\timerring.mp3')
            self.speak('Время вышло!!!')
        except ValueError:
            self.speak('Не понялa Вас')
        except TypeError:
            self.speak('Не понялa Вас')


    def weather(self):
        self.speak('В каком городе Вы хотите узнать погоду?')
        city = self.callback()
        cts = {'москва': 'Moscow', 'нахабино': 'Nakhabino', 'санкт-петербург': 'Saint Petersburg', 'волгоград': 'Volgograd',
               'сочи': 'Sochi', 'омск': 'Omsk', 'чита': 'Chita', 'рязань': 'Ryazan'}
        city = cts[city]
        loc = f'{city},RU'
        req = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'q': f'{loc}', 'units': 'metric', 'lang': 'ru',
                                   'APPID': '4b40bec5212b532c48066246c26cb887'}).json()

        temp = str(int(req['main']['temp']))
        end = temp[-1]
        ends = {0: '0 градусов', 1: '1 градус', 2: '2 градусa', 3: '3 градуса', 4: '4 градуса'}
        if -1 < int(end) < 5:
            temp = ends[int(end)]
        else:
            temp = end + ' градусов'
        press = int((req['main']['pressure']) * 0.75188)

        desc = req['weather'][0]['description']
        hum = req['main']['humidity']

        rc = {'Moscow': 'Москве',
              'Nakhabino': 'Нахабино',
              'Saint Petersburg': 'Санкт-Петербурге',
              'Volgograd': 'Волгограде',
              'Sochi': 'Сочи',
              'Omsk': 'Омске',
              'Chita': 'Чите',
              'Ryazan': 'Рязани'}
        city = rc[city]

        self.speak(f'В {city} {desc}, {temp}, давление: {press}, влажность: {hum}%')


    def factorial(self):
        self.speak('Факториал какого числа Вы хотите посчитать?')
        n = str(self.callback())
        try:
            k = int(n)
        except ValueError:
            return 'Я ожидал натуральное число('
        f = 1
        for i in range(2, k + 1):
            f = f * i
        self.speak(f'{f}')


    def yesorno(self):
        a = random.randint(0, 1)
        if a == 0:
            self.speak('Да!')
        else:
            self.speak('Нет!')


    def playMusic(self):
        self.speak('Какую песню включить?')
        song = self.listenEN()
        self.speak('Наслаждайтесь')
        path = "C:\\Users\\napap\\source\\repos\\PythonApplication1\\PythonApplication1\\Music\\" + f"{song}" + ".mp3"
        os.system(path)
        sys.exit(0)


    def support1(self):
        self.speak('Конечно, студенческая жизнь тяжела, но многие через это проходят. У вас тоже всё получится!')

    def support2(self):
        self.speak('Отдохните час, и с новыми силами приступайте к работе. Если это не поможет, то приступите к работе в новый день со свежей головой и новыми силами!')

    def support3(self):
        self.speak('Вы можете обратиться ко мне назвав соответствующую команду и я все сделаю за вас!')

    def support4(self):
        self.speak('Если вы не будете закрывать долги вовремя, то вас могут отчислить! Распределите ваше время и выполните поставленные задачи в срок во избежание опасных ситуаций!')

    def support5(self):
        self.speak('Ученье свет, а не ученье тьма! А сам могу сказать, что учение занимает одну из самых главных ролей в жизни человека.')



    def timetable(self):
        timetable = {'понедельник': 'второй парой Физика, третьей дискретная математика, четвертой основы программирования и пятой проектная практика',
                     'вторник': 'первой парой основы программирования, второй история, третьей физкультура и четвёртой линейная алгебра',
                     'среда': 'дистанционный день. вторая пара английский, третья математический анализ, четвёртая теория графов и пятой основы программирования',
                     'четверг': 'первой и третьей парой математический анализ, второй общая алгебра, четвёртой английский и пятой физкультура',
                     'пятница': 'дистанционный день. первой и второй парой общая алгебра, третьей физика, четвёртой история и пятая линейная алгебра',
                     'суббота': 'ура пар нет',
                     'воскресенье': 'ура пар нет'}
        self.speak('в какой день вы хотите узнать расписание?')
        dw = self.callback()
        self.speak(timetable[dw])


    def unclear(self):
        self.speak('Простите: не понимаю Вас')

# r = sr.Recognizer()
# m = sr.Microphone()
#
# with m as source:
#     r.adjust_for_ambient_noise(source)
#
# speak_engine = pyttsx3.init()
#
# speak('Бот запущен')
# speak('Я приветствую вас')
#
# while True:
#     callback()
#     sleep(0.1)

if __name__ == "__main__":
    print("Main initialization")
    bot = Bot()
    while True:
        bot.callback()
        sleep(0.1)
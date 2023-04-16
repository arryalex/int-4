import configparser
import os,json
from threading import Thread
from zipfile import ZipFile
from collections.abc import Iterable
import time
from rich.tree import Tree
import random
import asyncio
from datetime import datetime, timedelta
from datetime import datetime
from datetime import date
from os import path
import  pytz
from itertools import combinations
from datetime import datetime as rd
from rich.console import Console
Consol_ =Console(color_system="256", highlight=True, record=True) 
from rich.panel import Panel
from operator import itemgetter
from itertools import groupby
from pytz import timezone
from PIL import Image,ImageDraw,ImageFont
from rich import box
import telepot
from unzip import unzip
from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')
unzip()
API_KEY = str(config['bot authentication']['API'])
bot = telepot.Bot(API_KEY)
filename_1 = "Mantrigame.json"
today = date.today()
IST = pytz.timezone('Asia/Kolkata')


THIS_FOLDER = path.dirname(path.abspath(__file__))
emailfile_1=path.join(THIS_FOLDER,filename_1)
dictlist_1=[]
with open(emailfile_1,encoding='utf-8') as f: 
    dictlist_1 = json.load(f)




def flatten(lis):
     for item in lis:
         if isinstance(item, Iterable) and not isinstance(item, str):
             for x in flatten(item):
                 yield x
         else:        
             yield item

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat,end='\r')
        time.sleep(1)
        time_sec -= 1


def loadData(file):
  with open(file) as f:
    gobble = json.loads(f.read())
    return gobble


def Update_daily_numeric(theirloopvalue:int,combination_number :int,get_createTime):
  
  kids = loadData(file=f"Numeric Collections/{get_createTime}/Combination-{combination_number}.json")
  newVersion = []
  for each in kids:
    if theirloopvalue ==each['The loop value']:
      newRecord ={}
      newRecord['The loop value'] = theirloopvalue
      newRecord['How much Time in a Day'] = each['How much Time in a Day']+1
      newVersion.append(newRecord)
    else:
      newRecord = {}
      newRecord['The loop value'] = each['The loop value']
      newRecord['How much Time in a Day'] = each['How much Time in a Day']
      newVersion.append(newRecord)
    with open(f"Numeric Collections/{get_createTime}/Combination-{combination_number}.json",'w') as f:
      f.write(json.dumps(newVersion,indent=2))

def card_gen(round:str,num:dict,result:str=None,emoji:dict=None):
    today = date.today()
    d4 = today.strftime("%b-%d-%Y")
    now = datetime.now()
    cd = loadData(file='numeric values.json')
    #----------DATE-TIME-----------------------------------------

    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    d4 = today.strftime("%b-%d-%Y")
    image = Image.open('Pictures/Parity.jpg')
    #----------FONTS-----------------------------------------

    Date_font = ImageFont.truetype('Fonts/1980sWriter.ttf', size=60)
    prediction_font = ImageFont.truetype('Fonts/101! StaR StuDDeD.ttf', size=30)
    value_font = ImageFont.truetype('Fonts/LEMONMILK-Regular.otf', size=20)
    value_font_2 = ImageFont.truetype('Fonts/LEMONMILK-Regular.otf', size=40)
    time_font = ImageFont.truetype('Fonts/alarm clock.ttf', size=50)
    emoji_font = ImageFont.truetype('Fonts/Satluj.ttf', size=60)

    #----------IMAGE-CLIENT------------------------------

    draw = ImageDraw.Draw(image) 

    #----------PERAMETERS------------------------------
    width = 312
    width_2 = 312
    shape_system_2 = 0

    #------------------WEBSITE-LOGO--------------------------------
    draw.text(text='M   A   N   T   R   I   G   A   M   E ', xy=[800,220],font=value_font,fill='rgb(154,176,180)')

    #------------------DATE_TIME--------------------------------
    draw.text(text=current_time, xy=[1870, 230],font=time_font,fill='rgb(154,176,180)')
    draw.text(text=d4, xy=[1870, 1150],font=Date_font,fill='rgb(154,176,180)')

    #------------------ROUND-MANGE-----------------------------------------
    draw.text(text='PT - 1', xy=[100,1150],font=Date_font,fill='rgb(154,176,180)')
    draw.text(text=f'Round - {round} ', xy=[100, 210],font=value_font_2,fill='rgb(154,176,180)')
    r = 0

    for i in num:
        if result is not None :
            if emoji[r]==0:
                draw.text(text='x', xy=[530,width],font=emoji_font,fill='rgb(154,176,180)')
            else :
                draw.text(text='n', xy=[530,width],font=emoji_font,fill='rgb(154,176,180)')
            draw.text(text=str(result), xy=[430,width],font=prediction_font,fill='rgb(154,176,180)')

        draw.text(text=i, xy=[180,width],font=prediction_font,fill='rgb(154,176,180)')
        draw.text(text=str(cd[r][f'The loop value']), xy=[650,width],font=prediction_font,fill='rgb(154,176,180)')
        width += 86 ; width_2 += 86 ;r +=1
    r = 0  
    for i in num:
        shape_system = 0
        shape = [(755, 298+shape_system_2), (840,375+shape_system_2)]
        for i in range(int(cd[r][f'The loop value'])):
            shape = [(755+shape_system, 298+shape_system_2), (840+shape_system,375+shape_system_2)]
            shape_system += 87 
            draw.rectangle(shape, fill='rgb(154,176,180)',outline='#000000')
        shape_system_2 += 85
        r +=1
    image.save('Pictures/Parity-Round-1.Png')

def Update_database(collection:int,incoming:int =None):
  kids = loadData(file='numeric values.json')
  newVersion = []
  for each in kids:
    if collection ==each['Collection']:
      newRecord ={}
      newRecord['Collection'] = collection
      if incoming is not None :
        newRecord['The loop value'] = each['The loop value']+1
      if incoming == None :  
        newRecord['The loop value'] = 0
      newVersion.append(newRecord)
    else:
      newRecord = {}
      newRecord['Collection'] = each['Collection']
      newRecord['The loop value'] = each['The loop value']
      newVersion.append(newRecord)
    with open('numeric values.json','w') as f:
      f.write(json.dumps(newVersion,indent=2))



def divide_chunks(l):
    n = 2
    for i in range(0, len(l), n):
        yield l[i:i + n]

def Combo(numbers):
    groupsOf = 2 #elements
    combos = [
        x for x in combinations(numbers, groupsOf)
    ]
    return combos



def create_numeric(numeric,get_createTime):
    today = date.today()
    d4 = today.strftime("%b-%d-%Y")
    if numeric == 1 :
        try :
            os.mkdir(f'Numeric Collections/{get_createTime}')
        except FileExistsError :
            pass
    for i in range(3):
        i +=1
        with open(f"template.json") as json_file:
            data = json.load(json_file)
        json_object = json.dumps(data,indent = 1)
        with open(f"Numeric Collections/{get_createTime}/Combination-{i}.json", "w") as outfile:
            outfile.write(json_object)


def Prediction(Results,Final_result,get_createTime):
    Get_result_price=int(Results['resultPrice']) #filter Last Row Result Price
    Get_result_logTime= Results['logTime']#filter Last Row Result log
    get_current_period = int(Results['period'])+1#filter currect period
    server_time =  rd(year=2022,month=8,day=int(Get_result_logTime[8:10]),hour=int(Get_result_logTime[11:13]),minute=int(Get_result_logTime[14:16]),second=int(Get_result_logTime[17:]))
    Consol_.print(Panel.fit(f'[bold italic]Server Time >> {server_time}'),justify='center',style='light_sea_green')
    server_time_timestemp = server_time.timestamp()
    dictlist = loadData('Emred.json')
    find_json_list = [x for x in dictlist if x['resultPrice'] ==Get_result_price] # Find All same numbers i json Database
    json_list=[]
    for i in find_json_list:
        try :
            period = i['period'] #get Result Period
            Last_one = period+1 # Adding + So that Can Get Number After This one
            output_last= [x for x in dictlist if x['period'] == Last_one] 
            json_list.append(output_last[0]['resultNum'])
        except IndexError as E :
            Consol_.print(Panel.fit('[italic yellow]<< INDEX Error BE Carefull >>'),style='red1')
            pass
    
    Values  = [
            {   "number":0,
                "Value":json_list.count(0)
            },  
            {   "number":1,
                "Value":json_list.count(1)
            },
            {   "number":2,
                "Value":json_list.count(2)
            },
            {   "number":3,
                "Value":json_list.count(3)
            },
            {   "number":4,
                "Value":json_list.count(4)
            },
            {   "number":5,
                "Value":json_list.count(5)
            },
            {   "number":6,
                "Value":json_list.count(6)
            },
            {   "number":7,
                "Value":json_list.count(7)
            },
            {   "number":8,
                "Value":json_list.count(8)
            },
            {   "number":9,
                "Value":json_list.count(9)
            },  
        ]
    Data_process = sorted(Values,key=lambda k: k["Value"],reverse=True)
    numbers = []
    for i in Data_process:
        numbers.append(i['number'])
    HIGH =  str(list(flatten(numbers[:4])))[1:-1]
    LOW =  str(list(flatten(numbers[4:8])))[1:-1]
    lowest =  str(list(flatten(numbers[6:])))[1:-1]
    Combination = [HIGH,LOW,lowest]
    tree = Tree(Panel.fit('[bold italic]Processed Datasets ',style='dodger_blue1'))
    tree.add((Panel.fit(f'{HIGH} ',style='magenta',subtitle=';HIGH')))
    tree.add((Panel.fit(f'{LOW} ',style='cyan',subtitle='LOW')))
    tree.add((Panel.fit(f'{lowest} ',style='cyan',subtitle='LOW')))
    Consol_.print(Panel.fit(tree),style='green1')
    result_number =str(Final_result["resultNum"])
    emodi_dic = []
    XD = loadData(file='numeric values.json')
    x = 1
    z = 0
    for i in Combination : 
        see = str(i)
        if result_number in see :
            Consol_.print(Panel.fit(f"[italic bold]{result_number} found Number in {i}",style='green1'))
            emodi_dic.append(1)
            Update_daily_numeric(theirloopvalue=XD[z]['The loop value'],combination_number=z+1,get_createTime=get_createTime)
            Update_database(x)
            x += 1
            z += 1
        else :
            Consol_.print(Panel.fit(f"[italic bold]{result_number} not found in {i}",style='green1'))
            emodi_dic.append(0)
            Update_database(x,incoming=1)
            x += 1
            z += 1
    card_gen(num=Combination,result=result_number,round=get_current_period,emoji=emodi_dic)
    #bot.delete_message(chat_id=bot_message.chat.id,message_id=bot_message.id)
    bot.sendPhoto(photo=open('Pictures/Parity-Round-1.Png', 'rb'),chat_id=1518832426)

    

i = 1
for results in dictlist_1:
    today = date.today()
    d4 = today.strftime("%b-%d-%Y")
    createTime = str(results['createTime'])
    get_createTime =  (createTime.split(' '))[0]
    print(get_createTime)
    path = f'Numeric Collections/{get_createTime}'
    isExist = os.path.exists(path)
    if isExist == False :
        Consol_.print(Panel.fit('File Not Found Error !!!!',box=box.DOUBLE_EDGE),justify='center',style='deep_sky_blue4')
        with Consol_.status('[italic green1]generating directories........'):
            create_numeric(numeric=1,get_createTime=get_createTime)
    try :
        if __name__ == "__main__":
            Prediction(Results=results,Final_result=dictlist_1[i],get_createTime=get_createTime)
        Consol_.rule(title=f'[talic cyan]Next-IN => {i}', style='rule.line',characters='=')
        i+=1
    except Exception as E :
        Consol_.print_exception()
        Consol_.rule(title=f'[talic red]Next-IN => {i}', style='rule.line',characters='=')
        i+=1
import requests
import urllib
from os import path
import json




class Mantrimalls():
    def __init__(self) -> None:
        self.API = "https://mantrigame.com"
    
    def login(self):
        response = requests.post(f'{self.API}/lottery-backend/glserver/user/login?mobile=%2B919340801353&password=0c0de11aa82a89a6cdff736120af08e6')
        if response.status_code != 200: 
            return json.loads(response.text)
        else:
            self.json = json.loads(response.text)
            self.cookies = response.headers['set-cookie']
            self.cookie_data_JSESSIONID = self.cookies.split(';')[0]
            self.cookie_data_rememberMe = self.cookies.split(';')[6].split('rememberMe=')[1]
    
    def get_result(self,gameType: str,pageNum:str,pageSize:str):
        response = requests.post(f'{self.API}/lottery-backend/glserver/lottery/findGameLogByPage?gameType={gameType}&pageNum={pageNum}&pageSize={pageSize}',headers={"Cookie" :f"{self.cookie_data_JSESSIONID};rememberMe={self.cookie_data_rememberMe}"})
        if response.status_code != 200: 
            return json.loads(response.text)
        else: return json.loads(response.text)

    def get_user(self,gameType: str,pageNum:str,pageSize:str):
        response = requests.post(f'{self.API}/lottery-backend/glserver/lottery/findUserLogByPage?gameType={gameType}&pageNum={pageNum}&pageSize={pageSize}',headers={"Cookie" :f"{self.cookie_data_JSESSIONID};rememberMe={self.cookie_data_rememberMe}"})
        if response.status_code != 200: 
            return json.loads(response.text)
        else: return json.loads(response.text)

    def bet(self,gameType: str, Money :str, Number : str):
        response = requests.post(f'{self.API}/lottery-backend/glserver/lottery/pour?gameType={gameType}&pourType={Number}&pourCount=1&pourMoney={Money} ',headers={"Cookie" :f"{self.cookie_data_JSESSIONID};rememberMe={self.cookie_data_rememberMe}"})
        if response.status_code != 200: 
            return json.loads(response.text)
        else: return json.loads(response.text)

    def bonus(self):
        response = requests.post(f'{self.API}/lottery-backend/glserver/cash/getRedPacket?mobile=+917999608196&code=189427a4f4a14513ba93ed60c4b498a7')
        if response.status_code != 200: 
            print(json.loads(response.text))
            return json.loads(response.text)
        else: 
            print(json.loads(response.text))
            return json.loads(response.text)
    def SID(self):
        response = requests.post(f'{self.API}/lottery-backend/glserver/user/login?mobile=%2B919340801353&password=0c0de11aa82a89a6cdff736120af08e6')
        if response.status_code != 200: 
            return json.loads(response.text)
        else:
            self.json = json.loads(response.text)
            self.cookies = response.headers['set-cookie']
            self.cookie_data_JSESSIONID = self.cookies.split(';')[0]
            self.cookie_data_rememberMe = self.cookies.split(';')[6].split('rememberMe=')[1]
            return {"Cookie" :f"{self.cookie_data_JSESSIONID};rememberMe={self.cookie_data_rememberMe}"}
    

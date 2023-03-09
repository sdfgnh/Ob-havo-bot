from aiogram.types import Message, User, KeyboardButton, InlineKeyboardButton
from aiogram import Router, Dispatcher, Bot
from aiogram.filters.command import Command
from asyncio import run
from abc import ABC, abstractmethod
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from config import API_TOKEN


import requests
def get_date(city):
        data = {
            "q": city,
            "appid": API_TOKEN
        }
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather", params=data)
        if response.status_code == 200:
            response = response.json()
            return response["main"]["temp"]-273.15
        return None
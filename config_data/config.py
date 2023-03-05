from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str 

@dataclass
class UsId:
    id: str             


@dataclass
class Config:
    tg_bot: TgBot
    user_id: UsId


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')), user_id=UsId(id=int(env('MY_ID'))))
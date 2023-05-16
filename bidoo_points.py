import configparser
import asyncio
import webbrowser
import requests
import re
import time
import pyautogui
from bs4 import BeautifulSoup
from telethon import TelegramClient
from telethon.sync import events

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

def open_bidoo_link(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Check if Cloudflare anti-bot page is present
    if soup.find('title', string='Bidoo | Captcha'):
        print('Cloudflare anti-bot page detected')
        # Implement logic to solve the Cloudflare challenge
        webbrowser.open(url)
        time.sleep(8)
    else:
        webbrowser.open(url)

async def main():
    async with TelegramClient('anon', api_id, api_hash) as client:
        # channel_name = 'puntateaste'
        channel_name = 'bidoo_puntate_gratis'
        channel_entity = await client.get_entity(channel_name)
        
        ignore_counter = 0
        limit = 0
        limit = ignore_counter + limit

        if(limit):
            print('Opening old messages...')
            counter = 0
            async for message in client.iter_messages(channel_entity, limit = limit + 1):
                if (counter > ignore_counter):
                    if message.text is not None:
                        link_match = re.search(r'\(https?://it\.bidoo\.com/\S+\)', message.text)
                        if link_match:
                            link = link_match.group(0)[1:-1]
                        else:
                            link_match = re.search(r'https?://it\.bidoo\.com/\S+', message.text)
                            if link_match:
                                link = link_match.group(0)
                            else:
                                link = None

                        if link:
                            time.sleep(1)
                            print(f'Number {counter}')
                            open_bidoo_link(link)
                            time.sleep(2)
                            pyautogui.hotkey('ctrl', 'w')
                            counter += 1
                else:
                    counter += 1

        print('Listening for messages...')

        @client.on(events.NewMessage)
        async def handler(event):
            url = None
            if event.message.text is not None:
                url_match = re.search(r'\(https?://it\.bidoo\.com/\S+\)', event.message.text)
                if url_match:
                    url = url_match.group(0)[1:-1]
                else:
                    url_match = re.search(r'https?://it\.bidoo\.com/\S+', event.message.text)
                    if url_match:
                        url = url_match.group(0)

            if url:
                print(f'Link: {url}\n')
                open_bidoo_link(url)

        await client.run_until_disconnected()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

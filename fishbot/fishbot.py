from time import sleep
from discord import Client
from pyautogui import write, press
def fish():
    sleep(3)
    write('%f')
    press('enter')
def verify(expression):
    write('%v ' + str(eval(expression)))
    press('enter')
class MyClient(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.runBool = False
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        if message.author == self.user:
            return
        if (str(message.author) == "Virtual Fisher#7036") and message.embeds and self.runBool:
            embed = message.embeds[0]
            if(embed.title == 'Anti-bot\n%verify <result>'):
                verify(embed.description[52:-3])
                fish()
            elif(embed.title == 'You caught:'):
                fish()
            else:
                print(embed.title, '---', embed.description, sep='\n')
        if message.content == '==toggle' or message.content == '==t':
            self.runBool = not self.runBool
            await message.channel.send('Toggled ' + ('On' if self.runBool else 'Off'))

client = MyClient()
client.run('ODQ0MTg4ODExMTI3MDI5Nzkw.YKOyGA.Q4_ZBuz-QBfjL4xpgI3JMnNY76Y')
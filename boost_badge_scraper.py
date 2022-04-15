import discum, time 
import os
from colorama import init,Fore
init()

os.system("cls")


print(f"""{Fore.CYAN}
                   
───▄▄─▄████▄▐▄▄▄▌
──▐──████▀███▄█▄▌
▐─▌──█▀▌──▐▀▌▀█▀
─▀───▌─▌──▐─▌
─────█─█──▐▌█
~ L u n n y | S c r a p e r ~
                   {Fore.RESET}                                                             
           """)


token = input("Account Token: ")
guild_id = input("Server ID: ")
channel_id = input("Channel ID: ")
bot = discum.Client(token= token, log=True)

bot.gateway.fetchMembers(guild_id, channel_id, keep=['public_flags','username','discriminator','premium_since', 'premium_type'],startIndex=0, method='overlap')
@bot.gateway.command
def memberTest(resp):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched)+' members fetched')
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()

bot.gateway.run()

def __get_nitros(flags) -> list[str]:
    
        NITRO = {
            0 << 1:  'Nitro Classic',
            2 << 2:  'Nitro',
        }

        nitros = []

        for nitros_flag, nitros_name in NITRO.items():
            if flags & nitros_flag == nitros_flag:
                nitros.append(nitros_name)

        return nitros

with open('ids.txt', 'w', encoding="utf-8") as file :
    for memberID in bot.gateway.session.guild(guild_id).members:
        id = str(memberID)
        nitro = str(bot.gateway.session.guild(guild_id).members[memberID].get('premium_type'))
        temp = bot.gateway.session.guild(guild_id).members[memberID].get('public_flags')
        user = str(bot.gateway.session.guild(guild_id).members[memberID].get('username'))
        disc = str(bot.gateway.session.guild(guild_id).members[memberID].get('discriminator'))
        username = f'{user}#{disc}'
        creation_date = str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(((int(id) >> 22) + 1420070400000) / 1000)))
        if temp != None:
            z = __get_nitros(temp)
            if len(z) != 0:
                nitros = ', '.join(z)
            n = __get_nitros(temp)
            if len(z) != 0:
                nitros = ', '.join(z)
                print(f'{user}#{disc} ~ {id} ~ {nitro}')
                file.write(f'{id}\n')


            
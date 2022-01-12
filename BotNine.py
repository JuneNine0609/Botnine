import discord
import asyncio
import random

from discord import activity

client = discord.Client()

token = "OTI3Mzc0NTE5NjU4NzQ5OTk0.YdJS0w.rU4xX8AjBmX-ktsMuWlTko_vrjI"

@client.event
async def on_ready():

    print(client.user.name)
    print('I am ready!')
    game = discord.Game('봇나인 도움 이라고 하시면 봇나인과 대화를 할 수 있는 명령어들을 알려드려요!')
    await client.change_presence(status=discord.Status.online, activity=game)

    async def bt(games):
        await client.wait_until_ready()

        while not client.is_closed():
            for g in games:
                await client.change_presence(status = discord.Status.online, activity = discord.Game(g))
                await asyncio.sleep(10)

@client.event
async def on_message(message):
    if message.content.startswith('/유튜브'):
        await message.channel.send('https://www.youtube.com/channel/UCAf1WUT6KUSt4ZinqvaGBsA')
        
    if message.content.startswith('/준나인'):
        await message.channel.send("**나 만든 놈**")

    if message.content.startswith('/채널'):
        await message.channel.send('구독과 좋아요....~~라고 할줄 알았냐~~')
    
    if message.content.startswith('/김난다'):
        await message.channel.send('**구독자 100명 유튜버**')

    if message.content.startswith('/청한'):
        await message.channel.send('**zi존나느ㄴ샌쥬핑크팬티**')

    if message.content.startswith('/트위치'):
        await message.channel.send('https://www.twitch.tv/junenine_06')

    if message.content.startswith('/가라고'):
        await message.channel.send('~~아잉놈아~~')

    if message.content.startswith('/어몽어스'):
        await message.channel.send('AMOGUS')

    if message.content.startswith('/어모거스'):
        await message.channel.send('https://cdn.pixabay.com/photo/2021/04/21/10/17/meme-6195988_960_720.png')

    if message.content.startswith('/초대'):
        await message.channel.send('https://discord.com/api/oauth2/authorize?client_id=927374519658749994&permissions=2048&scope=bot')
    
    if message.content.startswith('/디스코드 서버'):
        await message.channel.send('https://discord.gg/6vSrcgugUE')

    if message.content.startswith('/안녕'):
        await message.channel.send('ㅎㅇ')

    if message.content.startswith('/니얼굴'):
        await message.channel.send('~~윤겔라~~')

    if message.content.startswith('/욕'):
        await message.channel.send('https://www.police.go.kr/')

    if message.content.startswith('/야구동영상'):
        await message.channel.send('https://www.koreabaseball.com/')

    if message.content.startswith('/뉴빈'):
        await message.channel.send('**개귀여운 준나인 동생**')

    if message.content.startswith('/영상 추천'):
        await message.channel.send(random.choice(['https://www.youtube.com/watch?v=T0CAD3Kimvg&t=5', 'https://www.youtube.com/watch?v=-jIX_u0SK9M', 'https://www.youtube.com/watch?v=eDzcVCpRplA', 'https://www.youtube.com/watch?v=jL_2Bl63GIQ', 'https://www.youtube.com/watch?v=C3ufSD9zgoU&t=10s', 'https://www.youtube.com/watch?v=12tPe7DfInM', 'https://www.youtube.com/watch?v=IvBZp6MriEk', 'https://www.youtube.com/watch?v=pFXsTghZzig', 'https://www.youtube.com/watch?v=KnQiO764RxA', 'https://www.youtube.com/watch?v=2lUfBbvNIbY', 'https://www.youtube.com/watch?v=F5h5FC3qthk', 'https://www.youtube.com/watch?v=TDVxUlDqD3I&t=229s', 'https://www.youtube.com/watch?v=vzknxLB0zOM', 'https://www.youtube.com/watch?v=ZqAiBF7VAs0&t=175s', 'https://www.youtube.com/watch?v=jGwbqJXWcqY']))

    if message.content.startswith('/어그로'):
        await message.channel.send('**미안하다 이거 보여주려고 어그로끌었다.. 준나인 영상 수준 ㄹㅇ실화냐? 진짜 세계관최강자들의 편집이다.. 그찐따같던 준나인이 맞나? 진짜 준나인은 전설이다..진짜옛날에 맨날준나인봘는데 준나인 구독자 하나하나 늘어가는거 보면 진짜내가다 감격스럽고 준나인 인트로부터 아웃트로까지 가슴울리는장면들이 뇌리에 스치면서 가슴이 웅장해진다.. 그리고 극장판 에 김난다 앞에 운석날라오는 거대한 걸 준나인 갑자기 순식간에 나타나서 부숴버리곤 개간지나게 김난다가 없다면 유튜브를 지킬 자는 나밖에 없다 라며 바람처럼 사라진장면은 진짜 준나인처음부터 본사람이면 안울수가없더라 진짜 너무 감격스럽고 뉴빈을 최근에 알았는데 미안하다.. 지금마크생존기1화보는데 진짜 준나인세대나와서 너무 감격스럽고 모두어엿하게 구독자 는거보니 내가 다 뭔가 알수없는 추억이라해야되나 그런감정이 이상하게 얽혀있다.. 블리자드는 말이많아진거같다 좋은캐릭이고..그리고 뉴빈왜욕하냐 귀여운데 준나인을보는것같다 성격도 닮았어 그리고뉴빈에 준나인김난다 둘이싸워도 이기는 신같은존재 나온다는게 사실임?? 그리고인터닛에 쳐봣는디 이거 ㄹㅇㄹㅇ 진짜팩트냐?? 저적이 뉴빈에 나오는 신급괴물임?ㅡ 준나인김난다 합체한거봐라 진짜 #$^*(#@&$) 이거보고 개충격먹어가지고 와 소리 저절로 나오더라 ;; 진짜 저건 개오지는데.. 저게 ㄹㅇ이면 진짜 꼭봐야돼 진짜 세계도 파괴시키는거아니야 .. 와 진짜 준나인김난다가 저렇게 되다니 진짜 눈물나려고했다.. 뉴빈그라서 계속보는중인데 저거 ㄹㅇ이냐..? 하.. )#*$ 김난다 보고싶다..  진짜언제 이렇게 신급 최강들이 되었을까 옛날생각나고 나 중딩때생각나고 뭔가 슬프기도하고 좋기도하고 감격도하고 여러가지감정이 복잡하네.. 아무튼 준나인은 진짜 유튭중최거채널임**')

    if message.content.startswith('봇나인 도움'):
        embed = discord.Embed(title='봇나인 명령어', description='봇나인이 받아줄 수 있는 명령어는? (접두사 /)')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/738712609427292192/927744999674765383/5232380134da8a91.png')
        embed.add_field(name='준나인', value='```준나인이 누구인지 알 수 있어요!```', inline=False)
        embed.add_field(name='김난다', value='```준나인의 동료, 김난다가 누구인지 알 수 있어요!```', inline=False)
        embed.add_field(name='청한', value='```스파를 하는 청한이 누구인지 알 수 있어요!```', inline=False)
        embed.add_field(name='트위치', value='```준나인의 트위치를 볼 수 있어요!```', inline=False)
        embed.add_field(name='유튜브', value='```준나인의 유튜브를 볼 수 있어요!```', inline=False)
        embed.add_field(name='채널', value='```....```', inline=False)
        embed.add_field(name='어몽어스', value='```AMOGUS```', inline=False)
        embed.add_field(name='어모거스', value='```이 세상 무언가....?```', inline=False)
        embed.add_field(name='초대', value='```봇나인과 함께 할 수 있는 링크!```', inline=False)
        embed.add_field(name='디스코드 서버', value='```준나인의 디스코드 링크!```', inline=False)
        embed.add_field(name='니얼굴', value='```자신의 얼굴의 상태를 확인 할 수 있어요!```', inline=False)
        embed.add_field(name='욕', value='```이건 양심적으로 하지 맙시다```', inline=False)
        embed.add_field(name='야구동영상', value='```준나인이 가장 좋아하는 야구 동영상을 볼 수 있어요!```', inline=False)
        embed.add_field(name='어그로', value='```어그로 잘 끄는법```', inline=False)
        embed.add_field(name='영상 추천', value='```유튜브 영상 추천!```', inline=False)
        embed.add_field(name='뉴빈', value='```뉴빈이 어떤 사람인지 알 수 있어요!```', inline=False)
        await message.channel.send(embed=embed)


client.run(token)
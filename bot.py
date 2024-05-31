import discord
import random

# Создаем клиент Discord бота
client = discord.Client()

# Словарь для хранения баланса пользователей
balances = {}

# Баланс админа (вы можете установить свое значение)
admin_balance = 1000

# Минимальная ставка и пополнение
min_bet = 1

# Команда для пополнения баланса криптовалютой
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!deposit'):
        amount = float(message.content.split()[1])
        if amount < min_bet:
            await message.channel.send("Минимальная сумма для пополнения - $1")
        else:
            user = message.author
            if user not in balances:
                balances[user] = 0
            balances[user] += amount
            await message.channel.send(f"Баланс пополнен на ${amount}")

    if message.content.startswith('!balance'):
        user = message.author
        if user in balances:
            await message.channel.send(f"Ваш текущий баланс: ${balances[user]}")
        else:
            await message.channel.send("У вас нет баланса")

    if message.content.startswith('!withdraw'):
        amount = float(message.content.split()[1])
        user = message.author
        if user in balances and balances[user] >= amount:
            balances[user] -= amount
            await message.channel.send(f"Сумма ${amount} выведена")
        else:
            await message.channel.send("Недостаточно средств для вывода")

    if message.content.startswith('!give'):
        if message.author.id == YOUR_ADMIN_ID:  # Замените YOUR_ADMIN_ID на ID вашего аккаунта Discord
            amount = float(message.content.split()[1])
            user = message.mentions[0]
            if user not in balances:
                balances[user] = 0
            balances[user] += amount
            await message.channel.send(f"Переведено ${amount} пользователю {user.mention}")

client.run('ваш_токен_бота')

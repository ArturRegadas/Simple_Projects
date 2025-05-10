import random as rdm
from Player import Player
from Stock import Stock
from Sector import Sector

def randomEvent() -> tuple:
    eventos = [
        ("Nada aconteceu.", 0.0),
        ("Boas notícias econômicas!", 0.01),
        ("Crise setorial!", -0.02),
        ("Fusão entre empresas!", 0.015),
        ("Alta de juros!", -0.01)
    ]
    return rdm.choice(eventos)

def main():
    tech = Sector("Tecnologia")
    health = Sector("Saúde")
    sectors = [tech, health]

    stocks = [
        Stock("TechCorp", 100, mu=0.01, sigma=0.03, sector=tech),
        Stock("MediPlus", 80, mu=0.008, sigma=0.025, sector=health)
    ]

    player = Player(cash=1000)

    days = 0
    while True:
        days += 1
        print(f"\n=== Dia {days} ===")
        for sector in sectors:
            sector.updateTrend()

        eventName, boost = randomEvent()
        print(f"Evento do dia: {eventName}")

        for stock in stocks:
            stock.updatePrice(event_boost=boost)

        for stock in stocks:
            print(f"{stock.getName()}: ${stock.getPrice()} (Setor: {stock.getSector().name})")

        player.summary(stocks)

        cmd = input("Digite 'b' para comprar, 'v' para vender, 'p' para passar, 'q' para sair: ").lower()
        if cmd == "q":
            break
        elif cmd == "b":
            nome = input("Nome da ação: ")
            qtd = int(input("Quantidade: "))
            stock = next((s for s in stocks if s.name == nome), None)
            if stock:
                player.buy(stock, qtd)
        elif cmd == "v":
            nome = input("Nome da ação: ")
            qtd = int(input("Quantidade: "))
            stock = next((s for s in stocks if s.name == nome), None)
            if stock:
                player.sell(stock, qtd)
    
if __name__=="__main__":
    main()
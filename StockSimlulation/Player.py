from Stock import Stock

class Player:
    def __init__(self, cash:float) -> None:
        self._cash = cash
        self._portfolio = {}

    def buy(self, stock:'Stock', qtd:int) -> bool:
        totalConst = stock.getPrice() * qtd
        if self._cash >= totalConst:
            self._cash -= totalConst
            if stock.getName() in self._portfolio:
                prevQtd, avgPrice = self._portfolio[stock.getName()]
                newQtd = prevQtd + qtd
                new_avg = (avgPrice * prevQtd + stock.getPrice() * qtd) / newQtd
                self._portfolio[stock.getName()] = (newQtd, round(new_avg, 2))

            else:
                self._portfolio[stock.getName()] = (qtd, stock.getPrice())
            
            return True
        return False
    
    def sell(self, stock:'Stock', qtd:int) -> bool:
        if stock.getName() in self._portfolio and self._portfolio[stock.getName][0] >= qtd:
            reward = stock.price * qtd
            self._cash+=reward
            remaining = self._portfolio[stock.getName()][0]-qtd
            if remaining == 0:
                del self._portfolio[stock.getName()]
            else:
                self._portfolio[stock.getName()] = (remaining, self._portfolio[stock.getName()][1])
            return True
        return False
    
    def summary(self, stocks:list['Stock']) -> None:
        print(f"\nDinheiro: ${round(self._cash, 2)}")
        print("Portfólio:")
        total = self._cash
        for name, (qtd, avg_price) in self._portfolio.items():
            current_price = next(s.price for s in stocks if s.name == name)
            val = current_price * qtd
            total += val
            print(f"  {name}: {qtd} (Média: {avg_price}) | Atual: {current_price} | Total: ${round(val, 2)}")
        print(f"Total estimado: ${round(total, 2)}\n")
    
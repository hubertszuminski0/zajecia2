class BankAccount:
    """Reprezentuje proste konto bankowe."""

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        if balance < 0:
            raise ValueError("Saldo początkowe nie może być ujemne")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Kwota wpłaty musi być dodatnia")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Kwota wypłaty musi być dodatnia")
        if amount > self.balance:
            raise ValueError("Brak wystarczających środków")
        self.balance -= amount

    def transfer(self, other: "BankAccount", amount: float) -> None:
        self.withdraw(amount)
        other.deposit(amount)

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self.balance})"

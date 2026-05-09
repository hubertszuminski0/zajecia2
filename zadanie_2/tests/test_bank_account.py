import pytest

from app.bank_account import BankAccount


@pytest.fixture
def account_with_100_balance():
    return BankAccount("Jan Kowalski", 100.0)


def test_create_account_with_default_balance():
    account = BankAccount("Jan Kowalski")

    assert account.balance == 0.0


def test_create_account_with_initial_balance():
    account = BankAccount("Anna Nowak", 100.0)

    assert account.balance == 100.0


def test_create_account_with_negative_balance_raises():
    with pytest.raises(ValueError, match="Saldo początkowe nie może być ujemne"):
        BankAccount("Jan Kowalski", -10.0)


@pytest.mark.parametrize("deposit_amount", [10.0, 50.0, 100.0])
def test_deposit_increases_balance(account_with_100_balance, deposit_amount):
    account_with_100_balance.deposit(deposit_amount)

    assert account_with_100_balance.balance == 100.0 + deposit_amount


def test_deposit_negative_amount_raises(account_with_100_balance):
    with pytest.raises(ValueError, match="Kwota wpłaty musi być dodatnia"):
        account_with_100_balance.deposit(-10.0)


def test_deposit_zero_raises(account_with_100_balance):
    with pytest.raises(ValueError, match="Kwota wpłaty musi być dodatnia"):
        account_with_100_balance.deposit(0.0)


def test_withdraw_decreases_balance(account_with_100_balance):
    account_with_100_balance.withdraw(30.0)

    assert account_with_100_balance.balance == 70.0


def test_withdraw_more_than_balance_raises(account_with_100_balance):
    with pytest.raises(ValueError, match="Brak wystarczających środków"):
        account_with_100_balance.withdraw(200.0)


def test_withdraw_negative_amount_raises(account_with_100_balance):
    with pytest.raises(ValueError, match="Kwota wypłaty musi być dodatnia"):
        account_with_100_balance.withdraw(-10.0)


def test_transfer_moves_money_between_accounts():
    source = BankAccount("Jan Kowalski", 100.0)
    target = BankAccount("Anna Nowak", 0.0)

    source.transfer(target, 50.0)

    assert source.balance == 50.0
    assert target.balance == 50.0


def test_repr_returns_expected_string():
    account = BankAccount("Jan Kowalski", 100.0)

    assert repr(account) == "BankAccount(owner='Jan Kowalski', balance=100.0)"

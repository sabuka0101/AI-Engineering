import pytest
from bank import BankAccount


@pytest.fixture
def account():
    return BankAccount("Ana", 100.0)


def test_initial_balance(account):
    assert account.balance == 0.0


def test_deposit_success(account):
    account.deposit(50.0)
    assert account.balance == 150.0


def test_deposit_negative(account):
    with pytest.raises(ValueError):
        account.deposit(-50.0)


def test_withdraw_success(account):
    account.withdraw(50.0)
    assert account.balance == 50


def test_withdraw_insufficient_funds(account):
    with pytest.raises(ValueError):
        account.withdraw(150.0)


def test_withdraw_negative(account):
    with pytest.raises(ValueError):
        account.withdraw(-50.0)

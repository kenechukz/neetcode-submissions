class Bank:
    """
    R:
    initial balance of (i+1)th accouint is balance[i] 
    as in 3rd account = 3-1
    given: balance - list of accounts

    E:
    cons: 1 to n accounts, where 1 <= n <= 10^5 
    if transfer from account balance < money:
        return false
    # for withdraw:
    if money > balance:
        false
    if account > n:
    A:
    ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
    [[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
    T:



    """
    def __init__(self, balance: List[int]):
        self.n = len(balance)
        self.balance = balance
    def validate(self, account: int) -> bool:
        return 1 <= account <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.validate(account1) and self.validate(account2):
            if money > self.balance[account1-1]:
                return False
            else:
                self.balance[account1-1] -= money
                self.balance[account2-1] += money
                return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:        
        if self.validate(account):
            self.balance[account-1] += money
            return True
        else:
            return False
            
    def withdraw(self, account: int, money: int) -> bool:
        if self.validate(account):
            if self.balance[account-1] >= money:
                self.balance[account-1] -= money
                return True
            else:
                return False
        else:
            return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
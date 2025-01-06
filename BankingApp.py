class BankingSystem:
  def __init__(self):
      # Dictionary to store account details: {name: {"balance": amount, "transactions": list}}
      self.accounts = {}

  def create_account(self, name, initial_balance):
      if name in self.accounts:
          return f"Account for {name} already exists."
      if initial_balance < 0:
          return "Initial balance cannot be negative."
      self.accounts[name] = {"balance": initial_balance, "transactions": [f"Account created with initial balance: {initial_balance}"]}
      return f"Account created for {name} with balance {initial_balance}."

  def deposit(self, name, amount):
      if name not in self.accounts:
          return f"Account for {name} does not exist."
      if amount <= 0:
          return "Deposit amount must be greater than zero."
      self.accounts[name]["balance"] += amount
      self.accounts[name]["transactions"].append(f"Deposited: {amount}")
      return f"Deposited {amount} into {name}'s account. Current balance: {self.accounts[name]['balance']}."

  def withdraw(self, name, amount):
      if name not in self.accounts:
          return f"Account for {name} does not exist."
      if amount <= 0:
          return "Withdrawal amount must be greater than zero."
      if self.accounts[name]["balance"] < amount:
          return f"Insufficient funds. Current balance: {self.accounts[name]['balance']}"
      self.accounts[name]["balance"] -= amount
      self.accounts[name]["transactions"].append(f"Withdrew: {amount}")
      return f"Withdrew {amount} from {name}'s account. Current balance: {self.accounts[name]['balance']}."

  def check_balance(self, name):
      if name not in self.accounts:
          return f"Account for {name} does not exist."
      return f"Current balance for {name}: {self.accounts[name]['balance']}"

  def print_statement(self, name):
      if name not in self.accounts:
          return f"Account for {name} does not exist."
      statement = f"Transaction statement for {name}:\n"
      statement += "\n".join(self.accounts[name]["transactions"])
      statement += f"\nCurrent balance: {self.accounts[name]['balance']}"
      return statement

# Example usage:
if __name__ == "__main__":
  bank = BankingSystem()
  print(bank.create_account("Alice", 1000))
  print(bank.deposit("Alice", 500))
  print(bank.withdraw("Alice", 200))
  print(bank.check_balance("Alice"))
  print(bank.print_statement("Alice"))

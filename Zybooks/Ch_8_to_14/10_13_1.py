class VendingMachine:
    def __init__(self):
        self.bottles = 20
        
    def purchase(self, amount):
        self.bottles = self.bottles - amount
      
    def restock(self, amount):
        self.bottles = self.bottles + amount
    
    def get_inventory(self):
        return self.bottles
        
    def report(self):
        print(f'Inventory: {self.bottles} bottles')

if __name__ == "__main__":

    '''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''

    machine = VendingMachine()
    machine.purchase(int(input()))
    machine.restock(int(input()))
    machine.report()

    '''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''
    
    
#task 10
class SultansDine:
    count = 0
    sell = 0
    lst=[]
    def __init__(self, name):
        self.name = name
        SultansDine.count += 1
        
    def sellQuantity(self, quantity):
        if quantity < 10:
            self.branch_sell = quantity * 300
        elif quantity < 20:
            self.branch_sell = quantity * 350
        else:
            self.branch_sell = quantity * 400
            
        SultansDine.sell += self.branch_sell
    
    def branchInformation(self):
        print(f'Branch Name: {self.name} \nBranch Sell: {self.branch_sell} Taka')
        
        SultansDine.lst.append(self.name)
        SultansDine.lst.append(self.branch_sell)
        
    @classmethod
    def details(cls):
        print(f'Total Number of branch(s): {SultansDine.count} \nTotal Sell: {SultansDine.sell} Taka')
        
        for i in range(0,len(SultansDine.lst), 2):
            print(f'Branch Name: {SultansDine.lst[i]}, Branch Sell: {SultansDine.lst[i+1]} Taka')
            print(f"Branch consists of total sell's: {(SultansDine.lst[i+1]/SultansDine.sell)* 100:.2f}%")
        
#============================================================

SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()
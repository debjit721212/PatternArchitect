from abc import ABC,abstractmethod


class Invoice:
    def __init__(self, amount, purpose):
        self.amount = amount
        self.purpose = purpose
        
        
class Approver(ABC):
    def __init__(self, next_approver=None):
        self.next_approver = next_approver

    @abstractmethod
    def approve(self, invoice):
        pass
    

class TeamLead(Approver):
    def approve(self, invoice):
        if invoice.amount <= 1000:
            print(f"Team Lead approved ${invoice.amount} for {invoice.purpose}")
        elif self.next_approver:
            self.next_approver.approve(invoice)

class Manager(Approver):
    def approve(self, invoice):
        if invoice.amount <=1500:
            print(f"Manager approved ${invoice.amount} for {invoice.purpose}")
        elif self.next_approver:
            self.next_approver.approve(invoice)

class Director(Approver):
    def approve(self, invoice):
        if invoice.amount <=5000:
            print(f"Director approved ${invoice.amount} for {invoice.purpose}")
        elif self.next_approver:
            self.next_approver.approve(invoice)


class CEO(Approver):
    def approve(self, invoice):
        print(f"CEO approved ${invoice.amount} for {invoice.purpose}")


invoice = Invoice(6500, "Team offsite event")

# Build chain
chain = TeamLead(Manager(Director(CEO())))
chain.approve(invoice)
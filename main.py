from savings import Savings
from current import CurrentAccount
from children_account import ChildrenAccount
from student_account import StudentAccount

def main():
    savings = Savings(balance=100000)
    current = CurrentAccount(balance=1000)
    children = ChildrenAccount(balance=0)
    student = StudentAccount(balance=4000)

    # Deposit savings
    depositSavings = savings.deposit(500)
    print(depositSavings)
    print(savings)

    #Withdraw savings
    withdrawSavings = savings.withdraw(600000)
    print(withdrawSavings)
    print(savings)
    
    #Withdraw current
    withdrawCurrent = current.withdraw(1000)
    print(withdrawCurrent)
    print(current)

    #Deposit Current
    depositCurrent = current.deposit(1000)
    print(depositCurrent)
    print(current)

    #Withdraw from student
    withdrawStudent = student.withdraw(2000)
    print(withdrawStudent)
    print(student)

    #Deposit to student
    depositStudent = student.deposit(2000)
    print(depositStudent)
    print(student)

    #Deposit to children
    depositChildren = children.deposit(4000)
    print(depositChildren)
    print(children)
    
if __name__ == "__main__":
    main()
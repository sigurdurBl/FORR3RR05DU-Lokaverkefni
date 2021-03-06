import json


class Node:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.salary = s
        self.prv = None
        self.nxt = None

    def append(self, n, a, s):
        if self.nxt:
            return self.nxt.append(n, a, s)
        else:
            curr = Node(n, a, s)
            self.nxt = curr
            curr.prv = self
            return True

    def printlist(self):
        if self.nxt:
            print(self.name,self.age,self.salary)
            self.nxt.printlist()
        else:
            print(self.name,self.age,salary)

    def find(self, n, a, s):
        if self.name == n and self.age == a and self.salary == s:
            return True
        else:
            if self.nxt:
                return self.nxt.find(n, a, s)
            else:
                return False

    def delete(self, n):

        if self.name == n and self.nxt is None:
            self.prv.nxt = None
            self.prv = None
            return True
        elif self.name == n:
            self.prv.nxt = self.nxt
            self.nxt.prv = self.prv
        else:
            if self.nxt:
                return self.nxt.delete(n)
            else:
                return False


class DLL:
    def __init__(self):
        self.head = None

    def push(self,n,a,s):
        if self.head:
            temp_next = self.head
            self.head = Node(n,a,s)
            self.head.nxt = temp_next
        else:
            self.head = Node(n,a,s)

    def append(self, n, a, s):
        if self.head:
            return self.head.append(n, a, s)
        else:
            self.head = Node(n, a, s)
            return True

    def printlist(self):
        if self.head:
            self.head.printlist()
        else:
            print("Empty list!")

    def find(self, n, a, s):
        if self.head:
            return self.head.find(n, a, s)
        else:
            return False

    def delete(self, n):
        if self.head is None:
            return False
        elif self.head == n:
            self.head = self.head.nxt
            return True
        else:
            return self.head.delete(n)



dbl = DLL()


with open('scratch.json', 'r')as myfile:
    data = myfile.read()
    obj = json.loads(data)
    for x in obj:
        name = x['Name']
        age = x['Age']
        salary = x['Salary']
        dbl.append(name,age,salary)
    dbl.printlist()
myfile.close()

n = 0
while n == 0:
    print("do you want to enter a new staf member press 1")
    print("do you want to find a staf member press 2")
    print("do you want to delete a staf member press 3")
    print("do you want to modify a staf info press 4")
    print("do you want to quit")
    val = int(input("what do you want to do"))

    if val == 1:
        name = input("Enter name")
        age = input("Enter age")
        salary = input("Enter salary")
        dbl.append(name, age, salary)
        dbl.printlist()
    if val == 2:
        name = input("Enter name")
        age = input("Enter age")
        salary = input("Enter salary")
        dbl.find(name, age, salary)
        print(dbl.find(name,age,salary))

    if val == 3:
        name = input("Enter name")
        dbl.delete(name)
        dbl.printlist()

    if val == 4:
        name = input("Enter name")
        age = input("Enter age")
        salary = input("Enter salary")
        print(dbl.find(name,age,salary))
        if name == name and age == age and salary == salary:
            a = 0
            while a == 0:
                print("1 Do you want to change the name?")
                print("2 DO you want to change the age?")
                print("3 Do you want to change the salary?")
                print("4 Quit")
                change = int(input("what do you want to do?"))
                if change == 1:
                    name1 = input("change name if not type the same name")
                    name = name1
                if change == 2:
                    age1 = input("change age if not type the same age")
                    age = age1
                if change == 3:
                    salary1 = input("change the salary if not type the same salary")
                    salary = salary1
                if change == 4:
                    dbl.printlist()
                    a = 1

    if val == 5:
        with open('scratch.json', 'w')as file:
            json.dump(dbl,file)
        myfile.close()
        n = 1
        
        







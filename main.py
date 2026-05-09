tasks=[]

print("\n 1.Add new \n 2.view task\n 3.delete task\n 4.exit")
choice=int(input("Enter the choice"))

while True:
    if choice=="1":
        task=input("enter task")
        tasks.append(task)
    elif choice=="2":
        for i,t in enumerate(tasks):
            print(i,t)
    elif choice=="3":

        index=int(input())
        tasks.pop(index)

    elif choice=="4":
        break


   
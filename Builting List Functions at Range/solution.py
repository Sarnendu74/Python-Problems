if __name__ == '__main__':
    N = int(input())
    my_list=[]
    for _ in range(N):
        command = input().strip().split()
        cmd = command[0]
         
        if cmd == 'insert':
            i,e = int(command[1]), int(command[2])
            my_list.insert(i,e)
        elif cmd == 'remove':
            x = int(command[1])
            my_list.remove(x)
        elif cmd == 'append':
            y = int(command[1])
            my_list.append(y)
        elif cmd == 'sort':
            my_list.sort()
        elif cmd == 'print':
            print(my_list)
        elif cmd == 'pop':
            my_list.pop()
        elif cmd == 'reverse':
            my_list.reverse()
            


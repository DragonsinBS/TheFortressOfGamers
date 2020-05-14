class crud:
    game_name=""
    game_gener=""
    game_writer=""
    def hash(self,pkey):
        pkey.upper()
        hashvalue=len(pkey)-4
        print(hashvalue)
        return hashvalue

    def packing(self,name,gener,writer):
        flag=0
        file_ent=name+"|"+gener+"|"+writer+"|"
        pos=self.hash(name)
        pos=pos*80
        for x in range (0,(80-len(file_ent)-1)):
            file_ent=file_ent+"|"
        file=open("gameFile.txt",'r+')
        while (flag!=1):
            file.seek(pos,0)
            temp=file.read(1)
            if temp=='*':
                file.seek(pos,0)
                file.write(file_ent)
                flag=1
            else:
                pos=pos+80
                
                flag=0
        file.close()
        return True

    def unpacking(self,temp):
        name=""
        gener=""
        writer=""
        iteams=temp.split('|')

        for i in temp:
            if i == '|':
                i=" "
                name=name+i
        print(name)


#            while (i!='|'):
#                gener=gener+i
#            print(gener)
#
#            while (i!='|'):
#                writer=writer+i
#            print(writer)
        #self.display(name,gener,writer)

    def search(self,pkey):
        name=""
        gener=""
        writer=""
        pos=self.hash(pkey)
        file=open("gameFile.txt","r+")
        file.seek(pos,0)
        temp= file.read(80)
        print(temp)
        self.unpacking(temp)


    def inputFunction(self):
        crud.game_name=input("Enter the name of the game.")
        crud.game_gener=input("Enter the gener of the game.")
        crud.game_writer=input("Enter the name of writer.")
        self.packing(crud.game_name,crud.game_gener,crud.game_writer)

    def display(self,name, gener, writer):
        print(name)
        print(gener)
        print(writer)
#def main():
#    c=crud()
#    c.inputFunction()
#    c.display()
#if __name__ == '__main__':
#    main()

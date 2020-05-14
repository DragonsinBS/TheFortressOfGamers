class basicfunction:
    buf=("*"*(80))+'\n'
    def __init__(self,file_name,file_info):
        self.name=file_info["name"]
        self.file_name=file_name
        self.file=open(file_name,'r+')
        self.field=file_info["field"]
        self.primary_key=file_info["primary_key"]

    def hash(self,pkey):
        hashvalue=len(pkey)-4
        print(hashvalue)
        return hashvalue
    
    def pack(self,data):
        buf=""
        flag=0
        pos=self.hash(data[self.primary_key])
        print(pos)
        for field in self.field:
            buf=buf+data[field]
            buf=buf+'|'
        print(buf)
        for i in range (0,(80-len(buf))):
            buf=buf+"|"
        buf=buf+'\n'
        pos=pos*82
        while(flag!=1):
            self.file.seek(pos,0)
            temp=self.file.read(1)
            if temp=='*':
                self.file.seek(pos,0)
                self.file.write(buf)
                self.file.flush()
                flag=1
            else:
                pos=pos+82

                
        return True

    def unpack(self,temp):
        iteam=temp.split('|')
        pac={}
        for i,j in enumerate(self.field):
            pac[j]=iteam[i]
        return pac

    def search(self,pkey):
        flag=0
        pos=self.hash(pkey)
        pos=pos*82
        while(flag!=1):
            self.file.seek(pos,0)
            temp=self.file.readline()
            if temp[0]=='*':
                return -1
            item=temp.split('|')
            if item[0]==pkey:
                return self.unpack(temp)
            else:
                pos=pos+82
                flag=0

    def delete(self,pkey):
        flag=0
        pos=self.hash(pkey)
        pos=pos*82
        while(flag!=1):
            self.file.seek(pos,0)
            temp=self.file.readline()
            if temp[0]=='*':
                return False
            item=temp.split('|')
            if item[0]==pkey:
                self.file.seek(pos,0)
                self.file.write(self.buf)
                self.file.flush()
                return True
            else:
                pos=pos+82
                flag=0
    
    def update(self,pkey,data):
        self.delete(pkey)
        self.insert(data)

    def insert(self,data):
        print(len(data["name"]))
        temp=self.search(data[self.primary_key])
        if temp!=-1:
            return False
        else:
            self.pack(data)

#def main():
 #   file_info={"name":"games",
  #  "field":["name","genre","writter"],
   # "primary_key":"name"}
    #c=crud("gameFile.txt",file_info)
   # c.insert({"name":"Nioh","genre":"Hack and slash","writter":"Kazunori Taguchi"})
   # c.insert({"name":"GTA 5","genre":"Action-adventure","writter":"Dan Houser"})
   # c.insert({"name":"Batman:Arkham Knight","genre":"Action-adventure","writter":"Martin Lancaster"})
   # print(c.search("GTA 5"))

#main()
#file_info={"name":"games","field":["name","genre","writter"],"primary_key":"name"}
import pymongo

client=pymongo.MongoClient("mongodb+srv://ocean:ocean@cluster0.ujxui1g.mongodb.net/?retryWrites=true&w=majority")
mydb=client["StudentDatabase"]
mycol=mydb["StudentDetails"]
##data=[{"_id":1001,"name":"iyyanar","age":24,"mark":434}]
##mycol.insert_one(data)
print("insert complete")
##x=mycol.find()
##for i in x:
##    print(i)

##import pymongo
##client=pymongo.MongoClient("mongodb+srv://root:root@cluster0.kenwm7e.mongodb.net/?retryWrites=true&w=majority")
####client=pymongo.MongoClient("mongodb+srv://root:root@cluster0.kenwm7e.mongodb.net/?retryWrites=true&w=majority")
##mydb=client["schooldatabase"]
##mycol=mydb["studentdata"]
##print("connected")
##data={"name":"iyyanar","age":24,"mark":434}
####data=[{"_id":1001,"name":"iyyanar","age":24,"mark":434},
####      {"_id":1002,"name":"sam","age":25,"mark":450},
####      {"_id":1003,"name":"gomathy","age":23,"mark":460},
####      {"_id":1004,"name":"lithika","age":3,"mark":450}]
##mycol.insert_one(data)
##print("insert complete")
####data={"name":{"$gt":"s"}}
####
####x=mycol.find_one(data)
####print(x)

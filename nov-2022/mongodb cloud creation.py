import pymongo
client=pymongo.MongoClient("mongodb+srv://ocean:ocean@cluster0.ujxui1g.mongodb.net/?retryWrites=true&w=majority")
mydb=client["school"]
mycol=mydb["student"]
print("connected")
data={"name":"iyyanar","age":24,"mark":434}
##data=[{"_id":1001,"name":"iyyanar","age":24,"mark":434},
##      {"_id":1002,"name":"sam","age":25,"mark":450},
##      {"_id":1003,"name":"gomathy","age":23,"mark":460},
##      {"_id":1004,"name":"lithika","age":3,"mark":450}]

mycol.insert_one({"name":12})
print("insert complete",)

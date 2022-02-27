from sys import path

import pymongo as pymongo
from pip._internal import req


def print_hi(name):
    print(f'Hi, {name}')


#def connectdb():

    ###to get names from the db given
    #print(db.list_collection_names())


##quest-1
#Get all the country where a letter or word given is in the name

def q1(name):
    client = pymongo.MongoClient(
        "mongodb+srv://Chetna:Datascience02@cluster0.tnqu0.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    countries = db.countries
    for country in countries.find():
        print(country['name'])
        
    query = {"name": {"$regex": name,
                      "$options": "i"}}
    result = countries.find(query)

    for i in result:
        print('\t')
        print(i['name'])

##quest-2
#Add a collection continent link to countries

def q2(name):
    client = pymongo.MongoClient(
        "mongodb+srv://Chetna:Datascience02@cluster0.tnqu0.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    countries = db.countries
    for country in countries.find():
        print(country['name'])
        
    res = countries.find().sort("population",1)
    for i in res:
        print('\t')
        print(i['name'])

##quest-3
#Send the list of continents with their number of countries

def q3():
    client = pymongo.MongoClient(
        "mongodb+srv://Chetna:Datascience02@cluster0.tnqu0.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    continents = db.continents
    for continent in continents.find():
        print(continent['name'])
    countries = db.countries
    for country in countries.find():
        print(country['name'])

    agg_res = continents.aggregate([{"$project": {"counts": {"$size": "$countries"}}}])

    for i in agg_res:
        print('\t')
        print(i)

##quest-4
#Send back the fourth countries of a continent by alphabetic order

def q4():
    client = pymongo.MongoClient(
        "mongodb+srv://Chetna:Datascience02@cluster0.tnqu0.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    continents = db.continents
    for continent in continents.find():
        print(continent['name'])
    countries = db.countries
    for country in countries.find():
        print(country['name'])

    res4 = continents.find().sort("name")
    for i in res4:
        countries = countries.find({"_id": {"$in": i["countries"]}}).sort("name")
        lis = []
        for j in countries:
            lis.append(j["name"]).sort("name")
        print("Continent:" + i["name"] + "," + "Countries" + "[", lis, "]")

##quest-5
#Add new attributes inside countries which is number of people (find it on Wikipedia)
def q5():
    client = pymongo.MongoClient(
        "mongodb+srv://Chetna:Datascience02@cluster0.tnqu0.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    countries = db.countries
    for country in countries.find():
        print(country['name'])
    list = [{"countries": "India", "population": 1390000000},
            {"countries": "Greece", "population":10370744},
            {"countries": "Great Britain", "population":68562151}]
    res5 = countries.insert_many(list)

    for i in res5:
        print('\t')
        print(i)

##quest-6
#Get all the countries order by number of people first the less populated and last the most populated
def q6():
    client = pymongo.MongoClient(
        "mongodb+srv://Chetna:Datascience02@cluster0.tnqu0.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    countries = db.countries
    for country in countries.find():
        print(country['name'])

    res6 = countries.find().sort({"population"})
    for i in res6:
        print('\t')
        print("countries:"+i["name"],","+"population:",i["population"])

##quest-7
#Get countries which have a ‘u’ in their name and more 100 000 people inside

def q7():
    client = pymongo.MongoClient(
        "mongodb+srv://Chetna:Datascience02@cluster0.tnqu0.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    countries = db.countries
    for country in countries.find():
        print(country['name'])

    query = {"name":{"$regex":'u',"$options":'i'},"population":{'$gt':100000}}
    res7 = countries.find(query)

    for i in res7:
        print("countries:"+i["name"],","+"population:",i["population"])

if __name__ == '__main__':
        print_hi('PyCharm')
        #connectdb()
        q1("in")
        q2()
        q3()
        q4()
        q5()
        q6()
        q7()


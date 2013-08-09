import riak

def riak_mapreduce():
    client=riak.RiakClient()
    bucket=client.bucket('myBucket')
    sturcrd=[{'Name':'Ram','Reg_No':'asdf01','marks':378,'stream':'science'},
    {'Name':'Pam','Reg_No':'asdf02','marks':468,'stream':'science'},
    {'Name':'Rohan','Reg_No':'asdf03','marks':368,'stream':'commerse'},
    {'Name':'Rahul','Reg_No':'asdf04','marks':438,'stream':'commerce'},
    {'Name':'Rahamat','Reg_No':'asdf05','marks':458,'stream':'humanities'}]

    for stu in sturcrd:
        item=bucket.new(stu['Reg_No'],stu)
        item.store()

    query=client.add("myBucket")
    query.map("""function(value){
        var data=Riak.mapValuesJson(value)[0];
        return [data.marks]
    }""")
    query.reduce("Riak.reduceMax")
    rslt=query.run()
    print "Maximum marks scored by student is "+rslt[0]

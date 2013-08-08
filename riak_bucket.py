import riak

def riak_bucket():
    client=riak.RiakClient()
    myBucket=client.bucket('myBucket')
    obj=myBucket.new(key='key',data='data')#creates new RiakObject stored as JSON.
    obj.store()#saves to riak.
    obj1=myBucket.get(key)#retrieves an object from Riak.
    obj_lst=myBucket.multiget(keys)#retrieves a list of objects.
    myBucket.delete(key)#deletes an object from riak.

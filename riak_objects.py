import riak

def riak_objs():
    client=riak.RiakClient()
    myBucket=client.bucket('myBucket')
    obj=myBucket.new(key='key',data='data')#creates new RiakObject.
    obj.store()
    data=obj.data #Returns the data stored in this object// 'data'
    raw_data=obj.encoded_data #Returns the raw data stored in object.// 'data'
    cntnt_type=obj.content_type #type of encoded data as string.// 'application/json'
    print raw_data,cntnt_type

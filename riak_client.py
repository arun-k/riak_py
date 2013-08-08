import riak

def client():
    client=riak.RiakClient()
    #connects to a single Riak node on localhost with the default ports
    #riak.RiakClient(protocol='http', host='127.0.0.1', http_port=8098)
    #riak.RiakClient(nodes=[{'host':'127.0.0.1','http_port':8098}])
    #riak.RiakClient(protocol='http', nodes=[RiakNode()])

    if client.ping():#check if the riak server for this client instance is alive
        buk_list=client.get_buckets()#returns a list of RiakBucket instaances.
        client.bucket("bucket_name")#creates new bucket.
        key_list-client.get_keys("bucket")#returns list of all keys in 'bucket'.
        

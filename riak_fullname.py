import riak

def riak_fullname():
    client=riak.RiakClient()
    myBucket=client.bucket('myBucket')
    myBucket.enable_search() #enable riak search
    myBucket.new("one", data={'value':'one'}).store()
    if myBucket.search_enabled():
        myBucket.search('value=one')
    myBucket.disable_search()

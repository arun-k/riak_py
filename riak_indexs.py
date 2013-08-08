import riak

def riak_indexs():
    client=riak.RiakClient()
    myBucket=client.bucket('myBucket')
    #Taging object with indexes
    sean = myBucket.new("seancribbs")
    sean.add_index("fname_bin", "Sean")
    sean.add_index("byear_int", 1979)
    sean.store()

    #performing equality query
    seans=myBucket.get_index("fname_bin", "Sean")

    #performing range query
    eighties=myBucket.get_index("byear_int", 1970,1980)

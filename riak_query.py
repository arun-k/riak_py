import riak

def query():
    client=riak.RiakClient(pb_port=8087,protocol='pbc')
    myBucket=client.bucket('myBucket')
    #insert
    obj=myBucket.new(key='one',data=1)
    obj.store()
    obj=myBucket.new(key='two',data=2)
    obj.store()
    dic={"value":3}
    obj=myBucket.new(key='three',data=dic)
    obj.store()
    #fetch
    fetch1=myBucket.get('one')
    fetch2=myBucket.get('two')
    fetch3=myBucket.get('three')
    #update
    fetch3.data['value']=13
    fetch3.store()
    #delete
    fetch1.delete()
    fetch2.delete()
    fetch3.delete()
    #verify deletions
    assert myBucket.get('one').exists == False
    assert myBucket.get('two').exists == False
    assert myBucket.get('three').exists == False

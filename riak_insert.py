import riak

def insert():
    
    myClient=riak.RiakClient(pb_port=8087,protocol='pbc')
    myBucket=myClient.bucket('myBucket')
    employee={'e_id':1,
              'First Name':'Edward',
              'Last Name':'John',
              'Address':'Gandhinagar 2nd street',
              'Department':'Technical'}
    obj=myBucket.new(key=employee['e_id'],data=employee)
    obj.store()
    fetch_employee=myBucket.get(employee['e_id'])
    

import riak
import uuid
import time

client = riak.RiakClient()
post_bucket = client.bucket('post')
comment_bucket = client.bucket('comment')

def create_post(post_dic):
    post_entry=post_bucket.new(post_dic['id'],pos_dic)
    post_entry.store()

def create_cmmnt(post_id,cmnt_dic):
    post=post_bucket.get(pos_id)
    cmnt_entry=comment_bucket.new(data=cmnt_dic)
    cmnt_entry.store()
    post.add_link(comment)
    post.store()

def get_post(post_id):
    post=post_bucket.get(post_id)
    comments=[]
    for link in post.get_links():
        comments.append(link.get().get_data())
    return {'post':post.data,'comments':comments}


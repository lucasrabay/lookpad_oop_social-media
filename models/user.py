from models.post import Post

class User:
    
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.friends = []
        self.friend_requests = []
        self.posts = []

    def __repr__(self):
        return '<User %r>' % self.name
    
    def __str__(self):
        return self.name
    
    def __eq__(self, other):
        return self.id == other.id 
    
    def get_posts(self):
        return self.posts
    
    def get_friends(self):
        return self.friends
    
    def get_friend_requests(self):
        return self.friend_requests
    
    def get_id(self):
        return self.id 
    def get_name(self):
        return self.name
    
    def share_post(self, content):
        post = Post(self, content, self.id)
        self.posts.append(content)
        return "Post shared successfully"
    
    def request_friend(self, user):
        self.friends.append(user)
        return "Friend request sent successfully"
    
    def accept_friend_request(self, user):
        self.friend_requests.append(user)
        return "Friend request sent successfully"
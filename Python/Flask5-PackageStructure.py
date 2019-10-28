from flask_sqlalchemy import SQLAlchemy
from additionals.Flask.Flask5 import app, db
from additionals.Flask.Flask5.Models import User, Post

db.drop_all()

db.create_all()
bruce = User(username='Bruce Wayne', email='Bruce@Richman.com', password='Batman')
db.session.add(bruce)
clark = User(username='Clark Kent', email='Kent@Superman.com', password='Superman')
db.session.add(clark)
db.session.commit()

print(User.query.all())

print()

print(User.query.first())
print(User.query.filter_by(username='Bruce Wayne').all())
print(User.query.filter_by(username='Bruce Wayne').first())

print()

user = User.query.filter_by(username='Bruce Wayne').first()
print(str(user.id))

print()

post1 = Post(title='The Arkham Knight', content='Arkham\'s Content', user_id=user.id)
db.session.add(post1)
post2 = Post(title='The Arham Asylum', content='Asylum\'s Content', user_id=user.id)
db.session.add(post2)
db.session.commit()

print(user.posts)

print()

for post in user.posts :
    print(post.title)

print()

post = Post.query.first()
print(post)
print(post.id)

print()

## Print post's author
print(post.author)
print()

db.drop_all()

## Automate debug and run flask
if __name__ == '__main__' :
    app.run(debug=True)

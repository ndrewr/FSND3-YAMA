"""
initial data for the course database. Future iteration
can add data at an external link or data object
"""
from yama import db, models

def loadDB():
  db.drop_all()
  db.create_all()


  # default users
  Admin = models.User(username="Big Brother", email="watching.you@gmail.com", picture="http://kimmckeeonline.com/wp-content/uploads/2015/03/gravatar_1.jpg")
  db.session.add(Admin)
  db.session.commit()

  # default categories; note their category id corresponds to the below order
  category1 = models.Category(name="JavaScript", description="The most widely used programming language in the world, JavaScript powers user interactions on the web. In other words, JavaScript is the programming language of HTML and the Web.")
  category2 = models.Category(name="Python", description="Python is a programming language that: is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.")
  category3 = models.Category(name="Rails", description="A web application development framework written in the Ruby language. It is designed to make programming web apps easier. Write less code while accomplishing more than many other languages and frameworks!")

  db.session.add_all([category1, category2, category3])
  db.session.commit()

  #default course offerings
  courses = []
  courses.append(models.Item(name="Udacity: JavaScript Basics",
                             url="https://www.udacity.com/course/javascript-basics--ud804",
                             description="In this course, you'll explore the JavaScript programming language by creating an interactive version of your resume.",
                             category_id=1,
                             user_id=1))

  courses.append(models.Item(name="Udacity: JavaScript Design Patterns",
                             url="https://www.udacity.com/course/javascript-design-patterns--ud989",
                             description="This course covers methods for organizing your code, both conceptually and literally. You'll learn the importance of separating concerns when writing JavaScript, gaining hands-on experience along the way.",
                             category_id=1,
                             user_id=1))

  courses.append(models.Item(name="Codeacademy: JavaScript Track",
                             url="http://www.codecademy.com/tracks/javascript",
                             description="Learn the fundamentals of JavaScript, the programming language of the Web.",
                             category_id=1,
                             user_id=1))

  courses.append(models.Item(name="Ready To Try JavaScript?",
                             url="http://www.javascript.com/resources",
                             description="JavaScript.com is a resource built by the Code School team for the JavaScript community. It is now and will always be free.",
                             category_id=1,
                             user_id=1))

  courses.append(models.Item(name="Udacity: Programming Foundations with Python",
                             url="https://www.udacity.com/course/programming-foundations-with-python--ud036",
                             description="This introductory course is for you if you want to be a software engineer, or if you want to collaborate with programmers. Mastering Object-Oriented Programming will propel your career in tech forward, and it's also a great way to learn how software engineers think about solving problems.",
                             category_id=2,
                             user_id=1))

  courses.append(models.Item(name="Codeacademy: Python Track",
                             url="http://www.codecademy.com/tracks/python",
                             description="Learn to program in Python, a powerful language used by sites like YouTube and Dropbox.",
                             category_id=2,
                             user_id=1))

  courses.append(models.Item(name="Learn Python the Hard Way",
                             url="http://learnpythonthehardway.org/book/index.html",
                             description="Read by 1.5 million people a year to learn the basics of programming, Learn Python The Hard Way is the most successful beginner programming book on the market.",
                             category_id=2,
                             user_id=1))

  courses.append(models.Item(name="Codeacademy: Ruby on Rails Track",
                             url="http://www.codecademy.com/learn/learn-rails",
                             description="Learn to build web apps with Ruby on Rails 4. By the end of the course, you'll be able to use Ruby on Rails to create your own apps.",
                             category_id=3,
                             user_id=1))

  courses.append(models.Item(name="Treehouse: Learn Rails Development",
                             url="https://teamtreehouse.com/tracks/rails-development",
                             description="Ruby on Rails is a popular web application framework written in the Ruby programming language. By the end of this track, we'll have created an application to create and manage todo lists.",
                             category_id=3,
                             user_id=1))

  courses.append(models.Item(name="JavaScript is Sexy: Learn JavaScript Properly",
                             url="http://javascriptissexy.com/how-to-learn-javascript-properly",
                             description="You do want to learn JavaScript. I presume you are here for that reason, and you have made a wise decision. JavaScript is undoubtedly the best web-development language to learn today",
                             category_id=1,
                             user_id=1))

  courses.append(models.Item(name="How I TRAINed to Learn Rails",
                             url="https://medium.com/how-i-learned-ruby-rails/how-i-trained-to-learn-rails-e08c94e2a51e",
                             description="A blogger reflects on the methods and resources he used to grok Rails development.",
                             category_id=3,
                             user_id=1))

  courses.append(models.Item(name="Rails Guides",
                             url="http://guides.rubyonrails.org",
                             description="These are the new guides for Rails 4.2 based on v4.2.3. These guides are designed to make you immediately productive with Rails, and to help you understand how all of the pieces fit together.",
                             category_id=3,
                             user_id=1))


  # db.session.add_all([course1, course2, course3, course4, course5, course6, course7])
  db.session.add_all(courses)
  db.session.commit()


# run loadDB
if __name__ == "__main__":
  loadDB()

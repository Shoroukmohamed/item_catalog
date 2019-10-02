from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Catagory, Base, CatagoryItem, User

engine = create_engine('sqlite:///catagories.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Menu for romance
catagory1 = Catagory(user_id=1, name="romance")

session.add(catagory1)
session.commit()

catagoryItem2 = CatagoryItem(user_id=1, name="i can hear your voice", description="hero can see what you think throgth your eyes",
                             catagory=catagory1)

session.add(catagoryItem2)
session.commit()


catagoryItem1 = CatagoryItem(user_id=1, name="her private life", description="How fan can do for his gange",
                             catagory=catagory1)

session.add(catagoryItem1)
session.commit()

# Menu for comedy
catagory2 = Catagory(user_id=1, name="COMEDY")

session.add(catagory2)
session.commit()


catagoryItem1 = CatagoryItem(user_id=1, name="laugh for wikiki", description="it is about fun and hotel",
                             catagory=catagory2)

session.add(catagoryItem1)
session.commit()

catagoryItem2 = CatagoryItem(user_id=1, name="king of shopping louis",
                             description="it is about one has amnesia and try to live ", catagory=catagory2)

session.add(catagoryItem2)
session.commit()

# Menu for youth
catagory1 = Catagory(user_id=1, name="youth")

session.add(catagory1)
session.commit()


catagoryItem1 = CatagoryItem(user_id=1, name="school 2013", description="it is about what faces the students in their schools.",
                             catagory=catagory1)

session.add(catagoryItem1)
session.commit()

print "added menu series!"

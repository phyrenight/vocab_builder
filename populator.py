from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from vocab_db import Base, Dict

engine = create_engine('sqlite:///Dictionary.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Add words
word1 = Dict(word="colloquial", definition="characteristics of or appropriate to ordinary or familiar conversation rather than formal speech or writing; informal")
session.add(word1)
word2 = Dict(word="acquiesce", definition="to assent tacitly, submit or comply silently or without protest; agree; consent")
session.add(word2)

word3 = Dict(word="ambiguity", definition="doubtfulness or uncertainty of meaning or intention")
session.add(word3)

word4 = Dict(word="anachronism", definition="something or someone that is not in its correct historical or chronological time, especially a thing or a person that belongs to an earlier time.")
session.add(word4)

word5 = Dict(word="andragogy", definition="the methods or techniques userd to teach adults")
session.add(word5)

session.commit()
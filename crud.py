from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import select


from models import User
from models import Address

engine = create_engine("sqlite:///new_file.db", echo=True, future=True)

# CREATE
with Session(engine) as session:
    spongebob = User(
        name="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    )
    sandy = User(
        name="sandy",
        fullname="Sandy Cheeks",
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
        ],
    )
    patrick = User(name="patrick", fullname="Patrick Star")
    session.add_all([spongebob, sandy, patrick])
    session.commit()



# READ(SELECT)
session = Session(engine)

stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

for user in session.scalars(stmt):
    print(user)



# READ(SELECT WITH JOIN)
stmt = (
 select(Address)
 .join(Address.user)
 .where(User.name == "sandy")
 .where(Address.email_address == "sandy@sqlalchemy.org")
)
sandy_address = session.scalars(stmt).one()
sandy_address

# UPDATE(추가)
stmt = select(User).where(User.name == "patrick")
patrick = session.scalars(stmt).one()
patrick.addresses.append(
    Address(email_address="patrickstar@sqlalchemy.org")
)
sandy_address.email_address = "sandy_cheeks@sqlalchemy.org"

session.commit()


# delete
sandy = session.get(User, 2)
sandy.addresses.remove(sandy_address)
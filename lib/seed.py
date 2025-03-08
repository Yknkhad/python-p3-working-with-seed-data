#!/usr/bin/env python3


from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    botw = Game(title="Elden Ring", platform="Playstation", genre="Action RPG", price=60)
    ffvii = Game(title="The Witcher 3", platform="PC", genre="RPG", price=40)
    mk8 = Game(title="Gran Turismo 7", platform="Playstation", genre="Racing", price=50)
    ccs = Game(title="Tetris Blitz", platform="Mobile", genre="Puzzle", price=5)
    dxt = Game(title="Cyber Strike", platform="Xbox", genre="Shooter", price=55)
    aka = Game(title="Legend of the Lost", platform="Switch", genre="Adventure", price=60)
    mpa = Game(title="F1 Grand Prix", platform="PC", genre="Racing", price=35)


    session.bulk_save_objects([botw, ffvii, mk8, ccs, dxt,aka, mpa])
    session.commit()

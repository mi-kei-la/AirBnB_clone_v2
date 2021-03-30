#!/usr/bin/python3
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ Database storage class.
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor
        """
        # dialect+driver://username:password@host:port/database
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:{}'
                                      .format(getenv(HBNB_MYSQL_USER),
                                              getenv(HBNB_MYSQL_PWD),
                                              getenv(HBNB_MYSQL_HOST),
                                              getenv(HBNB_MYSQL_DB)),
                                      pool_pre_ping=True)
        if getenv(HBNB_ENV) is "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        classes = [
                    User, Place,
                    State, City, Amenity,
                    Review
                  ]
        objects = {}
        if cls is not None:
            result = self.__session.query(cls).all()
            for row in result:
                key = type(row).__name__ + '.' + row.id
                objects[key] = row
        else:
            for instance in classes:
                result = self.__session.query(instance).all()
                for row in result:
                    key = type(row).__name__ + '.' + row.id
                    objects[key] = row
        return objects

#!/usr/bin/python3
"""DB Storage."""

from os import getenv
from sqlalchemy import create_engine
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel, Base


class DBStorage:
    """DB storage class."""
    __engine = None
    __session = None

    def __init__(self):
        """Method init for DBStorage."""
        username = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db_base = getenv('HBNB_MYSQL_DB')

        # Create a new Engine instance.
        self.__engine = create_engine('msql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(username,
                                              password,
                                              host,
                                              db_base),
                                      pool_pre_ping=True)  # test connections.
        # Drop all tables if the env == test
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Get all objects."""
        new_dict = {}  # Dictionary with all objects
        if cls is None:
            classes = ['Amenity', 'City', 'Place', 'Review', 'State', 'User']
            for my_class in classes:
                # Contain all objects of my_class
                my_query = self.__session.query(eval(my_class))
                for obj_query in my_query:
                    key =  type(obj_query).__name__+ "." + obj_query.id
                    new_dict[key] = obj_query
        else:
            # Contain all objects of cls.
            my_query = self.__sesssion.query(eval(cls))
            for obj_query in my_query:
                key =  type(obj_query).__name__+ "." + obj_query.id
                new_dict[key] = obj_query

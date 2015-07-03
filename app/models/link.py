# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Sequence, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

from ..models import engine


Base = declarative_base()


class Link(Base):
    __tablename__ = 'link'
    id = Column(Integer, Sequence('link_id_seq'), primary_key=True)
    url = Column(String(1000))
    slug = Column(String(1000))
    description = Column(String(1000))
    create_time = Column(DateTime)

    def __init__(self, slug, url, description, create_time):
        self.url = url
        self.slug = slug
        self.description = description
        self.create_time = create_time

    def __repr__(self):
        return "<Link('%s','%s','%s', '%s')>" % (self.url, 
                                                 self.slug, self.description,
                                                 self.create_time)


Link.metadata.create_all(engine)
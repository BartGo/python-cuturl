# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Sequence, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

from .. import settings

base = declarative_base()
engine = create_engine(settings.SQA_DBENGINE, echo=settings.SQA_ECHO)

class Link(base):
    __tablename__ = 'link'
    link_id = Column(Integer, Sequence('link_id_seq'), primary_key=True)
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
        rpr = "<Link('{0}', '{1}', '{2}', '{3}')>".format(self.url, self.slug, self.description, self.create_time)
        return rpr
        
Link.metadata.create_all(engine)

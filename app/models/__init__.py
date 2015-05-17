# -*- coding: utf-8 -*-
from sqlalchemy import create_engine

#engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite:///sqlite.db', echo=True)

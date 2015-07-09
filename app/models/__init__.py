# -*- coding: utf-8 -*-
from sqlalchemy import create_engine

from .. import settings

print "*** settings.SQA_DBENGINE = " + settings.SQA_DBENGINE
engine = create_engine(settings.SQA_DBENGINE, echo=settings.SQA_ECHO)

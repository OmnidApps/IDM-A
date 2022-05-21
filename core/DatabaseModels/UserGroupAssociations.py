from core.Pantheon.AppFactory import db
from sqlalchemy import Column, Integer, String, UniqueConstraint, Table, ForeignKey, TIMESTAMP
import uuid
from datetime import datetime

user_group_relations = Table(
    'user_group_assoc',
    db.metadata,
    Column('user_uuid', ForeignKey( 'user.uuid' ), primary_key=True ),
    Column('group_uuid', ForeignKey( 'group.uuid'), primary_key=True ),
    Column( TIMESTAMP, name='creation_date', default=datetime.utcnow, nullable=False )
)
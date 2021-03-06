# -*- encoding: utf-8 -*-
#
# Copyright 2014 Hewlett-Packard Development Company, L.P.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""Initial schema

Revision ID: 236f63c96b6a
Revises: None
Create Date: 2014-11-16 12:24:50.885039

"""

# revision identifiers, used by Alembic.
from cue.db.sqlalchemy import types

revision = '236f63c96b6a'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clusters',
    sa.Column('id', types.UUID(), nullable=False),
    sa.Column('project_id', sa.String(length=36), nullable=False),
    sa.Column('network_id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('flavor', sa.String(length=50), nullable=False),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('volume_size', sa.Integer(), nullable=True),
    sa.Column('deleted', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nodes',
    sa.Column('id', types.UUID(), nullable=False),
    sa.Column('cluster_id', types.UUID(), nullable=True),
    sa.Column('flavor', sa.String(length=36), nullable=False),
    sa.Column('instance_id', sa.String(length=36), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['cluster_id'], ['clusters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('endpoints',
    sa.Column('id', types.UUID(), nullable=False),
    sa.Column('node_id', types.UUID(), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=False),
    sa.Column('uri', sa.String(length=255), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['node_id'], ['nodes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('endpoints')
    op.drop_table('nodes')
    op.drop_table('clusters')
    ### end Alembic commands ###

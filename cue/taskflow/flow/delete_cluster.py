# -*- coding: utf-8 -*-
# Copyright 2015 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import taskflow.patterns.linear_flow as linear_flow
import taskflow.patterns.unordered_flow as unordered_flow

from cue.db.sqlalchemy import models
from cue.taskflow.flow import delete_cluster_node
import cue.taskflow.task as cue_tasks


def delete_cluster(cluster_id, node_ids):
    """Delete Cluster flow factory function

    This factory function uses :func:`cue.taskflow.flow.delete_cluster_node` to
    delete a multi node cluster.

    :param cluster_id: A unique ID assigned to the cluster being deleted
    :type cluster_id: string
    :param node_ids: The Cue Node id's associated with each node in the cluster
    :type node_ids: list of uuid's
    :return: A flow instance that represents the workflow for deleting a
             cluster
    """
    flow = linear_flow.Flow("deleting cluster %s" % cluster_id)
    sub_flow = unordered_flow.Flow("delete VMs")
    start_flow_status = {'cluster_id': cluster_id,
                         'cluster_values': {'status': models.Status.DELETING}}
    end_flow_status = {'cluster_id': cluster_id,
                       'cluster_values': {'status': models.Status.DELETED,
                                          'deleted': True}}

    #todo(dagnello): verify node_ids is a list and not a string
    for i, node_id in enumerate(node_ids):
        sub_flow.add(delete_cluster_node.delete_cluster_node(cluster_id, i,
                                                             node_id))

    flow.add(cue_tasks.UpdateClusterStatus(name="update cluster status start "
                                                "%s" % cluster_id,
                                           inject=start_flow_status))
    flow.add(sub_flow)
    flow.add(cue_tasks.UpdateClusterStatus(name="update cluster status end "
                                                "%s" % cluster_id,
                                           inject=end_flow_status))

    return flow

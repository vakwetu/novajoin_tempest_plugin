# Copyright 2016 Red Hat
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

from oslo_config import cfg

service_option = cfg.BoolOpt("novajoin",
                             default=True,
                             help="Whether or not novajoin is expected to be "
                                  "available")

novajoin_group = cfg.OptGroup(
    name="novajoin",
    title="Novajoin test plugin settings")

NovajoinGroup = [
    cfg.StrOpt('keytab',
               default='/home/stack/novajoin.keytab',
               help='Keytab to connect to IPA as the novajoin user'),
    cfg.StrOpt('tripleo',
               default='True',
               help='Run triple-O config tests'),
    cfg.ListOpt('tripleo_controllers',
                default=['overcloud-controller-0'],
                help='List of overcloud controller short host names'),
    cfg.ListOpt('tripleo_computes',
                default=['overcloud-novacompute-0'],
                help='List of overcloud compute short host names'),
    cfg.StrOpt('tripleo_undercloud',
               default='undercloud',
               help='Undercloud short host name'
               )
]

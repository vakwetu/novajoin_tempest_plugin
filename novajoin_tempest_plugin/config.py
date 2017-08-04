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

ipa_group = cfg.OptGroup(
    name="ipa",
    title="IPA connection information")

IpaGroup = [
    cfg.StrOpt('username',
               default='admin',
               help='User to connect to IPA'),
    cfg.StrOpt('password',
               default='password',
               help='Password to connect to IPA'),
]
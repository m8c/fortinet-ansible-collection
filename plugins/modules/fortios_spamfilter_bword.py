#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
# Copyright 2019 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fortios_spamfilter_bword
short_description: Configure AntiSpam banned word list in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify spamfilter feature and bword category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.0.5
version_added: "2.9"
author:
    - Miguel Angel Munoz (@mamunozgonzalez)
    - Nicolas Thomas (@thomnico)
notes:
    - Requires fortiosapi library developed by Fortinet
    - Run as a local_action in your playbook
requirements:
    - fortiosapi>=0.9.8
options:
    host:
        description:
            - FortiOS or FortiGate IP address.
        type: str
        required: false
    username:
        description:
            - FortiOS or FortiGate username.
        type: str
        required: false
    password:
        description:
            - FortiOS or FortiGate password.
        type: str
        default: ""
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        type: str
        default: root
    https:
        description:
            - Indicates if the requests towards FortiGate must use HTTPS protocol.
        type: bool
        default: true
    ssl_verify:
        description:
            - Ensures FortiGate certificate must be verified by a proper CA.
        type: bool
        default: true
    state:
        description:
            - Indicates whether to create or remove the object.
        type: str
        required: true
        choices:
            - present
            - absent
    spamfilter_bword:
        description:
            - Configure AntiSpam banned word list.
        default: null
        type: dict
        suboptions:
            comment:
                description:
                    - Optional comments.
                type: str
            entries:
                description:
                    - Spam filter banned word.
                type: list
                suboptions:
                    action:
                        description:
                            - Mark spam or good.
                        type: str
                        choices:
                            - spam
                            - clear
                    id:
                        description:
                            - Banned word entry ID.
                        required: true
                        type: int
                    language:
                        description:
                            - Language for the banned word.
                        type: str
                        choices:
                            - western
                            - simch
                            - trach
                            - japanese
                            - korean
                            - french
                            - thai
                            - spanish
                    pattern:
                        description:
                            - Pattern for the banned word.
                        type: str
                    pattern_type:
                        description:
                            - Wildcard pattern or regular expression.
                        type: str
                        choices:
                            - wildcard
                            - regexp
                    score:
                        description:
                            - Score value.
                        type: int
                    status:
                        description:
                            - Enable/disable status.
                        type: str
                        choices:
                            - enable
                            - disable
                    where:
                        description:
                            - Component of the email to be scanned.
                        type: str
                        choices:
                            - subject
                            - body
                            - all
            id:
                description:
                    - ID.
                required: true
                type: int
            name:
                description:
                    - Name of table.
                type: str
'''

EXAMPLES = '''
- hosts: localhost
  vars:
   host: "192.168.122.40"
   username: "admin"
   password: ""
   vdom: "root"
   ssl_verify: "False"
  tasks:
  - name: Configure AntiSpam banned word list.
    fortios_spamfilter_bword:
      host:  "{{ host }}"
      username: "{{ username }}"
      password: "{{ password }}"
      vdom:  "{{ vdom }}"
      https: "False"
      state: "present"
      spamfilter_bword:
        comment: "Optional comments."
        entries:
         -
            action: "spam"
            id:  "6"
            language: "western"
            pattern: "<your_own_value>"
            pattern_type: "wildcard"
            score: "10"
            status: "enable"
            where: "subject"
        id:  "13"
        name: "default_name_14"
'''

RETURN = '''
build:
  description: Build number of the fortigate image
  returned: always
  type: str
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: str
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: str
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: str
  sample: "id"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: str
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: str
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: str
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: str
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: str
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: str
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: str
  sample: "v5.6.3"

'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import FortiOSHandler
from ansible_collections.fortinet.fortios.plugins.module_utils.fortimanager.common import FAIL_SOCKET_MSG


def login(data, fos):
    host = data['host']
    username = data['username']
    password = data['password']
    ssl_verify = data['ssl_verify']

    fos.debug('on')
    if 'https' in data and not data['https']:
        fos.https('off')
    else:
        fos.https('on')

    fos.login(host, username, password, verify=ssl_verify)


def filter_spamfilter_bword_data(json):
    option_list = ['comment', 'entries', 'id',
                   'name']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def underscore_to_hyphen(data):
    if isinstance(data, list):
        for elem in data:
            elem = underscore_to_hyphen(elem)
    elif isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            new_data[k.replace('_', '-')] = underscore_to_hyphen(v)
        data = new_data

    return data


def spamfilter_bword(data, fos):
    vdom = data['vdom']
    state = data['state']
    spamfilter_bword_data = data['spamfilter_bword']
    filtered_data = underscore_to_hyphen(filter_spamfilter_bword_data(spamfilter_bword_data))

    if state == "present":
        return fos.set('spamfilter',
                       'bword',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('spamfilter',
                          'bword',
                          mkey=filtered_data['id'],
                          vdom=vdom)


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_spamfilter(data, fos):

    if data['spamfilter_bword']:
        resp = spamfilter_bword(data, fos)

    return not is_successful_status(resp), \
        resp['status'] == "success", \
        resp


def main():
    fields = {
        "host": {"required": False, "type": "str"},
        "username": {"required": False, "type": "str"},
        "password": {"required": False, "type": "str", "default": "", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "https": {"required": False, "type": "bool", "default": True},
        "ssl_verify": {"required": False, "type": "bool", "default": True},
        "state": {"required": True, "type": "str",
                  "choices": ["present", "absent"]},
        "spamfilter_bword": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "comment": {"required": False, "type": "str"},
                "entries": {"required": False, "type": "list",
                            "options": {
                                "action": {"required": False, "type": "str",
                                           "choices": ["spam", "clear"]},
                                "id": {"required": True, "type": "int"},
                                "language": {"required": False, "type": "str",
                                             "choices": ["western", "simch", "trach",
                                                         "japanese", "korean", "french",
                                                         "thai", "spanish"]},
                                "pattern": {"required": False, "type": "str"},
                                "pattern_type": {"required": False, "type": "str",
                                                 "choices": ["wildcard", "regexp"]},
                                "score": {"required": False, "type": "int"},
                                "status": {"required": False, "type": "str",
                                           "choices": ["enable", "disable"]},
                                "where": {"required": False, "type": "str",
                                          "choices": ["subject", "body", "all"]}
                            }},
                "id": {"required": True, "type": "int"},
                "name": {"required": False, "type": "str"}

            }
        }
    }

    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)

    # legacy_mode refers to using fortiosapi instead of HTTPAPI
    legacy_mode = 'host' in module.params and module.params['host'] is not None and \
                  'username' in module.params and module.params['username'] is not None and \
                  'password' in module.params and module.params['password'] is not None

    if not legacy_mode:
        if module._socket_path:
            connection = Connection(module._socket_path)
            fos = FortiOSHandler(connection)

            is_error, has_changed, result = fortios_spamfilter(module.params, fos)
        else:
            module.fail_json(**FAIL_SOCKET_MSG)
    else:
        try:
            from fortiosapi import FortiOSAPI
        except ImportError:
            module.fail_json(msg="fortiosapi module is required")

        fos = FortiOSAPI()

        login(module.params, fos)
        is_error, has_changed, result = fortios_spamfilter(module.params, fos)
        fos.logout()

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()

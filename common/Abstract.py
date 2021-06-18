# -*- coding:utf-8 -*-
'''
@Author  : Eric
@Time    : 2021-06-15 15:35
@IDE     : PyCharm
'''
import json
import sys


class AbstractModel(object):
    """Base class for all models."""

    def _serialize(self, allow_none=False):
        d = vars(self)
        ret = {}
        for k in d:
            if isinstance(d[k], AbstractModel):
                r = d[k]._serialize(allow_none)
            elif isinstance(d[k], list):
                r = list()
                for tem in d[k]:
                    if isinstance(tem, AbstractModel):
                        r.append(tem._serialize(allow_none))
                    else:
                        r.append(
                            tem.encode("UTF-8") if isinstance(tem, type(u"")) and sys.version_info[0] == 2 else tem)
            else:
                r = d[k].encode("UTF-8") if isinstance(d[k], type(u"")) and sys.version_info[0] == 2 else d[k]
            if allow_none or r is not None:
                ret[k[0].upper() + k[1:]] = r
        return ret


    def _deserialize(self, params):
        return None

    def to_json_string(self, *args, **kwargs):
        """Serialize obj to a JSON formatted str, ensure_ascii is False by default"""
        if "ensure_ascii" not in kwargs:
            kwargs["ensure_ascii"] = False
        return json.dumps(self._serialize(allow_none=True), *args, **kwargs)

    def from_json_string(self, jsonStr):
        """Deserialize a JSON formatted str to a Python object"""
        params = json.loads(jsonStr)
        self._deserialize(params)

    def __repr__(self):
        return "%s" % self.to_json_string()

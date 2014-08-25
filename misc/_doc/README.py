import good
from exdoc import doc, getmembers

import json

doccls = lambda cls, *predicates: {
    'cls': doc(cls),
    'attrs': {name: doc(m) for name, m in getmembers(cls, *predicates)}
}

data = {
    'good': doc(good),
    'Schema': doccls(good.Schema),
}

print json.dumps(data, indent=2)
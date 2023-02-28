import importlib
from importlib import metadata as importlib_metadata

dists = importlib_metadata.distributions()
for dist in dists:
    name = dist.metadata["Name"]
    version = dist.version
    license = dist.metadata["License"]
    print(f'found distribution {name}=={version}')
    if dist.metadata["Keywords"] is None or 'AutoPeachPlugins' not in dist.metadata["Keywords"]:
        continue
    module = importlib.import_module(name)
    if 'MetaInfo' not in module.__dict__:
        continue
    meta_info = module.__dict__['MetaInfo']
    cron = meta_info.get('cron')
    if not cron:
        continue
    cron()

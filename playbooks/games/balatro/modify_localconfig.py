import vdf

to_modify = "/tmp/localconfig.vdf"

with open(to_modify, "r") as f:
    d = vdf.loads(f.read(), mapper=vdf.VDFDict)

d["UserLocalConfigStore"]["Software"]["Valve"]["Steam"]["apps"]["2379780"]["LaunchOptions"] = 'WINEDLLOVERRIDES="version=n,b" %command%'

with open(to_modify, "w") as f:
    vdf.dump(d, f, pretty=True)
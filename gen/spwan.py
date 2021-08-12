for i in range(100):
    namespace_name = f"ns{i}"
    f = open(f"../manifests/{namespace_name}.yaml", "w")
    f.write(f"apiVersion: v1\nkind: Namespace\nmetadata:\n  name: {namespace_name}")
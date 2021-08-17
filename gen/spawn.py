directory = input("Enter Directory: ").strip()
num = int(input("Enter Number of Files: ").strip())
for i in range(num):
    namespace_name = f"ns{i}"
    f = open(f"../{directory}/{namespace_name}.yaml", "w")
    f.write(f"apiVersion: v1\nkind: Namespace\nmetadata:\n  name: {namespace_name}")
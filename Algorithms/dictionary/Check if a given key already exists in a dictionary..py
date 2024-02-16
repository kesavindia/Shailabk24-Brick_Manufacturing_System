dict = {"r":2,"h":4,"u":5}
search_key = "r"
if dict.get(search_key) is not None:
    print(f"the key {search_key} is present in dict.")
else:
    print(f"the key {search_key} is not present in dict.")

if dict['u'] is not None:
    print(f"the key 'u' is present in dict.")
if 'r' in dict:
    print(f"the key 'r' is present in dict.")


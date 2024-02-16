#Remove leading zeros from an IP address
def remove_zeros(Ipaddress):
    octets = Ipaddress.split('.')
    #split method splits the string based on the separator
    updatedoctets = [str(int(octet)) if octet.isdigit() else octet for octet in octets]
    updated_list = '.'.join(updatedoctets)
    #Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
    return  updated_list
Ipaddress = '133.800.009.009'
result = remove_zeros(Ipaddress)
print(result)
x = str(int('008'))
print(x)
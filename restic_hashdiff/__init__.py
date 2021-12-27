import os
import json
import hashlib
from pprint import pprint


def process_file(file_description):
    result = {'file' : file_description['path']}
    
    if not os.path.isfile(file_description['path']):
        result['state'] = 'missing'
        return result
    
    if os.path.getsize(file_description['path']) != file_description['size']:
        result['state'] = 'size_difference'
        return result
    
    if file_description['size'] == 0:
        result['state'] = 'identical'
        return result
    
    # here we know that file exists and has the same size, let's check data
    f = open(file_description['path'], 'rb')
    for block in zip(file_description['content'], file_description['contentsize']):
        data = f.read(block[1] - 32) # 32 bytes are added by restic
        if hashlib.sha256(data).hexdigest() != block[0]:
            result['state'] = 'hash_difference'
            return result
    
    result['state'] = 'identical'
    return result
    

class HashDiff(object):
    
    def __init__(self, hash_file):
        self.hash_file = open(hash_file)
    
    def next_object(self):
        line = self.hash_file.readline()
        if line:
            return json.loads(line)
        return None
    
    def next_file(self):
        result = self.next_object()
        while (result is not None) and ((result['struct_type'] != 'node') or (result['type'] != 'file')):
            result = self.next_object()
        return result
    
    def process_files(self):
        file_description = self.next_file()
        while file_description:
            result = process_file(file_description)
            if result['state'] != 'identical':
                print(result)
            file_description = self.next_file()

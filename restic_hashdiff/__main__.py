import sys
import restic_hashdiff

def main():
    if len(sys.argv) != 2:
        print("Usage: restic_hashdiff restic.json")
        return 1
    
    hash_file = sys.argv[1]
        
    hd = restic_hashdiff.HashDiff(hash_file)
    hd.process_files()
    return 0
    

if __name__ == '__main__':
    sys.exit(main())

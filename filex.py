#14.1
def sed(pattern_string, new_string, filename1, filename2):
    try:
        fl1 = open(filename1, 'r')
        fl2 = open(filename2, 'w')
    except:
        print("There is something wrong with opening the files")
    
    for line in fl1:
        if pattern_string in line:
            line.replace(pattern_string, new_string)
            fl2.write(line)
    fl1.close()
    fl2.close()

#14.3
import os

def search_file(dirname):
    """Finds the names of all files in dirname and its subdirectories.
    dirname: string name of directory
    """
    names = []
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(search_file(path))
    return names

def compute_checksum(filename):
    """Computes the MD5 checksum of the contents of a file. 
    filename: string
    """
    cmd = 'md5sum' + filename
    return pipe(cmd)

def check_diff(name1, name2):
    """Computes the difference between the contents of two files. 
    name1, name2: string filenames
    """
    cmd = 'diff %s %s' % (name1, name2)
    return pipe(cmd)

def pipe(cmd):
    """Runs a command in a subprocess. 
    cmd: string Unix command
    Reterns (res, stat), the output of the subprocess and the exit status. 
    """
    # Note: os.popen() is deprecated
    # now, which means we are supposed to stop using it and start using
    # the subprocess module. But for simple cases, I find
    # subprocess more complicates than necessary. So I am going
    # to keep using os.popen until they take it away.

    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    assert stat is None
    return res, stat

def compute_checksums(dirname, suffix):
    """Computes checksums for all files with the given suffix. 
    dirname: string name of directory ti search
    suffix: string suffix to match
    Returns: map from checksum to list of files with that checksum
    """
    names = search_file(dirname)

    d = {}
    for name in names:
        if name.endswith(suffix):
            res, stat = compute_checksum(name)
            checksum, _ = res.split()

            if checksum in d:
                d[checksum].append(name)
            else:
                d[checksum] = [name]
    
    return d

def check_pairs(names):
    """Checks whether any in alist of files differs from the others. 
    names: list of string filenames
    """
    for name1 in names:
        for name2 in names:
            if name1  < name2:
                res, stat = check_diff(name1, name2)
                if res:
                    return False

    return True

def print_duplicates(d):
    """Checks for duplicates files. 
    Reports any files with the same checksum and checks whether they 
    are, in fact, identical. 
    d: map from checlsum to list of files with that cheecksum
    """
    for key, names in d.items():
        if len(names) > 1:
            print('The following files have the same checksum:')
            for name in names:
                print(name)

            if check_pairs(names):
                print('And they are identical')

if __name__ == "__main__":
    dirname = os.getcwd()
    d = compute_checksums(dirname='.', suffix= '.py')
    print_duplicates(d)
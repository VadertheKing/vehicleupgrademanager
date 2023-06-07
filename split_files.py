import os
def get_words(file):
    with open(file, 'r') as f:
        data = f.read().replace('\n',' ')
    words = data.split()
    return len(words)

def split_file(file):
    with open(file, 'r') as f:
        data = f.read()
        if len(data.split()) > 4000:
            chunks = data.split('\n')
            chunks = [x.strip() for x in chunks if x.strip() != '']
            k = 1
            n = 1
            output = ''
            for chunk in chunks:
                l = len(output.split())
                output += chunk + str('\n')
                m = len(output.split())
                if m >= 4000:
                    with open(f'huge_file_{n}.txt', 'w') as f:
                        f.write(output)
                    output = ''
                    n += 1
            with open(f'huge_file_{n}.txt', 'w') as f:
                f.write(output)
        else:
            with open(f'{file}', 'r') as f:
                data = f.read()
                with open('new_'+file, 'w') as f:
                    f.write(data)
    os.remove(file)
    return 'new_'+file
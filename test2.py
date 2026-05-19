import os

def scan_files(root_dir):
    result = {}

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            size = os.path.getsize(full_path)
            key = filename[:3]

            if key not in result:
                result[key] = []
            result[key].append((size, filename))


    for key in result:
        result[key].sort(reverse=True)

    return result

#result = scan_files('/usr/share/doc')

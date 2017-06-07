import glob
import os
import sys
import subprocess




def resize_jpg_pc(path_in, path_out, size, list_files):
	for img_file in list_files:
		convert_process = subprocess.call(['convert', os.path.join(path_in, img_file), 
            '-resize', size, os.path.join(path_out, img_file)])
		print('File {} resize'.format(img_file))

def resize_jpg_mac(path_in, path_out, size, list_files):
    for img_file in list_files:
        copy_process = subprocess.run(['cp', os.path.join(path_in, img_file), 
            os.path.join(path_out, img_file)])
        convert_process = subprocess.run(['sips', '--resampleWidth', size, 
            os.path.join(path_out, img_file)])
        print('File {} resize'.format(img_file))
        
def read_file(path_in):
    files = os.listdir(path=path_in)
    print(files)
    return files

def main():
    path_in = 'Source'
    path_out = 'Result'
    size = '200'
    l_files = read_file(path_in)
    if sys.platform == 'darwin':
        resize_jpg_mac(path_in, path_out, size, l_files)
    else:
        resize_jpg_pc(path_in, path_out, size, l_files)

    print('Конвертация завершена')



main()

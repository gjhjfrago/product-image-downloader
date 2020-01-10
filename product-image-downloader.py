
import csv
import os
import sys
import urllib.request

join = os.path.join
basename = os.path.basename
splitext = os.path.splitext
exists = os.path.exists
mkdir = os.mkdir
urlretrieve = urllib.request.urlretrieve


def download_images(filename):
    folder_name = splitext(basename(filename))[0]
    projectDIR = join(os.getcwd(), folder_name)

    if not exists(projectDIR):
        mkdir(projectDIR)
        print('Folder {} created.'.format(str(folder_name)))

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        row_number = 0

        for row in csv_reader:
            sku = row[0]
            folderDIR = join(projectDIR, sku)
            mkdir(folderDIR)
            print('Working on product {}'.format(sku))
            suffix = 1

            for c in range(1, 13):
                try:
                    url = row[c]
                    image_name = str(sku) + '_' + str(suffix) + '.jpg'
                    image_directory = join(folderDIR, image_name)
                    urlretrieve(url, image_directory)
                    suffix += 1
                    print('Download successful')
                except:
                    print('Cell is invalid')

            row_number += 1
            no_of_images = suffix - 1
            print('{} images'.format(no_of_images))

        print('Downloaded images of {} products'.format(str(row_number)))


def main(args):

    if len(args) >= 2:
        filename = args[1]
        download_images(filename)
    else:
        print('Failed. Try again.')

    input('Press any key to exit')


main(sys.argv)

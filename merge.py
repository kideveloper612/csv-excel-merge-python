import os
import csv


def read_csv(path):
    with open(file=path, mode='r') as csv_file:
        rows = list(csv.reader(csv_file))
    return rows


def write_csv(lines, path):
    with open(file=path, encoding='utf-8', mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows(lines)


def main():
    write_csv(lines=[header], path='Save.csv')
    for files in os.listdir(folder):
        if 'csv' in files:
            if 'dealer' in files:
                dealers = read_csv(files)
            elif 'GM' in files:
                gms = read_csv(files)
                for gm in gms:
                    dealer_id = gm[0]
                    line = []
                    for dealer in dealers:
                        if dealer[0] == dealer_id:
                            street = dealer[6]
                            city = dealer[7]
                            state = dealer[8]
                            zip_code = dealer[10]
                            for i in gm[:7]:
                                line.append(i)
                            for i in [street, city, state, zip_code]:
                                line.append(i)
                            for i in gm[7:]:
                                line.append(i)
                            write_csv(lines=[line], path='Save.csv')
                            break


if __name__ == '__main__':
    header = ['dealer_id', 'First', 'Last', 'designation', 'email', 'phone', 'photo_url', 'street', 'city', 'state',
            'zip', 'url', 'dealership_name', 'domain', 'OEM1', 'OEM2', 'OEM3', 'OEM4', 'OEM5', 'OEM6', 'OEM7']

    folder = 'F:\\working\\python\\scrapping\\Randy\\dealerrater\\merge'
    main()

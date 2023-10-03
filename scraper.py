# python3 scraper.py --class=<combo|OR> --homework=<int> --directory=<str (recommended class + hw#)>

###############################################################################
#                                                                             #
#                            Author: Max White                                #
#                                                                             #
###############################################################################

import os
import requests
import argparse

parser = argparse.ArgumentParser(description="CLI for Alan Frieze Webscraper")

parser.add_argument('--class', dest='class_name', type=str, required=True)
parser.add_argument('--homework', type=int, required=True)
parser.add_argument('--directory', type=str, required=True)

or_years = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '17', '18', '19']
combo_years = ['05', '06', '07', '08', '09', '10', '11', '12', '15', '21']

def request(years, url, homework, download_dir):
    for year in years:
        year = 'F' + year
        for i in range(-1, 2):
            try:
                pdf_url = download_dir + '/' + year + 'hw' + str(homework+i) + 'a.pdf'
                response = requests.get(url + '/' + year + '/' + 'hw' + str(homework+i) + 'a.pdf')
                if response.status_code == 200:
                    with open(pdf_url, 'wb') as pdf_file:
                        pdf_file.write(response.content)
                    print(f"Downloaded PDF to {pdf_url}")

                else:
                    print(f"Failed to download PDF {pdf_url}. Status code: {response.status_code}")
        
            except requests.exceptions.RequestException as e:
                print(f"An error occured: {e}")

def main():
    args = parser.parse_args()

    class_name = args.class_name
    homework_number = args.homework

    script_dir = os.path.dirname(os.path.abspath(__file__))
    download_dir = os.path.join(script_dir, args.directory)
    os.makedirs(download_dir, exist_ok=True)

    if class_name == "combo":
        url = "https://www.math.cmu.edu/~af1p/Teaching/Combinatorics"
        request(combo_years, url, homework_number, download_dir)
    elif class_name == "OR":
        url = "https://www.math.cmu.edu/~af1p/Teaching/OR2"
        request(or_years, url, homework_number, download_dir)
    else:
        print("Class must be either 'combo' or 'OR' exiting...")
        exit(1)

if __name__ == '__main__':
    main()
    
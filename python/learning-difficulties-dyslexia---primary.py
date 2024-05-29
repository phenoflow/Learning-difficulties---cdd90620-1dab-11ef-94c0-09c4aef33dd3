# A. John, Y. Friedmann, M. DelPozo-Banos, A. Frizzati, T. Ford, A. Thapar, 2024.

import sys, csv, re

codes = [{"code":"R0463","system":"readv2"},{"code":"2B55.","system":"readv2"},{"code":"8E23.","system":"readv2"},{"code":"R48.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('learning-difficulties-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["learning-difficulties-dyslexia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["learning-difficulties-dyslexia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["learning-difficulties-dyslexia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

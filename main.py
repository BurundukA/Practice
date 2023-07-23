from parsing import parsing
from exracting_urls import extract_text_between_commas, extract_text_before_comma
from finding_data import extract_bacteria_names
import xlwt


excel_file = input("Enter the the full path and name of the files, where your links are being kept: ")
#C:/Users/Настя/PycharmProjects/Summer/PlantDisease.Scopus.Part.xlsx
link_count = int(input("Enter the number of links to extract: "))
extracted_text = extract_text_between_commas(excel_file, link_count)
extracted_year = extract_text_before_comma(excel_file, link_count)
#print(extracted_text, extracted_year)
book = xlwt.Workbook(encoding="utf-8")

sheet1 = book.add_sheet("Sheet1", cell_overwrite_ok=True)
sheet1.write(0, 0, "taxonomy ID")
sheet1.write(0, 1, "name of pathogen")
sheet1.write(0, 2, "host plant")
sheet1.write(0, 3, "geolocation")
sheet1.write(0, 4, "year of paper")
sheet1.write(0, 5, "doi")


index = 0
st = 0
for part_of_link in extracted_text:
    text_for_analys = parsing(part_of_link)
    names_id_pairs, geolocation = extract_bacteria_names(text_for_analys)
    print(geolocation)
    #print(len(names_id_pairs))
    for tax_id, name in names_id_pairs:
        sheet1.write(st, 0, str({tax_id}))  # Convert tax_id to a string before writing
        sheet1.write(st, 1, str({name}))
        sheet1.write(st, 4, str(extracted_year[index]))
        sheet1.write(st, 5, str(part_of_link))
        st+=1
    index += 1

book.save('bacterium_info.xls')
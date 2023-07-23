import xlwt


def add_data_to_excel (bacterium_info,extracted_doi,extracted_year,st, sheet1):
    for (tax_id, name) in enumerate(bacterium_info, start=0):
        sheet1.write(st, 0, str(tax_id))  # Convert tax_id to a string before writing
        sheet1.write(st, 1, str(name))
        sheet1.write(st, 4, str(extracted_year))
        sheet1.write(st, 5, str(extracted_doi))
        st += 1

    return st


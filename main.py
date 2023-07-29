from tablerworld import download
import json
import os
import pandas as pd

FILE_CONTACTS_JSON = "data_contacts.json"
FILE_CONTACTS_EXCEL = "data_contacts.xlsx"


def main():
    # Download contacts if not available
    if not os.path.isfile(FILE_CONTACTS_JSON):
        contacts = download.contacts()
        with open(FILE_CONTACTS_JSON, "w") as file_contacts:
            json.dump(contacts, file_contacts)
    else:
        # Read and parse contacts file
        with open(FILE_CONTACTS_JSON, "r") as file_contacts:
            contacts = json.load(file_contacts)

    df = pd.DataFrame(contacts)
    print(df)
    df.to_excel(FILE_CONTACTS_EXCEL, sheet_name="contacts", index=False)


if __name__ == "__main__":
    main()
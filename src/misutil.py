import json
import requests
import os
import tempfile
import zipfile


def get_ice_doc_list(report_id: str) -> dict:
    """
    Get a list of documents for a given report type id

    Parameters:
    ----------
        report_id (str): The report type id to get documents for

    Returns:
    ----------
        dict: A dictionary of documents
    """

    url = f'https://www.ercot.com/misapp/servlets/IceDocListJsonWS?reportTypeId={report_id}'
    r = requests.get(url)
    ice_doc_list = json.loads(r.text)
    documents = ice_doc_list['ListDocsByRptTypeRes']['DocumentList']
    return documents


def get_zipped_file_contents(document_id: str) -> bytes:
    """
    Get the contents of a zipped file from a url

    Parameters:
    ----------
        url (str): The url to get the zipped file from

    Returns:
    ----------
        bytes: The contents of the zipped file
    """
    url = f'https://www.ercot.com/misdownload/servlets/mirDownload?doclookupId={document_id}'

    filename = '/tmp/' + next(tempfile._get_candidate_names())
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)

    with zipfile.ZipFile(filename, "r") as f:
        target = f.filelist[0]
        file_path = f'/tmp/{target.filename}'
        f.extract(target, '/tmp')
        with open(file_path, 'rb') as f:
            b = f.read()

    # delete temporary file
    os.remove(filename)

    return b
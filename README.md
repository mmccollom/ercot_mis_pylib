# ERCOT Python Utility
This library aims to ease the use of the ERCOT MIS system.

### How to use
    from ercotutils import misutil
    
    # Get a list of all the ICE documents for a given report type
    ice_doc_list = misutil.get_ice_doc_list('13499')

    ....


    # Get the file contents of a zipped csv document
    byte_content = misutil.get_zipped_file_contents('4433444')


### License
MIT License
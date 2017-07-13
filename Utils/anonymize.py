import csv


def get_file_contents(filename):
    "Get the file contents of a CSV. Return the entries and a list of fieldnames."
    with open(filename) as f:
        reader = csv.DictReader(f)
        entries = list(reader)
        fieldnames = reader.fieldnames
        return entries, fieldnames


def anonymize(entries):
    "Anonymize the entries by mapping the IPs and worker IDs to integers."
    worker_ids = {e['_worker_id'] for e in entries}
    ip_addresses = {e['_ip'] for e in entries}
    
    ident_dict = {ident: i for i, ident in enumerate(worker_ids)}
    address_dict = {address: i for i, address in enumerate(ip_addresses)}
    
    for e in entries:
        worker_id = e['_worker_id']
        ip_address = e['_ip']
        
        e['_worker_id'] = ident_dict[worker_id]
        e['_ip'] = address_dict[ip_address]


def process_file(infile, outfile):
    "Process a file and write the anonymized version to the disk."
    entries, fieldnames = get_file_contents(infile)
    anonymize(entries)
    with open(outfile, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(entries)

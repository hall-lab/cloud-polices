import click, google.cloud, tabulate, sys

@click.command(short_help="list buckets")
@click.option("--size/--no-size", default=False, show_default=True, help="Add bucket size.")
def buckets_list_cmd(size):
    """
    List Buckets
    """
    storage_client = google.cloud.storage.Client()
    headers = ["NAME", "LOCATION", "CLASS", "USER", "PROJECT", "PIPELINE"]
    if size:
        headers.append("SIZE")
    rows = [headers]
    for bucket in storage_client.list_buckets():
        row = [bucket.name, bucket.location, bucket.storage_class]
        labels = bucket.labels
        if labels:
            for k in ("user", "project", "pipeline"):
                if k in labels:
                    row.append(labels[k])
                else:
                    row.append(None)
        else:
             row += [None, None, None]
        rows.append(row)
        if size:
            row.append(get_bucket_size(bucket))
        if len(rows) == 3: break

    sys.stdout.write(tabulate.tabulate(rows, headers="firstrow", tablefmt="simple"))

def get_bucket_size(bucket):
    sz = 0
    for blob in bucket.list_blobs():
        sz += blob.size
    return sz

#-- get_bucket_size

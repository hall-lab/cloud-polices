# Hall Lab Cloud Policies

---

# Access

Buckets will use IAM permissions through Google groups and service accounts for ownership and access instead of individual owners and access control lists (ACLs) when possible. IAM is applied at the bucket level, ACLs can be applied atthe object level. Access is only needed from one of these ways to have that permission on an object/bucket. IAM is currently preferred over ACLs.

## IAM

---

### IAM Defaults

---

### Storage Access Roles

* storage.admin - full control of objects and buckets. 
* storage.objectAdmin - full control of objects, including listing, creating, viewing, and deleting objects
* storage.objectCreator	 - allows users to create objects. Does not give permission to view, delete, or overwrite objects
* storage.objectViewer - view/list objects and their metadata

---

# FIN

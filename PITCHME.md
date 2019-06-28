# Hall Lab Cloud Policies

---

# Access Control

Buckets should preferrably use IAM (Identity and Access Management) via Google groups and service accounts for ownership/access instead of individual owners and access control lists (ACLs). IAM is applied at the bucket level, ACLs can be applied atthe object level. Access is only needed from one of these ways to have that permission on an object/bucket, leading to confusing permssions.

---

## ACLs

Still exist, but we will limit their scope to project owners.

Defaults ACLs Roles:
* OWNERS
** project-owners
** project-editors
* READER
** project-viewers

We will remove the all but the OWNER=project-owners ACL.

## IAM


---

### IAM Defaults

---

### IAM Storage Access Roles

* storage.admin - full control of objects and buckets. 
* storage.objectAdmin - full control of objects, including listing, creating, viewing, and deleting objects
* storage.objectCreator	 - allows users to create objects. Does not give permission to view, delete, or overwrite objects
* storage.objectViewer - view/list objects and their metadata

---

### Our IAM Settings

---

# FIN

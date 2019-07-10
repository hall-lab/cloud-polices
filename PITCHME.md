# Hall Lab Cloud Policies

---

# Access Control

---

## Identity Access Management (IAM)

Cloud IAM allows you to control who has access to the resources in your Google Cloud Platform project. Resources include Cloud Storage buckets and objects stored within buckets, as well as other GCP entities such as Compute Engine instances.

---

## Access Control Lists (ACL)
An ACL is a mechanism you can use to define who has access to your buckets and objects, as well as what level of access they have. In Cloud Storage, you apply ACLs to individual buckets and objects.

---

## IAM Policies

* Buckets should use primarily IAM for access management
* Google groups and service accounts should be used for ownership/access instead of individual owners and ACLs

---

### IAM Storage Access Roles

* storage.admin - full control of objects and buckets. 
* storage.objectAdmin - full control of objects, including listing, creating, viewing, and deleting objects
* storage.objectCreator	 - allows users to create objects. Does not give permission to view, delete, or overwrite objects
* storage.objectViewer - view/list objects and their metadata

---

## ACLs Policy

Per our policy, we want to limit the use of ACLs. We will still leave one ACl on buckets, the OWNER=project-owners role.

Defaults ACLs Roles:
* OWNERS
 * project-owners [keep]
 * project-editors [remove]
* READER
 * project-viewers [remove]

---

# Labels

Labels will be used to track ownership, and for calculating costs of projects and pielines.

---

## Required Lables

These labels are required, but others may be added.

* person - the user name of the primary contact for the bucket
* project - the general project that the bucket is being used for
* pipeline - software pipeline that is ancipated to be used

---

# FIN

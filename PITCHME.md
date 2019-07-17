# Hall Lab Cloud Policies

---

# Access Control

---

## Access Control Methods

* IAM
* ACLs

---

## Identity Access Management (IAM)

Cloud IAM allows you to control who has access to the resources in your Google Cloud Platform project. Resources include Cloud Storage buckets and objects stored within buckets, as well as other GCP entities such as Compute Engine instances.

---

### IAM Policies

* Buckets should use primarily IAM for access management
* Google groups and service accounts should be used for ownership/access instead of individual owners and ACLs

---

### IAM Storage Access Roles

* storage.admin - full control of objects and buckets. 
* storage.objectAdmin - full control of objects, including listing, creating, viewing, and deleting objects
* storage.objectCreator	 - allows users to create objects. Does not give permission to view, delete, or overwrite objects
* storage.objectViewer - view/list objects and their metadata

---

### Google Groups for IAM

Google groups are managed through G-Suite. They allow for granular and continuty in access by adding and removing users. Niel and Eddie can make groups, but once created, ownership can be modified.

---

## Access Control Lists (ACL)
An ACL is a mechanism you can use to define who has access to your buckets and objects, as well as what level of access they have. In Cloud Storage, you apply ACLs to individual buckets and objects.

---

### ACLs Policy

Per our policy, we want to limit the use of ACLs. We will still leave one ACL on buckets, the OWNER=project-owners role.

Defaults ACLs Roles:
* OWNERS
 * groups [add]
 * project-owners [keep]
 * project-editors [remove]
* READER
 * project-viewers [remove]

---

# Labels

Labels will be used to track ownership, and for calculating costs of projects and pipelines.

---

### Required Labels

These labels are required, but others may be added.

* person - the user name of the primary contact for the bucket
* project - the general project that the bucket is being used
* pipeline - software pipeline that is anticipated to be used

---

# README

A README file in the top level of the bucket provides additional notes.

---

### README Spec

* what should be included?
* what should the file name be?

---

# Scripts

Helper scripts will be available via docker image and github repo for making buckets, adding labels, and auditing.

---

# FIN

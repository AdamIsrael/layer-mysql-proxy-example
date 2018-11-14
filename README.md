# Overview

Few applications are so simple that they can run independently - most rely on other applications. A certain charm knows that it requires, say, a database and, correspondingly, a database charm knows that is capable of accommodating the other charm's requirements. The act of joining such mutually-dependent charms causes code (hooks) to run in each charm in such a way that both charms can effectively talk to one another. When charms have joined logically in this manner they are said to have formed a relation.

It becomes slightly more complicated when one of the applications is not deployed by a charm, such as a VNF running in a VM.

This charm provides an example of "proxying" the relation between a VNF and a cloud-native service (in this case, a database).

For more information, please refer to the following documentation:
- [Relation lifecycle](https://docs.jujucharms.com/2.4/en/authors-relations-in-depth)
- [Implementing relations](https://docs.jujucharms.com/2.4/en/authors-relations)
- [Creating a VNF charm](https://osm.etsi.org/wikipub/index.php/Creating_your_VNF_Charm)

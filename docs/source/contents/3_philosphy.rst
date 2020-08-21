##########
Philosophy
##########

*****
About
*****

In creating our mapping from MODS to RDF, the working group developed over time several principles to shape a shared
philosophy. Our philosophy seeks to ensure that we are good linked data citizens by attempting to adhere to the
principles, standards, and best practices set forth of linked data described in documents such as `Tim Berners-Lee’s Four Principles of Linked Data <https://www.w3.org/DesignIssues/LinkedData.html>`_,
`Best Practice Recipes for Publishing RDF Vocabularies <https://www.w3.org/TR/swbp-vocab-pub/>`_,
`How to Publish Linked Data on the Web <wifo5-03.informatik.uni-mannheim.de/bizer/pub/LinkedDataTutorial/>`_,
`Cool URIs for the Semantic Web <https://www.w3.org/TR/cooluris/>`_, and `RDF Schema <https://www.w3.org/TR/rdf-schema/>`_.
The philosophy also attempts to have a user centered approach to description and keep things as simple as possible
from a technical standpoint. Each principle is detailed below.

**********
Principles
**********

Principle One: Use Popular and Bibliographic Ontologies When Possible
=====================================================================

When choosing RDF properties, we recognize that reusing existing vocabularies allows our data to be easily consumed by other applications. In selecting existing vocabularies, we follow a few
simple rules:

1. Use core vocabularies when possible.  These are the vocabularies that are commonly used by RDF applications regardless of content and often describe people, projects, web resources, publications, and addresses. Use `Linked Open Vocabularies <https://lov.linkeddata.es/dataset/lov/>`_ as the source for identifying core vocabularies. Examples of core vocabularies include: RDF, RDFS, OWL, SKOS, FOAF, GeoNames, Dublin Core Elements, and Dublin Core Terms.
2. When a core vocabulary is not sufficient, use a “popular” vocabulary in use by libraries, archives, or museums. Examples include: BIBFRAME, OpaqueNamespaces
3. When possible, ensure that the vocabulary adheres to our other philosophical principles listed below. If this is not possible, we will justify why we are making an exception for a vocabulary.
4. Do not duplicate efforts. Look first to vocabularies suggested by other communities (Samvera, Islandora, DPLA).

Principle Two: Choose Dereferenceable and Content Negotiable URIs
=================================================================

When choosing RDF properties and classes, the working group attempts to select URIs that are not only dereferenceable
but adhere to the principles of content negotiation. In order to be dereferenceable, the URI should return information
about the URI when queried. This aligns with Tim Berners-Lee’s third principle by being able to “look up the properties
and classes one finds in data, and get information from the RDF, RDFS, and OWL ontologies including the relationships
between the terms in the ontology.” Additionally, the URIs should adhere to the principles of content negotiation and
specifically enable a user to agnostically request RDF from a URI and return RDF without having to possess any special
knowledge about a particular vocabulary or technical implementation. In other words, a user or application should not
have to concatenate a string to the end of a URI in order to get back RDF.

Principle Three: Adhere to "rdfs:domain" and "rdfs:range" Properties
====================================================================

When choosing RDF properties, the working group recognizes that the property in question may have rules for the subjects
and objects that relate to it.  These rules are expressed in the property’s properties and can come from a variety of
ontologies including RDFS and OWL but also lesser known ontologies. These rules may simply express whether the value of
an object can be a literal or URI but can also state more specifically the class the object must be an instance of.
While we closely review all properties of the RDF property being considered and attempt to understand all the rules its
schema states about its use, we ensure that we minimally adhere to any rules set forth by RDFS especially as it relates
to the rdfs:domain or rdfs:range property.

Principle Four: Avoid Blank Nodes
=================================

In our mapping of MODS to RDF, the working group decided to avoid using blank nodes in any circumstance. This is due mainly to feelings shared across the RDF and Linked Data communities that blank nodes create challenges for applications and users consuming your data. As stated by the W3C’s Sandro Hawke,

    “In general, blank nodes are a convenience for the content provider and a
    burden on the content consumer. Higher quality data feeds use fewer
    blank nodes, or none. Instead, they have a clear concept of identity
    and service for every entity in their data.

    If someone in the middle tries to convert (Skolemize) blank nodes, it’s
    a large burden on them. Specifically, they should provide web service
    for those new URIs, and if they get updated data from their sources,
    they’re going to have a very hard [perhaps impossible] time
    understanding what really changed.”

As Hawke states above, in order for a blank node to be dereferenced and consumed, it is often necessary to skolemize the blank node by converting it to a blank node. This process can provide a number of challenges and we would prefer to avoid this altogether.

While we do not create blank nodes, it is important to recognize that many of the URIs and properties that we use do. We do consider blank node use in our selection of vocabularies.

Principle Five: Mint Objects as a Last Resort
=============================================

The working group avoids minting objects unless it is absolutely necessary to do so. The only two use cases where an
object should be locally minted in our opinion are when retaining complexity is necessary or a local concept needs to
be linked to another URI. By retaining complexity, we mean associating related information between the objects of two
or more triples. We endeavor to eliminate complexity where possible so that minting for this reason is unnecessary. The
other and more acceptable use case is for when we need to create a local authority of a subject, person, or concept and
relate that concept to a related URI.

Principle Six: Follow Descriptive Standards for String Literals
===============================================================

A variety of descriptive standards inform our decisions on how to best present metadata. Formal standards include
`Resource Description and Access <https://www.rdatoolkit.org/>`_ (RDA) traditionally used primarily for the creation of
MARC records and the `Descriptive Cataloging of Rare Materials <http://rbms.info/dcrm/>`_ (DCRM) manuals. As the
University of Tennessee, Knoxville acts as a Digital Public Library of America (DPLA) service hub,
`DPLA’s Metadata Application Profile <https://pro.dp.la/hubs/metadata-application-profile>`_ (MAP) also informs
decisions concerning descriptive metadata. Given the direct impact on its ability to be shared, DPLA’s MAP often
takes precedence. Still, all of these resources inform how UTK’s metadata is currently in MODS and how the information
is mapped to RDF. Ultimately rules that make the metadata more accessible to users are privileged, regardless of the
source.

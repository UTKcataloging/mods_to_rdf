Modelling a UTK MODS File Based on the Islandora MODS to RDF Recommendations
============================================================================

The Samvera MODS to RDF Working Group's `MODS to RDF Mapping Recommendations <https://docs.google.com/document/d/1m14BxPglWNWeJykx5Pv9s4UCI1jgWCXMiy1wQpsL4S4/edit>`_
shares a direct mapping and a style guide.  This document illustrates how one of our XML files may look if we followed these mappings out-of-the-box.
For the purposes of this exercise, our group decided to use the MODS file for `knoxgardens:115 <https://digital.lib.utk.edu/collections/islandora/object/knoxgardens%3A115/datastream/MODS>`_.


Default Islandora Mapping
-------------------------

.. code-block:: turtle
    :linenos:
    :caption: RDF following Islandora Default Mapping
    :name: RDF following Islandora Default Mapping

    @prefix fedoraObject: <http://[LocalFedoraRepository]/> .
    @prefix identifiers: <http://id.loc.gov/vocabulary/identifiers> .
    @prefix dcterms: <http://purl.org/dc/terms/> .
    @prefix foaf: <http://xmlns.com/foaf/0.1/> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
    @prefix edm: <http://www.europeana.eu/schemas/edm/> .
    @prefix rdau: <http://rdaregistry.info/Elements/u/#> .
    @prefix dce: <http://purl.org/dc/elements/1.1/> .
    @prefix relators: <http://id.loc.gov/vocabulary/relators> .
    @prefix bf: <http://id.loc.gov/ontologies/bibframe/> .
    @prefix pcdm: <http://pcdm.org/models#> .
    @prefix dbo: <http://dbpedia.org/ontology/> .

    <fedoraObject:tq/57/nr/06/tq57nr067>
        dcterms:identifier "0012_000463_000214" ;
        dcterms:title "Tulip Tree" ;
        dcterms:abstract "Photograph slide of the Tennessee state tree, the tulip tree" ;
        dcterms:created "1930/1939" ;
        edm:hastype <http://vocab.getty.edu/aat/300134977> ;
        rdau:extent "3 1/4 x 5 inches" ;
        dce:format "image/jp2" ;
        relators:pht <http://id.loc.gov/vocabulary/relators/pht> 
    	foaf:name <https://example.org/names/1> ;
        dbo:collection "Knoxville Gardens Slides" ;
        dbo:isPartOf <https://n2t.net/ark:/87290/v88w3bgf> ;
        dcterms:type <http://id.loc.gov/vocabulary/resourceTypes/img> ;
        dce:subject <http://id.loc.gov/authorities/subjects/sh85101348>, <http://id.loc.gov/authorities/subjects/sh85053123>, <http://id.loc.gov/authorities/subjects/sh85077428>, <http://id.loc.gov/authorities/subjects/sh85049328>;
        dce:coverage <http://id.loc.gov/authorities/names/n79109786>, "35.96064, -83.92074" ;
        skos:note "Mrs. A. C. Bruner donated this collection to the University of Tennessee. Creation dates were inferred from the dates associated with the archival collection and the activity dates of the Jim Thompson Company." ;
        relators:rps <http://id.loc.gov/authorities/names/no2014027633> ;
        bf:physicalLocation "University of Tennessee, Knoxville. Special Collections" ;
        pcdm:memberOf <fedoraObject:jk/88/99/adklasd908ads> ;
        bf:descriptionLanguage "English" ;
        edm:provider <http://id.loc.gov/authorities/names/n87808088> ;
        edm:rights <http://rightsstatements.org/vocab/CNE/1.0/> .

==========
identifier
==========

Only three categories of identifiers are defined by the Islandora mapping: ISBNs, ISSNs, and
identifiers without types or with type="local". Instructions state that dcterms:identifier should be used "for identifiers 
without types or type= 'local'". All of our current identifiers have types. In MODS there is no 
controlled list of type terms, though there are suggested terms <https://www.loc.gov/standards/sourcelist/standard-identifier.html>.

.. code-block:: turtle

    @prefix fedoraObject: <http://[LocalFedoraRepository]/> .
    @prefix dcterms: <http://purl.org/dc/terms/> .

    <fedoraObject:tq/57/nr/06/tq57nr067>
        dcterms:identifier "0012_000463_000214" .

=========
titleInfo
=========

Islandora's mapping for title includes many advanced examples for uniform titles, translated titles,
and alternative titles. If nonSort, partNumber, or subTitle elements are present, the mapping shows how these can be
collapsed into a single string. Luckily our example is quite simple, but it's nice to have this
additional information. Note that while rdfs:label and skos:prefLabel were considered to represent the main title,
dcterms:title was used because it is "a mandatory element for RDF to be successfully pushed to Fedora."

.. code-block:: turtle

    @prefix fedoraObject: <http://[LocalFedoraRepository]/> .
    @prefix dcterms: <http://purl.org/dc/terms/> .

    <fedoraObject:tq/57/nr/06/tq57nr067>
                dcterms:title "Tulip Tree" .

========
abstract
========

All abstracts are mapped to dcterms:abstract.

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .
    @prefix fedoraObject: <http://[LocalFedoraRepository]/> .

    <fedoraObject:tq/57/nr/06/tq57nr067>
        dcterms:abstract "Photograph slide of the Tennessee state tree, the tulip tree" .

==========
originInfo
==========

Use `dcterms:created` to represent the date of creation (<mods:dateCreated>) for the object, formatted as an
EDTF​ string. If date intervals using point attributes are present, these should be transformed to a
single string following EDTF. Forward slashes are accepted in Level 0 to represent intervals - 
<https://www.loc.gov/standards/datetime/edtf.html> Further information on what levels of EDTF will be supported in
Islandora 8 can be found here <https://github.com/Islandora/documentation/issues/1364>

.. code-block:: turtle

    @prefix fedoraObject: <http://[LocalFedoraRepository]/> .
    @prefix dcterms: <http://purl.org/dc/terms/> .

    <fedoraObject:tq/57/nr/06/tq57nr067>
        dcterms:created "1930/1939" .

===================
physicalDescription
===================

Only <form>, <extent> and <internetMediaType> are present in this mapping. The value of dcterms:extent
is a blank node with a rdf:value which is a literal.

.. code-block:: xml

    <physicalDescription>
      <form authority="aat" valueURI="http://vocab.getty.edu/aat/300134977">lantern slides</form>
      <extent>3 1/4 x 5 inches</extent>
      <internetMediaType>image/jp2</internetMediaType>
    </physicalDescription>

.. code-block:: turtle

    @prefix fedoraObject: <http://[LocalFedoraRepository]/> .
    @prefix dcterms: <http://purl.org/dc/terms/> .

    <fedoraObject:tq/57/nr/06/tq57nr067>
        dcterms:format <http://vocab.getty.edu/aat/300134977> ;
        dcterms:extent "3 1/4 x 5 inches" ;
        dcterms:format <https://www.iana.org/assignments/media-types/image/jp2> .

====
name
====

The Islandora community felt it was important to retain the granularity many institutions
had created in their metadata through the use of MARC relator terms rather than simplifying
data to only use dc:contributor and dc:creator. Still, they leave this decision up to 
implementationBecause MARC relator are being used, this has 
the following implications for the mapping:

    MARC Relator terms are sub-properties of (rdfs:subPropertyOf) dc:contributor (the property in DC Elements),
    so this mapping entails (by rule rdfs7 of the RDFS Semantics Specification) that any named entity is also
    a dc:contributor of the work at hand.

Name values are minted, regardless of whether they already have an authorized form, because
many name values may not be authorized. Rather than treating the values differently or requiring
that name values be authorized, it was decided to mint entities across the board.

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .
    @prefix foaf: <http://xmlns.com/foaf/0.1/> .
    @prefix fedoraObject: <http://[LocalFedoraRepository]/> .

	<fedoraObject:tq/57/nr/06/tq57nr067>
    	relators:pht <http://id.loc.gov/vocabulary/relators/pht> 
    	foaf:name <https://example.org/names/1> ;
        a foaf:Person .


=======
subject
=======

Use dce:subject for topical subjects. Use edm:Place for geographic subjects. Create an agent
if the value refers to a name. Subjects are minted locally. The documentation deals extensively
with multiple topics nested within the same subject (though this complexity is not prevalent in
our metadata). Note that no XML or RDF examples are given for spatial values. Personally, I 
feel like some of this might need to be futher defined.

Still need to work in coordinates - "35.96064, -83.92074"

.. code-block:: turtle

    @prefix dce: <http://purl.org/dc/elements/1.1/> .

    <https://example.org/objects/1> dcterms:subject <https://example.org/subjects/1> .
 		<https://example.org/subjects/1> a skos:concept .
                                 rdfs:label "Photography of gardens" .
                                 schema:sameAs <http://id.loc.gov/authorities/subjects/sh85101348> .
    <https://example.org/objects/1> dcterms:subject <https://example.org/subjects/2> .
        <https://example.org/subjects/2> a skos:concept .
                                 rdfs:label "Gardens, American" .
                                 schema:sameAs <http://id.loc.gov/authorities/subjects/sh85053123> .
    <https://example.org/objects/1> dcterms:subject <https://example.org/subjects/3> .
        <https://example.org/subjects/3> a skos:concept .
                                 rdfs:label "Liriodendron tulipifera" .
                                 schema:sameAs <http://id.loc.gov/authorities/subjects/sh85077428> .
    <https://example.org/objects/1> dcterms:subject <https://example.org/subjects/4> .
        <https://example.org/subjects/4> a skos:concept .
                                 rdfs:label "Flowering trees" .
                                 schema:sameAs <http://id.loc.gov/authorities/subjects/sh85049328> .
                                 
	<https://example.org/objects/1> dce:spatial <https://example.org/spatial/1> .
		<https://example.org/spatial/1> a skos:concept .
                                 rdfs:label "Knoxville (Tenn.)" .
                                 schema:sameAs <http://id.loc.gov/authorities/names/n79109786> .


====
note
====

Notes that dc:description is not really appropriate for this element (despite recommendations
otherwise - <https://www.loc.gov/standards/mods/mods-dcsimple.html>) and that skos:note should
be used instead.

.. code-block:: turtle

    @prefix fedoraObject: <http://[LocalFedoraRepository]/> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .

    <fedoraObject:tq/57/nr/06/tq57nr067>
    skos:note "Mrs. A. C. Bruner donated this collection to the University of Tennessee. Creation dates were inferred from the dates associated with the archival collection and the activity dates of the Jim Thompson Company." ;

==============
typeOfResource
==============

The mapping suggests using LoC's resource type vocabulary <http://id.loc.gov/vocabulary/resourceTypes.html>
with dcterms:type

.. code-block:: xml

    <typeOfResource>still image</typeOfResource>

.. code-block:: turtle

    @prefix fedoraObject: <http://[LocalFedoraRepository]/> .
    @prefix dcterms: <http://purl.org/dc/terms/> .

    <fedoraObject:tq/57/nr/06/tq57nr067>
        dcterms:type <http://id.loc.gov/vocabulary/resourceTypes/img> .

===========
relatedItem
===========

From the docs:

    WARNING: Direct mappings for this element are complicated by the fact that <mods:relatedItem> "is a
    container element under which any MODS element may be used as a subelement" (​ MODS
    documentation​ ). For this reason, we ​ strongly ​ encourage the use of the ​ minted object mapping option
    for this element, in which minted objects for physical collections, series, subseries, and related works
    are described. This option is necessary if further nested series levels (subsubseries, etc.) are needed,
    and provides possibilities for more granular description of related objects.

In our sample, we have two stanzas (physical and digital):

.. code-block:: xml

    <relatedItem displayLabel="Project" type="host">
      <titleInfo>
         <title>Knoxville Garden Slides</title>
      </titleInfo>
    </relatedItem>
    <relatedItem displayLabel="Collection" type="host">
      <titleInfo>
         <title>Knoxville Gardens Slides</title>
      </titleInfo>
      <identifier>MS.1324</identifier>
      <location>
         <url>https://n2t.net/ark:/87290/v88w3bgf</url>
      </location>
    </relatedItem>

Use dbo:collection for the physical/source collection the item belongs to, if the value is a string literal.

Use dbo:isPartOf for the physical/source collection the item belongs to, if the value is a URI.

Use pcdm:isMemberOf to indicate the digital collection the item belongs to.

Use identifiers:[type] for an identifier corresponding to a parent item that the item being described belongs to. [Type] should be
replaced with the corresponding identifier type abbreviation from
`Library of Congress ​Standard Identifier Schemes​ <http://id.loc.gov/vocabulary/identifiers.html>`_.


.. code-block:: turtle

    @prefix fedoraObject: <http://[LocalFedoraRepository]/> .
    @prefix dbo: <http://dbpedia.org/ontology/> .
    @prefix pcdm: <http://pcdm.org/models#> .

    <fedoraObject:tq/57/nr/06/tq57nr067>
        pcdm:memberOf <fedoraObject:jk/88/99/adklasd908ads> ;
        dbo:collection "Knoxville Gardens Slides" ;
        dbo:isPartOf <https://n2t.net/ark:/87290/v88w3bgf> .

========
location
========

Mappings for the physical and online locations of the object being described and its digital surrogate.

Use relators:rps for <mods:physicalLocation> values, preferably using a URI for the organization from a controlled vocabulary
such as VIAF of Library of Congress Real World Objects.

.. code-block:: xml

    <location>
      <physicalLocation valueURI="http://id.loc.gov/authorities/names/no2014027633">University of Tennessee, Knoxville. Special Collections</physicalLocation>
    </location>

.. code-block:: turtle

    @prefix fedoraObject: <http://[LocalFedoraRepository]/> .
    @prefix relators: <http://id.loc.gov/vocabulary/relators> .

    <fedoraObject:tq/57/nr/06/tq57nr067>
        relators:rps <http://id.loc.gov/authorities/names/no2014027633> .

==========
recordInfo
==========

From the docs:

    WARNING: The predicates below from the BIBFRAME vocabulary are intended to describe an object
    with the class bf:adminMetadata rather than an intellectual, academic, or cultural heritage object. The
    usage recommended below is therefore questionable. However, since the group was unable to find
    other predicates representing these concepts, and because there is often a lack of distinction between
    a digital object and its metadata in many digital asset management systems, we have included the
    mappings here.

Here is our XML:

.. code-block:: xml

    <recordInfo>
      <recordContentSource valueURI="http://id.loc.gov/authorities/names/n87808088">University of Tennessee, Knoxville. Libraries</recordContentSource>
      <languageOfCataloging>
         <languageTerm type="text" authority="iso639-2b">English</languageTerm>
      </languageOfCataloging>
    </recordInfo>

Use edm:dataprovider for the organization responsible for creating the metadata record. Only used where this value may
need to be differentiated from the institution managing the repository.

Use edm:provider for the organization responsible for making the metadata record and/or digital object available.

Use bf:descriptionLanguage for the language of cataloging, preferably from a controlled vocabulary, such as ​
`ISO 639-2​ <http://id.loc.gov/vocabulary/iso639-2.html>`_.

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/> .
    @prefix fedoraObject: <http://[LocalFedoraRepository]/> .
    @prefix bf: <http://id.loc.gov/ontologies/bibframe/> .

    <fedoraObject:tq/57/nr/06/tq57nr067>
        bf:descriptionLanguage "English" ;
        edm:provider <http://id.loc.gov/authorities/names/n87808088> .

===============
accessCondition
===============

Since we have a rightsstatements.org URI, we should use `edm:rights`.

.. code-block:: xml

    <accessCondition type="use and reproduction"
                    xlink:href="http://rightsstatements.org/vocab/CNE/1.0/">
        Copyright Not Evaluated
    </accessCondition>

.. code-block:: turtle

    @prefix fedoraObject: <http://[LocalFedoraRepository]/> .
    @prefix edm: <http://www.europeana.eu/schemas/edm/> .

    <fedoraObject:tq/57/nr/06/tq57nr067>
        edm:rights <http://rightsstatements.org/vocab/CNE/1.0/> .

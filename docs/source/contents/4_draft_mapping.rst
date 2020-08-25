###############################
UTK MODS to RDF Mapping - Draft
###############################

***********
Style Guide
***********

This document aims to provide all of the information a member of Digital Initiatives needs to transform UTK’s existing
MODS XML to RDF, regardless of the platform chosen. In order to achieve this goal in a consistent and accessible manner,
we will compose the mapping document according to the following practices.

The document will be structured according to `MODS top level elements <https://www.loc.gov/standards/mods/userguide/generalapp.html>`_
and provide examples of use cases associated with each element. For each use case, example XML for the element being mapped,
along with a link to the full MODS record, should be included. Turtle notation, with semicolons separating separate statements
about the same subject, will be used as the RDF serialization format. All of the namespaces used as prefixes in the example
turtle should be included so that it can be validated. RDF should use example.org "URIs" that include a number (use /1 for
the first instance of a minted URI in each example, as though each individual example section is independent of all the others).
For more complex examples, graphs illustrating the RDF should also be included to make the relationships more easily understood.
More complex examples might include those with minted object or elements that include several relationships (like a geographic
subject with coordinates). Graphs should not be necessary for the RDF representing flat elements, like abstract.

Beyond the focused attention on individual elements, the document will also include broader examples and information. A
section listing all prefixes used will be present as well as a complete example of a single MODS record transformed
according to the guide’s specifications. The elements are listed in the order outlined on `DLTN technical documentation
<https://dltn-technical-docs.readthedocs.io/en/latest/style/xsl.html>`_.

Simple Example
==============

`Example record - knoxgardens:115 <https://digital.lib.utk.edu/collections/islandora/object/knoxgardens%3A115/datastream/MODS>`_.

.. code-block:: xml

    <abstract>Photograph slide of the Tennessee state tree, the tulip tree</abstract>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

        <https://example.org/objects/1> dcterms:abstract "Photograph slide of the Tennessee state tree, the tulip tree" .

**********
Namespaces
**********

+------------------+----------------------------------------+
| Predicate Prefix | Namespace                              |
+==================+========================================+
| bf               | http://id.loc.gov/ontologies/bibframe/ |
+------------------+----------------------------------------+
| dce              | http://purl.org/dc/elements/1.1/       |
+------------------+----------------------------------------+
| edm              | http://www.europeana.eu/schemas/edm/   |
+------------------+----------------------------------------+
| opaque           | http://opaquenamespace.org/ns/         |
+------------------+----------------------------------------+
| skos             | http://www.w3.org/2004/02/skos/core#   |
+------------------+----------------------------------------+

*******
Mapping
*******

identifier
==========

titleInfo
=========

+-----------------------------------+----------------+-------------------+-------------------------------------------------------------------------+
| Predicate                         | Value Type     | Range (if needed) | Usage Notes                                                             |
+===================================+================+===================+=========================================================================+
| dcterms:title                     | Literal        |                   | A name given to the resource. If multiple titleInfo elements are        |
|                                   |                |                   | present, supplied title is assumed to the title. Using of []            |
|                                   |                |                   | to note supplied has not been determined.                               |
+-----------------------------------+----------------+-------------------+-------------------------------------------------------------------------+
| dcterms:alternative               | Literal        |                   | An alternative name for the resource.                                   |
+-----------------------------------+----------------+-------------------+-------------------------------------------------------------------------+

titleInfo - one titleInfo element
---------------------------------

Use Case
^^^^^^^^

An object with a single titleInfo element.

Justification
^^^^^^^^^^^^^
No dispute on what the title is.

Xpath
^^^^^

`mods:titleInfo/mods:title`

Decision
^^^^^^^^
The string `mods:titleInfo/mods:title` can easily translate to the dcterms:title

`Example record from acwiley:280 <https://digital.lib.utk.edu/collections/islandora/object/acwiley%3A280/datastream/MODS>`_

.. code-block:: xml

    <titleInfo>
        <title>Pencil drawn portrait study of woman</title>
    </titleInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:title "Pencil drawn portrait study of woman" .

titleInfo - single titleInfo element having a supplied attribute of yes
-----------------------------------------------------------------------

Use Case
^^^^^^^^

A single titleInfo element having an attribute of supplied="yes".

Justification
^^^^^^^^^^^^^

Samvera uses brackets to wrap title strings in direct mapping examples. According to the `Aggregation Overview document <https://www.njstatelib.org/wp-content/uploads/2017/01/DPLA-Aggregation-Overview.pdf>`_
provided by DPLA, they recommend we "not have brackets or ending periods."


Xpath
^^^^^

`mods:titleInfo[@supplied="yes"]/mods:title`

Decision
^^^^^^^^

In these cases a supplied="yes" may also be present for one titleInfo element. Supplied titles would be used as dcterms:title. Triples will not indicate supplied titles using brackets.

`Example record from roth:5342 <https://digital.lib.utk.edu/collections/islandora/object/roth:5342/datastream/MODS/>`_

.. code-block:: xml

    <titleInfo supplied="yes">
        <title>Coprinus notebook 1</title>
    </titleInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:title "Coprinus notebook 1" .

titleInfo - Multiple titleInfo elements with one having a supplied attribute of yes
-----------------------------------------------------------------------------------

Use Case
^^^^^^^^

An object with a multiple titleInfo elements and one having a attribute of supplied="yes".

Justification
^^^^^^^^^^^^^

For consistency within collections, the best title to display for users is the supplied title.

See **single titleInfo element having a supplied attribute of yes** for justification regarding use of supplied in the transcribed turtle.

Xpath
^^^^^

`mods:titleInfo[@supplied="yes"]/mods:title` AND `mods:titleInfo/mods:title`

Decision
^^^^^^^^

In cases where supplied="yes" are present for one titleInfo element the mods:titleInfo[@supplied]/mods:title value will be used as dcterms:title.

`Example record from swim:162 <https://digital.lib.utk.edu/collections/islandora/object/swim:162/datastream/MODS/>`_

.. code-block:: xml

    <titleInfo>
        <title>Swimming 1969: The University of Tennessee </title>
    </titleInfo>
    <titleInfo supplied="yes">
        <title>University of Tennessee Swimming-Diving media guide, 1969</title>
    </titleInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1>
        dcterms:title "University of Tennessee Swimming-Diving media guide, 1969" ;
        dcterms:alternative "Swimming 1969: The University of Tennessee " .


titleInfo - titleInfo has partName sub-element
----------------------------------------------

Use Case
^^^^^^^^

An object with a single titleInfo element and sub-element of partName.

Justification
^^^^^^^^^^^^^

Consistent with previous UT description practices, we use commas rather periods to indicate
enumeration of an object within a string.

Xpath
^^^^^

`mods:titleInfo/mods:title` AND `mods:titleInfo/mods:partName`

Decision
^^^^^^^^
In these cases the string contained partName will be appended to the <title>. A ','
character will be used as glue when concatenating the strings.

`Example record from sanborn:1194 <https://digital.lib.utk.edu/collections/islandora/object/sanborn:1194/datastream/MODS/>`_

.. code-block:: xml

    <titleInfo>
        <title>Knoxville -- 1917</title>
        <partName>Sheet 56</partName>
    </titleInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:title "Knoxville -- 1917, Sheet 56" .



titleInfo - titleInfo has nonSort sub-element
---------------------------------------------

Use Case
^^^^^^^^

An object with a single titleInfo element and sub-element of nonSort.

Justification
^^^^^^^^^^^^^
We desire clean strings and will not retain nonSorts moving forward.

Xpath
^^^^^

`mods:titleInfo` AND `mods:titleInfo/mods:nonSort`

Decision
^^^^^^^^
The string contained within the nonSort element will be prepended to the title value.

`Example record from volvoices:2890 <https://digital.lib.utk.edu/collections/islandora/object/volvoices:2890/datastream/MODS/>`_

.. code-block:: xml

    <titleInfo>
        <nonSort>The </nonSort>
        <title>Guard at the Mountain Branch of the National Home for Disabled Volunteer Soldiers</title>
    </titleInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:title "The Guard at the Mountain Branch of the National Home for Disabled Volunteer Soldiers" .


titleInfo - Multiple titleInfo elements with one having a type of alternative
-----------------------------------------------------------------------------

Use Case
^^^^^^^^

An object with two titleInfo elements and one having an attribute of type="alternative".

Justification
^^^^^^^^^^^^^
Keeping direct mapping simple.

Xpath
^^^^^

`mods:titleInfo` AND `mods:titleInfo[@type="alternative"]`

Decision
^^^^^^^^

titleInfo elements with @type="alternative" will defined as dcterms:alternative

`Example record from pcard00:100233 <https://digital.lib.utk.edu/collections/islandora/object/pcard00:100233/datastream/MODS/>`_

.. code-block:: xml

    <titleInfo>
        <title>Prussian heroes march</title>
    </titleInfo>
    <titleInfo type="alternative">
        <title>Prussian heroes: Prussen helden march</title>
    </titleInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1>
        dcterms:title "Prussian heroes march" ;
        dcterms:alternative "Prussian heroes: Prussen helden march" .


titleInfo - Multiple titleInfo elements with one having a displayLabel attribute
--------------------------------------------------------------------------------

Use Case
^^^^^^^^

An object with a two titleInfo elements and one having an attribute of displayLabel="some string".

Justification
^^^^^^^^^^^^^

For cleanliness and consistency displayLabels won't be used to describe titles.

Xpath
^^^^^

`mods:titleInfo` AND `mods:titleInfo[@displayLabel="some string"]`

Decision
^^^^^^^^

We will not retain data regarding displayLabel attributes moving forward.

`Example record from womenbball:653 <https://digital.lib.utk.edu/collections/islandora/object/womenbball:653/datastream/MODS/>`_

.. code-block:: xml

    <titleInfo supplied="yes">
        <title>Tennessee Lady Volunteers basketball media guide, 1984-1985</title>
    </titleInfo>
    <titleInfo type="alternative" displayLabel="Cover Title">
        <title>Tennessee Lady Vols 1984-85: reaching for the Summitt of women's basketball</title>
    </titleInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1>
        dcterms:title "Tennessee Lady Volunteers basketball media guide, 1984-1985"  ;
        dcterms:alternative "Tennessee Lady Vols 1984-85: reaching for the Summitt of women's basketball" .


abstract
========

tableOfContents
===============

name
====

originInfo
==========

physicalDescription
===================

digitalOrigin
-------------

Use Case
^^^^^^^^

Currently there are 28,137 records that have a digitalOrigin value. This value is absent from 23,190 records. While present
in the MODS record, these values (we have "born digital", "digitized other analog", and "reformatted digital" in our collections)
are not publicly displayed anywhere. These values communicate the "method by which a resource achieved digital form."

Justification
^^^^^^^^^^^^^

We have decided for a number of reasons that migrating our digitalOrigin values does is not beneficial. As mentioned above,
these values are not currently viewable by users. Arguably, these values will also already be apparent from the technical
metadata and do not need to be captured in the descriptive metadata. In addition, we are unaware of any backend technical
use case for this data at present. While knowing if something is "born digital" might be useful, all of the content within
Digital Collections is curated and meets our technical expectations. A "born digital" label would be more actionable for
resources gathered outside of the Digital Collections creation process. These born digital resources from "the wild" would
likely not be on the same platform as Digital Collections resources.

Xpath
^^^^^

mods:physicalDescription/mods:digitalOrigin

Decision
^^^^^^^^

We have decided to not migrate these values as is justified above. Here's an `example record - voloh:10 <https://digital.lib.utk.edu/collections/islandora/object/voloh%3A10/datastream/MODS/view>`_

.. code-block:: xml

    <digitalOrigin>born digital</digitalOrigin>

note
----

Use Case
^^^^^^^^
Two collections, the Botanical Photography of Alan S. Heilman and the William Derris Film Collection, include <note> elements
within <physicalDescription>. These values are of two types. The majority of the values communicate camera settings for the
Heilman collection, while a smaller number of values share the "Film type" that was used to produce the print that was
digitized. Below is a small sample of these values:

1. Camera setting: 7@50 on 25; with filter
2. 0.18x magnification, 100 Velvia
3. Film type: Kodachrome Transparency
4. zoomA -> 70 [A], Auto f16E100s
5. Film type: GEMounts

These values are somewhat problematic because they do not describe the digitized resource, but instead provide information about
the process that created these resources. This is useful information to know, but isn't tied directly to the resource, making
the inclusion of the values within physicalDescription inaccurate.

Justification
^^^^^^^^^^^^^
Since we do not use mods:physicalDescription/mods:note regularly, it would streamline our data if these values could be
appropriately placed elsewhere. I attempted to match film type values ("GEMounts" and "Kodachrome Transparency") with AAT
terms, but wasn't able to find anything appropriate for "GEMounts." The accuracy of some of this information is questionable
(for instance, GEMounts are likely a brand instead of a film type), but without access to the actual materials during the quarantine, it's
impossible to make an informed judgement on what should be changed. To retain this contextual information that might
prove useful to researchers interested in photographic processes and techniques, it seems best to simply put these values
in a generic note field. If additional attention can be given to these two collections in the future, we can remediate
the metadata following migration with the benefit of having access to the physical materials.

Xpath
^^^^^
mods:physicalDescription/mods:note

Decision
^^^^^^^^
All values will be moved to a generic note field.

`Example record - derris:879 <https://digital.lib.utk.edu/collections/islandora/object/derris%3A879/datastream/MODS/view>`_

.. code-block:: xml

    <physicalDescription>
        <form authority="aat" valueURI="http://vocab.getty.edu/aat/300127478">transparencies</form>
        <digitalOrigin>digitized other analog</digitalOrigin>
        <note>Film type: GEMounts</note>
        <note>Camera setting: 10@50 at 4ft</note>
    </physicalDescription>

.. code-block:: turtle

    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .

    <https://example.org/objects/1>
        skos:note "Film type: GEMounts", "Camera setting: 10@50 at 4ft" .

extent
------

Use Case
^^^^^^^^
The element includes values that indicate time and physical dimensions. Time is consistently shared in hours, minutes
and seconds. Physical dimensions are most consistently represented in inches and feet, but cm are also used for smaller
items that might benefit from a more granular measurement. While this kind of information has historically been included
in MARC records to ensure that books are not larger than the shelf height, extent values can also provide important
contextual information that is relevant to better understanding resources in a digital environment. Particularly in the
case of photography, the dimensions can be used to help determine the type of film.

Justification
^^^^^^^^^^^^^
The working group's shared philosophies were influential in decided on the best property to use for <extent> values. The
Islandora Metadata Interest Group's default mapping suggests using dcterms:extent and using a blank node with a literal as
a RDF value. This group is against using blank nodes when at all possible because they make it more difficult for the
user to consume content. The Samvera mapping uses rdau:extent, which is less than ideal because rdau does not support
content negotiation. This means that the URI provided for the desired property does not allow a user to directly request
RDF. No other more suitable properties could be found for <extent> values. Given this predicament, the working group
decided to use rdau:extent because it is dereferenceable, which a blank node is not. Still, the inability to retrieve
RDF directly will limit users wishing to interact with our data in this way.

Xpath
^^^^^

mods:physicalDescription/mods:extent

Decision
^^^^^^^^
`Example record - knoxgardens:125 <https://digital.lib.utk.edu/collections/islandora/object/knoxgardens%3A125/datastream/MODS/view>`_

.. code-block:: xml

    <extent>3 1/4 x 5 inches</extent>

.. code-block:: turtle

    @prefix rdau: <http://rdaregistry.info/Elements/u/> .

    <https://example.org/objects/1>
        rdau:P60550 "3 1/4 x 5 inches" .

extent - @unit
--------------

Use Case
^^^^^^^^
The Great Smoky Mountains Colloquy collection is the only collection that includes the unit attribute on <extent>. The
collection consists of 34 total records.

Justification
^^^^^^^^^^^^^
It is important for the user to know what the unit of measurement is for a value within the <extent> field. It is also
important for us to share this information consistently. In order to retain the needed information while also conforming
the metadata from this collection with the rest of our records, we propose that the @unit value is added to the extent
string during migration. This would involve simply taking the existing value in <extent> and then adding ' pages' to the
string. Note that all of the resources within the Colloquy collection have more than one page, so the plural form of the
word will always be accurate. See the Decision section of extent above for more explanation of rdau:extent.en.

Xpath
^^^^^

mods:physicalDescription/mods:extent[@unit="pages"]

Decision
^^^^^^^^
`Example record - colloquy:202 <https://digital.lib.utk.edu/collections/islandora/object/colloquy%3A202/datastream/MODS/view>`_

.. code-block:: xml

    <extent unit="pages">4</extent>

.. code-block:: turtle

    @prefix rdau: <http://rdaregistry.info/Elements/u/> .

    <https://example.org/objects/1>
        rdau:P60550 "4 pages" .

form - No URI
-------------

Use Case
^^^^^^^^

At the time of analysis, there were 10,853 records that contained a form term without an associated valueURI attribute.
Through individually assessing the values, it was determined that all of these values do indeed come from the Art and
Architecture Thesaurus (AAT), but without additional remediation the relationship of these values to the controlled
vocabulary is not actionable. In the coming months, work will be done to add the appropriate valueURIs to these records,
but we want to make sure that this work is not a blocker to migration. In order to leverage the capabilities of Linked
Data, we plan to remediate as many of these records as possible while choosing a mapping that allows flexibility in the
value type. Anything values that are not remediated to include URIs before migration can be addressed via SPARQL queries
afterwards.

Justification
^^^^^^^^^^^^^

Form values are important access points that provide more specific information than is provided in higher-level elements
like <typeOfResource>. While these form values do not currently contain valueURI attributes, the strings themselves
are controlled terms that are clean and consistent so we want to bring them over.

Xpath
^^^^^

mods:physicalDescription/mods:form

Decision
^^^^^^^^

We will use edm:hasType instead of dcterms:format in order to accommodate form values without a URI. We need to move all
of the form values over, so using edm:hasType will make sure that we bring every form term regardless of whether it is
defined as a URI or a literal.

Here's an `example record - gamble:1 <https://digital.lib.utk.edu/collections/islandora/object/gamble%3A1/datastream/MODS/view>`_

.. code-block:: xml

    <form>cartoons (humorous images)</form>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/>

    <https://example.org/objects/1>
        edm:hasType "cartoons (humorous images)" .

form - Has URI
--------------

Use Case
^^^^^^^^

The majority of UTK's form values include a valueURI from the Art and Architecture Thesaurus (AAT). These values provide
important access to users by providing physical information about the original resource. Form values are not currently
displayed in DPLA's interface, but `DPLA's MAP 5 <https://drive.google.com/file/d/1fJEWhnYy5Ch7_ef_-V48-FAViA72OieG/view>`_
lists preferred from subtype values that will eventually be implemented. Work has been done to align as many of our form
terms as possible with this preferred list.

Justification
^^^^^^^^^^^^^

Form values are important access points that provide more specific information than is provided in higher-level elements
like <typeOfResource>

Xpath
^^^^^

mods:physicalDescription/mods:form[@valueURI]

Decision
^^^^^^^^

Here's an `example record - ruskin:108 <https://digital.lib.utk.edu/collections/islandora/object/ruskin%3A108/datastream/MODS/view>`_

.. code-block:: xml

    <form authority="http://vocab.getty.edu/aat/300046300">photographs</form>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/>

    <https://example.org/objects/1>
        edm:hasType <http://vocab.getty.edu/aat/300046300> .

form - @type="material"
-----------------------

Use Case
^^^^^^^^
The Archivision collection has a special type attribute so that the list of materials used to create specific buildings
can be faceted. The material types are consistently listed in the same order within the string to make this possible.

Justification
^^^^^^^^^^^^^
In order to attempt to streamline this data to better align with UTK's existing records, all existing terms were compared
with similar terms from the Art and Architecture Thesaurus. The hope was to split the string field on commas and find
controlled terms for each individual value so that these could simply be presented in mods:physicalDescription/mods:form
without the need for a unique type attribute. Analysis showed that a number of values included very specific descriptions
of the material type in parentheses following the broader term. For instance, 'marble (white Carrara and green Prato marble).'
This specificity made it impossible to use the AAT without losing some of the information present in the original records.
Treating these values as part of the abstract will ensure that they display prominently, which wouldn't be the case with
a note value necessarily. To make this read more fluidly, 'Made of ' can be added to the front of the string and an ending
period added ('.').

Xpath
^^^^^

mods:physicalDescription/mods:form[@type="material"]

Decision
^^^^^^^^
`Example record - archvision:8477 <https://digital.lib.utk.edu/collections/islandora/object/archivision%3A8477/datastream/MODS/view>`_

.. code-block:: xml

    <form type="material">granite, tile (pink Vermont granite, Spanish tile)</form>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

        <https://example.org/objects/1> dcterms:abstract "Made of granite, tile (pink Vermont granite, Spanish tile)." .

internetMediaType
-----------------

Use Case
^^^^^^^^
A total of 14,725 records have an <internetMediaType> while this element is not present in 36,602 records. It is used to indicate
the MIME type of the access file for the digitized resource.

Justification
^^^^^^^^^^^^^
We do not need to migrate this information from the descriptive metadata as it will be captured automatically during
file characterization in the new system. We also do not want to move the current values over from the existing metadata
because they often share inaccurate information. Finally, this element is currently present in only

Xpath
^^^^^

mods:physicalDescription/mods:internetMediaType

Decision
^^^^^^^^

Do not migrate.

`Example record - voloh:10 <https://digital.lib.utk.edu/collections/islandora/object/voloh%3A10/datastream/MODS/view>`_

.. code-block:: xml

    <internetMediaType>audio/wav</internetMediaType>

note
====

+-----------------------------------+----------------+-------------------+-------------------------------------------------------------------------+
| Predicate                         | Value Type     | Range (if needed) | Usage Notes                                                             |
+===================================+================+===================+=========================================================================+
| bf:IntendedAudience               | Literal or URI |                   | Use for information that identifies the specific audience or            |
|                                   |                |                   | intellectual level for which the content of the resource is considered  |
|                                   |                |                   | appropriate.                                                            |
+-----------------------------------+----------------+-------------------+-------------------------------------------------------------------------+
| dce:subject                       | Literal or URI |                   | Use for name, topical subjects, and uncontrolled keywords.              |
|                                   |                |                   | Use of a URI from a controlled subject vocabulary is preferred          |
|                                   |                |                   | over a literal value                                                    |
+-----------------------------------+----------------+-------------------+-------------------------------------------------------------------------+
| opaque:sheetmusic_instrumentation | Literal or URI |                   | Use for sheet music, a listing of the performing forces                 |
|                                   |                |                   | called for by a particular piece of sheet music, including              |
|                                   |                |                   | both voices and external instruments.                                   |
+-----------------------------------+----------------+-------------------+-------------------------------------------------------------------------+
| opaque:sheetmusic_firstLine       | Literal or URI |                   | Use for sheet music, entering a direct transcription of the             |
|                                   |                |                   | first line of lyrics appearing in the song.                             |
+-----------------------------------+----------------+-------------------+-------------------------------------------------------------------------+
| skos:note                         | Literal        |                   | Use for the note value.                                                 |
+-----------------------------------+----------------+-------------------+-------------------------------------------------------------------------+


note - Just a note
------------------

Use Case
^^^^^^^^

Usually, a note is just a note.  The xpath section below lists when this is the case. In the case that an xpath has a
specific attribute and value, prepend the value to the text node.

Justification
^^^^^^^^^^^^^

The Samvera community attempts to keep some of the granularity of MODS by prepending the text value of the attribute
to the text node when one exists.  When one doesn't, simply take the text node.

In Bibframe, there was no attempt to convert the 562 MARC field.  For this reason, "handwritten" documents are just
regular notes.

Xpath
^^^^^

`mods:note` OR `mods:note[@type="handwritten"]` OR `mods:note[@type="provenance"]` OR `mods:note[@displayLabel="Attribution"]`
OR `mods:note[@displayLabel="use and reproduction"]` OR `mods:note[@displayLabel="Local Rights"]`

Decision
^^^^^^^^

`Example record - bakerav:291 <https://digital.lib.utk.edu/collections/islandora/object/bakerav:291/datastream/MODS>`_

.. code-block:: xml

    <note>
        A_0:51:21 / B_0:59:44
    </note>
    <note>
        (Original, for: Mrs. Dirksen, Compliments: Tony Janak)
    </note>
    <note>
        No issues.
    </note>

.. code-block:: turtle

    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .

    <https://example.org/objects/1>
        skos:note "A_0:51:21 / B_0:59:44", "(Original, for: Mrs. Dirksen, Compliments: Tony Janak)", "No issues." .


note - Instrumentation
----------------------

Use Case
^^^^^^^^

When a note has a `@type = "Instrumenation"`, it is not a general note. Instead, this element is a listing of the
performing forces called for by a particular piece of music.

Justification
^^^^^^^^^^^^^

We reviewed several bibliographic and music ontologies including the Music Ontology, the Internet of Music Thingz, and
MusicBrainz, but none seemed to have a predicate to represent this idea. We did notice that Opaque Namespace by
Oregon Digital did have a matching predicate.  In the Samvera community, not only is this ontology used, but occasionally
the community has suggested new predicates to be created within Opaque Namespaces.

Xpath
^^^^^

`mods:note[@type="Instrumentation"]`

Decision
^^^^^^^^

`Example record from vanvactor:15773 <https://digital.lib.utk.edu/collections/islandora/object/vanvactor:15773/datastream/MODS>`_

.. code-block:: xml

    <note type="instrumentation">
        For soprano, mezzo-soprano, contralto, 2 flutes, 2 oboes, 2 clarinets, 2 bassoons, 2 horns, 2 trumpets, timpani, 2 violins, viola, cello, and double bass.
    </note>


.. code-block:: turtle

    @prefix opaque: <http://opaquenamespace.org/​ns/> .

    <https://example.org/objects/1>
        opaque:sheetmusic_instrumentation "For soprano, mezzo-soprano, contralto, 2 flutes, 2 oboes, 2 clarinets, 2 bassoons, 2 horns, 2 trumpets, timpani, 2 violins, viola, cello, and double bass." .


note - First Line
-----------------

Use Case
^^^^^^^^

When a note has a `@type = "First line"` or `@type = "first line"`, it is not a general note. Instead, this element is
a direct transcription of the first line of lyrics appearing in a song.

Justification
^^^^^^^^^^^^^

We reviewed several bibliographic and music ontologies including the Music Ontology, the Internet of Music Thingz, and
MusicBrainz, but none seemed to have a predicate to represent this idea. We did notice that Opaque Namespace by
Oregon Digital did have a matching predicate.  In the Samvera community, not only is this ontology used, but occasionally
the community has suggested new predicates to be created within Opaque Namespaces.

Xpath
^^^^^

`mods:note[@type="First line"]` or `mods:note[@type="first line"]`

Decision
^^^^^^^^

`Example record from vanvactor:15773 <https://digital.lib.utk.edu/collections/islandora/object/vanvactor:15773/datastream/MODS>`_

.. code-block:: xml

    <note type="First line">
        Ojitos de pena carita de luna, lloraba la niña sin causa ninguna.
    </note>


.. code-block:: turtle

    @prefix opaque: <http://opaquenamespace.org/​ns/> .

    <https://example.org/objects/1>
        opaque:sheetmusic_firstLine "Ojitos de pena carita de luna, lloraba la niña sin causa ninguna." ..


note - Target audience
----------------------

Use Case
^^^^^^^^

If a note has a displayLabel attribute with the value of "Grade level", it refers to the target audience of the resource.

Justification
^^^^^^^^^^^^^

The MARC 521 field should be mapped to the Bibframe intended audience field. The field is defined as information that
identifies the specific audience or intellectual level for which the content of the resource is considered appropriate.

Xpath
^^^^^

`mods:note[@displayLabel="Grade level"]`

Decision
^^^^^^^^

`Example record from arrowmont:9 <https://digital.lib.utk.edu/collections/islandora/object/arrowmont:9/datastream/MODS>`_

.. code-block:: xml

    <note displayLabel="Grade level">
        Second Grade
    </note>

.. code-block:: turtle

    @prefix bf: <http://id.loc.gov/ontologies/bibframe/> .

    <https://example.org/objects/1>
        bf:IntendedAudience "Second Grade" .


note - Uncontrolled keyword or Tag
----------------------------------

Use Case
^^^^^^^^

Some of our notes actually refer to uncontrolled keywords or tags.

Justification
^^^^^^^^^^^^^

While not preferred, Samvera treats these as dcterms:subjects with a literal rather than an a URI.

Xpath
^^^^^

`mods:note[@displayLabel="Tags"]`

Decision
^^^^^^^^

.. code-block:: xml

    <note displayLabel="Tags">
        (1955-1962) Bowden Wyatt
    </note>

.. code-block:: turtle

    @prefix dce: <http://purl.org/dc/elements/1.1/> .

    <https://example.org/objects/1>
        dce:subject "(1955 - 1962) Bowden Wyatt" .


note - DPN Deposits and Other Things to Ignore
----------------------------------------------

Use Case
^^^^^^^^

We have several notes that we do not need to migrate.

Justification
^^^^^^^^^^^^^

The data here is no longer important.

Xpath
^^^^^

`mods:note[@displayLabel="DPN"]` OR `mods:note[text()=""]` OR `mods:note[@displayLabel="Intermediate provider"]` OR
`mods:note[@displayLabel="Intermediate Provider"]` OR `mods:note[@displayLabel="Transcribed from Original Collection"]`
OR `mods:note[@displayLabel="Project Part"]`

Decision
^^^^^^^^

`Example record from heilman:1000 <https://digital.lib.utk.edu/collections/islandora/object/heilman:1000/datastream/MODS>`_

.. code-block:: xml

    <note displayLabel="dpn">
        This object was added to the Digital Preservation Network in November 2016.
    </note>

**Do not migrate!**


subject
=======

genre
=====

language
========

typeOfResource
==============

classification
==============

relateItem
==========

location
========

recordInfo
==========

accessCondition
===============

accessCondition - Rights Statements and Creative Commons Licenses
-----------------------------------------------------------------

Use Case
^^^^^^^^

When one of the twelve standardized rights statements from `https://righsstatements.org <https://righsstatements.org>`_
or one of the CC licenses is present, the value should be mapped to edm:rights and have a value type of URI.

Justification
^^^^^^^^^^^^^

DPLA maps both CC licenses and Rights Statements to edm:rights. So does Samvera. Presently only the heilman collection includes
a CC license

Xpath
^^^^^

mods:accessCondition[@xlink:href]

Decision
^^^^^^^^

`Example record for Rights Statements <https://digital.lib.utk.edu/collections/islandora/object/knoxgardens%3A115/datastream/MODS>`_

.. code-block:: xml

    <accessCondition type="use and reproduction"
                    xlink:href="http://rightsstatements.org/vocab/CNE/1.0/">
        Copyright Not Evaluated
    </accessCondition>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/> .


        <https://example.org/objects/1> edm:rights <http://rightsstatements.org/vocab/CNE/1.0/> .


`Example record for CC license <https://digital.lib.utk.edu/collections/islandora/object/heilman%3A1010/datastream/MODS/view>`_

.. code-block:: xml

    <accessCondition type="use and reproduction"
                    xlink:href="https://creativecommons.org/licenses/by-nc-nd/3.0/">
        Attribution-NonCommercial-NoDerivs 3.0 Unported (CC BY-NC-ND 3.0)
    </accessCondition>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/> .


        <https://example.org/objects/1> edm:rights <https://creativecommons.org/licenses/by-nc-nd/3.0/> .

accessCondition - Restrictions on Access
----------------------------------------

Use case
^^^^^^^^

The Howard Baker Audiovisual Collection includes 46 items that are "In Copyright" and therefore have restricted access to
avoid any potential copyright conflicts. Only on campus access is provided to the actual recordings, though the metadata
records are accessible from anywhere. Having the metadata accessible makes it so that anyone can discover these materials
and decide for themselves if it is worth a trip into campus. Some of the recordings had some deterioration and were therefore
digitized as a preservation measure. Having digitized copies also made providing on site access easier. In order to make
sure that users are aware of the on campus only restriction, a note needed to be added to the metadata. When off campus
users visit the metadata, this note makes it clear why they cannot access the recording.

Justification
^^^^^^^^^^^^^

As the value present in the current accessCondition node is not associated with a controlled vocabulary and simply needs to
be displayed to the user within the record, there is no reason to connect it with other accessCondition values. A note is
sufficient for this use case.

Xpath
^^^^^

mods:accessCondition[@type="restriction on access"]

Decision
^^^^^^^^

`Example record - bakerav:10 <https://digital.lib.utk.edu/collections/islandora/object/bakerav%3A10/datastream/MODS/view>`_

.. code-block:: xml

    <accessCondition type="restriction on access">
        This item can only be accessed on the University of Tennessee (Knoxville) campus
    </accessCondition>

.. code-block:: turtle

    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .

        <https://example.org/objects/1> skos:note 'This item can only be accessed on the University of Tennessee (Knoxville) campus' .

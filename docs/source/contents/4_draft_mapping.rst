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

+------------------------------+--------------+--------------------------------------------+
| Vocabulary Name              | Prefix       | URI                                        |
+==============================+==============+============================================+
| BIBFRAME                     | bf           | http://id.loc.gov/ontologies/bibframe/     |
+------------------------------+--------------+--------------------------------------------+
| Classification Schemes       | classSchemes | http://id.loc.gov/vocabulary/classSchemes/ |
+------------------------------+--------------+--------------------------------------------+
| DBpedia Ontology             | dbo          | http://dbpedia.org/ontology/               |
+------------------------------+--------------+--------------------------------------------+
| DCMI Metadata Terms          | dcterms      | http://purl.org/dc/terms/                  |
+------------------------------+--------------+--------------------------------------------+
| Dublin Core Metadata Element | dce          | http://purl.org/dc/elements/1.1/           |
| Set, Version 1.1             |              |                                            |
+------------------------------+--------------+--------------------------------------------+
| Europeana Data Model         | edm          | http://www.europeana.eu/schemas/edm/       |
+------------------------------+--------------+--------------------------------------------+
| MARC Code List for Relators  | relators     | http://id.loc.gov/vocabulary/relators/     |
+------------------------------+--------------+--------------------------------------------+
| Opaque Namespace             | opaque       | http://opaquenamespace.org/ns/             |
+------------------------------+--------------+--------------------------------------------+
| RDA Unconstrained            | rdau         | http://www.rdaregistry.info/Elements/u/    |
+------------------------------+--------------+--------------------------------------------+
| SKOS Simple Knowledge        | skos         | http://www.w3.org/2004/02/skos/core#       |
| Organization System          |              |                                            |
+------------------------------+--------------+--------------------------------------------+
| Standard Identifier Scheme   | identifiers  | http://id.loc.gov/vocabulary/identifiers/  |
+------------------------------+--------------+--------------------------------------------+

*******
Mapping
*******

identifier
==========

+------------------------+------------+---------------------------------------------------------------------------------------+
| Predicate              | Value Type |  Usage Notes                                                                          |
+========================+============+=======================================================================================+
| dbo:isbn               | Literal    | Use for identifiers with type="isbn"                                                  |
+------------------------+------------+---------------------------------------------------------------------------------------+
| dbo:issn               | Literal    | Use for identifiers with type="issn"                                                  |
+------------------------+------------+---------------------------------------------------------------------------------------+
| dbo:oclc               | Literal    | Use for identifiers with type="oclc"                                                  |
+------------------------+------------+---------------------------------------------------------------------------------------+
| identifiers:local      | Literal    | Use for the majority of identifiers (all those that do not fit into other categories) |
+------------------------+------------+---------------------------------------------------------------------------------------+
| opaque:accessionNumber | Literal    | Use for identifiers with type="acquisition"                                           |
+------------------------+------------+---------------------------------------------------------------------------------------+

Local Identifiers
-----------------

Use Case
^^^^^^^^

This is the catch-all category for identifiers that is important to keep but that do not need to be separated into individual
categories for discovery. UTK's adminDB values as well as a range of different locally created identifiers are present.
A great deal of the values were initially created by Special Collections in finding aids - for instance identifiers with a
type attribute of "slide number", "archival number", "cw", and "film number". If an identifier type attribute of "opac" is
present, this means that the resource also has a full MARC record present in the Alma catalog. The strings values for opac
identifiers are fourteen to sixteen digits, with the last five digits always being ‘02311.' The PID value is the main
identifier within the Islandora7 platform and is present in the records of collections that have undergone remediation.
Collections that were migrated from Omeka to Islandora7 often include identifiers with a type of "spc." These collections
include the Anna Catherine Wiley Sketches, Images of East Tennessee, and Photographs of the Ruskin Cooperative Association.

Justification
^^^^^^^^^^^^^

These values are being kept because they may be helpful to users in finding specific materials. For instance, while :code:`@type="pid"`
identifiers will no longer be the primary identifiers on UTK's next digital collections platform, they could be used to
identify cited resources that have broken links. Many of the identifiers associated with Special Collections allow users
to see how the same resource might be referenced within finding aids. Have :code:`@type="opac"` identifiers helps staff at UTK
know immediately whether a resource has a MARC record, which could prove useful if descriptive metadata is needed in this
form. Overall, little effort needs to be exerted to keep all of these values and they all have the potential to be helpful
in the future.

XPath
^^^^^

:code:`identifier[@type="Vendor ID"]` OR

:code:`identifier[@type="archival number"]` OR

:code:`identifier[@type="catalog"]` OR

:code:`identifier[@type="circular"]` OR

:code:`identifier[@type="cw"]` OR

:code:`identifier[@type="document ID"]` OR

:code:`identifier[@type="documentID"]` OR

:code:`identifier[@type="filename"]` OR

:code:`identifier[@type="film number"]` OR

:code:`identifier[@type="legacy"]` OR

:code:`identifier[@type="local"]` OR

:code:`identifier[@type="original ID"]` OR

:code:`identifier[@type="photograph number"]` OR

:code:`identifier[@type="slide number"]` OR

:code:`identifier[@type="pid"]` OR

:code:`identifier[@type="opac"]` OR

:code:`identifier[@type="spc"]`

Decision
^^^^^^^^

`Example of a record with a PID identifier - egypt:8 <https://digital.lib.utk.edu/collections/islandora/object/egypt:8/datastream/MODS>`_

.. code-block:: xml

    <identifier type="pid">egypt:8</identifier>

.. code-block:: turtle

    @prefix identifiers: <http://id.loc.gov/vocabulary/identifiers/> .
    <https://example.org/objects/1>
        identifiers:local "egypt:8" .

`Exception that requires pre-pending a string - agrutesc: <https://digital.lib.utk.edu/collections/islandora/object/agrutesc:2130/datastream/MODS>`_

.. code-block:: xml

    <identifier type="circular">79</identifier>

.. code-block:: turtle

    @prefix identifiers: <http://id.loc.gov/vocabulary/identifiers/> .

    <https://example.org/objects/1>
        identifiers:local "Circular 79" .

Acquisition Identifier
----------------------

Use Case
^^^^^^^^

Several of UTK's collections come from institutions outside the library and include identifiers assigned by those
institutions. The McClung Museum of Natural History and Culture on campus is one of these institutions. In the `Nineteenth
and Early Twentieth Century Images of Egypt collection <https://digital.lib.utk.edu/collections/islandora/object/collections%3Aegypt>`_ shared by McClung, traditional museum acquisition numbers
consisting of the year three numbers separated by periods (year.acquisition group.item) are present.

Justification
^^^^^^^^^^^^^

Both OpaqueNamespace and `CIDOC-CRM <http://www.cidoc-crm.org/>`_ properties were considered for mapping these values.
Both `opaque:accessionNumber <http://opaquenamespace.org/ns/cco_accessionNumber>`_ and `crm:E8 (Acquisition) <http://www.cidoc-crm.org/cidoc-crm/E8_Acquisition>`_ were defined
appropriately for UTK's use cases. Because CIDOC-CRM is particularly used in a museum context, we decided to use
`opaque:accessionNumber` as it is arguably more flexible. This allows us to use the same property for accession numbers
from a wide variety of institutions. Both properties supported content negotiation.

XPath
^^^^^

:code:`identifier[@type="acquisition"]`

Decision
^^^^^^^^

The property `opaque:accessionNumber` was selected.

`Example record - egypt:10 <https://digital.lib.utk.edu/collections/islandora/object/egypt%3A10/datastream/MODS/view>`_

.. code-block:: xml

<identifier type="acquisition">1996.10.1</identifier>

.. code-block:: turtle

    @prefix opaque: <http://opaquenamespace.org/ns/> .

    <https://example.org/objects/1>
            opaque:accessionNumber "1996.10.1" .

OCLC numbers
------------

Use Case
^^^^^^^^

Records from the Tennessee Documentary History collection include OCLC identifiers. These values can be used to identify
corresponding records in Worldcat.

Justification
^^^^^^^^^^^^^

OCLC identifiers could be useful if these materials are ever shared with HathiTrust, as this value is a requirement for
submission. Only one property, `dbo:oclc`, was identified to use and it aligns with our philosophy guidelines.

XPath
^^^^^

:code:`identifier[@type="oclc"]`

Decision
^^^^^^^^

`Example record - tdh:989 <https://digital.lib.utk.edu/collections/islandora/object/tdh:989/datastream/MODS>`_

.. code-block:: xml

    <identifier type="oclc">44394278</identifier>

.. code-block:: turtle

    @prefix dbo: <http://dbpedia.org/ontology/> .

    <https://example.org/objects/1>
        dbo:oclc "44394278" .

ISSNs
-----

Use Case
^^^^^^^^

Approximately 10% of our records describe periodicals. Effort has been invested in establishing official e-ISSNs for several
titles through the Library of Congress. These titles include:

1. Agricultural & Home Economics News
2. Agricultural & Home Economics Packet
3. Agricultural News
4. Alumnus
5. Circular
6. Farm News
7. Phoenix
8. Special Circular
9. Tennessee Farm and Home News
10. Tennessee Farm and Home Science
11. Tennessee Farm News
12. Torchbearer

* Note: Some resources within the Children's Defense Fund collection have both a ISSN and a ISBN.

More information on assigning an e-ISSN can be found here - https://www.loc.gov/issn/basics/basics-brochure-eserials.html.

As these identifiers have meaning outside of the context of UTK and might be used by patrons
in a search to find these materials, it is important that we continue to support a unique field for these values. In addition,
having a persistent link for resources with a particular ISSN is essential to the Libraries' HathiTrust submission
records. A title-level MARC XML record with a link to all issues with the same ISSN is shared for this purpose.

Justification
^^^^^^^^^^^^^

Properties for ISSN values are established in DBpedia and the Standard Identifiers Scheme. Both follow our philosophy
guidelines and could be used to accurately represent the ISSN values. Ultimately we decided to use DBpedia because it is
a widely used core ontology whereas the Standard Identifiers Scheme is more library specific.

XPath
^^^^^

:code:`identifier[@type="issn"]`

Decision
^^^^^^^^

`Example record - agrutesc:2130 <https://digital.lib.utk.edu/collections/islandora/object/agrutesc:2130/datastream/MODS>`_

.. code-block:: xml

    <identifier type="issn">2687-7325</identifier>

.. code-block:: turtle

    @prefix dbo: <http://dbpedia.org/ontology/> .

    <https://example.org/objects/1>
        dbo:issn "2687-7325" .

ISBNs
-----

Use Case
^^^^^^^^

International Standard Book Numbers are present as identifier values in the Children's Defense Fund collection. As these
identifiers have meaning outside of the context of UTK and might be used by patrons in a search to find these materials,
it is important that we continue to support a unique field for these values.

Justification
^^^^^^^^^^^^^

Properties for ISBN values are established in DBpedia and the Standard Identifiers Scheme. Because we give preference to
core ontologies rather than library specific ones, we selected `dbo:issn`.

XPath
^^^^^

:code:`identifier[@type="isbn"]`

Decision
^^^^^^^^

`Example record - cdf:6909 <https://digital.lib.utk.edu/collections/islandora/object/cdf:6909/datastream/MODS>`_

.. code-block:: xml

    <identifier type="isbn">0938008501</identifier>

.. code-block:: turtle

    @prefix dbo: <http://dbpedia.org/ontology/> .

    <https://example.org/objects/1>
        dbo:issn "0938008501" .

titleInfo
=========

+-----------------------------------+----------------+-------------------------------------------------------------------------+
| Predicate                         | Value Type     | Usage Notes                                                             |
+===================================+================+=========================================================================+
| dcterms:title                     | Literal        | A name given to the resource. If multiple titleInfo elements are        |
|                                   |                | present, supplied title is assumed to the title. Using of []            |
|                                   |                | to note supplied has not been determined.                               |
+-----------------------------------+----------------+-------------------------------------------------------------------------+
| dcterms:alternative               | Literal        | An alternative name for the resource.                                   |
+-----------------------------------+----------------+-------------------------------------------------------------------------+

titleInfo - one titleInfo element
---------------------------------

Use Case
^^^^^^^^

An object with a single :code:`titleInfo` element.

Justification
^^^^^^^^^^^^^
No dispute on what the title is.

XPath
^^^^^

:code:`titleInfo/title`

Decision
^^^^^^^^
The string :code:`titleInfo/title` can easily translate to the `dcterms:title` property.

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

A single :code:`titleInfo` element having an attribute of :code:`supplied="yes"`.

Justification
^^^^^^^^^^^^^

Samvera uses brackets to wrap title strings in direct mapping examples. According to the `Aggregation Overview document <https://www.njstatelib.org/wp-content/uploads/2017/01/DPLA-Aggregation-Overview.pdf>`_
provided by DPLA, they recommend we "not have brackets or ending periods."


XPath
^^^^^

:code:`titleInfo[@supplied="yes"]/title`

Decision
^^^^^^^^

In these cases a :code:`supplied="yes"` may also be present for one :code:`titleInfo` element. Supplied titles would be used as `dcterms:title`. Triples will not indicate supplied titles using brackets.

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

An object with a multiple :code:`titleInfo` elements and one having a attribute of :code:`supplied="yes"`.

Justification
^^^^^^^^^^^^^

For consistency within collections, the best title to display for users is the supplied title.

See **single titleInfo element having a supplied attribute of yes** for justification regarding use of supplied in the transcribed turtle.

XPath
^^^^^

:code:`titleInfo[@supplied="yes"]/title` AND

:code:`titleInfo/title`

Decision
^^^^^^^^

In cases where :code:`supplied="yes"` are present for one :code:`titleInfo` element the :code:`titleInfo[@supplied]/title` value will be used as `dcterms:title`.

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

An object with a single :code:`titleInfo` element and sub-element of :code:`partName`.

Justification
^^^^^^^^^^^^^

Consistent with previous UT description practices, we use commas rather periods to indicate
enumeration of an object within a string.

XPath
^^^^^

:code:`titleInfo/title` AND 

:code:`titleInfo/partName`

Decision
^^^^^^^^

In these cases the string contained in :code:`partName` will be appended to the :code:`title`. A ','
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

An object with a single :code:`titleInfo` element and sub-element of :code:`nonSort`.

Justification
^^^^^^^^^^^^^

We desire clean strings and will not retain :code:`nonSort` elements moving forward.

XPath
^^^^^

:code:`titleInfo` AND 

:code:`titleInfo/nonSort`

Decision
^^^^^^^^

The string contained within the :code:`nonSort` element will be prepended to the :code:`title` value.

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

An object with two :code:`titleInfo` elements and one having an attribute of :code:`type="alternative"`.

Justification
^^^^^^^^^^^^^

Keeping direct mapping simple.

XPath
^^^^^

:code:`titleInfo` AND 

:code:`titleInfo[@type="alternative"]`

Decision
^^^^^^^^

:code:`titleInfo` elements with :code:`@type="alternative"` will defined as `dcterms:alternative`.

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

An object with a two :code:`titleInfo` elements and one having an attribute of :code:`displayLabel="some string"`.

Justification
^^^^^^^^^^^^^

For cleanliness and consistency :code:`displayLabel`\ s won't be used to describe titles.

XPath
^^^^^

:code:`titleInfo` AND 

:code:`titleInfo[@displayLabel="some string"]`

Decision
^^^^^^^^

We will not retain data regarding :code:`displayLabel` attributes moving forward.

`Example record from womenbball:653 <https://digital.lib.utk.edu/collections/islandora/object/womenbball:653/datastream/MODS/>`_

.. code-block:: xml

    <titleInfo supplied="yes">
        <title>Tennessee Lady Volunteers basketball media guide, 1984-1985</title>
    </titleInfo>
    <titleInfo type="alternative" displayLabel="Cover Title">
        <title>Tennessee Lady Vols 1984-85: reaching for the Summitt of women's basketball</title>
    </titleInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1>
        dcterms:title "Tennessee Lady Volunteers basketball media guide, 1984-1985"  ;
        dcterms:alternative "Tennessee Lady Vols 1984-85: reaching for the Summitt of women's basketball" .


abstract
========

+------------------+------------+-----------------------------------------------------+
| Predicate        | Value Type | Usage Notes                                         |
+==================+============+=====================================================+
| dcterms:abstract | Literal    | Use for all mods:abstracts that are not blank nodes |
+------------------+------------+-----------------------------------------------------+

Abstracts that are not Blank Nodes
----------------------------------

Use Case
^^^^^^^^

If a record has an :code:`abstract` or many :code:`abstract`\ s, they will each be mapped to `dcterms:abstract` as long as the :code:`abstract`
does not have an empty text node.

Justification
^^^^^^^^^^^^^

Regardless of the number, the value has the same semantic relationship to the object as it did in MODS.

XPath
^^^^^

:code:`abstract[text()]`

Decision
^^^^^^^^

If it has one :code:`abstract` like `gamble:124 <https://digital.lib.utk.edu/collections/islandora/object/gamble%3A124/datastream/MODS>`_, map to `dcterms:abstract`.

.. code-block:: xml

    <abstract>
        Prosecutor John Keker gives his closing statement to the jury, explaining Col. John North's involvement in the Iran-Contra affair even though the majority of his statement is censored due to classified information.
    </abstract>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:abstract "Prosecutor John Keker gives his closing statement to the jury, explaining Col. John North's involvement in the Iran-Contra affair even though the majority of his statement is censored due to classified information." .

If it has more than one :code:`abstract` like `1001:1 <https://digital.lib.utk.edu/collections/islandora/object/1001%3A1/datastream/MODS>`_,
we will still map to `dcterms:abstract`.

.. code-block:: xml

    <abstract>
        Postcard with handwritten note sent from Knoxville to Miss Virginia Bogart, Loudon, Tennessee on March 2, 1944 for a postage of 1 cent.
    </abstract>
    <abstract>
        The hardwood forest of America, and probably of the entire world, originated in the Great Smoky Mountains, where remains the nation's largest body of virgin hardwood forest, and the world's greatest variety of trees, flowering shrubs and wild flowers.
    </abstract>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:abstract "Postcard with handwritten note sent from Knoxville to Miss Virginia Bogart, Loudon, Tennessee on March 2, 1944 for a postage of 1 cent.", "The hardwood forest of America, and probably of the entire world, originated in the Great Smoky Mountains, where remains the nation's largest body of virgin hardwood forest, and the world's greatest variety of trees, flowering shrubs and wild flowers." .

Blank Abstracts
---------------

Use Case
^^^^^^^^

We have a fair number of records with empty :code:`abstract`\ s.  When an :code:`abstract` is an empty node, don't map it.

Justification
^^^^^^^^^^^^^

The value of the text node has no semantic meaning or value.

XPaths
^^^^^^

:code:`abstract[string()=""]`

Decision
^^^^^^^^

Don't map!

tableOfContents
===============

Use Case
--------

The following collections include :code:`tableOfContents` - David Van Vactor Music Collection, Tennessee Farm and Home Science,
The Arrow of Pi Beta Phi. There are a total of 455 unique values. This element contains the names of individually titled
parts that make up the larger resource. It is used to provide more detailed information on the content of a resource in
a non-structured way. Note that punctuation separating part titles varies depending on the string values being separated.
The following punctuation is present in UTK's :code:`tableOfContents` elements: " -- ", " - ", and ";".

Justification
-------------

This information aides keyword discovery by adding more text to the record and providing users with a listing of parts
within the larger resource.

XPath
-----

:code:`tableOfContents`

Decision
--------

Below are examples showing the punctuation variations present in this element's values.

`Example record with ";" as separators - arrow:305 <https://digital.lib.utk.edu/collections/islandora/object/arrow%3A305/datastream/MODS/view>`_.

.. code-block:: xml

    <tableOfContents>Library Fund Honors Marian; Noted Craftsman Lauds Arrowmont; Gatlinburg Residents Enjoy Craft Courses;
    Tennessee Gammas Honor Prof. Heard</tableOfContents>

`Example record with "-" as separators - agrtfhs:2119 <https://digital.lib.utk.edu/collections/islandora/object/agrtfhs%3A2119/datastream/MODS/view>`_.

.. code-block:: xml

    <tableOfContents>Snap beans: machine vs. hand harvest - New bulletins - Protein with high silage rations -- dairy
     - Pepper yields and fertility, plant spacing - Stripping vs. spindle picking of 4 cottons - Personnel changes -
     Soybean irrigation - Alfalfa crown rot - Bedding for better cotton stands - Controlling bagworms -
     Nitrogen on shade trees</tableOfContents>

`Example record with " -- " as separators - vanvactor:15772 <https://digital.lib.utk.edu/collections/islandora/object/vanvactor%3A15772/datastream/MODS/view>`_.

.. code-block:: xml

    <tableOfContents>Preface -- David Van Vactor: life and works -- David Van Vactor: catalog of manuscripts --
    Catalog of books, scores, and manuscripts in Special Collections -- Books and scores in the George F. DeVine Music
    Library -- Sound recordings, 1942-1979</tableOfContents>

All values within :code:`tableOfContents` will be mapped to RDF in the same way. Below is a representation of arrow:305.

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1>
        dcterms:tableOfContents "Library Fund Honors Marian; Noted Craftsman Lauds Arrowmont; Gatlinburg Residents Enjoy Craft Courses; Tennessee Gammas Honor Prof. Heard" .

name
====

Namespaces
----------

+-----------------+-----------------------+----------------------------------------------------------------+
| Predicate       | Value Type            | Usage Notes                                                    |
+=================+=======================+================================================================+
| relators:[term] | URI or String Literal | Use with a role from MARC Code List of Relators role terms.    |
|                 |                       | Value is either text or URI from acontrolled vocabulary (like  |
|                 |                       | Library of CongressName Authority File).                       |
+-----------------+-----------------------+----------------------------------------------------------------+

Leverage Marc Relators for RDF Property Value and Relationship to the Digital Object
------------------------------------------------------------------------------------

Use Case
^^^^^^^^

For all instances of :code:`name`, leverage the marcrelator value found in its :code:`role/roleTerm` for
associating the name with the digital object.

A lookup table is included as an appendix to help with this.

If the :code:`name` has a :code:`valueURI` attribute, use it for the object of the triple.  If it does not, use
the text value of :code:`name/namePart`.

Justification
^^^^^^^^^^^^^

All instances of :code:`name` have a :code:`role/roleTerm` that can be leveraged to determine the name's
relationship with the digital object.  In some cases, there is a :code:`roleTerm/@valueURI`, but this is not always
the case.

XPaths
^^^^^^

:code:`name/namePart` OR

:code:`name[@valueURI!=""]`

Decisions
^^^^^^^^^

When you have a :code:`name` with a :code:`valueURI` attribute like `harp:1 <https://digital.lib.utk.edu/collections/islandora/object/harp%3A1/datastream/MODS>`_:

.. code-block:: xml
    :caption: Example XML record from `tdh:8803 MODS <https://digital.lib.utk.edu/collections/islandora/object/tdh%3A8803/datastream/MODS/>`_
    :name: Example XML record from `tdh:8803 MODS <https://digital.lib.utk.edu/collections/islandora/object/tdh%3A8803/datastream/MODS/>`_

    <name valueURI="http://id.loc.gov/authorities/names/n2017180154">
        <namePart>White, Hugh Lawson, 1773-1840</namePart>
        <role>
            <roleTerm authority="marcrelator" valueURI="http://id.loc.gov/vocabulary/relators/crp">
                Correspondent
            </roleTerm>
        </role>
    </name>

Leverage the :code:`valueURI` and make it the object of the triple:

.. code-block:: turtle
    :caption: Resulting RDF `from tdh:8803 MODS <https://digital.lib.utk.edu/collections/islandora/object/tdh%3A8803/datastream/MODS/>`_
    :name: Resulting RDF `from tdh:8803 MODS <https://digital.lib.utk.edu/collections/islandora/object/tdh%3A8803/datastream/MODS/>`_

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1>
        relators:crp <http://id.loc.gov/authorities/names/n2017180154> .

When there is no :code:`name/@valueURI`, use the string literal from :code:`name/namePart`:

.. code-block:: xml
    :caption: XML with Name missing a valueURI
    :name: XML with Name missing a valueURI

    <name type="personal">
        <namePart>Daniel, Charles R. (Charlie), Jr., 1930-</namePart>
        <role>
            <roleTerm type="text" authority="marcrelator" valueURI=" http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
    </name>

.. code-block:: turtle
    :caption: Resulting turtle for Name missing a valueURI
    :name: Resulting turtle for Name missing a valueURI

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1>
        relators:cre "Daniel, Charles R. (Charlie), Jr., 1930-" .

If there is a :code:`name/@valueURI` but it's empty, use the string literal instead:

.. code-block:: xml
    :caption: Example XML from `volvoices:2495 MODS <https://digital.lib.utk.edu/collections/islandora/object/volvoices:2495/datastream/MODS>`_
    :name: Example XML from `volvoices:2495 MODS <https://digital.lib.utk.edu/collections/islandora/object/volvoices:2495/datastream/MODS>`_

    <name authority="naf" type="corporate" valueURI="">
        <namePart>Bemis Bro. Bag Company</namePart>
        <role>
            <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/asn">Associated name</roleTerm>
        </role>
    </name>

.. code-block:: turtle
    :caption: Resulting turtle from `volvoices:2495 <https://digital.lib.utk.edu/collections/islandora/object/volvoices:2495/datastream/MODS>`_
    :name: Resulting turtle from `volvoices:2495 <https://digital.lib.utk.edu/collections/islandora/object/volvoices:2495/datastream/MODS>`_

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1>
        relators:asn "Bemis Bro. Bag Company" .

Names with Multiple Role Terms
------------------------------

Use Case
^^^^^^^^

Occasionally, a :code:`name` will have multiple roles.  When this happens, keep them all.

Justification
^^^^^^^^^^^^^

It's important that we keep the relationship between people and our digital object.

XPaths
^^^^^^

:code:`count(name/role)>1`

Decision
^^^^^^^^

.. code-block:: xml
    :caption: `Multi-role name from harp:1 MODS record <https://digital.lib.utk.edu/collections/islandora/object/harp%3A1/datastream/MODS>`_
    :name: `Multi-role name from harp:1 MODS record <https://digital.lib.utk.edu/collections/islandora/object/harp%3A1/datastream/MODS>`_

    <name authority="naf" valueURI="http://id.loc.gov/authorities/names/no2002022963">
        <namePart>Swan, W. H. (William H.)</namePart>
        <role>
            <roleTerm authority="marcrelator" valueURI="http://id.loc.gov/vocabulary/relators/cmp">
                Composer
            </roleTerm>
        </role>
        <role>
            <roleTerm authority="marcrelator" valueURI="http://id.loc.gov/vocabulary/relators/com">
                Compiler
            </roleTerm>
        </role>
    </name>

.. code-block:: turtle
    :caption:  `Resulting RDF for a name from harp:1 MODS record <https://digital.lib.utk.edu/collections/islandora/object/harp%3A1/datastream/MODS>`_
    :name: `Resulting RDF for a name from harp:1 MODS record <https://digital.lib.utk.edu/collections/islandora/object/harp%3A1/datastream/MODS>`_

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1>
        relators:cmp <http://id.loc.gov/authorities/names/no2002022963> ;
        relators:com <http://id.loc.gov/authorities/names/no2002022963> .

Do Not Keep Any Other Values Associated with a Name
---------------------------------------------------

Use Case
^^^^^^^^

There are other XPaths in our system that are associated with names that are no longer needed.  Do not migrate these.

Justification
^^^^^^^^^^^^^

In an RDF based system that leverages linked data, it's unnecessary to keep traditional :code:`name` information
like :code:`authority`, :code:`displayForm`, :code:`type`, or :code:`description`. Authorities are present in the URI itself and information such as
:code:`description` or :code:`displayForm` are available from the class our object refers to.  While :code:`type` is not available, it has little
meaning in our current system and will only complicate things in the future.

XPaths
^^^^^^

:code:`name/role/roleTerm/@authority` OR

:code:`name/@authority` OR

:code:`name/role/roleTerm/@authorityURI` OR

:code:`name/@type` OR

:code:`name/displayForm` OR

:code:`name/description`

Decision
^^^^^^^^

Do not migrate.

originInfo
==========

+-----------------+----------------+------------------------------------------------------------------------------+
| Predicate       | Value Type     | Usage Notes                                                                  |
+=================+================+==============================================================================+
| dcterms:created | Literal or URI | The date a resource was created, formatted as an EDTF string.                |
+-----------------+----------------+------------------------------------------------------------------------------+
| dcterms:issued  | Literal or URI | The date a resource was issued, formatted as an EDTF string.                 |
+-----------------+----------------+------------------------------------------------------------------------------+
| dcterms:date    | Literal or URI | An unspecified date associated with a resource, formatted as an EDTF string. |
+-----------------+----------------+------------------------------------------------------------------------------+
| relators:pbl    | Literal or URI | The publisher associated with the resource.                                  |
+-----------------+----------------+------------------------------------------------------------------------------+
| relators:pup    | Literal or URI | A place associated with the publication of the resource.                     |
+-----------------+----------------+------------------------------------------------------------------------------+

originInfo/dateCreated
----------------------

Use Case
^^^^^^^^

:code:`dateCreated` captures dates and date ranges identifying or approximating when the physical object was created.

Justification
^^^^^^^^^^^^^

No dispute on the values in :code:`dateCreated`.

XPath
^^^^^

:code:`originInfo/dateCreated` OR

:code:`originInfo/dateCreated[@encoding='edtf']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@keyDate='yes']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@keyDate='yes'][@point='end']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@keyDate='yes'][@point='end'][@qualifier='approximate']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@keyDate='yes'][@point='end'][@qualifier='inferred']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@keyDate='yes'][@point='start']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@keyDate='yes'][@point='start'][@qualifier='approximate']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@keyDate='yes'][@point='start'][@qualifier='inferred']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@keyDate='yes'][@point='start'][@qualifier='questionable']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@keyDate='yes'][@qualifier='approximate']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@keyDate='yes'][@qualifier='inferred']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@keyDate='yes'][@qualifier='questionable']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@point='end']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@point='end'][@qualifier='approximate']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@point='end'][@qualifier='inferred']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@point='start']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@point='start'][@keyDate='yes']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@point='start'][@keyDate='yes'][@qualifier='approximate']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@point='start'][@qualifier='approximate']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@point='start'][@qualifier='inferred'][@keyDate='yes']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@qualifier='approximate']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@qualifier='approximate'][@keyDate='yes'][@point='start']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@qualifier='approximate'][@point='end']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@qualifier='inferred'][@keyDate='yes'][@point='start']` OR

:code:`originInfo/dateCreated[@encoding='edtf'][@qualifier='inferred'][@point='end']` OR

:code:`originInfo/dateCreated[@encoding='w3cdtf'][@keyDate='yes'][@point='start']` OR

:code:`originInfo/dateCreated[@encoding='w3cdtf'][@point='start'][@keyDate='yes']` OR

:code:`originInfo/dateCreated[@point='end']` OR

:code:`originInfo/dateCreated[@qualifier='approximate']` OR

:code:`originInfo/dateCreated[@qualifier='approximate'][@encoding='edtf'][@keyDate='yes']` OR

:code:`originInfo/dateCreated[@qualifier='approximate'][@encoding='edtf'][@keyDate='yes'][@point='end']` OR

:code:`originInfo/dateCreated[@qualifier='approximate'][@encoding='edtf'][@keyDate='yes'][@point='start']` OR

:code:`originInfo/dateCreated[@qualifier='inferred']` OR

:code:`originInfo/dateCreated[@qualifier='inferred'][@encoding='edtf'][@keyDate='yes'][@point='start']` OR

:code:`originInfo/dateCreated[@qualifier='questionable']` OR

:code:`originInfo/dateCreated[@qualifier='questionable'][@encoding='edtf'][@keyDate='yes']`

Decisions
^^^^^^^^^

We will convert `w3cdtf` to `edtf` values as part of our migration process; additionally, we will integrate EDTF Level 2 features where necessary. The `dcterms:created` property was selected.

`Example record - ekcd:95 <https://digital.lib.utk.edu/collections/islandora/object/ekcd:95/datastream/MODS/view>`_

.. code-block:: xml

    <originInfo>
        <dateCreated qualifier="inferred">1955</dateCreated>
        <dateCreated encoding="edtf" keyDate="yes">1955</dateCreated>
    </originInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:created "1955", "1955~" .

`Example record - volvoices:3849 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A3849/datastream/MODS>`_

.. code-block:: xml

    <originInfo>
        <dateCreated>approximately between 1940 and 1950</dateCreated>
        <dateCreated encoding="edtf" keyDate="yes" point="start" qualifier="approximate">1940</dateCreated>
        <dateCreated encoding="edtf" keyDate="yes" point="end">1950</dateCreated>
    </originInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:created "approximately between 1940 and 1950", "1940~/1950" .

originInfo/dateIssued
---------------------

Use Case
^^^^^^^^

:code:`dateIssued` captures dates and date ranges identifying or approximating when the physical object was issued.

Justification
^^^^^^^^^^^^^

No dispute on the values in :code:`dateIssued`.

XPaths
^^^^^^

:code:`originInfo/dateIssued` OR

:code:`originInfo/dateIssued[@encoding='edtf']` OR

:code:`originInfo/dateIssued[@encoding='edtf'][@keyDate='yes']` OR

:code:`originInfo/dateIssued[@encoding='edtf'][@keyDate='yes'][@point='end'][@qualifier='inferred']` OR

:code:`originInfo/dateIssued[@encoding='edtf'][@keyDate='yes'][@point='start']` OR

:code:`originInfo/dateIssued[@encoding='edtf'][@keyDate='yes'][@point='start'][@qualifier='inferred']` OR

:code:`originInfo/dateIssued[@encoding='edtf'][@keyDate='yes'][@qualifier='approximate']` OR

:code:`originInfo/dateIssued[@encoding='edtf'][@keyDate='yes'][@qualifier='inferred']` OR

:code:`originInfo/dateIssued[@encoding='edtf'][@keyDate='yes'][@qualifier='questionable']` OR

:code:`originInfo/dateIssued[@encoding='edtf'][@point='end']` OR

:code:`originInfo/dateIssued[@encoding='edtf'][@point='start']` OR

:code:`originInfo/dateIssued[@encoding='edtf'][@point='start'][@keyDate='yes']` OR

:code:`originInfo/dateIssued[@point='end']` OR

:code:`originInfo/dateIssued[@qualifier='approximate']` OR

:code:`originInfo/dateIssued[@qualifier='approximate'][@encoding='edtf'][@keyDate='yes']` OR

:code:`originInfo/dateIssued[@qualifier='inferred']` OR

:code:`originInfo/dateIssued[@qualifier='inferred'][@encoding='edtf'][@keyDate='yes'][@point='end']` OR

:code:`originInfo/dateIssued[@qualifier='inferred'][@encoding='edtf'][@keyDate='yes'][@point='start']`

Decision
^^^^^^^^

We will integrate EDTF Level 2 features where applicable. The `dcterms:issued` property was selected.

`Example record - volvoices:2993 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A2993>`_

.. code-block:: xml

    <originInfo>
      <dateCreated>1948-01</dateCreated>
      <dateCreated encoding="edtf" keyDate="yes">1948-01</dateCreated>
      <dateIssued encoding="edtf" keyDate="yes" qualifier="approximate">1948</dateIssued>
    </originInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:created "1948-01", "1948-01" ;
        dcterms:issued "1948~" .

originInfo/dateOther
--------------------

Use Case
^^^^^^^^

:code:`dateOther` captures other significant dates associated with the resource.

Justification
^^^^^^^^^^^^^

No dispute on the values in :code:`dateOther`.

XPath
^^^^^

:code:`originInfo/dateOther` OR

:code:`originInfo/dateOther[@encoding='edtf']` OR

:code:`originInfo/dateOther[@encoding='edtf'][@point='end']` OR

:code:`originInfo/dateOther[@encoding='edtf'][@point='start']`

Decisions
^^^^^^^^^

As part of leveraging the EDTF format, some conversion will be necessary; e.g. translating date strings to EDTF values as in the following example. The `dcterms:date` property was selected.

`playbills:1052 <https://digital.lib.utk.edu/collections/islandora/object/playbills:1052/datastream/MODS/view>`_

.. code-block:: xml

    <originInfo>
      <dateIssued>Jun 30, 1965</dateIssued>
      <dateIssued encoding="edtf">1965-06-30</dateIssued>
      <dateOther encoding="edtf">1964/1965</dateOther>
      <place>
         <placeTerm valueURI="http://id.loc.gov/authorities/names/n80003889">University of Tennessee, Knoxville</placeTerm>
      </place>
      <publisher>University of Tennessee Theatre Department </publisher>
   </originInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .
    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1> dcterms:issued "Jun 30, 1965", "1965-06-30" ;
        dcterms:date "1964/1965" ;
        relators:pbl "University of Tennessee Theatre Department" ;
        relators:pub <http://id.loc.gov/authorities/names/n80003889> .

originInfo/place/placeTerm
---------------------------

Use Case
^^^^^^^^
This XPath identifies a place associated with the publication of the resource.

Justification
^^^^^^^^^^^^^

No dispute on the values in :code:`place/placeTerm`.

XPath
^^^^^

:code:`originInfo/place/placeTerm[@text]` OR

:code:`originInfo/place/placeTerm[@text][@valueURI]` OR

:code:`originInfo/place[@supplied]/placeTerm[@text][@valueURI]`

Decision
^^^^^^^^

The majority of the applicable values are associate with a :code:`@valueURI`.  The `relators:pup` property was selected.

.. code-block:: xml

    <originInfo>
        <place supplied="yes">
            <placeTerm type="text" valueURI="http://id.loc.gov/authorities/names/n79072935">Meadville (Crawford County, Pa.)</placeTerm>
        </place>
        <publisher>Keystone View Company</publisher>
        <dateCreated>between 1890 and 1930?</dateCreated>
        <dateCreated encoding="edtf" keyDate="yes" point="start" qualifier="questionable">1890</dateCreated>
        <dateCreated encoding="edtf" keyDate="yes" point="end">1930</dateCreated>
    </originInfo>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .
    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> relators:pbl "Keystone View Company" ;
        relators:pup <http://id.loc.gov/authorities/names/n79072935> ;
        dcterms:created "between 1890 and 1930?", "1890?/1930" .

Empty :code:`placeTerm` elements will be ignored.

originInfo/publisher
--------------------

Use Case
^^^^^^^^

Identifies a publisher associated with the resource.

Justification
^^^^^^^^^^^^^

No dispute on the values contained in :code:`publisher`.

XPath
^^^^^

:code:`originInfo/publisher`

Decision
^^^^^^^^

The `relators:pbl` property was selected.
`Example record - <https://digital.lib.utk.edu/collections/islandora/object/utsmc%3A13759>`_:

.. code-block:: xml

    <originInfo>
        <place>
            <placeTerm valueURI="http://id.loc.gov/authorities/names/n79006530">Baltimore (Md.)</placeTerm>
        </place>
        <publisher>Frederick D. Benteen</publisher>
    </originInfo>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1> relators:pbl "Frederick D. Benteen" ;
        relators:pup <http://id.loc.gov/authorities/names/n79006530> .

originInfo/issuance
-------------------

Use Case
^^^^^^^^

This XPath provides details for how the resource was published. All 4207 of our instances of :code:`issuance` have the value "serial".

Justification
^^^^^^^^^^^^^

The value held in the XPath doesn't provide any significantly useful information.

XPath
^^^^^

:code:`originInfo/issuance`

Decision
^^^^^^^^

We will not be migrating :code:`issuance`.

physicalDescription
===================

+------------------+----------------+--------------------------------------------------+
| Predicate        | Value Type     | Usage Notes                                      |
+==================+================+==================================================+
| dcterms:abstract | Literal        | Use for form values with @type="material".       |
+------------------+----------------+--------------------------------------------------+
| edm:hasType      | URI or Literal | Use for form values without attributes.          |
+------------------+----------------+--------------------------------------------------+
| rdau:P60550      | Literal        | Use for all extent values.                       |
+------------------+----------------+--------------------------------------------------+
| skos:note        | Literal        | Use for notes nested within physicalDescription. |
+------------------+----------------+--------------------------------------------------+

digitalOrigin
-------------

Use Case
^^^^^^^^

Currently there are 28,137 records that have a :code:`digitalOrigin` value. This value is absent from 23,190 records. While present
in the MODS record, these values (we have "born digital", "digitized other analog", and "reformatted digital" in our collections)
are not publicly displayed anywhere. These values communicate the "method by which a resource achieved digital form."

Justification
^^^^^^^^^^^^^

We have decided for a number of reasons that migrating our :code:`digitalOrigin` values does is not beneficial. As mentioned above,
these values are not currently viewable by users. Arguably, these values will also already be apparent from the technical
metadata and do not need to be captured in the descriptive metadata. In addition, we are unaware of any backend technical
use case for this data at present. While knowing if something is "born digital" might be useful, all of the content within
Digital Collections is curated and meets our technical expectations. A "born digital" label would be more actionable for
resources gathered outside of the Digital Collections creation process. These born digital resources from "the wild" would
likely not be on the same platform as Digital Collections resources.

XPath
^^^^^

:code:`physicalDescription/digitalOrigin`

Decision
^^^^^^^^

We have decided to not migrate these values as is justified above. Here's an `example record - voloh:10 <https://digital.lib.utk.edu/collections/islandora/object/voloh%3A10/datastream/MODS/view>`_

.. code-block:: xml

    <digitalOrigin>born digital</digitalOrigin>

note
----

Use Case
^^^^^^^^

Two collections, the Botanical Photography of Alan S. Heilman and the William Derris Film Collection, include :code:`note` elements
within :code:`physicalDescription`. These values are of two types. The majority of the values communicate camera settings for the
Heilman collection, while a smaller number of values share the "Film type" that was used to produce the print that was
digitized. Below is a small sample of these values:

1. Camera setting: 7@50 on 25; with filter
2. 0.18x magnification, 100 Velvia
3. Film type: Kodachrome Transparency
4. zoomA -> 70 [A], Auto f16E100s
5. Film type: GEMounts

These values are somewhat problematic because they do not describe the digitized resource, but instead provide information about
the process that created these resources. This is useful information to know, but isn't tied directly to the resource, making
the inclusion of the values within :code:`physicalDescription` inaccurate.

Justification
^^^^^^^^^^^^^

Since we do not use :code:`physicalDescription/note` regularly, it would streamline our data if these values could be
appropriately placed elsewhere. I attempted to match film type values ("GEMounts" and "Kodachrome Transparency") with AAT
terms, but wasn't able to find anything appropriate for "GEMounts." The accuracy of some of this information is questionable
(for instance, GEMounts are likely a brand instead of a film type), but without access to the actual materials during the quarantine, it's
impossible to make an informed judgement on what should be changed. To retain this contextual information that might
prove useful to researchers interested in photographic processes and techniques, it seems best to simply put these values
in a generic `note` field. If additional attention can be given to these two collections in the future, we can remediate
the metadata following migration with the benefit of having access to the physical materials.

XPath
^^^^^

:code:`physicalDescription/note`

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

The :code:`extent` element includes values that indicate time and physical dimensions. Time is consistently shared in hours, minutes
and seconds. Physical dimensions are most consistently represented in inches and feet, but cm are also used for smaller
items that might benefit from a more granular measurement. While this kind of information has historically been included
in MARC records to ensure that books are not larger than the shelf height, extent values can also provide important
contextual information that is relevant to better understanding resources in a digital environment. Particularly in the
case of photography, the dimensions can be used to help determine the type of film.

Justification
^^^^^^^^^^^^^

The working group's shared philosophies were influential in decided on the best property to use for :code:`extent` values. The
Islandora Metadata Interest Group's default mapping suggests using `dcterms:extent` and using a blank node with a literal as
a RDF value. This group is against using blank nodes when at all possible because they make it more difficult for the
user to consume content. The Samvera mapping uses `rdau:P60550`, which is less than ideal because `rdau` does not support
content negotiation. This means that the URI provided for the desired property does not allow a user to directly request
RDF. No other more suitable properties could be found for :code:`extent` values. Given this predicament, the working group
decided to use `rdau:P60550` because it is dereferenceable, which a blank node is not. Still, the inability to retrieve
RDF directly will limit users wishing to interact with our data in this way.

XPath
^^^^^

:code:`physicalDescription/extent`

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

The Great Smoky Mountains Colloquy collection is the only collection that includes the :code:`unit` attribute on :code:`extent`. The
collection consists of 34 total records.

Justification
^^^^^^^^^^^^^

It is important for the user to know what the unit of measurement is for a value within the :code:`extent` field. It is also
important for us to share this information consistently. In order to retain the needed information while also conforming
the metadata from this collection with the rest of our records, we propose that the :code:`@unit` value is added to the :code:`extent`
string during migration. This would involve simply taking the existing value in :code:`extent` and then adding ' pages' to the
string. Note that all of the resources within the Colloquy collection have more than one page, so the plural form of the
word will always be accurate. See the Decision section of extent above for more explanation of `rdau:P60550`.

XPath
^^^^^

:code:`physicalDescription/extent[@unit="pages"]`

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

At the time of analysis, there were 10,853 records that contained a :code:`form` term without an associated :code:`valueURI` attribute.
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
like :code:`typeOfResource`. While these form values do not currently contain :code:`valueURI` attributes, the strings themselves
are controlled terms that are clean and consistent so we want to bring them over.

XPath
^^^^^

:code:`physicalDescription/form`

Decision
^^^^^^^^

We will use `edm:hasType` instead of `dcterms:format` in order to accommodate form values without a URI. We need to move all
of the form values over, so using `edm:hasType` will make sure that we bring every form term regardless of whether it is
defined as a URI or a literal.

Here's an `example record - gamble:1 <https://digital.lib.utk.edu/collections/islandora/object/gamble%3A1/datastream/MODS/view>`_

.. code-block:: xml

    <form>cartoons (humorous images)</form>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/> .

    <https://example.org/objects/1>
        edm:hasType "cartoons (humorous images)" .

form - Has URI
--------------

Use Case
^^^^^^^^

The majority of UTK's :code:`form` values include a :code:`valueURI` from the Art and Architecture Thesaurus (AAT). These values provide
important access to users by providing physical information about the original resource. :code:`form` values are not currently
displayed in DPLA's interface, but `DPLA's MAP 5 <https://drive.google.com/file/d/1fJEWhnYy5Ch7_ef_-V48-FAViA72OieG/view>`_
lists preferred from subtype values that will eventually be implemented. Work has been done to align as many of our :code:`form`
terms as possible with this preferred list.

Justification
^^^^^^^^^^^^^

:code:`form` values are important access points that provide more specific information than is provided in higher-level elements
like :code:`typeOfResource`.

XPath
^^^^^

:code:`physicalDescription/form[@valueURI]`

Decision
^^^^^^^^

Here's an `example record - ruskin:108 <https://digital.lib.utk.edu/collections/islandora/object/ruskin%3A108/datastream/MODS/view>`_

.. code-block:: xml

    <form authority="http://vocab.getty.edu/aat/300046300">photographs</form>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/> .

    <https://example.org/objects/1>
        edm:hasType <http://vocab.getty.edu/aat/300046300> .

form - @type="material"
-----------------------

Use Case
^^^^^^^^

The Archivision collection has a special :code:`type` attribute so that the list of materials used to create specific buildings
can be faceted. The material types are consistently listed in the same order within the string to make this possible.

Justification
^^^^^^^^^^^^^

In order to attempt to streamline this data to better align with UTK's existing records, all existing terms were compared
with similar terms from the Art and Architecture Thesaurus. The hope was to split the string field on commas and find
controlled terms for each individual value so that these could simply be presented in :code:`physicalDescription/form`
without the need for a unique :code:`type` attribute. Analysis showed that a number of values included very specific descriptions
of the material type in parentheses following the broader term. For instance, 'marble (white Carrara and green Prato marble).'
This specificity made it impossible to use the AAT without losing some of the information present in the original records.
Treating these values as part of the abstract will ensure that they display prominently, which wouldn't be the case with
a note value necessarily. To make this read more fluidly, 'Made of ' can be added to the front of the string and an ending
period added ('.').

XPath
^^^^^

:code:`physicalDescription/form[@type="material"]`

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

A total of 14,725 records have an :code:`internetMediaType` while this element is not present in 36,602 records. It is used to indicate
the MIME type of the access file for the digitized resource.

Justification
^^^^^^^^^^^^^

We do not need to migrate this information from the descriptive metadata as it will be captured automatically during
file characterization in the new system. We also do not want to move the current values over from the existing metadata
because they often share inaccurate information. Finally, this element is currently present in only

XPath
^^^^^

:code:`physicalDescription/internetMediaType`

Decision
^^^^^^^^

Do not migrate.

`Example record - voloh:10 <https://digital.lib.utk.edu/collections/islandora/object/voloh%3A10/datastream/MODS/view>`_

.. code-block:: xml

    <internetMediaType>audio/wav</internetMediaType>

note
====

+-----------------------------------+----------------+-------------------------------------------------------------------------+
| Predicate                         | Value Type     | Usage Notes                                                             |
+===================================+================+=========================================================================+
| bf:IntendedAudience               | Literal or URI | Use for information that identifies the specific audience or            |
|                                   |                | intellectual level for which the content of the resource is considered  |
|                                   |                | appropriate.                                                            |
+-----------------------------------+----------------+-------------------------------------------------------------------------+
| dce:subject                       | Literal or URI | Use for name, topical subjects, and uncontrolled keywords.              |
|                                   |                | Use of a URI from a controlled subject vocabulary is preferred          |
|                                   |                | over a literal value                                                    |
+-----------------------------------+----------------+-------------------------------------------------------------------------+
| opaque:sheetmusic_instrumentation | Literal or URI | Use for sheet music, a listing of the performing forces                 |
|                                   |                | called for by a particular piece of sheet music, including              |
|                                   |                | both voices and external instruments.                                   |
+-----------------------------------+----------------+-------------------------------------------------------------------------+
| opaque:sheetmusic_firstLine       | Literal or URI | Use for sheet music, entering a direct transcription of the             |
|                                   |                | first line of lyrics appearing in the song.                             |
+-----------------------------------+----------------+-------------------------------------------------------------------------+
| skos:note                         | Literal        | Use for the note value.                                                 |
+-----------------------------------+----------------+-------------------------------------------------------------------------+


note - Just a note
------------------

Use Case
^^^^^^^^

Usually, a :code:`note` is just a :code:`note`.  The XPath section below lists when this is the case. In the case that an XPath has a
specific attribute and value, prepend the value to the text node.

Justification
^^^^^^^^^^^^^

The Samvera community attempts to keep some of the granularity of MODS by prepending the text value of the attribute
to the text node when one exists.  When one doesn't, simply take the text node.

In Bibframe, there was no attempt to convert the 562 MARC field.  For this reason, "handwritten" documents are just
regular notes.

XPath
^^^^^

:code:`note` OR

:code:`note[@type="handwritten"]` OR

:code:`note[@type="provenance"]` OR

:code:`note[@displayLabel="Attribution"]` OR

:code:`note[@displayLabel="use and reproduction"]` OR

:code:`note[@displayLabel="Local Rights"]`

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

When a note has a :code:`@type = "Instrumenation"`, it is not a general note. Instead, this element is a listing of the
performing forces called for by a particular piece of music.

Justification
^^^^^^^^^^^^^

We reviewed several bibliographic and music ontologies including the Music Ontology, the Internet of Music Thingz, and
MusicBrainz, but none seemed to have a predicate to represent this idea. We did notice that Opaque Namespace by
Oregon Digital did have a matching predicate.  In the Samvera community, not only is this ontology used, but occasionally
the community has suggested new predicates to be created within Opaque Namespaces.

XPath
^^^^^

:code:`note[@type="Instrumentation"]`

Decision
^^^^^^^^

`Example record from vanvactor:15773 <https://digital.lib.utk.edu/collections/islandora/object/vanvactor:15773/datastream/MODS>`_

.. code-block:: xml

    <note type="instrumentation">
        For soprano, mezzo-soprano, contralto, 2 flutes, 2 oboes, 2 clarinets, 2 bassoons, 2 horns, 2 trumpets, timpani, 2 violins, viola, cello, and double bass.
    </note>


.. code-block:: turtle

    @prefix opaque: <http://opaquenamespace.org/ns/> .

    <https://example.org/objects/1>
        opaque:sheetmusic_instrumentation "For soprano, mezzo-soprano, contralto, 2 flutes, 2 oboes, 2 clarinets, 2 bassoons, 2 horns, 2 trumpets, timpani, 2 violins, viola, cello, and double bass." .


note - First Line
-----------------

Use Case
^^^^^^^^

When a note has a :code:`@type = "First line"` or :code:`@type = "first line"`, it is not a general note. Instead, this element is
a direct transcription of the first line of lyrics appearing in a song.

Justification
^^^^^^^^^^^^^

We reviewed several bibliographic and music ontologies including the Music Ontology, the Internet of Music Thingz, and
MusicBrainz, but none seemed to have a predicate to represent this idea. We did notice that Opaque Namespace by
Oregon Digital did have a matching predicate.  In the Samvera community, not only is this ontology used, but occasionally
the community has suggested new predicates to be created within Opaque Namespaces.

XPath
^^^^^

:code:`note[@type="First line"]` OR

:code:`note[@type="first line"]`

Decision
^^^^^^^^

`Example record from vanvactor:15773 <https://digital.lib.utk.edu/collections/islandora/object/vanvactor:15773/datastream/MODS>`_

.. code-block:: xml

    <note type="First line">
        Ojitos de pena carita de luna, lloraba la niña sin causa ninguna.
    </note>


.. code-block:: turtle

    @prefix opaque: <http://opaquenamespace.org/ns/> .

    <https://example.org/objects/1>
        opaque:sheetmusic_firstLine "Ojitos de pena carita de luna, lloraba la niña sin causa ninguna." .


note - Target audience
----------------------

Use Case
^^^^^^^^

If a note has a :code:`displayLabel` attribute with the value of "Grade level", it refers to the target audience of the resource.

Justification
^^^^^^^^^^^^^

The MARC 521 field should be mapped to the Bibframe intended audience field. The field is defined as information that
identifies the specific audience or intellectual level for which the content of the resource is considered appropriate.

XPath
^^^^^

:code:`note[@displayLabel="Grade level"]`

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

Some of our :code:`note`\ s actually refer to uncontrolled keywords or tags.

Justification
^^^^^^^^^^^^^

While not preferred, Samvera treats these as `dcterms:subjects` with a literal rather than an a URI.

XPath
^^^^^

:code:`note[@displayLabel="Tags"]`

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

We have several :code:`note`\ s that we do not need to migrate.

Justification
^^^^^^^^^^^^^

The data here is no longer important.

XPath
^^^^^

:code:`note[@displayLabel="DPN"]` OR

:code:`note[string()=""]` OR

:code:`note[@displayLabel="Intermediate provider"]` OR

:code:`note[@displayLabel="Intermediate Provider"]` OR

:code:`note[@displayLabel="Transcribed from Original Collection"]` OR

:code:`note[@displayLabel="Project Part"]`

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

+-------------------------+----------------+------------------------------------------------------+
| Properties              | Value Type     | Usage Notes                                          |
+=========================+================+======================================================+
| dcterms:spatial         | URI or Literal | Use for geographic subjects and coordinates.         |
+-------------------------+----------------+------------------------------------------------------+
| dcterms:subject         | URI or Literal | Use for topic and name subjects. URIs are preferred. |
+-------------------------+----------------+------------------------------------------------------+
| schema:temporalCoverage | Literal        | Use for temporal subjects. Numeric values should     |
|                         |                |      be formatted using EDTF.                        |
+-------------------------+----------------+------------------------------------------------------+

None type
---------

Use Case
^^^^^^^^

Several :code:`subject` elements contain unintentional null values. There are five within Tennessee Documentary History. Additional null
:code:`subject`\ s include vpmoore:133 and adams:76. Most of roth seems to have null :code:`subject/name/namePart` values.
It appears we might have inserted some blank nodes using the Islandora form entry. As there is no information, these
"values" are not used and have no true use case.

Justification
^^^^^^^^^^^^^

These nodes contain no information.

XPath
^^^^^

    :code:`subject/topic[string() = '']` OR

    :code:`subject/geographic[string() = '']` OR

    :code:`subject/name/namePart[string() = '']`

Decision
^^^^^^^^

Do not migrate.

Here's an `example of a null topic value - tdh:366 <https://digital.lib.utk.edu/collections/islandora/object/tdh%3A366/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <topic/>
    </subject>

Here's an `example of a null geographic value - vpmoore:133 <https://digital.lib.utk.edu/collections/islandora/object/vpmoore%3A133/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <geographic/>
    </subject>

Here's an `example of a null namePart value - roth:1587 <https://digital.lib.utk.edu/collections/islandora/object/roth%3A1587/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <name authority="" valueURI="">
            <namePart/>
            </name>
    </subject>

Topical and name subjects with URIs
-----------------------------------

Use Case
^^^^^^^^

Remediated collections include :code:`subject` values with URIs.

Justification
^^^^^^^^^^^^^

In migration, :code:`subject`\ s with :code:`name` and :code:`topic` values will be treated in the same way. We have decided that the previous
distinction between :code:`name` and :code:`topic` values as :code:`subject`\ s is not essential - only the presence of all the values in the
metadata is important.

XPath
^^^^^

Note that there is inconsistency in where the :code:`valueURI` attribute is placed.

    :code:`subject[@valueURI]/topic` OR

    :code:`subject/topic[@valueURI]` OR

    :code:`subject[@valueURI]/name/namePart` OR

    :code:`subject/name[@valueURI]/namePart`

Decision
^^^^^^^^

When a :code:`valueURI` is present for :code:`topic` or :code:`name` subject, it will be the value used in migration. Examples showing each
of the distinct XPaths are given below:

`acwiley:280 as an example of subject[@valueURI]/topic <https://digital.lib.utk.edu/collections/islandora/object/acwiley%3A280/datastream/MODS/view>`_

.. code-block:: xml

    <subject authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85147554">
        <topic>Women in art</topic>
    </subject>
    <subject authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85147447">
        <topic>Women artists</topic>
    </subject>
    <subject authority="tgm" valueURI="http://id.loc.gov/vocabulary/graphicMaterials/tgm008085">
        <topic>Portraits</topic>
    </subject>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:subject <http://id.loc.gov/authorities/subjects/sh85147554> ;
        dcterms:subject <http://id.loc.gov/authorities/subjects/sh85147447> ;
        dcterms:subject <http://id.loc.gov/vocabulary/graphicMaterials/tgm008085> .

`cdf:5384 as an example of subject/topic[@valueURI] <https://digital.lib.utk.edu/collections/islandora/object/cdf%3A5384/datastream/MODS/view>`_

.. code-block:: xml

    <subject>
        <topic valueURI="http://id.loc.gov/authorities/subjects/sh85023396">Child welfare</topic>
    </subject>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:subject <http://id.loc.gov/authorities/subjects/sh85023396> .

`wwiioh:2451 as an example of subject[@valueURI]/name/namePart <https://digital.lib.utk.edu/collections/islandora/object/wwiioh%3A2451/datastream/MODS/view>`_.

.. code-block:: xml

    <subject authority="naf" valueURI="http://id.loc.gov/authorities/names/n85185770">
        <name>
            <namePart>United States. Army. Medical Corps</namePart>
        </name>
    </subject>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:subject <http://id.loc.gov/authorities/names/n85185770> .

`helser:24792 as an example of subject/name[@valueURI] <https://digital.lib.utk.edu/collections/islandora/object/hesler%3A24792/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n87116131">
            <namePart>Atkinson, George Francis, 1854-1918</namePart>
        </name>
    </subject>
    <subject>
        <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n88144876">
            <namePart>Arthur, Joseph Charles, 1850-1942</namePart>
        </name>
    </subject>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:subject <http://id.loc.gov/authorities/names/n88144876> ;
        dcterms:subject <http://id.loc.gov/authorities/names/n87116131> .

Name and topical subjects without URIs
--------------------------------------

Use Case
^^^^^^^^

We'll need to treat any of these :code:`subject`\ s that aren't able to be reconciled as string values. For the postcard collection,
the use of dots (Database of the Smokies) as the authority makes it impossible to include a URI presently. Other collections
with string values that are: Charlie Daniel Cartoon Collection, Ed Gamble Cartoon Collection, Football Programs, Insurance Company of
North America Records, the American Civil War Collection, Ramsey Family Papers, Tennessee Documentary History,
and Volunteer Voices.

The Volunteer Voices collection includes :code:`subject`\ s with three different :code:`displayLabel` values - "Volunteer Voices Curriculum Topics",
"Tennessee Social Studies K-12 Eras in American History", and "Broad Topics". These :code:`subject`\ s are currently given separate
facets in Islandora's metadata display. Discovery to the collection via two of these subject categories is also featured
on the `Tennessee State Library and Archives website <https://sos.tn.gov/products/tsla/volunteer-voices>`_ ("Broad Topics"
and "Tennessee Social Studies K-12 Eras in American History"). While these :code:`subject`\ s have been distinguished previously from
other :code:`subject`\ s in the past by their distinct XPath, having so many different types of :code:`subject`\ s was found to be unnecessary
going forward. "Broad Topics" and "Curriculum Topics" will be folded in with all other :code:`subject`\ s. For links to external websites,
like TSLA's, we can use the string values to supply a link without needing to place them in a separate property. Note that
:code:`subject`\ s associated with "Tennessee Social Studies K-12 Eras in American History" are dealt with
separately below.

Justification
^^^^^^^^^^^^^

:code:`subject`\ s values are important access points for users that require migration. While URIs would be ideal from a technical
standpoint, strings still support discovery.

XPath
^^^^^

    :code:`mods/subject[not(@valueURI)]/topic[not(@valueURI)]` OR

    :code:`mods/subject[not(@valueURI)]/name[not(valueURI)]/namePart[not(valueURI)]`

Decision
^^^^^^^^

String values for :code:`topic` or :code:`name` subjects will be migrated when a :code:`valueURI` is not present.

Here's an `example record where only string values are available for topical subjects - gamble:123 <https://digital.lib.utk.edu/collections/islandora/object/gamble%3A123/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <topic>Environmentalism</topic>
    </subject>
    <subject>
        <topic>Factory and trade waste--Environmental aspects</topic>
    </subject>
    <subject>
        <topic>Pollution</topic>
    </subject>
    <subject>
        <topic>Knight</topic>
    </subject>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:subject "Environmentalism" ;
        dcterms:subject "Factory and trade waste--Environmental aspects" ;
        dcterms:subject "Pollution" ;
        dcterms:subject "Knight" .

Here's an `example where only a string value is available for a name - gamble:144 <https://digital.lib.utk.edu/collections/islandora/object/gamble%3A144/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <name>
            <namePart>Xerox Corporation</namePart>
        </name>
    </subject>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:subject "Xerox Corporation" .

Here's an `example from Volunteer Voices of a "Broad Topics" subject - volvoices:4058 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A4058/datastream/MODS/view>`_.

.. code-block:: xml

    <subject displayLabel="Broad Topics">
        <topic>Frontier Settlement and Migration</topic>
    </subject>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:subject "Frontier Settlement and Migration" .

Here's an `example of @displayLabel="Volunteer Voices Curriculum Topics" - volvoices:2141 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A2141/datastream/MODS/view>`_.

.. code-block:: xml

    <subject displayLabel="Volunteer Voices Curriculum Topics">
        <topic>Civil Rights movement in Tennessee</topic>
    </subject>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:subject "Civil Rights movement in Tennessee" .

Temporal subjects
-----------------

Use Case
^^^^^^^^

:code:`temporal` :code:`subject`\ s share information about a time period using text or a date (:code:`edtf`). None of our existing :code:`temporal` :code:`subject`\ s include URIs.These values are prominent in Volunteer Voices and the Pi Beta Phi to Arrowmont collections.

Justification
^^^^^^^^^^^^^

:code:`temporal` :code:`subject`\ s provide important access points. While not associated with a URI, the values are often from controlled
vocabularies created as part of a grant project. Because they are associated with grants and cross-institutional projects,
retaining these values is particularly important.

XPath
^^^^^

:code:`mods/subject/temporal`

Decision
^^^^^^^^

:code:`temporal` :code:`subject`\ s without the :code:`displayLabel` attribute will be directly mapped as strings to `schema:temporalCoverage`. This
property was chosen because it allows a wider range of values than other potential solutions (such as `dcterms:temporalCoverage`
which requires that the value is part of the class PeriodOfTime).

`Example of temporal subject - arrow:268 <https://digital.lib.utk.edu/collections/islandora/object/arrow%3A268>`_.

.. code-block:: xml

    <subject>
        <temporal>The Birth of Arrowmont, Gatlinburg, Tennessee, 1965-1979</temporal>
    </subject>


.. code-block:: turtle

    @prefix schema: <http://schema.org/> .

    <https://example.org/objects/1> schema:temporalCoverage "The Birth of Arrowmont, Gatlinburg, Tennessee, 1965-1979" .

In addition to these textual values, UTK does have :code:`temporal` :code:`subject`\ s that share numeric dates in EDTF format. These are
primarily from the Volunteer Voices collection. `Here's an example record - volvoices:2945 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A2945/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <temporal>1970-09-30</temporal>
    </subject>

.. code-block:: turtle

    @prefix schema: <http://schema.org/> .

    <https://example.org/objects/1> schema:temporalCoverage "1970-09-30" .

Temporal subjects from Volunteer Voices (K-12 Eras) with string and XPath inconsistencies
-----------------------------------------------------------------------------------------

Use Case
^^^^^^^^

While two of the subject categories associated with the Volunteer Voices collection can be folded into `dcterms:subject`
directly ("Broad Topics" and "Volunteer Voices Curriculum Topics"), special attention needs to be given to :code:`subject`\ s associated
with "Tennessee Social Studies K-12 Eras in American History". There are instances in which a value associated with one
of these topics is used, but the :code:`displayLabel` has been left off and they have incorrectly been categorized as :code:`geographic`
:code:`subject`\ s.

Justification
^^^^^^^^^^^^^

It is important to treat these values as a separate category to ensure that the text value is not split across separate
categories (aka `schema:temporalCoverage` and `dcterms:subject`). In addition, some standardization of the label needs to be
done for all the records associated with a given concept to be colocated.

XPath
^^^^^

    :code:`subject/geographic[string()="Contemporary United States (1968-present)."]` OR

    :code:`subject/geographic[string()="Postwar United States (1945-1970)."]` OR

    :code:`subject/geographic[string()="The Great Depression and World War II (1929-1945)."]` OR

    :code:`subject/geographic[string()="The Emergence of Modern America (1890-1930)."]` OR

    :code:`subject/geographic[string()="The Development of the Industrial United States (1870-1900)."]` OR

    :code:`subject/geographic[string()="Expansion and Reform (1801-1861)."]` OR

    :code:`subject/geographic[string()="Revolution and the New Nation (1754-1820)."]` OR

    :code:`subject/geographic[string()="Colonization and Settlement (1585-1763)."]`

Decision
^^^^^^^^

An `example of a record that leaves off the displayLabel, but the string matches a K-12 era - volvoices:11303  <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A11303/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <geographic>Expansion and Reform (1801-1861).</geographic>
    </subject>

The final :code:`subject/geographic` value actually matches one of the values listed in the "Tennessee Social Studies K-12 Eras
in American History". While it is placed in a :code:`geographic` :code:`subject` here in the XML, it should be in a :code:`temporal` :code:`subject` (as
the date range following the text suggests). One value is placed in :code:`subject/topic`.The following values are all
of the exceptions:

We will want to remediate before migration, match on and transform these values during migration, or deal with them after migration. The string values
also don't exactly match the string values present in :code:`topic[@displayLabel="Tennessee Social Studies K-12 Eras in American History"]`.
The eras ("Era 2 - ", "Era 3 - ", etc.) need to be added and the trailing periods removed for these to match. Below is a
table of the values that need to be edited along with their appropriate match.

+--------------------------------------------------------------+---------------------------------------------------------------------+
| Incorrect Value                                              | Established Era Term                                                |
+--------------------------------------------------------------+---------------------------------------------------------------------+
| Contemporary United States (1968-present).                   | Era 10 - Contemporary United States (1968 to the present)           |
+--------------------------------------------------------------+---------------------------------------------------------------------+
| Postwar United States (1945-1970).                           | Era 9 - Postwar United States (1945-1970's)                         |
+--------------------------------------------------------------+---------------------------------------------------------------------+
| The Great Depression and World War II (1929-1945).           | Era 8 - The Great Depression and World War II (1929-1945)           |
+--------------------------------------------------------------+---------------------------------------------------------------------+
| The Emergence of Modern America (1890-1930).                 | Era 7 - The Emergence of Modern America (1890-1930)                 |
+--------------------------------------------------------------+---------------------------------------------------------------------+
| The Development of the Industrial United States (1870-1900). | Era 6 - The Development of the Industrial United States (1870-1900) |
+--------------------------------------------------------------+---------------------------------------------------------------------+
| Expansion and Reform (1801-1861).                            | Era 4 - Expansion and Reform (1801-1861)                            |
+--------------------------------------------------------------+---------------------------------------------------------------------+
| Revolution and the New Nation (1754-1820).                   | Era 3 -Revolution and the New Nation (1754-1820)                    |
+--------------------------------------------------------------+---------------------------------------------------------------------+
| Colonization and Settlement (1585-1763).                     | Era 2 - Colonization and Settlement (1585-1763)                     |
+--------------------------------------------------------------+---------------------------------------------------------------------+

.. code-block:: turtle

    @prefix schema: <http://schema.org/> .

    <https://example.org/objects/1> schema:temporalCoverage "Era 4 - Expansion and Reform (1801-1861)" .

`Example of @displayLabel="Tennessee Social Studies K-12 Eras in American History" - volvoices:1833 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A1833/datastream/MODS/view>`_.

.. code-block:: xml

    <subject displayLabel="Tennessee Social Studies K-12 Eras in American History">
        <temporal>Era 9 - Postwar United States (1945-1970's)</temporal>
    </subject>

These will simply be treated as other :code:`temporal` :code:`subject`\ s are. Note that we only have strings for :code:`temporal` :code:`subject`\ s.

.. code-block:: turtle

    @prefix schema: <http://schema.org/> .

    <https://example.org/objects/1> schema:temporalCoverage "Era 9 - Postwar United States (1945-1970's)" .

Geographic subjects
-------------------

Use Case
^^^^^^^^

UTK has :code:`geographic` :code:`subject`\ s with and without URIs. Like with other elements, the placement of the URIs is not consistent.
URIs will be used when present, but strings can be used when there is no URI.

Justification
^^^^^^^^^^^^^

:code:`geographic` :code:`subject`\ s warrant a separate property from both :code:`temporal` and :code:`topic` :code:`subject`\ s so that they can be displayed
separately on the interface. :code:`geographic` :code:`subject`\ s aid with discovery.

XPath
^^^^^

    :code:`subject[@valueURI]/geographic` OR

    :code:`subject/geographic[@valueURI]`

As noted previously, there are a handful of string values in :code:`geographic` elements within volvoices that need to be moved
to be treated differently than other :code:`geographic` values.

    :code:`subject/geographic[not(string()="Contemporary United States (1968-present).")]` OR

    :code:`subject/geographic[not(string()="Postwar United States (1945-1970).")]` OR

    :code:`subject/geographic[not(string()="The Great Depression and World War II (1929-1945).")]` OR

    :code:`subject/geographic[not(string()="The Emergence of Modern America (1890-1930).")]` OR

    :code:`subject/geographic[not(string()="The Development of the Industrial United States (1870-1900).")]` OR

    :code:`subject/geographic[not(string()="Expansion and Reform (1801-1861).")]` OR

    :code:`subject/geographic[not(string()="Revolution and the New Nation (1754-1820).")]` OR

    :code:`subject/geographic[not(string()="Colonization and Settlement (1585-1763).")]`

Decision
^^^^^^^^

`Here's an example where the URI is present on the subject - webster:1127 <https://digital.lib.utk.edu/collections/islandora/object/webster%3A1127/datastream/MODS/view>`_.

.. code-block:: xml

    <subject authority="geonames" valueURI="http://sws.geonames.org/4050810">
        <geographic>The Sawteeth</geographic>
        <cartographics>
            <coordinates>35.64342, -83.36237</coordinates>
        </cartographics>
    </subject>
    <subject authority="geonames" valueURI="http://sws.geonames.org/4609260">
        <geographic>Brushy Mountain</geographic>
        <cartographics>
            <coordinates>35.67787, -83.43016</coordinates>
    </cartographics>
    </subject>
    <subject authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85057008">
        <geographic>Great Smoky Mountains (N.C. and Tenn.)</geographic>
    </subject>

`Here's an example where the URI is present on the geographic element - roth:2165 <https://digital.lib.utk.edu/collections/islandora/object/roth%3A2165/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <geographic authority="geonames" valueURI="http://sws.geonames.org/4178924/about.rdf">Yulee Sugar Mill Ruins Historic State Park</geographic>
    </subject>

Regardless of URI placement, we will map the values the same. Note that if the :code:`geographic` term includes coordinates and
a :code:`geonames` URI, we will drop the coordinates. More information on this is given in the Coordinates section following this
section. Below is the decision for webster:1127.

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:spatial <http://sws.geonames.org/4050810> ;
        dcterms:spatial <http://sws.geonames.org/4609260> ;
        dcterms:spatial <http://id.loc.gov/authorities/subjects/sh85057008> .

If only strings are present, like with `volvoices:14173 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A14173/datastream/MODS/view>`_, then the string value will be kept.

.. code-block:: xml

    <subject>
        <geographic>Covington (Tenn.)</geographic>
    </subject>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:spatial "Covington (Tenn.)" .

Coordinates
-----------

Use Case
^^^^^^^^

There are a total of **702 unique coordinate values** in UTK's collections. Many are associated with geonames terms,
but there are 8 coordinates associated with Library of Congress terms. These terms are "Great Smoky Mountains
National Park (N.C. And Tenn.)", "Knoxville (Tenn.)", "Sevier County (Tenn.)", "Dickson County (Tenn.)", "Hardin County (Tenn.)",
"Bluff City (Tenn.)", and "Saint Andrews (Tenn.)". In addition, there are **120 geographic names that are not associated**
**with an authority** through the use of a URI, but they contain coordinates. The following lists some: "Abrams Creek", "Anthony Creek (Tenn.)",
"Arcadia Dam (Okla.)", "Arch Rock", "Arizona", "Arkansas", "Becky Cable House (Tenn.)", "Boston (Mass.)", "Bote Mountain Trail (Tenn.)",
"Bristol (Tenn.)", "Cades Cove Campground (Tenn.)", "Cades Cove Loop Road (Tenn.)", "Cades Cove Picnic Area (Tenn.)",
"Calderwood Dam (Tenn.)", "California", "Chattanooga (Tenn.)", "Cherokee Orchard (Tenn.)", "Chestnut Flats", "Chilhowee (Extinct city)",
"Chimney Tops", "Chimney Tops (Tenn.)", "Chimney Tops Foot Bridge (Tenn.)", "Chimney Tops Trail", "Clingmans Dome Road",
"Davenport Gap (Tenn.)", "Deals Gap (Tenn.)", "Dry Sluice Gap (Tenn.)", "Dry Valley (Tenn.)", "Elijah Oliver Place (Tenn.)",
"Fighting Creek Gap (Tenn.)", "Florida", "Fontana Dam (N.C.)", "Foothills Parkway", "Forge Creek", "Forney Ridge Parking Lot (N.C.)",
"Fort George Site", "Fort Manuel Site", "Fowler (Kan.)", "Gatlinburg (Tenn.)", "Greenbrier Pinnacle (Tenn.)", "Gregory Bald (Tenn.)",
"Guyot, Mount (Tenn.)", "Harrison, Mount (Tenn.)", "Headrick Chapel (Tenn.)", and many more.

For those :code:`geographic` names associated with :code:`geonames` through a URI, there is arguably no need to migrate the coordinates
as a string value as these can be retrieved using the URI at any time.

Justification
^^^^^^^^^^^^^

Having :code:`coordinates` to leverage support mapping and digital humanities projects. :code:`coordinates` increase the number of
ways in which our data can be used.

XPath
^^^^^

    :code:`subject/cartographics/coordinates`

Decision
^^^^^^^^

`Here's an example record - webster:1005 <https://digital.lib.utk.edu/collections/islandora/object/webster%3A1005/datastream/MODS/view>`_.

.. code-block:: xml

    <subject authority="geonames" valueURI="https://sws.geonames.org/4630912">
        <geographic>House Mountain</geographic>
        <cartographics>
            <coordinates>36.11175, -83.76657</coordinates>
        </cartographics>
    </subject>

All that is needed in this case is to bring over the URI.

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:spatial <https://sws.geonames.org/4630912> .

Given the extent of :code:`coordinates` that cannot be retrieved using a URI (120), a separate solution is needed to preserve these values.
`Here's an example record - derris:610 <https://digital.lib.utk.edu/collections/islandora/object/derris%3A610/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <geographic>Becky Cable House (Tenn.)</geographic>
        <cartographics>
            <coordinates>35.58546, -83.84444</coordinates>
        </cartographics>
    </subject>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:spatial <https://sws.geonames.org/4630912> ;
        dcterms:spatial "35.58546, -83.84444" .

Name values with roleTerms represented as subjects
--------------------------------------------------

Use Case
^^^^^^^^

The Arrowmont Simple Images collection includes :code:`subject/name/namePart` values with :code:`roleTerm`\ s. Something should
be treated as a :code:`subject` if it is represented within a photograph and treated as a name with a :code:`roleTerm` if the individual
listed is associated with the creation or provenance of the item depicted. As the :code:`name` values are currently represented
in the metadata, these two distinct categories are mixed. The only place where the two can overlap is if the name
is given a role of `"Depicted" - <https://id.loc.gov/vocabulary/relators/dpc>`_.

Justification
^^^^^^^^^^^^^

As the :code:`name`\ s are currently represented, they share incorrect information.

XPath
^^^^^

    :code:`mods/subject/name[role]`

Decision
^^^^^^^^

`Example record - arrsimple:344 <https://digital.lib.utk.edu/collections/islandora/object/arrsimple%3A344/datastream/MODS/view>`_
This record is particularly problematic because it both suggests that Aunt Lydia Whaley is the photographer and that the
photographer is unknown. This suggests that she cannot have the role of photographer. She may be depicted within the
photograph, but this is also unconfirmed. While more vague, the safest way to deal with these records is to drop the
:code:`roleTerm` and treat the :code:`name`\ s as general subjects. For this record, the inclusion of this :code:`subject` could mean that
Aunt Lydia is the woman depicted, but it could also reinforce the title (Aunt Lydia's cave by the creek). It is
ambiguous, but doesn't state anything that is clearly untrue.

.. code-block:: xml

    <subject authority="local">
        <name>
            <namePart>Whaley, Aunt Lydia.</namePart>
        <role>
            <roleTerm authority="marcrelator" valueURI="http://id.loc.gov/vocabulary/relators/pht">Photographer</roleTerm>
        </role>
        </name>
    </subject>
    <name>
        <namePart>Unknown</namePart>
        <role>
            <roleTerm authority="marcrelator" valueURI="http://id.loc.gov/vocabulary/relators/pht">Photographer</roleTerm>
        </role>
    </name>
    <title>Aunt Lydia's cave by the creek, Francisa.</title>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:subject "Whaley, Aunt Lydia" .

genre
=====
+-----------------+--------------------+------------------------------------------------------------------------------------+
| Predicate       | Value Type         |  Usage Notes                                                                       |
+=================+====================+====================================================================================+
| dcterms:type    | URI/String Literal |  Use for MODS genre values of 'cartographic' or 'notated music.' Also use when     |
|                 |                    |  genre[@authority='dct']= 'text', 'image', 'still image'.                          |
+-----------------+--------------------+------------------------------------------------------------------------------------+
| dcterms:subject | URI/String Literal |  Use for MODS genre values with an authority of 'aat' or 'lcsh'.                   |
+-----------------+--------------------+------------------------------------------------------------------------------------+
| edm:hasType     | URI/String Literal |  Use for MODS genre values without attributes that do not equal 'cartographic' OR  |
|                 |                    |  'notated music.' Also use when genre[@authority="lcgft"].                         |
+-----------------+--------------------+------------------------------------------------------------------------------------+

genre: values that map to dcterms:type
--------------------------------------

Use Case
^^^^^^^^

:code:`genre`, without any attributes, has been used as a catch-all descriptive element that may or may not hold values from a controlled vocabulary, and that may or may not provide appropriate descriptive information about the resource. :code:`genre[@authority='dct']` has three distinct values: "text", "still image", and "image", that broadly indicate the type of the resource being described.

Justification
^^^^^^^^^^^^^

For values *outside* of the following table, we selected the `edm:hasType` property as it aligns well with the possible overlap between :code:`genre` and :code:`physicalDescription/form`. To help prevent duplicating string literals and URIs, the following table suggests a mapping for a limited subset of the union of values in :code:`genre[not(@*)]` and :code:`genre[@authority='dct']`.

+-----------------------------------------------+---------------+--------------------------------------------------+--------------------+
| (//genre[not(@*] | //genre[@authority='dct']) | RDF Predicate | URI                                              | dcterms text value |
+-----------------------------------------------+---------------+--------------------------------------------------+--------------------+
| cartographic                                  | dcterms:type  | <http://id.loc.gov/vocabulary/resourceTypes/car> | Cartographic       |
+-----------------------------------------------+---------------+--------------------------------------------------+--------------------+
| image                                         | dcterms:type  | <http://id.loc.gov/vocabulary/resourceTypes/img> | Image              |
+-----------------------------------------------+---------------+--------------------------------------------------+--------------------+
| notated music                                 | dcterms:type  | <http://id.loc.gov/vocabulary/resourceTypes/not> | Notated music      |
+-----------------------------------------------+---------------+--------------------------------------------------+--------------------+
| still image                                   | dcterms:type  | <http://id.loc.gov/vocabulary/resourceTypes/img> | Still image        |
+-----------------------------------------------+---------------+--------------------------------------------------+--------------------+
| text                                          | dcterms:type  | <http://id.loc.gov/vocabulary/resourceTypes/txt> | Text               |
+-----------------------------------------------+---------------+--------------------------------------------------+--------------------+

XPaths
^^^^^^

:code:`genre[not(@*)][string() = 'cartographic']` OR

:code:`genre[not(@*)][string() = 'notated music']` OR

:code:`genre[@authority = 'dct'][string() = 'image']` OR

:code:`genre[@authority = 'dct'][string() = 'still image']` OR

:code:`genre[@authority = 'dct'][string() = 'text']`

Alternately, these XPaths can be notated as:
:code:`genre[(not(@*) and (string() = ('cartographic', 'notated music')) or (@authority = 'dct' and (string() = ('text', 'image', 'still image')))]`

Decision
^^^^^^^^

The `dcterms:type` property has been selected.

`Example record - volvoices:11551 <https://digital.lib.utk.edu/collections/islandora/object/volvoices:11551/datastream/MODS/view>`_

.. code-block:: xml

    <genre>notated music</genre>
    <genre>sheet music</genre>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/> .
    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> edm:hasType "sheet music" ;
        dcterms:type <http://id.loc.gov/vocabulary/resourceTypes/not> .

`Example record - volvoices:11262 <https://digital.lib.utk.edu/collections/islandora/object/volvoices:11262/datastream/MODS/view>`_

.. code-block:: xml

    <genre>notated music</genre>
    <genre authority="dct">still image</genre>
    <genre>sheet music</genre>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/> .
    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> edm:hasType "sheet music" ;
        dcterms:type <http://id.loc.gov/vocabulary/resourceTypes/not> ;
        dcterms:type <http://id.loc.gov/vocabulary/resourceTypes/img> .

genre values that map to edm:hasType
------------------------------------

Use Case
^^^^^^^^

:code:`genre[not(@*)]` has been used a catch-all descriptive element that may or may not hold values from a controlled vocabulary, and that may or may not provide appropriate descriptive information about the resource.

Justification
^^^^^^^^^^^^^

The values in this XPath fall outside of the table presented in the preceding section ("genre values that map to dcterms:type").

XPath
^^^^^

:code:`genre[not(@*) and not(string() = ('cartographic','notated music'))]`

Decision
^^^^^^^^

Use the `edm:hasType` property for these values.

`Example record - volvoices:3827 <https://digital.lib.utk.edu/collections/islandora/object/volvoices:3827/datastream/MODS/content>`_

.. code-block:: xml

    <genre>Hogsheads</genre>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/> .

    <https://example.org/objects/1> edm:hasType "Hogsheads" .

genre[@authority='aat']
-----------------------

Use Case
^^^^^^^^

:code:`genre[@authority='aat']` appears in the Archivision collection and uses a controlled vocabulary.

Justification
^^^^^^^^^^^^^

These will be treated as `dcterms:subject`, based on the values from the AAT controlled vocabulary.

XPath
^^^^^

:code:`genre[@authority='aat']`

Decision
^^^^^^^^

The `dcterms:subject` property was selected.

`Example record - archivision:404 <https://digital.lib.utk.edu/collections/islandora/object/archivision:404/datastream/MODS/view>`_
.. code-block:: xml

    <genre authority="aat" valueURI="http://vocab.getty.edu/aat/300021140">Renaissance</genre>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/object/1> dcterms:subject <http://vocab.getty.edu/aat/300021140> .

genre[@authority='lcsh']
------------------------

Use Case
^^^^^^^^

Used in the Archivision, Charlie Daniels, and AirScoop collections. There are four distinct values in the XPath: "Editorial cartoons", "College student newspapers and periodicals", "Twentieth century", and "Nineteenth century".

Justification
^^^^^^^^^^^^^

XPath
^^^^^

:code:`genre[@authority='lcsh']`

Decision
^^^^^^^^

The `dcterms:subject` property was selected.

`Example record - cDanielCartoon:455 <https://digital.lib.utk.edu/collections/islandora/object/cDanielCartoon:455/datastream/MODS/view>`_.

.. code-block:: xml

    <genre authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85040974">Editorial cartoons</genre>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/> .

    <https://example.org/object/1> edm:hasType <http://id.loc.gov/authorities/subjects/sh85040974> .

and `archivision:1754 <https://digital.lib.utk.edu/collections/islandora/object/archivision:1754/datastream/MODS/view>`_.

.. code-block:: xml

    <genre authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85139020">Twentieth century</genre>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/> .

    <https://example.org/object/1> edm:hasType <http://id.loc.gov/authorities/subjects/sh85040974> .

genre[@authority='lcgft']
-------------------------

Use Case
^^^^^^^^

This :code:`genre` element is used in the Arrowmont, Van Vactor, VP Moore, and Kefauver Crime Documents collections.

Justification
^^^^^^^^^^^^^

XPath
^^^^^

:code:`genre[@authority='lcgft']`

Decision
^^^^^^^^

The `edm:hasType` property was selected.

`Example record - ekcd:611 <https://digital.lib.utk.edu/collections/islandora/object/ekcd:611/datastream/MODS/view>`_

.. code-block:: xml

    <genre authority="lcgft" valueURI="http://id.loc.gov/authorities/genreForms/gf2014026131">Newsletters</genre>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/> .

    <https://example.org/object/1> edm:hasType <http://id.loc.gov/authorities/genreForms/gf2014026131> .

`Example record - vpmoore:50 <https://digital.lib.utk.edu/collections/islandora/object/vpmoore:50/datastream/MODS/view>`_

.. code-block:: xml

    <genre authority="lcgft" authorityURI="http://id.loc.gov/authorities/genreForms" valueURI="http://id.loc.gov/authorities/genreForms/gf2014026173">Scrapbooks</genre>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/> .

    <https://example.org/object/1> edm:hasType <http://id.loc.gov/authorities/genreForms/gf2014026173> .

genre[@authority='lcmpt']
-------------------------

Use Case
^^^^^^^^

This XPath is used in the Van Vactor collection to express performance medium and instrumentation information.

Justification
^^^^^^^^^^^^^

XPath
^^^^^

:code:`genre[@authority='lcmpt']`

Decision
^^^^^^^^

The `dcterms:subject` property was selected.

`Example record - vanvactor:12350 <https://digital.lib.utk.edu/collections/islandora/object/vanvactor:12350/datastream/MODS/view>`_

.. code-block:: xml

    <genre authority="lcmpt" valueURI="http://id.loc.gov/authorities/performanceMediums/mp2013015074">bassoon</genre>
    <genre authority="lcmpt" valueURI="http://id.loc.gov/authorities/performanceMediums/mp2013015342">horn</genre>
    <genre authority="lcmpt" valueURI="http://id.loc.gov/authorities/performanceMediums/mp2013015748">trumpet</genre>
    <genre authority="lcmpt" valueURI="http://id.loc.gov/authorities/performanceMediums/mp2013015540">percussion</genre>
    <genre authority="lcgft" valueURI="http://id.loc.gov/authorities/genreForms/gf2014027156">Variations (Music)</genre>
    <genre authority="lcgft" valueURI="http://id.loc.gov/authorities/genreForms/gf2014026956">Musical sketches</genre>
    <genre authority="lcgft" valueURI="http://id.loc.gov/authorities/genreForms/gf2014026097">Excerpts</genre>
    <genre authority="lcgft" valueURI="http://id.loc.gov/authorities/subjects/sh99001779">Scores</genre>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/object/1>
        dcterms:subject <http://id.loc.gov/authorities/performanceMediums/mp2013015074> ;
        dcterms:subject <http://id.loc.gov/authorities/performanceMediums/mp2013015342> ;
        dcterms:subject <http://id.loc.gov/authorities/performanceMediums/mp2013015748> ;
        dcterms:subject <http://id.loc.gov/authorities/performanceMediums/mp2013015540> ;
        dcterms:type <http://id.loc.gov/authorities/genreForms/gf2014027156> ;
        dcterms:type <http://id.loc.gov/authorities/genreForms/gf2014026956> ;
        dcterms:type <http://id.loc.gov/authorities/genreForms/gf2014026097> ;
        dcterms:type <http://id.loc.gov/authorities/subjects/sh99001779> .

genre[not(text())]
------------------

Use Case
^^^^^^^^

Empty :code:`genre` elements should not be migrated.

Justification
^^^^^^^^^^^^^

XPath
^^^^^

:code:`genre[not(text())]`

Decision
^^^^^^^^

Do not migrate.

..code-block:: xml
    <genre valueURI=""/>

..code-block:: xml
    <genre authority="lcgft" authorityURI="http://id.loc.gov/authorities/genreForms"/>

language
========

+-----------------------------------+----------------+-------------------------------------------------------------------------+
| Predicate                         | Value Type     | Usage Notes                                                             |
+===================================+================+=========================================================================+
| dcterms:language                  | URI            | The language of the resource. Preference is to use a                    |
|                                   |                | value from a controlled vocabulary, such as ISO 639-2.                  |
+-----------------------------------+----------------+-------------------------------------------------------------------------+

item has one language
---------------------

Use Case
^^^^^^^^

Single instance of :code:`languageTerm` where item language is known. Many of our resources will have one instance of a
:code:`language` element with a single subelement of :code:`languageTerm`. The :code`type` attribute for :code:`languageTerm` may be either
"text" or "code".

Justification
^^^^^^^^^^^^^

Both Samvera and Islandora handle this case similarly, directly mapping the URI, however, Islandora does offer an
alternative with additional minting of objects required. We will opt to go with the cleanest possible route of direct
mapping to the controlled vocabulary, ISO 639-2, and avoid minting new objects.

XPath
^^^^^

:code:`language/languageTerm[@type="text"]` OR

:code:`language/languageTerm[@type="code"]`

Decision
^^^^^^^^

https://digital.lib.utk.edu/collections/islandora/object/tatum%3A188/datastream/MODS/view

.. code-block:: xml

    <language>
        <languageTerm authority="iso639-2b" type="text">English</languageTerm>
    </language>

https://digital.lib.utk.edu/collections/islandora/object/ekcd:9/datastream/MODS/view

.. code-block:: xml

    <language>
        <languageTerm authority="iso639-2b" type="code">eng</languageTerm>
    </language>

Turtle would map the same in both cases.

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:language <http://id.loc.gov/vocabulary/iso639-2/eng> .

"No linguistic content" cases can be found across some of our resources. In these cases, a :code:`code` attribute is present with a "zxx"
value or :code:`type` attribute with a *text* value, and the :code:`languageTerm` element has a value of "No linguistic content". Justifications from the single :code:`language` case above also apply here. These are handled just like other languages in ISO 639-2 Collection of Bibliographic Codes. In this case, the "zxx" code denotes a declared absence of linguistic information.

https://digital.lib.utk.edu/collections/islandora/object/tdh:911/datastream/MODS/view

.. code-block:: xml

    <language>
        <languageTerm authority="iso639-2b" type="text">No linguistic content</languageTerm>
    </language>

https://digital.lib.utk.edu/collections/islandora/object/tdh:911/datastream/MODS/view

.. code-block:: xml

    <language>
        <languageTerm type="code" authority="iso639-2b">zxx</languageTerm>
    </language>

Turtle would map the same in both cases.

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:language <http://id.loc.gov/vocabulary/iso639-2/zxx> .

item has multiple languages
---------------------------

Use Case
^^^^^^^^

Multiple instances of a :code:`languageTerm` present. In very few cases (13 total), multiple :code:`language`\ s can be found for an item.
In all cases, :code:`language`\ s are assigned a known authority, with the :code:`type` attribute's value as "text: or "code".

Justification
^^^^^^^^^^^^^

Similar to items with one :code:`language`, URIs are directly mapped in the Samvera recommendations. Islandora does not have
recommendations for this use case. We could separate :code:`language`\ s onto new lines with a duplicate predicate. However,
as style choice and to simplify in mapped turtle, multiple :code:`language`\ s in our items will be delineated by a comma.
Justifications from the single :code:`language` case also apply here.

XPath
^^^^^

:code:`language/languageTerm[@type="text"]` OR

:code:`language/languageTerm[@type="code"]`

Decision
^^^^^^^^

https://digital.lib.utk.edu/collections/islandora/object/utsmc:725/datastream/MODS/view

.. code-block:: xml

    <language>
        <languageTerm authority="iso639-2b" type="text">French</languageTerm>
    </language>
    <language>
        <languageTerm authority="iso639-2b" type="text">Italian</languageTerm>
    </language>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1>
        dcterms:language <http://id.loc.gov/vocabulary/iso639-2/fre> , <http://id.loc.gov/vocabulary/iso639-2/ita> .

typeOfResource
==============

+--------------+------------+-----------------------------------------------------------+
| Predicate    | Value Type | Usage Notes                                               |
+==============+============+===========================================================+
| dcterms:type | URI        | Use with a type from a controlled vocabulary (such as the |
|              |            | LoC Resource Types Scheme or DCMI Type                    |
|              |            | Vocabulary).                                              |
+--------------+------------+-----------------------------------------------------------+

typeOfResource with no attributes
---------------------------------

Use case
^^^^^^^^

Most records currently have a :code:`typeOfResource` value with no attributes. Depending on the item being described, it is possible
for there to be multiple :code:`typeOfResource` values in a single record. The Islandora Metadata Interest Group has carefully
created a mapping to translate MODS :code:`typeOfResource` values to `dcterms` resource types. A selection of the mapping is
included below that addresses all of the values UTK has within its metadata. Note that the final row, collection="yes"
is addressed in a subsequent category.

+----------------------------+---------------+--------------------------------------------------+--------------------+
|                            | RDF Predicate | RDF Value                                        | dcterms text value |
| MODS typeOfResource        |               |                                                  |                    |
+----------------------------+---------------+--------------------------------------------------+--------------------+
| text                       | dcterms:type  | <http://id.loc.gov/vocabulary/resourceTypes/txt> | Text               |
+----------------------------+---------------+--------------------------------------------------+--------------------+
| cartographic               | dcterms:type  | <http://id.loc.gov/vocabulary/resourceTypes/car> | Cartographic       |
+----------------------------+---------------+--------------------------------------------------+--------------------+
| notated music              | dcterms:type  | <http://id.loc.gov/vocabulary/resourceTypes/not> | Notated music      |
+----------------------------+---------------+--------------------------------------------------+--------------------+
| sound recording-nonmusical | dcterms:type  | <http://id.loc.gov/vocabulary/resourceTypes/aun> | Audio non-musical  |
+----------------------------+---------------+--------------------------------------------------+--------------------+
| sound recording            | dcterms:type  | <http://id.loc.gov/vocabulary/resourceTypes/aud> | Audio              |
+----------------------------+---------------+--------------------------------------------------+--------------------+
| still image                | dcterms:type  | <http://id.loc.gov/vocabulary/resourceTypes/img> | Still image        |
+----------------------------+---------------+--------------------------------------------------+--------------------+
| moving image               | dcterms:type  | <http://id.loc.gov/vocabulary/resourceTypes/mov> | Moving image       |
+----------------------------+---------------+--------------------------------------------------+--------------------+
| three dimensional object   | dcterms:type  | <http://id.loc.gov/vocabulary/resourceTypes/art> | Artifact           |
+----------------------------+---------------+--------------------------------------------------+--------------------+
| collection="yes"           | dcterms:type  | <http://id.loc.gov/vocabulary/resourceTypes/col> | Collection         |
+----------------------------+---------------+--------------------------------------------------+--------------------+

Justification
^^^^^^^^^^^^^

Values within :code:`typeOfResource` are used for initial faceting in search for both UTK's local digital collections website
and for DPLA's interface. As DPLA doesn't display :code:`physicalDescription/form` values, it is important to share this
less granular indication of the resource type.

XPath
^^^^^

:code:`typeOfResource`

Decision
^^^^^^^^

Here's an `example record - vanvactor:1 <https://digital.lib.utk.edu/collections/islandora/object/vanvactor%3A1/datastream/MODS/view>`_.

.. code-block:: xml

    <typeOfResource collection="yes">notated music</typeOfResource>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:type <http://id.loc.gov/vocabulary/resourceTypes/not> .

typeOfResource with @collection="yes"
-------------------------------------

Use case
^^^^^^^^

In MODS, an attribute can be used on :code:`typeOfResource` to indicate that the record refers to an entire collection rather
than an individual resource. This is useful because it makes it possible to distinguish between object and collection
records in the catalog so that patrons understand more quickly how much content is associated with the record. The
Islandora Metadata Interest Group has come up with the solution of using the `dcterms` resource type of "Collection." In
this situation we will need multiple triples to preserve the information currently present - one for indicating the record is
for a collection and one (or more) for indicating prevalent resource type(s) in the collection. In MODS :code:`typeOfResource` is
a repeatable field. Note that we will need to make sure that we do not repeat the :code:`collection` resource type in cases
where there are multiple :code:`typeOfResource[@collection="yes"]` instances.

+----------------------------+---------------+--------------------------------------------------+--------------------+
| collection="yes"           | dcterms:type  | <http://id.loc.gov/vocabulary/resourceTypes/col> | Collection         |
+----------------------------+---------------+--------------------------------------------------+--------------------+

Justification
^^^^^^^^^^^^^

We need to be able to distinguish between an item and collection resource, so retaining this information is necessary.

XPath
^^^^^

:code:`typeOfResource[@collection="yes"]`

Decision
^^^^^^^^

Here's a complex example that includes two :code:`typeOfResource` values - `gsmrc:smhc <https://digital.lib.utk.edu/collections/islandora/object/gsmrc%3Asmhc/datastream/MODS/view>`_.

.. code-block:: xml

    <typeOfResource collection="yes">text</typeOfResource>
    <typeOfResource collection="yes">still image</typeOfResource>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:type <http://id.loc.gov/vocabulary/resourceTypes/col> ;
        dcterms:type <http://id.loc.gov/vocabulary/resourceTypes/txt> ;
        dcterms:type <http://id.loc.gov/vocabulary/resourceTypes/img> .

Missing typeOfResource value
----------------------------

Use case
^^^^^^^^

Currently 9,993 records are missing a :code:`typeOfResource` value. The affected collections include Volunteer Voices (not entire
collection), Roth, the Howard Baker Speeches and Remarks, Great Smoky Mountains Colloquy, and the Great Smoky Mountains Postcard Collection. We can consider if we would like to apply a blanket value to a collection at the time of migration. For monolithic collections like Roth and Baker, this would be easy to achieve (`roth = "still image"` and `baker = "text"` in MODS). For collections with varied formats, like Volunteer Voices, this will not be possible.

Justification
^^^^^^^^^^^^^

Given that the Digital Collections home page currently uses :code:`typeOfResource` to initially limit searches, it would be
beneficial for this value to be more consistently present. It would also assist with discovery in DPLA.

XPath
^^^^^

:code:`not(typeOfResource)`

Decision
^^^^^^^^

During or post migration we will plan to add :code:`typeOfResource` on a collection basis if possible. See the chart below for decisions.

+----------------------------+---------------------------------------------------+
| collection PID             | dcterms:type                                      |
+----------------------------+---------------------------------------------------+
| colloquy                   | <http://id.loc.gov/vocabulary/resourceTypes/txt>  |
+----------------------------+---------------------------------------------------+
| hbs                        | <http://id.loc.gov/vocabulary/resourceTypes/txt>  |
+----------------------------+---------------------------------------------------+
| pcard00                    | <http://id.loc.gov/vocabulary/resourceTypes/img>  |
+----------------------------+---------------------------------------------------+
| roth                       | <http://id.loc.gov/vocabulary/resourceTypes/img>  |
+----------------------------+---------------------------------------------------+
| volvoices                  | cannot assign blanket value                       |
+----------------------------+---------------------------------------------------+

Here's an example record with no :code:`typeOfResource` value - `roth:100 <https://digital.lib.utk.edu/collections/islandora/object/roth%3A100/datastream/MODS/view>`_.

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:type <http://id.loc.gov/vocabulary/resourceTypes/img> .

classification
==============

+------------------+------------+---------------------------------------------------------+
| Predicate        | Value Type | Usage Notes                                             |
+------------------+------------+---------------------------------------------------------+
| classSchemes:lcc | Literal    | Use for values from Library of Congress Classification. |
+------------------+------------+---------------------------------------------------------+

Use case
--------

Some of our resources have already been formally cataloged and have a :code:`classification` number. When these are available,
they are included in the MODS metadata. Serials like the Alumnus and many of the Athletics media guides are good examples.
Some collections, like the University of Tennessee Commencements collection include full :code:`shelfLocator`\ s in the :code:`classification`
field (e.g. LD5297 .U55 2013). These should be edited before migration.

Justification
-------------

This information is helpful to include as it provides information about where the physical item is shelved (though this
is not a complete :code:`shelfLocator`) and the broad subject the materials relate to.

XPath
-----

:code:`classification[@authority="lcc"]` OR

:code:`classification`

Decision
--------

`Example record without authority - tenngirl:977 <https://digital.lib.utk.edu/collections/islandora/object/tenngirl:977/datastream/MODS>`_

.. code-block:: xml

    <classification>LD5296 .W6</classification>

`Example record with authority - agrtfhs:2275 <https://digital.lib.utk.edu/collections/islandora/object/agrtfhs:2275/datastream/MODS>`_

.. code-block:: xml

    <classification authority="lcc">S1 .T43</classification>

.. code-block:: turtle

    @prefix classSchemes: <http://id.loc.gov/vocabulary/classSchemes/> .

        <https://example.org/objects/1> classSchemes:lcc "S1 .T43" .

part
====

Use Case
--------

The MODS :code:`part` element is infrequently used to describe a portion of a larger resource. In UTK's metadata, :code:`part` is used
in two collections - Great Smoky Mountains Colloquy and Sanborn Fire Insurance Map Collection.

Justification
-------------

Ultimately it was decided that this information is not important to keep because it is already present in the title field
in both instances. With the Sanborn maps there is a difference between how the :code:`part` is named - Sheet versus District-Ward,
but it was not felt strongly that any additional remediation needed to be done.

XPath
-----

:code:`part`

Decision
--------

Drop all values in :code:`part`.

`Example record - sanborn:1237 <https://digital.lib.utk.edu/collections/islandora/object/sanborn:1237/datastream/MODS>`_

.. code-block:: xml

    <titleInfo>
        <title>Knoxville -- 1917</title>
        <partName>Sheet 99</partName>
    </titleInfo>
    <part>
        <detail>
                <title>District-Ward 99</title>
        </detail>
    </part>


relatedItem
===========

+-------------------------------+--------------------+-------+--------------------------------------------------------------------------------------------+
| Predicate                     | Value Type         | Range | Use Case                                                                                   |
+-------------------------------+--------------------+-------+--------------------------------------------------------------------------------------------+
| dcterms:bibliographicCitation | String Literal     | N/A   | A String Literal of the bibliographic citation for the resource.                           |
+-------------------------------+--------------------+-------+--------------------------------------------------------------------------------------------+
| dcterms:tableOfContents       | String Literal     | N/A   | A String Literal that represents constituent parts of a resource.                          |
+-------------------------------+--------------------+-------+--------------------------------------------------------------------------------------------+
| dcterms:hasVersion            | URI                | N/A   | A String Literal that represents constituent parts of a resource.                          |
+-------------------------------+--------------------+-------+--------------------------------------------------------------------------------------------+
| dbo:collection                | String Literal     | N/A   | A String Literal that represents the physical archival collection the resource belongs to. |
+-------------------------------+--------------------+-------+--------------------------------------------------------------------------------------------+
| dbo:isPartOf                  | URI                | N/A   | A URI that represents the physical archival collection a resource belongs to.              |
+-------------------------------+--------------------+-------+--------------------------------------------------------------------------------------------+
| opaque:sheetMusic_hostItem    | URI/String Literal | N/A   | A URI or String Literal that indicates the host item for the resource being described.     |
+-------------------------------+--------------------+-------+--------------------------------------------------------------------------------------------+
| relators:[term]               | URI/String Literal | N/A   | Use with a role from MARC Code List of Relators role terms.                                |
|                               |                    |       | Value is either text or URI from a controlled vocabulary (like                             |
|                               |                    |       | Library of Congress Name Authority File).                                                  |
+-------------------------------+--------------------+-------+--------------------------------------------------------------------------------------------+

relatedItem - do not migrate
----------------------------

Use Case
^^^^^^^^

:code:`relatedItem`, with and without attributes, is used in a number of collections to express structural relationships. Currently, values in this XPath are displayed in both search/browse facets and the item-level metadata display. Post-migration, we will need to consider how to express these relationships in our next-gen DAMS.

Justification
^^^^^^^^^^^^^

These relationships will be handled/expressed by default behavior in our next-gen DAMS. In the case of :code:`relatedItem/abstract`, the values present should be handled at the collection level.

XPath
^^^^^

:code:`relatedItem[not(@*)]` OR

:code:`relatedItem[@type='host'][@displayLabel[matches(., 'project') or matches(., 'Project') or matches(., 'Digital Collection') or matches(., 'Project Part') or matches(., 'Is Part Of')]` OR

:code:`relatedItem/abstract` OR

:code:`relatedItem[@displayLabel='Featured Item']`

Decision
^^^^^^^^

Do not migrate.

`Example record - relatedItem[not(@)]: volvoices:11925 <https://digital.lib.utk.edu/collections/islandora/object/volvoices:11925/datastream/MODS/content>`_

.. code-block:: xml

    <relatedItem>
      <titleInfo>
        <title>Digital Collection: The Growth of Democracy in Tennessee: A Grassroots Approach to Volunteer Voices</title>
      </titleInfo>
    </relatedItem>

`Example record - relatedItem[@displayLabel='Project'][@type='host'] - roth:3346 <https://digital.lib.utk.edu/collections/islandora/object/roth:3346/datastream/MODS/view>`_

.. code-block:: xml

    <relatedItem displayLabel="Project" type="host">
      <titleInfo>
        <title>Albert "Dutch" Roth Photograph Collection</title>
      </titleInfo>
    </relatedItem>

`Example record - relatedItem[@displayLabel='project'][@type='host'] - thompson:1 <https://digital.lib.utk.edu/collections/islandora/object/thompson:1/datastream/MODS/view>`_

.. code-block:: xml

    <relatedItem type="host" displayLabel="project">
      <titleInfo>
        <title>Thompson Brothers Commercial Photographers</title>
      </titleInfo>
    </relatedItem>

`Example record - relatedItem[@displayLabel='Digital Collection'][@type='host'] - cdf:7850 <https://digital.lib.utk.edu/collections/islandora/object/cdf:7850/datastream/MODS/view>`_. Synonymous with `@displayLabel = "Project"`.

.. code-block:: xml

    <relatedItem displayLabel="Digital Collection" type="host">
      <titleInfo>
        <title>Children's Defense Fund</title>
      </titleInfo>
    </relatedItem>

`Example record - relatedItem[@displayLabel='Project Part'][@type='host'] - arrow:167 <https://digital.lib.utk.edu/collections/islandora/object/arrow:167/datastream/MODS/view>`_.

.. code-block:: xml

    <relatedItem type="host" displayLabel="Project">
      <titleInfo>
        <title>From Pi Beta Phi to Arrowmont</title>
      </titleInfo>
    </relatedItem>
    <relatedItem displayLabel="Project Part" type="host">
      <titleInfo>
        <title>The Arrow of Pi Beta Phi</title>
      </titleInfo>
    </relatedItem>
    <relatedItem displayLabel="Bibliographic Citation" type="host">
      <titleInfo>
        <title>The Arrow, Volume 61, Number 4</title>
      </titleInfo>
    </relatedItem>

`Example record - relatedItem[@displayLabel='Featured Item'] - collections:mugwump <https://digital.lib.utk.edu/collections/islandora/object/collections:mugwump/datastream/MODS/view>`_.

.. code-block:: xml

    <relatedItem displayLabel="Featured Item">
      <titleInfo>
        <title>Mugwump, volume 11, number 6</title>
      </titleInfo>
      <identifier type="pid">mugwump:3380</identifier>
      <abstract>Monthly student publication that highlights student life issues, sports, literary critiques, poetry, as well as cartoons and art work.</abstract>
      <originInfo>
        <dateIssued>March 1931</dateIssued>
      </originInfo>
    </relatedItem>

relatedItem[@type='host'][@displayLabel='Collection']
-----------------------------------------------------

Use Case
^^^^^^^^

This XPath is used to indicate the resource's archival collection.

Justification
^^^^^^^^^^^^^

We use these values for search/browse facets, as well as item-level metadata display. Additionally, collection titles are shared with DPLA.

XPath
^^^^^

:code:`relatedItem[@type='host'][@displayLabel='Collection']`

Decision
^^^^^^^^

The `dbo:collection` property was selected.

`Example record - heilman:261 <https://digital.lib.utk.edu/collections/islandora/object/heilman:261/datastream/MODS/view>`_

.. code-block:: xml

    <relatedItem type="host" displayLabel="Project">
      <titleInfo>
        <title>Botanical Photography of Alan S. Heilman</title>
      </titleInfo>
    </relatedItem>
    <relatedItem type="host" displayLabel="Collection">
      <titleInfo>
        <title>Botany Department Photographs</title>
      </titleInfo>
      <identifier type="local">AR.0488</identifier>
    </relatedItem>

.. code-block:: turtle

    @prefix dbo: <http://dbpedia.org/ontology/> .

    <https://example.org/objects/1> dbo:collection "Botany Department Photographs, AR.0488" .

relatedItem[@type='series'][@displayLabel='Project']
----------------------------------------------------

Use Case
^^^^^^^^

The `@type='series'` XPath indicates a resource's archival series.

Justification
^^^^^^^^^^^^^

We decided not to migrate to be consistent with how we are approaching other parts of metadata relating back to a resource's archival collection. We are not migrating box and folder information, so we will not migrate series information either.

XPath
^^^^^

:code:`relatedItem[@type='series'][@displayLabel='Project']`

Decision
^^^^^^^^

Do not migrate.

`Example record - roth:1538 <https://digital.lib.utk.edu/collections/islandora/object/roth:1538/datastream/MODS/view>`_

.. code-block:: xml

    <relatedItem type="series" displayLabel="Project">
      <titleInfo>
        <title>Series II: Margaret Ann Roth Photographs and Other Materials, 1947 March 11-2002 December 14 (bulk 1947 March 11-1955 March 20). Sub-Series A: Photographs, 1947 March 11-1955 March 139</title>
      </titleInfo>
    </relatedItem>
    <relatedItem displayLabel="Collection" type="host">
      <titleInfo>
        <title>A. G. "Dutch" and Margaret Ann  Roth  Papers</title>
      </titleInfo>
      <identifier>MS.3334</identifier>
    </relatedItem>
    <relatedItem displayLabel="Project" type="host">
      <titleInfo>
        <title>Albert "Dutch" Roth Photograph Collection</title>
      </titleInfo>
    </relatedItem>

relatedItem[@type='host'][@displayLabel='Bibliographic Citation']
-----------------------------------------------------------------

Use Case
^^^^^^^^

This XPath only appears 1264 times in the Arrowmont Collection, specifically the Arrow of Pi Beta Phi sub-collection.

Justification
^^^^^^^^^^^^^

XPath
^^^^^

:code:`relatedItem[@type='host'][@displayLabel='Bibliographic Citation']`

Decision
^^^^^^^^

The `dcterms:bibliographicCitation` predicate was selected for these values.

`Example record - arrow:1 <https://digital.lib.utk.edu/collections/islandora/object/arrow:1/datastream/MODS/view>`_

.. code-block:: xml

    <relatedItem type="host" displayLabel="Project">
      <titleInfo>
        <title>From Pi Beta Phi to Arrowmont</title>
      </titleInfo>
    </relatedItem>
    <relatedItem displayLabel="Project Part" type="host">
      <titleInfo>
        <title>The Arrow of Pi Beta Phi</title>
      </titleInfo>
    </relatedItem>
    <relatedItem displayLabel="Bibliographic Citation" type="host">
      <titleInfo>
        <title>The Arrow, Volume 27, Number 1</title>
      </titleInfo>
    </relatedItem>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:bibliographicCitation "The Arrow, Volume 27, Number 1" .

relatedItem[@type="otherVersion"]
---------------------------------

Use Case
^^^^^^^^

:code:`relatedItem[@type="otherVersion"]` is used to indicate identifying information about another version of the resource. It appears in the Van Vactor and Arrowmont metadata; it is used, respectively, to identify an alternate version of the sheet music or the scrapbook that holds the image.

Justification
^^^^^^^^^^^^^

XPath
^^^^^

:code:`relatedItem[@type='otherVersion']/identifier` OR

:code:`relatedItem[@type='otherVersion']/location/url`

Decision
^^^^^^^^

See the following section on :code:`relatedItem/identifier[@type]`.

The XPath :code:`relatedItem[@type='otherVersion']/location/url` will not be migrated. Because it provides a link back to the hosting scrapbook, we will not be able to migrate this specific XPath. This will need to be a post-migration metadata update.

`Example record - arrpgimg:319 <https://digital.lib.utk.edu/collections/islandora/object/arrpgimg:319/datastream/MODS/view>`_

.. code-block:: xml

    <relatedItem type="otherVersion">
      <titleInfo>
         <title>Gaitlinburg from All Sides</title>
      </titleInfo>
      <location>
         <url>https://digital.lib.utk.edu/collections/islandora/object/arrowmont%3A16</url>
      </location>
    </relatedItem>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:hasVersion <uri-of-source-scrapbook-in-new-system> .

relatedItem/identifier[@type = 'local']
---------------------------------------

Use Case
^^^^^^^^

This XPath's attribute value (:code:`local`) is used to indicate the manuscript number associated with the resource's archival collection.

Justification
^^^^^^^^^^^^^

While we have decided to ignore granular archival metadata (e.g. box/folder or series information), migrating a known manuscript number gives us the ability to link back to the resource's finding aid.

XPath
^^^^^

:code:`relatedItem/identifier[@type='local']`

Decision
^^^^^^^^

:code:`@type='local'`\ 's value, if present, maps in to the `dbo:collection` property.

`Example record - heilman:26 <https://digital.lib.utk.edu/collections/islandora/object/heilman:261/datastream/MODS/view>`_

.. code-block:: xml

    <relatedItem type="host" displayLabel="Collection">
      <titleInfo>
        <title>Botany Department Photographs</title>
      </titleInfo>
      <identifier type="local">AR.0488</identifier>
    </relatedItem>

.. code-block:: turtle

    @prefix dbo: <http://dbpedia.org/ontology/> .

    <https://example.org/objects/1> dbo:collection "Botany Department Photographs, AR.0488" .

relatedItem/identifier[@type = 'catalog']
-----------------------------------------

Use Case
^^^^^^^^

:code:`@type='catalog'` is used exclusively in the Van Vactor collection to indicate the identifying number for an alternate version of the score.

Justification
^^^^^^^^^^^^^

This XPath provides contextual data for users.

XPath
^^^^^

:code:`relatedItem/identifier[@type='catalog']`

Decision
^^^^^^^^

:code:`@type='catalog'`\ 's value, if present, will be represented by the `opaque:sheetmusic_hostItem` property.

`Example record - vanvactor:10012 <https://digital.lib.utk.edu/collections/islandora/object/vanvactor:10012/datastream/MODS/view>`_

.. code-block:: xml

    <relatedItem type="otherVersion">
      <titleInfo>
        <title>Three songs for soprano, alto flute, English horn, and bass clarinet</title>
      </titleInfo>
      <identifier type="catalog">M120</identifier>
    </relatedItem>
    <relatedItem displayLabel="Project" type="host">
      <titleInfo>
        <title>David Van Vactor Music Collection</title>
      </titleInfo>
    </relatedItem>
    <relatedItem displayLabel="Collection" type="host">
      <titleInfo>
        <title>David Van Vactor Papers</title>
      </titleInfo>
      <identifier>MS.1942</identifier>
      <location>
        <url>https://n2t.net/ark:/87290/v8pz5703</url>
      </location>
    </relatedItem>

.. code-block:: turtle

    @prefix dbo: <http://dbpedia.org/ontology/> .
    @prefix opaque: <http://opaquenamespace.org/ns/> .

    <https://example.org/objects/1> dbo:collection "David Van Vactor Papers, MS.1942" ;
        dbo:isPartOf <https://n2t.net/ark:/87290/v8pz5703> ;
        opaque:sheetmusic_hostItem "Three songs for soprano, alto flute, English horn, and bass clarinet, M120" .

relatedItem/identifier[@type = 'pid']
-------------------------------------

Use Case
^^^^^^^^

:code:`@type='pid'` is used in collection-level records to indicate featured items and should not be migrated.

Justification
^^^^^^^^^^^^^

We will determine alternate ways of modeling featured item metadata post-migration.

XPath
^^^^^

:code:`relatedItem/identifier[@type='pid']`

Decision
^^^^^^^^
Do not migrate.

`Example record - collections:knoxgardens <https://digital.lib.utk.edu/collections/islandora/object/collections:knoxgardens/datastream/MODS/view>_`

.. code-block:: xml

    <relatedItem displayLabel="Featured Item">
        <titleInfo>
            <title>Mrs. Hazz's Dogwoods</title>
        </titleInfo>
        <identifier type="pid">knoxgardens:133</identifier>
        <abstract>Glass slide of Dogwoods in a garden.</abstract>
        <originInfo>
            <dateCreated>1927-1935</dateCreated>
        </originInfo>
    </relatedItem>

relatedItem/location/url
------------------------

Use Case
^^^^^^^^

This XPath is used 8516 times, but only has 33 distinct strings.

Justification
^^^^^^^^^^^^^

This value is used to highlight the archival collection related to the resource being described. Its availability encourages users to further explore the archival collection by giving them a link to the finding aid.

XPath
^^^^^

:code:`relatedItem/location/url`

Decision
^^^^^^^^

The `dbo:isPartOf` property was selected.

`Example record - ruskin:204 <https://digital.lib.utk.edu/collections/islandora/object/ruskin:204/datastream/MODS/view>`_

.. code-block:: xml

    <relatedItem displayLabel="Collection" type="host">
      <titleInfo>
        <title>Ruskin Cooperative Association Collection</title>
      </titleInfo>
      <identifier>MS.0023</identifier>
      <location>
        <url>https://n2t.net/ark:/87290/v81g0jf1</url>
      </location>
    </relatedItem>

.. code-block:: turtle

    @prefix dbo: <http://dbpedia.org/ontology/> .

    <https://example.org/objects/1> dbo:isPartOf <https://n2t.net/ark:/87290/v81g0jf1> ;
        dbo:collection "Ruskin Cooperative Association Collection, MS.0023" .

relatedItem/location/physicalLocation/
--------------------------------------

Use Case
^^^^^^^^

This XPath is used once in the Charles Dabney collection. It provides an :code:`authority`, a :code:`valueURI`, and string value, in this single case, for the University of Tennessee's Special Collections.

Justification
^^^^^^^^^^^^^

As this is only used once in our metadata, we have decided to remediate this XPath.

XPath
^^^^^

:code:`relatedItem[@type='host'][@displayLabel='Collection']/location/physicalLocation`

Decision
^^^^^^^^

Do not migrate.

`Example record - collections:dabney <https://digital.lib.utk.edu/collections/islandora/object/collections:dabney/datastream/MODS/view>`_

.. code-block:: xml

    <relatedItem displayLabel="Collection" type="host">
      <titleInfo>
        <title>University of Tennessee President's Papers, 1867-1954</title>
      </titleInfo>
      <identifier>AR.0001</identifier>
      <location>
        <physicalLocation authority="naf" valueURI="http://id.loc.gov/authorities/names/no2014027633">University of Tennessee, Knoxville. Special Collections</physicalLocation>
      </location>
    </relatedItem>

relatedItem[@type='constituent']
--------------------------------

Use Case
^^^^^^^^

:code:`relatedItem[@type='constituent']` appears 131 times in the Bass collection. The children of :code:`relatedItem[@type='constituent']` provide descriptive information about distinct parts of the resource.

Justification
^^^^^^^^^^^^^

XPaths
^^^^^^

:code:`relatedItem[@type='constituent']/titleInfo/title` AND

:code:`relatedItem[@type='constituent']/name[namePart][role/roleTerm[@authority='marcrelator'][@type='text'][@valueURI]]` AND

:code:`relatedItem[@type='constituent']/name[@authority='naf'][@valueURI][namepart][role/roleTerm[@authority='marcrelator'][@type='text'][@valueURI]]`

Decision
^^^^^^^^

The `dcterms:tableOfContents` property was selected to capture the title information available, the `relators:` namespace was chosen to capture information available in the :code:`roleTerm` elements, and `dbo:collection` property serves to identify the name of the physical archival collection.

`Example record - bass:19644 <https://digital.lib.utk.edu/collections/islandora/object/bass:19644/datastream/MODS/view>`_

.. code-block:: xml

    <relatedItem displayLabel="Project" type="host">
      <titleInfo>
        <title>The Dr. William M. Bass III Collection - The Bass Field Notes</title>
      </titleInfo>
    </relatedItem>
    <relatedItem displayLabel="Collection" type="host">
      <titleInfo>
        <title>Dr. William M. Bass III Collection</title>
      </titleInfo>
      <identifier type="local">MS.3689</identifier>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>M.B.P. weekly progress reports, Summer 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n83189337">
        <namePart>Bass, William M., 1928-</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project Weekly Report, June 24</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n84053297">
        <namePart>Stephenson, Robert L. (Robert Lloyd), 1919-</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>Archeological progress report no.8, Field season of 1963, December, 1963</title>
      </titleInfo>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>Archaeological progress report no.9, Field Season of 1964, November, 1964</title>
      </titleInfo>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report, Party no.1 - Kansas and Nebraska surveys, Report no.1-3, May 10-24, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/no2004018542">
        <namePart>Brown, Lionel A.</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report Party no.3 - Sully Burial analysis, Report no.1, 3-9, June 7, 22-August 2, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n83189337">
        <namePart>Bass, William M., 1928-</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report, Party #5 - Upper Yellowtail Reservoir, Report no.1-12, June 14-July 5-August 30, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/no90027536">
        <namePart>Husted, Wilfred M.</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report Party #10 - Dewey County Party, Report no.1-12, June 14-August 30, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n82020447">
        <namePart>Neuman, Robert W.</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report Party #12 - Davis Creek Site, Report no.1-12, June 14-August 30, 1963 [Numbering of the reports is off, went by dates]</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n87856030">
        <namePart>Bowers, Alfred W.</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n85031246">
        <namePart>Muller, Jon</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report, News from Lincoln, Report no.1-5, June 24-August 12, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n84053297">
        <namePart>Stephenson, Robert L. (Robert Lloyd), 1919-</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>University of South Dakota, Gavins Point Project no.2, Cooperators Party B, Report no.1-7, June 21-August 2, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/no2001006452">
        <namePart>Gant, Robert D.</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report, Party no.6 - Historic sites (Big Bend &amp; Oahe Res. Areas), Report no.1-10, June 22-August 24, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n81119648">
        <namePart>Smith, G. Hubert (George Hubert), 1908-1972</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report, Party no.7 - Pierre South Dakota, Report no.1-10, June 21-August 24, 1963 [numbering off, going by date]</title>
      </titleInfo>
      <name>
        <namePart>Jensen, Richard E.</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project Weekly Report, Parties no. 8 and 9 - La Roche and Chapelle Creek, Report no.1-11, June 21-September 3, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/no2004118058">
        <namePart>Hoffman, J. J. (John Jacob), 1931-</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report, Party no.11 - Moreau Party, Report no.2-11, June 21-August 30, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/no2004118055">
        <namePart>Mallory, Oscar L.</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>University of Kansas Milford Reservoir Archeological Party, Cooperators Party A, Report no.3, June 28, 1963</title>
      </titleInfo>
      <name>
        <namePart>Schock, Jack</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>Nebraska State Historical Society - National Science Foundation Logan Creek Project - Cooperators Party C, Report no.1, June 28, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n88243079">
        <namePart>Kivett, Marvin F.</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project Weekly report, Party no. 9 - Chapelle Creek, Report no.3-10, July 5-August 23, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n78078895">
        <namePart>Folan, William J.</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report, Party no. 4 - Garrison Diversion, Report no.1-6, July 26-August 30, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n50038965">
        <namePart>Johnson, Elden</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>

.. code-block:: turtle

    @prefix dbo: <http://dbpedia.org/ontology/> .
    @prefix dcterms: <http://purl.org/dc/terms/> .
    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1> dbo:collection "Dr. William M. Bass III Collection , MS.3689" ;
        dcterms:tableOfContents "M.B.P. weekly progress reports, Summer 1963 (Bass, William M., 1928-) -- Archeological progress report no.8, Field season of 1963, December, 1963 -- Archaeological progress report no.9, Field Season of 1964, November, 1964 -- 1963 Missouri Basin Project weekly report, Party no.1 - Kansas and Nebraska surveys, Report no.1-3, May 10-24, 1963 (Brown, Lionel A.) -- 1963 Missouri Basin Project weekly report Party no.3 - Sully Burial analysis, Report no.1, 3-9, June 7, 22-August 2, 1963 (Bass, William M., 1928-) -- 1963 Missouri Basin Project weekly report, Party #5 - Upper Yellowtail Reservoir, Report no.1-12, June 14-July 5-August 30, 1963 (Husted, Wilfred M.) -- 1963 Missouri Basin Project weekly report Party #10 - Dewey County Party, Report no.1-12, June 14-August 30, 1963 (Neuman, Robert W.) -- 1963 Missouri Basin Project weekly report Party #12 - Davis Creek Site, Report no.1-12, June 14-August 30, 1963 [Numbering of the reports is off, went by dates] (Bowers, Alfred W.) -- 1963 Missouri Basin Project weekly report, News from Lincoln, Report no.1-5, June 24-August 12, 1963 (Stephenson, Robert L. (Robert Lloyd), 1919-) -- University of South Dakota, Gavins Point Project no.2, Cooperators Party B, Report no.1-7, June 21-August 2, 1963 (Gant, Robert D.) -- 1963 Missouri Basin Project weekly report, Party no.6 - Historic sites (Big Bend & Oahe Res. Areas), Report no.1-10, June 22-August 24, 1963 (Smith, G. Hubert (George Hubert), 1908-1972) -- 1963 Missouri Basin Project weekly report, Party no.7 - Pierre South Dakota, Report no.1-10, June 21-August 24, 1963 [numbering off, going by date] (Jensen, Richard E.) -- 1963 Missouri Basin Project Weekly Report, Parties no. 8 and 9 - La Roche and Chapelle Creek, Report no.1-11, June 21-September 3, 1963 (Hoffman, J. J. (John Jacob), 1931-) -- 1963 Missouri Basin Project weekly report, Party no.11 - Moreau Party, Report no.2-11, June 21-August 30, 1963 (Mallory, Oscar L.) -- University of Kansas Milford Reservoir Archeological Party, Cooperators Party A, Report no.3, June 28, 1963 (Schock, Jack) -- Nebraska State Historical Society - National Science Foundation Logan Creek Project - Cooperators Party C, Report no.1, June 28, 1963 (Kivett, Marvin F.) -- 1963 Missouri Basin Project Weekly report, Party no. 9 - Chapelle Creek, Report no.3-10, July 5-August 23, 1963 (Folan, William J.) -- 1963 Missouri Basin Project weekly report, Party no. 4 - Garrison Diversion, Report no.1-6, July 26-August 30, 1963 (Johnson, Elden)" ;
        relators:cre <http://id.loc.gov/authorities/names/n83189337> ;
        relators:cre <http://id.loc.gov/authorities/names/n84053297> ;
        relators:cre <http://id.loc.gov/authorities/names/no2004018542> ;
        relators:cre <http://id.loc.gov/authorities/names/n83189337> ;
        relators:cre <http://id.loc.gov/authorities/names/no90027536> ;
        relators:cre <http://id.loc.gov/authorities/names/n82020447> ;
        relators:cre <http://id.loc.gov/authorities/names/n87856030> ;
        relators:cre <http://id.loc.gov/authorities/names/n85031246> ;
        relators:cre <http://id.loc.gov/authorities/names/n84053297> ;
        relators:cre <http://id.loc.gov/authorities/names/no2001006452> ;
        relators:cre <http://id.loc.gov/authorities/names/n81119648> ;
        relators:cre "Jensen, Richard E." ;
        relators:cre <http://id.loc.gov/authorities/names/no2004118058> ;
        relators:cre <http://id.loc.gov/authorities/names/no2004118055> ;
        relators:cre "Schock, Jack" ;
        relators:cre <http://id.loc.gov/authorities/names/n88243079> ;
        relators:cre <http://id.loc.gov/authorities/names/n78078895> ;
        relators:cre <http://id.loc.gov/authorities/names/n50038965> .

location
========

+-----------------------------------+----------------+-------------------------------------------------------------------------+
| Predicate                         | Value Type     | Usage Notes                                                             |
+===================================+================+=========================================================================+
| relators:rps                      | Literal or URI | Use for :code:`mods:physicalLocation` values, preferably using          |
|                                   |                | a URI for the organization from a controlled vocabulary                 |
|                                   |                | such as VIAF of Library of Congress Real World Objects.                 |
+-----------------------------------+----------------+-------------------------------------------------------------------------+
| skos:note                         | Literal        | Use to note :code:`mods:shelfLocator` strings.                          |
+-----------------------------------+----------------+-------------------------------------------------------------------------+
| dbo:collection                    | Literal        | Use to note :code:`mods:physicalLocation[@displayLabel="Collection"]`   |
|                                   |                | strings.                                                                |
+-----------------------------------+----------------+-------------------------------------------------------------------------+

physicalLocation as URI
-----------------------

Use Case
^^^^^^^^

Many records have :code:`valueURI` attributes set for :code:`physicalLocation`. This is inconsistent, even in our own collections.

Justification
^^^^^^^^^^^^^

When available, we will opt to use :code:`valueURI` values as the URI value for `relators:rps`, to better qualify objects of `relators:rps`.

XPath
^^^^^

:code:`location/physicalLocation[@valueURI]`

Decision
^^^^^^^^

The :code:`valueURI` attribute :code:`location/physicalLocation` is set as object.

`Example record from egypt:79 <https://digital.lib.utk.edu/collections/islandora/object/egypt:79/datastream/MODS/view>`_

.. code-block:: xml

    <location>
        <physicalLocation valueURI="http://id.loc.gov/authorities/names/no2017033007">Frank H. McClung Museum of Natural History and Culture</physicalLocation>
    </location>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1>
        relators:rps <http://id.loc.gov/authorities/names/no2017033007> .

physicalLocation as string (UTK)
--------------------------------

Use Case
^^^^^^^^

In many of our own collections, we use strings to describe :code:`physicalLocation`. We are inconsistent in the structuring of these strings, leading to many different variations for both our Libraries and Special Collections, some of these include misspellings or just different formatting:

- "The University of Tennessee Libraries, Knoxville"
- "University of Tennesse Knoxville. Libraries"
- "University of Tennessee Knoxville. Libraries"

Justification
^^^^^^^^^^^^^

To create better consistency and cleanliness going forward, we will isolate all instances of these strings and transcribe them to appropriate URIs for UT Libraries and Special collections.

XPath
^^^^^

:code:`location/physicalLocation[not(@valueURI)][text()="The University of Tennessee Libraries, Knoxville" or text()="University of Tennesse Knoxville. Libraries" or text()="University of Tennessee Knoxville. Libraries"]`

Decision
^^^^^^^^

Even when MODS only has a string present, we will map "The University of Tennessee Libraries, Knoxville" and "University of Tennessee, Knoxville. Special Collections" to relative URIs.

`Example record from fbpro:94819 <https://digital.lib.utk.edu/collections/islandora/object/fbpro:94819/datastream/MODS/view>`_

.. code-block:: xml

    <location>
        <physicalLocation>The University of Tennessee Libraries, Knoxville</physicalLocation>
    </location>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1>
        relators:rps <http://id.loc.gov/authorities/names/n80003889> .

`Example record from cDanielCartoon:1177 <https://digital.lib.utk.edu/collections/islandora/object/cDanielCartoon:1177/datastream/MODS/view>`_

.. code-block:: xml

    <location>
        <physicalLocation>University of Tennessee, Knoxville. Special Collections</physicalLocation>
        <holdingSimple>
            <copyInformation>
                <shelfLocator>Taxes and Economy</shelfLocator>
            </copyInformation>
        </holdingSimple>
    </location>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1>
        relators:rps <http://id.loc.gov/authorities/names/no2014027633> .

physicalLocation as string (non-UTK)
------------------------------------

Use Case
^^^^^^^^

Across our collections, there are also many cases where non-UTK items do not have URIs and instead use strings.

Justification
^^^^^^^^^^^^^

Translating these to a relative URIs would require significant effort, and the value added may be trivial at this point.

XPath
^^^^^

:code:`location/physicalLocation[not(@valueURI)][not(text()="The University of Tennessee Libraries, Knoxville" or text()="University of Tennesse Knoxville. Libraries" or text()="University of Tennessee Knoxville. Libraries")]`

Decision
^^^^^^^^

In cases that the :code:`physicalLocation` are non-UTK and only a string is provided, we will only use the string literal.

.. code-block:: xml

    <location>
        <physicalLocation>Blount County Public Library</physicalLocation>
        <holdingExternal>
            <holding xsi:schemaLocation="info:ofi/fmt:xml:xsd:iso20775 http://www.loc.gov/standards/iso20775/N130_ISOholdings_v6_1.xsd">
                <physicalAddress>
                    <text>City: Maryville</text>
                    <text>County: Blount County</text>
                    <text>State: Tennessee</text>
                </physicalAddress>
            </holding>
        </holdingExternal>
    </location>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1>
        relators:rps "Blount County Public Library" .

physicalLocation with shelfLocator (UTK)
----------------------------------------

Use Case
^^^^^^^^

In many cases, some of our collection items will have :code:`shelfLocator` information. This information may not currently be accurate and can found via Special Collections’ finding aids.

Justification
^^^^^^^^^^^^^

Because our records in MODS records may not be accurate and this information is located elsewhere, and perhaps more accurate, we will drop this information when :code:`shelfLocator` is used in conjunction with our repositories.

XPath
^^^^^

:code:`location[physicalLocation[text()[contains(., "University of Tennessee")]]]/shelfLocator`

Decision
^^^^^^^^

We will drop :code:`shelfLocator` data when present for UT Knoxville records.

`Example record from scopes:1258 <https://digital.lib.utk.edu/collections/islandora/object/scopes:1258/datastream/MODS/view>`_

.. code-block:: xml

    <location>
        <physicalLocation valueURI="http://id.loc.gov/authorities/names/no2014027633">University of Tennessee, Knoxville. Special Collections</physicalLocation>
        <shelfLocator>Box 5, Folder 8</shelfLocator>
    </location>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1>
        relators:rps <http://id.loc.gov/authorities/names/no2014027633> .

physicalLocation with shelfLocator (non-UTK)
--------------------------------------------

Use Case
^^^^^^^^

Instances where non-UTK held items have :code:`shelfLocator` information.

Justification
^^^^^^^^^^^^^

While, we do not not know if this :code:`shelfLocator` information is accurate, we will opt to retain it going forward as a string and map to `skos:note`. Samvera does note some possible future availability of `opaque:locationShelfLocator`, however this predicate does not exist yet.

XPath
^^^^^

:code:`location[physicalLocation[text()[not(contains(., "University of Tennessee"))]]]/shelfLocator`
:code:`location[physicalLocation[not(contains(.,'University of Tennessee'))] and holdingSimple/copyInformation/shelfLocator]`

Decision
^^^^^^^^

We will retain :code:`shelfLocator` data when present for non-UTK records, and transcribe this to a `skos:note`.

`Example record from volvoices:2136 <https://digital.lib.utk.edu/collections/islandora/object/volvoices:2136/datastream/MODS/view>`_

.. code-block:: xml

    <location>
        <physicalLocation>Cleveland State Community College</physicalLocation>
        <holdingSimple>
            <copyInformation>
                <shelfLocator>Photograph Collection 2, People</shelfLocator>
            </copyInformation>
        </holdingSimple>
        <holdingExternal>
            <holding xsi:schemaLocation="info:ofi/fmt:xml:xsd:iso20775 http://www.loc.gov/standards/iso20775/N130_ISOholdings_v6_1.xsd">
                <physicalAddress>
                    <text>City: Cleveland</text>
                    <text>County: Bradley County</text>
                    <text>State: Tennessee</text>
                </physicalAddress>
            </holding>
        </holdingExternal>
    </location>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .

    <https://example.org/objects/1>
        relators:rps "Cleveland State Community College" ;
        skos:note "Shelf locator: Photograph Collection 2, People" .

physicalLocation with holdingExternal
-------------------------------------

Use Case
^^^^^^^^

Some instances in our collections contain nested subelements for :code:`holdingExternal` and the further nested :code:`physicalAddress` information.

Justification
^^^^^^^^^^^^^

To keep our metadata as simple as possible from a technical standpoint we will drop all information for :code:`holdingExternal`. This type of information has little additive value when :code:`physicalLocation` is already referenced.

XPath
^^^^^

:code:`location/holdingExternal`

Decision
^^^^^^^^

We will drop all information for :code:`holdingExternal`.

`Example record from volvoices:2199 <https://digital.lib.utk.edu/collections/islandora/object/volvoices:2199/datastream/MODS/view>`_

.. code-block:: xml

    <location>
        <physicalLocation>University of Memphis. Special Collections</physicalLocation>
        <holdingSimple>
            <copyInformation>
                <shelfLocator>Manuscript Number 5</shelfLocator>
            </copyInformation>
        </holdingSimple>
        <holdingExternal>
            <holding xsi:schemaLocation="info:ofi/fmt:xml:xsd:iso20775 http://www.loc.gov/standards/iso20775/N130_ISOholdings_v6_1.xsd">
                <physicalAddress>
                    <text>City: Memphis</text>
                    <text>County: Shelby County</text>
                    <text>State: Tennessee</text>
                </physicalAddress>
            </holding>
        </holdingExternal>
    </location>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .

    <https://example.org/objects/1>
        relators:rps "University of Memphis. Special Collections" ;
        skos:note "Shelf locator: Manuscript Number 5" .

physicalLocation with @displayLabel="Address"
---------------------------------------------

Use Case
^^^^^^^^

Some of items with the :code:`physicalLocation` of Pi Beta Phi Fraternity also have a :code:physicalLocation subelement with the :code:`displayLabel` attribute value of "Address".

Justification
^^^^^^^^^^^^^

Similar to the :code:`holdingExternal`, we will opt drop this information to maintain simplicity of our data from a technical standpoint.

XPath
^^^^^

:code:`location/physicalLocation[@displayLabel="Address"]`

Decision
^^^^^^^^

Drop this.

`Example record from volvoices:2199 <https://digital.lib.utk.edu/collections/islandora/object/volvoices:2199/datastream/MODS/view>`_

.. code-block:: xml

    <location>
        <physicalLocation>Pi Beta Phi Fraternity</physicalLocation>
        <physicalLocation displayLabel="Address">1154 Town and Country Commons Drive, Town and Country, Missouri 63017</physicalLocation>
        <shelfLocator>Box 36, Folder 14</shelfLocator>
    </location>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .

    <https://example.org/objects/1>
        relators:rps "Pi Beta Phi Fraternity" ;
        skos:note "Shelf locator: Box 36, Folder 14" .

physicalLocation with @displayLabel="Collection"
------------------------------------------------

Use Case
^^^^^^^^

In a some collections for Arrowmont, we will find items having a :code:`physicalLocation` subelement with the :code:`displayLabel` attribute value of "Collection" with text containing "Archives Collection". We also have extra :code:`physicalLocation` subelements with :code:`displayLabel` attribute values of "Detailed Location", "City" and "State".

Justification
^^^^^^^^^^^^^

Because these records do not already have a `dbo:collection` predicate, we will transcribe the string literal to `dbo:collection` for :code:`location/physicalLocation[@displayLabel="Collection"]`. No other data here needs to be retained and will be dropped.

XPath
^^^^^

:code:`location/physicalLocation[@displayLabel="Collection" and text()[contains(.,"Archives Collection")]]`
:code:`location/physicalLocation[@displayLabel="Repository"]`
:code:`location/physicalLocation[@displayLabel="Detailed Location"]`
:code:`location/physicalLocation[@displayLabel="City"]`
:code:`location/physicalLocation[@displayLabel="State"]`

Decision
^^^^^^^^

We will keep the string for the :code:`physicalLocation` instance with :code:`displayLabel="Collection"` and transcribe this to literal for `dbo:collection`.

Similar to when :code:`physicalLocation` has no :code:`displayLabel` attribute, :code:`physicalLocation` with an :code:`displayLabel` attribute value of "Repository" is retained as `relators:rps`.

All other :code:`physicalLocation` ("Detailed Location", "City", "State") data is dropped.

`Example record from volvoices:2199 <https://digital.lib.utk.edu/collections/islandora/object/volvoices:2199/datastream/MODS/view>`_

.. code-block:: xml

    <location>
        <physicalLocation displayLabel="Collection">Archives Collection</physicalLocation>
        <physicalLocation displayLabel="Repository">Arrowmont School of Arts and Crafts</physicalLocation>
        <physicalLocation displayLabel="Detailed Location"/>
        <physicalLocation displayLabel="City">Gatlinburg</physicalLocation>
        <physicalLocation displayLabel="State">Tennessee</physicalLocation>
    </location>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .
    @prefix dbo: <http://dbpedia.org/ontology/> .

    <https://example.org/objects/1>
        relators:rps <http://id.loc.gov/authorities/names/no2001080757> ;
        dbo:collection "Archives Collection" .

physicalLocation within volvoices used for provider information
---------------------------------------------------------------

Use Case
^^^^^^^^

There is one collection in which location information needs to be used to correct inaccuracies for other metadata fields. The Volunteer Voices collection lists the University of Tennessee as the :code:`recordContentSource` for all records. While UTK may have created the metadata records, our mapping with DPLA makes it so that we are noted as the source of these records rather than the actual contributing institution. There are instances within volvoices in which the institution in physicalLocation and the one listed in recordContent Source are the same. This action doesn't need to be taken for those records.

Justification
^^^^^^^^^^^^^

Providing contributing institutions with the proper credit is important for inter-institutional projects.

XPath
^^^^^

:code:`location/physicalLocation[. != recordInfo/recordContentSource]`

Note: an easier way to resolve this particular XPath expression might be to start at the document node, :code:`mods`; e.g. :code:`mods[location/physicalLocation != recordInfo/recordContentSource]`.

Decision
^^^^^^^^

Will be mapped to both `relators:rps` and `edm:dataProvider`. `edm:dataProvider` is being used because the value is an "organisation who contributes data indirectly to an aggregation service" (aka to UTK first and then to DPLA).

Here's an example record -

`Example record from volvoices:2737 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A2737/datastream/MODS/view>`_

.. code-block:: xml

    <recordInfo>
        <recordContentSource>University of Tennessee, Knoxville. Special Collections</recordContentSource>
    </recordInfo>
    <location>
        <physicalLocation>Chattanooga-Hamilton County Bicentennial Library</physicalLocation>
    </location>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/> .
    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1>
        edm:dataProvider "Chattanooga-Hamilton County Bicentennial Library" ;
        relators:rps "Chattanooga-Hamilton County Bicentennial Library" .

url
---

Use Case
^^^^^^^^

Some of our metadata for volvoices may contain self-referential URL locations. The data contained in these directly reference objects in our current Islandora 7 build and the object’s datastreams.

Justification
^^^^^^^^^^^^^

This is self-referential and has no value in a new system.

XPath
^^^^^

:code:`location/url`

Decision
^^^^^^^^

Drop this.

`Example record from volvoices:9999 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A9999/datastream/MODS/view>`_

.. code-block:: xml

    <location>
        <url access="object in context" usage="primary display">https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A9999</url>
        <url access="preview">https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A9999/datastream/TN/view</url>
    </location>

recordInfo
==========

+------------------+----------------+-----------------------------------------------------------------------------------------------------------------+
| Predicate        | Value Type     | Usage Notes                                                                                                     |
+==================+================+=================================================================================================================+
| edm:dataProvider | URI or Literal | Use the name of the organization who contributes data indirectly                                                |
|                  |                | to an aggregation service. Note that we have decided to only use literals even though the property allows URIs. |
+------------------+----------------+-----------------------------------------------------------------------------------------------------------------+
| edm:provider     | URI or Literal | Use the name of the organization (typically UTK) who delivers data directly to an aggregation                   |
|                  |                | service. Note that we have decided to only use literals even though the property allows URIs.                   |
+------------------+----------------+-----------------------------------------------------------------------------------------------------------------+

recordIdentifier
----------------

Use Case
^^^^^^^^

Unremediated records often contain identifiers for the record. These take a couple of different forms. The Heilman
collection and Volunteer Voices collections contain this element. In Volunteer Voices the identifier is simply the adminDB
value with 'record' appended to the beginning (`e.g. volvoices:2352 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A2352/datastream/MODS/view>`_).

Justification
^^^^^^^^^^^^^

As the basic root of the :code:`recordIdentifier` value is already present in the :code:`identifier` element in all cases and the
:code:`recordIdentifier` value is never used on its own, there is no reason to retain these values.

XPath
^^^^^

:code:`recordInfo/recordIdentifier`

Decision
^^^^^^^^

All :code:`recordIdentifier` values should be dropped, so no RDF example is included below.

Here's an `example record - heilman:1001 <https://digital.lib.utk.edu/collections/islandora/object/heilman%3A1001/datastream/MODS/view>`_.

.. code-block:: xml

    <identifier type="local">Pseudolarix_0858</identifier>
    <recordInfo>
        <recordIdentifier>record_Pseudolarix_0858</recordIdentifier>
    </recordInfo>

languageOfCataloging
--------------------

Use Case
^^^^^^^^

All of the recently migrated SCOUT to TEI collections (e.g. American Civil War Collection, Tennessee Documentary History, etc.)
as well as some of UTK's less recent collections (e.g. Sanborn, mpabaker, etc.) contain the element :code:`languageOfCataloging`.
In total, it is found in approximately 6,000 records. Note that in all cases the language is English, but this information
is represented as both a code ("eng") and a text value ("English").

Justification
^^^^^^^^^^^^^

Currently :code:`languageOfCataloging` is not publicly displayed anywhere outside of the MODS XML. The values of this element
do have the potential to be used if UTK has materials that might warrant cataloging in another language, but currently
this is not the case. An example of a project that includes two records, one catalogued in Spanish and one in English, is
`UNC's New Roots / Nuevas Raíces <https://newroots.lib.unc.edu/>`_. While UTK may want to pursue a project like this in the
future, presently it seems unlikely that it will. More importantly, if such a project became a priority, it would not be
difficult to distinguish via code UTK's existing English records from records in another language. If we did want to create
a project like this, information on the language of cataloging could be added across the repository with minimal effort.

XPath
^^^^^

:code:`recordInfo/languageOfCataloging`

Decision
^^^^^^^^

Since we are not currently utilizing these values in any way, these should be dropped in the mapping.

Here's an `example record - sanborn:1002 <https://digital.lib.utk.edu/collections/islandora/object/sanborn%3A1002/datastream/MODS/view>`_.

.. code-block:: xml

    <recordInfo>
        <languageOfCataloging>
            <languageTerm authority="iso639-2b" type="code">eng</languageTerm>
        </languageOfCataloging>
    </recordInfo>

recordOrigin
------------

Use Case
^^^^^^^^

The :code:`recordOrigin` element includes information about what methods or transformations were used to prepare a record. There
are six different distinct values in UTK's metadata.

Justification
^^^^^^^^^^^^^

Because the existing values all relate to MODS XML, the string values present will no longer be applicable in a RDF-based
platform. Discussion indicated that there might be some use for the general property of :code:`recordOrigin` if a link to this
mapping document or some other relevant resource was shared in place of the existing values. This administrative information
could also be shared on the Digital Collections website or elsewhere rather than the record. As a convincing argument
was not made that this information is essential, it was decided to drop these values

XPath
^^^^^

:code:`recordInfo/recordOrigin`

Decision
^^^^^^^^

Drop all values.

Here's an `example record - cDanielCartoon:1177 <https://digital.lib.utk.edu/collections/islandora/object/cDanielCartoon%3A1177/datastream/MODS/view>`_

.. code-block:: xml

    <recordInfo>
        <recordOrigin>Created and edited in general conformance to MODS Guidelines (Version 3.5).</recordOrigin>
    </recordInfo>

recordChangeDate
----------------

Use Case
^^^^^^^^

This element is used sparingly in UTK's metadata records. Currently there are five distinct values, all indicating that the
last change to the record was made in 2015, which simply isn't sharing accurate information.

Justification
^^^^^^^^^^^^^

Keeping this information is not be useful as it doesn't allow someone viewing the record to see when it was actually
last updated. Inaccurate information is shared. In addition, in a system like Islandora it's easy enough for an internal
staff member to view when the metadata datastream has been updated without tracking this in the record. This element can
be dropped.

XPath
^^^^^

:code:`recordInfo/recordChangeDate`

Decision
^^^^^^^^

This element should be dropped.

Here's an `example record - volvoices:3435 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A3435/datastream/MODS/view>`_.

.. code-block:: xml

    <recordInfo>
        <recordChangeDate encoding="edtf">2015-03-23</recordChangeDate>
        <recordChangeDate encoding="edtf">2015-03-31</recordChangeDate>
        <recordChangeDate encoding="edtf">2015-04-01</recordChangeDate>
    </recordInfo>

recordCreationDate
------------------

Use Case
^^^^^^^^

A total of 167 values are present for :code:`recordCreationDate`. This value shows when the record was originally created. All
but one of these values precedes 2010. All of the recently migrated TEI SCOUT records (2,386) have a value of
"2020-04-23-04:00". This is the only value not presented in EDTF format. Otherwise all of the values appear to come from
Volunteer Voices.

Justification
^^^^^^^^^^^^^

Unlike :code:`recordChangeDate`, all of the values within :code:`recordCreationDate` are at least accurate. Currently this information
is not used or displayed for users. Given this and the fact that this element is present in a very small percentage of
UTK records, it does not seem useful to keep this information. Again, a repository system should have a way to track
when a metadata datastream for a particular digital object was created. Therefore keeping this information adds unnecessary
complexity.

XPath
^^^^^

:code:`recordInfo/recordCreationDate`

Decision
^^^^^^^^

These values will be dropped.

Here's an `example record - volvoices:1857 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A1857/datastream/MODS/view>`_.

.. code-block:: xml

    <recordInfo>
        <recordCreationDate encoding="edtf">2007-10-26</recordCreationDate>
    </recordInfo>

recordContentSource - University of Tennessee, Knoxville as value
-----------------------------------------------------------------

Use Case
^^^^^^^^

The :code:`recordContentSource` element is one of the most essential elements within :code:`recordInfo`, as we currently use it to
communicate the provider in DPLA. Because DPLA cannot handle URIs, the decision has been made to only deliver strings.
We do not feel strongly that the added functionality provided by using a URI for this field warrants the effort needed
to process URIs into strings for delivery to DPLA. We recognize that this goes against our general philosophy to use URIs
when possible.

To better understand UTK's use of this element some background information is helpful. At UTK the information we share in
this element is not consistent with the definition of :code:`recordContentSource` - "The code or name of the entity (e.g. an
organization and/or database) that either created or modified the original record." While we work with other partners,
like the Children's Defense Fund and the McClung Museum, we are still technically the creators of the records in these
situations. Despite this, we typically list these institutions as the record creator because we set up :code:`recordContentSource`
as the element that DPLA should map to for content provider. In actuality, when the content provider is not UTK, this
information should be communicated in :code:`physicalLocation` and our DPLA mapping should be updated. Despite these semantic
issues, UTK has consistently put this information in an incorrect element, so the mapping is not affected.

Justification
^^^^^^^^^^^^^

A content provider is required in DPLA. This value also provides UTK with the opportunity to attribute collections to
the institution that provided them, which is important for maintaining respectful relationships. Because of DPLA's
limitations, we will provide this information as a string.

XPath
^^^^^

:code:`recordInfo/recordContentSource`

Decision
^^^^^^^^

Because UTK acts as a service hub for DPLA and it delivers data directly to this aggregator, it can be considered an
`edm:provider`. This is defined as "The name or identifier of the organization who delivers data directly to an aggregation
service (e.g. Europeana)."

When UTK physically holds the material and created the record, the metadata resembles this `example record - acwiley:284 <https://digital.lib.utk.edu/collections/islandora/object/acwiley%3A284/datastream/MODS/view>`_.

.. code-block:: xml

    <recordInfo>
        <recordContentSource valueURI="http://id.loc.gov/authorities/names/n87808088">University of Tennessee, Knoxville. Libraries</recordContentSource>
    </recordInfo>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/> .

        <https://example.org/objects/1> edm:provider "University of Tennessee, Knoxville. Libraries" .

recordContentSource - not University of Tennessee, Knoxville as value
---------------------------------------------------------------------

Use Case
^^^^^^^^

When a resource comes from a non-UTK institution, its name is typically placed in :code:`recordContentSource`. An exception to
this is Volunteer Voices, which only includes the contributing institution in :code:`location/physicalLocation`. See
:code:`location` for more information.

Justification
^^^^^^^^^^^^^

A content provider is required in DPLA. Sharing the names of institutional partners within the Digital Library of Tennessee
is also a great way to recognize the contributions of these libraries. Because of DPLA's limitations, we will provide
this information as a string.

XPath
^^^^^

:code:`recordInfo/recordContentSource`

Decision
^^^^^^^^

When the institution listed as providing the information is not UTK, `edm:dataProvider` should be used instead of
`edm:provider`. `edm:dataProvider` is defined as "The name or identifier of the organisation who contributes data indirectly
to an aggregation service."

Here's an `example record - cdf:70 <https://digital.lib.utk.edu/collections/islandora/object/cdf%3A70/datastream/MODS/view>`_.
It is also coupled with an "Intermediate Provider" note, as shown below. McClung's Egypt collection is also treated similarly.

.. code-block:: xml

    <recordInfo>
        <recordContentSource valueURI="http://id.loc.gov/authorities/names/no2017113530">Langston Hughes Library (Children's Defense Fund Haley Farm)</recordContentSource>
    </recordInfo>
    <note displayLabel="Intermediate Provider">University of Tennessee, Knoxville. Libraries</note>
    <location>
        <physicalLocation valueURI="http://id.loc.gov/authorities/names/no2017113530">Langston Hughes Library (Children's Defense Fund Haley Farm)</physicalLocation>
    </location>

For the purposes of DPLA, we only need the :code:`recordContentSource` value and not also the :code:`physicalLocation` value. Because
these institutions are not directly contributing to DPLA, they are listed as an `edm:dataProvider` instead of an `edm:provider`.

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/> .

        <https://example.org/objects/1> edm:dataProvider "Langston Hughes Library (Children's Defense Fund Haley Farm)" .

accessCondition
===============

+------------+------------+----------------------------------------------------------------+
| Predicate  | Value Type | Usage Notes                                                    |
+============+============+================================================================+
| edm:rights | URI        | Use for rights URIs from RightsStatements or Creative Commons. |
+------------+------------+----------------------------------------------------------------+
| skos:note  | Literal    | Use for accessConditions with @type="restrictions on access".  |
+------------+------------+----------------------------------------------------------------+

accessCondition - Rights Statements and Creative Commons Licenses
-----------------------------------------------------------------

Use Case
^^^^^^^^

When one of the twelve standardized rights statements from `https://righsstatements.org <https://righsstatements.org>`_
or one of the CC licenses is present, the value should be mapped to `edm:rights` and have a value type of URI.

Justification
^^^^^^^^^^^^^

DPLA maps both CC licenses and Rights Statements to `edm:rights`. So does Samvera. Presently only the Heilman Collection includes
a CC license.

XPath
^^^^^

:code:`accessCondition[@xlink:href]`

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

        <https://example.org/objects/1> edm:rights <https://creativecommons.org/licenses/by-nc-nd/3.0/rdf> .

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

As the value present in the current :code:`accessCondition` node is not associated with a controlled vocabulary and simply needs to
be displayed to the user within the record, there is no reason to connect it with other :code:`accessCondition` values. A note is
sufficient for this use case.

XPath
^^^^^

:code:`accessCondition[@type="restriction on access"]`

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

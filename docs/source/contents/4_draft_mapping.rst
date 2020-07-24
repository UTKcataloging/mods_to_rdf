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

`mods:note` OR `mods:note[@type="handwritten"]` OR `mods:note[@type="provenance"]`

Decision
^^^^^^^^

`Example record from bakerav:291 <https://digital.lib.utk.edu/collections/islandora/object/bakerav:291/datastream/MODS>`_

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

Some of our notes actually refer to unconrtolled keywords or tags.

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
`mods:note[@displayLabel="Intermediate Provider"]`

Decision
^^^^^^^^

`Example record from heilman:1000 <https://digital.lib.utk.edu/collections/islandora/object/heilman:1000/datastream/MODS>`_

.. code-block:: xml

    <note displayLabel="dpn">
        This object was added to the Digital Preservation Network in November 2016.
    </note>

**Do not migrate!**


notes - Undecided
-----------------

xpath
^^^^^

* `mods:note[@displayLabel="use and reproduction"]`
* `mods:note[@displayLabel="Transcribed from Original Collection"]`
* `mods:note[@displayLabel="Project Part"]`
* `mods:note[@displayLabel="Local Rights"]`
* `mods:note[@displayLabel="Attribution"]`


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

**Use case**

When one of the twelve standardized rights statements from `https://righsstatements.org <https://righsstatements.org>`_
or one of the CC licenses is present, the value should be mapped to edm:rights and have a value type of URI.

**Justification**

DPLA maps both CC licenses and Rights Statements to edm:rights. So does Samvera. Presently only the heilman collection includes
a CC license

**Xpath**

mods:accessCondition[@xlink:href]

**Decision**

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

**Use case**

The Howard Baker Audiovisual Collection includes 46 items that are "In Copyright" and therefore have restricted access to
avoid any potential copyright conflicts. Only on campus access is provided to the actual recordings, though the metadata
records are accessible from anywhere. Having the metadata accessible makes it so that anyone can discover these materials
and decide for themselves if it is worth a trip into campus. Some of the recordings had some deterioration and were therefore
digitized as a preservation measure. Having digitized copies also made providing on site access easier. In order to make
sure that users are aware of the on campus only restriction, a note needed to be added to the metadata. When off campus
users visit the metadata, this note makes it clear why they cannot access the recording.

**Justification**

As the value present in the current accessCondition node is not associated with a controlled vocabulary and simply needs to
be displayed to the user within the record, there is no reason to connect it with other accessCondition values. A note is
sufficient for this use case.

**Xpath**

mods:accessCondition[@type="restriction on access"]

**Decision**

`Example record - bakerav:10 <https://digital.lib.utk.edu/collections/islandora/object/bakerav%3A10/datastream/MODS/view>`_

.. code-block:: xml

    <accessCondition type="restriction on access">
        This item can only be accessed on the University of Tennessee (Knoxville) campus
    </accessCondition>

.. code-block:: turtle

    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .

        <https://example.org/objects/1> skos:note 'This item can only be accessed on the University of Tennessee (Knoxville) campus' .

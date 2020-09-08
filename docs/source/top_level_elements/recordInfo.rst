recordInfo
==========

About
-----

This section describes all elements present within UTK's recordInfo nodes. Note that <recordInfoNote> and <descriptionStandard>
are not used.

recordIdentifier
----------------
Unremediated records often contain identifiers for the record. These take a couple of different forms. Identifiers starting
with "record_spc" used to be present in the Scopes collection, but these were recently removed. In addition, the Heilman
collection and Volunteer Voices collections contain this element. In Volunteer Voices the identifier is simply the adminDB
value with 'record' appended to the beginning (`e.g. volvoices:2352 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A2352/datastream/MODS/view>`_).

Here's another `example record - heilman:1001 <https://digital.lib.utk.edu/collections/islandora/object/heilman%3A1001/datastream/MODS/view>`_.

.. code-block:: xml

    <identifier type="local">Pseudolarix_0858</identifier>
    <recordInfo>
        <recordIdentifier>record_Pseudolarix_0858</recordIdentifier>
    </recordInfo>

In all cases, the same basic string is captured in <identifier>. Because of this, I would recommend that we always drop this
element in migration.

languageOfCataloging
--------------------

All of the recently migrated SCOUT to TEI collections (e.g. American Civil War Collection, Tennessee Documentary History, etc.)
as well as some of UTK's less recent collections (e.g. Sanborn, mpabaker, etc.) contain the element languageOfCataloging.
In total, it is found in approximately 6,000 records. Note that in call cases the language is English, but this information
is represented as both a code ('eng') and a text value ('English'):

{'languageTerm': {'@authority': 'iso639-2b', '#text': 'eng'}}

{'languageTerm': {'@authority': 'iso639-2b', '@type': 'code', '#text': 'eng'}}

{'languageTerm': {'@authority': 'iso639-2b', '@type': 'text', '#text': 'English'}}

{'languageTerm': {'@type': 'code', '@authority': 'iso639-2b', '#text': 'eng'}}

{'languageTerm': {'@type': 'text', '@authority': 'iso639-2b', '#text': 'English'}}

Here's an `example record - sanborn:1002 <https://digital.lib.utk.edu/collections/islandora/object/sanborn%3A1002/datastream/MODS/view>`_.

.. code-block:: xml

    <recordInfo>
        <languageOfCataloging>
            <languageTerm authority="iso639-2b" type="code">eng</languageTerm>
        </languageOfCataloging>
    </recordInfo>

Given that we only use English as the cataloging language at UTK, I propose that we either include this information in all
records or drop it entirely. Note that including foreign language strings for titles when transcribed, etc. does not change
the language of cataloging from English. To open us up to the possibility of including records in more than one language
if justified by a new collection, it may be ideal to include a languageOfCataloging element for all records.

recordOrigin
------------

The <recordOrigin> element includes information about what methods or transformations were used to prepare a record. There
are six different distinct values.

Here's an `example record - cDanielCartoon:1177 <https://digital.lib.utk.edu/collections/islandora/object/cDanielCartoon%3A1177/datastream/MODS/view>`_

.. code-block:: xml

    <recordInfo>
        <recordOrigin>Created and edited in general conformance to MODS Guidelines (Version 3.5).</recordOrigin>
    </recordInfo>

In an RDF-based system, these MODS comments will no longer be applicable. I would suggest that we drop these values.

recordChangeDate
----------------

This element is used sparingly in UTK's metadata records. Currently there are five distinct values, all indicating that the
last change to the record was made in 2015:

    {'@encoding': 'edtf', '#text': '2015-03-23'}

    {'@encoding': 'edtf', '#text': '2015-03-28'}

    {'@encoding': 'edtf', '#text': '2015-03-31'}

    {'@encoding': 'edtf', '#text': '2015-04-01'}

    {'@encoding': 'edtf', '#text': '2015-04-02'}

All of the records associated with this element are in the Volunteer Voices collection. Here's an `example record -
volvoices:3435 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A3435/datastream/MODS/view>`_.

.. code-block:: xml

    <recordInfo>
        <recordChangeDate encoding="edtf">2015-03-23</recordChangeDate>
        <recordChangeDate encoding="edtf">2015-03-31</recordChangeDate>
        <recordChangeDate encoding="edtf">2015-04-01</recordChangeDate>
    </recordInfo>

Given that the example record has been altered since 2015, keeping this information may not be useful. It doesn't actually allow
someone viewing the record to see when it was last updated. In addition, in a system like Islandora it's easy enough for
an internal staff member to view when the metadata datastream has been updated without tracking this in the record. I would
argue for dropping this element.

recordCreationDate
------------------

A total of 167 values are present for <recordCreationDate>. All but one of these values precedes 2010. All of the recently
migrated TEI SCOUT records (2,386) have a value of "2020-04-23-04:00". This is the only value not presented in EDTF format.
Otherwise all of the values appear to come from Volunteer Voices.

Here's an `example record - volvoices:1857 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A1857/datastream/MODS/view>`_.

.. code-block:: xml

    <recordInfo>
        <recordCreationDate encoding="edtf">2007-10-26</recordCreationDate>
    </recordInfo>

From an analysis perspective, it may be interesting to see when a record was first created in order to establish UTK's
longest standing collections. That being said, a very small percentage of our records include this in the metadata. One
could also argue that the "record" is completely changed through transformation and is a new record - making the original
ingest date of the digital content not really relevant. I'd like to see if others have a strong use case for keeping this
information.

recordContentSource
-------------------

The <recordContentSource> element is one of the most essential elements within <recordInfo>, as we currently use it to
communicate the provider in DPLA. At UTK though, the information we share in this element is not consistent with the
definition of <recordContentSource> - "The code or name of the entity (e.g. an organization and/or database) that either
created or modified the original record." While we work with other partners, like the Children's Defense Fund and the
McClung Museum, we are still technically the creators of the records in these situations. Despite this, we typically list
these institutions as the record creator because we set up <recordContentSource> as the element that DPLA should map to
for content provider. In actuality, when the content provider is not UTK, this information should be communicated in
<physicalLocation> and are DPLA mapping should be updated. Below are several examples showing how UTK uses this element.
There are 37 distinct values present in this element.

When UTK physically holds the material and created the record, the metadata resembles this `example record - acwiley:284 <https://digital.lib.utk.edu/collections/islandora/object/acwiley%3A284/datastream/MODS/view>`_.

.. code-block:: xml

    <recordInfo>
        <recordContentSource valueURI="http://id.loc.gov/authorities/names/n87808088">University of Tennessee, Knoxville. Libraries</recordContentSource>
    </recordInfo>

Note that UTK held items can also appear without a URI defining the institution as with `tdh:8803 <https://digital.lib.utk.edu/collections/islandora/object/tdh%3A8803/datastream/MODS/view>`_.
It looks like we also have a misspelling here.

.. code-block:: xml

    <recordInfo>
        <recordContentSource>University of Tennesse Knoxville. Libraries</recordContentSource>
    </recordInfo>

Sometimes when the resource comes from another institution, that institution name is placed in <recordContentSource>. For instance,
here's an `example record - cdf:70 <https://digital.lib.utk.edu/collections/islandora/object/cdf%3A70/datastream/MODS/view>`_.
Here it is also coupled with an "Intermediate Provider" note. McClung's Egypt collection is also treated similarly.

.. code-block:: xml

    <recordInfo>
        <recordContentSource valueURI="http://id.loc.gov/authorities/names/no2017113530">Langston Hughes Library (Children's Defense Fund Haley Farm)</recordContentSource>
    </recordInfo>
    <note displayLabel="Intermediate Provider">University of Tennessee, Knoxville. Libraries</note>
    <location>
        <physicalLocation valueURI="http://id.loc.gov/authorities/names/no2017113530">Langston Hughes Library (Children's Defense Fund Haley Farm)</physicalLocation>
    </location>

In addition, the TDH collection has null values. An example is `tdh:8597 <https://digital.lib.utk.edu/collections/islandora/object/tdh%3A8597/datastream/MODS/view>`_.

.. code-block:: xml

    <recordInfo>
        <recordContentSource/>
    </recordInfo>

Finally, there are 59 records that do not have <recordContentSource>. A few of these are starter namespaces (like baseball) that
will be filled out once metadata for the collection is created. 55 of the records are associated with Kintner. This collection
is currently being remediated by Andrew and this missing element will be addressed. Here's an `example record - kintner:10 <https://digital.lib.utk.edu/collections/islandora/object/kintner%3A10/datastream/MODS/view>`_.



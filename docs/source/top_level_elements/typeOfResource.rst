typeOfResource
==============

About
-----

This section describes the values and usage of <typeOfResource> within UTK metadata. Note that the manuscript attribute
is not used in any record.

typeOfResource with no attributes
---------------------------------

Most records currently have a typeOfResource value with no attributes. Depending on the item being described, it is possible
for there to be multiple typeOfResource values in a single record. The Islandora Metadata Interest Group has carefully
created a mapping to translate MODS typeOfResource values to dcterms resource types. A selection of the mapping is
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

Here's an `example record - vanvactor:1 <https://digital.lib.utk.edu/collections/islandora/object/vanvactor%3A1/datastream/MODS/view>`_.

.. code-block:: xml

    <typeOfResource collection="yes">notated music</typeOfResource>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:type <http://id.loc.gov/vocabulary/resourceTypes/not> .

typeOfResource with @collection="yes"
-------------------------------------

In MODS, an attribute can be used on typeOfResource to indicate that the record refers to an entire collection rather
than an individual resource. This is useful because it makes it possible to distinguish between object and collection
records in the catalog so that patrons understand more quickly how much content is associated with the record. The
Islandora Metadata Interest Group has come up with the solution of using the dcterms resource type of "Collection." In
this situation we will need multiple triples to preserve the information currently present - one for indicating the record is
for a collection and one (or more) for indicating prevalent resource type(s) in the collection. In MODS typeOfResource is
a repeatable field. Note that we will need to make sure that we do not repeat the Collection resource type in cases
where there are multiple typeOfResource[@collection="yes"] instances.

Here's a complex example that includes two <typeOfResource> values - `gsmrc:smhc <https://digital.lib.utk.edu/collections/islandora/object/gsmrc%3Asmhc/datastream/MODS/view>`_.

.. code-block:: xml

    <typeOfResource collection="yes">text</typeOfResource>
    <typeOfResource collection="yes">still image</typeOfResource>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms: <http://id.loc.gov/vocabulary/resourceTypes/col> ;
        dcterms:type <http://id.loc.gov/vocabulary/resourceTypes/txt> ;
        dcterms:type <http://id.loc.gov/vocabulary/resourceTypes/img> .

Missing typeOfResource value
----------------------------

Currently 9,993 records are missing a typeOfResource value. Some affected collections include Volunteer Voices, Roth, and
the Howard Baker Speeches and Remarks. We can consider if we would like to apply a blanket value to a collection at the time
of migration. For monolithic collections like Roth and Baker, this would be easy to achieve (roth = "still image" and
baker = "text" in MODS). For collections with varied formats, like Volunteer Voices, this will not be possible. Given that the
Digital Collections home page currently uses typeOfResource to initially limit searches, it would be beneficial for this
to be more consistently present.

Here's a record with no typeOfResource value - `roth:100 <https://digital.lib.utk.edu/collections/islandora/object/roth%3A100/datastream/MODS/view>`_.
If writing in these values by collection is desired, a list of collections and which accepted typeOfResource value should
be added can be created. This can also be dealt with in remediation.

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:type <http://id.loc.gov/vocabulary/resourceTypes/img> .
location
========

About
-----
This section describes all the different types of location elements that we have in our Islandora repository right now.

Distinct Cases
--------------

physicalLocation with explicit uri
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

https://digital.lib.utk.edu/collections/islandora/object/egypt:79/datastream/MODS/view

.. code-block:: xml

    <location>
        <physicalLocation valueURI="http://id.loc.gov/authorities/names/no2017033007">Frank H. McClung Museum of Natural History and Culture</physicalLocation>
    </location>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .

    <https://example.org/objects/1> relators:rps <http://id.loc.gov/authorities/names/no2017033007> .

physicalLocation as string (special collections)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

https://digital.lib.utk.edu/collections/islandora/object/roth:4245/datastream/MODS/view

.. code-block:: xml

    <location>
        <physicalLocation>University of Tennessee, Knoxville. Special Collections</physicalLocation>
    </location>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .
    @prefix relators: <http://id.loc.gov/vocabulary/relators> .

    <https://example.org/objects/1> relators:rps <http://id.loc.gov/authorities/names/no2014027633> .

physicalLocation as string (libraries)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**The University of Tennessee Libraries, Knoxville** 574 instances

https://digital.lib.utk.edu/collections/islandora/object/fbpro:94819/datastream/MODS/view

.. code-block:: xml

    <location>
        <physicalLocation>The University of Tennessee Libraries, Knoxville</physicalLocation>
    </location>

**University of Tennessee Knoxville. Libraries** 664 instances

https://digital.lib.utk.edu/collections/islandora/object/tatum:609/datastream/MODS/view

.. code-block:: xml

    <location>
        <physicalLocation>University of Tennessee Knoxville. Libraries</physicalLocation>
    </location>

**University of Tennesse Knoxville. Libraries** 397 instances

https://digital.lib.utk.edu/collections/islandora/object/tdh:8781/datastream/MODS/view

.. code-block:: xml

    <location>
        <physicalLocation>University of Tennesse Knoxville. Libraries</physicalLocation>
    </location>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .

    <https://example.org/objects/1> relators:rps <http://id.loc.gov/authorities/names/n80003889> .

physicalLocation and shelfLocator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

https://digital.lib.utk.edu/collections/islandora/object/scopes:1258/datastream/MODS/view

.. code-block:: xml

    <location>
        <physicalLocation valueURI="http://id.loc.gov/authorities/names/no2014027633">University of Tennessee, Knoxville. Special Collections</physicalLocation>
        <shelfLocator>Box 5, Folder 8</shelfLocator>
    </location>

In most cases, especially those under our purview, we will likely opt to drop box and folder number references.

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .

    <https://example.org/objects/1> relators:rps <http://id.loc.gov/authorities/names/no2014027633> .

physicalLocation with holdingSimple and holdingExternal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

https://digital.lib.utk.edu/collections/islandora/object/volvoices:2199/datastream/MODS/view

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

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .

    <https://example.org/objects/1> relators:rps "University of Memphis. Special Collections" .

physicalLocation with displayLabel="Address"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

https://digital.lib.utk.edu/collections/islandora/object/arrow:58/datastream/MODS/view

.. code-block:: xml


    <location>
        <physicalLocation>Pi Beta Phi Fraternity</physicalLocation>
        <physicalLocation displayLabel="Address">1154 Town and Country Commons Drive, Town and Country, Missouri 63017</physicalLocation>
        <shelfLocator>Box 36, Folder 14</shelfLocator>
    </location>

Samvera documentation does demonstrate use of Opaque Namespace **locationShelfLocator** predicate, however, this may still be under development or maybe even abandoned. Though, we likely do not want to do this for every item in our collections, there may be special cases where we want to use predicates to reference box and folder number and names. If so, we can use **boxNumber**, **boxName**, **folderNumber**, and **folderName**  `opaquenamespace predicates <http://opaquenamespace.org/predicates>`_.

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .
    @prefix opaque: <http://opaquenamespace.org/ns/> .

    <https://example.org/objects/1> relators:rps "Pi Beta Phi Fraternity" ;
        opaque:boxNumber "36" ;
        opaque:folderNumber "14" .

physicalLocation with displayLabel attributes for Collection and Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

https://digital.lib.utk.edu/collections/islandora/object/arrowmont%3A208/datastream/MODS/view

.. code-block:: xml


    <location>
        <physicalLocation displayLabel="Collection">Archives Collection</physicalLocation>
        <physicalLocation displayLabel="Repository">Arrowmont School of Arts and Crafts</physicalLocation>
        <physicalLocation displayLabel="Detailed Location"/>
        <physicalLocation displayLabel="City">Gatlinburg</physicalLocation>
        <physicalLocation displayLabel="State">Tennessee</physicalLocation>
    </location>

*I am not sold on whether retaining the Archives Collection string is necessary. I don't think the city and state are necessary if a URI is used instead of string.*

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .
    @prefix dbo: <http://dbpedia.org/ontology/> .

    <https://example.org/objects/1> relators:rps <http://id.loc.gov/authorities/names/no2001080757> ;
        dbo:collection "Archives Collection" .

url with a preview
^^^^^^^^^^^^^^^^^^

The URIs referenced are relative to our current system and would not be migrated. Translating this to RDF would be self-referential and not descriptive metadata.

**This can be dropped.**

https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A9999

.. code-block:: xml

    <location>
        <url access="object in context" usage="primary display">https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A9999</url>
        <url access="preview">https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A9999/datastream/TN/view</url>
    </location>

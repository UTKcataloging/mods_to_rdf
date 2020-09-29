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

    <https://example.org/objects/1>
        relators:rps <http://id.loc.gov/authorities/names/no2017033007> .

physicalLocation as string (special collections)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

https://digital.lib.utk.edu/collections/islandora/object/roth:4245/datastream/MODS/view

.. code-block:: xml

    <location>
        <physicalLocation>University of Tennessee, Knoxville. Special Collections</physicalLocation>
    </location>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .

    <https://example.org/objects/1>
        relators:rps <http://id.loc.gov/authorities/names/no2014027633> .

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

    <https://example.org/objects/1>
        relators:rps <http://id.loc.gov/authorities/names/n80003889> .

physicalLocation and shelfLocator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In cases the physical location is under the purview of University of Tennessee Libraries or University of Tennessee Libraries Special Collections, we will opt to drop shelfLocator strings.

https://digital.lib.utk.edu/collections/islandora/object/scopes:1258/datastream/MODS/view

.. code-block:: xml

    <location>
        <physicalLocation valueURI="http://id.loc.gov/authorities/names/no2014027633">University of Tennessee, Knoxville. Special Collections</physicalLocation>
        <shelfLocator>Box 5, Folder 8</shelfLocator>
    </location>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .

    <https://example.org/objects/1>
        relators:rps <http://id.loc.gov/authorities/names/no2014027633> .

We will translate that shelfLocator string to a skos:note if outside UT Libraries.

https://digital.lib.utk.edu/collections/islandora/object/volvoices:2136/datastream/MODS/view

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

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .

    <https://example.org/objects/1>
        relators:rps "Cleveland State Community College" ;
        skos:note "Shelf locator: Photograph Collection 2, People" .

physicalLocation with holdingSimple and holdingExternal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All of extra data under the holdingExternal subelement can be dropped.

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
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .

    <https://example.org/objects/1>
        relators:rps "University of Memphis. Special Collections" ;
        skos:note "Shelf locator: Manuscript Number 5" .

physicalLocation with displayLabel="Address"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We will opt to drop physicalLocation subelements with a displayLabel of *Address*.

https://digital.lib.utk.edu/collections/islandora/object/arrow:58/datastream/MODS/view

.. code-block:: xml

    <location>
        <physicalLocation>Pi Beta Phi Fraternity</physicalLocation>
        <physicalLocation displayLabel="Address">1154 Town and Country Commons Drive, Town and Country, Missouri 63017</physicalLocation>
        <shelfLocator>Box 36, Folder 14</shelfLocator>
    </location>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .

    <https://example.org/objects/1>
        relators:rps "Pi Beta Phi Fraternity" ;
        skos:note "Shelf locator: Box 36, Folder 14" .

physicalLocation with displayLabel attributes for Collection and Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have some cases *arrowmont* and *arrsimple* where a displayLabel="Collection" contains a string of **Archives Collection**. In these instances, *dbo:collection* will be used to retain that information. Other than *displayLabel="Repository"*, All other physicalLocation subelements with a displayLabel will be dropped.

https://digital.lib.utk.edu/collections/islandora/object/arrowmont%3A208/datastream/MODS/view

.. code-block:: xml

    <location>
        <physicalLocation displayLabel="Collection">Archives Collection</physicalLocation>
        <physicalLocation displayLabel="Repository">Arrowmont School of Arts and Crafts</physicalLocation>
        <physicalLocation displayLabel="Detailed Location"/>
        <physicalLocation displayLabel="City">Gatlinburg</physicalLocation>
        <physicalLocation displayLabel="State">Tennessee</physicalLocation>
    </location>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .
    @prefix dbo: <http://dbpedia.org/ontology/> .

    <https://example.org/objects/1>
        relators:rps <http://id.loc.gov/authorities/names/no2001080757> ;
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

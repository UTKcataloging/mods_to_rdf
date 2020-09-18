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

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .
    @prefix opaque: <http://opaquenamespace.org/ns/> .

    <https://example.org/objects/1> relators:rps <http://id.loc.gov/authorities/names/no2014027633> ;
        opaque:locationShelfLocator "Box 5, Folder 8" .

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
    @prefix opaque: <http://opaquenamespace.org/ns/> .

    <https://example.org/objects/1> relators:rps "University of Memphis. Special Collections" ;
        opaque:locationShelfLocator "Manuscript Number 5" .

physicalLocation with displayLabel="Address"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

https://digital.lib.utk.edu/collections/islandora/object/arrow:58/datastream/MODS/view

.. code-block:: xml


    <location>
        <physicalLocation>Pi Beta Phi Fraternity</physicalLocation>
        <physicalLocation displayLabel="Address">1154 Town and Country Commons Drive, Town and Country, Missouri 63017</physicalLocation>
        <shelfLocator>Box 36, Folder 14</shelfLocator>
    </location>

*This is one where I'm not sure where to go with.*

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .
    @prefix opaque: <http://opaquenamespace.org/ns/> .

    <https://example.org/objects/1> relators:rps "Pi Beta Phi Fraternity" ;
        opaque:locationShelfLocator "Box 36, Folder 14" .


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

*These only occur in volvoices. Obviously, this is a case where the turtle object URIs will be relative to the new platform.*

https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A9999

.. code-block:: xml

    <location>
        <url access="object in context" usage="primary display">https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A9999</url>
        <url access="preview">https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A9999/datastream/TN/view</url>
    </location>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/> .

    <https://example.org/objects/1> edm:isShownAt <https://digital.lib.utk.edu/placeholder/shownat/uri> ;
        edm:preview <https://digital.lib.utk.edu/placeholder/preview/uri> ;
        edm:object <https://digital.lib.utk.edu/placeholder/object/uri> .

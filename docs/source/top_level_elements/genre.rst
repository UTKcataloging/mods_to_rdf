genre
=====

About
-----

This section describes the different values for :code:`genre` that we currently have in our Islandora repository.

genre[@authority = 'dct']
-------------------------

We will explore other options for records using `@authority = 'dct'` or uncontrolled vocabularies, e.g. mapping values as `typeOfResource`. Many of the records in Volunteer Voices have multiple `genre`s; e.g. `volvoices:14311 <https://digital.lib.utk.edu/collections/islandora/object/volvoices:14311/datastream/MODS/view>`_.

.. code-block:: xml

    <genre authority="dct">text</genre>
    <genre>letter</genre>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/> .
    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:type "text" ;
        edm:hasType "letter" .

Roughly 300 other records have more than two :code:`genre`s; e.g. `volvoices:11262 <https://digital.lib.utk.edu/collections/islandora/object/volvoices:11262/datastream/MODS/view>`_.

.. code-block:: xml

    <genre>notated music</genre>
    <genre authority="dct">still image</genre>
    <genre>sheet music</genre>

.. code-block:: turtle

    @prefix
genre[@authority = 'aat']
-------------------------

:code:`genre[@authority = 'aat']` appears in the Archivision collection and uses a `@valueURI` for controlled vocabulary; e.g. `archivision:404 <https://digital.lib.utk.edu/collections/islandora/object/archivision:404/datastream/MODS/view>`_.

.. code-block:: xml

    <genre authority="aat" valueURI="http://vocab.getty.edu/aat/300021140">Renaissance</genre>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/> .

    <https://example.org/object/1> edm:hasType <http://vocab.getty.edu/aat/300021140> .

genre[@authority = 'lcsh']
--------------------------

Used in the Archivision and Charlie Daniel collections; e.g. `cDanielCartoon:455 <https://digital.lib.utk.edu/collections/islandora/object/cDanielCartoon:455/datastream/MODS/view>`_.

.. code-block:: xml

    <genre authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85040974">Editorial cartoons</genre>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/object/1> dcterms:type <http://id.loc.gov/authorities/subjects/sh85040974> .

and `archivision:1754 <https://digital.lib.utk.edu/collections/islandora/object/archivision:1754/datastream/MODS/view>`_.

.. code-block:: xml

    <genre authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85139020">Twentieth century</genre>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/object/1> dcterms:type <http://id.loc.gov/authorities/subjects/sh85040974> .


genre[@authority = 'lcgft']
---------------------------

Appears once in Kefauver Crime Documents (`ekcd:611 <https://digital.lib.utk.edu/collections/islandora/object/ekcd:611/datastream/MODS/view>`), otherwise is present in Arrowmont, Van Vactor, and VP Moore.

.. code-block:: xml

    <genre authority="lcgft" valueURI="http://id.loc.gov/authorities/genreForms/gf2014026131">Newsletters</genre>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/object/1> dcterms:type <http://id.loc.gov/authorities/genreForms/gf2014026131> .

In 124 of the records in the VP Moore collection, with `@authority='lcgft'`, the `@authorityURI = 'http://id.loc.gov/authorities/genreForms'` is used; e.g. `vpmoore:50 <https://digital.lib.utk.edu/collections/islandora/object/vpmoore:50/datastream/MODS/view>`_.

.. code-block:: xml

    <genre authority="lcgft" authorityURI="http://id.loc.gov/authorities/genreForms" valueURI="http://id.loc.gov/authorities/genreForms/gf2014026173">Scrapbooks</genre>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/object/1> dcterms:type <http://id.loc.gov/authorities/genreForms/gf2014026173> .

genre[@authority = 'lcmpt']
---------------------------

:code:`@authority = 'lcmpt'` is used in the Van Vactor collection to express genre/performance medium instrumentation information; e.g. `vanvactor:12350 <https://digital.lib.utk.edu/collections/islandora/object/vanvactor:12350/datastream/MODS/view>`_.

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
    @prefix gnd: <https://d-nb.info/standards/elementset/gnd#> .

    <https://example.org/object/1>
        gnd:playedInstrument <http://id.loc.gov/authorities/performanceMediums/mp2013015074> ;
        gnd:playedInstrument <http://id.loc.gov/authorities/performanceMediums/mp2013015342> ;
        gnd:playedInstrument <http://id.loc.gov/authorities/performanceMediums/mp2013015748> ;
        gnd:playedInstrument <http://id.loc.gov/authorities/performanceMediums/mp2013015540> ;
        dcterms:type <http://id.loc.gov/authorities/genreForms/gf2014027156> ;
        dcterms:type <http://id.loc.gov/authorities/genreForms/gf2014026956> ;
        dcterms:type <http://id.loc.gov/authorities/genreForms/gf2014026097> ;
        dcterms:type <http://id.loc.gov/authorities/subjects/sh99001779> .

genre[@authority = 'lctgm']
---------------------------

This appears on a few records in Arrowmont and on two collection-level records (humbug and uarc); e.g. `arrowmont:208 <https://digital.lib.utk.edu/collections/islandora/object/arrowmont:208/datastream/MODS/view>`_.

.. code-block:: xml

    <genre authority="lctgm" valueURI="http://www.loc.gov/pictures/item/tgm009266/">scrapbooks</genre>

We won't be migrating these values.

genre[@valueURI = '']
---------------------

There are ~190 records in the Smokies Postcards collection that have empty :code:`genre` elements, and empty :code:`@valueURI` attributes; e.g. `100233:1 <https://digital.lib.utk.edu/collections/islandora/object/100233:1/datastream/MODS/view>`_.

.. code-block:: xml

   <genre valueURI=""/>

We should drop these elements.
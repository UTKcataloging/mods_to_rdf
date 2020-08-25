genre
=====

About
-----

This section describes the different values for `genre` that we currently have in our Islandora repository.

genre[@authority = 'dct']
-------------------------

Many of the records in Volunteer Voices have multiple `genre`s; e.g. `volvoices:14311 <https://digital.lib.utk.edu/collections/islandora/object/volvoices:14311/datastream/MODS/view>`:_

.. code-block:: xml

    <genre authority="dct">text</genre>
    <genre>letter</genre>

.. code-block:: turtle

    @prefix edm: <http://www.europeana.eu/schemas/edm/>

    <https://example.org/object/1> edm:hasType ____ ; # get dct URI
        edm:hasType "letter" .


Roughly 300 other records have more than two `genre`s; e.g. `volvoices:11262 <https://digital.lib.utk.edu/collections/islandora/object/volvoices:11262/datastream/MODS/view>`:_

.. code-block:: xml

    <genre>notated music</genre>
    <genre authority="dct">still image</genre>
    <genre>sheet music</genre>

genre[@authority = 'aat']
-------------------------

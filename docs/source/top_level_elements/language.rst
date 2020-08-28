language
========

About
_____
This section describes all the different types of language elements that we have in our Islandora repository right now.

language has languageTerm subelement with an @authority of "iso639-2b" and a @type of "text"
--------------------------------------------------------------------------------------------

https://digital.lib.utk.edu/collections/islandora/object/tatum%3A188/datastream/MODS/view

.. code-block:: xml

    <language>
        <languageTerm authority="iso639-2b" type="text">English</languageTerm>
    </language>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:language <http://id.loc.gov/vocabulary/iso639-2/eng> .

language has languageTerm subelement with an @authority of "iso639-2b" and a @type of "code"
--------------------------------------------------------------------------------------------

https://digital.lib.utk.edu/collections/islandora/object/ekcd:9/datastream/MODS/view

.. code-block:: xml

    <language>
        <languageTerm authority="iso639-2b" type="code">eng</languageTerm>
    </language>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:language <http://id.loc.gov/vocabulary/iso639-2/eng> .

language has multiple elements
------------------------------

Present for 11 total in utsmc

https://digital.lib.utk.edu/collections/islandora/object/utsmc:725/datastream/MODS/view

.. code-block:: xml

    <language>
        <languageTerm authority="iso639-2b" type="text">French</languageTerm>
    </language>
    <language>
        <languageTerm authority="iso639-2b" type="text">Italian</languageTerm>
    </language>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1>
        dcterms:language <http://id.loc.gov/vocabulary/iso639-2/fre> ;
        dcterms:language <http://id.loc.gov/vocabulary/iso639-2/ita> .

Present for 1 total in egypt

https://digital.lib.utk.edu/collections/islandora/object/egypt:59/datastream/MODS/view

.. code-block:: xml

    <language>
        <languageTerm type="code" authority="iso639-2b">eng</languageTerm>
    </language>
    <language>
        <languageTerm type="code" authority="iso639-2b">fre</languageTerm>
    </language>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1>
        dcterms:language <http://id.loc.gov/vocabulary/iso639-2/eng> ;
        dcterms:language <http://id.loc.gov/vocabulary/iso639-2/fre> .

language has language subelement with an @type of #text and value of "No linguistic content"
--------------------------------------------------------------------------------------------

https://digital.lib.utk.edu/collections/islandora/object/tdh:911/datastream/MODS/view

.. code-block:: xml

    <language>
        <languageTerm authority="iso639-2b" type="text">No linguistic content</languageTerm>
    </language>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:language <http://id.loc.gov/vocabulary/iso639-2/zxx> ;

language has language subelement with an @type = "code" and value of "zxx"
--------------------------------------------------------------------------

https://digital.lib.utk.edu/collections/islandora/object/tdh:911/datastream/MODS/view

.. code-block:: xml

    <language>
        <languageTerm type="code" authority="iso639-2b">zxx</languageTerm>
    </language>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:language <http://id.loc.gov/vocabulary/iso639-2/zxx> ;



language has language subelement without a stated @authority and a @code value of "fra"
---------------------------------------------------------------------------------------

Two questions here along with my proposed:

1. How do we handle any that have no stated authority?
2. Two volvoices objects use "fra". Is there a difference between fra and fre as codes?

https://digital.lib.utk.edu/collections/islandora/object/volvoices:9928/datastream/MODS/vieww

.. code-block:: xml

    <language>
        <languageTerm type="code">fra</languageTerm>
    </language>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:language <http://id.loc.gov/vocabulary/iso639-2/fre> ;

Special Note
------------
https://digital.lib.utk.edu/collections/islandora/object/collections:utsmc/datastream/MODS/view

The collection object for utsmc has the follow language XML. While it may not matter with it being a
collection level object, I wonder how we would approach this if it were something we actually did want
to migrate.

.. code-block:: xml

    <language>
        <languageTerm authority="iso639-2b" type="text">English</languageTerm>
        <languageTerm authority="iso639-2b" type="text">French</languageTerm>
        <languageTerm authority="iso639-2b" type="text">German</languageTerm>
        <languageTerm authority="iso639-2b" type="text">Italian</languageTerm>
        <languageTerm authority="iso639-2b" type="text">Spanish</languageTerm>
    </language>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1>
        dcterms:language <http://id.loc.gov/vocabulary/iso639-2/eng> ;
        dcterms:language <http://id.loc.gov/vocabulary/iso639-2/fre> ;
        dcterms:language <http://id.loc.gov/vocabulary/iso639-2/ger> ;
        dcterms:language <http://id.loc.gov/vocabulary/iso639-2/ita> ;
        dcterms:language <http://id.loc.gov/vocabulary/iso639-2/spa> .
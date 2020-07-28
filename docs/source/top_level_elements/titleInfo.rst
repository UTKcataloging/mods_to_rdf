titleInfo
===============

About
_____
This section describes all the different types of titleInfo elements that we have in our Islandora repository right now.

|

titleInfo has partName sub-element
----------------------------------

https://digital.lib.utk.edu/collections/islandora/object/sanborn:1194/datastream/MODS/view

.. code-block:: xml

    <titleInfo>
        <title>Knoxville -- 1917</title>
        <partName>Sheet 56</partName>
    </titleInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:title "Knoxville -- 1917, Sheet 56" .

|

titleInfo has nonSort sub-element
---------------------------------

https://digital.lib.utk.edu/collections/islandora/object/volvoices:2890/datastream/MODS/view

.. code-block:: xml

    <titleInfo>
        <nonSort>The </nonSort>
        <title>Guard at the Mountain Branch of the National Home for Disabled Volunteer Soldiers</title>
    </titleInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:title "The Guard at the Mountain Branch of the National Home for Disabled Volunteer Soldiers" .

|

Multiple titleInfo elements with one having a type of alternative
-----------------------------------------------------------------

https://digital.lib.utk.edu/collections/islandora/object/pcard00:100233/datastream/MODS/view

.. code-block:: xml

    <titleInfo>
        <title>Prussian heroes march</title>
    </titleInfo>
    <titleInfo type="alternative">
        <title>Prussian heroes: Prussen helden march</title>
    </titleInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:title "Prussian heroes march" ;
        dcterms:alternative "Prussian heroes: Prussen helden march" .

|

Multiple titleInfo elements with one having a partName sub-element, and a type of alternative
---------------------------------------------------------------------------------------------

https://digital.lib.utk.edu/collections/islandora/object/pcard00:100233/datastream/MODS/view

.. code-block:: xml

    <titleInfo>
        <title>Souvenir of Great Smoky Mountains National Park</title>
    </titleInfo>
    <titleInfo type="alternative">
        <title>Souvenir of Great Smoky Mountains National Park</title>
        <partName>Postcard 1</partName>
    </titleInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:title "Souvenir of Great Smoky Mountains National Park"  ;
        dcterms:alternative "Souvenir of Great Smoky Mountains National Park, Postcard 1" .

|

Multiple titleInfo elements with one having a partName sub-element, and a displayLabel
--------------------------------------------------------------------------------------

https://digital.lib.utk.edu/collections/islandora/object/womenbball:653/datastream/MODS/view

.. code-block:: xml

    <titleInfo supplied="yes">
        <title>Tennessee Lady Volunteers basketball media guide, 1984-1985</title>
    </titleInfo>
    <titleInfo type="alternative" displayLabel="Cover Title">
        <title>Tennessee Lady Vols 1984-85: reaching for the Summitt of women's basketball</title>
    </titleInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:title "[Tennessee Lady Volunteers basketball media guide, 1984-1985]"  ;
        dcterms:alternative "Tennessee Lady Vols 1984-85: reaching for the Summitt of women's basketball" .


https://digital.lib.utk.edu/collections/islandora/object/colloquy:202/datastream/MODS/view

.. code-block:: xml

    <titleInfo>
        <title>Great Smoky Mountains Colloquy: Volume 18, Number 2</title>
    </titleInfo>
    <titleInfo type="alternative" displayLabel="Also known as">
        <title>Colloquy</title>
    </titleInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:title "Great Smoky Mountains Colloquy: Volume 18, Number 2"  ;
        dcterms:alternative "Colloquy" .

|

Multiple titleInfo elements with one having a supplied attribute of yes
-----------------------------------------------------------------------

https://digital.lib.utk.edu/collections/islandora/object/roth:5342/datastream/MODS/view

.. code-block:: xml

    <titleInfo>
        <title>Norris Dam (Envelope 246) (12 of 12)</title>
    </titleInfo>
    [...]
    <titleInfo supplied="yes">
        <title>Norris Dam</title>
    </titleInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:title "[Norris Dam]" ;
            dcterms:alternative "Norris Dam (Envelope 246) (12 of 12)" .

https://digital.lib.utk.edu/collections/islandora/object/knoxgardens%3A139/datastream/MODS/view

.. code-block:: xml

    <titleInfo supplied="yes">
        <title>View of Mrs. Sanford's pond</title>
    </titleInfo>
    <titleInfo>
        <title>Mrs. A. F. Sanford</title>
    </titleInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:title "[View of Mrs. Sanford's pond]" ;
            dcterms:alternative "Mrs. A. F. Sanford" .

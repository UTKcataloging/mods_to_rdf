originInfo: dates
=================

About
-----

This section describes all of the different subelements of originInfo in our MODS.

Dates
-----

We have three different date-related subelements: dateCreated, dateIssued, and dateOther.

dateCreated
-----------

dateCreated has the widest range of possible values and attributes.

dateCreated[@encoding][@keyDate][@point]
----------------------------------------

.. code-block:: xml

    <originInfo>
      <dateCreated>1870-1913</dateCreated>
      <dateCreated encoding="edtf" keyDate="yes" point="start">1870</dateCreated>
      <dateCreated encoding="edtf" keyDate="yes" point="end">1913</dateCreated>
    </originInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:created "1870/1913" .


dateCreated[@encoding][@keyDate][@point][@qualifier]
----------------------------------------------------

.. code-block:: xml

    <originInfo>
      <dateCreated>approximately between 1900 and 1940</dateCreated>
      <dateCreated encoding="edtf" keyDate="yes" point="start" qualifier="approximate">1900</dateCreated>
      <dateCreated encoding="edtf" keyDate="yes" point="end">1940</dateCreated>
    </originInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:created "1900~/1940" .


Attributes on dateCreated
-------------------------

dateCreated[@encoding]
----------------------

dateCreated[@encoding] has two distinct values: "edtf" and "w3cdtf". "w3cdtf" appears in a smaller number of records; e.g. `arrowmont:698 <https://digital.lib.utk.edu/collections/islandora/object/arrowmont%3A698/datastream/MODS>`_:

.. code-block:: xml

    <originInfo>
        <dateCreated encoding="edtf" keyDate="yes" point="start">1910</dateCreated>
    </originInfo>

.. code-block:: xml

    <originInfo>
        <dateCreated encoding="w3cdtf" keyDate="yes" point="start">1941</dateCreated>
    </originInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:created "1910" .

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:created "1941" .


dateCreated[@keyDate]
---------------------

The keyDate attribute is always "yes".

.. code-block:: xml

    @keyDate = "yes"


dateCreated[@qualifier]
-----------------------

The qualifier attribute has three distinct values: "inferred", "approximate", and "questionable". It usually appears with other attributes but not always; e.g. `ekcd:95 <https://digital.lib.utk.edu/collections/islandora/object/ekcd:95/datastream/MODS>`_:

.. code-block:: xml

    <originInfo>
        <dateCreated qualifier="inferred">1955</dateCreated>
        <dateCreated encoding="edtf" keyDate="yes">1955</dateCreated>
    </originInfo>

.. code-block:: xml

    <originInfo>
        <dateCreated>Undated</dateCreated>
        <dateCreated encoding="edtf" keyDate="yes" point="start" qualifier="inferred">1910</dateCreated>
        <dateCreated encoding="edtf" keyDate="yes" point="end" qualifier="inferred">1955</dateCreated>
    </originInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:created "1955~" .

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:created "1910~/1955~" .

dateCreated[@point]
-------------------

The point attribute has two distinct values: "start" and "end". They are frequently, but not consistently paired; e.g. `volvoices:2152 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A2152/datastream/MODS>`_: and `volvoices:3849 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A3849/datastream/MODS>`_:

.. code-block:: xml

    <originInfo>
        <dateCreated>1915</dateCreated>
        <dateCreated encoding="edtf" keyDate="yes" point="start">1915</dateCreated>
    </originInfo>
    <originInfo>
        <dateCreated>approximately between 1940 and 1950</dateCreated>
        <dateCreated encoding="edtf" keyDate="yes" point="start" qualifier="approximate">1940</dateCreated>
        <dateCreated encoding="edtf" keyDate="yes" point="end">1950</dateCreated>
    </originInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:created "1915/" .

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:created "1940~/1950" .

dateIssued
----------

`dateIssued`'s attributes and possible values follow the examples in `dateCreated` very closely. The primary difference between the two is that `dateIssued` is used in records describing serials.

dateIssued[@encoding][@keyDate][@point][@qualifier]
---------------------------------------------------

.. code-block:: xml

    <originInfo>
        <dateIssued>1934</dateIssued>
        <dateIssued encoding="edtf" keyDate="yes">1934</dateIssued>
    </originInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:issued "1934" .

.. code-block:: xml

    <originInfo>
        <dateIssued>1989</dateIssued>
        <dateIssued encoding="edtf">1989-23</dateIssued>
    </originInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:issued "1989-23" . # display as 'Spring, 1989'

.. code-block:: xml

    <originInfo>
        <dateIssued qualifier="approximate">1954</dateIssued>
        <dateIssued encoding="edtf" keyDate="yes" qualifier="approximate">1954</dateIssued>
    </originInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:issued "1954~" .

An example of multiple date elements, `volvoices:2993 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A2993>`:_

.. code-block:: xml

    <originInfo>
      <dateCreated>1948-01</dateCreated>
      <dateCreated encoding="edtf" keyDate="yes">1948-01</dateCreated>
      <dateIssued encoding="edtf" keyDate="yes" qualifier="approximate">1948</dateIssued>
    </originInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:created "1948-01" ;
        dcterms:issued "1948~" .

dateOther
---------

dateOther is rarely used (it appears in ~2700 records).

An example where converting the string value would be necessary: `kintner:56 <https://digital.lib.utk.edu/collections/islandora/object/kintner%3A56>`_:

.. code-block:: xml

    <originInfo>
        <dateOther>1974 December 10</dateOther>
    </originInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:date "1974-12-10" .

The Archivision collection uses `dateOther` to indicate dates of remodeling or architectural changes.

.. code-block:: xml

    <originInfo>
        <publisher>Archivision, Inc.</publisher>
        <dateCreated>founded 314; rebuilt and remodelled between 440-1885</dateCreated>
        <dateCreated encoding="edtf" keyDate="yes">314</dateCreated>
        <dateOther encoding="edtf" point="start">440</dateOther>
        <dateOther encoding="edtf" point="end">1885</dateOther>
    </originInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:created "314" ;
        dcterms:date "440/1885" .


copyrightDate
-------------

This value appears once in our MODS, in `calahan:1 <https://digital.lib.utk.edu/collections/islandora/object/calahan%3A1>`_:

.. code-block:: xml

    <originInfo>
        <dateCreated>undated</dateCreated>
        <copyrightDate>1941</copyrightDate>
    </originInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:created "undated" ;
        dcterms:dateCopyrighted "1941" .
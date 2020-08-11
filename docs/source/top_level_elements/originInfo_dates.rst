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
    <originInfo>
        <dateCreated encoding="w3cdtf" keyDate="yes" point="start">1941</dateCreated>
    </originInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:created "1910/" .


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
    <originInfo>
        <dateCreated>Undated</dateCreated>
        <dateCreated encoding="edtf" keyDate="yes" point="start" qualifier="inferred">1910</dateCreated>
        <dateCreated encoding="edtf" keyDate="yes" point="end" qualifier="inferred">1955</dateCreated>
    </originInfo>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> dcterms:created "1910~/1955~" .


dateCreated[@point]
-------------------

The point attribute has two distinct values: "start" and "end". They are frequently, but not consistently paired; e.g. `volvoices:2152 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A2152/datastream/MODS>`_: and `volvoices:3849 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A3849/datastream/MODS>`_:

..code-block:: xml

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

    <https://example.org/objects/1> dcterms:created "1870/1913" .
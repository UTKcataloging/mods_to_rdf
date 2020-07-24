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



dateCreated[@encoding][@keyDate][@point][@qualifier]
----------------------------------------------------

.. code-block:: xml

    <originInfo>
      <dateCreated>approximately between 1900 and 1940</dateCreated>
      <dateCreated encoding="edtf" keyDate="yes" point="start" qualifier="approximate">1900</dateCreated>
      <dateCreated encoding="edtf" keyDate="yes" point="end">1940</dateCreated>
    </originInfo>


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


dateCreated[@keyDate]
---------------------

The keyDate attribute is always "yes".

.. code-block:: xml

    @keyDate = "yes"


dateCreated[@qualifier]
-----------------------

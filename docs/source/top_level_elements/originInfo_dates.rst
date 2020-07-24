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
---------

dateCreated[@encoding] has two distinct values:

.. code-block:: xml

    <dateCreated encoding="edtf"/>
    <dateCreated encoding="w3cdtf"/>

@keyDate
--------

The keyDate attribute is always "yes".

.. code-block:: xml

    @keyDate = "yes"




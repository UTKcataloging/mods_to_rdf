classification
==============

About
-----

This section describes all the different types of classifications that we have in our Islandora repository right now.

No authority
------------

A few records have classifications with no authorities like `tenngirl:977 <https://digital.lib.utk.edu/collections/islandora/object/tenngirl:977/datastream/MODS>`_

While no authority is present, these are still all `lcc`.

.. code-block:: xml

    <classification>LD5296 .W6</classification>

Values with years
-----------------

Some records have values with years that need to be removed because these values aren't consistent with classification
values. The values present currently are shelfLocators rather than purely subject-focused values. Islandora's
recommendation to map classification values to dc:subject highlights this focus. An example record that requires edits
is `harp:1 <https://digital.lib.utk.edu/collections/islandora/object/harp%3A1/datastream/MODS>`_

.. code-block:: xml

    <classification authority="lcc">M2117. H25 1857</classification>

With an authority
-----------------

All others have lcc as an authority like `agrtfhs:2275 <https://digital.lib.utk.edu/collections/islandora/object/agrtfhs:2275/datastream/MODS>`_

.. code-block:: xml

    <classification authority="lcc">S1 .T43</classification>


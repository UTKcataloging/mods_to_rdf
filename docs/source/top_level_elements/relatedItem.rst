relatedItem
===========

About
-----

This section describes the usage of `relatedItem` in our MODS.

relatedItem[not(@*)]
--------------------

`relatedItem`, without attributes, is used 3245 times in Volunteer Voices.

.. code-block:: xml

    <relatedItem>
      <titleInfo>
        <title>Digital Collection: The Growth of Democracy in Tennessee: A Grassroots Approach to Volunteer Voices</title>
      </titleInfo>
    </relatedItem>

relatedItem[@displayLabel = "Project"][@type = "host"]
------------------------------------------------------

This XPath is typically used to indicate the digital project/digital collection for a given object; e.g. `roth:3346 <https://digital.lib.utk.edu/collections/islandora/object/roth:3346/datastream/MODS/view>`_.

.. code-block:: xml

    <relatedItem displayLabel="Project" type="host">
      <titleInfo>
        <title>Albert "Dutch" Roth Photograph Collection</title>
      </titleInfo>
    </relatedItem>

relatedItem[@type = "series"]
--------------------------------------------------------


Empty elements
--------------

Sometimes `relatedItem` will be empty; this only seems to be a problem in the Roth collection: e.g. `roth:3066 <https://digital.lib.utk.edu/collections/islandora/object/roth:3066/datastream/MODS/view>`_.

.. code-block:: xml

    <relatedItem type="series" displayLabel="Project"/>
    <relatedItem displayLabel="Collection" type="host">
      <identifier>MS.3334</identifier>
    </relatedItem>
    <relatedItem displayLabel="Project" type="host"/>

We should ignore these.

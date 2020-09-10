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

relatedItem[@type = "host"][@displayLabel = "Project"]
------------------------------------------------------

This XPath is typically used to indicate the digital project/digital collection for a given object; e.g. `roth:3346 <https://digital.lib.utk.edu/collections/islandora/object/roth:3346/datastream/MODS/view>`_.

.. code-block:: xml

    <relatedItem displayLabel="Project" type="host">
      <titleInfo>
        <title>Albert "Dutch" Roth Photograph Collection</title>
      </titleInfo>
    </relatedItem>

relatedItem[@type = "host"][@displayLabel = "Collection"]
---------------------------------------------------------

This XPath is typically used to indicate the archival collection for a given object; e.g. `heilman:261 <https://digital.lib.utk.edu/collections/islandora/object/heilman:261/datastream/MODS/view>`_.

    <relatedItem type="host" displayLabel="Project">
      <titleInfo>
        <title>Botanical Photography of Alan S. Heilman</title>
      </titleInfo>
    </relatedItem>
    <relatedItem type="host" displayLabel="Collection">
      <titleInfo>
        <title>Botany Department Photographs</title>
      </titleInfo>
      <identifier type="local">AR.0488</identifier>
    </relatedItem>

relatedItem[@type = "host"][@displayLabel = "project"]
------------------------------------------------------

This XPath is used 798 times and only appears in the Thompson Brothers Photograph Collection; e.g. `thompson:1 <https://digital.lib.utk.edu/collections/islandora/object/thompson:1/datastream/MODS/view>`_.

.. code-block:: xml

    <relatedItem type="host" displayLabel="project">
      <titleInfo>
        <title>Thompson Brothers Commercial Photographers</title>
      </titleInfo>
    </relatedItem>

relatedItem[@type = "host"][@displayLabel = "Digital Collection"]
-----------------------------------------------------------------

This XPath is used 362 times in the Children's Defense Fund collection: e.g. `cdf:7850 <https://digital.lib.utk.edu/collections/islandora/object/cdf:7850/datastream/MODS/view`_. Synonymous with `@displayLabel = "Project"`.

.. code-block:: xml

    <relatedItem displayLabel="Digital Collection" type="host">
      <titleInfo>
        <title>Children's Defense Fund</title>
      </titleInfo>
    </relatedItem>

relatedItem[@type = "host"][@displayLabel = "Project Part"]
-----------------------------------------------------------

This XPath is used 2632 times in the Arrowmont Collection; e.g. `arrow:1 <https://digital.lib.utk.edu/collections/islandora/object/arrow:1/datastream/MODS/view>`_.

.. code-block:: xml

    <relatedItem type="host" displayLabel="Project">
      <titleInfo>
        <title>From Pi Beta Phi to Arrowmont</title>
      </titleInfo>
    </relatedItem>
    <relatedItem displayLabel="Project Part" type="host">
      <titleInfo>
        <title>The Arrow of Pi Beta Phi</title>
      </titleInfo>
    </relatedItem>
    <relatedItem displayLabel="Bibliographic Citation" type="host">
      <titleInfo>
        <title>The Arrow, Volume 27, Number 1</title>
      </titleInfo>
    </relatedItem>

relatedItem[@type = "host"][@displayLabel = "Bibliographic Citation"]
---------------------------------------------------------------------

This XPath, closely related to the preceding `[@displayLabel = "Project Part"]`, also only appears 1264 times in the Arrowmont Collection - and only in the Arrow of Pi Beta Phi subcollection.

relatedItem[@type = "host"][@displayLabel = "Is Part Of"]
---------------------------------------------------------

This XPath is only used 449 in the Volunteer Voices collection; e.g. `volvoices:1846 <https://digital.lib.utk.edu/collections/islandora/object/volvoices:1846/datastream/MODS/view>`_.

.. code-block:: xml

    <relatedItem displayLabel="Project" type="host">
      <titleInfo>
        <title>Volunteer Voices</title>
      </titleInfo>
      <location>
        <url>http://digital.lib.utk.edu/collections/volvoices</url>
      </location>
    </relatedItem>
    <relatedItem displayLabel="Collection" type="host">
      <titleInfo>
        <title>Prints Collection</title>
      </titleInfo>
    </relatedItem>
    <relatedItem displayLabel="Is Part Of" type="host">
      <titleInfo>
        <title>Harper's Weekly</title>
      </titleInfo>
    </relatedItem>

relatedItem[@type = "series"][@displayLabel = "Project"]
--------------------------------------------------------

This XPath is typically used to indicate an object's archival series; e.g. `roth:1538 <https://digital.lib.utk.edu/collections/islandora/object/roth:1538/datastream/MODS/view>`_. It is only used in 2756 records in the Roth Collection. When populated, it supplies granular information about the archival collection.

.. code-block:: xml

    <relatedItem type="series" displayLabel="Project">
      <titleInfo>
        <title>Series II: Margaret Ann Roth Photographs and Other Materials, 1947 March 11-2002 December 14 (bulk 1947 March 11-1955 March 20). Sub-Series A: Photographs, 1947 March 11-1955 March 139</title>
      </titleInfo>
    </relatedItem>
    <relatedItem displayLabel="Collection" type="host">
      <titleInfo>
        <title>A. G. "Dutch" and Margaret Ann  Roth  Papers</title>
      </titleInfo>
      <identifier>MS.3334</identifier>
    </relatedItem>
    <relatedItem displayLabel="Project" type="host">
      <titleInfo>
        <title>Albert "Dutch" Roth Photograph Collection</title>
      </titleInfo>
    </relatedItem>

relatedItem/identifier[@type]
-----------------------------

This XPath's `type` attribute has three distinct values: `local`, `catalog`, and `pid`. The `pid` attribute is used in collection-level records to distinguish featured items.

`[@type = 'local']`, e.g. `heilman:261 <https://digital.lib.utk.edu/collections/islandora/object/heilman:261/datastream/MODS/view>`_.

.. code-block:: xml

    <relatedItem type="host" displayLabel="Collection">
      <titleInfo>
        <title>Botany Department Photographs</title>
      </titleInfo>
      <identifier type="local">AR.0488</identifier>
    </relatedItem>

`[@type = 'catalog']`, e.g. `vanvactor:1 <https://digital.lib.utk.edu/collections/islandora/object/vanvactor:1/datastream/MODS/view>`_.

.. code-block:: xml

    <relatedItem type="otherVersion">
      <titleInfo>
        <title>Gefunden</title>
      </titleInfo>
      <identifier type="catalog">M047</identifier>
    </relatedItem>
    <relatedItem displayLabel="Project" type="host">
      <titleInfo>
        <title>David Van Vactor Music Collection</title>
      </titleInfo>
    </relatedItem>
    <relatedItem displayLabel="Collection" type="host">
      <titleInfo>
        <title>David Van Vactor Papers</title>
      </titleInfo>
      <identifier>MS.1942</identifier>
      <location>
        <url>https://n2t.net/ark:/87290/v8pz5703</url>
      </location>
    </relatedItem>

`[@type =  'pid']`, e.g. `collections:agrutesc <https://digital.lib.utk.edu/collections/islandora/object/collections:agrutesc/datastream/MODS/view>`_.

    <relatedItem displayLabel="Featured Item">
      <titleInfo>
        <title>Barns</title>
      </titleInfo>
      <identifier type="pid">agrutesc:923</identifier>
      <abstract>Special circular showcasing barn designs for housing cattle or horses and mules.</abstract>
      <originInfo>
        <dateIssued>1948</dateIssued>
      </originInfo>
    </relatedItem>

relatedItem/location[physicalLocation]
--------------------------------------

This XPath appears once, in the record for the Charles Dabny collection; i.e. `collections:dabney <https://digital.lib.utk.edu/collections/islandora/object/collections:dabney/datastream/MODS/view>`_.

.. code-block:: xml

    <relatedItem displayLabel="Collection" type="host">
      <titleInfo>
        <title>University of Tennessee President's Papers, 1867-1954</title>
      </titleInfo>
      <identifier>AR.0001</identifier>
      <location>
        <physicalLocation authority="naf" valueURI="http://id.loc.gov/authorities/names/no2014027633">University of Tennessee, Knoxville. Special Collections</physicalLocation>
      </location>
    </relatedItem>

relatedItem/location
--------------------

This XPath `relatedItem/location/url` is used 8516 times, but only uses 33 distinct strings;

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

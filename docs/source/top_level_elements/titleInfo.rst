titleInfo
===============

About
_____
This section describes all the different types of titleInfo elements that we have in our Islandora repository right now.

**Case 1: Multiple titleInfo elements with one having a supplied attribute of yes**

https://digital.lib.utk.edu/collections/islandora/object/roth:5342/datastream/MODS/view

.. code-block:: xml

    <titleInfo>
        <title>Norris Dam (Envelope 246) (12 of 12)</title>
    </titleInfo>
    [...]
    <titleInfo supplied="yes">
        <title>Norris Dam</title>
    </titleInfo>

**Case 2: titleInfo has partName sub-element**

https://digital.lib.utk.edu/collections/islandora/object/sanborn:1194/datastream/MODS/view

.. code-block:: xml

    <titleInfo>
        <title>Knoxville -- 1917</title>
        <partName>Sheet 56</partName>
    </titleInfo>

**Case 3: titleInfo has nonSort sub-element**

https://digital.lib.utk.edu/collections/islandora/object/volvoices:2890/datastream/MODS/view

.. code-block:: xml

    <titleInfo>
        <nonSort>The </nonSort>
        <title>Guard at the Mountain Branch of the National Home for Disabled Volunteer Soldiers</title>
    </titleInfo>

**Case 4: Multiple titleInfo elements with one having a partName sub-element, and a type of alternative**

https://digital.lib.utk.edu/collections/islandora/object/pcard00:100233/datastream/MODS/view

.. code-block:: xml

    <titleInfo>
        <title>Souvenir of Great Smoky Mountains National Park</title>
    </titleInfo>
    <titleInfo type="alternative">
        <title>Souvenir of Great Smoky Mountains National Park</title>
        <partName>Postcard 1</partName>
    </titleInfo>

**Case 5: Multiple titleInfo elements with one having a partName sub-element, and a displayLabel**

https://digital.lib.utk.edu/collections/islandora/object/womenbball:653/datastream/MODS/view

.. code-block:: xml

    <titleInfo supplied="yes">
        <title>Tennessee Lady Volunteers basketball media guide, 1984-1985</title>
    </titleInfo>
    <titleInfo type="alternative" displayLabel="Cover Title">
        <title>Tennessee Lady Vols 1984-85: reaching for the Summitt of women's basketball</title>
    </titleInfo>

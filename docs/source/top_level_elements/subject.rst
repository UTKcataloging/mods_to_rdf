subject
=======

About
-----

This section describes all the different types of subjects that we have in our Islandora repository right now. Authorities
represented are dots, fast, agrovoc, geonames, lcsh, local, naf, tgm, and Wikidata. The "authority" lcna is also included,
though this refers to naf. Note that UTK does not currently have any records with mods:subject/mods:hierarchicalGeographic.
We also do not use mods:subject/mods:occupation, mods:subject/mods:genre, mods:subject/mods:titleInfo, or mods:subject/
mods:geographicCode.

None type
---------

Several elements contain null values. There are five within Tennessee Documentary History. Additional null subjects include
vpmoore:133 and adams 76. Most of roth seems to have null mods:subject/mods:name/mods:namePart values. It appears we might
have inserted some blank nodes using the Islandora form entry.

Here's an `example record - tdh:366 <https://digital.lib.utk.edu/collections/islandora/object/tdh%3A366/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <topic/>
    </subject>

Here's an example from `roth - roth:1587 <https://digital.lib.utk.edu/collections/islandora/object/roth%3A1587/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <name authority="" valueURI="">
            <namePart/>
            </name>
    </subject>

Topical subjects with @authority values but no URI
--------------------------------------------------
All of the Estes Kefauver Crime Documents have controlled LCSH terms within mods:subject/mods:topic, but no URI is given.
Effort should be made to add in the URIs for these subjects if possible. If not, they will need to be treated as strings.
This is confined to mods:subject/mods:topic

`Example record - ekcd: <https://digital.lib.utk.edu/collections/islandora/object/ekcd%3A7/datastream/MODS/view>`_

.. code-block:: xml

    <subject>
        <topic authority="lcsh">Juvenile delinquency</topic>
    </subject>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:subject "Juvenile delinquency" .


Topical and name subjects
-------------------------

Topical subjects without URIs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In migration, subjects with name and topical values will be treated in the same way. Their treatment will be the same
regardless of whether or not a URI or string is used.

Approximately 12,000 records have at least one subject without a URI. Note that this number is hard to pin down due to
inconsistencies with where @valueURI is placed on subject nodes. We'll need to treat any of these subjects that aren't able
to be reconciled as string values. For the postcard collection, the use of dots (Database of the Smokies) as the authority
makes it impossible to include a URI presently. Other collections with string values that could be
revisited are: Charlie Daniel Cartoon Collection, Ed Gamble Cartoon Collection, Football Programs, Insurance Company of
North America Records, the American Civil War Collection, Ramsey Family Papers, Tennessee Documentary History,
and Volunteer Voices.

Here's an `example record - gamble:123 <https://digital.lib.utk.edu/collections/islandora/object/gamble%3A123/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <topic>Environmentalism</topic>
    </subject>
    <subject>
        <topic>Factory and trade waste--Environmental aspects</topic>
    </subject>
    <subject>
        <topic>Pollution</topic>
    </subject>
    <subject>
        <topic>Knight</topic>
    </subject>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:subject "Environmentalism" ;
        dcterms:subject "Factory and trade waste--Environmental aspects" ;
        dcterms:subject "Pollution" ;
        dcterms:subject "Knight" .

Topical subjects with URIs
^^^^^^^^^^^^^^^^^^^^^^^^^^

Note the variations in where @valueURI is placed in the Xpaths listed below.

    mods:subject[@valueURI]/mods:topic
    mods:subject/mods:topic[@valueURI]

`acwiley:280 as an example of mods:subject[@valueURI]/mods:topic <https://digital.lib.utk.edu/collections/islandora/object/acwiley%3A280/datastream/MODS/view>`_

.. code-block:: xml

    <subject authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85147554">
        <topic>Women in art</topic>
    </subject>
    <subject authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85147447">
        <topic>Women artists</topic>
    </subject>
    <subject authority="tgm" valueURI="http://id.loc.gov/vocabulary/graphicMaterials/tgm008085">
        <topic>Portraits</topic>
    </subject>

`cdf:5384 as an example of mods:subject
/mods:topic[@valueURI] <https://digital.lib.utk.edu/collections/islandora/object/cdf%3A5384/datastream/MODS/view>`_

.. code-block:: xml

    <subject>
        <geographic valueURI="http://id.loc.gov/vocabulary/geographicAreas/n-us">United States</geographic>
    </subject>
    <subject>
        <topic valueURI="http://id.loc.gov/authorities/subjects/sh85023396">Child welfare</topic>
    </subject>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:subject "http://id.loc.gov/authorities/subjects/sh85023396" .

Name subjects with URIs
^^^^^^^^^^^^^^^^^^^^^^^

Like with other subjects, placement of URIs for name values is not consistent. Here are the variations:

      mods:subject[@valueURI]/mods:name/mods:namePart
      mods:subject/mods:name[@valueURI]/mods:namePart

There are also many instances in which only strings are available.

`Here's an example where the valueURI is on the subject element - wwiioh:2451 <https://digital.lib.utk.edu/collections/islandora/object/wwiioh%3A2451/datastream/MODS/view>`_.

.. code-block:: xml

    <subject authority="naf" valueURI="http://id.loc.gov/authorities/names/n85185770">
        <name>
            <namePart>United States. Army. Medical Corps</namePart>
        </name>
    </subject>

`Here's an example where the valueURI is on the name element - helser:24792 <https://digital.lib.utk.edu/collections/islandora/object/hesler%3A24792/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n87116131">
            <namePart>Atkinson, George Francis, 1854-1918</namePart>
        </name>
    </subject>
    <subject>
        <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n88144876">
            <namePart>Arthur, Joseph Charles, 1850-1942</namePart>
        </name>
    </subject>

When a URI is available it will be mapped as follows:

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:subject "http://id.loc.gov/authorities/names/n88144876" ;
        dcterms:subject "http://id.loc.gov/authorities/names/n87116131" .

Name subjects without URIs
^^^^^^^^^^^^^^^^^^^^^^^^^^

`Here's an example where only a string value is available - gamble:144 <https://digital.lib.utk.edu/collections/islandora/object/gamble%3A144/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <name>
            <namePart>Xerox Corporation</namePart>
        </name>
    </subject>

If only a string is available, like with , we will use that:

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:subject "Xerox Corporation" .

Temporal subjects
-----------------

None of our existing temporal subjects include URIs. Most will be treated as strings. These values are prominent in
Volunteer Voices and the Pi Beta Phi to Arrowmont collections.

`Example of temporal subject - volvoices:1833 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A1833/datastream/MODS/view>`_.

.. code-block:: xml

    <subject displayLabel="Tennessee Social Studies K-12 Eras in American History">
        <temporal>Era 9 - Postwar United States (1945-1970's)</temporal>
    </subject>


.. code-block:: turtle

    @prefix schema: <http://schema.org/> .

    <https://example.org/objects/1> schema:temporalCoverage "Era 9 - Postwar United States (1945-1970's)" .

In addition to these textual values, UTK does have temporal subjects that share numeric dates in EDTF format. These are
primarily from the Volunteer Voices collection. `Here's an example record - volvoices:2945 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A2945/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <temporal>1970-09-30</temporal>
    </subject>

.. code-block:: turtle

    @prefix schema: <http://schema.org/> .

    <https://example.org/objects/1> schema:temporalCoverage "1970-09-30" .

Geographic subjects
-------------------

UTK has geographic subjects with and without URIs. Like with other elements, the placement of the URIs is not consistent.
URIs will be used when present, but strings can be used when there is no URI.

    mods:subject[@valueURI]/mods:geographic
    mods:subject/mods:geographic[@valueURI]

`Here's an example where the URI is present on the subject - webster:1127 <https://digital.lib.utk.edu/collections/islandora/object/webster%3A1127/datastream/MODS/view>`_.

.. code-block:: xml

    <subject authority="geonames" valueURI="http://sws.geonames.org/4050810">
        <geographic>The Sawteeth</geographic>
        <cartographics>
            <coordinates>35.64342, -83.36237</coordinates>
        </cartographics>
    </subject>
    <subject authority="geonames" valueURI="http://sws.geonames.org/4609260">
        <geographic>Brushy Mountain</geographic>
        <cartographics>
            <coordinates>35.67787, -83.43016</coordinates>
    </cartographics>
    </subject>
    <subject authority="lcsh" valueURI="http://id.loc.gov/authorities/subjects/sh85057008">
        <geographic>Great Smoky Mountains (N.C. and Tenn.)</geographic>
    </subject>

`Here's an example where the URI is present on the geographic element - roth:2165 <https://digital.lib.utk.edu/collections/islandora/object/roth%3A2165/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <geographic authority="geonames" valueURI="http://sws.geonames.org/4178924/about.rdf">Yulee Sugar Mill Ruins Historic State Park</geographic>
    </subject>

Regardless of URI placement, we will map the values the same. Note that if the geographic term includes coordinates and
a geonames URI, we will drop the coordinates. More information on this is given in the Coordinates section following this
section. Below is the decision for webster:1127.

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:spatial <http://sws.geonames.org/4050810> ;
        dcterms:spatial <http://sws.geonames.org/4609260> ;
        dcterms:spatial <http://id.loc.gov/authorities/subjects/sh85057008> .

If only strings are present, like with volvoices:14173 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A14173/datastream/MODS/view>`_, then the string value will be kept.

.. code-block:: xml

    <subject>
        <geographic>Covington (Tenn.)</geographic>
    </subject>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:spatial "Covington (Tenn.)" .

Coordinates
-----------

There are a total of **702 unique coordinate values** in UTK's collections. Many are associated with geonames terms,
but there are 8 coordinates associated with Library of Congress terms. These terms are "Great Smoky Mountains
National Park (N.C. And Tenn.)", "Knoxville (Tenn.)", "Sevier County (Tenn.)", "Dickson County (Tenn.)", "Hardin County (Tenn.)",
"Bluff City (Tenn.)", and "Saint Andrews (Tenn.)". In addition, there are **120 geographic names that are not associated**
**with an authority** through the use of a URI, but they contain coordinates. The following lists some: "Abrams Creek", "Anthony Creek (Tenn.)",
"Arcadia Dam (Okla.)", "Arch Rock", "Arizona", "Arkansas", "Becky Cable House (Tenn.)", "Boston (Mass.)", "Bote Mountain Trail (Tenn.)",
"Bristol (Tenn.)", "Cades Cove Campground (Tenn.)", "Cades Cove Loop Road (Tenn.)", "Cades Cove Picnic Area (Tenn.)",
"Calderwood Dam (Tenn.)", "California", "Chattanooga (Tenn.)", "Cherokee Orchard (Tenn.)", "Chestnut Flats", "Chilhowee (Extinct city)",
"Chimney Tops", "Chimney Tops (Tenn.)", "Chimney Tops Foot Bridge (Tenn.)", "Chimney Tops Trail", "Clingmans Dome Road",
"Davenport Gap (Tenn.)", "Deals Gap (Tenn.)", "Dry Sluice Gap (Tenn.)", "Dry Valley (Tenn.)", "Elijah Oliver Place (Tenn.)",
"Fighting Creek Gap (Tenn.)", "Florida", "Fontana Dam (N.C.)", "Foothills Parkway", "Forge Creek", "Forney Ridge Parking Lot (N.C.)",
"Fort George Site", "Fort Manuel Site", "Fowler (Kan.)", "Gatlinburg (Tenn.)", "Greenbrier Pinnacle (Tenn.)", "Gregory Bald (Tenn.)",
"Guyot, Mount (Tenn.)", "Harrison, Mount (Tenn.)", "Headrick Chapel (Tenn.)", and many more.

For those geographic names associated with geonames through a URI, there is arguably no need to migrate the coordinates
as a string value as these can be retrieved using the URI at any time.

`Here's an example record - webster:1005 <https://digital.lib.utk.edu/collections/islandora/object/webster%3A1005/datastream/MODS/view>`_.

.. code-block:: xml

    <subject authority="geonames" valueURI="https://sws.geonames.org/4630912">
        <geographic>House Mountain</geographic>
        <cartographics>
            <coordinates>36.11175, -83.76657</coordinates>
        </cartographics>
    </subject>

All that is needed in this case is to bring over the URI.

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:spatial <https://sws.geonames.org/4630912> .

Given the extent of coordinates that cannot be retrieved using a URI (120), a separate solution is needed to preserve these values.
`Here's an example record - derris:610 <https://digital.lib.utk.edu/collections/islandora/object/derris%3A610/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <geographic>Becky Cable House (Tenn.)</geographic>
        <cartographics>
            <coordinates>35.58546, -83.84444</coordinates>
        </cartographics>
    </subject>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:spatial <https://sws.geonames.org/4630912> ;
        dcterms:spatial "35.58546, -83.84444" .

HierarchicalGeographic subjects
-------------------------------

A few instances of subject/hierarchicalGeographic existed in the Blount County Historical and Architectural Index, but these
have been removed as of summer 2020. We can safely ignore this element.


Subjects with attribute displayLabel
------------------------------------

The Volunteer Voices collection includes subjects with three different displayLabel values - Volunteer Voices Curriculum Topics,
Tennessee Social Studies K-12 Eras in American History, and Broad Topics. These subjects are currently given separate
facets in Islandora's metadata display. Discovery to the collection via two of these subject categories is also featured
on the `Tennessee State Library and Archives website <https://sos.tn.gov/products/tsla/volunteer-voices>`_ (Broad Topics
and Tennessee Social Studies K-12 Eras in American History). There are instances in which a value associated with one
of these topics is used, but the displayLabel has been left off. For instance `volvoices:11303 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A11303/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <topic>Jacksonian democracy and Tennessee's leadership role in the early republic .</topic>
    </subject>
    <subject>
        <topic>Music and Performing Arts.</topic>
    </subject>
    <subject>
        <topic>Frontier Settlement and Migration.</topic>
    </subject>
    <subject>
        <geographic>Expansion and Reform (1801-1861).</geographic>
    </subject>

The final subject/geographic value actually matches one of the values listed in the Tennessee Social Studies K-12 Eras
in American History. While it is placed in a geographic subject here in the XML, it should be in a temporal subject (as
the date range following the text suggests). One value is placed in subject/topic.The following values are all
of the exceptions:

1. Contemporary United States (1968-present).
2. Postwar United States (1945-1970).
3. The Great Depression and World War II (1929-1945).
4. The Emergence of Modern America (1890-1930).
5. The Development of the Industrial United States (1870-1900).
6. The Development of the Industrial United States (1870-1900). (in topic)
7. Expansion and Reform (1801-1861).
8. Revolution and the New Nation (1754-1820).
9. Colonization and Settlement (1585-1763).

We will want to remediate before migration, match on and transform these values during migration, or deal with them after migration. The string values
also don't exactly match the string values present in mods:topic[@displayLabel="Tennessee Social Studies K-12 Eras in American History"].
The eras ("Era 2 - ", "Era 3 - ", etc.) need to be added and the trailing periods removed for these to match.

.. code-block:: turtle

    @prefix schema: <http://schema.org/> .

    <https://example.org/objects/1> schema:temporalCoverage "Era 4 - Expansion and Reform (1801-1861)" .


`Example of @displayLabel="Broad Topics" - volvoices:4058 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A4058/datastream/MODS/view>`_.

.. code-block:: xml

    <subject displayLabel="Broad Topics">
        <topic>Frontier Settlement and Migration</topic>
    </subject>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:subject "Frontier Settlement and Migration" .

`Example of @displayLabel="Tennessee Social Studies K-12 Eras in American History" - volvoices:1833 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A1833/datastream/MODS/view>`_.

.. code-block:: xml

    <subject displayLabel="Tennessee Social Studies K-12 Eras in American History">
        <temporal>Era 9 - Postwar United States (1945-1970's)</temporal>
    </subject>

These will simply be treated as other temporal subjects are. Note that we only have strings for temporal subjects.

.. code-block:: turtle

    @prefix schema: <http://schema.org/> .

    <https://example.org/objects/1> schema:temporalCoverage "Era 9 - Postwar United States (1945-1970's)" .

`Example of @displayLabel="Volunteer Voices Curriculum Topics" - volvoices:2141 <https://digital.lib.utk.edu/collections/islandora/object/volvoices%3A2141/datastream/MODS/view>`_.

.. code-block:: xml

    <subject displayLabel="Volunteer Voices Curriculum Topics">
        <topic>Civil Rights movement in Tennessee</topic>
    </subject>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:subject "Civil Rights movement in Tennessee" .

Name values represented as subjects
-----------------------------------

The Arrowmont Simple Images collection includes mods:subject/mods:name/mods:namePart values with roleTerms. Rather than
nesting these within <subject>, they really should be treated more simply as names.

`Example record - arrsimple:344 <https://digital.lib.utk.edu/collections/islandora/object/arrsimple%3A344/datastream/MODS/view>`_

.. code-block:: xml

    <subject authority="local">
        <name>
            <namePart>Whaley, Aunt Lydia.</namePart>
        <role>
            <roleTerm authority="marcrelator" valueURI="http://id.loc.gov/vocabulary/relators/pht">Photographer</roleTerm>
        </role>
        </name>
    </subject>
    <name>
        <namePart>Unknown</namePart>
        <role>
            <roleTerm authority="marcrelator" valueURI="http://id.loc.gov/vocabulary/relators/pht">Photographer</roleTerm>
        </role>
    </name>

No Subjects
-----------

While not significant from a mapping standpoint, it is also helpful to note that **5085 records** have no subjects at all. From
a discovery and access standpoint, adding subject values to these records would be very helpful. The Albert "Dutch" Roth
photograph collection is the most significant offender. An `example record is roth:3095 <https://digital.lib.utk.edu/collections/islandora/object/roth%3A3095/datastream/MODS/view>`_
The nine records from the Arrowmont Curriculum Documents also do not include any subjects.
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

Bass Identifiers as Subjects
----------------------------

Presently site number identifiers for the Dr. William M. Bass III Collection are represented as topical subjects. The values
for these 73 items arguably belong in mods:identifier instead. There are already geographic subject terms in the data that
can be faceted upon if desired. The site identifiers are also present in the title of the documents.

Here's an `example record - bass:10081 <https://digital.lib.utk.edu/collections/islandora/object/bass%3A10081/datastream/MODS/view>`_.

.. code-block:: xml

    <subject>
        <topic>39SL4</topic>
    </subject>
    <subject>
        <geographic>Sully Site (S.D.)</geographic>
    </subject>
    <subject>
        <geographic>Oahe Reservoir Site (S.D. and N.D.)</geographic>
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


Topical subjects without URIs
-----------------------------

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

Subjects with URIs
------------------

Note the variations in where @valueURI is placed in the Xpaths listed below. The only subject element that never includes
a valueURI is <temporal>.

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

Also an example of mods:subject/mods:geographic[@valueURI]

.. code-block:: xml

    <subject>
        <geographic valueURI="http://id.loc.gov/vocabulary/geographicAreas/n-us">United States</geographic>
    </subject>
    <subject>
        <topic valueURI="http://id.loc.gov/authorities/subjects/sh85023396">Child welfare</topic>
    </subject>

    mods:subject[@valueURI]/mods:geographic
    mods:subject/mods:geographic[@valueURI]

    mods:subject[@valueURI]/mods:name/mods:namePart
    mods:subject/mods:name[@valueURI]/mods:namePart




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


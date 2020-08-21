subject
=======

About
-----

This section describes all the different types of subjects that we have in our Islandora repository right now. Authorities
represented are dots, fast, agrovoc, geonames

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


Subjects with @authority values but no URI
------------------------------------------
All of the Estes Kefauver Crime Documents have controlled LCSH terms within mods:subject/mods:topic, but no URI is given.
Effort should be made to add in the URIs for these subjects if possible. If not, they will need to be treated as strings.

.. code-block:: xml


Subjects without URIs
---------------------

Approximately 12,000 records have at least one subject without a URI. Note that this number is hard to pin down due to
inconsistencies with where @valueURI is placed on subject nodes. We'll need to treat any of these subjects that aren't able
to be reconciled as string values. For the postcard collection, the use of dots (Database of the Smokies) as the authority
makes it impossible to include a URI presently. A similar exception is Other collections with string values that could be
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


Note the following variations in Xpaths:

    mods:subject



No Subjects
-----------

While not significant from a mapping standpoint, it is also helpful to note that **5085 records** have no subjects at all. From
a discovery and access standpoint, adding subject values to these records would be very helpful. The Albert "Dutch" Roth
photograph collection is the most significant offender. An `example record is roth:3095 <https://digital.lib.utk.edu/collections/islandora/object/roth%3A3095/datastream/MODS/view>`_
The nine records from the Arrowmont Curriculum Documents also do not include any subjects.


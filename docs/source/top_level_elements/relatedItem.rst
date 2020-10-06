relatedItem
===========

About
-----

This section describes the usage of :code:`relatedItem` in our MODS.

relatedItem[not(@*)]
--------------------

:code:`relatedItem`, without attributes, is used 3245 times in Volunteer Voices.

.. code-block:: xml

    <relatedItem>
      <titleInfo>
        <title>Digital Collection: The Growth of Democracy in Tennessee: A Grassroots Approach to Volunteer Voices</title>
      </titleInfo>
    </relatedItem>

The relationship expressed here is structural in nature and should be reflected by default behavior in our DAMS.

relatedItem[@type = "host"][@displayLabel = "Project"]
------------------------------------------------------

This XPath is typically used to indicate the digital project/digital collection for a given object; e.g. `roth:3346 <https://digital.lib.utk.edu/collections/islandora/object/roth:3346/datastream/MODS/view>`_.

.. code-block:: xml

    <relatedItem displayLabel="Project" type="host">
      <titleInfo>
        <title>Albert "Dutch" Roth Photograph Collection</title>
      </titleInfo>
    </relatedItem>

The relationship expressed here is structural in nature and should be reflected by default behavior in our DAMS.

relatedItem[@type = "host"][@displayLabel = "Collection"]
---------------------------------------------------------

This XPath is typically used to indicate the archival collection for a given object; e.g. `heilman:261 <https://digital.lib.utk.edu/collections/islandora/object/heilman:261/datastream/MODS/view>`_.

.. code-block:: xml

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

.. code-block:: turtle

    @prefix dbo: <http://dbpedia.org/ontology/> .

    <https://example.org/objects/1> dbo:collection "Botany Department Photographs, AR.0488" .

relatedItem[@type = "host"][@displayLabel = "project"]
------------------------------------------------------

This XPath is used 798 times and only appears in the Thompson Brothers Photograph Collection; e.g. `thompson:1 <https://digital.lib.utk.edu/collections/islandora/object/thompson:1/datastream/MODS/view>`_.

.. code-block:: xml

    <relatedItem type="host" displayLabel="project">
      <titleInfo>
        <title>Thompson Brothers Commercial Photographers</title>
      </titleInfo>
    </relatedItem>

The relationship expressed here is structural in nature and should be reflected by default behavior in our DAMS.

relatedItem[@type = "host"][@displayLabel = "Digital Collection"]
-----------------------------------------------------------------

This XPath is used 362 times in the Children's Defense Fund collection: e.g. `cdf:7850 <https://digital.lib.utk.edu/collections/islandora/object/cdf:7850/datastream/MODS/view>`_. Synonymous with :code:`@displayLabel = "Project"`.

.. code-block:: xml

    <relatedItem displayLabel="Digital Collection" type="host">
      <titleInfo>
        <title>Children's Defense Fund</title>
      </titleInfo>
    </relatedItem>

The relationship expressed here is structural in nature and should be reflected by default behavior in our DAMS.

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

The relationship expressed here in :code:`[@type='host'][@displayLabel='Project Part']` is structural in nature and should be reflected by default behavior in our DAMS.

relatedItem[@type = "host"][@displayLabel = "Bibliographic Citation"]
---------------------------------------------------------------------

This XPath, closely related to the preceding :code:`[@displayLabel = "Project Part"]`, also only appears 1264 times in the Arrowmont Collection - and only in the Arrow of Pi Beta Phi subcollection.

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:bibliographicCitation "The Arrow, Volume 27, Number 1" .

relatedItem[@type = "host"][@displayLabel = "Is Part Of"]
---------------------------------------------------------

This XPath is only used 449 in the Volunteer Voices collection; e.g. `volvoices:1846 <https://digital.lib.utk.edu/collections/islandora/object/volvoices:1846/datastream/MODS/view>`_.

.. code-block:: xml

    <abstract>From: Harper's Weekly, v.9, no.463, November 11, 1865. At head, left, and right margins: "Boorish tailor, drunken beast, patriot, statesman, Jackson; Beastly instincts, demagogical habits, boorish mind; 'Not one word or act of his which a national democrat would not defend.'" Caption quotations located at four corners.</abstract>
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

:code:`[@displayLabel='Is Part Of']` may be sufficiently captured in other parts of the MODS (e.g. :code:`abstract`). Flip-flopping backwards, we should ignore this XPath.

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

.. code-block:: turtle

    @prefix dbo: <http://dbpedia.org/ontology/> .
    @prefix opaque: <http://opaquenamespace.org/ns/> .

    <https://example.org/objects/1> dbo:collection """A. G. "Dutch" and Margaret Ann Roth Papers, MS.3334""" ;
        opaque:memberOfArchivalSeries "Series II: Margaret Ann Roth Photographs and Other Materials, 1947 March 11-2002 December 14 (bulk 1947 March 11-1955 March 20). Sub-Series A: Photographs, 1947 March 11-1955 March 139" .

relatedItem/identifier[@type]
-----------------------------

This XPath's :code:`type` attribute has three distinct values: `local`, `catalog`, and `pid`. The `pid` attribute is used in collection-level records to distinguish featured items.

:code:`[@type = 'local']`, e.g. `heilman:261 <https://digital.lib.utk.edu/collections/islandora/object/heilman:261/datastream/MODS/view>`_.

.. code-block:: xml

    <relatedItem type="host" displayLabel="Collection">
      <titleInfo>
        <title>Botany Department Photographs</title>
      </titleInfo>
      <identifier type="local">AR.0488</identifier>
    </relatedItem>

.. code-block:: turtle

    @prefix dbo: <http://dbpedia.org/ontology/> .

    <https://example.org/objects/1> dbo:collection "Botany Department Photographs, AR.0488" .

:code:`[@type = 'catalog']`, e.g. `vanvactor:1 <https://digital.lib.utk.edu/collections/islandora/object/vanvactor:1/datastream/MODS/view>`_.

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

.. code-block:: turtle

    @prefix dbo: <http://dbpedia.org/ontology/> .
    @prefix opaque: <http://opaquenamespace.org/ns/> .

    <https://example.org/objects/1> dbo:collection "David Van Vactor Papers, MS.1942" ;
        dbo:isPartOf <https://n2t.net/ark:/87290/v8pz5703> ;
        opaque:sheetmusic_hostItem "Gefunden, M047" .

:code:`[@type =  'pid']`, e.g. `collections:agrutesc <https://digital.lib.utk.edu/collections/islandora/object/collections:agrutesc/datastream/MODS/view>`_.

.. code-block:: xml

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

Decision: we'll ignore these and find an alternate way to express/represent featured items for a collection.

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

This XPath :code:`relatedItem/location/url` is used 8516 times, but only uses 33 distinct strings; e.g. `ruskin:204 <https://digital.lib.utk.edu/collections/islandora/object/ruskin:204/datastream/MODS/view>`_.

.. code-block:: xml

    <relatedItem displayLabel="Collection" type="host">
      <titleInfo>
        <title>Ruskin Cooperative Association Collection</title>
      </titleInfo>
      <identifier>MS.0023</identifier>
      <location>
        <url>https://n2t.net/ark:/87290/v81g0jf1</url>
      </location>
    </relatedItem>

.. code-block:: turtle

    @prefix dbo: <http://dbpedia.org/ontology/> .

    <https://example.org/objects/1> dbo:isPartOf <https://n2t.net/ark:/87290/v81g0jf1> ;
        dbo:collection "Ruskin Cooperative Association Collection, MS.0023" .

relatedItem/abstract
--------------------

:code:`relatedItem/abstract` is used 865 times, across several collections; e.g. `sanborn:1196 <https://digital.lib.utk.edu/collections/islandora/object/sanborn:1196/datastream/MODS/view>`_.

.. code-block:: xml

    <relatedItem displayLabel="Project" type="host">
      <titleInfo>
        <title>Sanborn Fire Insurance Maps Collection</title>
      </titleInfo>
      <location>
        <url>http://digital.lib.utk.edu/collections/sanbornmapcollection</url>
      </location>
      <abstract>The Sanborn Fire Insurance Maps are a large-scale representation of the growth and layout of American cities. The University of Tennessee Libraries' collection currently provides digital versions of the four earliest sets of Knoxville maps - 1884, 1890, 1903, and 1917.</abstract>
    </relatedItem>

The values expressed in :code:`relatedItem/abstract` should be handled at the collection level. Do no migrate these.

relatedItem/name
----------------

:code:`relatedItem/name` appears 131 times, only in the Bass Collection, and only in :code:`relatedItem[@type = 'constituent']`; e.g. `bass:19644 <https://digital.lib.utk.edu/collections/islandora/object/bass:19644/datastream/MODS/view>`_.

.. code-block:: xml

    <relatedItem displayLabel="Project" type="host">
      <titleInfo>
        <title>The Dr. William M. Bass III Collection - The Bass Field Notes</title>
      </titleInfo>
    </relatedItem>
    <relatedItem displayLabel="Collection" type="host">
      <titleInfo>
        <title>Dr. William M. Bass III Collection</title>
      </titleInfo>
      <identifier type="local">MS.3689</identifier>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>M.B.P. weekly progress reports, Summer 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n83189337">
        <namePart>Bass, William M., 1928-</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project Weekly Report, June 24</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n84053297">
        <namePart>Stephenson, Robert L. (Robert Lloyd), 1919-</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>Archeological progress report no.8, Field season of 1963, December, 1963</title>
      </titleInfo>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>Archaeological progress report no.9, Field Season of 1964, November, 1964</title>
      </titleInfo>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report, Party no.1 - Kansas and Nebraska surveys, Report no.1-3, May 10-24, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/no2004018542">
        <namePart>Brown, Lionel A.</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report Party no.3 - Sully Burial analysis, Report no.1, 3-9, June 7, 22-August 2, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n83189337">
        <namePart>Bass, William M., 1928-</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report, Party #5 - Upper Yellowtail Reservoir, Report no.1-12, June 14-July 5-August 30, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/no90027536">
        <namePart>Husted, Wilfred M.</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report Party #10 - Dewey County Party, Report no.1-12, June 14-August 30, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n82020447">
        <namePart>Neuman, Robert W.</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report Party #12 - Davis Creek Site, Report no.1-12, June 14-August 30, 1963 [Numbering of the reports is off, went by dates]</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n87856030">
        <namePart>Bowers, Alfred W.</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n85031246">
        <namePart>Muller, Jon</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report, News from Lincoln, Report no.1-5, June 24-August 12, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n84053297">
        <namePart>Stephenson, Robert L. (Robert Lloyd), 1919-</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>University of South Dakota, Gavins Point Project no.2, Cooperators Party B, Report no.1-7, June 21-August 2, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/no2001006452">
        <namePart>Gant, Robert D.</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report, Party no.6 - Historic sites (Big Bend &amp; Oahe Res. Areas), Report no.1-10, June 22-August 24, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n81119648">
        <namePart>Smith, G. Hubert (George Hubert), 1908-1972</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report, Party no.7 - Pierre South Dakota, Report no.1-10, June 21-August 24, 1963 [numbering off, going by date]</title>
      </titleInfo>
      <name>
        <namePart>Jensen, Richard E.</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project Weekly Report, Parties no. 8 and 9 - La Roche and Chapelle Creek, Report no.1-11, June 21-September 3, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/no2004118058">
        <namePart>Hoffman, J. J. (John Jacob), 1931-</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report, Party no.11 - Moreau Party, Report no.2-11, June 21-August 30, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/no2004118055">
        <namePart>Mallory, Oscar L.</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>University of Kansas Milford Reservoir Archeological Party, Cooperators Party A, Report no.3, June 28, 1963</title>
      </titleInfo>
      <name>
        <namePart>Schock, Jack</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>Nebraska State Historical Society - National Science Foundation Logan Creek Project - Cooperators Party C, Report no.1, June 28, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n88243079">
        <namePart>Kivett, Marvin F.</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project Weekly report, Party no. 9 - Chapelle Creek, Report no.3-10, July 5-August 23, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n78078895">
        <namePart>Folan, William J.</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>
    <relatedItem type="constituent">
      <titleInfo>
        <title>1963 Missouri Basin Project weekly report, Party no. 4 - Garrison Diversion, Report no.1-6, July 26-August 30, 1963</title>
      </titleInfo>
      <name authority="naf" valueURI="http://id.loc.gov/authorities/names/n50038965">
        <namePart>Johnson, Elden</namePart>
        <role>
          <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
      </name>
    </relatedItem>

.. code-block:: turtle

    @prefix rdfs: <https://www.w3.org/TR/rdf-schema/> .
    @prefix pcdm: <http://pcdm.org/models#> .
    @prefix dbo: <http://dbpedia.org/ontology/> .
    @prefix opaque: <http://opaquenamespace.org/ns/> .
    @prefix dcterms: <http://purl.org/dc/terms/> .
    @prefix relators: <http://id.loc.gov/vocabulary/relators> .

    <https://example.org/collections/1> a pcdm:Collection ;
        rdfs:label "The Dr. William M. Bass III Collection - The Bass Field Notes" .

    <https://example.org/objects/1> dcterms:isPartOf <https://example.org/collections/1> ;
        dbo:collection "Dr. William M. Bass III Collection , MS.3689" ;
        dcterms:tableOfContents "M.B.P. weekly progress reports, Summer 1963 (Bass, William M., 1928-) -- Archeological progress report no.8, Field season of 1963, December, 1963 -- Archaeological progress report no.9, Field Season of 1964, November, 1964 -- 1963 Missouri Basin Project weekly report, Party no.1 - Kansas and Nebraska surveys, Report no.1-3, May 10-24, 1963 (Brown, Lionel A.) -- 1963 Missouri Basin Project weekly report Party no.3 - Sully Burial analysis, Report no.1, 3-9, June 7, 22-August 2, 1963 (Bass, William M., 1928-) -- 1963 Missouri Basin Project weekly report, Party #5 - Upper Yellowtail Reservoir, Report no.1-12, June 14-July 5-August 30, 1963 (Husted, Wilfred M.) -- 1963 Missouri Basin Project weekly report Party #10 - Dewey County Party, Report no.1-12, June 14-August 30, 1963 (Neuman, Robert W.) -- 1963 Missouri Basin Project weekly report Party #12 - Davis Creek Site, Report no.1-12, June 14-August 30, 1963 [Numbering of the reports is off, went by dates] (Bowers, Alfred W.) -- 1963 Missouri Basin Project weekly report, News from Lincoln, Report no.1-5, June 24-August 12, 1963 (Stephenson, Robert L. (Robert Lloyd), 1919-) -- University of South Dakota, Gavins Point Project no.2, Cooperators Party B, Report no.1-7, June 21-August 2, 1963 (Gant, Robert D.) -- 1963 Missouri Basin Project weekly report, Party no.6 - Historic sites (Big Bend & Oahe Res. Areas), Report no.1-10, June 22-August 24, 1963 (Smith, G. Hubert (George Hubert), 1908-1972) -- 1963 Missouri Basin Project weekly report, Party no.7 - Pierre South Dakota, Report no.1-10, June 21-August 24, 1963 [numbering off, going by date] (Jensen, Richard E.) -- 1963 Missouri Basin Project Weekly Report, Parties no. 8 and 9 - La Roche and Chapelle Creek, Report no.1-11, June 21-September 3, 1963 (Hoffman, J. J. (John Jacob), 1931-) -- 1963 Missouri Basin Project weekly report, Party no.11 - Moreau Party, Report no.2-11, June 21-August 30, 1963 (Mallory, Oscar L.) -- University of Kansas Milford Reservoir Archeological Party, Cooperators Party A, Report no.3, June 28, 1963 (Schock, Jack) -- Nebraska State Historical Society - National Science Foundation Logan Creek Project - Cooperators Party C, Report no.1, June 28, 1963 (Kivett, Marvin F.) -- 1963 Missouri Basin Project Weekly report, Party no. 9 - Chapelle Creek, Report no.3-10, July 5-August 23, 1963 (Folan, William J.) -- 1963 Missouri Basin Project weekly report, Party no. 4 - Garrison Diversion, Report no.1-6, July 26-August 30, 1963 (Johnson, Elden)" ;
        relators:cre <http://id.loc.gov/authorities/names/n83189337> ;
        relators:cre <http://id.loc.gov/authorities/names/n84053297> ;
        relators:cre <http://id.loc.gov/authorities/names/no2004018542> ;
        relators:cre <http://id.loc.gov/authorities/names/n83189337> ;
        relators:cre <http://id.loc.gov/authorities/names/no90027536> ;
        relators:cre <http://id.loc.gov/authorities/names/n82020447> ;
        relators:cre <http://id.loc.gov/authorities/names/n87856030> ;
        relators:cre <http://id.loc.gov/authorities/names/n85031246> ;
        relators:cre <http://id.loc.gov/authorities/names/n84053297> ;
        relators:cre <http://id.loc.gov/authorities/names/no2001006452> ;
        relators:cre <http://id.loc.gov/authorities/names/n81119648> ;
        relators:cre "Jensen, Richard E." ;
        relators:cre <http://id.loc.gov/authorities/names/no2004118058> ;
        relators:cre <http://id.loc.gov/authorities/names/no2004118055> ;
        relators:cre "Schock, Jack" ;
        relators:cre <http://id.loc.gov/authorities/names/n88243079> ;
        relators:cre <http://id.loc.gov/authorities/names/n78078895> ;
        relators:cre <http://id.loc.gov/authorities/names/n50038965> .


Note: this is an initial attempt at :code:`relatedItem[@type='constituent']` - I expect that we'll want to refine how we're modeling this kind of metadata.


Empty elements
--------------

Sometimes :code:`relatedItem` will be empty; this only seems to be a problem in the Roth collection: e.g. `roth:3066 <https://digital.lib.utk.edu/collections/islandora/object/roth:3066/datastream/MODS/view>`_.

.. code-block:: xml

    <relatedItem type="series" displayLabel="Project"/>
    <relatedItem displayLabel="Collection" type="host">
      <identifier>MS.3334</identifier>
    </relatedItem>
    <relatedItem displayLabel="Project" type="host"/>

We should ignore these.

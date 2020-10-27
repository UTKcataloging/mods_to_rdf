====
name
====

-----
About
-----

This section describes our use of the top level element name.

-------------------
Names and Roleterms
-------------------

A Bit of Background and the Importance of Derefenceable Marcrelators
====================================================================

In rdf, both the Samvera and Islandora communities recommend marcrelators to serve as the rdf property that relate names
to the digital object record.

We usually use `mods:name/mods:role/mods:roleTerm` to store a marcrelator text value, but not always.  Here is the unique
list of values we use for `mods:name/mods:role/mods:roleTerm`:

.. code-block:: python

    ['Addressee', 'Architect', 'Arranger', 'Artist', 'Associated', 'Associated name', 'Attributed', 'Attributed name', 'Author', 'Autographer', 'Cartographer', 'Choreographer', 'Client', 'Compiler', 'Composer', 'Contractor', 'Contributor', 'Copyright holder', 'Correspondent', 'Costume designer', 'Creator', 'Dedicatee', 'Depicted', 'Designer', 'Distributor', 'Donor', 'Editor', 'Engraver', 'Former owner', 'Honoree', 'Illustrator', 'Instrumentalist', 'Interviewee', 'Interviewer', 'Issuing body', 'Lithographer', 'Lyricist', 'Minute', 'Music copyist', 'Musical director', 'Originator', 'Other', 'Owner', 'Performer', 'Photographer', 'Printer', 'Printer of plates', 'Producer', 'Production company', 'Publisher', 'Set designer', 'Signer', 'Stage director', 'Stage manager', 'Standards body', 'Surveyor', 'Videographer', 'Witness', 'creator']

Similarly, here are the text values related to marc relators:

.. code-block:: python

    ['Abridger', 'Art copyist', 'Actor', 'Art director', 'Adapter', 'Author of afterword, colophon, etc.', 'Analyst', 'Animator', 'Annotator', 'Bibliographic antecedent', 'Appellee', 'Appellant', 'Applicant', 'Author in quotations or text abstracts', 'Architect', 'Artistic director', 'Arranger', 'Artist', 'Assignee', 'Associated name', 'Autographer', 'Attributed name', 'Auctioneer', 'Author of dialog', 'Author of introduction, etc.', 'Screenwriter', 'Author', 'Binding designer', 'Bookjacket designer', 'Book designer', 'Book producer', 'Blurb writer', 'Binder', 'Bookplate designer', 'Broadcaster', 'Braille embosser', 'Bookseller', 'Caster', 'Conceptor', 'Choreographer', 'Collaborator', 'Client', 'Calligrapher', 'Colorist', 'Collotyper', 'Commentator', 'Composer', 'Compositor', 'Conductor', 'Cinematographer', 'Censor', 'Contestant-appellee', 'Collector', 'Compiler', 'Conservator', 'Collection registrar', 'Contestant', 'Contestant-appellant', 'Court governed', 'Cover designer', 'Copyright claimant', 'Complainant-appellee', 'Copyright holder', 'Complainant', 'Complainant-appellant', 'Creator', 'Correspondent', 'Corrector', 'Court reporter', 'Consultant', 'Consultant to a project', 'Costume designer', 'Contributor', 'Contestee-appellee', 'Cartographer', 'Contractor', 'Contestee', 'Contestee-appellant', 'Curator', 'Commentator for written text', 'Distribution place', 'Defendant', 'Defendant-appellee', 'Defendant-appellant', 'Degree granting institution', 'Degree supervisor', 'Dissertant', 'Delineator', 'Dancer', 'Donor', 'Depicted', 'Depositor', 'Draftsman', 'Director', 'Designer', 'Distributor', 'Data contributor', 'Dedicatee', 'Data manager', 'Dedicator', 'Dubious author', 'Editor of compilation', 'Editor of moving image work', 'Editor', 'Engraver', 'Electrician', 'Electrotyper', 'Engineer', 'Enacting jurisdiction', 'Etcher', 'Event place', 'Expert', 'Facsimilist', 'Film distributor', 'Field director', 'Film editor', 'Film director', 'Filmmaker', 'Former owner', 'Film producer', 'Funder', 'First party', 'Forger', 'Geographic information specialist', 'Graphic technician', 'Host institution', 'Honoree', 'Host', 'Illustrator', 'Illuminator', 'Inscriber', 'Inventor', 'Issuing body', 'Instrumentalist', 'Interviewee', 'Interviewer', 'Judge', 'Jurisdiction governed', 'Laboratory', 'Librettist', 'Laboratory director', 'Lead', 'Libelee-appellee', 'Libelee', 'Lender', 'Libelee-appellant', 'Lighting designer', 'Libelant-appellee', 'Libelant', 'Libelant-appellant', 'Landscape architect', 'Licensee', 'Licensor', 'Lithographer', 'Lyricist', 'Music copyist', 'Metadata contact', 'Medium', 'Manufacture place', 'Manufacturer', 'Moderator', 'Monitor', 'Marbler', 'Markup editor', 'Musical director', 'Metal-engraver', 'Minute taker', 'Musician', 'Narrator', 'Opponent', 'Originator', 'Organizer', 'Onscreen presenter', 'Other', 'Owner', 'Panelist', 'Patron', 'Publishing director', 'Publisher', 'Project director', 'Proofreader', 'Photographer', 'Platemaker', 'Permitting agency', 'Production manager', 'Printer of plates', 'Papermaker', 'Puppeteer', 'Praeses', 'Process contact', 'Production personnel', 'Presenter', 'Performer', 'Programmer', 'Printmaker', 'Production company', 'Producer', 'Production place', 'Production designer', 'Printer', 'Provider', 'Patent applicant', 'Plaintiff-appellee', 'Plaintiff', 'Patent holder', 'Plaintiff-appellant', 'Publication place', 'Rubricator', 'Recordist', 'Recording engineer', 'Addressee', 'Radio director', 'Redaktor', 'Renderer', 'Researcher', 'Reviewer', 'Radio producer', 'Repository', 'Reporter', 'Responsible party', 'Respondent-appellee', 'Restager', 'Respondent', 'Restorationist', 'Respondent-appellant', 'Research team head', 'Research team member', 'Scientific advisor', 'Scenarist', 'Sculptor', 'Scribe', 'Sound designer', 'Secretary', 'Stage director', 'Signer', 'Supporting host', 'Seller', 'Singer', 'Speaker', 'Sponsor', 'Second party', 'Surveyor', 'Set designer', 'Setting', 'Storyteller', 'Stage manager', 'Standards body', 'Stereotyper', 'Technical director', 'Teacher', 'Thesis advisor', 'Television director', 'Television producer', 'Transcriber', 'Translator', 'Type designer', 'Typographer', 'University place', 'Voice actor', 'Videographer', 'Vocalist', 'Writer of added commentary', 'Writer of added lyrics', 'Writer of accompanying material', 'Writer of added text', 'Woodcutter', 'Wood engraver', 'Writer of introduction', 'Witness', 'Writer of preface', 'Writer of supplementary textual content']

I wrote a bit of code to compare these two lists and look for occurences that fall outside of marcrelators:

.. code-block:: python

    marc_relators = role_terms = for_review []

    with open("relators.txt", 'r') as relators:
        for relator in relators:
            marc_relators.append(relator.split('\t')[1].replace('\n', ''))

    with open('roleterms.txt', 'r') as roles:
        for role in roles:
            role_terms.append(role.replace('\n', ''))

    for term in role_terms:
        if term not in marc_relators:
            for_review.append(term)

    print(for_review)

The output of this is:

.. code-block:: python

    ['Associated', 'Attributed', 'Minute', 'creator']

Since these are not from marc relators, we need to do something with them.  We can use marcrelators and the text node
only for relationship building for everything else.

Suggestions
===========

Name Has a Marcrelator Roleterm
-------------------------------

Most records have a name with a marcrelator roleterm.

If the role term is associated with a marcrelator:

.. code-block:: xml

    <mods:name>
        <mods:namePart>Marre, Albert</mods:namePart>
        <mods:role>
            <mods:roleTerm authority="marcrelator" valueURI="http://id.loc.gov/vocabulary/relators/stm">Stage manager</mods:roleTerm>
        </mods:role>
    </mods:name>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1>
        relators:stm "Marre, Albert" .

Name Does Not have a Marcrelator Roleterm
-----------------------------------------

If the name does not have a marcrelator roleterm, we either need to fix or create a lookup table.

Associated Role Term
^^^^^^^^^^^^^^^^^^^^

There are 82 records with names that have malformed URIs and "Associated" role terms that should be mapped to
:code:`http://id.loc.gov/vocabulary/relators/asn`.

Here is the list of pids:

.. code-block:: python

    ['tdh:8754', 'tdh:8762', 'tdh:1471', 'tdh:1492', 'tdh:1374', 'tdh:1377', 'tdh:1314', 'tdh:1319', 'tdh:1329', 'tdh:1335', 'tdh:1349', 'tdh:1352', 'tdh:1356', 'tdh:1365', 'tdh:1368', 'tdh:1371', 'tdh:197', 'tdh:202', 'tdh:131', 'tdh:6951', 'tdh:7092', 'tdh:7001', 'tdh:7171', 'tdh:9334', 'tdh:9462', 'tdh:9380', 'tdh:9383', 'tdh:9374', 'tdh:9377', 'tdh:9407', 'tdh:9409', 'tdh:9412', 'tdh:9415', 'tdh:80', 'tdh:7287', 'tdh:7328', 'tdh:7423', 'tdh:9281', 'tdh:9154', 'tdh:9157', 'tdh:9232', 'tdh:9234', 'tdh:9237', 'tdh:9240', 'tdh:9185', 'tdh:9120', 'tdh:7560', 'tdh:8829', 'tdh:8835', 'tdh:9004', 'tdh:9038', 'tdh:9051', 'tdh:9064', 'tdh:8931', 'tdh:8787', 'tdh:8800', 'tdh:8343', 'tdh:8301', 'tdh:8307', 'tdh:5548', 'tdh:418', 'tdh:426', 'tdh:5330', 'tdh:5362', 'tdh:6907', 'tdh:5888', 'tdh:432', 'tdh:434', 'tdh:6774', 'tdh:6637', 'tdh:6670', 'tdh:6779', 'tdh:5632', 'tdh:6213', 'tdh:1561', 'tdh:1651', 'tdh:1583', 'tdh:7851', 'tdh:7814', 'tdh:7881', 'tdh:802', 'tdh:804']

Attributed Role Term
^^^^^^^^^^^^^^^^^^^^

There are 3 records with names that have malformed URIs and "Attributed" role terms that should be mapped to
:code:`http://id.loc.gov/vocabulary/relators/att`.

Here is the list of pids:

.. code-block:: python

    ['tdh:1362', 'tdh:691', 'tdh:6290']

Minute Role Term
^^^^^^^^^^^^^^^^

There is 1 record with names that have malformed URIs and "Minute" role terms that should be mapped to
:code:`http://id.loc.gov/vocabulary/relators/mtk`.

It is `tdh:186 <https://digital.lib.utk.edu/collections/islandora/object/tdh%3A186/>`_

creator Role Term
^^^^^^^^^^^^^^^^^

There are 86 records with names that have a "creator" role term that should be mapped to
:code:`http://id.loc.gov/vocabulary/relators/cre`.

Here is a list of the pids:

.. code-block:: python

    ['kintner:1', 'kintner:10', 'kintner:11', 'kintner:12', 'kintner:13', 'kintner:14', 'kintner:15', 'kintner:16', 'kintner:17', 'kintner:30', 'kintner:31', 'kintner:32', 'kintner:33', 'kintner:34', 'kintner:35', 'kintner:36', 'kintner:37', 'kintner:38', 'kintner:39', 'kintner:4', 'kintner:40', 'kintner:41', 'kintner:42', 'kintner:44', 'kintner:21', 'kintner:22', 'kintner:23', 'kintner:24', 'kintner:25', 'kintner:26', 'kintner:27', 'kintner:28', 'kintner:3', 'kintner:18', 'kintner:19', 'kintner:2', 'kintner:20', 'kintner:43', 'kintner:53', 'kintner:54', 'kintner:56', 'kintner:57', 'kintner:6', 'kintner:7', 'kintner:8', 'kintner:9', 'kintner:45', 'kintner:46', 'kintner:47', 'kintner:48', 'kintner:49', 'kintner:5', 'kintner:50', 'kintner:51', 'kintner:52', 'volvoices:11019', 'volvoices:11020', 'volvoices:11021', 'volvoices:11022', 'volvoices:11023', 'volvoices:11024', 'volvoices:11008', 'volvoices:11009', 'volvoices:11010', 'volvoices:11012', 'volvoices:11013', 'volvoices:11014', 'volvoices:11015', 'volvoices:11016', 'volvoices:11017', 'volvoices:10997', 'volvoices:10999', 'volvoices:11000', 'volvoices:11001', 'volvoices:11002', 'volvoices:11004', 'volvoices:11005', 'volvoices:11006', 'volvoices:11007', 'volvoices:10992', 'volvoices:10993', 'volvoices:10994', 'volvoices:10995', 'volvoices:10996', 'volvoices:10862', 'volvoices:10863']

Name has more than one roleterm
-------------------------------

Some names have more than one roleTerm like the ones found in
`harp:1 <https://digital.lib.utk.edu/collections/islandora/object/harp%3A1/datastream/MODS>`_:

.. code-block:: xml

    <name authority="naf" valueURI="http://id.loc.gov/authorities/names/no2002022963">
        <namePart>Swan, W. H. (William H.)</namePart>
        <role>
            <roleTerm authority="marcrelator" valueURI="http://id.loc.gov/vocabulary/relators/cmp">
                Composer
            </roleTerm>
        </role>
        <role>
            <roleTerm authority="marcrelator" valueURI="http://id.loc.gov/vocabulary/relators/com">
                Compiler
            </roleTerm>
        </role>
    </name>

Because roleterms are rdf properties, names with two roleterms should be modeled like this:

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1>
        relators:cmp <http://id.loc.gov/authorities/names/no2002022963> ;
        relators:com <http://id.loc.gov/authorities/names/no2002022963> .

Names with URIs
---------------

We have at least 19,670 records with names with matching valueURIs.

If a name has a URI, we should use it as the object like the name in
`harp:1 <https://digital.lib.utk.edu/collections/islandora/object/harp%3A1/datastream/MODS>`_:

.. code-block:: xml

    <name authority="naf" valueURI="http://id.loc.gov/authorities/names/no2002022963">
        <namePart>Swan, W. H. (William H.)</namePart>
        <role>
            <roleTerm authority="marcrelator" valueURI="http://id.loc.gov/vocabulary/relators/cmp">
                Composer
            </roleTerm>
        </role>
        <role>
            <roleTerm authority="marcrelator" valueURI="http://id.loc.gov/vocabulary/relators/com">
                Compiler
            </roleTerm>
        </role>
    </name>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1>
        relators:cmp <http://id.loc.gov/authorities/names/no2002022963> ;
        relators:com <http://id.loc.gov/authorities/names/no2002022963> .


Names without URIs
------------------

We have at least 31,618 records without names with matching valueURIs.

If the name does not have a URI, we can just use the string literal of namePart as the value.

An example can be found in `cDanielCartoon:1178 <https://digital.lib.utk.edu/collections/islandora/object/cDanielCartoon%3A1178/datastream/MODS>`_:

.. code-block:: xml

    <name type="personal">
        <namePart>Daniel, Charles R. (Charlie), Jr., 1930-</namePart>
        <role>
            <roleTerm type="text" authority="marcrelator" valueURI=" http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
    </name>

We would just model this as:

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1>
        relators:cre "Daniel, Charles R. (Charlie), Jr., 1930-" .

Names with empty URIs
---------------------

There are some records with the namePart "Bemis Bro. Bag Company".  The matches would all be apart of this set:


.. code-block:: python

    ['volvoices:2495', 'volvoices:2496', 'volvoices:2497', 'volvoices:2498', 'volvoices:2499', 'volvoices:2500', 'volvoices:2501', 'volvoices:2502', 'volvoices:2503', 'volvoices:2504', 'volvoices:2505', 'volvoices:2506', 'volvoices:2507', 'volvoices:2508', 'volvoices:2509', 'volvoices:2510', 'volvoices:2511', 'volvoices:2512', 'volvoices:2513', 'volvoices:2455', 'volvoices:2456', 'volvoices:2457', 'volvoices:2477', 'volvoices:2478', 'volvoices:2479', 'volvoices:2480', 'volvoices:2481', 'volvoices:2482', 'volvoices:2483', 'volvoices:2484', 'volvoices:2485', 'volvoices:2486', 'volvoices:2467', 'volvoices:2468', 'volvoices:2469', 'volvoices:2470', 'volvoices:2471', 'volvoices:2472', 'volvoices:2473', 'volvoices:2474', 'volvoices:2475', 'volvoices:2476', 'volvoices:2458', 'volvoices:2459', 'volvoices:2461', 'volvoices:2462', 'volvoices:2463', 'volvoices:2464', 'volvoices:2465', 'volvoices:2466', 'volvoices:2487', 'volvoices:2488', 'volvoices:2489', 'volvoices:2490', 'volvoices:2491', 'volvoices:2492', 'volvoices:2493', 'volvoices:2494']

We should fix these and add the actual valueURI.

Names with @usage="primary"
---------------------------

There are 314 records with an @usage="primary" attribute.  An example is
`kefauver:150412002 <https://digital.lib.utk.edu/collections/islandora/object/kefauver%3A150412002/datastream/MODS>`_.

.. code-block:: xml

    <name usage="primary">
        <namePart>unknown</namePart>
        <role>
            <roleTerm authority="marcrelator" type="text" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
    </name>

We should drop this.

Namepart with @type="date"
--------------------------

There are 10,370 records with a namePart with a @type="date".  This value seems to relate to the birth and death dates of
the person.

An example is `egypt:230 <https://digital.lib.utk.edu/collections/islandora/object/egypt%3A230/datastream/MODS>`_

.. code-block:: xml

    <name type="personal" valueURI="http://vocab.getty.edu/ulan/500356123">
        <namePart>Sébah, Jean Pascal</namePart>
        <namePart type="date">1872-1947</namePart>
        <description>Turkish</description>
        <role>
            <roleTerm type="text" authority="marcrelator" valueURI="http://id.loc.gov/vocabulary/relators/pht">Photographer</roleTerm>
        </role>
    </name>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1>
        relators:pht <http://vocab.getty.edu/ulan/500356123> .

If we need this data, like description, we can dereference from the URI.

Name Descriptions
-----------------

We have 10,309 records with a name with a description.  This is normally a nationality.  Here is the exhaustive list:

.. code-block:: python

    [None, 'American', 'Argentine', 'Austrian', 'Brazilian', 'British', 'Canadian', 'Danish', 'Dutch', 'Finnish', 'Flemish', 'French', 'German', 'Greek', 'Italian', 'Japanese', 'Norwegian', 'Spanish', 'Swiss', 'Turkish']

An example is `archivision:4817 <https://digital.lib.utk.edu/collections/islandora/object/archivision%3A4817>`_.

.. code-block:: xml

    <name type="personal" authority="ulan" valueURI="http://vocab.getty.edu/ulan/500026409">
        <namePart>Andreu, Paul</namePart>
        <displayForm>Paul Andreu</displayForm>
        <namePart type="date">born 1938</namePart>
        <description>French</description>
        <role>
            <roleTerm type="text" authority="marcrelator" valueURI="ttp://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
    </name>

If we need extra data, we can dereference from the URI of the creator.

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .

    <https://example.org/objects/1>
        relators:cre <http://vocab.getty.edu/ulan/500026409> .

Name Types
----------

We have 2,297 records with a name with a type attribute equal to corporate and 12,806 records with a name with a type equal
to personal.

Here are examples of each:

* `egypt:24 <https://digital.lib.utk.edu/collections/islandora/object/egypt%3A24/datastream/MODS>`_
* `cDanielCartoon:1179 <https://digital.lib.utk.edu/collections/islandora/object/cDanielCartoon%3A1178/datastream/MODS>`_

I don't think we need this information.

Name Display Forms
------------------

We have 10,284 records with a name/displayForm.

An example is `archivision:2480 <https://digital.lib.utk.edu/collections/islandora/object/archivision%3A2480/datastream/MODS>`_.

.. code-block:: xml

    <name type="personal" authority="ulan" valueURI="http://vocab.getty.edu/ulan/500023721">
        <namePart>Loos, Adolf</namePart>
        <displayForm>Adolf Loos</displayForm>
        <namePart type="date">1870-1933</namePart>
        <description>Austrian</description>
        <role>
            <roleTerm type="text" authority="marcrelator" valueURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
    </name>

Do we need this?  What are the use cases?

**Note to self:** http://vocab.getty.edu/aat/300111153

Role Term Types
---------------

We have 23,811 role terms with a type="text".

An example is `cDanielCartoon:1178 <https://digital.lib.utk.edu/collections/islandora/object/cDanielCartoon%3A1178/datastream/MODS>`_.

.. code-block:: xml

    <name type="personal">
        <namePart>Daniel, Charles R. (Charlie), Jr., 1930-</namePart>
        <role>
            <roleTerm type="text" authority="marcrelator" valueURI=" http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
    </name>

We don't need to keep this.

Role Term Authority URIs
------------------------

We have 745 role terms with authorityURIs.

An example is `insurancea:163 <https://digital.lib.utk.edu/collections/islandora/object/insurancena%3A163/datastream/MODS>`_.

.. code-block:: xml

    <name type="personal">
        <namePart>George Meade</namePart>
        <role>
            <roleTerm authority="marcrelator" authorityURI="http://id.loc.gov/vocabulary/relators/cre">Creator</roleTerm>
        </role>
    </name>

We don't need to keep this.

Names Missing Roleterms
-----------------------

We have a small number of names that have no roles.  Because the role will be used to express property, it is critical that
we address these in some way even if that were to mean giving these a generic role like dc:contributor.

Here are other strings that we need to fix, but I'll create Jira tickets with precise instructions for these.

* {'@authority': 'naf', '@type': 'personal', '@valueURI': '', 'namePart': 'Jackson, Andrew, 1767-1845'}
* {'@type': 'corporate', 'namePart': 'W. T. Thomas School'}
* {'@type': 'personal', 'namePart': 'Driver, Jim'}
* {'@type': 'personal', 'namePart': 'Williams, John, Mrs.'}
* {'@valueURI': 'http://id.loc.gov/authorities/names/n79137102', 'namePart': 'Calhoun, John C.(John Caldwell), 1782-1850'}
* {'namePart': 'Howard, Eric'}
* {'namePart': 'Johnson, Charles'}
* {'namePart': 'King, James Moore'}
* {'namePart': 'Mitchell, James C.'}
* {'namePart': 'Thompson Brothers Commercial Photographers, 1920-1940'}
* {'namePart': 'Tinsley, Stanley'}
* {'namePart': '[Fergusson, Adam]'}
* {'namePart': 'unknown'}

Other Xpaths to Trash
---------------------

There are a few other garbage that we need to trash.  Rather than talking about them in depth, here are the xpaths:

* :code:`name/role/roleTerm/@authority`
* :code:`name/@authority`
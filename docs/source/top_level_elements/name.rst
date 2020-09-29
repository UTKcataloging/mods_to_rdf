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

If the role term is associated with a marcrelator:

.. code-block:: xml

    <mods:name>
        <mods:namePart>
            Example name
        </mods:namePart>
        <mods:role>
            <mods:roleTerm>
                Stage manager
            </mods:roleTerm>
        </mods:role>
    </mods:name>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .

    <https://example.org/objects/1>
        relators:stg "Example name" .

Other terms:

* "Associated" == "Associated name"
* "Attributed" == "Attributed name"
* "Minute" == "Minute taker"
* "creator" == "Creator"

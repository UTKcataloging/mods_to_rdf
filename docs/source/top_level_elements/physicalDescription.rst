physicalDescription
===================

About
-----

This section covers the top-level element `<physicalDescription> <https://www.loc.gov/standards/mods/userguide/physicaldescription.html>`_ and all of its sub-elements:
<form>, <reformattingQuality>, <internetMediaType>, <extent>, <digitalOrigin>, and <note>. Currently UTK
does not have any existing values for <reformattingQuality>.

The hope is for all records to at least have a value for mods:physicalDescription/mods:form, but this is not the case
presently. 6,074 have no form term at all (collections affected include arrsimple, tdh, revwar, civilwar, insurancena,
fbpro, and thompson).

physicalDescription - Null values
---------------------------------

All 460 records associated with `Images: From Pi Beta Phi to Arrowmont <https://digital.lib.utk.edu/collections/islandora/object/arrowmont%3Aarrsimple>`_
have empty <physicalDescription> nodes.

Here's `arrsimple:105 <https://digital.lib.utk.edu/collections/islandora/object/arrsimple%3A105/datastream/MODS/view>`_ as an example:

.. code-block:: xml

    <physicalDescription/>

physicalDescription.extent - Null values
--------------------------------------

There are two records in the University of Tennessee Sheet Music Collection that have empty <extent> nodes. These will be
addressed quickly via `DIGITAL-759 <https://jirautk.atlassian.net/browse/DIGITAL-759>`_.

Here's `utsmc:17742 <https://digital.lib.utk.edu/collections/islandora/object/utsmc%3A17742/datastream/MODS/view>`_ as an example:

.. code-block:: xml

    <physicalDescription>
        <extent/>
        <form authority="aat" valueURI="http://vocab.getty.edu/aat/300026430">sheet music</form>
        <internetMediaType>image/jpeg</internetMediaType>
    </physicalDescription>

physicalDescription.form - AAT
------------------------------

UTK's metadata includes form terms with and without URIs. Values without a valueURI or authority may or may not follow a
controlled vocabulary. For instance, all of the Ed Gamble Cartoon collection has a form value of "cartoons (humorous images)",
which is a term from the Art and Architecture Thesaurus, but no attributes indicate this. Scopes also had this issue, but his
has just recently been addressed. Here's an example record - `gamble:1 <https://digital.lib.utk.edu/collections/islandora/object/gamble%3A1/datastream/MODS/view>`_.

.. code-block:: xml

    <physicalDescription>
        <extent>11 inches by 17 inches</extent>
        <form>cartoons (humorous images)</form>
        <digitalOrigin>reformatted digital</digitalOrigin>
    </physicalDescription>

A large number of records list the 'aat' as the authority, but do not include a valueURI. This most significantly affects the Tennessee
Farm and Home News (consisting of 3,450 records). Here's an example record - `agrtfn:44508 <https://digital.lib.utk.edu/collections/islandora/object/agrtfn%3A44508/datastream/MODS/view>`_.

.. code-block:: xml

    <physicalDescription>
        <form authority="aat">press releases</form>
        <form authority="aat">periodicals</form>
        <extent>5 pages</extent>
    </physicalDescription>

Note also that a small number of records have an authorityURI attribute present for AAT - http://www.getty.edu/research/tools/vocabularies/aat/.
These records include the Virginia P. Moore collection. Here's is an example record - `vpmoore:100 <https://digital.lib.utk.edu/collections/islandora/object/vpmoore%3A100/datastream/MODS/view>`_.

.. code-block:: xml

    <physicalDescription>
        <form authority="aat" authorityURI="http://www.getty.edu/research/tools/vocabularies/aat/" valueURI="http://vocab.getty.edu/aat/300046300">photographs</form>
        <extent>1 photograph, black and white, 7 x 11.5 cm.</extent>
        <digitalOrigin>reformatted digital</digitalOrigin>
    </physicalDescription>

The Estes Kefauver Image collection and the Children's Defense Fund include the valueURI on the wrong attribute. They are placed
on the authority attribute. Here's an example record - `kefauver:150412003 <https://digital.lib.utk.edu/collections/islandora/object/kefauver%3A150412003/datastream/MODS/view>`_.

.. code-block:: xml

    <physicalDescription>
        <extent>1 photograph</extent>
        <form authority="http://vocab.getty.edu/aat/300046300">photographs</form>
        <digitalOrigin>reformatted digital</digitalOrigin>
        <internetMediaType>image/jp2</internetMediaType>
    </physicalDescription>

physicalDescription.form - @type="materials"
--------------------------------------------

The `Archivision collection <https://digital.lib.utk.edu/collections/islandora/object/collections%3Aarchivision>`_ has a
special type attribute so that the list of materials used to create specific buildings can be faceted. The material types
are consistently listed in the same order within the string to make this possible.

Here's an example record - `archvision:2274 <https://digital.lib.utk.edu/collections/islandora/object/archivision%3A2274/datastream/MODS/view>`_.

.. code-block:: xml

    <physicalDescription>
        <form authority="aat" valueURI="http://vocab.getty.edu/aat/300265418">built works</form>
        <form type="material">wood, stucco</form>
        <digitalOrigin>reformatted digital</digitalOrigin>
    </physicalDescription>

physicalDescription.form - no valueURI
--------------------------------------

There are a total of 10,853 records with no valueURI. Note that I have not identified an instance of a term that is not
an AAT term other than those mentioned in @type="materials". The exceptions mentioned above in the AAT section should cover this.
If enough remediation is done to add URIs where they are applicable, we should only have to consider form values that are represented by URIs.

physicalDescription.digitalOrigin
---------------------------------

There are three total values found within <digitalOrigin>: "born digital", "digitized other analog", and "reformatted digital."
The majority of records with <digitalOrigin> are "reformatted digital" - **27,793** in total. There are 334 instances of "digitzed other analog"
(Derris films and slides) and 10 instances of "born digital" (only the Voices Out Loud Oral Histories Collection). Technically,
there should be more UTK records with "digitized other analog". It's definition is "A resource was created by digitizing an intermediate
form of the original resource (but not microform) such as photocopy, transparency, slide, 2nd generation analog tapes, etc." Roth, knoxgardens,
and several other collections came from intermediate resources, but have a value of "reformatted digital."

Note that there are **23,190** that are missing <digitalOrigin>. This shows that this element is used very inconsistently. Potentially
we could assume that those items without this element should have a <digitalOrigin> value of "reformatted digital" so that
our metadata is more consistent. We could also drop digitalOrigin altogether if its value / purpose in our metadata is uncertain.

Here's an example - `voloh:10 <https://digital.lib.utk.edu/collections/islandora/object/voloh%3A10>`_.

.. code-block:: xml

    <physicalDescription>
        <form authority="aat" valueURI="http://vocab.getty.edu/aat/300026392">interviews</form>
        <internetMediaType>audio/wav</internetMediaType>
        <extent>52 minutes, 09 seconds</extent>
        <digitalOrigin>born digital</digitalOrigin>
    </physicalDescription>

physicalDescription.internetMediaType
-------------------------------------

UTK metadata records contain 6 distinct values for <internetMediaType>: "application/pdf" (34 records - colloquy),
"audio/wav" (639 records - voloh & wwiioh), "image/jp2" (4,401 records), "image/jpeg" (7,417 records), "image/tif" (1,759 records),
and "pdf" (475 records). A total of **14,725** records have an <internetMediaType> while this element is not present in **36,602** records.

In many cases, the <internetMediaType> given is inaccurate for the materials being described. For instance, the University of
Tennessee Sheet Music collection has an <internetMediaType> of "image/jpeg", but the datastreams only show a pdf. Given that
only 40% of records have this element, it might be best to remove it from the descriptive metadata going forward, especially since this
information is present in technical metadata.

Here's an example of a record incorrectly given the value "image/jpeg" - `utsmc:10002 <https://digital.lib.utk.edu/collections/islandora/object/utsmc%3A10002>`_.

You can see this by looking at its datastreams `here <https://digital.lib.utk.edu/collections/islandora/object/utsmc%3A10002/manage/datastreams>`_.

.. code-block:: xml

    <physicalDescription>
        <form authority="aat" valueURI="http://vocab.getty.edu/aat/300026392">interviews</form>
        <internetMediaType>audio/wav</internetMediaType>
        <extent>52 minutes, 09 seconds</extent>
        <digitalOrigin>born digital</digitalOrigin>
    </physicalDescription>


physicalDescription.extent
--------------------------

Historically, UTK extent fields have included both the number of items/objects and the number of pages etc. More recently,
the number of items/objects has not been included if the total is one - as in "1 book (151 pages)." In this instance, just
the pages would be recorded. Historically digital pages have also been distinguished from physical pages. For instance,
"1 digital image; 1 cartoon with caption; 15 x 15 inches." Presently we use the number of digital files to determine the
number of "pages" in a book, which diverges from the cataloging standard of using the physical page numbering. It would be
ideal to remove "1 digital image" if possible when migrating.

Extent fields in many cases also contain information that is not proper to place within <extent>. For instance, the `Of Monkeys
and Men Collection <https://digital.lib.utk.edu/collections/islandora/object/collections%3Ascopes>`_ often includes information
not related to the units of the resource within <extent>. Andrew Wyatt has just (as of July 20th) finished cleaning up <extent>
within this collection. The string "black and white", referring to the type of photograph was often put into extent. The number
of physical copies available in the archive (but not digitized. . .) was also sometimes tucked into <extent>.

Here is an example record - `scopes:748 <https://digital.lib.utk.edu/collections/islandora/object/scopes%3A748/datastream/MODS/view>`_:

.. code-block:: xml

    <physicalDescription>
        <extent>1 photograph, notes on reverse, 2 copies (2 pages)</extent>
        <digitalOrigin>reformatted digital</digitalOrigin>
        <form>photographs</form>
    </physicalDescription>

This <extent> value attempts to communicate that the original photograph was digitized as two pages (back and front) and
erroneously reports that there are "notes on reverse". Remediation resulted in the complete removal of this value. All of the
non-unit information ("notes on reverse" and "2 copies") were elsewhere in the record.

The element includes values that indicate time and physical dimensions. Time is consistently shared in hours, minutes and
seconds with the exception of the following values: "113 minutes, 25 seconds", "83 minutes, 38 minutes", "94 minutes, 55 seconds",
and "111 minutes, 5 seconds." Physical dimensions are most consistently represented in inches and feet, but cm are also used
for smaller items that might benefit from a more granular measurement.

In terms of mapping decisions, there is only one use case that differs from the standard reporting of total pages, dimensions,
or length, etc. The Arrow of Pi Beta Phi has <extent> values that share the page numbers the article digitized covers. Strictly
speaking, this is not the extent of the article, but it can be calculated from this information. Here is an example record -
`arrow:2 <https://digital.lib.utk.edu/collections/islandora/object/arrow%3A2/datastream/MODS/view>`_.

.. code-block:: xml

    <physicalDescription>
        <form authority="aat" valueURI="http://vocab.getty.edu/aat/300026657">periodicals</form>
        <extent>Pages 427-434</extent>
    </physicalDescription>

Finally, the following values included typos or encoding issues that could be addressed before migration:

1. 1 letter (2 pages, 6 1/2 in xÌÄ®ÕÌ¢‰âÂ�ÁÌÄ‰Û_ÌâåÊ11 in)
2. 329 phtographs, 152 postcards, 7 maps, 4 stereographs, 1 painting
3. 104 phtographs
4. 10.75 x 8.75 inchesches
5. 1 scores (6 pges)
6. 1 scores (4 pages)
7. 1 minutes, 15 seconds
8. 1 minutes, 29 seconds
9. 1 minutes, 37 seconds
10. 1 leave of page ; 28 cm.
11. 1 digital imags; 1 photograph, 8 x 10 inches
12. 1 digital image; 1 photorgaph
13. 1 digital image; 1 photogaph
14. 1 digital image; 1 photgraph; 8 x 10 inches
15. 1 digital image; 1 photgraph
16. 83 minutes, 38 minutes

physicalDescription.extent - @unit
----------------------------------

The Great Smoky Mountains Colloquy collection includes the unit attribute on <extent>. This collection needs to be remediated
to remove this attribute and add the string ' pages' to each extent value. The collection consists of 34 total records.
Here's an example - `colloquy: <https://digital.lib.utk.edu/collections/islandora/object/colloquy%3A202/datastream/MODS/view>`_.

.. code-block:: xml

    <physicalDescription>
        <extent unit="pages">4</extent>
        <form authority="aat" valueURI="http://vocab.getty.edu/aat/300026652"> newsletters</form>
        <internetMediaType>application/pdf</internetMediaType>
        <internetMediaType>application/pdf</internetMediaType>
    </physicalDescription>

physicalDescription.note
------------------------

A total of 463 records have <note> values nested within <physicalDescription>. These string values share information
on camera settings, magnification, film type, and zoom/aperture. Here are four example values:

1. Camera setting: 7@50 on 25; with filter
2. 0.18x magnification, 100 Velvia
3. Film type: Kodachrome Transparency
4. zoomA -> 70 [A], Auto f16E100s

A total of 31 records in volvoices also have "reformatted digital" incorrectly placed in a <note> element. Otherwise, the
collections with these values include the Botanical Photographs of Alan S. Heilman and the William Derris Slide Collection.

An example record is `heilman:1001 <https://digital.lib.utk.edu/collections/islandora/object/heilman%3A1001/datastream/MODS/view>`_.

.. code-block:: xml

    <physicalDescription>
        <form authority="aat" valueURI="http://vocab.getty.edu/aat/300046300">photographs</form>
        <internetMediaType>image/jpeg</internetMediaType>
        <digitalOrigin>reformatted digital</digitalOrigin>
        <note>0.2x magnification</note>
    </physicalDescription>
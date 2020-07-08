note
====

About
-----

This section describes all the different types of notes that we have in our Islandora repository right now.

Null
----

Some digital records have blank nodes like `brehm:5 <https://digital.lib.utk.edu/collections/islandora/object/brehm:5/datastream/MODS>`_.

.. code-block:: xml

    <note/>

No attributes
-------------

Most notes have no attributes like the ones found on `bakerav:291 <https://digital.lib.utk.edu/collections/islandora/object/bakerav%3A291/datastream/MODS>`_

.. code-block:: xml

    <note>A_0:51:21 / B_0:59:44</note>
    <note>(Original, for: Mrs. Dirksen, Compliments: Tony Janak)</note>
    <note>No issues.</note>

@displayLabel="Attribution"
---------------------------

Some records have a note with an "Attribution" displayLabel, `heilman:1000 <https://digital.lib.utk.edu/collections/islandora/object/heilman:1000/datastream/MODS>`_.

.. code-block:: xml

    <note displayLabel="Attribution">
        Photograph © Alan S. Heilman; Digital Image © 2011 The University of Tennessee Libraries. Creative Commons License Attribution-NonCommercial-NoDerivs 3.0 Unported (CC BY-NC-ND 3.0) with attribution as follows: [Photograph title and item number], The Botanical Photography of Alan S. Heilman, © Alan S. Heilman, © The University of Tennessee Libraries, 2011.
    </note>

@displayLabel="Grade level"
---------------------------

Some records have a note with a "Grade Level" displayLabel,`arrowmont:9 <https://digital.lib.utk.edu/collections/islandora/object/arrowmont:9/datastream/MODS>`_:

.. code-block:: xml

    <note displayLabel="Grade level">
        Second Grade
    </note>

@displayLabel="Intermediate Provider"
-------------------------------------

Some records have a note with a "Intermediate Provider" displayLabel, `cdf:6186 <https://digital.lib.utk.edu/collections/islandora/object/cdf:6186/datastream/MODS>`_:

.. code-block:: xml

    <recordInfo>
        <recordContentSource valueURI="http://id.loc.gov/authorities/names/no2017113530">
            Langston Hughes Library (Children&apos;s Defense Fund Haley Farm)
        </recordContentSource>
    </recordInfo>
    <note displayLabel="Intermediate Provider">
        University of Tennessee, Knoxville. Libraries
    </note>

@displayLabel="Intermediate provider"
-------------------------------------

Some records have a note with a "Intermediate provider" displayLabel, `thompson:515 <https://digital.lib.utk.edu/collections/islandora/object/thompson:515/datastream/MODS>`_:

.. code-block:: xml

    <recordInfo>
        <recordContentSource authority="lcnaf" valueURI="http://id.loc.gov/authorities/names/n82163095">
            Arnold Arboretum
        </recordContentSource>
    </recordInfo>
    <note displayLabel="Intermediate provider">
        University of Tennessee, Knoxville. Libraries
    </note>

@displayLabel="Local Rights"
----------------------------

Some records have a note with a "Local Rights" displayLabel, `egypt:79 <https://digital.lib.utk.edu/collections/islandora/object/egypt:79/datastream/MODS>`_:

.. code-block:: xml

    <accessCondition type="use and reproduction" xlink:href="http://rightsstatements.org/vocab/NoC-US/1.0/">
        No Copyright - United States
    </accessCondition>
    <note displayLabel="Local Rights">
        Permission granted for reproduction for use in research and teaching, provided proper attribution of source. Credit line should read: [description of item, including photographic number], 'Courtesy of McClung Museum of Natural History and Culture, The University of Tennessee.' For all other uses consult https://mcclungmuseum.utk.edu/research/image-services/rights-reproductions/ or call 865-974-2144.
    </note>

@displayLabel="Project Part"
----------------------------

Some records have a note with a "Project Part" displayLabel, `arrowmont:535 <https://digital.lib.utk.edu/collections/islandora/object/arrowmont:535/datastream/MODS>`_:


.. code-block:: xml

    <note displayLabel="Project Part">
        Arrowmont Scrapbooks
    </note>

@displayLabel="Tags"
--------------------

Some records have a note with a "Tags" displayLabel, `fbpro:94819 <https://digital.lib.utk.edu/collections/islandora/object/fbpro:94819/datastream/MODS>`_.

This was used to ensure we had a sortable field based on year of the guide, but it looks like some of these have the same
information in `originInfo/dateIssued`:

.. code-block:: xml

    <originInfo>
        <dateIssued>
            1961
        </dateIssued>
    </originInfo>
    <note displayLabel="Tags">
        1961
    </note>

@displayLabel="Transcribed from Original Collection"
----------------------------------------------------

Some records have a note with a "Transcribed from Original Collection" displayLabel, `roth:2974 <https://digital.lib.utk.edu/collections/islandora/object/roth:2974/datastream/MODS>`_

.. code-block:: xml

<titleInfo>
    <title>Inside of Old Mill up Kalance Fork Greenbrier (Negative 251)</title>
</titleInfo>
<note displayLabel="Transcribed from Original Collection">
    Inside of Old Mill up Kalance Fork Greenbrier (Negative 251)
</note>

@displayLabel="dpn"
-------------------

Some records have a note that signifies it was in dpn. `heilman:1000 <https://digital.lib.utk.edu/collections/islandora/object/heilman:1000/datastream/MODS>`_.

We no longer need this.  Don't migrate it.

.. code-block:: xml

    <note displayLabel="dpn">
        This object was added to the Digital Preservation Network in November 2016.
    </note>

@displayLabel="use and reproduction"
------------------------------------

Some records have a note with a "use and reproduction" displayLabel, `thompson:258 <https://digital.lib.utk.edu/collections/islandora/object/thompson:258/datastream/MODS>`_:

.. code-block:: xml

    <note displayLabel="use and reproduction">
        To use photographs or to order reproductions which belong to the McClung Historical Collection, contact DigitalCollections@knoxlib.org or phone 865 215-8808. Please refer to Image Number and provide a brief description of the photograph
    </note>

@type="First line"
------------------

Some records have a note with a "First line" type, `vanvactor:15773 <https://digital.lib.utk.edu/collections/islandora/object/vanvactor:15773/datastream/MODS>`_:

.. code-block:: xml

    <note type="First line">
        Ojitos de pena carita de luna, lloraba la niña sin causa ninguna.
    </note>

@type="first line"
------------------

Some records have a note with a "first line" type, `utsmc:17498 <https://digital.lib.utk.edu/collections/islandora/object/utsmc:17498/datastream/MODS>`_:

.. code-block:: xml

    <note type="first line">
        Cualquiera que el tejado
    </note>

@type="handwritten"
-------------------

Some records have a note with a "handwritten" type, `vanvactor:322 <https://digital.lib.utk.edu/collections/islandora/object/vanvactor:322/datastream/MODS>`_:

.. code-block:: xml

    <note type="handwritten">
        D.V.V.
    </note>

@type="instrumentation"
-----------------------

Some records have a note with a "instrumentation" type, `vanvactor:15773 <https://digital.lib.utk.edu/collections/islandora/object/vanvactor:15773/datastream/MODS>`_:

.. code-block:: xml

    <note type="instrumentation">
        For soprano, mezzo-soprano, contralto, 2 flutes, 2 oboes, 2 clarinets, 2 bassoons, 2 horns, 2 trumpets, timpani,
        2 violins, viola, cello, and double bass.
    </note>

@type="provenance"
------------------

Some records have a note with a "provenance" type, `scopes:470 <https://digital.lib.utk.edu/collections/islandora/object/scopes:470/datastream/MODS>`_:

.. code-block:: xml

    <note type="provenance">
        One of multiple documents from a single source in Texas.
    </note>
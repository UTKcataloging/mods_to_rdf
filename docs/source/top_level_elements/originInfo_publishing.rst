originInfo: publishing information
==================================

About
-----

This section describes the non-date specific subelements of originInfo in our MODS.

publisher
---------

An example, `utsmc:13759 <https://digital.lib.utk.edu/collections/islandora/object/utsmc%3A13759>`_:

.. code-block:: xml

    <originInfo>
        <place>
            <placeTerm valueURI="http://id.loc.gov/authorities/names/n79006530">Baltimore (Md.)</placeTerm>
        </place>
        <publisher>Frederick D. Benteen</publisher>
    </originInfo>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators>

    <https://example.org/objects/1> relators:pbl "Frederick D. Benteen" ;
        relators:pup <http://id.loc.gov/authorities/names/n79006530> .

.. code-block:: xml

    <originInfo>
      <publisher>Archivision, Inc.</publisher>
      <dateCreated>begun 1665</dateCreated>
      <dateCreated encoding="edtf" keyDate="yes">1665</dateCreated>
    </originInfo>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators>
    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> relators:pbl "Archivision, Inc." ;
        dcterms:created "1665/" .

place
-----

issuance
--------

The `issuance` element appears 4207 times and the value is always "serial".

.. code-block:: xml

    <issuance>serial</issuance>




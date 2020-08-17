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
        dcterms:created "begun 1665", "1665" .

place
-----

.. code-block:: xml

    <originInfo>
        <place supplied="yes">
            <placeTerm type="text" valueURI="http://id.loc.gov/authorities/names/n79072935">Meadville (Crawford County, Pa.)</placeTerm>
        </place>
        <publisher>Keystone View Company</publisher>
        <dateCreated>between 1890 and 1930?</dateCreated>
        <dateCreated encoding="edtf" keyDate="yes" point="start" qualifier="questionable">1890</dateCreated>
        <dateCreated encoding="edtf" keyDate="yes" point="end">1930</dateCreated>
    </originInfo>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators>
    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> relators:pbl "Keystone View Company" ;
        relators:pup <http://id.loc.gov/authorities/names/n79072935> ;
        dcterms:created "between 1890 and 1930?", "1890?/1930" .

There are problematic uses of `place` in `collections:sanborn` (empty elements).

.. code-block:: xml

  <originInfo>
    <place supplied="yes">
      <placeTerm type="text"/>
    </place>
    <publisher>Sanborn Map &amp; Publishing Co., Ltd</publisher>
    <dateCreated>1917</dateCreated>
    <dateCreated encoding="edtf" keyDate="yes">1917</dateCreated>
  </originInfo>

.. code-block:: turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators>
    @prefix dcterms: <http://purl.org/dc/terms/>

    <https://example.org/objects/1> relators:pbl "Sanborn Map & Publishing Co., Ltd" ;
        dcterms:created "1917", "1917" .

issuance
--------

The `issuance` element appears 4207 times and the value is always "serial". We will not migrate `issuance`.

.. code-block:: xml

    <issuance>serial</issuance>




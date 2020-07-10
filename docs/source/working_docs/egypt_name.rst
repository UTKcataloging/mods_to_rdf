Modelling name element of Jeune fille du liban coiffée du tentour or egypt:101 to RDF Recommendations
=====================================================================================================

Given MODS
----------

.. code-block:: xml
    :linenos:
    :caption: Given MODS element
    :name: Given MODS element

    <name type="corporate" valueURI="http://vocab.getty.edu/ulan/500057278">
        <namePart>Bonfils family</namePart>
        <namePart type="date">19th-20th centuries</namePart>
        <role>
            <roleTerm type="text" authority="marcrelator" valueURI="http://id.loc.gov/vocabulary/relators/pht">Photographer</roleTerm>
        </role>
    </name>

RDF as turtle
-------------

.. code-block:: turtle
    :linenos:
    :caption: Islandora RDF as turtle
    :name: Islandora RDF as turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .
    @prefix ulan: <http://vocab.getty.edu/ulan> .

    <https://example.org/objects/1> relators:pht <https://example.org/names/1> .

    <https://example.org/names/1> foaf:name "Bonfils family" ;
        a foaf:Organization ;
        schema:sameAs <ulan:500057278> .

.. code-block:: turtle
    :linenos:
    :caption: Samvera direct mapping RDF as turtle
    :name: Samvera Direct Mapping  RDF as turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .
    @prefix ulan: <http://vocab.getty.edu/ulan> .

    <https://example.org/objects/1> relators:pht <ulan:500057278> ;
        a foaf:Organization .

.. code-block:: turtle
    :linenos:
    :caption: Samvera minted object mapping RDF as turtle
    :name: Samvera minted object mapping as turtle

    @prefix relators: <http://id.loc.gov/vocabulary/relators> .
    @prefix ulan: <http://vocab.getty.edu/ulan> .

    <https://example.org/objects/1> relators:pht <https://example.org/name/1> .

    <https://example.org/name/1> a foaf:Organization ;
        schema:sameAs <ulan:500057278> ;
        foaf:name "Bonfils Family"@en .

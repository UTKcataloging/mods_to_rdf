Proof of Concept for Review and Merge of Pull Requests
======================================================

Example Code
------------

.. code-block:: turtle
    :caption: Good Turtle
    :name: Good Turtle
    :linenos:

    @prefix utkevents: <http://[address-to-triplestore]/events/> .
    @prefix bf: <http://id.loc.gov/ontologies/bibframe/> .
    @prefix dcterms: <http://purl.org/dc/terms/> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .

    <utkevents:2>
        a bf:provisionActivity ;
        dcterms:created "1939" ;
        skos:note "Date: Inferred" .


.. code-block:: turtle
    :caption: Bad Turtle
    :name: Bad Turtle
    :linenos:

    @prefix utkevents: <http://[address-to-triplestore]/events/> .
    @prefix bf: <http://id.loc.gov/ontologies/bibframe/> .
    @prefix dcterms: <http://purl.org/dc/terms/> ,
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> ;

    <utkevents:2>
        a bf:provisionActivity ;
        dcterms:created "1939" -
        skos:note "Date: Inferred" ;
        test:yo "yo".

.. code-block:: xml
    :caption: Good XML
    :name: Good XML
    :linenos:

    <mods:titleInfo supplied="yes">
        <mods:title>
            Didn't mail your tax returns until 11:59 PM last night
        </mods:title>
    </mods:titleInfo>

.. code-block:: xml
    :caption: Bad XML
    :name: Bad XML
    :linenos:

    <mods:titleInfo @supplied="yes">
        <mods:title>
            Didn't mail your tax returns until 11:59 PM last night
        </mods:title>
    </mods:titleInfo>

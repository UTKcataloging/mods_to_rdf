abstract
========

About
-----

Most of our records have at least one abstract. This element is used to record a succinct summary of some aspect of the
content of the resource.

One or Many Abstracts
---------------------

Use Case
^^^^^^^^

If a record has an abstract or many abstracts, they will each be mapped to `dcterms:abstract` as long as the abstract
does not have an empty text node.

Justification
^^^^^^^^^^^^^

Regardless of the number, the value has the same semantic relationship to the object as it did in MODS.

Xpath
^^^^^

:code:`mods:abstract[text()!=""]`

Decision
^^^^^^^^

If it has one abstract like `gamble:124 <https://digital.lib.utk.edu/collections/islandora/object/gamble%3A124/datastream/MODS>`_, map to dcterms:abstract.

.. code-block:: xml

    <abstract>
        Prosecutor John Keker gives his closing statement to the jury, explaining Col. John North's involvement in the Iran-Contra affair even though the majority of his statement is censored due to classified information.
    </abstract>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:abstract "Prosecutor John Keker gives his closing statement to the jury, explaining Col. John North's involvement in the Iran-Contra affair even though the majority of his statement is censored due to classified information." .

If it has more than one abstract like `1001:1 <https://digital.lib.utk.edu/collections/islandora/object/1001%3A1/datastream/MODS>`_,
we will still map to dc:terms abstract.

.. code-block:: xml

    <abstract>
        Postcard with handwritten note sent from Knoxville to Miss Virginia Bogart, Loudon, Tennessee on March 2, 1944 for a postage of 1 cent.
    </abstract>
    <abstract>
        The hardwood forest of America, and probably of the entire world, originated in the Great Smoky Mountains, where remains the nation's largest body of virgin hardwood forest, and the world's greatest variety of trees, flowering shrubs and wild flowers.
    </abstract>

.. code-block:: turtle

    @prefix dcterms: <http://purl.org/dc/terms/> .

    <https://example.org/objects/1> dcterms:abstract "Postcard with handwritten note sent from Knoxville to Miss Virginia Bogart, Loudon, Tennessee on March 2, 1944 for a postage of 1 cent.", "The hardwood forest of America, and probably of the entire world, originated in the Great Smoky Mountains, where remains the nation's largest body of virgin hardwood forest, and the world's greatest variety of trees, flowering shrubs and wild flowers." .

Blank Abstracts
---------------

Use Case
^^^^^^^^

We have a fair number of records with empty abstracts.  When an abstract is an empty node, don't map it.

Justification
^^^^^^^^^^^^^

The value of the text node has no semantic meaning or value.

Xpaths
^^^^^^

:code:`mods:abstract[text()=""]`

Decision
^^^^^^^^

Don't map!
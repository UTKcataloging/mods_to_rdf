The Complexity of Moving from MODS to RDF
=========================================

The MODS RDF Ontology
---------------------

When moving from MODS XML to RDF and linked data, it makes sense to consider migrating your XML to the `MODS RDF ontology <https://github.com/blunalucero/MODS-RDF/>`_.
While the ontology is functional, it has issues that make its adoption problematic. As the Samvera MODS to RDF working
group explains, the problems include a "lack of active maintenance, heavy reliance on the use of blank nodes and/or
minted objects in its implementation, and perhaps most importantly a lack of adoption." [#f1]_ As the ​ W3C RDF Primer​ states:
"Vocabularies get their value from reuse: the more vocabulary IRIs are reused by others, the more valuable it becomes to use the IRIs." [#f2]_
Because of this, the Samvera MODS to RDF working group "opted to pursue an approach mapping MODS XML elements to RDF using
a variety of vocabularies that have been extensively used in other Linked Data datasets, instead of pursuing a stricter
translation of MODS."

.. rubric:: Footnotes

.. [#f1] MODS to RDF Mapping Recommendations. *Original Document prepared by the Samvera MODS to RDF Working Group (January 2019)*. `<https://wiki.duraspace.org/download/attachments/87460857/MODS-RDF-Mapping-Recommendations_SMIG_v1_2019-01.pdf?api=v2>`_.
.. [#f2] RDF 1.1 Primer. *Original Document prepared by the W3C Working Group (June 24, 2014)*. `<https://www.w3.org/TR/rdf11-primer/>`_.

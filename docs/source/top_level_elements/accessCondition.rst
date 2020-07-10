accessCondition
===============

About
-----

This section describes all the different types of accessCondition values that we have in our Islandora repository right now.
There are 25 distinct values (7 of which require no changes in their form). In several cases the wrong form of URI has been used
(page instead of vocab - http://rightsstatements.org/page/NKC/1.0/). Note that for DPLA, each record needs to have an
accessCondition that includes a value from `rightsstatements.org <rightsstatements.org>`_. Otherwise many other issues
relate to simple string variations that shouldn't be present.

One potential way to map these values to RDF is to use edm:rights, which is what DPLA indicates should be used in their
`MAP (Metadata Application Profile) 4.0 document <https://drive.google.com/file/d/1743zMwrrZQFleAZiMZNe_f5H3TXv6Iyg/view>`_.

Digital Image Copyright
-----------------------

The Blount County Historical and Architectural Index collection includes incorrect statements from Blount County Public
Library that they hold the copyright for the 93 images within the collection. This metadata has already been completely
remediated by Katie Hill this spring, but I have not made time to review the changes and create XML from this `work <https://github.com/UTKcataloging/bcpl_remediation>`_. All of the items within the collection are "In Copyright."

Here's `bcpl:100 <https://digital.lib.utk.edu/collections/islandora/object/bcpl%3A100>`_. as an example:

.. code-block:: xml

    <accessCondition type="use and reproduction">Digital Image Copyright (c) 2004. Blount County Public Library, Maryville, TN. All Rights Reserved. For permission to use, contact: Reference Department, Blount County Public Library, 508 N. Cusick Street, Maryville, TN 37804 (865-982-0982).</accessCondition>
    
Here's also `bcpl:107 <https://digital.lib.utk.edu/collections/islandora/object/bcpl%3A107>`_. Rather than "use and reproduction",
this node has a type attribute value of "local rights statment."

.. code-block:: xml

    <accessCondition type="local rights statement">Digital Image Copyright (c) 2004. Blount County Public Library, Maryville, TN. All Rights Reserved. For permission to use, contact: Reference Department, Blount County Public Library, 508 N. Cusick Street, Maryville, TN 37804 (865-982-0982).</accessCondition>

smokies@utk.edu
---------------

The kintner collection has an in copyright statement with contact information (smokies@utk.edu). Beyond this
no longer being a project in Special Collections, it also needs to be updated to match rightsstatements.org

Here's an example - `kintner:1 <https://digital.lib.utk.edu/collections/islandora/object/kintner%3A1>`_.

.. code-block:: xml

    <accessCondition>Images in the collection are protected by copyright. Contact smokies@utk.edu for permission to reproduce images from the collection.</accessCondition>

special@utk.edu
---------------

Like the previous example, this group of statements indicates that the materials are in copyright and that users should
get in contact with Special Collections for more information. In total, 68 records from the Bass collection use this
statement.

Here's an example - `bass:8597 <https://digital.lib.utk.edu/collections/islandora/object/bass%3A8597>`_.

.. code-block:: xml

    <accessCondition type="use and reproduction">The copyright interests in this item remain with the creator. For more information, contact Special Collections at special@utk.edu.</accessCondition>

'@xlink:href': '    '
---------------------

A single record within the Arrowmont Photos of Scrapbooks collection (`arrpgimg:455 <https://digital.lib.utk.edu/collections/islandora/object/arrpgimg%3A455>`_)
has a tab instead of a URI. This needs to be replaced with `http://rightsstatements.org/vocab/CNE/1.0/ <http://rightsstatements.org/vocab/CNE/1.0/>`_.

.. code-block:: xml

    <accessCondition type="use and reproduction" xlink:href=" ">Copyright Not Evaluated</accessCondition>

'@xlink:href': '0'
---------------------

A single record within the vanvactor collection has a value of zero within xlink:href (`vanvactor:2555
<https://digital.lib.utk.edu/collections/islandora/object/vanvactor%3A2555>`_) This needs to be replaced with
`http://rightsstatements.org/vocab/InC/1.0/ <http://rightsstatements.org/vocab/InC/1.0/>`_.

.. code-block:: xml

    <accessCondition type="use and reproduction" xlink:href="0">In Copyright</accessCondition>

URI for 'page' versus 'vocab'
-------------------------------------

This category affects all of the records in the Estes Kefauver Crime Documents collection. The rightsstatements.org
vocabularies need to refer to the 'vocab' link and not the link that simply points to the page.

The InC-RUU statement has a single record with page: `ekcd:633 <https://digital.lib.utk.edu/collections/islandora/object/ekcd%3A633>`_.

.. code-block:: xml

    <accessCondition type="use and reproduction" xlink:href="http://rightsstatements.org/page/InC-RUU/1.0/">In Copyright - Rights-holder(s) Unlocatable or Unidentifiable</accessCondition>

The NKC statement has 77 records from the Estes Kefauver Crime Documents with page. For instance: `ekcd:282
<https://digital.lib.utk.edu/collections/islandora/object/ekcd%3A282>`_.

.. code-block:: xml

    <accessCondition type="use and reproduction" xlink:href="http://rightsstatements.org/page/NKC/1.0/">No Known Copyright</accessCondition>

The NoC-US statement has 7 records with page. An example is `ekcd:204 <https://digital.lib.utk.edu/collections/islandora/object/ekcd%3A204>`_.

.. code-block:: xml

    <accessCondition type="use and reproduction" xlink:href="http://rightsstatements.org/page/NoC-US/1.0/">No Copyright - United States</accessCondition>

The UND statement has 4 records with page. An example is `ekcd:315 <https://digital.lib.utk.edu/collections/islandora/object/ekcd%3A315>`_.

.. code-block:: xml

    <accessCondition type="use and reproduction" xlink:href="http://rightsstatements.org/page/UND/1.0/">Copyright Undetermined</accessCondition>

Variations on Copyright Not Evaluated
-------------------------------------

The CNE statement has a few variations that need to be addressed.

After the URI for 783 CNE statements there is an extra space! This needs to be removed across all of arrsimple and
the arrow. An example is `arrow:232 <https://digital.lib.utk.edu/collections/islandora/object/arrow%3A232>`_.

.. code-block:: xml

    <accessCondition type="use and reproduction" xlink:href="http://rightsstatements.org/vocab/CNE/1.0/ ">Copyright Not Evaluated</accessCondition>

Another 464 CNE statements have a new line character where they shouldn't in the text value. The collections affected are
arrow and arrowmont. An example is `arrowmont:208 <https://digital.lib.utk.edu/collections/islandora/object/arrowmont%3A208>`_.
dltn_metadata_qa shares the string as "'#text': 'Copyright Not\n            Evaluated'".

.. code-block:: xml

    <accessCondition type="use and reproduction" xlink:href="http://rightsstatements.org/vocab/CNE/1.0/ ">Copyright Not Evaluated</accessCondition>

Capitalization for InC-NC
-------------------------

The "In Copyright - Non-Commercial Use Permitted" statement has a capitalization variation for 272 records. Some values
are given as "In Copyright - Non-commercial Use Permitted." Since capitalization is present in the code (the final "C" in "InC-NC"),
the string also should have capitalization. An example is `utkcomm:24621 <https://digital.lib.utk.edu/collections/islandora/object/utkcomm%3A24621>`_.

.. code-block:: xml

    <accessCondition type="use and reproduction" xlink:href="http://rightsstatements.org/vocab/InC-NC/1.0/">In Copyright - Non-commercial Use Permitted</accessCondition>

Dash Variation for NoC-US
-------------------------

For both menbball and ladytennis, an em dash is used instead of an en dash in "No Copyright - United States." This appears
as a result in dltn_metadata_qa as "'#text': 'No Copyright \x96 United States'". An example record is `menbball:601
<https://digital.lib.utk.edu/collections/islandora/object/menbball%3A601>`_.

.. code-block:: xml

    <accessCondition type="use and reproduction" xlink:href="http://rightsstatements.org/vocab/NoC-US/1.0/">No Copyright – United States</accessCondition>

Creative Commons
----------------

In our collections we have one Creative Commons license that is used in an accessCondition. 1121 records from the Heilman
collection use the statement "Attribution-NonCommercial-NoDerivs 3.0 Unported (CC BY-NC-ND 3.0)." An example record is
`heilman:3 <https://digital.lib.utk.edu/collections/islandora/object/collections%3Aheilman>`_. We will want to consider if
there is any reason for CC licenses to be mapped to a different field than our rightsstatements.org values. DPLA
allows either CC or rightstatements to be used for their required values. More documentation on the standards for rights
values within DPLA can be found `here <https://docs.google.com/document/d/1aInokOIIsgf-B4iMTXU33qYN5B2jA3s91KgWoh7DZ7Q/edit>`_.

.. code-block:: xml

    https://digital.lib.utk.edu/collections/islandora/object/collections%3Aheilman


No Cosmetic Changes Needed
--------------------------

The follow instances from dltn_metadata_qa require no edits:

1. {'@type': 'use and reproduction', '@xlink:href': 'http://rightsstatements.org/vocab/CNE/1.0/', '#text': 'Copyright Not Evaluated'}
2. {'@type': 'use and reproduction', '@xlink:href': 'http://rightsstatements.org/vocab/InC-EDU/1.0/', '#text': 'In Copyright - Educational Use Permitted'}
3. {'@type': 'use and reproduction', '@xlink:href': 'http://rightsstatements.org/vocab/InC-NC/1.0/', '#text': 'In Copyright - Non-Commercial Use Permitted'}
4. {'@type': 'use and reproduction', '@xlink:href': 'http://rightsstatements.org/vocab/InC/1.0/', '#text': 'In Copyright'}
5. {'@type': 'use and reproduction', '@xlink:href': 'http://rightsstatements.org/vocab/NKC/1.0/', '#text': 'No Known Copyright'
6. {'@type': 'use and reproduction', '@xlink:href': 'http://rightsstatements.org/vocab/NoC-US/1.0/', '#text': 'No Copyright - United States'}
7. {'@type': 'use and reproduction', '@xlink:href': 'http://rightsstatements.org/vocab/UND/1.0/', '#text': 'Copyright Undetermined'}
Sphinx is a markup formatting engine / ecosystem, originally developed for documenting the Python programming language.

- Sphinx uses 'reStructuredText', or 'RST' for short. 

- It sits in-between MarkDown and LaTex by power and complexity.

- Sphinx is designed primarily for creating HTML documentation, but can also create static PDFs etc.


    
reST grammar: 
================================

reST is mainly based on directives that are defined as follows:
`rest <http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html>`_

``
.. <name>:: <arguments>
    :<option>: <option values>

    content
``

double backquotes are used to make a text verbatim. 

Example:

.. image:: ../images/test.png
    :width: 200pt

Internal and External Links
------------------------------
`Internal and External links`_

.. _begin:

`Python <http://www.python.org/>`_


Aliases
----------
.. _Python: http://www.python.org/

OR

.. |longtext| replace:: this is a very very long text to include

and then insert |longtext| wherever needed.

Comments
---------
.. comments

colored boxes: note, seealso, topic, todo, warnings, Sidebar directive
---------------------------------------------------

.. seealso:: This is a simple **seealso** note. Other inline directive may be included (e.g., math :math:`\alpha`) but not al of them.


Inserting code and Literal blocks

This is a simple example:
::

    import math
    print 'import done'


Maths and Equations with LaTeX
-----------------------------------

glossary, centered, Field list, index, download
-----------------------------------------------------



Footnote
------------------------
Some text that requires a footnote [#f1]_ .

.. rubric:: Footnotes

.. [#f1] Text of the first footnote.

Citations
-----------
.. [CIT2002] A citation
          (as often used in journals).
          
and called as follows:

[CIT2002]_


**bold** and *italics*
星号: *text* 是强调 (斜体),
双星号: **text** 重点强调 (加粗),
反引号: ``text`` 代码样式.

`Docs for this project <http://packages.python.org/an_example_pypi_project/>`_

jumps to another section: `Table of Contents`_

| Line blocks are useful for addresses,
| verse, and adornment-free lists.


Images syntax is like this:

.. figure::  images/sweat.jpg
   :align:   center

   Proof that getting rich is mostly luck.

Here is something I want to talk about::

    def my_fn(foo, bar=True):
        """A really useful function.

        Returns None
        """

.. |biohazard| image:: images/biohazard.png

The |biohazard| symbol must be used on containers used to dispose of medical waste.

:download:`An Example Pypi Project<docs/examplepypi.pdf>`

.. |doctest| replace:: :mod:`doctest`

I really like |doctest|.

Autonumbered footnotes are
possible, like using [#]_ and [#]_.

.. [#] This is the first one.
.. [#] This is the second one.

They may be assigned 'autonumber
labels' - for instance,
[#fourth]_ and [#third]_.

.. [#third] a.k.a. third_

.. [#fourth] a.k.a. fourth_
Footnote references, like [5]_.
Note that footnotes may get
rearranged, e.g., to the bottom of
the "page".

.. [5] A numerical footnote. Note
   there's no colon after the ``]``.
   

.. include myfile.rst


.. note::

.. warning::

.. versionadded:: version

.. versionchanged:: version

.. seealso::

.. code-block:: python
   :emphasize-lines: 3,5

   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'
       
External hyperlinks, like `Python
<http://www.python.org/>`_.



Some references:

- https://pythonhosted.org/an_example_pypi_project/sphinx.html

- https://github.com/timstaley/sphinx-example

- https://zh-sphinx-doc.readthedocs.io/en/latest/markup/code.html

- http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html

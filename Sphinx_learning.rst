Sphinx is a markup formatting engine / ecosystem, originally developed for documenting the Python programming language.

- Sphinx uses 'reStructuredText', or 'RST' for short. 

- It sits in-between MarkDown and LaTex by power and complexity.

- Sphinx is designed primarily for creating HTML documentation, but can also create static PDFs etc.

RST grammar: 
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

- https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst

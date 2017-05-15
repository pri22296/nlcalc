######################################################################################
Natural Language Mathematical Calculator
######################################################################################

.. inclusion-marker-badges-start

.. image:: https://badge.fury.io/py/nlcalc.svg
    :target: https://badge.fury.io/py/nlcalc

.. image:: https://coveralls.io/repos/github/pri22296/nlcalc/badge.svg?branch=master
    :target: https://coveralls.io/github/pri22296/nlcalc?branch=master

.. image:: https://travis-ci.org/pri22296/nlcalc.svg?branch=master
    :target: https://travis-ci.org/pri22296/nlcalc

.. image:: https://api.codacy.com/project/badge/Grade/0ad006a377474ddcb251dc94418d48a2 
    :target: https://www.codacy.com/app/pri22296/nlcalc?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=pri22296/nlcalc&amp;utm_campaign=Badge_Grade

.. image:: https://landscape.io/github/pri22296/nlcalc/master/landscape.svg?style=flat
    :target: https://landscape.io/github/pri22296/nlcalc/master
    :alt: Code Health
   
.. image:: https://readthedocs.org/projects/nlcalc/badge/?version=latest
    :target: http://nlcalc.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. inclusion-marker-badges-end


.. inclusion-marker-introduction-start

**************************************************************************
Introduction
**************************************************************************

This Package is an example project for the
`botify <https://github.com/pri22296/botify>`_ framework. It can be
used to parse mathematical expressions expressed in natural language
and evaluate the result.

.. inclusion-marker-introduction-end

.. inclusion-marker-usage-start

**************************************************************************
Usage
**************************************************************************

.. code:: python

    >>> from nlcalc import NLCalculator
    >>> my_calc = NLCalculator()
    >>> result = my_calc.calculate("what is two plus twenty five")
    >>> print(result)
    27
    >>> result = my_calc.calculate("3 square plus four square")
    >>> print(result)
    25

.. inclusion-marker-usage-end


.. inclusion-marker-install-start

**************************************************************************
Installation
**************************************************************************

::

    pip install nlcalc


.. inclusion-marker-install-end


.. inclusion-marker-links-start

**************************************************************************
Links
**************************************************************************

* `Documentation <http://nlcalc.readthedocs.io/en/latest/>`_

* `Source <https://github.com/pri22296/nlcalc>`_

* `API Reference <http://nlcalc.readthedocs.io/en/latest/source/nlcalc.html#module-nlcalc>`_


.. inclusion-marker-links-end


.. inclusion-marker-license-start

**************************************************************************
License
**************************************************************************

This project is licensed under the MIT License - see the `LICENSE.txt <https://github.com/pri22296/nlcalc/blob/master/LICENSE.txt>`_ file for details.


.. inclusion-marker-license-end
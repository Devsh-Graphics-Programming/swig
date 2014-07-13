#!/usr/bin/python

import doxygen_basic_notranslate
import string
import sys
import commentVerifier

commentVerifier.check(doxygen_basic_notranslate.function.__doc__,
    r"""
    \brief
    Brief description.

    The comment text
    \author Some author
    \return Some number
    \sa function2

    """
)

commentVerifier.check(doxygen_basic_notranslate.function2.__doc__,
    r"""
    A test of a very very very very very very very very very very very very very very very very
    very very very very very long comment string.

    """
)

commentVerifier.check(doxygen_basic_notranslate.function3.__doc__,
    r"""
    *Overload 1:*

     A test for overloaded functions
     This is function \b one
     
    *Overload 2:*

     A test for overloaded functions
     This is function \b two
     
    """
)

commentVerifier.check(doxygen_basic_notranslate.function4.__doc__,
    r"""
    A test of some mixed tag usage
    \if CONDITION
    This \a code fragment shows us something \.
    \par Minuses:
    \arg it's senseless
    \arg it's stupid
    \arg it's null

    \warning This may not work as expected

    \code
    int main() { while(true); }
    \endcode
    \endif

    """
)
commentVerifier.check(doxygen_basic_notranslate.function5.__doc__,
    r"""
    This is a post comment. 
    """
)
commentVerifier.check(doxygen_basic_notranslate.function6.__doc__,
    r"""
    Test for default args
    @param a Some parameter, default is 42

    """
)
commentVerifier.check(doxygen_basic_notranslate.function7.__doc__,
    r"""
    Test for a parameter with difficult type
    (mostly for python)
    @param a Very strange param

    """
)

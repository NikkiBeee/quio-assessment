#Overview
Thanks for the opportunity to complete a coding assessment for QuiO. The following repository corresponds to [this prompt] (https://docs.google.com/document/d/1Lr0SQ4j9-i5y8MUbWsqd0vaXvNKtcWeeNhCWUojkSQ4/edit?usp=sharing)

#Repo Contents
* All iterations of the interview function has been organized in the 'interviewIterations' directory. 'interview0.py' is the original given code in the prompt and each file is incremented accordingly based on the steps in the prompt.
* The 'testFileStructure' directory is used for the black box tests. I've created files and subdirectories to cover the following use cases: 
  * Reads a file within a directory
  * Reads multiple files within a directory
  * Reads files within subdirectories (multiple levels)
  * Does not throw error or break if directory is empty
  * Does not throw error or break if file is empty
* ./tests.sh - Will run the the black box tests and static analyses


#Written Responses to Prompt
* Step 1: Issues with interview0.py. First issue: the given code only printed out the even lines of each file. Second issue: the given code printed out a summary of the output multiple times instead of once at the end. Fixes are in interview1.py 
  * The first issue occurred because in each evaluation of the while loop, the ".readline()" method is invoked and the first line of the file is read. Once the first line of the file is read, the next time the method is called, it reads the second line. This occurs in within the while loop, and the second line is printed. This repeats with the 3rd line being evaluated as the criteria for the while loop, and the fourth line is printed, etc. To fix this, I removed the while loop and utilized the ".read()" method
  * The second issue occurs because the whole function is being called recursively, and prints out the current summary of traversed folders each time the function is called. To fix this, I created a helper function within the interview function that can be called recursively, and placed the line to print the output outside of this helper function.
* Step 2: Proper file handling. The given code did not close the files back and also opened them with read AND write ability. To fix this, I added code to close each file after reading it, and changed the 'r+' to 'r' in the open function to ensure that the program only had read capabilities. Fixes are in interview2.py
* Step 3: Static Analysis. Using the prospector tool, I discovered that there was an unused wildcard import. To fix, I deleted the unnecessary "from typing import *" line in the code. See end of README for full error. Fixes are in interview3.py
* Step 4: Whitebox Testing. Based on all my research, my understanding is that white box testing tests for the structure of the code. The options and examples I found, were all for testing methods on a class, and I was unable to find an adequate solution for a stand alone function. I will need to keep researching. With the proper methods, I'd check number of times print was called, number of times the helper "read_Files" function was called, and ensure every open file was closed. 
* Step 5:  Cyclomatic Complexity. The Cyclomatic Complexity of interview3.py is 6 and is below 10 - within acceptable range. [Image of control flow graph here.](https://screencast.com/t/agK74bVtUd)

        Source: https://en.wikipedia.org/wiki/Cyclomatic_complexity
        The complexity M is then defined as[2]

        M = E − N + 2P,
        where

        E = the number of edges of the graph --> 13
        N = the number of nodes of the graph. --> 9
        P = the number of connected components. --> 1

        M = 13 - 9 + 2(1)
        M = 6
* Unusual Bug. I tested running the interview function in interview3.py twice, and received expected results. 




#Notes
Errors found with prospector tool:

  interview2.py
  Line: 2
    pylint: unused-wildcard-import / 
    Unused imports from wildcard import: abc, collections, contextlib, functools, operator, stdlib_re, sys, types, Any, NoReturn, ClassVar, Union, Optional, ForwardRef, TypeVar, Generic, cast, get_type_hints, no_type_check, no_type_check_decorator, overload, T, KT, VT, T_co, V_co, VT_co, T_contra, CT_co, AnyStr, Hashable, Awaitable, Coroutine, AsyncIterable, AsyncIterator, Iterable, Iterator, Reversible, Sized, Container, Collection, Callable, AbstractSet, MutableSet, Mapping, MutableMapping, Sequence, MutableSequence, ByteString, Tuple, List, Deque, Set, FrozenSet, MappingView, KeysView, ItemsView, ValuesView, ContextManager, AsyncContextManager, Dict, DefaultDict, OrderedDict, Counter, ChainMap, Generator, AsyncGenerator, Type, SupportsInt, SupportsFloat, SupportsComplex, SupportsBytes, SupportsAbs, SupportsRound, NamedTupleMeta, NamedTuple, NewType, Text, TYPE_CHECKING, IO, BinaryIO, TextIO, io, Pattern, Match, re, abstractmethod, abstractproperty, WrapperDescriptorType, MethodWrapperType, MethodDescriptorType
    pyflakes: F401 / 'typing.*' imported but unused (col 1)
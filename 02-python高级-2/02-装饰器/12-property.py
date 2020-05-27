#!/usr/bin/env python
# -*- coding:utf-8 -*-

      class  Student(object):
	  
         @property
         def  get_score(self):
              return self._score
			  
         @get_score.setter
         def  score(self, value): 
             if not isinstance(value, int)
                 raise ValueError('score must be integer')
             if value<0 or value >100:
                 raise ValueError('score must between 0 ~100!')
             self._score = value
		
      s = Student()
      s.score = 60
      s.get_score

In [21]: s.
s.get_score  s.score    


In [18]: s.score = -60
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-18-c86bd3850b05> in <module>()
----> 1 s.score = -60

<ipython-input-14-d4664cf934a9> in score(self, value)
      8             raise ValueError('score must be integer')
      9         if value<0 or value>100:
---> 10             raise ValueError('score must between 0 ~100!')
     11         self._score = value
     12 

ValueError: score must between 0 ~100!




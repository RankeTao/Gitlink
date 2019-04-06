# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time
"""
calculate day hour minute second since the Epoch
"""
t = time.time()
(tminute, second) = divmod(t, 60.0)
(thour, minute) = divmod(tminute, 60)
(day, hour) = divmod(thour, 24)
print("Time has passed %f days %f hours %f minutes %.2f seconds since the Epoch" % (day, hour, minute, second))
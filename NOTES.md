For task2 I reviewed several commonly used email validation regex 
patterns but found that none provide full accuracy.
Valid email formats vary widely, including quoted local parts, 
Unicode characters, IP-based domains, and unusual but technically 
correct structures. Most regexes either reject valid but uncommon 
addresses or accept clearly invalid ones.

For all tasks, I designed small tests that specifically target 
edge cases and boundary conditions to evaluate the robustness 
and correctness of each implementation. I have included all of 
these tests under the test folder.
__author__ = 'student'

from sock1_reader_writer.reader_writer import reader_writer
from socket import socket

sock = socket()

sock.connect(('localhost',12345))

print("Connection made")

rw = reader_writer(sock)

data = '''This is the story of what a Woman's patience can endure, and what a
Man's resolution can achieve.

If the machinery of the Law could be depended on to fathom every case
of suspicion, and to conduct every process of inquiry, with moderate
assistance only from the lubricating influences of oil of gold, the
events which fill these pages might have claimed their share of the
public attention in a Court of Justice.

But the Law is still, in certain inevitable cases, the pre-engaged
servant of the long purse; and the story is left to be told, for the
first time, in this place.  As the Judge might once have heard it, so
the Reader shall hear it now.  No circumstance of importance, from the
beginning to the end of the disclosure, shall be related on hearsay
evidence.  When the writer of these introductory lines (Walter
Hartright by name) happens to be more closely connected than others
with the incidents to be recorded, he will describe them in his own
person.  When his experience fails, he will retire from the position of
narrator; and his task will be continued, from the point at which he
has left it off, by other persons who can speak to the circumstances
under notice from their own knowledge, just as clearly and positively
as he has spoken before them.

Thus, the story here presented will be told by more than one pen, as
the story of an offence against the laws is told in Court by more than
one witness--with the same object, in both cases, to present the truth
always in its most direct and most intelligible aspect; and to trace
the course of one complete series of events, by making the persons who
have been most closely connected with them, at each successive stage,
relate their own experience, word for word.

Let Walter Hartright, teacher of drawing, aged twenty-eight years, be
heard first.

'''

for c in data:
    rw.write(c)
rw.close_write()

print("sending done")

c = rw.read()
while c:
    print(c,end='') #same line
    c = rw.read()

sock.close()
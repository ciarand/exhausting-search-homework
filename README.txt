= Exhaustive Search
Ciaran Downey <ciarand@csu.fullerton.edu>

This is my solution to project 2, "exhaustive search," which involves
implementing solutions to the Euclidean versions of the minimum spanning
tree and traveling salesman problems.

== Structure

The app is distributed as a pip bundle. This helps make sure that tests are
sanitary (i.e. no unresolved dependencies at runtime on a foreign system).

The authors have provided some helpful `make` commands to ease the process
of installation and testing.

The actual `euclidean_mst` and `euclidean_tsp` functions are defined in the
`src/exhaustive_search` module. They are unit tested with `pytest`
(coordinated via `tox`).

Additionally, a modified version of the GUI script is available via the
`bin/gui` tool. See <<Running the GUI>> for more details.

== Prequisites for running the GUI

- Python3 (available as `python3`)
- tkinkter for Python3
- pip for Python3 (default expected name is `pip3`)

== Running the GUI

Get the dependencies first:

[source,sh]
----
pip3 install -e requirements.txt
----

Now to run the script for the minimum spanning tree problem:

----
./bin/gui mst
----

Or, for the traveling salesman problem:

[source,sh]
----
./bin/gui tsp
----

== Setting up a development environment

=== Prequisites

- virtualenv for Python3 (default expected name is `virtualenv3`)
- GNU Make (shown in the examples as `make`)

=== Initial setup

Run `make deps` to setup your virtualenv, then run `source env/bin/activate`
to setup your $PATH as appropriate for the project. When you're done, you
can run your virtualenv's `deactivate` bin to restore your $PATH.

== Development commands

- make deps - installs the dependencies (minus tkinter)
- make test - runs the tests

=== Supporting alternative command names

All of the above binaries may be available under different names. For
`make`, this may be that the GNU Make is under `gmake`. That's ok, you can
run `gmake $COMMAND` just the same.

For the others, custom names are accomplished via environment variables:

[source,sh]
----
PIP=pip-dev PYTHON=custompython3 VIRTUALENV=customvirtualenv3 make $COMMAND
----

=== Pointing Python to Tcl/Tk

The gui depends on the `tkinter` package, which isn't available via `pip`.
Assuming you have the appropriate tcl/tk libraries installed, configuration
is achieved through environment variables. As an example, on Ubuntu the
configuration will look something like this:

[source,bash]
----
TK_LIBRARY=/usr/lib/python2.7/lib-tk:/usr/lib/python2.7/site-packages/PIL:/usr/lib
TKPATH=/usr/lib/python2.7/lib-tk:/usr/lib/python2.7/site-packages/PIL:/usr/lib
TCL_LIBRARY=/usr/lib
export TCL_LIBRARY TK_LIBRARY TKPATH
----

=== Supporting other Python versions

Normally tox tests are run against Python 3.4 (py34). If you need to target
a different version, you can edit the tox/envlist parameter in tox.ini like
so:

----
[tox]
envlist = py34,py33,py32,pyWhatever,CoolPy,etc
----

Just rerun `make test` (or `tox`) to see the new tests being run.

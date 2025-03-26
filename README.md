# paper-folding-model-maven
A Computational Model for Reasoning About the Paper Folding Task Using Visual Mental Images

We instead adopt the approach of implementing a computational cognitive model that simulates solving the task—the cognitive systems approach of artificial intelligence.

Cognitive systems model how intelligent agents combine different cognitive processes, like learning, reasoning, and memory, to perform a task. By implementing a cognitive system that simulates solving visuospatial tasks, we can look “under the hood” at specific types of information processing mechanisms that might drive visuospatial ability.

In particular, the model we present can be considered as an experiment on the sufficiency of certain imagery-based
representations and operations for solving paper folding,
which is valuable for understanding how different cognitive
mechanisms might in theory contribute to visuospatial abil-
ity in people, and especially how certain cognitive limitations
might affect task performance. Ultimately, we hope that re-
sults from this line of work will serve as a basis to suggest
routes for how such cognitive limitations might eventually be
overcome, i.e., in developing new visuospatial training inter-
ventions for use in education.

Paper folding tasks are usually presented as line-drawings of
paper cut-outs or folded pieces of paper. People are then
asked to imagine changes that happen when this paper is ma-
nipulated in different ways.

Next, we present a computational model that attempts to
solve the paper folding task using simulated “mental rota-
tions” in “three dimensions”. The exact formulation of the
paper folding task we intend to tackle with this model is “The
Punched Hole” test (Ekstrom et al., 1976).

A sequence of images sent as input to the model
(blue and white), and the corresponding bitmaps that are used
by the model after inputs are processed (black and white).
The first input row corresponds to the initial “problem” part
of a paper folding item. The second input row contains the
possible choices the model is presented with.

The main task of the model is to analyze a sequence of
images that depict the folding and punching in a problem
of the paper folding task to determine what the paper would
look like when unfolded. It achieves this by maintaining a
three dimensional representation of the paper which is stored
as a stack of two dimensional images. Each image on the
stack represents a single level of folding performed in a single
time-slice. The actual fold operations are performed with im-
age reflections that provide a simplified simulation of three-
dimensional rotations.

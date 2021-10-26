# Adding Heterogeneity to the Schelling Model
## Mira Flynn and Ben Morris

### 1. Abstract

With this project, we want to further investigate the Schelling model of segregation. We recreate experiments from several papers that include Schelling's original model and papers including an extension of the model, varying vision distance of each cell. After investigating those models, we further extend Schelling’s model by exploring the addition of a preference for heterogeneity. In real life, people may prefer to be around a varied assortment of people. Here, we explore what threshold of percent preference for heterogeneity leads to integrated societies across various vision distances.

### 2. Schelling’s Model

Schelling’s original model centered on a grid of squares, representing some city. Each square would either be red, blue, or empty. The inhabitants of the grid are “happy” if the percent of the houses in their Moore neighborhood (the eight surrounding cells) that share a color with them is above a certain threshold.

![Base Schelling threshold example 1](imgs/moore_examples.png)

Figure 2.1: In the left graphs, the middle cell is happy, as the surrounding cells are more than 37.5% red. In the right graphs, the middle cell is unhappy, since less than 37.5% of surrounding cells are red. Empty squares, as in the bottom row, are not counted.

Each time step, Schelling selects an unhappy square at random and moves it to an empty cell, and runs this simulation with a few thousand updates. Schelling shows that even with relatively low thresholds, segregation occurs in a society, as shown in Figure 2.2, below.

![An example city with Schelling’s original model](imgs/schelling_moore_city.png)

Figure 2.2: An example city generated with Schelling’s original model. As time progresses, the city becomes more segregated.

To track the movement towards segregation, we calculate, for each cell, the percentage of occupied houses they can see which share a color with them. The segregation coefficient for the entire city is the average of all of these. Plotting this coefficient over time gives a graph like that in Figure 2.3.

![Schelling model results](imgs/schelling_moore_results.png)

Figure 2.3: The average segregation coefficient over time. The flat section at the end shows the equilibrium position when all cells are happy, somewhere around 75%.

### 3. Variable Radius

In the variable radius model, the only thing that changes is the kernel - each cell’s effective vision. The variable radius model assumes any cell is a neighbor if the Manhattan distance from the center cell to the cell in question is less than or equal to the radius. Figure 3.1 shows the Moore kernel from the original model and kernels for each radius value we tested:

![The kernels we used for testing the Schelling model and the vision radius expansion](imgs/kernels_demo.png)

Figure 3.1: The Moore kernel and various von Neumann kernels.

Here is an image of the graph created using the vision radius model, which measures the final segregation level versus vision radius and preference threshold:

![Segregation vs. Vision Radius and Preference for the vision radius model](imgs/s_vs_r_p_base.png)

Figure 3.2: Equilibrium segregation coefficient across various visions and thresholds

This wide range of values for each preference threshold can be seen qualitatively in Figure 3.3. As the threshold increases, the size of the single-colored blobs - segregated neighborhoods - also tends to increase. And, as radius increases, the segregation becomes more extreme; integrated cities become more integrated and segregated cities become more segregated.

![Qualitative Segregation vs Vision Radius](imgs/3x3_radius_by_threshold.png)

Figure 3.3: Equilibrium cities for varying vision radii and segregation thresholds.


### 4. Heterogeneity

To further extend this model, we added a preference heterogeneity to this model. In real life, it might not be the case that people would be happy if everyone around them was the same as them. Instead, some may prefer a mixture of different types of people. Whether or not this assumption is adhered to has the potential to have huge impacts on the results of the model. In the original Schelling paper, and in the vision extension paper, agents always prefer more of their same type, so while the extent of segregation may be surprising, segregation itself is not necessarily surprising. If instead some agents preferred to be around a mixture of people, the anticipated results are a bit harder to determine. Here, we delve into cities that contain agents with a preference for both homogeneity and heterogeneity, and explore when, if ever, this may produce more integrated cities than in the previous models.

When the city is created, the same rules are mostly kept; each square either represents an empty house, a blue house, or a red house. However, each agent is also randomly chosen to have a preference for homogeneity or heterogeneity, which stays with them as they move. The proportion of agents with a heterogenous preference is an extra parameter of the model. An agent is unhappy if:

- It has a preference for homogeneity and the percent same is less than the given threshold OR

- It has a preference for heterogeneity and the percent same is less than half the given threshold or the percent difference is less than half the given threshold

	- Half the threshold is used here so that the valid domain for the threshold remains between 0 and 1. If the threshold was not halved, all agents with a heterogenous preference would always be unhappy as soon as the threshold was more than 0.5.

### Appendix A: Annotated Bibliography

[Models of Segregation](https://www.jstor.org/stable/pdf/1823701.pdf)

Thomas C. Schelling (1969)

Schelling introduces a new type of segregation model consisting of two types of cells (not including empty cells). Each cell prefers to have more than half of its neighbors of the same type, and will move to an empty cell if the empty cell fits its preferences. This model has cells with only minor preferences, but produces very high segregation nonetheless. The only stable states are ones with high segregation. This new model offers an explanation for how segregation occurs by setting up several reasonable rules and showing a behavior that is prevalent in the real world.

[Role of 'Vision' in Neighbourhood Racial Segregation: A Variant of the Schelling Segregation Model](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.1027.3357&rep=rep1&type=pdf)

Alexander J. Laurie, Narendra K. Jaggi (2003) 

Laurie and Jaggi extend the Schelling Segregation Model by adding an extra parameter R - the vision, or the range houses each agent looks at when determining whether to move. They find that contrary to the original Schelling model, certain values of R produce stable, integrated societies. They use a metric to measure total segregation and, through many simulations, find that certain values of R and p (percent of people each agent would like to be the same in their neighborhood) actually lowers this metric compared to Schelling’s original report. This serves as both an explanation and a design – it explains how integrated societies could exist, and provides some ideas (none fully fleshed out, but still gives some) on how we can get closer to this type of society in practice.

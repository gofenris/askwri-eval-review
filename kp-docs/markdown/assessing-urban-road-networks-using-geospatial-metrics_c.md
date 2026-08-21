---
doc_id: assessing-urban-road-networks-using-geospatial-metrics_c
source_pdf: documents/assessing-urban-road-networks-using-geospatial-metrics_c.pdf
extraction_method: postgres-full-text
parse_backend: mistral
parse_model: mistral-ocr-latest
char_count: 142306
title: Assessing Urban Road Networks Using Geospatial Metrics
authors: Archiman Biswas; Bina Shetty; Madhav Pai; Raj Bhagat Palanichamy; Sonal Ganvir; Janhavi Mane; Priam Pillai
date_published: 2026-07-09
year_published: 2026
article_type: Working Paper
wri_primary_office: WRI India
language: en
doi: 10.46830/wriwp.25.00042
status: searchable
---

WRI INDIA

# WORKING PAPER

# Assessing urban road networks using geospatial metrics

Authors: Archiman Biswas, Bina Shetty, Madhav Pai, Raj Bhagat Palanichamy, Sonal Ganvir, Janhavi Mane, and Priam Pillai

# CONTENTS

Highlights...1

Executive summary ...2

Introduction...3

Methodology...4

Key findings from the systematic literature review...5

Identified indicators...6

Data Management...14

Significance of identified indicators...15

Application of indicators to assess efficiency of urban road networks...16

Conclusion...20

Appendices...21

Abbreviations ...46

Endnotes...47

References...47

Acknowledgments...52

About the authors...52

Working Papers contain preliminary research, analysis, findings, and recommendations. They are circulated to stimulate timely discussion and critical feedback, and to influence ongoing debate on emerging issues.

Suggested Citation: Biswas, A., B. Shetty, M. Pai, R. B. Palanichamy, S. Ganvir, J. Mane, and P. Pillai. 2026. "Assessing urban road networks using geospatial metrics." Working Paper. New Delhi. Available online at: https://doi.org/10.46830/wriwp.25.00042

# Highlights

- Many Indian cities are grappling with acute mobility challenges, marked by declining travel speeds, and growing delays. Cities such as Kolkata, Bengaluru, Pune, and Hyderabad consistently rank among the world's most congested, according to the TomTom Traffic Index.
- Evaluating urban mobility efficiency necessitates the use of geospatial indicators of road networks that quantitatively describe their structural configuration. However, prior studies have rarely systematically identified indicators that explain these challenges. This working paper addresses this gap by identifying key metrics that influence road network connectivity and travel speeds across Indian cities.
- A multi-stage research design is employed, integrating a hybrid literature review, a PRISMA-guided screening process, and bibliometric analysis, followed by expert consultations to validate and contextualize the indicators and case examples from India to demonstrate the relevance of these indicators.
- Bibliometric analysis identifies five major thematic clusters: Nodal Connections, Road Segments, Barrier Blocks, Traffic Flow, and Directional Patterns. Our systematic literature review highlights 21 geospatial indicators.
- For each indicator, the paper outlines its definition, data and computational requirements, methodological steps, limitations, and analytical significance.

WRI INDIA

WORKING PAPER | July 2026

1

## Executive summary

### Context

Urban mobility in India faces persistent challenges arising from rapid population growth and largely unplanned urban expansion. Despite substantial investments in transport infrastructure, many Indian cities continue to experience declining travel speeds, increasing vehicular emissions, and inequitable access issues (TomTom Traffic Index 2025). Several previous studies have consistently highlighted the limited prioritization of public transit and pedestrian infrastructure as a key contributor to these challenges.

In the Indian context, systematic identification and assessment of indicators influencing road network connectivity remain relatively underexplored in academic literature. This gap highlights the need for a comprehensive evaluation of road network functionality that is sensitive to the spatial and morphological characteristics of Indian cities.

### About this working paper

This working paper seeks to identify the key geospatial indicators essential for evaluating road network connectivity in urban India. Hence, this study adopts a hybrid systematic literature review methodology, integrating the PRISMA framework with bibliometric analysis to synthesize both global and national research. Through this approach, the paper identifies and categorizes geospatial indicators associated with road connectivity and travel speed. These indicators were subsequently validated through expert

consultations to ensure their relevance to the heterogeneous and often organically evolved urban forms typical of Indian cities.

### Key findings

Several Indian studies reveal distinct urban morphologies shaped by unplanned, organic growth, particularly in older towns (Debnath 2022; Dhingra et al. 2017). These morphologies produce road networks featuring grid-tree hybrid layouts, elevated dead-end proportions, and irregular connectivity, especially in peri-urban areas (Arif & Gupta 2020; Biswas, Samanta, et al. 2025a; Haldar et al. 2023; Narain 2017; Narain & Nischal 2007). This structural divergence highlights the need for more research in the Indian context. These studies also emphasize metrics like Dead-End Proportion, Spatial Distribution of Dead-End Clusters, and Grid-Tree Pattern Index alongside road connectivity indices (Alpha, Beta, Gamma) for comprehensive evaluation (J. Li 2011; Mukherjee 2012a; Munshi 2016; Narain 2017; Narain & Nischal 2007; Pitale et al. 2025).

The bibliometric analysis highlights five major themes: Traffic Flow, Directional Patterns, Nodal Connections, Road Segments, and Barrier Blocks.

The systematic literature review identified a total of 21 geospatial indicators across the five thematic areas. Figure ES-1 visually presents the five themes and their associated indicators and summarizes the key outcomes of the study.

Figure ES-1 | Themes and indicators identified through systematic literature review and bibliometric analysis

![img-0.jpeg](img-0.jpeg)

Source: WRI India Authors.

2

[Non-Text]

WRI INDIA

Assessing urban road networks using geospatial metrics

**This working paper demonstrates the practical application of these indicators through case studies across Indian cities.**

The analyses reveal that areas with structured road layouts exhibit higher connectivity ratios, while neighborhoods with organic or unplanned morphologies show lower ratios, higher dead-end clusters, and substantial peak-hour speed reductions. These findings highlight the importance of the identified indicators for assessing road network connectivity in Indian cities.

## Introduction

Indian cities are currently grappling with an unprecedented urban mobility crisis. As the nation undergoes rapid urbanization and population growth, the rate of motorization has far outpaced infrastructure development. Consequently, major urban centers face persistent declining travel speeds, traffic congestion, and debilitating travel delays. According to the TomTom Traffic Index, Indian cities like Kolkata, Bengaluru, Pune, and Hyderabad consistently rank among the most congested globally (TomTom Traffic Index, 2025). This performance deficit is critical because a vast majority of India's population remains deeply dependent on road-based transport for daily mobility, freight movement, and access to essential services (Gadepalli, 2016).

Although congestion is the most visible symptom of the mobility crisis, the underlying cause often lies in the structural configuration of the road network. Road network connectivity (the ease with which paths connect different nodes) is a fundamental determinant of travel speed, route choice, and overall accessibility. This crisis is further compounded by historical underinvestment in public transit and a lack of robust travel demand management strategies.

The overall efficiency of a city's mobility remains largely undergirded by the structural configuration of its road network. Poor connectivity limits the number of available routes, forcing traffic into a few overburdened corridors and reducing the network's resilience to disruptions. In the current

Indian scenario, assessing connectivity has become an essential requirement for improving urban mobility outcomes and mitigating the economic losses associated with traffic delays.

Several studies indicate that a strong urban form depends on a well-planned hierarchical road network made up of arterial roads, collectors, and local streets (Albers et al. 2012; Das et al. 2019; Rivera-Royero et al. 2022; Vishnu et al. 2023; Wang et al. 2015). High connectivity is essential for urban sustainability because it reduces commuting costs and lowers environmental emissions by minimizing travel distances. Additionally, well-connected networks promote active transport modes, such as walking and cycling, by providing direct and safe routes (Barton et al. 2012; Debnath 2022). On the other hand, fragmented networks lead to a greater dependence on private vehicles, which in turn exacerbates congestion and environmental problems (Akbar et al. 2018; Cervero et al. 2009).

The urban landscape in India faces unique challenges that differ significantly from those in cities in the Global North. Urban growth in India tends to be unplanned, incremental, and organic (Arora and Gargava 2023; Kumar et al. 2017). This results in irregular street layouts characterized by "missing links", "dead ends", and lack of a clear functional hierarchy. Such organic sprawl leads to uneven accessibility across various urban zones. To address this complexity, geospatial tools provide an objective, scalable, and sophisticated framework for analysis. Unlike traditional surveys, geospatial metrics can identify intricate patterns of connectivity and network structure that are often overlooked in conventional planning (Biswas and Chattopadhyay 2024; Korzhenevych and Jain 2018).

Although several studies have been conducted in the Global North, very few have focused on the Indian context. Findings from the Global North are often not directly applicable to Indian cities due to significant differences in urban form, infrastructure provision, and travel behavior. Pai et al. (2025) highlight that road connectivity plays a pivotal role in shaping urban mobility outcomes in India and argue that a shift

**Table 1 | Mode of transport shares in Indian cities**

|  POPULATION | BUS | AUTO RICKSHAW | RAIL / METRO | CAR | MOTORIZED TWO-WHEELER | CYCLE | WALK | TOTAL  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  > 10 million | 20 | 3 | 14 | 6 | 9 | 5 | 43 | 100  |
|  1-10 million | 13 | 11 | 2 | 3 | 23 | 13 | 37 | 100  |
|  < 1 million | 4 | 13 | 0 | 2 | 27 | 6 | 49 | 100  |

Source: Gadepalli (2016).

WORKING PAPER | July 2026 | 3

from ad hoc, reactive, and project-centric interventions to a systemic, network-based planning approach is essential for achieving sustainable mobility outcomes. This study aims to address this gap by identifying and describing the geospatial indicators that influence road network connectivity and travel speeds in Indian cities. To achieve this, the study employs a multistage methodology involving a hybrid literature review, the Preferred Reporting Items for Systematic reviews and Meta-Analyses (PRISMA) framework, and a bibliometric analysis, followed by consultations with experts to validate the indicators. The indicators identified through this research are not exclusive to the Indian context; rather, this study evaluates their applicability and relevance to Indian cities through consultations with experts. This research will be helpful for urban planners, policymakers, and transport practitioners by providing a robust, context-sensitive geospatial framework to evaluate road network connectivity, inform evidence-based planning decisions, and guide targeted interventions aimed at improving travel efficiency and sustainable mobility in Indian cities.

## Methodology

### Systematic literature review

This systematic literature review aims to identify the geospatial indicators influencing road network connectivity and travel speeds in the Indian context.

The review was conducted following the PRISMA reporting guidelines (Biswas et al. 2024; Foláyan et al. 2024). The step-by-step PRISMA procedure, including literature identification, screening, eligibility assessment, and final inclusion, is explained in detail in Appendices A and B, and the PRISMA flow diagram is presented in Figure 1. In addition, a bibliometric analysis was undertaken to understand publication trends, thematic evolution, and research clusters within the reviewed literature.

### Themes identified using bibliometric analysis

To identify the key thematic clusters for classification of indicators, a keyword co-occurrence analysis was conducted to reveal emerging focus areas within the field of geospatial indicators and their influence on road connectivity and travel speeds. This approach helps uncover prevailing research themes (Biswas et al. 2024).

The network clustering revealed five major thematic groups (Figure 2). The naming of each theme was based on the nature of the indicators and keywords grouped within the respective clusters (Appendix C).

Figure 1 | The PRISMA flowchart

![img-1.jpeg](img-1.jpeg)

* Considered publications from the last 10 years (2014–2025)

Source: WRI India Authors.

4

[Non-Text]

WRI INDIA

Assessing urban road networks using geospatial metrics

Figure 2 | Keyword co-occurrence network showing the five major themes identified through bibliometric analysis using VOSviewer

![img-2.jpeg](img-2.jpeg)

Source: WRI India Authors.

The first cluster (the green cluster) includes keywords such as Average Travel Speeds, Congestion Frequency Index, Transport Performance in Grid versus Radial Layout, Modal Split Ratios, Accessibility to Employment Centers, Freight Route Performance, and Travel Time Reliability Index. These keywords primarily relate to an assessment of the efficiency of movement for people and goods within a road network, emphasizing aspects such as congestion, reliability, and overall system responsiveness. Hence, we named this cluster “Traffic Flow.”

The second cluster (the red cluster) comprises keywords such as Compass-Based Connectivity Score, Directional Bias in Old Towns, Mean Directional Bias, Directional Symmetry in Colonial Layouts, Local Indicator of Spatial Association (LISA), Direction-Based Accessibility Gradient, and Directional Skewness. These terms highlight the significance of orientation, flow patterns, and spatial configuration within road networks. Therefore, we named this cluster “Directional Patterns.”

The third cluster (the purple cluster) includes keywords such as 4-Way Intersection Proportion, Angular Connectivity, Average Connections Per Node, Average Link Length Per Node, Average Node Degree, Central Node Proportion, and Critical Junction Count. These indicators emphasize the connectivity and structural characteristics of intersections or nodes within the transport network that play a vital role in determining flow efficiency and route flexibility. Accordingly, we named this cluster “Nodal Connections.”

The fourth cluster (the yellowish-green cluster) comprises keywords such as Average Segment Straightness, Segment Diversity Index, Segment Redundancy Factor, Road Density Index, Segment Accessibility Per Block, and Right-of-Way Consistency. These indicators evaluate the condition, continuity, and geometric design of individual road segments, assessing how they contribute to overall network connectivity,

redundancy, and travel efficiency. Hence, we named this cluster “Road Segments.”

The fifth cluster (blue cluster) consists of keywords such as Block-Level Integration Score, Number of Barrier Edges, Visual Permeability of Blocks, Inward-Facing Block Proportion, Number of Isolated Blocks, Barrier Block Identification Index, and Closed Block Density. These terms collectively focus on identifying and characterizing physical or visual barriers within the urban fabric that impede connectivity. Therefore, we named this cluster “Barrier Blocks.”

Additionally, an expert consultation was conducted involving professors, specialists from WRI India, and practitioners from urban local bodies (ULBs) to assess the relevance of the identified indicators.

### Key findings from the systematic literature review

The majority of studies on road network structure and traffic speeds were conducted in the Global North, as well as in China (Boeing 2021a; Kickert et al. 2020; Zhang et al. 2017). However, there is a notable lack of such research in the Indian context, where urban dynamics, infrastructure conditions, and travel behaviors may differ significantly (Appendix D) (Debnath 2022; Kumar et al. 2017).

Studies conducted in India reveal unique urban morphology and transportation challenges. Indian cities, particularly older ones such as Varanasi, Ujjain, Madurai, and Alwar, have grown organically with limited or no initial planning (Biswas et al. 2025a; Debnath 2022; Dhingra et al. 2017). This has led to road networks that diverge significantly from the grid-based, hierarchical structures commonly found in the cities of developed countries. Several studies have pointed out that the road layout in such older Indian cities often exhibits a

WORKING PAPER | July 2026

5

grid-tree hybrid pattern, resulting in a high proportion of dead ends and irregular connectivity, especially in peri-urban areas (Arif and Gupta 2020; Biswas and Chattopadhyay 2024; Biswas et al. 2025b; Haldar et al. 2023; Narain 2017; Narain and Nischal 2007).

The literature on Indian cities consistently highlights the importance of including dead-end proportion, spatial distribution of dead-end clusters, and the grid-tree pattern index as critical measures under the broader umbrella of degree of connectivity (Boeing 2017; Debnath 2022; Sreelekha et al. 2016). These indicators are crucial for capturing micro-scale accessibility and identifying the structural inefficiencies that arise due to unplanned urban sprawl. For instance, a high dead-end density typically signals poor network permeability and limited route options, contributing to localized congestion and reduced travel efficiency (Li 2011; Mukherjee 2012; Munshi 2016; Narain 2017; Narain and Nischal 2007; Pitale et al. 2025).

Further, this review has revealed that although conventional network connectivity indices such as alpha, beta, and gamma remain useful for assessing overall connectivity, they are insufficient on their own to capture the complexities of the Indian road network. Therefore, the integration of indicators such as dead-end proportions and dead-end clustering alongside conventional connectivity metrics presents a more holistic framework for evaluating road networks in the Indian context.

Studies on active travel modes and road network connectivity further reinforce the importance of these indicators. Research on walkability and cycling behavior reveals that high network

connectivity and road layout quality can positively influence active travel choices. For instance, Knapskog developed a walkability assessment tool for neighborhood-level transit nodes in Norwegian cities, incorporating indicators such as travel-distance-to-road-density-index ratio, degree of connectivity (alpha, beta, gamma), and travel time. The study found that dense, permeable, and well-connected environments near public transport nodes significantly support zero-traffic growth policies and encourage walking over car use. Accordingly, the identified indicators were classified into five themes (Figure 3).

## Identified indicators

This section presents a comprehensive analysis of the key indicators identified through the systematic literature review.

### Nodal Connections (NC)

#### NC 1: Node to length ratio

##### DEFINITION

The node-to-length ratio is a measure of the connectedness of a road network. It is calculated by dividing the total number of nodes (intersections) by the total length of the road network within that network. Nodes represent decision points such as intersections, junctions, and roundabouts, whereas road segments (edges) connect adjacent nodes. A higher node-to-length ratio suggests more intersections per unit length of road, indicating a better-connected network, whereas a lower ratio implies a lower intersection density and inferior

Figure 3 | Themes and indicators identified with the help of a systematic literature review and bibliometric analysis

![img-3.jpeg](img-3.jpeg)

Source: WRI India Authors.

6 | WRI INDIA

Assessing urban road networks using geospatial metrics

network connectivity (Mukherjee 2012; Nagurney et al. 2001; Turok et al. 2021).

## METHOD

Node-to-length-ratio = Number of nodes / Total length of road network

### LIMITATIONS

The node-to-length ratio can vary significantly depending on the scale of the analysis (e.g., citywide versus neighborhood-level networks), making comparisons challenging.

### NC 2: Average connections per node

#### DEFINITION

The average connections per node indicator represents the number of road sections meeting at a junction node. It indicates how well a road network is connected. A moderate number of connections could indicate better accessibility and network flexibility, whereas too many connections at a single junction could lead to operational inefficiencies and traffic-related challenges (Jabari 2016; Wang et al. 2011, 2014).

#### METHODS

Average connections per node is a key metric used to assess the connectivity of a road network. It represents the mean number of connections or road segments linked to each node, where a node typically corresponds to a junction, intersection, or endpoint in the network. The formula used to calculate this metric is

Average connections per node =  \( \Sigma \)  Number of connections at each node / Total number of nodes

This value indicates how well the network is structured in terms of interconnectivity. This metric can be calculated using geographic information systems (GIS) software. In QGIS, the road network is first converted into a set of nodes by extracting the vertices from the road lines using the Extract Vertices tool. Each node is then analyzed to determine how many road segments connect to it, which can be done by identifying the number of lines intersecting at each node using spatial analysis tools. The sum of these connections is then divided by the total number of unique nodes to compute the average. In ArcGIS, a similar process is followed using tools such as Intersect, Spatial Join, and Summary Statistics to derive the total number of connections and the node count. This value gives a quantitative measure of the overall connectivity within the road network and serves as a useful indicator in urban planning and transport analysis.

#### LIMITATIONS

This metric accounts only for the number of connections at nodes but does not consider the quality or capacity of those

connections, such as road width, traffic control measures, or directional flow, which affect actual accessibility and network performance. Cities have diverse road network morphologies (organic versus planned), and the average connections per node metric might not fully reflect the complexity of connectivity for irregular or mixed layouts; supplementary indicators or qualitative analysis may be required.

### NC 3: Node angle extremities

#### DEFINITION

The node angle extremities indicator refers to the angles formed between intersecting roads at a node (i.e., an intersection). The “skewness” of an intersection describes the degree to which the intersection angle deviates from the standard  \( 90^{\circ} \)  configuration (Distefano and Leonardi 2018). An intersection with a perfect right angle ( \( 90^{\circ} \) ) is considered optimal in terms of safety and traffic flow, whereas skewed intersections—those with acute or obtuse angles—pose challenges in terms of visibility, maneuverability, and safety (Yang et al. 2025).

#### METHODS

The measurement of node angle extremities involves determining the angles formed between intersecting roads at a given node to assess their deviation from the optimal  \( 90^{\circ} \)  configuration. One of the most common methods for this analysis is GIS, where digital mapping tools extract and measure intersection angles automatically. This allows planners to evaluate large road networks efficiently and identify problematic intersections.

#### LIMITATIONS

One of the key limitations in measuring node angle extremities is the availability and quality of data. Accurate assessment of intersection skewness relies on high-resolution geospatial data, which may not always be accessible or up to date for all regions, particularly in developing areas or rapidly changing urban environments.

### NC 4: Dead-end proportion

#### DEFINITION

The dead-end proportion indicator refers to the ratio or density of dead-end streets (or cul-de-sacs) in a road network relative to its total street length, node count, or area. A dead end is a road segment that terminates without connecting to another street, forming a node with only one link. This metric is often used to assess the connectivity of road networks and their suitability for traffic flow, pedestrian accessibility, or urban planning (Arora and Gargava 2023; Debnath 2022).

WORKING PAPER | July 2026

7

## METHODS

The dead-end proportion is determined by identifying nodes within a road network that are connected to only one edge:

\[
\text { Dead - end   proportion } = \mathrm{N} ^ {\text { dead }} / \mathrm{N} ^ {\text { total }}
\]

### LIMITATIONS

One key limitation in assessing dead-end streets using satellite or remote sensing data is the potential for inaccuracies due to outdated imagery, visual obstructions, or the inability to capture details such as private gates or temporary closures, which can lead to misidentification. Additionally, many dead ends exist intentionally within gated communities, industrial areas, or restricted-access zones, where they serve security or privacy functions rather than indicating poor connectivity, and should ideally be excluded from connectivity analyses (Low 2001). For a more nuanced understanding of network connectivity, two separate analyses could be conducted, one considering the boundaries of gated communities, industrial complexes, and restricted areas and another considering only the underlying road network irrespective of such boundaries.

### NC 5: Spatial distribution of dead-end clusters

#### DEFINITION

The spatial distribution of dead-end clusters indicator refers to the arrangement and grouping of dead-end streets within specific urban zones. It identifies areas where dead-ends are concentrated, revealing patterns that may impact transportation efficiency, land use, and accessibility. Dead-end clusters provide valuable insights into urban planning, connectivity issues, and potential traffic bottlenecks, allowing planners to evaluate how these clusters affect overall mobility.

#### METHODS

The assessment of dead-end clusters begins by calculating the degree  \( d(v) \)  of each node v, which represents the number of connected edges at a given intersection. Nodes with  \( d(v) = 1 \)  are classified as dead-end nodes. Once such nodes are identified, spatial analysis techniques, such as clustering algorithms or spatial autocorrelation methods (e.g., Moran's I), can be applied to detect the formation of dead-end clusters across an urban area (Lee and Li 2017).

#### LIMITATIONS

Dead-end clusters do not always indicate inefficiencies, because many residential and industrial areas are intentionally designed with dead-ends for safety and controlled traffic flow. This makes interpretation complex: planners must distinguish between planned and unplanned dead-end formations.

### Road Segments (RS)

#### RS 1: Shimbel distance

#### DEFINITION

Introduced by Alfred Shimbel in 1953, the Shimbel distance is a fundamental concept in network analysis that is used to measure the shortest path distances between nodes in a network. It quantifies the accessibility of locations based on the number of edges required to reach other nodes (Guze 2019). The Shimbel distance matrix represents the shortest paths between nodes, and the total distance for each row in this matrix is the Shimbel distance for that location (Istrate 2015). A lower Shimbel distance indicates higher accessibility, whereas a higher value signifies poor connectivity (Guze 2019).

#### METHODS

The Shimbel index is used to determine the accessibility of the network. It represents the sum of the lengths of all the shortest path distances among all points (vertices and nodes) in a circuit. A lower Shimbel index indicates higher accessibility, whereas a higher index indicates lower accessibility. The Shimbel index is expressed as

\[
\mathbf {S I} _ {\mathrm{i}} = \sum_ {i = 1} ^ {n} d _ {i j}
\]

where  \( SI_{i} \)  is the Shimbel index for node i,  \( d_{ij} \)  represents the shortest distance between nodes i and j, and n denotes the total number of nodes in the network.

#### LIMITATIONS

Despite its usefulness, the Shimbel distance has certain limitations. Incomplete or outdated data could lead to inaccurate accessibility assessments. Additionally, the Shimbel index primarily considers connectivity based on the number of arcs, without accounting for real-world travel constraints such as congestion, road conditions, or traffic regulations. It assumes uniform travel conditions across all road segments, which may not always be the case.

### RS 2: Average circuitry

#### DEFINITION

The average circuitry measures the degree to which actual travel paths in a network deviate from the most direct (straight-line) paths between nodes. It quantifies network efficiency by comparing actual travel distances with the corresponding Euclidean distances. Mathematically, circuitry is calculated as the ratio of the actual path length to the straight-line distance for a given origin-destination pair, with values equal to or greater than 1. The average circuitry is obtained by taking the mean of these ratios across all node pairs in the network (Boeing 2025; Cruise et al. 2017).

8

[Non-Text]

WRI INDIA

Assessing urban road networks using geospatial metrics

## METHODS

The average circuitry of a transportation network is calculated using the formula:

\[
\text { Average   circuitry } = (\Sigma \text { Actual   travel   distances }) / (\Sigma \text { Straight   line   distances })
\]

This method requires determining the shortest possible straight-line distances between nodes and comparing them to the real-world travel distances along the existing network. GIS and network analysis tools, such as ArcGIS or QGIS, are commonly used to compute these values efficiently for large-scale networks. Urban transportation networks exhibit circuitry values ranging from approximately 1.05 to 1.8, depending on factors such as network type, urban form, and city density (Boeing 2017b, 2019b).

### LIMITATIONS

Although circuitry is a useful measure of network efficiency, it has several limitations. The metric focuses on shortest paths, potentially overlooking alternative routes that provide greater resilience and redundancy in the network. Furthermore, unless weighted adjustments are introduced, circuitry fails to account for spatial constraints, such as land use, topography, or urban design elements. Despite these limitations, circuitry remains a valuable tool for assessing network performance and guiding transportation planning decisions.

### RS 3: Degree of connectivity (Alpha, Beta, and Gamma Indices)

#### DEFINITION

The degree of connectivity measures how well a network's nodes (junctions or vertices) and links (roads or edges) are interconnected. It is a fundamental concept in graph theory, urban planning, and transportation engineering, and is used to evaluate a network's efficiency, robustness, and redundancy (Oyebisi et al. 2025). Connectivity is quantified through three key indices (Cichocki and Amari 2010):

Alpha index ( \( \alpha \) ): It measures the proportion of actual cycles (closed loops) in a network relative to the maximum possible cycles. It ranges from 0 to 1, where 0 indicates no cycles (a tree structure), and values closer to 1 represent highly interconnected networks (Cichocki and Amari 2010; Oyebisi et al. 2025).

Beta index ( \( \beta \) ): It represents the ratio of edges (links) to nodes (vertices) (Millsap and Hartog 1988; Oyebisi et al. 2025; Waples and Gaggiotti 2006). A beta index below 1 indicates a sparse network, whereas values approaching or exceeding 1 indicate a higher level of connectivity.

Gamma index ( \( \gamma \) ): It compares the actual number of links in a network to the theoretical maximum number of possible links (Mondragón 2020; Waples and Gaggiotti 2006). It

also ranges from 0 to 1, where 1 represents a fully connected network (though such networks are rare in practice), and a value of 0 indicates a completely disconnected network with no links between nodes.

#### METHODS

The methods for calculating connectivity indices rely on specific mathematical formulas.

The alpha index is calculated using the following formula (Cichocki and Amari 2010; Millsap and Hartog 1988; Mondragón 2020; Oyebisi et al. 2025; Waples and Gaggiotti 2006):

\[
\alpha = (e - v + 1) / (2 v - 5)
\]

where e represents the number of edges, and v represents the number of vertices.

The beta index follows the following formula (Cichocki and Amari 2010; Millsap and Hartog 1988; Mondragón 2020; Oyebisi et al. 2025; Waples and Gaggiotti 2006):

\[
\beta = e / v
\]

It determines the level of connectivity based on the ratio of links to nodes.

The gamma index is given by

\[
\gamma = e / (3 (v - 2))
\]

which evaluates the connectivity of a network by comparing the actual number of links to the maximum number of possible links (Cichocki and Amari 2010; Millsap and Hartog 1988; Mondragón 2020; Oyebisi et al. 2025; Waples and Gaggiotti 2006).

Additionally, the grid-tree pattern is often used to classify network connectivity structures, particularly in hierarchical urban layouts (Cichocki and Amari 2010; Millsap and Hartog 1988; Mondragón 2020; Oyebisi et al. 2025; Waples and Gaggiotti 2006). The grid-tree pattern typically ranges from 0 to 1, where values closer to 0 indicate a tree-like structure characterized by hierarchical branching, limited alternative paths, and low redundancy, whereas values closer to 1 represent a grid-like structure with high connectivity.

\[
\mathrm{GTP} = (\mathrm{e} - \mathrm{v} + 1) / (\sqrt {\mathrm{v}} - 1) ^ {2}
\]

The connectivity of an urban road network can be analyzed using graph-theoretical indices such as alpha, beta, and gamma.

#### LIMITATIONS

Despite their usefulness, these indices have certain limitations. They assume an idealized network structure, often ignoring real-world complexities such as road hierarchies or one-way streets. In some urban environments, excessive connectivity may lead to increased infrastructure costs without significantly

WORKING PAPER

July 2026

9

improving mobility. These indices are also primarily designed for at-grade networks and may not accurately represent grade-separated roads or multilevel transport systems, such as highways with overpasses or underpasses. These metrics also perform poorly in complex geometries such as rotaries, and nonstandard intersections with more than four edges, where the actual path distance often deviates significantly from simplified node-link representations. Additionally, these indicators are most effective for intracity comparisons, such as evaluating one pocket or neighborhood of a city against another. At the citywide scale, the degree of connectivity tends to average out and well-connected areas can offset poorly connected ones, making it difficult to draw meaningful comparisons between different cities.

## RS 4: Tortuosity ratio

### DEFINITION

The tortuosity ratio is a key metric in road network analysis that is used to assess the degree of curvature or winding of a road or route (Cefalo et al. 2024). It is defined as the ratio of the actual traveled length of a road segment to the shortest straight-line distance between its starting and ending points (Cao et al. 2019). A tortuosity value of 1 indicates a perfectly straight road, whereas values greater than 1 signify increasing levels of curvature. This measure is particularly useful in evaluating road geometry, because it highlights deviations from the shortest possible route and provides insights into the structural design of transportation networks (Cao et al. 2019; Cefalo et al. 2024).

### METHODS

The calculation of the tortuosity ratio follows a simple mathematical formula:

$$\text{Tortuosity ratio} = (\text{Actual length of road (L)}) / (\text{Straight line distance (D)})$$

This ratio provides insight into the geometric structure of the road network. A value of 1 indicates a completely straight and direct route, whereas values greater than 1 suggest detours, bends, or indirect connections between points. Lower tortuosity ratios are generally associated with better accessibility and more efficient road layouts.

The tortuosity ratio can be calculated using ArcGIS or QGIS. In QGIS, the actual length of each road segment can be obtained directly from the geometry of the road layer, and the straight-line distance can be calculated using the Point to Point Distance or Geometry by Expression tools. The resulting ratio can be computed using the Field Calculator by dividing the road length by the straight-line distance between the start and end points of each segment.

### LIMITATIONS

Despite its usefulness, the tortuosity ratio has certain limitations. It provides a simplistic representation of road characteristics, focusing solely on geometry without accounting for factors such as road functionality, design speeds, or traffic conditions, which are essential for comprehensive network analysis. The measure is also scale dependent, because different levels of data resolution can influence the perceived level of curvature; small-scale maps may oversimplify road geometry, whereas high-resolution data may exaggerate minor bends. Additionally, classifying roads based on tortuosity values could be subjective, because the thresholds for defining “high” or “low” tortuosity vary across different regions and applications (Cao et al. 2019). This metric is most effective when integrated with other indicators, such as road width, safety measures, and connectivity indices, to provide a more complete assessment of the efficiency of a transportation network.

## RS 5: Road hierarchy

### DEFINITION

Road hierarchy is a system used to classify roads according to their function and importance within an urban transport network (Marshall and Garrick 2010; Vishnu et al. 2023; Zhang et al. 2015). According to IRC:SP:118-2018 (*Manual for Planning and Development of Urban Roads and Streets*), urban roads are classified into urban expressways, arterial roads, sub-arterial roads, collector streets, local streets, and nonmotorized transport (NMT) streets and greenways. Arterial roads serve as major conduits for high-speed, long-distance travel by channeling large traffic volumes, and collector roads act as intermediaries, connecting local roads to arterials and distributing traffic. Local roads primarily provide direct access to residences and businesses and support slower travel speeds. This hierarchical structuring balances the dual purposes of mobility and accessibility (Albers et al. 2012; Xie and Levinson 2007). Road hierarchy affects travel speeds because higher-order roads are designed for faster travel with fewer interruptions, whereas lower-order roads prioritize access and slower speeds.

### METHODS

GIS-based mapping methods are extensively used to analyze and visualize road hierarchy within urban networks. These methods involve collecting spatial data layers that include road attributes such as functional classification, speed limits, lane counts, traffic volume, and access control. Using GIS software, roads can be categorized into hierarchical classes by applying predefined criteria or multi-criteria decision analysis that incorporates several road features. Network analysis tools within GIS further help evaluate how each road functions within the larger transport network by examining

10 | WRI INDIA

Assessing urban road networks using geospatial metrics

connectivity, shortest paths, and traffic distribution patterns. The spatial representation of road hierarchy enables planners to identify connectivity gaps, analyze travel speeds across different road classes, and plan interventions to enhance last-mile connectivity effectively. By overlaying other GIS datasets such as land use or population density, the analysis can be contextualized to prioritize road improvements in high-demand areas.

### LIMITATIONS

Despite its usefulness, road hierarchy as an indicator has some limitations. In complex or rapidly urbanizing areas—especially in informal or unplanned settlements, which are common in Indian cities—roads may serve mixed functions that the hierarchy cannot fully represent. GIS-based mapping and analysis require accurate, detailed, and up-to-date spatial and traffic data; any deficiencies in data quality, availability, or resolution can limit the reliability of hierarchical classification and connectivity assessments.

### RS 6: Travel distance

#### DEFINITION

The travel distance refers to the distance that can be traveled from a specific point while following the existing road network factors (Ballou et al. 2002; Jenelius 2009; Wang et al. 2020). The total travel distance is measured in a straight line from the starting point. In areas with a meandering road network, where roads are not straight, the straight-line travel distance is shorter than that of areas with a more direct and structured road network, where the travel distance is higher (Boeing and Riggs 2024). Traffic congestion and flow are not typically considered in the calculation, because it is based purely on the road network structure.

The maximum travel distance is the farthest possible distance that can be covered in a specific direction within a given time frame (Boeing 2022; Shanmugasundaram et al. 2019). It depends on the straightness and connectivity of the road network—more direct roads result in a higher maximum travel distance.

The average travel distance is the average of the travel distances covered in all directions. It reflects the overall multidirectional connectivity of a location. Areas with more diagonal and well-connected road networks tend to have a higher average travel distance, because travel potential is distributed across multiple directions (Ballou et al. 2002; Xie and Levinson 2007).

Typically, the travel distance is measured using a standard travel speed of 30 kilometers per hour (km/h) and a time frame of 15 minutes.

### METHODS

The travel distance is usually measured using a standard travel speed and a fixed time frame to assess the extent of accessibility from a given point. In this study, a travel speed of 30 km/h and a time duration of 15 minutes were used to evaluate how far one can travel within that period based solely on the connectivity of the road network.

### LIMITATIONS

The theoretical travel distance assumes ideal conditions without accounting for real-world factors such as traffic congestion, stoplights, or detours, making it less reliable in practice. Travel distances can fluctuate over time due to external factors such as weather, construction, and peak-hour congestion, affecting the precision of accessibility analysis.

### RS 7: Road connectivity ratio

#### DEFINITION

The road connectivity ratio (RCR) measures the extent of road network accessibility within a defined area (Soczówka et al. 2020; Sreelekha et al. 2016). It is calculated by comparing the total length of roads that can be covered within a 15-minute travel distance at 30 km/h to the total road length within a 7.5 km radius. A higher RCR value indicates better connectivity, meaning the road network is well-developed and efficiently linked. The maximum possible connectivity is represented by an RCR of 1, whereas lower values indicate poor connectivity, with the RCR often approaching 0 in areas with sparse or fragmented road networks.

### METHODS

The RCR is a metric used to evaluate the accessibility and efficiency of a road network by measuring how much of the network can be reached within a specified travel time. It is calculated using the following formula:

\[
\begin{array}{r l} \text { RCR } & = (\text { Total   length   of   roads   within   a   30   km / h   service   area }) / \\ & (\text { Total   road   length   within   a   7.5   km   radius }) \end{array}
\]

This equation quantifies road network connectivity by comparing the length of accessible roads within a 15-minute travel distance (at 30 km/h) to the total road length within a 7.5 km circular area. A higher RCR value indicates better connectivity, whereas a lower value suggests limited road access and poor connectivity.

The RCR can be calculated using ArcGIS or QGIS through a combination of service area analysis and spatial queries. In QGIS, the Service Area can be generated using the QNEAT3 plug-in or through the Iso-Area (from Layer) tool, which models the reachable area within 15 minutes of travel time at a speed of 30 km/h. Once the service area is delineated, the total length of roads within this polygon can be calculated

WORKING PAPER | July 2026

11

by intersecting it with the road network and summing the lengths using the Field Calculator. Similarly, a 7.5 km circular buffer can be generated around the same origin point, and the total road length within this buffer is computed.

In ArcGIS, a similar approach is used with the Network Analyst extension to create the service area polygon based on time and speed parameters. Road lengths within the service area and buffer are calculated using the Intersect and Summary Statistics tools. This method provides a standardized way to evaluate the relative accessibility of different locations based on the structure and reach of the road network.

# LIMITATIONS

Although the RCR serves as a useful indicator for assessing the efficiency of urban transport networks, it has several limitations. The accuracy of the RCR largely depends on the completeness and quality of the GIS road network data used for analysis. Inaccurate or incomplete datasets can lead to misleading interpretations of connectivity.

# RS 8: Self-loop proportion

# DEFINITION

In the context of road network topology, the self-loop proportion (SLP) is the ratio of self-loops to the total number of edges in a network. A self-loop occurs when a road segment begins and ends at the same node without intervening junctions. A high SLP signifies a reduction in network permeability.

# METHODS

The SLP is calculated by analyzing the adjacency characteristics of a directed or undirected graph. The process involves identifying edges where the starting node ID equals the ending node ID.

$$L_{t} = e_{a} / E$$

where $L_{t} = \text{SLP}$; $e_{a} =$ the count of edges where the road segment begins and ends at the same node; E = total number of edges in the network.

# LIMITATIONS

The SLP is limited by its sensitivity to map simplification, where inconsistent data processing can fail to register physical loops as single topological edges. It also suffers from functional ambiguity, treating small cul-de-sacs and large roundabouts identically without accounting for their physical size or traffic purpose.

# Barrier Blocks (BB)

# BB 1: Area of closed block

# DEFINITION

The area of a closed block refers to the spatial extent of a polygon completely enclosed by intersecting road segments (Gülgen and Gökgöz 2011). These polygons represent individual urban blocks, bounded by roads on all sides.

# METHOD

The area of each closed urban block is calculated by converting the road network into polygons and measuring the area enclosed by each block. This helps identify the spatial size and distribution of blocks within the network (Li et al. 2025; Zeng et al. 2019). Larger blocks typically indicate poorer connectivity, as they represent larger areas without internal connections, whereas smaller blocks are generally associated with better connectivity. However, extremely small or irregular blocks may suggest fragmentation or weak connectivity in the urban fabric.

# LIMITATIONS

This metric captures only physical enclosures, not functional connectivity. It may fail to reflect true accessibility in cases where blocks are interrupted by pedestrian-only paths or underpasses.

# BB 2: Node to block ratio

# DEFINITION

The node-to-block ratio is calculated by dividing the total number of nodes (road intersections and dead ends) by the number of closed blocks in the road network. It measures how many connection points exist per urban block (Gülgen and Gökgöz 2011; Xie and Levinson 2007; Zeng et al. 2019).

# METHOD

The node-to-block ratio is calculated by dividing the number of road network nodes (intersections and endpoints) by the number of closed blocks (Yang et al. 2018; Zeng et al. 2019). This ratio reflects the connectivity density of the road system. A higher ratio implies a well-connected network with more intersections per block, whereas a lower ratio may indicate sparse connectivity or excessive block amalgamation. It helps assess the efficiency and navigability of the urban road layout.

# LIMITATIONS

This ratio provides a quantitative–not qualitative–measure. It does not consider the functional hierarchy of roads (e.g., highways versus local roads), nor does it account for pedestrian-only access points. A high ratio could also result from overly fragmented networks that do not necessarily improve navigability.

12

[LOGO]

WRI INDIA

Assessing urban road networks using geospatial metrics

### Traffic Flow (TF)

#### TF 1: Travel time

##### DEFINITION

The travel time refers to the duration required to traverse a specific route between two points within a transportation network (Albers et al. 2012; Frank et al. 2008; Vuk et al. 2016; Xie and Levinson 2007). In the context of this study, the travel time focuses on transit travel time, specifically for transit-route design. Depending on the type of network–automobile roadways or transit systems such as rail–the term may encompass various factors such as congestion levels, transit schedules, and transfer times.

##### METHOD

To collect and analyze travel time data, GIS tools and the Google Travel Distance API are employed. The data collection process includes origin–destination coordinates for identifying key points within the transit network, travel distance and duration for measuring the length of the route and estimated travel time, duration in traffic–when applicable–to account for variations due to congestion or real-time conditions, and query timestamp to capture time-dependent variations for temporal analysis. These tools allow for accurate measurement of travel times, facilitating effective transit planning and optimization.

##### LIMITATIONS

Although GIS tools and the Google Travel Distance API provide valuable insights, they are subject to certain limitations. Data accuracy may be influenced by unexpected factors such as accidents, weather conditions, or infrastructure disruptions. Transit variations can affect calculations, because travel time estimates may not always reflect real-world events such as delays, missed transfers, or schedule deviations.

#### TF 2: Velocity statistics

##### DEFINITION

The velocity statistics indicator refers to the collection and analysis of speed data across a transportation network. These data provide insights into traffic conditions, congestion levels, and travel efficiency (Akbar et al. 2018; Albers et al. 2012; Jabari 2016; Xie and Levinson 2007; Yang et al. 2018). Velocity statistics are calculated based on travel time data collected through the Google Maps API.

##### METHODS

The Google API is also used to gather real-time speed data. Several parameters are utilized to assess congestion, such as travel delay, the travel time index, travel rate, the travel rate index, and the speed reduction index. As an illustration of this data application, Figure F-12 and Appendix G present

the velocity statistics for 20 Indian cities, calculated using the BEST_GUESS traffic model from the Google Routes API.

For traffic speed prediction, advanced machine learning models such as auto-regression methods, support vector regression, and artificial neural networks are employed. The enhanced Recurrent Convolutional Neural Network (eRCNN) approach is utilized to model spatiotemporal interactions of traffic speeds among road segments. To improve prediction accuracy, separate error-feedback neurons are introduced in the recurrent layer of eRCNN to capture abrupt changes in traffic speeds caused by peak hours and accidents (Wang et al. 2016; Xu et al. 2025).

Segments of roads are clustered using a Pearson-correlation-coefficient-based algorithm to group contiguous segments with similar traffic patterns. This clustering approach enables knowledge transfer between segments and enhances prediction accuracy. Additionally, model parameters are fine-tuned using local spatiotemporal data, dividing 24-hour periods into eight time ranges to account for different traffic conditions throughout the day.

Also, the mean ratio of traffic velocity statistics is commonly used in research to assess traffic conditions by comparing peak-hour speeds to non-peak-hour speeds (Wang et al. 2018). This ratio is calculated as follows:

\[
\text { Mean   ratio } = (\text { Peak - hour   speed }) / (\text { Non - peak - hour   speed })
\]

where the peak-hour speed is often measured at around 7 PM and the non-peak-hour speed at around 3 AM (Lelke and Friedrich 2025). A higher value of this ratio indicates better traffic conditions during peak hours because it suggests that peak-hour speeds are closer to free-flow non-peak-hour speeds, signifying lower congestion levels.

##### LIMITATIONS

Although velocity statistics provide valuable insights, there are limitations to consider. Data accuracy may be affected by GPS errors, signal interference, and unexpected traffic events. Traditional traffic models struggle with abrupt changes in speed, requiring advanced neural network architectures such as eRCNN to improve prediction performance. Additionally, Google provides velocity statistics across all modes of transport (not just for four-wheelers or two-wheelers) and also includes freight vehicles such as trucks and truck trailers, which typically travel at much lower speeds.

#### TF 3: Peakedness

##### DEFINITION

Peakedness, or traffic flow, refers to the movement of vehicles along a roadway or transportation network. It is a critical

geospatial indicator influencing road network connectivity and travel speed (Akbar et al. 2018; Cooper et al. 2021).

WORKING PAPER | July 2026

13

Traffic flow is typically measured in terms of traffic volume, which is the number of vehicles passing a specific point within a given time frame; traffic density, which represents the number of vehicles present per unit length of a roadway; and traffic speed, which varies with congestion levels and road conditions (Gülgen and Gökgöz 2011; Honda and Horiguchi 2000). Traffic flow analysis is essential for designing road infrastructure, optimizing signal timings, and managing congestion effectively.

## METHODS

Data for traffic flow analysis are collected using GPS-enabled devices, the Google API, and traffic monitoring systems. Traffic flow models describe vehicle flows using three basic parameters: average speed (v) in km/h, density (k) in the number of vehicles/km, and flow (q) in the number of vehicles/h:

\[
\mathbf {q} = \mathbf {k v}
\]

### LIMITATIONS

Despite its significance, analyzing peakedness involves challenges. The accuracy of traffic flow data can be impacted by signal interferences, weather conditions, and sensor limitations. Traditional models often struggle with abrupt changes in traffic speeds due to accidents or peak hours, requiring advanced machine learning techniques for accurate predictions.

### Directional Patterns (D)

#### D 1: Directional differences

### DEFINITION

The directional differences indicator refers to variations in traffic flow, congestion levels, and travel speeds between opposite directions on a given roadway or transportation network (Boeing and Riggs 2024; Honda and Horiguchi 2000). These differences arise due to factors such as peak-hour demand, road infrastructure, signal timing, and land-use patterns. Understanding directional differences helps improve road network design, optimize traffic signal control, and enhance overall transportation efficiency.

### METHODS

Directional differences are measured using real-time traffic data collected from GPS devices, traffic sensors, and the Google API. Methods such as directional volume-to-capacity ratio calculations, speed variation analysis, and congestion index calculations are used to assess disparities in traffic conditions across opposing travel directions. GIS and machine learning models help visualize and predict directional traffic trends for improved road planning.

### LIMITATIONS

The accuracy of directional difference analysis can be affected by external factors such as roadwork, accidents, and weather conditions. Short-term fluctuations in traffic patterns may require continuous data collection for reliable insights.

#### D 2: Entropy

### DEFINITION

Entropy, in the context of road network analysis, is a quantitative measure of uncertainty, disorder, or randomness in the distribution of elements within a network (Boeing 2019b). It reflects the diversity in route choices, traffic flows, or the structure of the network itself. A higher entropy value indicates a more complex and unpredictable system, whereas a lower entropy value suggests a more ordered and predictable configuration.

### METHOD

Several methods exist for assessing entropy in road networks. Shannon's entropy is commonly used to measure the randomness in the distribution of links, nodes, or travel paths. Topological entropy examines how uniformly connections are distributed among the nodes of the network. Path entropy quantifies the diversity and number of possible paths between nodes, reflecting route options available to travelers. Flow-based entropy involves analyzing how traffic flows are distributed across the links in the network. The fundamental entropy formula applied is

\[
\mathrm{H} = - \sum_ {i = 1} ^ {n} \mathrm{p} _ {i} \ln (\mathrm{p} _ {i})
\]

where H = entropy value, n = number of categories (e.g., modes, destinations, time periods),  \( p_{i} \)  = proportion of trips, flow, or activity in category i,  \( \Sigma p_{i}=1 \) .

### LIMITATIONS

Despite its usefulness, entropy analysis in road networks has limitations. Comprehensive and up-to-date data are required for accurate results, which are not always obtainable. Interpreting entropy values can be challenging because different types of entropy metrics may lead to conflicting conclusions.

## Data management

The systematic literature review helped to not only identify the indicators but also formulate a structured workflow for data management. This workflow ensured accurate processing, standardization, calculation, and storage of data associated with the identified indicators. The workflow consists of three

14

[Non-Text]

WRI INDIA

Assessing urban road networks using geospatial metrics

key steps designed to accommodate the unique requirements of India's transportation network while leveraging global geospatial datasets for benchmarking and trend analysis.

### Step 1: Defining the administrative and functional boundaries

The first step is to define the geographical boundaries of the analysis to ensure dataset consistency and enable comparisons across cities. Each urban area is divided into two levels: the Overall Area of Interest (the full municipality or metropolitan region) for intercity comparisons and Subareas (such as wards or districts) for detailed, localized assessments of transport patterns and network performance.

Where available, official administrative boundaries from government sources are used; otherwise, global datasets such as geoBoundaries or OpenStreetMap (OSM) serve as alternatives.

### Step 2: Extracting transportation-specific geospatial data layers

After defining the boundaries, geospatial datasets related to transportation connectivity and performance are extracted to form the foundation for computing indicators and analyzing network efficiency. To ensure comprehensive coverage, data include information on road networks, traffic flow, nodal connections, and spatial attributes sourced from satellite imagery, GPS data, traffic monitoring systems, and open repositories.

To maintain organization and compatibility, datasets are structured using predefined schemas: raster data (e.g., satellite imagery, heatmaps) can be stored in GeoTIFF format, and vector data (e.g., roads, intersections) can be stored in GeoJSON format. Metadata for each dataset can be documented in JSON format, capturing sources, extraction methods, and preprocessing details.

### Step 3: Indicator calculation and final data processing

The final step is to compute transportation indicators using the extracted geospatial data through spatial statistical analysis for each defined zone. Techniques such as weighted reduction on platforms such as ArcGIS Pro and QGIS ensure accuracy by accounting for spatial dependencies and network topology. Indicators such as nodal connectivity, segment quality, and traffic performance are calculated using standardized methods to maintain consistency across areas.

The computed indicator values are then aggregated at the zonal level.

## Significance of identified indicators

This section outlines the relevance of the selected geospatial indicators and the overall data management approach. Based on the identified indicators, Appendix E summarizes the significance of each indicator in analyzing travel speeds and road network connectivity while also emphasizing their implications for active travel modes such as walking and cycling. Additionally, stakeholder consultations were conducted to assess the applicability and contextual relevance of these indicators within Indian cities.

To evaluate the relevance and applicability of the selected indicators within India's urban context, stakeholder consultations were conducted with a diverse group of experts. The participants included 7 professors from leading national institutes, 12 internal experts from WRI India, and 11 urban and transport planners currently engaged with ULBs across various Indian cities.

The academic experts emphasized that incorporating indicators such as dead-end proportion, dead-end clustering pattern analysis, and the grid-tree classification approach greatly enhances the contextual relevance of the indicator set, particularly for analyzing organically developed urban areas. They stressed that the interpretation of road network metrics must be context specific, because their implications vary depending on a city's planning typology. For instance, although a higher number of nodes often suggests better connectivity and improved access to public transport, this may not hold true in planned cities, where numerous nodes result from design patterns rather than from genuine access points. Conversely, in unplanned or organically developed areas, a higher node count tends to represent genuine route diversity.

The experts also pointed out that the degree of connectivity (alpha, beta, and gamma indices) is an effective indicator to differentiate between grid-based and radial layouts, and circuitry further quantifies the resulting routing inefficiencies. In many urban contexts, cities are undergoing a gradual shift, growing more radial over time as historical cores expand outward through the addition of peripheral ring roads and major arterial spokes designed to facilitate rapid suburban-to-center commuting. This transition is often driven by land-use changes where agricultural or peri-urban land is converted into residential hubs, necessitating new radial connections that bypass congested older grids. Hence, in the Indian context, the road connectivity index is important to understand these changes. The experts also highlighted the need to account for a city's economic category (High-Performing, Aspirational, Transitional, or Declining) \( ^{1} \) and tier classification, because indicator performance and relevance can differ widely. What works well for Tier-II \( ^{2} \) or Tier-III cities may not apply to

WORKING PAPER | July 2026

15

Tier-I cities with denser populations and heavier traffic loads. The internal WRI India experts agreed on the usefulness of the indicators but cautioned that interpretation should always be grounded in the local context, given variations in density, planning history, and travel behavior. They noted that similar travel speed measurements could imply very different mobility conditions across central, suburban, or peripheral zones. They also warned against overreliance on aggregated averages, which could obscure the challenges faced by vulnerable groups such as women, children, and older adults.

Experts from ULBs acknowledged the strong potential of the identified indicators for assessing road network quality and travel efficiency but pointed out key challenges related to data availability, integration, and operationalization. They noted that existing datasets are often fragmented, inconsistent, and stored in isolated systems, making comprehensive analysis difficult. The experts called for real-time, high-resolution data to enable timelier and evidence-based decisions. They also cautioned against the uniform application of indicators across diverse cities without contextual adjustments and underscored the need for standardized benchmarks and comparative best practices to guide local improvements. Across all three expert groups, there was broad consensus that the indicator framework is robust, comprehensive, and well suited to assessing road network connectivity and travel speeds in Indian cities.

## Application of indicators to assess efficiency of urban road networks

This section presents case studies demonstrating how the identified indicators can be applied to assess road connectivity and the efficiency of urban networks. Using Bengaluru as the study area, Figure 4 illustrates how the selected indicators, such as the RCR, can effectively evaluate levels of urban connectivity. The detailed insets show that areas with more structured road layouts, such as Basavanagudi, tend to have higher connectivity ratios, whereas neighborhoods with organic or unplanned layouts, such as Whitefield, display lower connectivity.

Similarly, Figure 5 illustrates the maximum distance that can be traveled within 15 minutes from different locations in the city, serving as a proxy for road network connectivity. The larger spatial extent of green areas in Ahmedabad indicates that a greater portion of the city than Bengaluru and Hyderabad can be accessed within this fixed travel-time threshold, reflecting stronger network connectivity. This visualization also helps identify specific urban pockets with limited secondary network links (red patches), enabling more targeted interventions to improve the overall road network structure.

Figure 4 | Bengaluru: Ward-wise road connectivity ratio (the enlargement highlights variations in road layout)

![img-4.jpeg](img-4.jpeg)

Source: WRI India Authors.

16

[LOGO]

WRI INDIA

Assessing urban road networks using geospatial metrics

Figure 5 | Maximum travel distance of Ahmedabad, Bengaluru and Hyderabad

![img-5.jpeg](img-5.jpeg)

Ahmedabad

![img-6.jpeg](img-6.jpeg)

Bengaluru

![img-7.jpeg](img-7.jpeg)

Hyderabad

Maximum distance (in m) traveled in 15 minutes

![img-8.jpeg](img-8.jpeg)

Source: WRI India Authors.

Figure 6 illustrates the ward-wise distribution of dead-end proportions in Bengaluru, with red shading indicating wards that have a higher concentration of dead ends. This visualization helps identify areas with limited road connectivity, highlighting zones that may require targeted planning and infrastructure interventions.

Figure 7 depicts the variation in travel speeds along Bellary Road (shown in green), revealing a substantial difference of 34 km/h between peak and non-peak hours. The map also highlights that Thanisandra Main Road (shown in pink) runs parallel to Bellary Road but lacks significant connecting routes between the two roads. Consequently, commuters depend

heavily on Bellary Road during peak hours, resulting in severe congestion along this corridor.

To illustrate how these indicators vary across different urban contexts, maps and results for 20 Indian cities—encompassing Tier-I and Tier-II cities (Figure 8)—are provided in Appendix F. Figure 8 presents velocity statistics using the mean ratio, defined as the ratio between peak-hour speeds and non-peak-hour speeds. This mean ratio reflects the speed difference between peak and non-peak periods, indicating the extent of speed reduction that occurs during peak hours (Appendix G).

WORKING PAPER | July 2026

17

Figure 6 | Bengaluru: Ward-wise distribution of dead-end proportion

![img-9.jpeg](img-9.jpeg)

# Dead-End Street Proportion

Very Low (> 1.5 SD below mean)
Low (1 to 1.5 SD below mean)
Below Average (0.5 to 1 SD below mean)
Slightly Below Average (0 to 0.5 SD below mean)
Slightly Above Average (0 to 0.5 SD above mean)
Above Average (0.5 to 1 SD above mean)
High (1 to 1.5 SD above mean)
Very High (≥ 1.5 SD above mean)

Mean = 0.25

Median = 0.26

SD = 0.05

![img-10.jpeg](img-10.jpeg)

Source: WRI India Authors.

Figure 7 | Road Network and Travel Speed of Bellary Road (Green line in figure A)

Observations made at 15-minute intervals on 6 August 2024

![img-11.jpeg](img-11.jpeg)

(A)

![img-12.jpeg](img-12.jpeg)

(B)

Source: WRI India Authors.

18

WRI INDIA

Assessing urban road networks using geospatial metrics

Figure 8 | Ratio of peak-hour (7 pm) to non-peak-hour (3 am) travel speeds across twenty selected Indian cities

![img-13.jpeg](img-13.jpeg)

Legend

![img-14.jpeg](img-14.jpeg)

Map created using Traffic Data from Google Maps Platform (2026); Travel times estimated using the Google Routes API under Optimistic (Free-flow) and Pessimistic (Peak-hour) scenarios. Disclaimer: This map is for illustrative purpose and does not imply the expression of any opinion on the part of WRI India concerning the legal status of any country or territory or concerning the delimitation of frontiers or boundaries.

Source: WRI India Authors.

WORKING PAPER | July 2026

19

## Conclusion

This working paper identified the key geospatial indicators that influence road network connectivity and travel speeds in Indian cities by using a hybrid methodology that integrates a PRISMA-guided systematic literature review, bibliometric analysis, and expert consultations. The key findings of this research are summarized as follows:

- The systematic literature review identified 21 key geospatial indicators influencing road network connectivity and travel speed.
- The bibliometric analysis revealed key research trends in this domain and identified five major thematic areas, enabling the classification of indicators into five broad categories.
- Each identified indicator was explained in depth, including its conceptual basis, relevance, and analytical significance.
- Expert consultations validated the relevance and applicability of the identified indicators in the Indian urban context and improved the analysis and interpretation of results.
- The study demonstrated the practical application of these indicators in assessing the efficiency of urban road networks, using illustrative examples from Indian cities.

Building on these findings, future research could develop a composite index using the identified indicators to rank

cities based on an overall road network connectivity score. In addition, future studies could investigate the relationship between road network characteristics based on the identified indicators and environmental outcomes such as carbon emissions, thereby supporting emission reduction strategies and India's climate goals.

This study focused only on geospatial indicators for assessing road network connectivity. A significant avenue for future research lies in transitioning from purely geometric, two-dimensional analysis to dynamic, spatiotemporal connectivity modeling. Future work should explore how connectivity indicators fluctuate across different time scales.

Several qualitative and operational factors, such as signal cycle times, road surface quality, one-way traffic regulations, temporary or permanent road closures, trip experience, traffic management practices, and enforcement levels, also significantly influence road network performance and travel speeds; however, these factors were not considered in the present analysis. By integrating temporal flow data with network topology, future frameworks can bridge the gap between abstract GIS representations and the lived reality of urban transport. This approach would highlight how “effective connectivity” is not just a factor of road geometry but is a dynamic state that changes with traffic loads and management practices.

20

[LOGO]

WRI INDIA

Assessing urban road networks using geospatial metrics

## Appendices

### Appendix A: PRISMA Methodology

For the systematic literature review, we utilized the Web of Science and Scopus databases. An initial search was conducted in Scopus using the term "Urban-street network connectivity." The 10 most cited articles in this research domain were identified (see Appendix B). Based on the research questions and the most frequently used keywords in these highly cited articles, we developed a search string. In the literature related to road network connectivity and travel speeds, many synonymous terms—such as road network, road connectivity, street network, and network connectivity—are used extensively. Furthermore, the term network connectivity appears in various scientific disciplines beyond transportation planning, including health psychology, social network studies, material science, and supply chain management. To ensure specificity to transportation and urban planning, relevant terms were incorporated into the search string. The final search query was: "(street OR road OR transport OR transit) AND (network OR connectivity) AND (urban* OR urban morphology OR urban planning OR GIS OR geography OR geo-spatial)". This search identified 446 documents and was limited to English-language publications from the last 10 years (2014–2025). To ensure quality,

only articles published in journals with a CiteScore greater than 1 were considered. Key bibliographic details—including title, abstract, keywords, authors' names and affiliations, journal name, and year of publication—were exported to an MS Excel spreadsheet (Biswas et al. 2024; Pahlevan-Sharif et al. 2019). The search query was executed using the TITLE-ABS-KEY function in both Scopus and Web of Science databases between January 9 and January 30, 2025. The screening process was carried out in multiple stages. First, a title and abstract screening eliminated 232 articles that were not relevant to the research questions. A subsequent full-text review excluded an additional 86 studies. Next, 6 studies were included through snowball. Finally, 134 articles were selected for inclusion in this systematic literature review. The screening process followed methodologies used in previous literature reviews (Billore and Anisimova 2021; Paul and Rosado-Serrano 2019; Sharma et al. 2022; Södergren 2021).

The systematic literature review also helped us understand the data management workflow, ensuring standardized, spatially consistent processing of geospatial indicators for Indian urban transport networks (Boeing 2021a; Mackres et al. 2025).

WORKING PAPER | July 2026

21

## Appendix B: Most cited articles

Table B-1 | The 10 most cited articles

|  PAPER TITLE | AUTHORS | JOURNAL | YEAR | CITATIONS  |
| --- | --- | --- | --- | --- |
|  Influences of Built Environments on Walking and Cycling: Lessons from Bogotá | Cervero, Robert; Sarmiento, Olga L.; Jacoby, Enrique; Gomez, Luis Fernando; Neiman, Andrea | International Journal of Sustainable Transportation | 2009 | 638  |
|  The Network Analysis of Urban Streets: A Primal Approach | Porta, Sergio; Crucitti, Paolo; Latora, Vito | Environment and Planning B: Planning and Design | 2006 | 609  |
|  Designing the Walkable City | Southworth, Michael | Journal of Urban Planning and Development | 2005 | 607  |
|  Topological Analysis of Urban Street Networks | Jiang Bin; Claramunt, Christophe | Environment and Planning B: Planning and Design | 2004 | 463  |
|  VANET Routing on City Roads using Real-Time Vehicular Traffic Information | Nzouonta, Josiane; Rajgure, Neeraj; Wang, Guiling; Borcea, Cristian | IEEE Transactions on Vehicular Technology | 2009 | 417  |
|  A Topological Pattern of Urban Street Networks: Universality and Peculiarity | Jiang Bin | Physica A: Statistical Mechanics and its Applications | 2007 | 254  |
|  School Site and the Potential to Walk to School: The Impact of Street Connectivity and Traffic Exposure in School Neighborhoods | Giles-Corti, Billie; Wood, Gina; Pikora, Terri; Learnihan, Vincent; Bulsara, Max; Van Niel, Kimberly; Timperio, Anna; McCormack, Gavin; Villanueva, Karen | Health and Place | 2011 | 248  |
|  A Structural Approach to the Model Generalization of an Urban Street Network | Jiang Bin; Claramunt, Christophe | GeoInformatica | 2004 | 238  |
|  Resilient Urban Forms: A Review of Literature on Streets and Street Networks | Sharifi, Ayyoob | Building and Environment | 2019 | 201  |
|  Developing an Enhanced Weight-Based Topological Map-Matching Algorithm for Intelligent Transport Systems | Velaga, Nagendra R.; Quddus, Mohammed A.; Bristow, Abigail L. | Transportation Research Part C: Emerging Technologies | 2009 | 191  |

Source: WRI India Authors.

22 | WRI INDIA

Assessing urban road networks using geospatial metrics

## Appendix C: Bibliometric analysis

Table C-1 | Keyword clusters from the bibliometric analysis

|  GROUP NAME | KEYWORDS  |
| --- | --- |
|  Group 1 (Green) | Average Travel Speeds, Congestion Frequency Index, Transport Performance in Grid versus Radial Layout, Modal Split Ratios, Accessibility to Employment Centers, Freight Route Performance, Automated Traffic Flow Index, Origin-Destination Travel Cost, Travel Time Reliability Index, Mobility-as-a-Service (MaaS) Access, GIA Travel Speeds Calibration, Estimation of Origin-Destination, Adaptive Neuro-Fuzzy Inference, Machine Learning, Commute Disruption by Cultural Precincts, Route Choice Index, Traffic Impact in Tourism Zones, Speed Variability Score, Response Time to Incidents, Traffic Flow Efficiency, Peak versus Off-Peak Travel Times, Adaptive Signal Performance Index, Peakedness, Peak Hour Travel Efficiency, Travel Delay in Historic Districts, Level of Service (LOS), Numerical Model, Congestion Delay Index, Google Traffic API Data, Network-Wide Delay Estimation, Google API Commute Time Analysis, Route Delay Statistics, Accessibility to Urban Centers, Color Features, Adversarial Machine Learning, Real-Time Congestion Data, Emotional Experience, Commute Time Index, Travel Time Estimation using GPS Data, Planned City Commute Consistency, Dynamic Traffic Assignment Score, Delay Per Kilometer, Navigation App Delay Reporting, Traffic Saturation Index, Travel Time Decay Function, Adaptive Neuro-Fuzzy Inference, Multimodal Accessibility Score, Average Delay at Intersections, Traffic Heatmap Score, Public Transport Accessibility Score, Urban Form versus Travel Time Study, Urban Mobility Score, Vehicle Accessibility in Gated Zones, Vehicle-Kilometer Traveled (VKT), Velocity Statistics  |
|  Group 2 (Red) | Compass-Based Connectivity Score, Directional Bias in European Old Towns, Mean Directional Bias, Analytical Framework, Directional Symmetry in Colonial Layouts, Case Studies, Sectoral Accessibility Score, Local Indicator of Spatial Association (LISA), Direction-Based Accessibility Gradient, Directional Skewness, Artificial Neural Network, Grid Orientation Consistency, Connectivity by Directional Cluster, United Kingdom, Urban Orientation in Coastal Cities, Traditional Urban Fabric Directional Flow, Visual Directional Continuity, Seoul, Axial Line Orientation in Historic Cores, Slope-Aware Accessibility, Sector-Based Directional Access Mapping, Lanzhou, Grassland, Road Orientation Histogram, Data Fusion, Google Earth Street Orientation Extraction, Radial Accessibility Index, East-West versus North-South Ratio, Urban Grain Directionality, Directional Legibility in Planned Cities, Cultural Grid Direction Influence, 15-Minute City, Spatial Autocorrelation (Moran's I), Directional Entropy, Directional Differences, Polar Orientation Index, River Valley, Spatial Distribution, Axial Angular Change by Neighborhood Type, Orientation Variability across Urban Typologies, Centrifugal Connectivity Index, Spatial Bias in Road Layout  |
|  Group 3 (Purple) | 4-Way Intersection Proportion, Angular Connectivity, Autocorrelation, Average Angular Change at Nodes, Average Connections Per Node, Average Link Length Per Node, Average Node Degree, Central Node Proportion, China, Connected Nodes Per Hectare, Critical Junction Count, Crossroad Density, Dead-End Proportion, Degree Distribution Skewness, Degree of Accessibility, Gated Community Entry Points, GIS-Based Nodal Mapping, Google API Intersection Count, High-Frequency Node Network, Historical Junction Morphology, Intersection Density, Intersection Hierarchy in Planned Cities, Junction Proximity Index, Lanzhou, Local Node Accessibility, Minimum Path Nodes, Network Intersection Spacing, Nodal Connectivity Index, Nodal Flow Capacity, Nodal Network Redundancy, Node Alignment in European Towns, Node Angle Extremities, Node Betweenness Centrality, Node Degree Centrality, Node Evolution in Heritage Areas, Node Spacing Entropy, Node Spacing Regularity, Node to Length Ratio, Organic Street Pattern Nodes, Proportion of Cul-De-Sacs, Proximity to Intersections, Regular Gridness Index, River Valley, Segment-Level GIA Output, Spatial Distribution of Dead-End Clusters, Street Node Integration, T-Junction Ratio, Urban Nodal Cluster Detection, Urban Renewal Impact on Node Density  |
|  Group 4 (Yellow) | Self-loop Proportion, Average Segment Straightness, Remote Sensing of Street Layout, Segment Diversity Index, Average Circuit, Segment Redundancy Factor, Road Density Index, Segment Accessibility per Block, Axial Segment Analysis, Right-of-Way Consistency, Road Segment Hierarchy, Shortest Path Index, Beta Index, Average Street Width, Average Segment Length, Historic Pathways, Segment Redesign Impact Assessment, Segment Hierarchy in Colonial Towns, Street Length Regularity in Grid Cities, Edge Continuity Score, Route Factor (Tortuosity Ratio), Mean Segment Directional Change, Urban Grain Coarseness, Google Maps Segment Length Comparison, Road Length Per Capita, Pavement Continuity Score, Segment Integration Score, Built-Up to Segment Ratio, Street Grid Irregularity Index, Travel Distance, Segment Fragmentation Index, Segment Angle Variation, Shimbel Distance, Segment-Level Centrality, Segment-Level Betweenness, Average Segment Tortuosity, Weighted Segment Accessibility, Linear Density of Roads, Segment-Level GIA Output, Planned versus Organic Segment Pattern, Gamma Index, Travel Distance to Road Density Ratio, Pedestrian Street Inclusion, Grid Spacing Consistency, Computer Software Selection Analysis  |
|  Group 5 (Blue) | Block-Level Integration Score, Number of Barrier Edges, Local Accessibility, Visual Permeability of Blocks, Node-to-Block Ratio, Inward-Facing Block Proportion, Number of Isolated Blocks, Physical Barriers in Planned Communities, Barrier Block Identification Index, Closed Block Density, Block Inaccessibility Score, Average Block Size, Block Orientation Consistency, Spatial Segregation Index, Street Canyon Block Influence, Canada, Spatial Analysis, Old Precincts, Obesity, Spatial Discontinuity in Redeveloped Areas, Heritage Block Enclosure Score, Accessibility, Ratio of Accessible to Total Blocks, Impenetrable Block Clusters, Block Perimeter-Area Ratio, Network Detour Factor Per Block, Urban Enclave Detection, Number of Impassable Barriers, Environment characteristic, Block Area Variation, Block Boundary Complexity, Block Elongation Index, Morphological Block Clustering, Urban Block Fragmentation Index, Road Barriers Per Block, Area of Closed Blocks (Statistics), Perimeter-to-Road Access Ratio, Block Size Inequality Index, Block Inaccessibility in Historic Centers, Block Compactness, Natural versus Artificial Block Barriers, Block-Level Permeability, Connectivity, Built Environment, Urban Planning, Fair, Architecture  |

Source: WRI India Authors.

WORKING PAPER | July 2026

23

## Appendix D: Systematic literature review highlights

Table D-1 | Key findings from the systematic literature review

|  SOURCE | INDICATORS | METHODOLOGY | OBJECTIVE  |
| --- | --- | --- | --- |
|  (Albalawneh & Mohamed, 2024) | Travel time, travel distance, travel distance to road density index ratio, road connectivity ratio (RCR) | Federated genetic algorithm integrated with ArcGIS Network Analyst and geographic information system (GIS) tools | Developed a route planning tool using ArcGIS Network Analyst to enhance both cost and service quality measures, taking into account several factors to determine the best route based on the users' preferences  |
|  (Xie and Levinson 2007) | Node-to-length ratio, node angle extremities, average connections per node, degree of connectivity (alpha, beta, gamma) | Review and enhancement of spatial network analysis using proposed structural measures applied to 16 test networks derived from 4 idealized base networks (90°, 45°, 30°, fully connected) | Quantitatively evaluate, compare, and describe road network structures; support urban planning and transportation design through analysis of network quality and structural evolution from a traveler's perspective  |
|  (C. Liu et al. 2022) | Velocity statistics, peakedness, travel distance, directional differences, node-to-block ratio | Multi-index evaluation using Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS), Principal Component Analysis (PCA), and network theory | Identify, classify, and prioritize critical nodes in urban road networks to improve emergency response, resilience, and operational reliability under normal and crisis conditions  |
|  (Wright et al. 2017) | Travel time, travel distance, RCR, Shim-bel distance | Macroscopic traffic modeling with node and link models; use of split ratios, demand/supply functions, and high-dimensional node representations for simulation; support for Integrated Corridor Management (ICM)/Decision Support Systems (DSS) using ensemble-based and real-time evaluation | Simulate and evaluate traffic behavior in complex urban networks; manage real-time traffic operations efficiently in ICM and DSS through scalable, accurate modeling  |
|  (Yu et al. 2021) | Average circuitry, spatial distribution of dead-end clusters, self-loop proportion, directional differences | Spatiotemporal node selection optimization using a greedy algorithm based on utility maximization; evaluates both network topology and real-time traffic dynamics | Improve Urban Traffic Mobile Crowd Sensing (MCS) efficiency by selecting optimal sensing nodes, reducing redundancy, and ensuring sufficient coverage while considering dynamic traffic conditions and resource constraints  |
|  (Ahmadzai et al., 2019) | Degree of connectivity (alpha, beta, gamma), area of closed blocks, dead-end proportion, node-to-block ratio | Integrated Graph of Natural Road Network (IGNRN) using weighted graphs and centrality metrics (applied via GIS); includes primal and dual comparisons, and evaluation using Kandahar city road data | Assess and model urban road networks using spatial graph theory to identify critical nodes and links, enabling planners to evaluate connectivity, efficiency, and vulnerability in support of sustainable urban transport development  |
|  (Jabari 2016) | Travel time, Shimbel distance, dead-end proportion, tortuosity ratio | First-order link models coupled with general node models; includes supply-demand constraints, mass-balance, flow-maximization, holding-free conditions, invariance principle, and conflict-aware flow allocation based on signal control | Develop robust and realistic models of urban traffic flow that resolve congestion propagation at intersections by enforcing physical constraints and invariance, ensuring correct direction of information propagation and computational efficiency  |
|  (Ballou et al. 2002) | Average circuitry, travel distance, travel-distance-to-road-density-index ratio | Empirical estimation of circuitry factors by comparing actual road travel distances with great circle distances across multiple countries using geospatial data, road atlases, and regression models for fitting distance functions | Improve accuracy of travel distance estimation in logistics applications (e.g., facility location, supply chain design) by accounting for road network meandering and regional variability using practical distance estimating functions and circuitry adjustments  |

24

[Non-Text]

WRI INDIA

Assessing urban road networks using geospatial metrics

|  SOURCE | INDICATORS | METHODOLOGY | OBJECTIVE  |
| --- | --- | --- | --- |
|  (Wang et al. 2020) | Road Connectivity Ratio (RCR), Area of Closed Blocks, Travel Distance to Road Density Index Ratio, Degree of Connectivity (Alpha, Beta, Gamma) | Empirical analysis using case cities in China, comparing travel costs in simplified and real-world network structures; examining effects of network densification and expansion on vehicle movement and transport performance | Assess how road network density and configuration affect motor vehicle travel efficiency and overall transport performance in urban areas, highlighting planning trade-offs between accessibility, congestion, and liveability  |
|  (Sirmatel et al. 2021) | Vehicle Accumulation (proxy for Travel Time), Shimbel Distance, Directional Differences, Node to Block Ratio | The methodology involves developing a multi-region M-model that integrates a speed-based MFD with the average remaining travel distance while incorporating boundary queues to maintain consistency between accumulation and distance. Model parameters are calibrated through system identification, and the model is validated using simulations on both hypothetical networks and real-world data from Barcelona | The objective is to enhance perimeter control performance by more accurately capturing spatial heterogeneity and trip-based traffic dynamics, while offering a computationally efficient alternative to traditional trip-based models and enabling scalable traffic state estimation and control  |

Source: WRI India Authors.

WORKING PAPER | July 2026

25

## Appendix E: Significance of identified indicators

Table E-1 | Significance of identified indicators

|  INDICATOR NAME | IMPORTANCE FOR PUBLIC TRANSPORT | RELEVANCE FOR ACTIVE TRAVEL | INDICATOR SCALE | SOURCE(S)  |
| --- | --- | --- | --- | --- |
|  Node-to-length ratio | Indicates network density influencing route options and efficiency. | Higher ratio indicates more intersections per unit length, supporting connectivity and shorter walking routes. | City Level Indicator | (Jabari 2016; Yu et al. 2021)  |
|  Average connections per node | Reflects intersection connectivity enhancing route diversity and network fluidity. | More connections typically improve route options and accessibility for pedestrians and cyclists. | Kernel Level Indicator | (Jabari 2016; Yu et al. 2021)  |
|  Node angle extremities | Captures sharpness of turns affecting ease and smoothness of movement. | Influences walkability by affecting ease and safety of movement; smoother angles favor active travel. | Kernel Level Indicator | (Debnath 2022; Martín et al. 2021; X. Wang et al. 2013; Wright et al. 2017)  |
|  Dead-end proportion | Measures isolated segments that limit route choices and reduce permeability. | High dead-end proportion reduces route choices, limiting walkability and active travel routes. Cul-de-sacs (a form of dead end) can enhance walkability if pedestrian/cyclist paths connect beyond the dead end. | Kernel Level Indicator | (Krishna 2024; Mukherjee 2012; Pandey and Ven-kataraman 2014)  |
|  Spatial distribution of dead-end clusters | Shows clustering of dead ends that create isolated network pockets. | Clusters of dead ends without pedestrian links reduce permeability, but connected clusters can form walkable neighborhoods. | Kernel Level Indicator | (Anirudh et al. 2022; Gadepalli 2016; Kor-zhenevych and Jain 2018; Krishna 2024; Pitale et al. 2025)  |
|  Shimbel distance | Quantifies route indirectness indicating inefficiencies and longer distances. | Longer Shimbel distances indicate less direct routes, reducing walking/cycling efficiency. | Kernel Level Indicator | (Boeing 2019b, 2021a, 2022; Rivera-Royero et al. 2022; Taylor et al. 2006; Zhang et al. 2015)  |
|  Average circuitry | Reflects detour severity compared to direct distance, indicating route out-of-directness. | Higher circuitry means less direct paths, negatively affecting active travel. | City Level/Ward-Level Indicator | (Z. Liu et al. 2022; Soczówka et al. 2020; Wang et al. 2015)  |
|  Degree of connectivity (alpha, beta, gamma, grid-tree pattern) | Demonstrates network complexity and availability of route options. | Higher connectivity indices support better walkability and multiple active travel route options. | City Level Indicator | (Jabari 2016; Rivera-Royero et al. 2022)  |
|  Tortuosity ratio | Shows windingness of routes; more direct paths aid quicker movement. | Less tortuosity supports easier navigation and more direct active travel routes. | Kernel Level Indicator | (Z. Liu et al. 2022; Soczówka et al. 2020; Wang et al. 2015)  |
|  Road Hierarchy | Defines roads by capacity and function, enabling efficient public transport on arterial roads and supporting access via collector roads for last-mile connectivity. It helps manage traffic flow, improving transit speeds and reliability. | Separates high-speed traffic from local streets, creating safer, low-traffic routes for walking and cycling. It enhances connectivity and access to transit for active travel modes. | City Level Indicator | (Soczówka et al. 2020; Taylor et al. 2006; Wang et al. 2020; Wright et al. 2017)  |

26

[Non-Text]

WRI INDIA

Assessing urban road networks using geospatial metrics

|  INDICATOR NAME | IMPORTANCE FOR PUBLIC TRANSPORT | RELEVANCE FOR ACTIVE TRAVEL | INDICATOR SCALE | SOURCE(S)  |
| --- | --- | --- | --- | --- |
|  Travel distance | Measures trip length influencing duration and user effort. | Shorter travel distances generally favor walking and cycling over motorized travel. | Origin-Destination Indicator | (Albers et al. 2012; Marzolf et al. 2006; Sanghera and Satybaldieva 2020; Vishnu et al. 2023; Wang et al. 2020)  |
|  Road connectivity ratio | Captures proportion of roads facilitating through movement and permeability. | Higher RCR improves network permeability for pedestrians and cyclists. | Kernel Level Indicator | (Berrigan et al. 2010; Boeing 2019a, 2020; Boeing et al. 2022)  |
|  Travel-distance-to-road-connectivity ratio | Balances network compactness and accessibility to optimize routing efficiency. | Optimal ratios indicate accessible yet navigable networks supporting active travel. | City Level Indicator | (Boeing 2021a, 2022; Porta et al. 2009)  |
|  Self-loop proportion | Reflects redundant loops that may reduce route efficiency. | Lower self-loop proportion favors more useful travel paths for walking and cycling. | Kernel Level Indicator | (Debnath 2022; Krishna 2024; Mukherjee 2012)  |
|  Area of closed blocks | Smaller block sizes indicate fine-grained networks enhancing accessibility and route choices. | Smaller closed blocks correlate with finer-grain street networks supporting walkability. | Kernel Level Indicator | (Bansal and Sen 2022; Debnath 2022; Deore and Lathia 2019)  |
|  Node to block ratio | High ratios imply dense intersections, increasing route options and network quality. | Higher values indicate more intersections per block, facilitating active travel. | Kernel Level Indicator | (Jabari 2016; Yu et al. 2021)  |
|  Travel time | Directly reflects network efficiency by measuring duration to traverse segments. | Shorter travel times enhance walkability and promote active travel. | Origin-Destination Indicator | (Bhat 1998; Boeing 2022; Frank et al. 2008; Wu and Hong 2022)  |
|  Velocity Statistics | Summarizes typical travel speeds indicating operational quality. | Lower speeds generally favor walking and cycling safety. | City Level Indicator | (Boeing 2022; Jain et al. 2022; Jenelius 2009; Wright et al. 2017)  |
|  Peakedness | Reveals variability in flow or congestion affecting reliability. | Stable, less peaky conditions support consistent active travel ease. | Kernel Level Indicator | (Z. Liu et al. 2022; Wang et al. 2020; Zhou 2015)  |
|  Directional differences | Indicates complexity and orientation diversity influencing navigation ease. | High directional variety relates to network complexity impacting route choice for active travel. | City Level Indicator | (Albers et al. 2012; Boeing 2019b; Jabari 2016)  |
|  Entropy | Measures randomness in layout impacting predictability and legibility. | Moderate entropy balances legibility and network richness; very high entropy may degrade walkability due to confusion. | City Level Indicator | (Boeing 2019b; Jabari 2016; Sirmatel et al. 2021; Wright et al. 2017)  |

Source: WRI India Authors.

WORKING PAPER

July 2026

27

## Appendix F: Results from 20 Indian Cities

Figure F-1 | Node-to-length ratio (Number of nodes / Total length of road network)

![img-15.jpeg](img-15.jpeg)

NOTE: Cities are sorted in descending order based on population size.

Source: WRI India Authors.

28 | WRI INDIA

Assessing urban road networks using geospatial metrics

Figure F-2 | Intersection Density

![img-16.jpeg](img-16.jpeg)

Delhi

![img-17.jpeg](img-17.jpeg)

Ahmedabad

![img-18.jpeg](img-18.jpeg)

Bengaluru

![img-19.jpeg](img-19.jpeg)

Coimbatore

![img-20.jpeg](img-20.jpeg)

Hyderabad

![img-21.jpeg](img-21.jpeg)

Kochi

![img-22.jpeg](img-22.jpeg)

Kolkata

![img-23.jpeg](img-23.jpeg)

Kozhikode

![img-24.jpeg](img-24.jpeg)

Mumbai

![img-25.jpeg](img-25.jpeg)

Bhopal

Intersection density is a measure of urban street network connectivity, expressed as the number of road intersections (nodes) per square kilometre, where higher values indicate a more finely gridded, walkable street network and lower values suggest a sparse, vehicle-dependent layout.

### Legend

Number of intersections per sq. km

![img-26.jpeg](img-26.jpeg)

Map drawn at

50km Radius 30km Radius 20km Radius

Classification of cities

Tier 1 ▲ Tier 2

WORKING PAPER

July 2026

29

Figure F-2 | Intersection Density (cont.)

![img-27.jpeg](img-27.jpeg)

Chennai

![img-28.jpeg](img-28.jpeg)

▲ Indore

![img-29.jpeg](img-29.jpeg)

Jaipur

![img-30.jpeg](img-30.jpeg)

Kanpur

![img-31.jpeg](img-31.jpeg)

Lucknow

![img-32.jpeg](img-32.jpeg)

▲ Nagpur

![img-33.jpeg](img-33.jpeg)

▲ Patna

![img-34.jpeg](img-34.jpeg)

Pune

![img-35.jpeg](img-35.jpeg)

▲ Surat

![img-36.jpeg](img-36.jpeg)

▲ Thrissur

Intersection density is a measure of urban street network connectivity, expressed as the number of road intersections (nodes) per square kilometre, where higher values indicate a more finely gridded, walkable street network and lower values suggest a sparse, vehicle-dependent layout.

### Legend

Number of intersections per sq. km

![img-37.jpeg](img-37.jpeg)

Map drawn at

50km Radius 30km Radius 20km Radius

Classification of cities

Tier 1 ▲ Tier 2

Source: WRI India Authors.

30

[Non-Text]

WRI INDIA

Assessing urban road networks using geospatial metrics

Figure F-3 | Bengaluru: Ward-wise dead-end proportion

![img-38.jpeg](img-38.jpeg)

Source: WRI India Authors.

# Dead-End Street Proportion

- Very Low (> 1.5 SD below mean)
- Low (1 to 1.5 SD below mean)
- Below Average (0.5 to 1 SD below mean)
- Slightly Below Average (0 to 0.5 SD below mean)
- Slightly Above Average (0 to 0.5 SD above mean)
- Above Average (0.5 to 1 SD above mean)
- High (1 to 1.5 SD above mean)
- Very High (≥ 1.5 SD above mean)

Mean = 0.25

Median = 0.26

SD = 0.05

Figure F-4 | Bengaluru: Ward-wise average circuitry

![img-39.jpeg](img-39.jpeg)

Source: WRI India Authors.

# Average Circuitry

- Very Low (> 1 SD below mean)
- Low (0.5 to 1 SD below mean)
- Moderately Low (0 to 0.5 SD below mean)
- Moderately High (0 to 0.5 SD above mean)
- High (0.5 to 1 SD above mean)
- Very High (> 1 SD above mean)

Mean = 1.03

Median = 1.03

SD = 0.02

WORKING PAPER | July 2026

31

Figure F-5 | Degree of connectivity (alpha, beta, and gamma indices)

![img-40.jpeg](img-40.jpeg)

Gamma Index

Bengaluru

![img-41.jpeg](img-41.jpeg)

Gamma Index

- Very Low (> 1.5 SD below mean)
- Low (1 to 1.5 SD below mean)
- Below Average (0.5 to 1 SD below mean)
- Slightly Below Average (0 to 0.5 SD below mean)
- Slightly Above Average (0 to 0.5 SD above mean)
- Above Average (0.5 to 1 SD above mean)
- High (1 to 1.5 SD above mean)
- Very High (≥ 1.5 SD above mean)

SD = 0.02

Source: WRI India Authors.

32 WRI INDIA

Assessing urban road networks using geospatial metrics

Figure F-6 | Tortuosity ratio

![img-42.jpeg](img-42.jpeg)

![img-43.jpeg](img-43.jpeg)

![img-44.jpeg](img-44.jpeg)

![img-45.jpeg](img-45.jpeg)

![img-46.jpeg](img-46.jpeg)

![img-47.jpeg](img-47.jpeg)

![img-48.jpeg](img-48.jpeg)

![img-49.jpeg](img-49.jpeg)

![img-50.jpeg](img-50.jpeg)

![img-51.jpeg](img-51.jpeg)

### Legend

Tortuosity Ratio

Equal to 1

Greater than 1

Classification of cities

Tier 1

Tier 2

Map drawn at

50km Radius

30km Radius

20km Radius

WORKING PAPER

July 2026

33

Figure F-6 | Tortuosity ratio (cont.)

![img-52.jpeg](img-52.jpeg)

Chennai

![img-53.jpeg](img-53.jpeg)

▲ Indore

![img-54.jpeg](img-54.jpeg)

Jaipur

![img-55.jpeg](img-55.jpeg)

Kanpur

![img-56.jpeg](img-56.jpeg)

Lucknow

![img-57.jpeg](img-57.jpeg)

▲ Nagpur

![img-58.jpeg](img-58.jpeg)

▲ Patna

![img-59.jpeg](img-59.jpeg)

Pune

![img-60.jpeg](img-60.jpeg)

▲ Surat

![img-61.jpeg](img-61.jpeg)

▲ Thrissur

### Legend

Tortuosity Ratio

Equal to 1

Greater than 1

Classification of cities

Tier 1

Tier 2

Map drawn at

50km Radius

30km Radius

20km Radius

Source: WRI India Authors.

34

[Non-Text]

WRI INDIA

Assessing urban road networks using geospatial metrics

Figure F-7 | Road hierarchy

![img-62.jpeg](img-62.jpeg)

Delhi

![img-63.jpeg](img-63.jpeg)

Ahmedabad

![img-64.jpeg](img-64.jpeg)

Bengaluru

![img-65.jpeg](img-65.jpeg)

Coimbatore

![img-66.jpeg](img-66.jpeg)

Hyderabad

![img-67.jpeg](img-67.jpeg)

Kochi

![img-68.jpeg](img-68.jpeg)

Kolkata

![img-69.jpeg](img-69.jpeg)

Kozhikode

![img-70.jpeg](img-70.jpeg)

Mumbai

![img-71.jpeg](img-71.jpeg)

Bhopal

### Legend

Less than 10m Between 10-20m
Between 20-35m More than 35m

### Map drawn at

50km Radius 30km Radius 20km Radius

### Classification of cities

Tier 1 ▲ Tier 2

WORKING PAPER

July 2026

35

Figure F-7 | Road hierarchy (cont.)

![img-72.jpeg](img-72.jpeg)

Chennai

![img-73.jpeg](img-73.jpeg)

▲ Indore

![img-74.jpeg](img-74.jpeg)

Jaipur

![img-75.jpeg](img-75.jpeg)

Kanpur

![img-76.jpeg](img-76.jpeg)

Lucknow

![img-77.jpeg](img-77.jpeg)

▲ Nagpur

![img-78.jpeg](img-78.jpeg)

▲ Patna

![img-79.jpeg](img-79.jpeg)

Pune

![img-80.jpeg](img-80.jpeg)

▲ Surat

![img-81.jpeg](img-81.jpeg)

▲ Thrissur

#### Legend

Less than 10m

Between 10-20m

Between 20-35m

More than 35m

#### Map drawn at

50km Radius

30km Radius

20km Radius

#### Classification of cities

Tier 1

▲ Tier 2

Source: WRI India Authors.

36

[Non-Text]

WRI INDIA

Assessing urban road networks using geospatial metrics

Figure F-8 | Average travel distance

![img-82.jpeg](img-82.jpeg)

Delhi

![img-83.jpeg](img-83.jpeg)

Ahmedabad

![img-84.jpeg](img-84.jpeg)

Bengaluru

![img-85.jpeg](img-85.jpeg)

Coimbatore

![img-86.jpeg](img-86.jpeg)

Hyderabad

![img-87.jpeg](img-87.jpeg)

Kochi

![img-88.jpeg](img-88.jpeg)

Kolkata

![img-89.jpeg](img-89.jpeg)

Kozhikode

![img-90.jpeg](img-90.jpeg)

Mumbai

![img-91.jpeg](img-91.jpeg)

Bhopal

### Legend

Average Distance (in m) travelled in 15 minutes

3,000

7,000

Classification of cities

Tier 1

Tier 2

Waterbodies

Other natural features

No data

Map drawn at

50km Radius

30km Radius

20km Radius

WORKING PAPER

July 2026

37

Figure F-8 | Average travel distance (cont.)

![img-92.jpeg](img-92.jpeg)

Chennai

![img-93.jpeg](img-93.jpeg)

▲ Indore

![img-94.jpeg](img-94.jpeg)

Jaipur

![img-95.jpeg](img-95.jpeg)

Kanpur

![img-96.jpeg](img-96.jpeg)

Lucknow

![img-97.jpeg](img-97.jpeg)

▲ Nagpur

![img-98.jpeg](img-98.jpeg)

▲ Patna

![img-99.jpeg](img-99.jpeg)

Pune

![img-100.jpeg](img-100.jpeg)

▲ Surat

![img-101.jpeg](img-101.jpeg)

▲ Thrissur

### Legend

Average Distance (in m) travelled in 15 minutes

3,000

7,000

Classification of cities

Tier 1

Tier 2

Waterbodies

Other natural features

No data

Map drawn at

50km Radius

30km Radius

20km Radius

Source: WRI India Authors.

38

[Non-Text]

WRI INDIA

Assessing urban road networks using geospatial metrics

Figure F-9 | Maximum travel distance

![img-102.jpeg](img-102.jpeg)

![img-103.jpeg](img-103.jpeg)

![img-104.jpeg](img-104.jpeg)

![img-105.jpeg](img-105.jpeg)

![img-106.jpeg](img-106.jpeg)

![img-107.jpeg](img-107.jpeg)

![img-108.jpeg](img-108.jpeg)

![img-109.jpeg](img-109.jpeg)

![img-110.jpeg](img-110.jpeg)

![img-111.jpeg](img-111.jpeg)

Maximum Distance (in m) travelled in 15 minutes

![img-112.jpeg](img-112.jpeg)

Classification of cities

Tier 1 ▲ Tier 2

Waterbodies Other natural features No data

Map drawn at

50km Radius 30km Radius 20km Radius

WORKING PAPER

July 2026

39

Figure F-9 | Maximum travel distance (cont.)

![img-113.jpeg](img-113.jpeg)

Chennai

![img-114.jpeg](img-114.jpeg)

▲ Indore

![img-115.jpeg](img-115.jpeg)

Jaipur

![img-116.jpeg](img-116.jpeg)

Kanpur

![img-117.jpeg](img-117.jpeg)

Lucknow

![img-118.jpeg](img-118.jpeg)

▲ Nagpur

![img-119.jpeg](img-119.jpeg)

▲ Patna

![img-120.jpeg](img-120.jpeg)

Pune

![img-121.jpeg](img-121.jpeg)

▲ Surat

![img-122.jpeg](img-122.jpeg)

▲ Thrissur

### Legend

Maximum Distance (in m) travelled in 15 minutes

![img-123.jpeg](img-123.jpeg)

Classification of cities

Tier 1

Tier 2

Waterbodies

Other natural features

No data

Map drawn at

50km Radius

30km Radius

20km Radius

Source: WRI India Authors.

40

[Non-Text]

WRI INDIA

Assessing urban road networks using geospatial metrics

Figure F-10 | Road connectivity ratio

![img-124.jpeg](img-124.jpeg)

![img-125.jpeg](img-125.jpeg)

![img-126.jpeg](img-126.jpeg)

![img-127.jpeg](img-127.jpeg)

![img-128.jpeg](img-128.jpeg)

![img-129.jpeg](img-129.jpeg)

![img-130.jpeg](img-130.jpeg)

![img-131.jpeg](img-131.jpeg)

![img-132.jpeg](img-132.jpeg)

![img-133.jpeg](img-133.jpeg)

![img-134.jpeg](img-134.jpeg)

Tier 1 ▲ Tier 2

Waterbodies Other natural features No data

Map drawn at
50km Radius 30km Radius 20km Radius

WORKING PAPER | July 2026

41

Figure F-10 | Road connectivity ratio (cont.)

![img-135.jpeg](img-135.jpeg)

Chennai

![img-136.jpeg](img-136.jpeg)

▲ Indore

![img-137.jpeg](img-137.jpeg)

Jaipur

![img-138.jpeg](img-138.jpeg)

Kanpur

![img-139.jpeg](img-139.jpeg)

Lucknow

![img-140.jpeg](img-140.jpeg)

▲ Nagpur

![img-141.jpeg](img-141.jpeg)

▲ Patna

![img-142.jpeg](img-142.jpeg)

Pune

![img-143.jpeg](img-143.jpeg)

▲ Surat

![img-144.jpeg](img-144.jpeg)

▲ Thrissur

### Legend

Road Connectivity Ratio

![img-145.jpeg](img-145.jpeg)

Classification of cities

Tier 1 ▲ Tier 2

Waterbodies □ Other natural features □ No data

Map drawn at

50km Radius 30km Radius 20km Radius

Source: WRI India Authors.

42

[Non-Text]

WRI INDIA

Assessing urban road networks using geospatial metrics

Figure F-11 | Bengaluru: Ward-wise area of closed blocks

![img-146.jpeg](img-146.jpeg)

Source: WRI India Authors.

#### Area of Closed Blocks (in hectares)

Very Low (>1 SD below mean)
Low (0.5 to 1 SD below mean)
Moderately Low (0 to 0.5 SD below mean)
Moderately High (0 to 0.5 SD above mean)
High (0.5 to 1 SD above mean)
Very High (> 1 SD above mean)

Mean = 0.57

Median = 0.51

SD = 0.26

Figure F-12 | Velocity statistics

![img-147.jpeg](img-147.jpeg)

NOTE: Cities are sorted in descending order based on population size.

Source: Google Maps Platform (Traffic Data) 2021, WRI India Authors; Travel times estimated using the Google Routes API under Optimistic (Free-flow) and Pessimistic (Peak-hour) scenarios

WORKING PAPER

July 2026

43

Figure F-13 | Entropy

![img-148.jpeg](img-148.jpeg)

![img-149.jpeg](img-149.jpeg)

![img-150.jpeg](img-150.jpeg)

![img-151.jpeg](img-151.jpeg)

![img-152.jpeg](img-152.jpeg)

![img-153.jpeg](img-153.jpeg)

![img-154.jpeg](img-154.jpeg)

![img-155.jpeg](img-155.jpeg)

![img-156.jpeg](img-156.jpeg)

![img-157.jpeg](img-157.jpeg)

![img-158.jpeg](img-158.jpeg)

![img-159.jpeg](img-159.jpeg)

![img-160.jpeg](img-160.jpeg)

![img-161.jpeg](img-161.jpeg)

![img-162.jpeg](img-162.jpeg)

![img-163.jpeg](img-163.jpeg)

![img-164.jpeg](img-164.jpeg)

![img-165.jpeg](img-165.jpeg)

![img-166.jpeg](img-166.jpeg)

![img-167.jpeg](img-167.jpeg)

Source: WRI India Authors.

Classification of cities

Tier 1 ▲ Tier 2

44

[Non-Text]

WRI INDIA

Assessing urban road networks using geospatial metrics

## Appendix G: Velocity statistics of selected 20 Indian cities

Table G-1 | Velocity statistics (Mean Ratio)

|  CITIES | MEAN SPEED (7 PM) | MEAN SPEED (3 AM) | RATIO OF PEAK-HOUR (7 PM) TO NON-PEAK-HOUR (3 AM) TRAVEL SPEEDS  |
| --- | --- | --- | --- |
|  Bengaluru | 13 | 38 | 0.34  |
|  Chennai | 12 | 34 | 0.35  |
|  Pune | 13 | 36 | 0.36  |
|  Jaipur | 14 | 38 | 0.37  |
|  Hyderabad | 15 | 40 | 0.38  |
|  Mumbai | 15 | 40 | 0.38  |
|  Kolkata | 11 | 29 | 0.38  |
|  Kochi | 13 | 34 | 0.38  |
|  Indore | 12 | 31 | 0.39  |
|  Delhi | 19 | 46 | 0.41  |
|  Lucknow | 15 | 36 | 0.42  |
|  Nagpur | 14 | 33 | 0.42  |
|  Patna | 13 | 30 | 0.43  |
|  Coimbatore | 14 | 32 | 0.44  |
|  Ahmedabad | 15 | 34 | 0.44  |
|  Kanpur | 14 | 31 | 0.45  |
|  Bhopal | 15 | 32 | 0.47  |
|  Surat | 15 | 32 | 0.47  |
|  Kozhikode | 16 | 33 | 0.48  |
|  Thrissur | 18 | 33 | 0.55  |

Source: WRI India Authors.

WORKING PAPER

July 2026

45

## Abbreviations

|  **API** | Application Programming Interface | **NMT** | Nonmotorized Transport  |
| --- | --- | --- | --- |
|  **BB** | Barrier Blocks | **OSM** | OpenStreetMap  |
|  **DSS** | Decision Support System | **PBI** | Performance-Based Indicators  |
|  **GIA** | Global Information Aggregation | **PCA** | Principal Component Analysis  |
|  **GIS** | Geographic Information System | **PRISMA** | Preferred Reporting Items for Systematic Reviews and Meta-Analyses  |
|  **GPS** | Global Positioning System | **RCR** | Road Connectivity Ratio  |
|  **GTFS** | General Transit Feed Specification | **RS** | Road Segments  |
|  **ICM** | Integrated Corridor Management | **TITLE-ABS-KEY** | Title, Abstract, and Keyword  |
|  **IRC** | Indian Roads Congress | **TOPSIS** | Technique for Order Preference by Similarity to Ideal Solution  |
|  **LISA** | Local Indicator of Spatial Association | **ULB** | Urban Local Body  |
|  **LOS** | Level of Service | **VKT** | Vehicle Kilometers Traveled  |
|  **MaaS** | Mobility-as-a-Service | **WRI** | World Resources Institute  |
|  **MFD** | Macroscopic Fundamental Diagram |  |   |
|  **NC** | Nodal Connection |  |   |

46 | WRI INDIA

Assessing urban road networks using geospatial metrics

## Endnotes

1. These economic categories (High Performing, Aspirational, Transitional, and Declining) refer to a classification framework used to assess urban growth trajectories and economic vitality. For a detailed breakdown of the criteria used for these designations, see Katekar and Deshmukh (2024) and Mohammad et al. (2025).

2. Indian cities are classified into tiers based mainly on population size, economic development, and infrastructure (Biswas et al. 2025b; RBI 2012). Tier-I cities have populations over 1 million and are the most developed, including metros such as Mumbai and Delhi. Tier-II cities have populations between 200,000 and 1 million, showing moderate growth and infrastructure. Tier-III cities are smaller, with populations between 50,000 and 200,000. They are emerging urban centers and are generally less developed.

## References

Ahmadzai, F., K.M.L. Rao, and S. Ulfat. 2019. "Assessment and Modelling of Urban Road Networks Using Integrated Graph of Natural Road Network (a GIS-Based Approach)." Journal of Urban Management 8 (1): 109–125. https://doi.org/10.1016/j.jum.2018.11.001.

Akbar, M., R. Khan, M.T. Khan, B. Alam, M. Elahi, B., Wali, and A.A. Shah. 2018. "Methodology for Simulating Heterogeneous Traffic Flow at Intercity Roads in Developing Countries: A Case Study of University Road in Peshawar." Arabian Journal for Science and Engineering 43 (4): 2021–36. https://doi.org/10.1007/s13369-017-2860-0.

Albalawneh, D.A., and M.A. Mohamed. 2024. "A New Federated Genetic Algorithm-Based Optimization Technique for Multi-Criteria Vehicle Route Planning using ArcGIS Network Analyst." International Journal of Pervasive Computing and Communications 20 (2): 206–27. https://doi.org/10.1108/ijpcc-02-2022-0082.

Albers, H.J., A.W. Ando, M. Bu, and M.G. Wing. 2012. "Road-Network Agglomeration, Road Density, and Protected-Area Fragmentation." Letters in Spatial and Resource Sciences 5 (3): 137–50. https://doi.org/10.1007/s12076-012-0078-z.

Anirudh, B., T.N. Mazumder, and A. Das. 2022. "Examining Effects of City's Size and Regional Context on Vehicle Ownership Levels in the Indian Context." Transportation Research Part D: Transport and Environment 108: 103279. https://doi.org/10.1016/j.trd.2022.103279.

Arif, M., and K. Gupta. 2020. "Spatial Development Planning in Peri-Urban Space of Burdwan City, West Bengal, India: Statutory Infrastructure as Mediating Factors." SN Applied Sciences 2: 1779. https://doi.org/10.1007/s42452-020-03587-0.

Arora, S., and P. Gargava. 2023. "E-Mobility: Hindrances and Motivators for Policies Implementation in India." Case Studies on Transport Policy 11: 100955. https://doi.org/10.1016/j.cstp.2023.100955.

Ballou, R.H., H., Rahardja, and N. Sakai. 2002. "Selected Country Circuitry Factors for Road Travel Distance Estimation." Transportation Research Part A: Policy and Practice 36 (9): 843–48. https://doi.org/10.1016/s0965-8564(01)00044-1.

Bansal, S., and J. Sen. 2022. "Network Assessment of Tier-II Indian Cities' Airports in Terms of Type, Accessibility, and Connectivity." Transport Policy 124: 221–32. https://doi.org/10.1016/J.TRANPOL.2021.05.009.

Barton, H., M. Horswell, and P. Millar. 2012. "Neighbourhood Accessibility and Active Travel." Planning Practice & Research 27 (2): 177–201. https://doi.org/10.1080/02697459.2012.661636.

Berrigan, D., L.W. Pickle, and J. Dill. 2010. "Associations between Street Connectivity and Active Transportation." International Journal of Health Geographics 9 (1): 1–18. https://doi.org/10.1186/1476-072x-9-20.

Bhat, C.R. 1998. "Analysis of Travel Mode and Departure Time Choice for Urban Shopping Trips." Transportation Research Part B: Methodological 32 (6): 361–71. https://doi.org/10.1016/s0191-2615(98)00004-6.

Billore, S., and T. Anisimova. 2021. "Panic Buying Research: A Systematic Literature Review and Future Research Agenda." International Journal of Consumer Studies 45 (4): 777–804. https://doi.org/10.1111/ijcs.12669.

WORKING PAPER | July 2026

47

Biswas, A., and S. Chattopadhyay. 2024. "What Makes Neighbourhood-Level Commercial Centres Attractive for Neighbourhood Residents?" *Regional Studies, Regional Science* 11 (1): 291–310. https://doi.org/10.1080/21681376.2024.2334057.

Biswas, A., S. Chattopadhyay, and H. Banerji. 2025a. "A Comparative Analysis of Commercial Centres at Neighbourhood Level in Traditional and Planned Indian Cities." In *Urban Planning and Design for Megacities in the Global South*, edited by M.C. Feroz, B. Dahiya, L.P. Rajendran, L.K. Dashora, and U. Chatterjee, 165–89. Singapore: Springer. https://doi.org/10.1007/978-981-97-8370-0_8.

Biswas, A., P. Samanta, and S. Chattopadhyay. 2025b. "What Drives Change? Factors Influencing Business Shifts in Neighborhood-Level Commercial Centers." *Papers in Applied Geography* 12 (1): 69–90. https://doi.org/10.1080/23754931.2025.2489371.

Biswas, A., S. Chattopadhyay, P. Barai, and P. Samanta. 2024. "Understanding the Relationship between in-Store and Online Shopping Channel Choice Behaviour of Customers: A Systematic Literature Review." *Cogent Business and Management* 11 (1): 2402510. https://doi.org/10.1080/23311975.2024.2402510.

Boeing, G. 2017. "OSMnx: A Python Package to Work with Graph-Theoretic OpenStreetMap Street Networks." *The Journal of Open Source Software* 2 (12): 215. https://doi.org/10.21105/joss.00215.

Boeing, G. 2019a. "Street Network Models and Measures for Every U.S. City, County, Urbanized Area, Census Tract, and Zillow-Defined Neighborhood." *Urban Science* 3 (1). https://doi.org/10.3390/urbansci3010028.

Boeing, G. 2019b. "Urban Spatial Order: Street Network Orientation, Configuration, and Entropy." *Applied Network Science* 4: 67. https://doi.org/10.1007/s41109-019-0189-1.

Boeing, G. 2020. "A Multi-Scale Analysis of 27,000 Urban Street Networks: Every US City, Town, Urbanized Area, and Zillow Neighborhood." *Environment and Planning B: Urban Analytics and City Science* 47 (4): 590–608. https://doi.org/10.1177/2399808318784595.

Boeing, G. 2021a. "Off the Grid ... and Back Again?: The Recent Evolution of American Street Network Planning and Design." *Journal of the American Planning Association* 87 (1): 123–37. https://doi.org/10.1080/01944363.2020.1819382.

Boeing, G. 2021b. "Spatial Information and the Legibility of Urban Form: Big Data in Urban Morphology." *International Journal of Information Management* 56: 102013. https://doi.org/10.1016/j.ijinfomgt.2019.09.009.

Boeing, G. 2022. "Street Network Models and Indicators for Every Urban Area in the World." *Geographical Analysis* 54 (3): 519–35. https://doi.org/10.1111/gean.12281.

Boeing, G. 2025. "Modeling and Analyzing Urban Networks and Amenities with OSMnx." *Geographical Analysis* 57 (4): 567–77. https://doi.org/10.1111/gean.70009.

Boeing, G., and W. Riggs. 2024. "Converting One-Way Streets to Two-Way Streets to Improve Transportation Network Efficiency and Reduce Vehicle Distance Traveled." *Journal of Planning Education and Research* 44 (3): 1670–78. https://doi.org/10.1177/0739456x221106334.

Boeing, G., C. Higgs, S. Liu, B. Giles-Corti, J.F. Sallis, E. Cerin, M. Lowe, et al. 2022. "Using Open Data and Open-Source Software to Develop Spatial Indicators of Urban Design and Transport Features for Achieving Healthy and Sustainable Cities." *The Lancet Global Health* 10 (6): e907–e918. https://doi.org/10.1016/S2214-109x(22)00072-9.

Cao, T., L. Zhang, G. Sun, C. Wang, Y. Zhang, N. Yan, and A. Xu. 2019. "Model for Predicting the Tortuosity of Transport Paths in Cement-Based Materials." *Materials* 12 (21): 3623. https://doi.org/10.3390/ma12213623.

Cefalo, R., T. Sluga, G. Ossich, and R. Roberti. 2024. "Assessment of Design Consistency for Two-Lane Rural Highways with Low Tortuosity Alignment." *Sustainability* 16 (3): 987. https://doi.org/10.3390/su16030987.

Cervero, R., O.L. Sarmiento, E. Jacoby, L.F. Gomez, and A. Neiman. 2009. "Influences of Built Environments on Walking and Cycling: Lessons from Bogotá." *International Journal of Sustainable Transportation* 3 (4): 203–26. https://doi.org/10.1080/15568310802178314.

Cichocki, A., and S. Amari. 2010. "Families of Alpha-Beta- and Gamma-Divergences: Flexible and Robust Measures of Similarities." *Entropy* 12 (6): 1532–68. https://doi.org/10.3390/e12061532.

Cooper, C.H.V., I. Harvey, S. Orford, and A.J.F. Chiaradia. 2021. "Using Multiple Hybrid Spatial Design Network Analysis to Predict Longitudinal Effect of a Major City Centre Redevelopment on Pedestrian Flows." *Transportation* 48 (2): 643–72. https://doi.org/10.1007/s11116-019-10072-0.

Cruise, S.M., R.F. Hunter, F. Kee, M. Donnelly, G. Ellis, and M.A. Tully. 2017. "A Comparison of Road- and Footpath-Based Walkability Indices and Their Associations with Active Travel." *Journal of Transport & Health* 6: 119–27. https://doi.org/10.1016/j.jth.2017.05.364.

Das, D., A.K. Ojha, H. Kramsapi, P.P. Baruah, and M.K. Dutta. 2019. "Road Network Analysis of Guwahati City Using GIS." *SN Applied Sciences* 1 (8): 1–11. https://doi.org/10.1007/s42452-019-0907-4.

Debnath, P. 2022. "A QGIS-Based Road Network Analysis for Sustainable Road Network Infrastructure: An Application to the Cachar District in Assam, India." *Infrastructures* 7 (9): 114. https://doi.org/10.3390/infrastructures7090114.

Deore, P., and S. Lathia. 2019. "Streets as Public Spaces: Lessons from Street Vending in Ahmedabad, India." *Urban Planning* 4 (2): 138–53. https://doi.org/10.17645/up.v4i2.2058.

Dhingra, M., M.K. Singh, and S. Chattopadhyay. 2017. "Macro Level Characterization of Historic Urban Landscape: Case Study of Alwar Walled City." *City, Culture and Society* 9: 39–53. https://doi.org/10.1016/j.ccs.2016.10.001.

Distefano, N., and S. Leonardi. 2018. "A List of Accident Scenarios for Three Legs Skewed Intersections." *IATSS Research* 42 (3): 97–104. https://doi.org/10.1016/j.iatssr.2017.07.003.

Foláyan, M. 'Oluwátóyin, E.M.R. de Barros Coelho, C.A. Feldens, B. Gaffar, J.I. Virtanen, A. Kemoli, D. Duangthip, et al. 2024. "A Scoping Review on the Associations between Early Childhood Caries and Sustainable Cities and Communities using the Sustainable Development Goal 11 Framework." *BMC Oral Health* 24 (1): 1–10. https://doi.org/10.1186/s12903-024-04521-1.

48 | WRI INDIA

Assessing urban road networks using geospatial metrics

Frank, L., M. Bradley, S. Kavage, J. Chapman, and T.K. Lawton. 2008. “Urban Form, Travel Time, and Cost Relationships with Tour Complexity and Mode Choice.” Transportation 35 (1): 37–54. https://doi.org/10.1007/s11116-007-9136-6.

Gadepalli, R. 2016. “Role of Intermediate Public Transport in Indian Cities.” Economic and Political Weekly 51 (9): 46–49. http://www.jstor.org/stable/44004442.

Gülgen, F., and T. Gökgöz. 2011. “A Block-Based Selection Method for Road Network Generalization.” International Journal of Digital Earth 4 (2): 133–53. https://doi.org/10.1080/17538947.2010.489972.

Guze, S. 2019. “Graph Theory Approach to the Vulnerability of Transportation Networks.” Algorithms 12 (12): 270. https://doi.org/10.3390/a12120270.

Haldar, S., S. Mandal, S. Bhattacharya, and S. Paul. 2023. “Assessing and Mapping Spatial Accessibility of Peri-Urban and Rural Neighborhood of Durgapur Municipal Corporation, India: A Tool for Transport Planning.” Case Studies on Transport Policy 12: 100990. https://doi.org/10.1016/j.cstp.2023.100990.

Honda, Y., and T. Horiguchi. 2000. “Self-Organization in Four-Direction Traffic-Flow Model.” Journal of the Physical Society of Japan 69 (11): 3744–51. https://doi.org/10.1143/JPSJ.69.3744.

Istrate, M.I. 2015. “Assessment of Settlements’ Centrality in Botoşani County Using Shimbel Index.” Jurnalul Practicilor Comunitare Pozitive, XV (3): 57–69. https://www.ceeol.com/search/article-detail?id=466564.

Jabari, S.E. 2016. “Node Modeling for Congested Urban Road Networks.” Transportation Research Part B: Methodological 91: 229–49. https://doi.org/10.1016/j.trb.2016.06.001.

Jain, G.V., S.S. Jain, and M. Parida. 2022. “Evaluation of Travel Speed of Conventional Buses and Bus Rapid Transit Service in Ahmedabad City, India using Geo-Informatics.” Journal of Public Transportation 24: 100034. https://doi.org/10.1016/j.jpubtr.2022.100034.

Jenelius, E. 2009. “Network Structure and Travel Patterns: Explaining the Geographical Disparities of Road Network Vulnerability.” Journal of Transport Geography 17 (3): 234–44. https://doi.org/10.1016/j.jtrangeo.2008.06.002.

Katekar, V.P., and S.S. Deshmukh. 2024. “Assessment of Socioeconomic Development of the Aspirational District in Central India: A Methodological Comparison.” Journal of Asian and African Studies 59 (3): 935–63. https://doi.org/10.1177/00219096221124937.

Kickert, C., R. vom Hofe, T. Haas, W. Zhang, and B. Mahato. 2020. “Spatial Dynamics of Long-Term Urban Retail Decline in Three Transatlantic Cities.” Cities 107: 102918. https://doi.org/10.1016/j.cities.2020.102918.

Korzhenevych, A., and M. Jain. 2018. “Area- and Gender-Based Commuting Differentials in India’s Largest Urban-Rural Region.” Transportation Research Part D: Transport and Environment 63: 733–46. https://doi.org/10.1016/j.trd.2018.07.013.

Krishna, B.A. 2024. “Medium-Term Projections of Vehicle Ownership, Energy Demand and Vehicular Emissions from Private Road Transport in India.” Environment, Development and Sustainability 27: 13839–67. https://doi.org/10.1007/s10668-024-04473-0.

Kumar, R., D.P. Parida, D.E. Madhu, and A.V.A.B. Kumar. 2017. “Does Connectivity Index of Transport Network Have Impact on Delay for Driver?” Transportation Research Procedia 25: 4988–5002. https://doi.org/10.1016/j.trpro.2017.05.377.

Lee, J., and S. Li. 2017. “Extending Moran’s Index for Measuring Spatiotemporal Clustering of Geographic Events.” Geographical Analysis 49 (1): 36–57. https://doi.org/10.1111/gean.12106.

Lelke, T., and B. Friedrich. 2025. “Extracting Representative Peak Hour Travel Speeds Using Vehicle Trajectories.” Transportation Research Procedia 86: 793–800. https://doi.org/10.1016/j.trpro.2025.04.099.

Li, J. 2011. “Decoupling Urban Transport from GHG Emissions in Indian Cities—a Critical Review and Perspectives.” Energy Policy 39 (6): 3503–14. https://doi.org/10.1016/j.enpol.2011.03.049.

Li, Y., T. Wang, Y. Zhao, and B. Yang. 2025. “Identifying Polycentric Urban Structure Using the Minimum Cycle Basis of Road Network as Building Blocks.” Entropy 27 (6): 618. https://doi.org/10.3390/e27060618.

Liu, C., H. Yin, Y. Sun, L. Wang, and X. Guo. 2022. “A Grade Identification Method of Critical Node in Urban Road Network Based on Multi-Attribute Evaluation Correction.” Applied Sciences 12 (2): 813. https://doi.org/10.3390/app12020813.

Liu, Z., H. Chen, E. Liu, and W. Hu. 2022. “Exploring the Resilience Assessment Framework of Urban Road Network for Sustainable Cities.” Physica A: Statistical Mechanics and Its Applications 586: 126465. https://doi.org/10.1016/J.PHYSA.2021.126465.

Low, S.M. 2001. “The Edge and the Center: Gated Communities and the Discourse of Urban Fear.” American Anthropologist 103 (1): 45–58. https://doi.org/10.1525/aa.2001.103.1.45.

Mackres, E., T. Wong, S. Shabou, E.J. Wesley, and T.H. Tun. 2025. “Calculating Indicators from Global Geospatial Data Sets for Benchmarking and Tracking Change in the Urban Environment.” Technical Note. Washington, DC: World Resources Institute. https://doi.org/10.46830/writn.22.00123v2.

Marshall, W.E., and N.W. Garrick. 2010. “Street Network Types and Road Safety: A Study of 24 California Cities.” Urban Design International 15 (3): 133–47. https://doi.org/10.1057/udi.2009.31.

Martín, B., E. Ortega, R. Cuevas-Wizner, A. Ledda, and A. De Montis. 2021. “Assessing Road Network Resilience: An Accessibility Comparative Analysis.” Transportation Research Part D: Transport and Environment 95: 102851. https://doi.org/10.1016/j.trd.2021.102851.

Marzolf, F., M. Trépanier, and A. Langevin. 2006. “Road Network Monitoring: Algorithms and a Case Study.” Computers & Operations Research 33 (12): 3494–507. https://doi.org/10.1016/j.cor.2005.02.040.

Millsap, R.E., and S.B. Hartog. 1988. “Alpha, Beta, and Gamma Change in Evaluation Research: A Structural Equation Approach.” Journal of Applied Psychology 73 (3): 574–84. https://doi.org/10.1037/0021-9010.73.3.574.

Mohammad, T., A.P. Shanmugam, S. Venkatachalapathi, N.W. Qureshi, P. Seenivasan, and V. Thangavel. 2025. “Vulnerable yet Aspiring: Insights from Micro-and Meso-Level Socio-Economic Vulnerability Assessment of an Aspirational District in Central India.” Sustainable Futures 10: 101329. https://doi.org/10.1016/j.sftr.2025.101329.

WORKING PAPER | July 2026 | 49

Mondragón, R.J. 2020. “Estimating Degree–Degree Correlation and Network Cores from the Connectivity of High–Degree Nodes in Complex Networks.” *Scientific Reports* 10 (1): 5668. https://doi.org/10.1038/s41598-020-62523-9.

Mukherjee, S. 2012. “Statistical Analysis of the Road Network of India.” *Pramana – Journal of Physics* 79 (3): 483–91. https://doi.org/10.1007/s12043-012-0336-z.

Munshi, T. 2016. “Built Environment and Mode Choice Relationship for Commute Travel in the City of Rajkot, India.” *Transportation Research Part D: Transport and Environment* 44: 239–53. https://doi.org/10.1016/j.trd.2015.12.005.

Nagurney, A., J. Dong, and P.L. Mokhtarian. 2001. “Teleshopping versus Shopping: A Multicriteria Network Equilibrium Framework.” *Mathematical and Computer Modelling* 34 (7–8): 783–98. https://doi.org/10.1016/S0895-7177(01)00099-1.

Narain, V. 2017. “Taken for a Ride? Mainstreaming Periurban Transport with Urban Expansion Policies.” *Land Use Policy* 64: 145–52. https://doi.org/10.1016/j.landusepol.2017.01.050.

Narain, V., and S. Nischal. 2007. “The Peri-Urban Interface in Shahpur Khurd and Karnera, India.” *Environment and Urbanization* 19 (1): 261–73. https://doi.org/10.1177/0956247807076905.

Oyebisi, S., K.A. Kaaf, M.I. Shammas, M. Seyam, and O.M. Oyewola. 2025. “Predicting Alpha and Gamma Indexes from Industrial Recyclates Using Artificial Intelligence.” *Discover Applied Sciences* 7 (11): 1370. https://doi.org/10.1007/s42452-025-07828-y.

Pahlevan-Sharif, S., P. Mura, and S.N.R. Wijesinghe. 2019. “A Systematic Review of Systematic Reviews in Tourism.” *Journal of Hospitality and Tourism Management* 39: 158–65. https://doi.org/10.1016/j.jhtm.2019.04.001.

Pai, M., P. Mulukutla, and A. Mukherjee. 2025. “Toward a Framework to Support Better Decision-Making in India’s Mobility Planning: Supply, Demand, and Performance.” Expert Note. New Delhi: WRI India. https://doi.org/10.46830/wrien.25.00012.

Pandey, A., and C. Venkataraman. 2014. “Estimating Emissions from the Indian Transport Sector with On-Road Fleet Composition and Traffic Volume.” *Atmospheric Environment* 98: 123–33. https://doi.org/10.1016/j.atmosenv.2014.08.039.

Paul, J., and A. Rosado-Serrano. 2019. “Gradual Internationalization vs Born-Global/International New Venture Models: A Review and Research Agenda.” *International Marketing Review* 36 (6): 830–58. https://doi.org/10.1108/IMR-10-2018-0280.

Pitale, A.M., S. Sadhukhan, and M. Parida. 2025. “Exploring Factors Influencing Commuters’ Satisfaction towards Regional Transit System: A Case of National Capital Region, India.” *Case Studies on Transport Policy* 19: 101372. https://doi.org/10.1016/j.cstp.2025.101372.

Porta, S., E. Strano, V. Iacoviello, R. Messora, V. Latora, A. Cardillo, F. Wang, and S. Scellato. 2009. “Street Centrality and Densities of Retail and Services in Bologna, Italy.” *Environment and Planning B: Urban Analytics and City Science* 36 (3): 450–65. https://doi.org/10.1068/b34098.

RBI (Reserve Bank of India). 2012. “Section 23 of the Banking Regulation Act, 1949—Master Circular on Branch Authorisation—Census Data 2011,” July 2. https://www.rbi.org.in/commonperson/English/scripts/Notification.aspx?id=1068.

Rivera-Royero, D., G. Galindo, M. Jaller, and J. Betancourt Reyes. 2022. “Road Network Performance: A Review on Relevant Concepts.” *Computers & Industrial Engineering* 165: 107927. https://doi.org/10.1016/j.cie.2021.107927.

Sanghera, B., and E. Satybaldieva. 2020. “The Other Road to Serfdom: The Rise of the Rentier Class in Post-Soviet Economies.” *Social Science Information* 59 (3): 505–36. https://doi.org/10.1177/0539018420943077.

Shanmugasundaram, N., K. Sushita, S.P. Kumar, and E.N. Ganesh. 2019. “Genetic Algorithm-Based Road Network Design for Optimising the Vehicle Travel Distance.” *International Journal of Vehicle Information and Communication Systems* 4 (4): 355–74. https://doi.org/10.1504/IJVICS.2019.103931.

Sharma, K., C. Aswal, and J. Paul. 2022. “Factors Affecting Green Purchase Behavior: A Systematic Literature Review.” *Business Strategy and the Environment* 32 (4): 2078–92. https://doi.org/10.1002/bse.3237.

Sirmatel, I.I., D. Tsitsokas, A. Kouvelas, and N. Geroliminis. 2021. “Modeling, Estimation, and Control in Large-Scale Urban Road Networks with Remaining Travel Distance Dynamics.” *Transportation Research Part C: Emerging Technologies* 128: 103157. https://doi.org/10.1016/j.trc.2021.103157.

Soczówka, P., R. Zochowska, and G. Karoń. 2020. “Method of the Analysis of the Connectivity of Road and Street Network in Terms of Division of the City Area.” *Computation* 8 (2): 54. https://doi.org/10.3390/computation8020054.

Södergren, J. 2021. “Brand Authenticity: 25 Years of Research.” *International Journal of Consumer Studies* 45 (4): 645–63. https://doi.org/10.1111/ijcs.12651.

Sreelekha, M.G., K. Krishnamurthy, and M.V.L.R. Anjaneyulu. 2016. “Interaction between Road Network Connectivity and Spatial Pattern.” *Procedia Technology* 24: 131–39. https://doi.org/10.1016/j.protcy.2016.05.019.

Taylor, M.A.P., S.V.C. Sekhar, and G.M. d’Este. 2006. “Application of Accessibility Based Methods for Vulnerability Analysis of Strategic Road Networks.” *Networks and Spatial Economics* 6 (3–4): 267–91. https://doi.org/10.1007/s11067-006-9284-9.

TomTom Traffic Index. 2025. “Traffic Index Ranking 2025.” https://www.tomtom.com/traffic-index/ranking/.

Turok, I., L. Seeliger, and J. Visagie. 2021. “Restoring the Core? Central City Decline and Transformation in the South.” *Progress in Planning* 144: 100434. https://doi.org/10.1016/j.progress.2019.100434.

Vishnu, N., S. Kameshwar, and J.E. Padgett. 2023. “Road Transportation Network Hazard Sustainability and Resilience: Correlations and Comparisons.” *Structure and Infrastructure Engineering* 19 (3): 345–65. https://doi.org/10.1080/15732479.2021.1945114.

Vuk, G., J.L. Bowman, A. Daly, and S. Hess. 2016. “Impact of Family in-Home Quality Time on Person Travel Demand.” *Transportation* 43 (4): 705–24. https://doi.org/10.1007/S11116-015-9613-2.

Wang, F., A. Antipova, and S. Porta. 2011. “Street Centrality and Land Use Intensity in Baton Rouge, Louisiana.” *Journal of Transport Geography* 19 (2): 285–93. https://doi.org/10.1016/j.jtrangeo.2010.01.004.

50 | WRI INDIA

Assessing urban road networks using geospatial metrics

Wang, W.X., R.J. Guo, and J. Yu. 2018. "Research on Road Traffic Congestion Index Based on Comprehensive Parameters: Taking Dalian City as an Example." Advances in Mechanical Engineering 10 (6). https://doi.org/10.1177/1687814018781482.

Wang, Z., L. Li, and Y. Li. 2015. "From Super Block to Small Block: Urban Form Transformation and Its Road Network Impacts in Chenggong, China." Mitigation and Adaptation Strategies for Global Change 20 (5): 683–99. https://doi.org/10.1007/s11027-014-9614-z.

Wang, F., C. Chen, C. Xiu, and P. Zhang. 2014. "Location Analysis of Retail Stores in Changchun, China: A Street Centrality Perspective." Cities 41 (Part A): 54–63. https://doi.org/10.1016/j.cities.2014.05.005.

Wang, X., X. Wu, M. Abdel-Aty, and P.J. Tremont. 2013. "Investigation of Road Network Features and Safety Performance." Accident Analysis & Prevention 56: 22–31. https://doi.org/10.1016/j.aap.2013.02.026.

Wang, S., D. Yu, M.P. Kwan, L. Zheng, H. Miao, and Y. Li. 2020. "The Impacts of Road Network Density on Motor Vehicle Travel: An Empirical Study of Chinese Cities Based on Network Theory." Transportation Research Part A: Policy and Practice 132: 144–156. https://doi.org/10.1016/j.tra.2019.11.012.

Wang, X., T. Fan, W. Li, R. Yu, D. Bullock, B. Wu, and P. Tremont. 2016. "Speed Variation during Peak and Off-Peak Hours on Urban Arterials in Shanghai." Transportation Research Part C: Emerging Technologies, 67: 84–94. https://doi.org/10.1016/j.trc.2016.02.005.

Waples, R.S., and O. Gaggiotti. 2006. "What Is a Population? An Empirical Evaluation of Some Genetic Methods for Identifying the Number of Gene Pools and Their Degree of Connectivity." Molecular Ecology 15 (6): 1419–39. https://doi.org/10.1111/j.1365-294X.2006.02890.x.

Wright, M.A., G. Gomes, R. Horowitz, and A.A. Kurzhanskiy. 2017a. "On Node Models for High-Dimensional Road Networks." Transportation Research Part B: Methodological 105: 212–34. https://doi.org/10.1016/j.trb.2017.09.001.

Wu, G., and J. Hong. 2022. "An Analysis of the Role of Residential Location on the Relationships between Time Spent Online and Non-Mandatory Activity-Travel Time Use over Time." Journal of Transport Geography 102: 103378. https://doi.org/10.1016/j.jtrangeo.2022.103378.

Xie, F., and D. Levinson. 2007. "Measuring the Structure of Road Networks." Geographical Analysis 39 (3): 336–56. https://doi.org/10.1111/j.1538-4632.2007.00707.x.

Xu, S., X. Xie, C. Wang, and J. Yan. 2025. "On the Safety Effects of Off-Peak Hour Speed Characteristics of Urban Arterials." Multimodal Transportation 4 (2): 100206. https://doi.org/10.1016/j.multra.2025.100206.

Yang, Z., Y. Yao, and L. Zhang. 2025. "Optimizing Autonomous Taxi Deployment for Safety at Skewed Intersections: A Simulation Study." Sensors 25 (11): 3544. https://doi.org/10.3390/S25113544.

Yang, X., Y. Li, Y. Cai, Y. Cao, K.Y. Lee, and Z. Jia. 2018. "Impact of Road-Block on Peak-Load of Coupled Traffic and Energy Transportation Networks." Energies 11 (7): 1776. https://doi.org/10.3390/en11071776.

Yu, H., J. Fang, S. Liu, Y. Ren, and J. Lu. 2021. "A Node Optimization Model Based on the Spatiotemporal Characteristics of the Road Network for Urban Traffic Mobile Crowd Sensing." Vehicular Communications 31: 100383. https://doi.org/10.1016/j.vehcom.2021.100383.

Zeng, J., Y. Qian, Z. Ren, D. Xu, and X. Wei. 2019. "Road Landscape Morphology of Valley City Blocks under the Concept of 'Open Block'—Taking Lanzhou City as an Example." Sustainability 11 (22): 6258. https://doi.org/10.3390/SU11226258.

Zhang, Y., X. Li, A. Wang, T. Bao, and S. Tian. 2015. "Density and Diversity of OpenStreetMap Road Networks in China." Journal of Urban Management 4 (2): 135–46. https://doi.org/10.1016/j.jum.2015.10.001.

Zhou, Q. 2015. "Comparative Study of Approaches to Delineating Built-Up Areas Using Road Network Data." Transactions in GIS 19 (6): 848–76. https://doi.org/10.1111/tgis.12135.

WORKING PAPER | July 2026

51

## Acknowledgments

We would like to thank the external reviewers, Professor Sumit Sen from the Indian Institute of Technology Bombay and Professor Sumana Gupta from the Indian Institute of Technology Kharagpur, for their valuable feedback and insightful comments, which helped improve the quality of this manuscript.

We also extend our sincere gratitude to the internal reviewers from WRI India—Aloke Mukherjee, Rohan Rao, Thet Hein Tun, and David Perez Barbosa—for their thoughtful suggestions and constructive inputs.

We are especially grateful to Aloke Mukherjee for his continuous guidance and encouragement throughout this publication journey. We also thank Manu V. Mathai, Director, Research Integrity, and Purva Sharma, Lead, Research Integrity, for their guidance during the review and publication process.

We would like to acknowledge Robin Infant Raj Devadoss and his editorial team for their editorial assistance. Our thanks also go to Karthikeyan Shanmugam, Santhosh Matthew Paul, Ankita Rajeshwari, and Rama Thoopal for their essential administrative, design, and editorial support.

Finally, we thank our teammates and colleagues for their contributions to this working paper, with particular appreciation for Arundhati Hakhu and S. Nileena for their design expertise and dedication in bringing this document to its final form.

## About the authors

**Dr. Archiman Biswas** (ORCID 0000-0003-2045-1143) is a Program Associate, Spatial Data and Data Analytics, Sustainable Cities and Transport Program, WRI India.

Contact: archiman.biswas@wri.org

**Bina Shetty** is the Director, Spatial Data and Data Analytics, Sustainable Cities and Transport Program, WRI India.

Contact: bina.shetty@wri.org

**Madhav Pai** is CEO, WRI India.

Contact: madhav.pai@wri.org

**Raj Bhagat Palanichamy** is a Senior Program Manager, Geo Analytics, Sustainable Cities and Transport Program, WRI India.

Contact: rajbhagat.p@wri.org

**Sonal Ganvir** is a Junior Program Associate, Integrated Transport, Sustainable Cities and Transport Program, WRI India.

Contact: sonal.ganvir@wri.org

**Janhavi Mane** is a Senior Program Associate, Geo Analytics, Sustainable Cities and Transport Program, WRI India.

Contact: janhavi.mane@wri.org

**Dr. Priam Pillai** is an Associate Professor,

Pillai College of Engineering, India.

Contact: ppillai@mes.ac.in

## About WRI India

WRI India, an independent knowledge organization registered as India Resources Trust, provides objective information and practical proposals to foster environmentally sound and socially equitable development. Through research, analysis, and recommendations, WRI India puts ideas into action to build transformative solutions to protect the earth, promote livelihoods, and enhance human well-being.

Know more: wri-india.org

creative commons

Copyright 2026 WRI India. This work is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-nd/4.0/

52 | WRI INDIA

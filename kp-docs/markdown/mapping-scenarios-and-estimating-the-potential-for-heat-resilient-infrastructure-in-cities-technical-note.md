---
doc_id: mapping-scenarios-and-estimating-the-potential-for-heat-resilient-infrastructure-in-cities-technical-note
source_pdf: documents/mapping-scenarios-and-estimating-the-potential-for-heat-resilient-infrastructure-in-cities-technical-note.pdf
extraction_method: postgres-full-text
parse_backend: mistral
parse_model: mistral-ocr-latest
char_count: 186007
title: Mapping Scenarios and Estimating the Potential for Heat-Resilient Infrastructure in Cities
authors: Elizabeth Jane Wesley; Eric Mackres; Kurt Shickman; Clemens Janssen; Madeline Mulder; Theodore Wong
date_published: 2026-03-16
year_published: 2026
article_type: Technical Note
wri_primary_office: WRI Global
language: en
doi: 10.46830/writn.24.00028
status: searchable
---

![img-0.jpeg](img-0.jpeg)

WORLD
RESOURCES
INSTITUTE

TECHNICAL NOTE

# Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

Elizabeth Jane Wesley, Eric Mackres, Kurt Shickman, Clemens Janssen, Madeline Mulder, and Theodore Wong

CONTENTS

Introduction...2
Methodology...9
Limitations...39
Findings...40
Endnotes...41
Conclusions...41
References...41
Acknowledgments...44
About the authors...44

Technical notes document the research or analytical methodology underpinning a publication, interactive application, or tool.

Suggested Citation: Wesley, E.J., E. Mackres, K. Shickman, C. Janssen, M. Mulder, and T. Wong. 2026. "Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities." Technical Note. Washington, DC: World Resources Institute. Available online at doi.org/10.46830/writn.24.00028.

Abstract

Cities worldwide face rising heat from climate change and urbanization. Passive, heat-resilient infrastructure—like trees, cool roofs, reflective pavements, and shade structures—are low-energy solutions, yet many cities lack data and tools to plan implementation. We present a globally scalable, open-source framework for generating infrastructure implementation scenarios. We introduce OpenUrban—a high-resolution urban land-use/land-cover dataset validated at 93 percent accuracy in the United States and 83 percent globally—and pair it with remotely sensed surface characteristics (albedo, tree canopy, fractional vegetation, land-surface temperature). Using these inputs, we construct three nested scenario levels: technical (maximum feasible), achievable (benchmarked to high-performing areas), and program (policy-driven). We then produce scenario maps—spatially explicit simulations of infrastructure—and quantify them with potentials—indicators of area-wide changes in surface characteristics under full implementation. Together, these outputs provide a practical entry point for evidence-based action, lowering data barriers and supporting more resilient futures. The framework serves both technical and nontechnical practitioners, translating complex data into actionable takeaways.

WORLD RESOURCES INSTITUTE

TECHNICAL NOTE | Version 1.0 | March 2026 | 1

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

## Introduction

Urban areas are often significantly hotter than surrounding rural regions and are warming at twice the global average rate (United Nations 2021). Yet the same characteristics that drive this heat—particularly dark, impervious surfaces and a lack of vegetation—also present opportunities for mitigation through thoughtful urban design. Heat-resilient infrastructure, such as trees, vegetation, cool roofs, and reflective pavements, can reduce individual heat exposure and lower area-wide temperatures when implemented at scale. And unlike active cooling infrastructure such as air conditioning, these passive solutions can also support cities in reaching net-zero energy goals. In alignment with the literature, we use the term “heat-resilient infrastructure” to refer to infrastructure interventions that increase urban resilience to extreme heat by reducing heat exposure and thermal stress, rather than infrastructure designed solely to withstand heat damage.

Despite these benefits, cities often lack the information needed to identify the most effective heat-resilient interventions and where to implement them. Developing locally relevant analytical tools is frequently time-consuming, expensive, and out of reach for many urban decision-makers (Jain and Espey 2022). Additionally, developing the capacity and expertise within city governments to obtain and refine vast quantities of data into actionable information and insights is a frequently reported challenge (Ukkusuri et al. 2024). While a core set of passive heat mitigation strategies is widely recognized, the optimal combination of solutions is highly context-specific (United Nations 2021). Although more city plans are beginning to address urban heat, few include actionable data or a range of infrastructure solutions (Turner et al. 2022). Moreover, many existing data sources are not outcome-oriented enough to guide effective policy (Jain and Espey 2022).

To better understand cities’ needs for long-term adaptation to rising temperatures, we conducted in-depth interviews and workshops with city officials, urban planners, and subject matter experts in a diverse selection of global cities. Across cities, there was a strong call for scenario-based, solution-oriented data and tools that could bridge the gap between heat risk information and implementation. Officials wanted platforms that not only show where heat risks are highest but also model the potential impacts, costs, and trade-offs of different heat-resilient infrastructure intervention types. As one city official from a climate adaptation department put it, “If we could do intervention scenarios, that would be amazing.” This kind of actionable insight, they stressed, would allow them to prepare more compelling proposals, coordinate better across departments, and secure political and financial backing for heat adaptation measures.

Experts in climate resilience, public health, and urban planning echoed the importance of contextualized outputs and visuals that could spark cross-sector dialogue.

This technical note presents methods for defining scenarios of heat-resilient infrastructure implementation, calculating potentials, and generating infrastructure maps (Figure 1). Potentials are indicators that quantify how surface characteristics—such as vegetation, reflectivity, and shade—could change through the implementation of different types of infrastructure. Scenario maps are spatial representations of those changes, illustrating what implementation might look like and how it would alter surface characteristics in an urban area. Together, these outputs provide a structured, data-driven way for cities to evaluate opportunities for cooling, compare intervention types, and prioritize strategies that best meet local needs. While cost is not yet included in this framework, it is a priority for future development.

Cities have consistently asked for flexible decision-support frameworks that can translate complex spatial data into actionable, policy-aligned resources. The methods presented here address this gap. Rather than prescribing specific interventions, the methods equip cities with consistent ways to understand current conditions of heat-related infrastructure and to identify, visualize, and quantify opportunities for new or expanded implementation through scenarios. For example, a tree-planting scenario for parks would estimate existing tree cover, identify where additional canopy could be added, map what tree cover could look like under specific park-level standards, and quantify the resulting change across the city.

The methods are flexible, meaning they can be applied across a range of urban contexts and infrastructure types; adaptable, in that they can be modified to incorporate new data, priorities, or planning needs over time; and scalable, allowing for analysis at both neighborhood and city levels depending on the scope of application.

These heat-resilient infrastructure scenarios are designed to serve both practitioners and researchers, supporting uses that span community engagement, policy development, planning processes, and integration into heat-modeling analyses. Additionally, they have been specifically developed within a broader ecosystem of tools that includes modeling the effects of these implementation scenarios on thermal comfort (Engel et al. 2026), as well as an interactive application called the Cool Cities Lab designed to help users extract insights from the data that can support their heat-resilient planning goals (Figure 2). Together, they help provide cities with meaningful information,

2 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

Figure 1 | Our framework for mapping scenarios and estimating potential for heat-resilient infrastructure, using street trees as an example

![img-1.jpeg](img-1.jpeg)

Note: The Baseline column (a) shows the foundational datasets used in our data fusion workflow, including OpenUrban land use and land cover, tree canopy height, shade, and albedo. These layers define existing surface characteristics and physical constraints. For the street tree scenarios we use OpenUrban (b) and tree canopy (c) to determine the current levels of street tree implementation. The Scenario definition column (d) demonstrates how we identify where additional infrastructure could be implemented (within the plantable areas of pedestrian areas) at levels defined by locally derived targets. The citywide distribution of existing street tree cover is shown in the density plot (e), with a red line at the 90th percentile that defines the achievable target (19.5% tree cover). Finally, the Scenario map and potential column (f) shows a spatially explicit scenario map that simulates tree planting under a program scenario, resulting in a quantifiable potential—in this example, an area-wide tree cover of 9.5% increase from the baseline of 4.8% from planting street trees to the achievable target. Together, these components summarize the full workflow: mapping existing conditions (a), defining technical, achievable, and program scenarios (d), and estimating both spatial patterns and area-wide impacts of infrastructure implementation (f).

Source: WRI authors.

TECHNICAL NOTE | March 2026

3

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

Figure 2 | Cool Cities Lab workflow

![img-2.jpeg](img-2.jpeg)

Note: The orange boxes represent methods presented in this technical note for baselining surface characteristics and generating scenarios. The blue box represents the thermal comfort modeling presented in Engel et al. (2026). The thermal comfort modeling takes both baseline (existing conditions) and scenario (modeled conditions) maps as inputs and estimates high-resolution spatial data on thermal comfort. The green boxes represent the Cool Cities Lab, where we compare the thermal comfort outputs from the baseline and the scenarios to evaluate the impacts of infrastructure implementation. The information presented in the Cool Cities Lab allows cities to prioritize actions.

Source: WRI authors.

context, and insight to support more informed and targeted planning to reduce extreme heat.

The central output of our methods is not just measurements of urban surfaces but actionable scenarios of heat-resilient infrastructure implementation that directly address the needs cities identified in our engagement.

## Heat-resilient infrastructure

Heat-resilient infrastructure affects urban temperatures by altering the way energy is partitioned, stored, and dissipated in the urban environment. Broadly, heat-resilient infrastructure influences heat in three ways: reducing the amount of solar radiation converted to sensible heat, lowering anthropogenic heat inputs, and dissipating stored heat.

- **High-albedo surfaces** such as cool roofs and reflective pavements reflect more solar energy than darker materials. They lower surrounding air temperatures by preventing surfaces from absorbing and reradiating heat into the atmosphere. When applied to roofs, they also reduce indoor temperatures, which decreases the demand for air conditioning and in turn lowers anthropogenic heat emissions.

- **Shade**, whether provided by structures or trees, reduces direct human exposure to solar radiation, which is often the most important factor in how hot people feel. When buildings are shaded, indoor cooling demand is reduced.

- **Trees, other vegetation, and permeable surfaces** partition energy into latent rather than sensible heat through evapotranspiration, which increases humidity and dissipates heat. Water bodies provide similar cooling through evaporation.

Additionally, strategies to increase ventilation and wind flow, like designing buildings and controlling road layouts to create ventilation corridors, can dissipate heat. By deploying and combining heat-resilient infrastructures, cities can create cooler, more comfortable urban environments and reduce the health risks associated with extreme heat (United Nations 2021).

The effectiveness of these interventions depends both on where and how extensively they are applied and on the broader urban context. Heat exposure in cities varies with physical factors like geography, climate, topography, built form, land cover, and construction practices and is affected by human factors including health, wealth, age, and access to active cooling (United Nations 2021). Additionally, vulnerability varies across these dimensions.

4 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

Ideally, solutions are tailored to each city’s environmental and socioeconomic conditions.

Several strategies are broadly relevant and were prioritized by many of the city stakeholders we interviewed, although it is worth noting that strategies focused on keeping people cool indoors—including resources like cooling centers—, which cannot be modeled using this framework. Our user research highlights four infrastructure intervention types of greatest interest for urban cooling: increasing the reflectivity of roofs, increasing the reflectivity of pavements, expanding tree canopy, and shade structures. Each of these has been shown to reduce urban temperatures, with the magnitude of cooling depending on both the fraction of area treated and the intensity of implementation (Krayenhoff and Voogt 2010). These interventions form the building blocks of the scenarios we design and will be described in greater detail in the following subsections.

## Reflective surfaces

A promising strategy for reducing urban heat is to increase the solar reflectance of roofs, walls, and pavements (Levinson et al. 2023). Solar reflectivity, or albedo, is the fraction of incoming sunlight that a surface reflects, expressed as a unitless value ranging from 0 (no reflectance) to 1 (perfect reflectance). Surfaces with high albedo stay relatively cooler than darker, low-albedo surfaces because they reflect more solar energy and absorb—and subsequently emit—less heat. Because their cooling effect is driven by reflected solar radiation, high-albedo surfaces are most effective for heat mitigation in environments with high solar exposure.

A systematic review of numeric modeling studies by Krayenhoff et al. (2021) found that increasing surface albedo at the neighborhood scale (100–5,000 square meters [m$^{2}$]) can reduce daytime air temperatures by 0.2–0.6 degrees Celsius (°C) per 0.1 increase in albedo. Although large-scale experimental deployments are limited, observational research has documented localized cooling effects: for example, widespread application of white coatings of greenhouses in southern Spain produced statistically significant reductions in surrounding temperatures (Campra et al. 2008).

In addition to local cooling benefits, reflective surfaces may help mitigate global climate change. Akbari et al. (2009) estimate that increasing the albedo of all roofs and roads worldwide—assuming an urban surface coverage of 25 percent for roofs and 35 percent for paved areas—could produce a radiative forcing reduction equivalent to offsetting approximately 44 gigatons of carbon dioxide (CO$_{2}$) emissions annually—more than the total global CO$_{2}$-related emissions in 2023 (IEA 2024).

The following subsections provide details on types of reflective surfaces and their impacts on urban heat.

## COOL ROOFS

Cool roofs, made with reflective materials or coatings, reduce building and air temperatures by reflecting solar energy and limiting heat absorption (Croce and Vettorato 2021; Hewitt et al. 2014). By lowering indoor temperatures, cool roofs reduce the need for air conditioning, decreasing energy consumption, peak power demand, and energy costs for building owners and occupants (Hewitt et al. 2014; Levinson et al. 2023). A study in the Chicago metropolitan area found that widespread adoption of cool roofs could reduce energy consumption used for cooling by 16.6 percent (Tan et al. 2023).

Cool roofs also provide citywide benefits by lowering ambient temperatures, mitigating the urban heat island effect, improving air quality, and contributing to climate mitigation (Hewitt et al. 2014; Levinson et al. 2023). These broader impacts can translate into meaningful health outcomes, particularly during extreme heat events. For example, a study in London estimated that converting all city roofs to cool roofs could have reduced heat-related mortality during the 2018 summer heatwave by 32 percent (Simpson et al. 2024). While large-scale real-world studies are still limited and observed temperature effects are likely to be smaller than model-based estimates due to partial implementation, the ability of cool roofs to reduce air temperatures is well documented.

In addition to providing thermal benefits, cool roof materials experience less heat-related expansion and contraction than darker roofs, which can extend roof lifespan and reduce construction material waste (Hewitt et al. 2014). Some technologies, such as reflective coatings, can be applied to existing roofs at relatively low cost (Keith and Meerow 2022). Although cool roofs are not compatible with green roofs, they are generally more effective at reducing air temperatures (Krayenhoff et al. 2021), are often more cost-effective, and their effectiveness is not limited by water availability (Keith and Meerow 2022). As temperatures continue to rise, cool roofs represent a low-risk, high-benefit strategy for climate adaptation (Levinson et al. 2023).

## REFLECTIVE PAVEMENTS AND WALLS

Like cool roofs, reflective pavements and walls can help reduce ambient temperatures by increasing solar reflectance. Numerical models suggest that widespread application of reflective surfaces across an entire city can produce substantial cooling benefits—for example, in Chicago, simulated large-scale adoption was found to reduce maximum daytime temperatures by up to 1.9°C,

TECHNICAL NOTE | March 2026 | 5

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

with potentially greater impacts in hotter, sunnier climates (Sen and Khazanovich 2021).

However, the effects of increasing the albedo of walls and pavements are considerably more complex and context-dependent than those of roofs, where reflected solar radiation primarily dissipates upward. Ground and wall surfaces operate within the street canyon environment, where the directional reflection of light can lead to unintended consequences. For instance, light reflected from high-albedo pavement or opposing walls may increase the solar heat gain on adjacent building facades, potentially raising indoor temperatures and increasing cooling demand (Yaghoobian and Kleissl 2012).

While reflective pavements are highly effective at reducing the pavement surface temperature—with observed midday drops up to 4–6°C (Middel et al. 2020) and a peak reduction of 8.4°C (Schneider et al. 2023) compared to traditional asphalt—this cooling benefit does not directly translate to human comfort. The high albedo of the pavement reflects solar radiation upward, resulting in a significant trade-off: the mean radiant temperature for pedestrians is elevated by as much as 5.1°C during the midday period, causing an increase in perceived heat stress despite having negligible impact on ambient air temperature (Schneider et al. 2023). Furthermore, the light-colored surfaces introduce glare, which poses a policy-relevant safety concern by reducing visual comfort and visibility for drivers and pedestrians (Middel et al. 2020). Consequently, evidence-based guidance stresses that reflective pavements should not be applied to high-occupancy pedestrian areas and must be co-located with shading strategies (such as trees or engineered canopies) to shield people from the radiant heat penalty and reflected glare, ensuring that the surface cooling benefits are realized without compromising human health or safety (Middel et al. 2020; Schneider et al. 2023).

## Green surfaces

Urban vegetation cools cities through evapotranspiration—the process by which plants release water vapor into the air. As liquid water absorbed by plant roots evaporates from leaves, it consumes heat from the surrounding environment, converting sensible heat into latent heat and thereby lowering air temperatures (Winbourne et al. 2020). This cooling effect is strongest in hot, dry climates where high vapor pressure deficits enhance plant transpiration (Li et al. 2024). The cooling effects of evapotranspiration peak during midday, when solar radiation is highest.

In addition to reducing urban air temperatures, increasing green surfaces—like trees, parks, informal green spaces, or green roofs—provides a range of co-benefits. In addition to these biophysical benefits, urban greenery helps manage stormwater

runoff, encourages physical activity, and can improve air quality (Hewitt et al. 2014; Leff 2016), although evidence on air-quality impacts is mixed (Eisenman et al. 2019). Trees enhance the aesthetic appeal of streetscapes, reduce building energy use through shading, and can increase property values (Hewitt et al. 2014; Leff 2016). Greenspaces can also contribute to safer and more inviting public spaces, strengthen community cohesion, and support a range of public health benefits (Leff 2016; TNC 2016). Finally, they provide habitat for numerous species, further enriching urban ecosystems (Leff 2016). The following subsections provide details on green surfaces and their impacts on urban heat.

### TREES

Trees provide extensive benefits in urban areas, including cooling through both shading (discussed below in “Natural and constructed shade”) and through evapotranspiration, which accounts for approximately 29 percent of total cooling within tree canopies (Winbourne et al. 2020). A global meta-analysis by Li et al. (2024) found that trees are reported to reduce pedestrian-level air temperatures by an average of 1–2.5°C depending on urban morphology and climate zone. Likewise, a meta-analysis by Krayenhoff et al. (2021) estimates that trees can provide cooling of up to 0.33°C per 10 percent increase in tree cover.

### GREENSPACE

Vegetated, permeable areas like parks and informal greenspaces can lower daytime air temperatures through evapotranspiration by 1–5°C, particularly in areas with dense vegetation (Bowler et al. 2010). These areas often create park cool islands (PCI), where cooling extends beyond park boundaries and reduces temperatures in adjacent neighborhoods. The PCI effect can lower nearby air temperatures by 1–2°C and extend up to 1–2 kilometers (km), depending on park size, vegetation type, and surrounding land cover (Ziter et al. 2019). In addition to cooling, greenspaces reduce flood risk, support biodiversity, offer mental health benefits, and strengthen community well-being (Keith and Meerow 2022).

### GREEN ROOFS

Green roofs are vegetated systems installed on rooftops that cool by providing both insulation and evapotranspiration. While they typically provide less direct cooling than reflective (white) roofs, they offer additional environmental benefits, including stormwater management, improved building energy efficiency, and support for urban biodiversity (Santamouris 2014). A review of studies from the United States and Asia suggests that full deployment of green roofs across a city could reduce air temperatures by 0.3–3°C (Santamouris 2014).

6 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

## Natural and constructed shade

Shade plays a vital role in reducing the impacts of urban heat by blocking direct solar radiation, lowering surface temperatures, and improving thermal comfort. Whether provided by trees or built structures, shade helps mitigate heat exposure, supports outdoor activity, and contributes to public health and well-being. The following subsections offer details on shade-providing infrastructures and their impacts on urban heat.

# TREES

Beyond the benefits discussed above in “Green surfaces,” trees mitigate urban heat most directly by blocking incoming solar radiation and shading people, buildings, and pavements. In Phoenix, measurements showed that trees lowered mean radiant temperature—an indicator of perceived heat that is strongly influenced by shade—by up to 26°C (Middel et al. 2021). In Ohio, pavement temperatures under tree shade were found to be 5–25°C cooler (Naik et al. 2017). Model results from the Los Angeles basin suggest that reducing pavement temperatures by 10°C could extend pavement lifespan by a factor of 25 by decreasing its sensitivity to distortion from repeated use (Akbari et al. 2001).

# SHADE STRUCTURES

Shade structures provide immediate relief from heat by blocking direct solar radiation to both people and surfaces (Kappou et al. 2022; Keith and Meerow 2022; Middel et al. 2020). This results in reduced surface temperatures and lower mean radiant temperature, improving thermal comfort and expanding the usability of outdoor spaces (Buo et al. 2023).

Unlike trees, which require time to grow and mature, built shade structures can be deployed rapidly and designed for targeted use—such as playgrounds, transit stops, or walkways. They can also be oriented or designed to provide shade at specific times of day or in areas where tree planting is not feasible (Keith and Meerow 2022; Middel et al. 2020). For example, breezeways and tunnels can provide consistent shade throughout the day (Middel et al. 2020), while building overhangs can be oriented to block peak sun angles (Keith and Meerow 2022). Shade sails, pergolas, canopies, and umbrellas all contribute to cooler, more comfortable urban environments and can enhance the visual character of public spaces (Keith and Meerow 2022; Middel et al. 2020). Even temporary shade structures, such as umbrellas and sails, have been shown to reduce surface temperatures by more than 17°C during the day (Middel et al. 2020).

In addition to improving outdoor comfort, shade structures attached to buildings can help keep buildings cooler by blocking sunlight from hitting walls and windows, which reduces

the need for air conditioning and lowers energy use (Keith and Meerow 2022). Permanent structures like pergolas can also be designed with reflective roofing materials to further enhance their cooling potential.

## Heat-resilient infrastructure potential

Here we define scenarios of heat-resilient infrastructure implementation and describe methods to produce two complementary outputs: potentials and scenario maps. Potentials are indicators that quantify the levels of surface characteristics attainable through the full implementation of a heat-resilient infrastructure scenario. They are expressed as area-wide percentages of vegetation or tree cover, surface reflectivity, or shade cover. These potentials form a set of indices that can be used to evaluate how changes in surface characteristics—resulting from different infrastructure interventions—translate into heat-related outcomes. Scenario maps are spatial realizations of infrastructure implementation scenarios and are useful for visualizing possibilities and evaluating their impacts on thermal comfort.

Scenarios are organized into three nested categories (Figure 3):

- **Technical**—the maximum possible implementation of an infrastructure intervention, given baseline surface conditions and current technologies.
- **Achievable**—a more conservative implementation based on existing high levels of infrastructure in parts of the city.
- **Program**—implementation constrained by specific programmatic or policy assumptions.

Framing scenarios in these three levels allows them to reflect both physical and institutional realities: technical scenarios benchmark what is physically possible, achievable scenarios set more realistic targets that are ambitious but may be possible, and program scenarios illustrate how policy objectives could shape implementation. These terms are widely adopted in the energy-efficiency literature as a framework for estimating the potential of interventions across levels of constraint (EPA 2007). The parameters defining each scenario can be customized based on user needs and local context, but we provide reasonable default values derived from existing research, planning guidelines, and material specifications.

By combining the constraints that define these scenarios with spatial data on land use and land cover (LULC) and heat-relevant surface characteristics (e.g., vegetation, albedo, shade), we can quantify the effects of implementation on these characteristics with indicators of potential and create detailed maps that visualize where and how infrastructure could be implemented across an area. These potentials and maps help cities estimate

TECHNICAL NOTE | March 2026 | 7

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

**Figure 3 | Heat-resilient infrastructure scenario framework**

![img-3.jpeg](img-3.jpeg)

*Note:* Technical scenarios represent the maximum infrastructure implementation given the baseline conditions and current technological limitations. Achievable scenarios represent a level of implementation determined by the highest levels of current implementation within a given city. There are many possible program scenarios, which represent the level of implementation that could be realized through specific policies and programs. The nested circles indicate that the achievable and program scenarios are subsets of the technical potential. It is possible that a program scenario may represent a higher level of implementation than the achievable scenario if current implementation of an infrastructure is low in a city.

*Source:* WRI authors.

the magnitude of opportunity and make comparisons across intervention types, and they provide a transferrable knowledge base for integrating local expertise to guide decisions. They are not forecasts or implementation plans but quantifications and spatially explicit visualizations of what could be possible—tools to support evidence-based planning and discussions of priorities and trade-offs.

These methods are designed to be city-agnostic and low-complexity, using globally available datasets to lower barriers for cities with limited analytical capacity while remaining adaptable to local needs and future infrastructure types.

## Technical scenarios

Where is it possible to implement heat-resilient infrastructure, and what levels of coverage can be supported using existing technologies? Technical scenarios represent the maximum implementation of a given intervention based on current surface conditions. For cities that lack basic information about their current infrastructure gaps, this provides a useful benchmark for identifying opportunities and evaluating infrastructure implementation targets.

We define technical scenarios by applying a set of simple rules to an area of interest (AOI), based on spatial data about surface

characteristics. These rules, detailed below in “Methodology,” allow us to estimate the technical potential—how much change is technically possible for each type of infrastructure. For example, the technical potential for trees is the area-wide percentage of tree cover that results from increasing the tree cover of the plantable area to 100 percent.

## Achievable scenarios

While heat-resilience targets should be ambitious enough to affect cooling, they should also be achievable (Keith and Meerow 2022). While technical scenarios are based on what is theoretically possible, achievable scenarios are based on what has already been implemented in parts of the city. This provides a more conservative estimate, grounded in local conditions and capacities.

To define achievable scenarios, we first assess existing levels of infrastructure implementation across the city by computing coverage within a 100 meter (m) grid. These values are then summarized into a statistical distribution, from which we use percentile-based thresholds to establish implementation targets. Achievable scenarios represent the level of coverage that could be attained if all areas reached a benchmark based on the city’s highest-coverage locations. We typically use the 90th percentile of the distribution to capture high-performing areas, but this percentile can be adjusted—for example, when the upper tail reflects atypical conditions, or when practical, ecological, or institutional constraints make the 90th percentile an unrealistic target. Because they are based on local variation within open and globally available datasets, the achievable scenarios reflect context-specific constraints while remaining scalable across geographies and regions without additional local input.

## Program scenarios

Where should heat-resilient infrastructure be placed to meet specific objectives, and how might implementation shift in response to policy goals? Program scenarios describe infrastructure deployment guided by particular policy priorities—such as protecting pedestrians or expanding access to cool public spaces—and illustrate how the city could look if these objectives shaped implementation. Many different program scenarios can be created by varying the constraints placed on infrastructure placement, material properties, and other specifications. These outputs are most useful when the constraints are guided by real-world policy requirements and objectives.

Program scenarios can be evaluated relative to baseline conditions as well as to the technical and achievable scenarios, providing a framework to assess the expected effectiveness of a proposed program. For example, in a given AOI, baseline tree

8 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

cover might be 10 percent, the technical potential 35 percent, the achievable potential 25 percent, and a specific program scenario 22 percent. Comparing these values—and contrasting them with alternative program designs, such as one yielding only 15 percent tree cover—helps cities weigh trade-offs and make informed decisions about which implementation strategies best align with their goals.

Technical and achievable scenarios estimate the *potential* for each type of heat-resilient infrastructure without actually simulating where new infrastructure would be placed. Instead, they use a target—a specified level of implementation, such as “20 percent tree cover”—and calculate how much coverage would result if all suitable areas across the city were brought up to that level. Because these scenarios do not model the location of individual installations, their potentials can be computed as weighted averages based solely on suitable land area and the chosen target.

Program scenarios differ in two ways:

- They simulate implementation spatially to meet a policy or program constraint (e.g., planting trees only along roads, or only within underserved areas).
- Their potentials are derived from the resulting map, not from a simple area × target calculation.

Because of this difference, the resulting potential may differ between scenarios even when the value of the target is the same. For example, consider a program scenario designed to raise street-tree coverage to the same achievable target used in the achievable scenario. In the achievable scenario, the potential tree cover is computed by applying the target percentage uniformly across all plantable area. In the program scenario, however, we apply spacing rules and simulate the actual placement of trees along roads. The resulting map may or may not reach the target exactly, and the program potential is calculated from the simulated outcome rather than from the area-based formula.

## Methodology

### User research

To better understand cities’ needs for long-term adaptation to rising temperatures, we conducted in-depth interviews and workshops with city officials, urban planners, and subject matter experts across our global network of city partners. These included city officials from Monterrey, Mexico; Rio de Janeiro, Brazil; Cape Town, South Africa; Dhaka North, Bangladesh; and Barcelona, Spain. In 2023, we engaged 12 subject matter experts and 40 potential data users; in 2024, this expanded to

27 experts (17 from Arsht-Rock / Atlantic Council, National Observatory of Athens, or the United Nations, and 10 from WRI Africa and India) and 170 potential data users, including engagements with participants at heat-focused workshops and in-person meetings and events. Table 1 lists the cities we engaged.

**Table 1 | Cities engaged in our user research process to understand needs for long-term adaptation to rising temperatures**

|  CONTINENT | COUNTRY | CITY/STATE/COUNTY  |
| --- | --- | --- |
|  **Africa** | South Africa | Cape Town  |
|   |   | Durban  |
|  **Europe** | Spain | Barcelona  |
|   |  The Netherlands | Rotterdam  |
|  **Latin America** | Argentina | Buenos Aires  |
|   |  Brazil | Rio de Janeiro  |
|   |  Mexico | Cancún  |
|   |   | Hermosillo  |
|   |   | Mexico City  |
|   |   | Monterrey  |
|  **North America** | United States | Austin (TX)  |
|   |   | LA County  |
|  **Asia** | Bangladesh | Dhaka North  |
|   |  India | Assam (State)  |
|   |   | Bhopal  |
|   |   | Bihar State  |
|   |   | Chennai  |
|   |   | Delhi  |
|   |   | Hyderabad  |
|   |   | Jaipur  |
|   |   | Kochi  |
|   |   | Mumbai  |
|   |   | Trivandrum  |
|   |   | Udaipur  |
|   | Pakistan | Karachi  |

TECHNICAL NOTE | March 2026 | 9

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

Our research centered on how cities plan and implement cooling interventions and other infrastructural changes to adapt to a warming climate. We were less concerned with short-term response protocols for extreme heat events than with the strategies, decision-making processes, and data needs that shape long-term heat resilience. Interviews followed a semistructured format using prompts such as “What actions has your city taken in the past to mitigate heat risk, and how are you planning future interventions?” or “Which departments or roles are involved in deciding where and how to implement these actions?” Most participating city officials were based in climate or planning departments, often working cross-functionally with agencies such as parks and transportation.

## Code availability

While these methods are presented as documentation for the work of World Resource Institute’s Global Cities Data and Tools Team for use in the Cool Cities Lab, they are also available to any users interested in implementing them independently of our work in Github. These methods are designed specifically for urban applications and produce meaningful insights at both the city scale and when applied to subcity geographies such as neighborhoods or districts.

## OpenUrban land use and land cover mapping

By measuring the types and spatial distribution of urban surfaces, we can establish a baseline understanding of current heat-mitigating and heat-promoting surfaces and begin to map where heat-resilient infrastructure can most usefully be implemented. Cities are made up of surfaces like roads and parking lots, buildings, and vegetated spaces, all of which influence heat and can be modified to reduce temperatures and heat risk. However, most globally available land use and land cover data products have spatial resolutions too coarse (10 m or more) to map small urban features and often use one class to represent all urbanized areas, which is too broad for subcity-level heat mapping. Indeed, our user research highlighted challenges city officials faced that spanned both a lack of relevant datasets and the limited usability of existing ones. In some cases, environmental data existed but were too high-level to guide specific interventions.

A primary objective of this research is to map the locations of these surfaces so that their heat-relevant characteristics can be measured. While some cities have capacity to process and analyze LULC data, many do not, and this greatly inhibits their

Figure 4 | OpenUrban data for Portland, Oregon (United States)

![img-4.jpeg](img-4.jpeg)

Note: The classification for US cities includes roof slope predictions.

Source: WRI authors.

10 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

ability to plan implementation of heat-resilient infrastructure. Additionally, for research purposes or planning at larger scales (regional, state, national), having standard, comparable class definitions available across multiple cities is important.

To address these issues, we created OpenUrban, a high-resolution (1 m) LULC dataset (Figures 4 and 5) with categories designed to be specifically relevant to the implementation of heat-resilient infrastructure (Table 2), validated at 93 percent accuracy in the United States and 83 percent globally (16 cities across eight world regions and a range of city sizes). We chose these LULC categories to map the types of features (roads, parking lots, buildings, water, and public open spaces) that are modifiable for the purposes of heat mitigation. Additionally, we include three generic categories (green space [other], built-up [other], and barren) to fill the gaps between features of interest and ensure continuous coverage over urban areas. We use only free and globally available data—the spatial extent of the datasets covers all land areas worldwide—so that our methods can be implemented for any city, regardless of local data availability. Where available, OpenUrban could be supplemented with higher-resolution or locally sourced data to potentially improve accuracy. The OpenUrban dataset is continually expanding as we add coverage of more cities. These data serve as the foundation for generating scenarios, providing the spatial detail needed to

identify where different forms of heat-resilient infrastructure can realistically be implemented.

Data can be explored further at: https://wri-datalab.earthengine.app/view/open-urban.

### Methods for creating OpenUrban data

To create the dataset, we need reasonably up-to-date information on the features of the urban environment (e.g., roads, parking lots, buildings, and public open spaces) that are modifiable for the purposes of heat mitigation. We source this information from OpenStreetMap (OSM) (OpenStreetMap Contributors 2025) and Overture Maps (Overture Maps Foundation 2025) because they are the most complete, free, regularly updated, and globally available datasets for these features. Additional raster information is incorporated to fill in gaps between features and to classify the types of buildings based on urban land use and roof slope (United States only). All data sources are listed in Table 3.

To create the data, we first create a bounding box around an AOI and buffer it by half a mile (approximately 805 m) to ensure that the data cover the entire area. The buffer ensures that contextual information about the surrounding area is available. The AOI will most often be a city boundary, and urban devel-

Figure 5 | OpenUrban data for Istanbul

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

Green space (other)

Built-up (other)

Barren

Public open space

Water

Parking

Roads

Residential building

Nonresidential building

Source: WRI authors.

TECHNICAL NOTE | March 2026

11

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

Table 2 | OpenUrban LULC category definitions and datasets

|  LULC CATEGORY |   |   | CODE | DEFINITION | SOURCE  |
| --- | --- | --- | --- | --- | --- |
|  Green space (other) |   |   | 110 | Areas not covered by a feature in OSM and classified as tree, shrubland, grassland, or cropland in the ESA WorldCover dataset | ESA WorldCover  |
|  Built-up (other) |   |   | 120 | Areas not covered by a feature in OSM and classified as built-up in the ESA WorldCover dataset |   |
|  Barren |   |   | 130 | Areas not covered by a feature in OSM and classified as bare/sparse vegetation or moss and lichen in the ESA WorldCover dataset |   |
|  Public open space |   |   | 200 | Parks and other public outdoor spaces | OSM, ParkServe (United States only)  |
|  Water |   |   | 300 | Water bodies | OSM  |
|  Parking |   |   | 400 | Parking lots | OSM  |
|  Roads |   |   | 500 | Roads | OSM  |
|  Buildings | Unclassified | Unclassified slope | 600 | Buildings not classified by the WRI Urban Land Use dataset | Overture Maps, WRI Urban Land Use, Global Human Settlement Layer—Average Net Building Height  |
|   |   |  Low-slope | 601 | Low-slope unclassified building  |   |
|   |   |  High-slope | 602 | High-slope unclassified building  |   |
|   |  Residential | Unclassified slope | 610 | Buildings classified as atomistic, informal, formal, or housing project in the WRI Urban Land Use dataset  |   |
|   |   |  Low-slope | 611 | Low-slope residential building*  |   |
|   |   |  High-slope | 612 | High-slope residential building  |   |
|   |  Nonresidential | Unclassified slope | 620 | Buildings classified as nonresidential or open space in the WRI Urban Land Use dataset  |   |
|   |   |  Low-slope | 621 | Low-slope nonresidential building  |   |
|   |   |  High-slope | 622 | High-slope nonresidential building  |   |

Notes: ESA = European Space Agency; LULC = land use and land cover; OSM = OpenStreetMap; WRI = World Resources Institute. The categories highlighted in orange are derived from raster data while the categories highlighted in yellow are feature-based.

* All residential buildings are currently predicted to have high-slope roofs; therefore, the low-slope residential category is not represented in the data. This category is retained to preserve a consistent numerical classification scheme and to avoid ambiguity when interpreting class codes.

opment is seldom limited to this boundary. A grid with tiles measuring 0.15" × 0.15" (approximately 17 × 17 km at the equator) is generated to cover the AOI; only grid cells intersecting the AOI are retained as tile extents. This grid is used to process the data in tiles; the size was chosen as a compromise between processing speed and the number of iterations required.

The OpenUrban dataset is constructed based on urban features. These are discrete polygon representations of physical features in the urban landscape. Many of these come from OpenStreetMap, where each feature is labeled with simple tags made of a key (the category) and a value (the specific type). These tags are referred

to by OSM as keys and values, or key-value pairs, and are required to download the features of interest. We have chosen the most used and relevant categories and category types to define the urban features represented in OpenUrban (Table 4).

For each grid cell, features are downloaded for each of the feature-based LULC categories (public open space, water, roads, buildings, and parking lots) in Table 2 from the specified data source and converted to raster representations of the data. These rasters are then combined and gaps between the features filled with generic classes to create a single output raster of LULC classes.

12

[LOGO]

WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

**Table 3 | Input datasets for OpenUrban**

|  DATASET | ACCESSED THROUGH | DATA TYPE | DATA SOURCE  |
| --- | --- | --- | --- |
|  OpenStreetMap | Overpass API | Vector | Crowd sourced  |
|  Overture Maps Buildings | Python command-line tool | Vector | Combined data from OpenStreetMap Esri Community Maps Instituto Geográfico Nacional (Spain) City of Vancouver (Canada) Google Open Buildings Microsoft Global ML Building Footprints Buildings in East Asian countries  |
|  ParkServe | https://www.tpl.org/park-data-downloads, GEE asset 'projects/wri-datalab/USA_ParkServe_Parks' | Vector | City data or digitized from imagery and Street View  |
|  WRI Urban Land Use | GEE asset 'projects/wri-datalab/cities/urban_land_use/V1' | Raster (5 m) | Derived from Sentinel-2 using machine learning  |
|  Global Human Settlement Layer Average Net Building Height | GEE asset 'projects/wri-datalab/GHSL/GHS-BUILT-H- ANBH_R2023A' | Raster (100 m) | Building heights derived from AW3D30 and SRTM DEMs, refined using Sentinel-2 shadow data  |
|  European Space Agency WorldCover | GEE asset 'ESA/WorldCover/v200' | Raster (10 m) | Derived from Sentinel-1 and Sentinel-2 data using Random Forest classification  |

Notes: API = application programming interface; AW3D30 = ALOS Global Digital Surface Model, three dimensions, 30 meters; GEE = Google Earth Engine; ML = machine learning; SRTM DEM = Shuttle Radar Topography Mission Digital Elevation Model.

## PUBLIC OPEN SPACES, WATER, AND PARKING CLASSES

Public open spaces—parks and other publicly accessible outdoor spaces—are downloaded from OSM using the categories and category types in Table 4. For cities in the United States, we also download features from the ParkServe dataset from the Trust for Public Land (TPL 2025). The public open space polygons from OSM and ParkServe are combined and rasterized to create a 1 m resolution raster mapping the presence and absence of public open spaces. Water bodies and parking lots are treated similarly, downloaded from OSM using their respective categories and tags (Table 4) then rasterized to 1 m to represent the presence and absence of features.

## ROADS CLASS

Road network data are downloaded from OpenStreetMap for each grid cell (Table 4). Because the road data are in the form of road centerlines, the roads need to be converted into road areas to create a raster representation of surface area. To accomplish this, roads are buffered to have a width equal to the number of lanes multiplied by 10 feet (3,048 m), following the National Association of City Transportation Officials guidelines specifying

ing the ideal width of urban road lanes (NACTO 2025). Road features from OSM contain a variable for the number of lanes, but for some this information is missing. To address this, we calculate the average number of lanes per road type using all the road segments in the AOI, rounding the values to the nearest integer. For roads missing the number of lanes, we impute the average number of lanes according to the road type (e.g., primary, secondary). The buffered roads are then rasterized to 1 m.

## BUILDINGS CLASS

Building data are processed using multiple sources and steps. First, building footprints are downloaded from Overture Maps and filtered to contain only valid geometries, which removes any data that are not a polygon. Next the building footprints are classified as residential, nonresidential, or unclassified. This is done by reclassifying the Urban Land Use (ULU) data from World Resources Institute into residential (atomistic, informal subdivision, formal subdivision, housing project), nonresidential (nonresidential), and unclassified (open space) categories. Because the buildings and the ULU are created from different data sources, some buildings may be partially located in

TECHNICAL NOTE | March 2026 | 13

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

**Table 4 | OSM categories and category types used to identify features of interest for the OpenUrban dataset**

|  OPENURBAN CATEGORY | RELEVANT OSM CATEGORY (KEYS) | RELEVANT OSM CATEGORY TYPES (VALUES)  |
| --- | --- | --- |
|  Roads | Highway | Busway, living street, mini roundabout, motorway, motorway junction, motorway link, passing place, primary, primary link, residential, road, secondary, secondary link, service, tertiary, tertiary link, trunk, trunk link, turning circle, turning loop, unclassified  |
|  Public open space | Leisure | Common, disc golf course, dog park, garden, golf course, nature reserve, park, pitch, playground, recreation ground  |
|   | Boundary | Forest, forest compartment, national park, protected area  |
|  Water | Water |   |
|   | Natural | Water  |
|   | Waterway |   |
|  Parking lot | Parking |   |
|   | Amenity | Parking  |

Notes: OSM = OpenStreetMap. OSM categories and category types are referred to as key-value pairs in OSM. Key-value pairs are agreed-upon combinations of tags that describe features in OSM and are used to specify which data to download. This table contains the combinations of categories and tags that select the features we download for each OpenUrban land use and land cover category. "Pitch" is the OSM term for an athletics field.

more than one ULU category, so values are assigned based on maximum coverage per building footprint. For buildings in the United States, we additionally classify the building footprints as low-slope or high-slope (Figure 6). We consider roofs low-slope if they have a pitch of 2/12 or less and high-slope if they have a pitch of greater than 2/12 (ASHRAE 2025).

To predict the slope of buildings, we built a classification tree model using the rpart package in R, based on the average building height, whether the building is in a residential or non-residential area, and the building footprint area. A classification tree works by repeatedly dividing the data into smaller groups, each time splitting the data based on the variable that produces the greatest separation. The result is a tree-like structure that helps make predictions based on a series of simple decisions. In testing, our model accurately predicted roof slope for 84 percent of buildings, demonstrating strong performance given the limited input data.

To collect ground-truth data for the regression tree analysis, we sampled a total of 431 building footprints from 10 cities in the United States that are part of the Cities for Smart Surfaces project (at least 40 each from Atlanta, Boston, Charlotte, Columbia, Dallas, Jacksonville, New Orleans, Phoenix, Portland, and San Antonio). The slopes of these buildings were manually classified as high slope or low slope by examining high-resolution satellite imagery in Google Maps. High-slope buildings are generally considered to have a slope of greater than approximately 16.6°

(2/12) (ASHRAE 2025) (90.1 C402.2), so buildings with any visible slope were classified as high slope. For each building in the sample we extract the average height of the buildings surrounding each building footprint from the average net building height (ANBH, 100 m spatial resolution) from the Global Human Settlement Layer (GHSL) (Pesaresi and Politis 2018), using the mean where a building footprint intersects multiple pixels. Additionally, we calculate the area of each building footprint. The ground truth sampling design was stratified to ensure representative coverage of large and small buildings, areas of tall and short buildings, and residential and nonresidential areas. To build the model we reserved 30 percent of the sampled buildings for testing. The resulting classification tree (Figure 6) has a 0.84 overall accuracy on the testing data. The slope category for each building footprint in US cities is predicted from the ULU category, the ANBH, and the footprint size based on the classification tree model. For buildings classified as residential, the roof-slope classification model most consistently predicts high-slope roofs, independent of building footprint or height. Although some residential buildings (e.g., apartment blocks) have low-slope roofs and misclassifications are inevitable, this assignment represents the most accurate and robust prediction available given the training data. We therefore default residential buildings to the high-slope category in the absence of more detailed information. We include the category in Table 2 to maintain parallel structure and future flexibility. The buildings

14 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

**Figure 6 | Roof slope classification (United States only)**

![img-7.jpeg](img-7.jpeg)

Notes: m = meters; m² = square meters. The roof slope classification is based on the residential/nonresidential classification (urban land use), the average net building height (ANBH) from the Global Human Settlement Layer, and the building footprint area. If a building falls in an area classified as residential, the building is classified as high slope. If a building falls in an area classified as nonresidential and has an area greater than 3,393 m², it is classified as low slope. If a building falls in an area classified as nonresidential and has an area less than 3,393 m², it is classified as high slope if the ANBH is less than 11 m and low slope if the ANBH is greater than 11 m.

Source: WRI authors.

TECHNICAL NOTE | March 2026 | 15

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

are then assigned LULC values according to Table 2 and the data are rasterized to 1 m.

## GENERIC CLASSES

Not all urban land is covered by public open space, water, roads, buildings, and parking lots. To fill the gaps between features and create a continuous raster we use the European Space Agency (ESA) WorldCover data as generic classes. We reclassify the WorldCover data into green space, built-up, and barren according to Table 2. The WorldCover data have a native spatial resolution of 10 m, and we use nearest-neighbor resampling to align it with the 1 m resolution of the feature-based raster layers. While this is sufficient to provide information on nonfeature-based land cover, it introduces uncertainty because 1 m pixels derived from 10 m inputs do not represent true subpixel variation.

Because OpenUrban is a raster dataset there can be no overlapping features. For the final processing step, all raster layers are combined by using the hierarchy of classes in Table 2. A pixel is assigned the highest numerical code from the input raster layers. The pixel values represent the LULC codes and were chosen so that features most likely to appear on top on the ground (e.g., roads over water bodies, buildings within parks) have higher values and so are retained in the final OpenUrban data layer. The three background WorldCover categories have the lowest values and so only occur in the OpenUrban dataset when no other features are present. The completed OpenUrban raster layer is saved as a Google Engine Asset for further analysis. We also maintain the vector data used to generate each feature raster for use in subsequent methods.

## Validation

The OpenUrban dataset was validated using a stratified random point sampling approach to ensure an unbiased and representative assessment of land cover classification accuracy across US and global cities. Sampling was designed to prioritize land cover types most relevant to heat-resilient infrastructure—buildings, roads, parking lots, and public open spaces—while still capturing variation across geography, urban form, and land cover heterogeneity.

In the United States, validation was conducted across the 10 Cities for Smart Surfaces partners (Atlanta, Boston, Charlotte, Columbia, Dallas, Jacksonville, New Orleans, Phoenix, Portland, and San Antonio). Across these 10 US cities, 2,505 sample points were allocated proportionally based on each city's total area. City boundaries were defined using the 2020 US Census, and urban core versus periphery regions were delineated using the Global Human Settlement Layer. The core was defined as contiguous pixels classified as Urban Center pixels sharing

common edges (not corners), while the remaining urban pixels were classified as periphery. Within each region, 70 percent of the samples were evenly divided among four priority classes: roads, high-slope buildings, low-slope buildings, and parking lots (each receiving 17.5 percent), while the remaining 30 percent of samples were randomly assigned to the remaining LULC categories.

While the US-based validation was designed to meet reporting needs for specifically examining various categories of urban features, we also conducted a global validation to assess how the OpenUrban dataset performs in diverse international contexts. This broader effort was motivated by interest in expanding the dataset's use for global applications in urban heat resilience planning. To ensure a robust global validation, we selected 16 cities from the Atlas of Urban Expansion (NYU et al. 2016) to represent all eight world regions as defined in the atlas, and a range of city sizes (small to mega, based on population thresholds used in the atlas). We generated OpenUrban data for each city using the connected GHSL pixels classified as Urban Center around a central coordinate for each city. Each region was allocated at least 1,000 total sample points, which were split between two cities based on their relative size category. For example, if one region contained a size 3 city and a size 2 city (as defined by the atlas), the total regional weight was 5, and sample allocation followed a 60/40 split (i.e., 600 and 400 points, respectively). Within each city, 80 percent of samples were assigned equally among points belonging to four priority classes: roads, buildings, parking lots, and public open space (each receiving 20 percent). The remaining 20 percent were evenly divided among the secondary classes: green space (other), built-up (other), barren, and water (each receiving 5 percent).

Sampling points were selected randomly using Google Earth Engine, constrained to pixels within each land cover class and exported for manual interpretation in the Quantum Geographic Information System (QGIS) using high-resolution imagery. Each sample consisted of a point and was cross-referenced in QGIS using high-resolution satellite imagery from multiple basemaps to determine the ground-truth classification at that point. Results were evaluated in R, using confusion matrices to calculate overall, producer's, and user's accuracy.

Across the United States, buildings were classified with near-perfect accuracy (99 percent producer's, 100 percent user's), and road and parking lot classifications were also high (over 90 percent for both metrics). Roof slope classification—essential for identifying cool roof potential—achieved 93 percent accuracy, with slightly better performance in peripheral areas than urban cores. A combined "other" category of green space (other), built-up (other), barren, and public open space achieved

16 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

**Table 5 | Accuracy assessment of OpenUrban for US cities**

|  CITY | STATE | TOTAL SAMPLES | OVERALL ACCURACY  |
| --- | --- | --- | --- |
|  Atlanta | GA | 611 | 0.90  |
|  Boston | MA-NH | 422 | 0.92  |
|  Charlotte | NC-SC | 166 | 0.93  |
|  Columbia | SC | 94 | 0.93  |
|  Dallas–Fort Worth–Arlington | TX | 434 | 0.96  |
|  Jacksonville | FL | 161 | 0.96  |
|  New Orleans | LA | 66 | 0.92  |
|  Phoenix-Mesa-Scottsdale | AZ | 272 | 0.93  |
|  Portland | OR-WA | 128 | 0.98  |
|  San Antonio | TX | 150 | 0.94  |

**Table 6 | Accuracy assessment of OpenUrban for global cities**

|  CITY | COUNTRY | REGION | SIZE CATEGORY | SAMPLE COUNT | OVERALL ACCURACY  |
| --- | --- | --- | --- | --- | --- |
|  Sydney | Australia | East Asia and Pacific | 3 | 600 | 0.87  |
|  Ulaanbaatar | Mongolia | East Asia and Pacific | 2 | 401 | 0.80  |
|  Palermo | Italy | Europe | 2 | 401 | 0.87  |
|  Warsaw | Poland | Europe | 3 | 600 | 0.86  |
|  Cabimas | Venezuela | Latin America and Caribbean | 1 | 199 | 0.90  |
|  São Paulo | Brazil | Latin America and Caribbean | 4 | 802 | 0.84  |
|  Atlanta | United States | North America | 4 | 669 | 0.83  |
|  Hermosillo | Mexico | North America | 2 | 335 | 0.86  |
|  Bhopal | India | South and Central Asia | 3 | 527 | 0.74  |
|  Tashkent | Uzbekistan | South and Central Asia | 3 | 502 | 0.82  |
|  Cần Thơ | Vietnam | Southeast Asia | 1 | 199 | 0.76  |
|  Manila | Philippines | Southeast Asia | 4 | 802 | 0.81  |
|  Cape Town | South Africa | Sub-Saharan Africa | 3 | 752 | 0.86  |
|  Nakuru | Kenya | Sub-Saharan Africa | 1 | 253 | 0.88  |
|  Malatya | Turkey | Western Asia and North Africa | 1 | 335 | 0.81  |
|  Marrakesh | Morocco | Western Asia and North Africa | 2 | 666 | 0.85  |

Note: Size categories from the Atlas of Urban Expansion are small (1), medium (2), large (3), and mega (4).

TECHNICAL NOTE | March 2026 | 17

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

Table 7 | Comparison of overall accuracy of different land cover datasets

|  DATASET | COVERAGE | SPATIAL RESOLUTION (M) | ACCURACY  |
| --- | --- | --- | --- |
|  OpenUrban | United States | 1 | 0.93  |
|  UrbanWatch | United States | 1 | 0.92  |
|  OpenUrban | Global | 1 | 0.83  |
|  WorldCover | Global | 10 | 0.77  |
|  DynamicWorld | Global | 10 | 0.74  |
|  Esri Landcover | Global | 10 | 0.85  |
|  GlobeLand30 | Global | 30 | 0.80  |
|  MODIS Landcover Type v6.1 | Global | 500 | 0.75  |

Notes: m = meters; MODIS = Moderate Resolution Imaging Spectroradiometer.

an accuracy of 91 percent (both metrics). Overall, the four categories of buildings (exclusive of slope), roads, parking lots, and other were classified at 93 percent accuracy (Table 5). Every city had an overall accuracy exceeding the generally accepted 85 percent accuracy standard for reliable land cover datasets (Strahler et al. 2006).

Globally, the dataset performed slightly less consistently, with an overall accuracy of 83 percent (Table 6). All priority classes (roads, buildings, parking lots, and public open space) exceeded 80 percent accuracy in both producer and user metrics, indicating strong reliability for features related to heat-resilient planning. However, some regional and class-specific challenges were observed. Cities in Sub-Saharan Africa and Latin America achieved the highest accuracy ( \( \geq \)  86 percent), while South and Southeast Asian cities showed lower performance (78–80 percent). Accuracy was relatively consistent across city size categories, though large cities and megacities showed slightly lower performance than smaller ones.

Compared to other globally available land cover datasets (Table 7), OpenUrban demonstrates strong overall accuracy. While global land cover products differ in spatial resolution and class structure, OpenUrban's combination of high accuracy, fine spatial resolution, and detailed urban class taxonomy distinguishes it from coarser datasets that represent urban areas with a single built class. In particular, OpenUrban provides 10 urban land-use classes at high resolution, making it well suited for city planning applications and analyses that require detailed representations of urban form.

### Heat-relevant surface characteristics

Understanding how urban surfaces contribute to or mitigate heat requires mapping their physical characteristics—here, we measure their tree cover, reflectivity (albedo), vegetation cover, shading cover, and surface temperature. Each of these surface characteristics plays a distinct role in urban heat dynamics and is derived using different remote sensing datasets and processing methods. In this subsection, we describe how we calculate each characteristic, beginning with tree cover, derived from high-resolution tree height data; followed by albedo and fractional vegetation cover, both derived from Sentinel-2 imagery; land surface temperature from Landsat 8; and shade cover, modeled from 3D surface and feature data (Table 8). Together, these datasets establish a spatially explicit baseline of urban surface condition that serves as a foundation for generating infrastructure implementation scenarios and evaluating how such interventions may modify heat-relevant characteristics. While fractional vegetation cover and land surface temperature are not yet incorporated into the heat-resilient infrastructure scenarios presented in this technical note, they are included here because they provide valuable contributions to the spatial baselining of heat-relevant surface characteristics and are anticipated to support future analyses.

#### Tree cover

Tree cover is mapped from the High-Resolution Canopy Height Maps produced by WRI and Meta (Tolan et al. 2024), which provide global estimates of canopy height at 1 m resolution. Tolan et al. (2024) report an average mean absolute error of 2.8 m and a mean error of 0.6 m to summarize continuous height prediction performance and user's and producer's accuracies of

18

[Non-Text]

WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

Table 8 | Input datasets for measuring surface characteristics

|  DATASET | CITATION | ACCESSED THROUGH  |
| --- | --- | --- |
|  High Resolution Canopy Height Maps by WRI and Meta | Tolan et al. 2024 | GEE asset, "projects/meta-forest-monitoring-okw37/assets/CanopyHeight"  |
|  Sentinel-2 | European Space Agency 2017 | GEE asset, "COPERNICUS/S2_SR_HARMONIZED"  |
|  Cloud Score + | Pasquarella et al. 2023 | GEE asset, "GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED"  |
|  Dynamic World | Brown et al. 2022 | GEE asset, "GOOGLE/DYNAMICWORLD/V1"  |
|  Landsat 8 | USGS 2021 | GEE asset, "LANDSAT/LC08/C02/T1_L2"  |

Note: GEE = Google Earth Engine.

approximately 0.88 and 0.82, respectively, for distinguishing tree presence or absence based on a canopy height threshold of 1 m.

To distinguish trees from shrubs and other low-lying woody vegetation, we apply a canopy height threshold of 3 m. This threshold is based on Potapov et al. (2021), who use this definition to delineate tree canopy in global mapping efforts. Defining a minimum height is necessary to ensure that we are capturing the structural characteristics of trees—namely, their ability to provide overhead shade and influence microclimate through transpiration and canopy interception—rather than including shorter vegetation that does not provide the same heat-mitigation benefits. This 3 m definition has also been confirmed through private correspondence with David Nowak of the US Forest Service as a reasonable and widely accepted threshold for distinguishing trees in urban forest analyses. Here, we map each 1 m pixel as the presence or absence of tree cover ( \( \geq \)  3 m height).

### Albedo

Albedo, or solar reflectance, is the fraction of incoming sunlight reflected by a surface. Higher-albedo surfaces absorb less solar radiation, reducing surface temperatures and contributing to urban cooling. We calculate albedo using imagery from the Sentinel-2 satellite.

First, we filter Sentinel-2 data to include only summer months—June, July, and August for the Northern Hemisphere; December, January, and February for the Southern Hemisphere—for the year of interest. This seasonal selection captures periods of high sun angles and relatively consistent illumination, which reduces shadowing and improves the accuracy of surface

reflectance estimates. These months were used consistently across all cities, including those in the tropics. While tropical regions experience relatively stable sun angles year-round (with the sun remaining within  \( 23^{\circ} \)  of zenith at noon), the summer months still offer reduced shadowing, and near the equator shadowing does not differ greatly between seasons, making them suitable for estimating surface reflectance. Sentinel-2 collects imagery at approximately 10:30 a.m. local time, which is close to, but slightly before, the daily solar zenith. Shadows are important to minimize because shaded surfaces appear darker and can artificially lower estimated albedo values. While we model shade explicitly elsewhere in this technical note, here we are only concerned with shadows as a source of error in satellite-based reflectance estimates.

Albedo ( \( \alpha \) ) is calculated from the blue, green, and red visible (B2, B3, B4), near infrared (NIR, B8), and shortwave infrared (SWIR, B11, B12) bands using the narrow-to-broadband conversion coefficients presented in Bonafoni and Sekertekin (2020) using the following equation:

\[
\alpha = B 2 \times 0. 2 2 6 6 + B 3 \times 0. 1 2 3 6 + B 4 \times 0. 1 5 7 3 + B 8 \times 0. 3 4 1 7 + B 1 1 \times 0. 1 1 7 0 + B 1 2 \times 0. 0 3 3 8
\]

In this process the SWIR bands (20 m resolution) are bilinearly resampled to match the spatial resolution of the visible bands (10 m). For each pixel, we compute the median albedo value across all available cloud-free summer images from the year of interest. Using the median instead of the mean helps suppress the influence of outliers caused by residual cloud contamination, glare, or shadows. The resulting albedo maps represent the typical summertime reflectivity of urban surfaces at 10 m resolution.

TECHNICAL NOTE | March 2026

19

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

## Fractional vegetation

In addition to trees, other forms of vegetation like grasses and shrubs also influence urban heat, and satellite remote sensing can provide us with information about the abundance of vegetated surfaces. The normalized difference vegetation index (NDVI) is the most common vegetation index; while used in many studies as a proxy for the relative abundance of vegetation, it is not a measure of physical quantity but rather a dimensionless measure of the overall health of photosynthetically active vegetation ranging from -1 to 1 (Carlson and Ripley 1997). A better approach for estimating the relative abundance of vegetation in remote sensing imagery is to scale vegetation indices by the index values associated with the presence and absence of vegetation—this effectively bounds the vegetation index between zero vegetation cover and 100 percent vegetation cover (Gillies and Carlson 1995). By scaling NDVI we can obtain a physically meaningful estimate of the fractional cover of vegetation within a pixel.

While there are many methods for doing so, the quadratic method proposed by Gillies and Carlson (1995) and refined by Carlson and Ripley (1997) is a well-respected approach that outperforms many other types of algorithms in terms of being robust to both soil noise and scale effects (Gao et al. 2020). As given in Carlson and Ripley (1997), the pixel-wise fraction vegetation (Fr) of an image is calculated as

$$Fr = \left( \frac{NDVI - NDVI_0}{NDVI_{veg} - NDVI_0} \right)^2$$

where NDVI is the pixel value of NDVI, $NDVI_0$ is the NDVI of a pixel without any vegetation, and $NDVI_{veg}$ is the NDVI of a fully vegetated pixel. NDVI is calculated as

$$NDVI = \frac{NIR - Red}{NIR + Red}$$

Where NIR and Red are the pixel values of the near infrared (NIR) and red bands, respectively.

However, a major problem with this method is the establishment of values for $NDVI_0$ and $NDVI_{veg}$. While many studies use invariant values, this is questionable given a large geographic area because neither the NDVI of bare soil nor that of vegetation is constant in space and time. In particular, $NDVI_{veg}$ varies with both species and phenology (spatially variable), as well as vegetation health (temporally variable) (Gao et al. 2020). Using values of $NDVI_0$ and $NDVI_{veg}$ derived from a climatically different location or year—for example, an arid location versus

a tropical location, or a drought year versus a year with typical rainfall—can systematically bias the Fr estimates by misrepresenting true vegetation health and soil moisture conditions. For estimating Fr for cities around the globe that represent a range of ecoregions, we must derive these values both per city and per year.

Zeng et al. (2000) present methods for doing so, using the distributions of NDVI values within land use and land cover categories, including 13 categories of vegetation. They first take the maximum annual NDVI value per pixel and then use the distribution of $NDVI_{max}$ per land cover category to estimate the values of $NDVI_0$ and $NDVI_{veg}$. By manually estimating the fractional vegetation from high-resolution satellite imagery over the United States and Western Europe, Zeng et al. (2000) determined that the 5th percentile of NDVI values for barren land is appropriate for estimating $NDVI_0$ and that the 75th percentile of NDVI values for vegetated land is appropriate for estimating $NDVI_{veg}$ for all but one of the vegetated classes.

Gao et al. (2020) identify two primary issues with this approach that are relevant to our work:

1. There may be a temporal or spatial mismatch between the remotely sensed data and the LULC data.
2. A full year of data is required from the same satellite sensor.

To address these issues, we obtain LULC types from the Dynamic World dataset—a near-real-time global dataset that probabilistically maps nine land cover types derived from Sentinel-2—and estimate NDVI from Sentinel-2 imagery. Both datasets are available from June 27, 2015, to the present, with a revisit time of every two to five days (beginning in 2018) ensuring ample data availability.

We make four main changes to the methods from Zeng et al. (2000). First, we estimate the values of $NDVI_0$ and $NDVI_{veg}$ on a per city basis. Second, we use the 90th percentile of NDVI values per pixel instead of the maximum to exclude outliers while representing peak vegetation characteristics. Third, we estimate the value for $NDVI_0$ from the urban built-up class rather than the barren class of the LULC data as this is a more appropriate approach for estimating the NDVI of nonvegetated pixels in urban areas, and barren land cover may not be present in all (Gillies and Carlson 1995). And fourth, instead of estimating $NDVI_{veg}$ separately for each vegetation type, we use only the trees, grass, and shrub and scrub LULC classes from Dynamic World and combine them into one vegetated class because the within-city variation of vegetation is unlikely to vary at the pixel scale with the same magnitude as the variation between vegetated classes at the global scale.

20 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

**Table 9 | DynamicWorld LULC categories are recategorized to estimate $NDVI_o$ (built-up) and $NDVI_{veg}$ (vegetated)**

|  LULC CLASS | NDVI CATEGORY  |
| --- | --- |
|  Grass | Vegetated  |
|  Trees | Vegetated  |
|  Shrub and scrub | Vegetated  |
|  Built-up | Built-up  |
|  Water | Other  |
|  Flooded vegetation | Other  |
|  Crops | Other  |
|  Bare | Other  |
|  Snow and ice | Other  |

To calculate the Fr for a city, we first calculate the values of $NDVI_o$ and $NDVI_{veg}$ in Google Earth Engine. For an AOI, in this case a city boundary, the Sentinel-2 data are filtered to only images covering the AOI for the summer months in the year of interest. The images are then cloud-masked using the Cloud Score + dataset and a clear threshold of 0.60. For each image, NDVI is calculated per 10 m pixel, and then for each pixel the 75th percentile NDVI value across all summer images is selected to produce a single mosaicked image. The Dynamic World data are also filtered to only images covering the AOI for the summer months in the year of interest, and a mosaic is created by taking the most frequently occurring class of each pixel. The pixels are then recategorized into vegetated, built-up, and other (Table 9). $NDVI_o$ is estimated as the 5th percentile value of the distribution of built-up pixels and $NDVI_{veg}$ is estimated as the 75th percentile value of the distribution of vegetated pixels. These values are then used to calculate Fr for each pixel from the mosaicked maximum pixel-wise NDVI image.

## Shade

Shade is more challenging to measure than the other surface characteristics, which are easily derived using freely available satellite imagery. Shade cover changes throughout the day and year. Mapping shade requires three-dimensional data on objects that cast shadows, notably buildings and trees in urban areas but also terrain. While the WRI-Meta tree canopy data provide reasonably accurate tree heights (mean error 0.6 m), there is no single,

standard high-resolution, globally available building height dataset, and the best available global building footprint data do not contain heights for all buildings. Our team has developed methods to combine globally available building height data from UT-GLOBUS (Kamath et al. 2024) with global building footprint data from Overture Maps to estimate building heights, data then combined with the global FABDEM (Forest and Buildings Digital Elevation Model) (Hawker et al. 2022) to create a digital surface model (Engel et al. 2026).

Shade is calculated using the SOLWEIG (solar and longwave environmental irradiance geometry) model from the Urban Multi-scale Environmental Predictor tool (Lindberg et al. 2020). Because shadow mapping is integrated into the thermal comfort modeling process, we calculate both shadows and access to shade on the same day we model thermal comfort—specifically, the hottest day in the past five years for each city. This date is determined by analyzing daily average temperatures from the Copernicus ERA5-Land Daily reanalysis dataset, which provides global coverage at 0.25-degree spatial resolution (approximately 28 km at the equator) (Hersbach et al. 2020). We identify the hottest day by selecting the date with the highest average temperature over that period. We produce 1 m resolution maps identifying areas of no shade, tree shade, and building shade for each time of day for which we run the model (12 p.m., 3 p.m., 6 p.m.). In areas where building and tree shade overlap, we identify shadows as building shade because of its more robust coverage. The shade maps show agreement of 0.814 between the observed shade and the expected shade when validated against LiDAR (light detection and ranging)-derived shade maps and perform highest in areas with no shade (Engel et al. 2026). See Engel et al. (2026) for more details on the data and methods for modeling shade.

The spatial distribution of shade changes throughout the day with the position of the sun: 12 p.m. represents the time of least shade, 3 p.m. corresponds to the period of peak heat exposure, and 6 p.m. captures the longer shadows of the early evening. While shade patterns vary slightly from day to day, we model shade on the hottest day in the past five years because it provides a realistic representation of extreme heat conditions—those most relevant to public health and urban cooling interventions. Although this day may not capture the full range of summer-time solar angles, future hottest days are likely to be proximal in time and have similar solar conditions. Because our goal is to assess shade as a mitigating resource during periods of highest heat exposure, prioritizing shade on the hottest day supports decision-making focused on thermal resilience.

TECHNICAL NOTE | March 2026 | 21

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

## Land surface temperature

Land surface temperature (LST) was calculated from the surface temperature band (ST_B10) of Landsat 8 Collection 2 data. To generate representative LST composites, we first defined the hot season for each city as the three-month period centered on the hottest day from the last five years based on ERA5 reanalysis data, as described in “Shade” above. Restricting analysis to this period ensures that the resulting composites reflect conditions most relevant for heat exposure.

For each Landsat scene within the hot season, cloudy pixels were masked using the associated quality assessment band, after which the data were scaled and converted from Kelvin to degrees Celsius. To mitigate gaps resulting from Landsat’s eight-day revisit cycle and frequent cloud contamination, we combine imagery from the three most recent complete hot seasons for each area of interest and compute the pixel-wise 95th percentile of clear-sky LST values. This percentile-based compositing approach emphasizes consistently hot, cloud-free conditions while reducing sensitivity to single-day extremes. The resulting composites provide LST at a nominal spatial resolution of 30 m. However, because the thermal band is natively acquired at 100 m resolution and only downscaled by the US Geological Survey to match the reflective bands, the effective resolution of the LST product is closer to 100 m. Users should therefore interpret LST values as representing the surface-energy balance over approximately a 100 m area.

## Metrics

When we have data on both the surface types (see “OpenUrban land use and land cover mapping” above) and the surface characteristics (“Heat-relevant surface characteristics”), we know the locally specific makeup of the major contributing factors to the urban heat island in the city. Combing the two provides us with baseline data on heat-resilient (and heat-promoting) infrastructure as well as a starting point for assessing options for locally specific solutions.

## Zonal statistics

Zonal statistics are summary metrics—such as mean, median, or percentage cover—calculated for defined geographic areas or zones. The surface characteristic maps allow us to quantify baseline conditions relevant to heat resilience by calculating zonal statistics for both entire areas of interest and specific land use and land cover classes. For example, we calculate the overall percentage tree cover of an AOI, as well as the percentage of tree cover specifically over roads, buildings, parking lots, or public open spaces. These different types of zonal statistics offer complementary insights: citywide or AOI-level sum-

summaries help track broad progress or compare neighborhoods, while LULC-specific summaries reveal where particular types of surfaces—like roads or rooftops—lack vegetation, shade, or reflectivity. This information supports both strategic prioritization of interventions and a better understanding of how existing surface characteristics contribute to urban heat patterns.

## Proximity

Proximity metrics provide critical insights into access to heat-mitigating infrastructure—especially shade and vegetation—by measuring how close different areas are to these features. While zonal statistics summarize what is present within a given zone, proximity focuses on spatial relationships: how far people or places are from beneficial surface characteristics.

In our analysis, we can calculate Euclidean distance from each pixel to the nearest pixel that meets a defined threshold of a desired surface characteristic—such as tree cover, shade, or vegetation. These metrics can be calculated for the entire area of interest or filtered by LULC class to focus on specific surface types like roads, buildings, or parks. For example, we measure the distance from each public open space pixel to the nearest area of shade cover to quantify access to shade in parks.

Proximity is especially valuable in understanding equity of access to cooling infrastructure. Even if tree cover or shade exists in a city, it may not be equitably distributed—large gaps in proximity can leave some neighborhoods more exposed to heat. By quantifying these spatial gaps, cities can identify underserved areas, set meaningful goals (e.g., reducing maximum distance to shade), and prioritize infrastructure investments that improve accessibility. In combination with other metrics, proximity supports a more human-centered understanding of urban heat resilience.

## Opportunity

Beyond measuring existing heat-relevant conditions, cities benefit from understanding where meaningful improvements are possible. Opportunity metrics translate surface characteristics into spatially explicit estimates of the potential for additional cooling infrastructure—revealing where the greatest increases in tree canopy, rooftop reflectivity, or other interventions are possible (Figure 7). Opportunity metrics quantify the gains that can be achieved within the constraints of current land-use patterns and surface characteristics.

Opportunity layers are generated using the WorldPop (2023) 100 m grid, ensuring consistent spatial units across cities. For each grid cell, we compare existing conditions to what could be achieved if areas available for implementation met locally derived or technology-based targets for infrastructure coverage.

22 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

Figure 7 | Tree (left) and cool roof (right) opportunity in Cape Town, South Africa

![img-8.jpeg](img-8.jpeg)

Tree cover increase

![img-9.jpeg](img-9.jpeg)

![img-10.jpeg](img-10.jpeg)

Albedo increase

![img-11.jpeg](img-11.jpeg)

Note: The overall opportunity for trees is an increase of 5.7% tree cover, while the overall opportunity for cool roofs is an increase of 10% reflectivity (0.10 albedo).

Source: WRI authors.

The difference between the possible value and current value represents the opportunity for that location. These layers help cities identify high-impact zones, compare intervention types, and align planning efforts around where the greatest benefits of heat-resilient infrastructure could be realized. These metrics complement the baseline and scenario analyses by offering a consistent and transferable way to identify areas of potential that may warrant priority attention in planning, policy development, and investment.

### TREE OPPORTUNITY

Identifying where cities can most effectively expand urban canopy requires understanding not only where tree cover is currently low but also where tree planting is physically feasible. The tree opportunity metric captures this by estimating the potential increase in canopy cover that would result if all plantable LULC classes were brought to their achievable potential. This provides a spatially explicit indicator of where meaningful canopy gains are possible, supporting prioritization across diverse urban surfaces.

We consider green space (other), built-up (other), barren, public open space, and parking to be plantable areas. Additionally, we consider the road right-of-way as a separate plantable class. We estimate the road right-of-way as the 5 m adjacent to roads that is not road, water, or buildings. Achievable targets are derived

from the statistical distribution of existing tree cover within each plantable OpenUrban LULC class across the urban area.

Within each grid cell, we calculate the existing percentage tree cover of each plantable LULC class and use class-specific percentile thresholds to define realistic—but ambitious—targets. These thresholds are selected to reflect cities' differing levels of flexibility to influence tree canopy across land-use types. For green space (other), built-up (other), barren, and parking, where change is typically more constrained, these thresholds were selected empirically based on examination of canopy-cover distributions across cities and represent the central tendency of the distribution of tree cover. Barren, built-up (other), and parking areas are assigned lower targets (30th percentile), and green space (other) a moderate target (50th percentile). Public open space and road rights-of-way, which are often directly managed by cities and where tree-planting programs can exert greater influence, are assigned higher targets (90th percentile).

To compute tree opportunity, we calculate the following for each grid cell:

1. Existing tree canopy cover of each plantable LULC class.
2. Total plantable area per class (all land not currently covered by tree canopy).
3. Total land area per grid cell (excluding water).

TECHNICAL NOTE | March 2026

23

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

Canopy targets are then applied to each class, and the potential canopy gain is estimated as

$$\text{Canopy gain} = \text{Plantable area} \times (\text{Target tree cover \%} - \text{Existing tree cover \%})$$

If existing canopy exceeds the target for a class, the increase is set to zero. Class-level increases are then summed within each 100 m cell and the tree opportunity is expressed as a percentage of total land area:

$$\text{Tree opportunity} = \frac{\text{Canopy gain}}{\text{Total land area}}$$

This produces a tree opportunity layer that highlights where canopy expansion is both feasible and impactful.

## COOL ROOF OPPORTUNITY

The roof opportunity metric quantifies the potential increase in area-wide albedo that could be realized if all rooftops were brought to technically feasible reflectivity levels. This metric provides a spatially explicit estimate of gains from cool roof implementation and highlights where the greatest reflectivity improvements are possible.

For each 100 m grid cell, we first compute the baseline mean surface albedo using all pixels within the cell. We then compute the mean albedo of roof pixels identified using the OpenUrban dataset; in the United States, mean roof albedo is calculated separately for low-slope and high-slope roofs.

For cities with roof-slope classification, low-slope roofs are assigned a target albedo of 0.62 and high-slope roofs a target albedo of 0.28, unless the existing mean albedo already exceeds these values. These targets are derived from widely available cool roofing materials (Table 11). For cities without roof-slope classification, cool roof opportunity is estimated by increasing the mean roof albedo in each grid cell to a target reflectivity of 0.62, unless the existing mean roof albedo already exceeds this value. This assumption may overestimate potential albedo increases in cities with a substantial share of high-slope roofs. See “Cool roofs” in “Methodology” for further discussion.

The resulting change in roof albedo is then translated into a grid-cell-level albedo change by computing an area-weighted average, using the fraction of the grid cell covered by roof pixels. This yields the potential increase in mean surface albedo for each grid cell under full adoption of cool roof materials:

$$\text{Potential gridcell albedo} = \frac{\text{Baseline gridcell albedo} + \text{Roof area fraction} \times (\text{Target roof albedo} - \text{Baseline roof albedo})}{\text{Target roof albedo} - \text{Baseline roof albedo}}$$

$$\text{Cool roof opportunity} = \text{Potential gridcell albedo} - \text{Baseline gridcell albedo}$$

Mapped across the urban area, the roof opportunity layer identifies

- where large clusters of dark roofs could provide significant reflectivity gains,
- areas where cool roof adoption would produce the greatest area-weighted impact, and
- regions that may be strategic targets for policy interventions, incentive programs, or voluntary campaigns.

## Heat-resilient infrastructure scenarios

Here we present methods for defining scenarios for heat-resilient infrastructure. We focus on four interventions: trees, cool roofs, reflective pavements, and nontree shade structures. Many other strategies, such as green roofs or permeable pavements, are also relevant—while not detailed here, similar methods can be applied to estimate their potential.

We define three types of scenarios—technical, achievable, and program (see “Heat-resilient infrastructure potential” in the introduction for more details). Technical scenarios represent the maximum feasible implementation given current land use and land cover; achievable scenarios define a realistic upper bound target based on the highest levels of existing implementation within some neighborhoods in a city; and program scenarios represent outcomes under specific policies or planning objectives. Together, these scenarios provide the framework for quantifying and generating maps of infrastructure implementation scenarios that illustrate how different strategies could be deployed across an area of interest—from small districts to entire cities. For citywide analyses, we use the urban extents developed by Angel et al. (2024) as AOIs.

The parameters used to quantify technical, achievable, and program scenarios may be adjusted when implementing these methods to reflect a city’s specific context and goals. These parameters control both the amount and placement of infrastructure in each scenario, and adjusting them produces different maps and potentials. Key variables include the priority LULC type (e.g., roads or public open spaces for tree planting), the area (e.g., large vs. small buildings for cool roofs), the distance (e.g., maximum spacing between shaded areas), and the level of implementation (e.g., high or low percentage shade coverage). The parameters for the technical scenarios determine what constraints define maximum coverage. The parameters for the achievable scenarios determine how the achievable target is drawn from the distribution of existing conditions—whether the achievable scenarios are defined by high implementation conditions or if they reflect more average conditions. The parameters

24 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

for the program scenarios specify the rules and priorities for simulating particular policies or plans.

The values for each parameter described in the rest of this technical note are defaults drawn from the literature and our expert judgment that can be adjusted when implementing these methods to respond to particular research needs or local contexts. Changing parameter values will alter the results of the analysis, but the underlying methods remain the same.

Though these methods provide indicators and maps assuming full implementation of a scenario, they do not model the timing of implementation. In practice, infrastructure is installed incrementally, and cities may wish to model progress over time. While we do not explicitly include a temporal dimension, rough estimates can provide a minimum timeline for full implementation under typical conditions:

- ■ **Urban trees** deliver limited benefits in the early years after planting, with meaningful cooling often beginning after 10–20 years and maximum benefits typically reached around 30 years, when mature canopy cover is achieved (Li et al. 2023).

- ■ **Cool roofs** are installed as part of the normal roof replacement cycle, which averages 15–25 years. This means about 5 percent of roofs are replaced annually, so a cool roof policy could reach 50 percent of the building stock within 10 years and near-complete coverage in 20 years (Alhazmi et al. 2023).
- ■ **Reflective pavements**—particularly coatings and sealants—can be deployed much faster. As categorized by the Heat Action Platform, these are considered short-term interventions, with typical implementation timelines of one to two years at the project scale, though citywide rollout may take longer depending on resources and road network size (Arsht-Rockefeller Foundation 2023).
- ■ **Shade structures** offer immediate cooling once installed. Temporary structures such as shade sails can be deployed in a single day, while permanent structures may require permitting and construction time. Broad-scale implementation may take several years depending on program scope and capacity.

Figure 8 | Area of interest in Cape Town, South Africa

![img-12.jpeg](img-12.jpeg)

Note: A satellite basemap is shown on the left and the OpenUrban data (with building categories combined) are shown on the right.

Source: WRI authors.

TECHNICAL NOTE | March 2026 | 25

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

**Table 10 | Summary of potentials for the Cape Town AOI scenarios**

|  INFRASTRUCTURE | BASELINE | TECHNICAL | ACHIEVABLE |  | PROGRAM  |
| --- | --- | --- | --- | --- | --- |
|  Street trees (% tree cover) | 4.8% | 14.1% | 6.7% | Street trees achievable | 9.5%  |
|  Park trees (% tree cover) | 4.8% | 5.2% | 4.9% | Park trees achievable | 4.9%  |
|  Cool roofs (% reflectivity) | 20.4 | 31.4 | 21.7 | Large buildings | 21.7  |
|   |  |  |  | All buildings | 31.1  |
|  Reflective pavements (% reflectivity) | 20.4 | 21.4 | 20.7 | Low-traffic-volume roads | 21.4  |
|  Shade structures (% shade) | 26.9 | 31.4 | 27.1 | All parks | 27.0  |

Except for trees, all infrastructure types presented here deliver immediate cooling benefits upon installation, although trees offer limited near-term effects through evapotranspiration and other co-benefits (see “Green surfaces” in the introduction). These rough time frames can help cities interpret the results of the potential maps in relation to near- or long-term planning horizons.

In addition to detailing methods for defining the technical and achievable scenarios and calculating their potentials for each intervention type—cool roofs, reflective pavements, tree canopy, and shade structures—we present, for each, a default program scenario and the corresponding potential and scenario map. These scenarios were developed based on input from city stakeholders (see “User research” in the next subsection) and are the scenarios offered in the Cool Cities Lab:

- Tree planting on all nonhighway roads to match the highest existing level of street-tree coverage in the city
- Large roofs upgraded to the albedo of available cool roofing technology levels
- Low-traffic-volume roads upgraded to the albedo of available reflective pavement technology levels
- Shade cover in parks increased to match minimum target levels

Additionally, we present program scenarios of tree planting in public open spaces to match the coverage found in the most-forested parks and full cool roof implementation to help illustrate the range and flexibility of our methods.

The city of Cape Town, South Africa, was the first city partner represented in the Cool Cities Lab, so we use it here as an illustrative example. We present potentials and scenario maps for a small AOI (0.25 km²) within the city (Figure 8), and a summary of these potentials is provided in Table 10.

## Trees

We measure the potential for increasing tree cover by simulating the planting of new trees in eligible locations. Our methods support tree planting across a wide range of urban spaces, with plantable areas defined based on land use and land cover categories from the input datasets. This flexibility allows us to create program scenarios that align with city priorities—for example, planting trees in barren land, informal green spaces, or alongside residential buildings. These methods are not limited to a fixed set of options but can be adapted to explore planting opportunities wherever conditions permit. We present methods for planting street trees within rights-of-way and planting trees in public open spaces. These are areas where cities frequently invest in tree planting and where shade can improve pedestrian comfort and accessibility.

To quantify where new street trees can be planted, we use a simple set of rules that estimate the plantable area. We first define the road right-of-way as the area within 5 m of roads that is not road or water. This area can be thought of as a pedestrian zone. We then define the plantable area for street trees as the subset of the road right-of-way that is classified in the OpenUrban data as green space (other), built-up (other), barren, or public open space. Excluded from the plantable area are the 1 m

26 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

pixels covered by existing tree canopy. For the program scenarios we adopt more restrictive definitions of plantable areas.

Public open spaces (outside of road right-of-way areas) are another set of places where cities may be interested in planting trees. We define the plantable area as public open space pixels in the OpenUrban data, excluding pixels covered by existing tree canopy.

In addition to road rights-of-way and public open spaces, a more general estimate of plantable area can be derived by identifying all areas in the OpenUrban LULC dataset that are not classified as buildings, roads, or water. This includes categories such as green space (other), built-up (other), barren land, and any other surfaces not explicitly excluded due to imperviousness or functional use. While these areas may not fall into formal public infrastructure zones, they often represent informal greenspace, vacant land, or underutilized areas where tree planting could be feasible. Defining plantable area in this broader way allows cities to explore the full extent of opportunities for canopy expansion, particularly in areas that may lack formal parks or tree-lined roads.

Tree-cover potential, as defined here, reflects *canopy area* rather than the ground area required to establish plantings. As a result, the fraction of area that could be covered by tree canopy does not correspond 1:1 to the fraction of horizontal ground surface that would need to be converted to planting space (e.g., through tree trenches). These potentials represent the *canopy extent*, not a literal allocation of ground surface or planting pits, although the number of existing trees and the number of trees needed to reach a target potential can be estimated.

#### TECHNICAL SCENARIO FOR TREE PLANTING

The technical scenario for tree planting represents the AOI if there were full tree cover of the plantable area. We calculate the technical potential as the area-wide percentage of tree cover that results from 100 percent tree cover in the plantable area, with the increase in tree canopy technically possible being the technical potential minus the current percentage of tree cover.

The Cape Town AOI has an area of 0.25 km² and a plantable area for street trees of 9,001 m². Planting 100 percent of the plantable area in the AOI results in a technical potential of 8.4 percent tree cover compared to the baseline tree cover of 4.8 percent. The Cape Town AOI has a plantable area for public open spaces of 1,082 m²—planting 100 percent of this area results in a technical potential for park trees of 5.2 percent.

#### ACHIEVABLE SCENARIO FOR TREE PLANTING

We create the achievable scenario by identifying the highest levels of existing tree cover within a city and using them as locally grounded benchmarks for what may be feasible elsewhere, given the city's social, economic, ecological, and political context. This approach assumes that if high levels of tree cover have already been achieved in some parts of the city, then similar conditions may allow for comparable levels of implementation in other areas—without requiring detailed, location-specific assumptions about water availability, soil quality, or ecoregion. Rather than applying a hypothetical or universal target, the achievable scenario uses an empirical estimate derived from the city's own observed patterns of tree cover, making it a more realistic—but still ambitious—and locally relevant target.

To define the tree cover target for the achievable scenario for tree planting, we examine the distribution of the percentage tree cover in the plantable area for the entire city. For street trees or general tree planting, we create a 100 m grid over the urban area—100 m being an approximation of the scale of a city block—and calculate the percentage of the plantable area that is covered by existing tree canopy within each grid cell. For park trees, we calculate the coverage per public open space polygon within the urban area. The achievable tree cover target is estimated from the 90th percentile of the distribution of existing tree cover within the land category of interest (road right-of-way, parks, or other plantable area), excluding from the distribution grid cells or public open space polygons with no plantable area. We calculate the achievable potential as the percentage tree cover of the AOI if the percentage tree cover of the plantable area equaled the achievable target.

The achievable target for street trees (90th percentile of existing street tree cover) in Cape Town is 19.8 percent tree cover in the plantable area. Planting 19.8 percent of street tree plantable areas in the AOI results in an achievable potential of 6.1 percent tree cover for the AOI compared to the baseline tree cover of 4.8 percent for the AOI.

The achievable target for park trees (90th percentile of existing tree cover in parks) in Cape Town is 29.5 percent tree cover in the plantable area. Planting 29.5 percent of park plantable areas in the AOI results in an achievable potential of 4.9 percent tree cover for the AOI compared to the baseline tree cover of 4.8 percent for the AOI. If more park areas were available within the AOI, the potential would be higher, as achievable potential is constrained by the area available for modification.

TECHNICAL NOTE | March 2026 | 27

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

## PROGRAM SCENARIOS FOR TREE PLANTING

Program scenarios for tree planting estimate the area-wide tree cover if a tree planting program were implemented. To create maps of tree cover scenarios for the program potentials for an AOI, we generate simulated trees based on tree sizes identified from the statistical distribution of the estimated existing tree canopy heights within the AOI. This eliminates the need to make location-specific assumptions about tree species, growth rates, and die-off rates while generating data that resemble the existing tree cover. First, the baseline tree height raster dataset is converted to tree points and crown polygons using the LiDAR (light detection and ranging) package for R. This package enables the extraction of individual tree information from a canopy height model (CHM) raster. From the CHM, we identify both the location and height of each tree trunk, as well as the size, shape, and pixel-level heights of each tree crown. To detect tree locations, we apply a local maximum filter, which identifies the tallest point within a specified radius—interpreted as the location of an individual tree trunk. The choice of radius is important: if it is too small, the algorithm may identify multiple peaks within a single tree crown and too many trees will be identified; if it is too large, it may miss smaller or closely spaced trees. We use a 5 m radius for this filter because the minimum observed crown diameter in the canopy height dataset is 3 m (Tolan et al. 2024). After identifying the trunk locations, we delineate tree crowns using an algorithm from Dalponte and Coomes (2016) that segments the CHM based on canopy structure. The resulting tree crowns are then converted into polygons for use in further analysis, including simulation of new trees and estimation of planting potential.

The distribution of heights from the existing tree points is used to define three representative tree types for simulation: small (25th percentile height), medium (50th percentile height), and large (75th percentile height). These three categories are assigned fixed probabilities: 50 percent for medium trees, and 25 percent each for small and large trees. This weighted probability scheme reflects a simplified version of the full height distribution and can be adjusted to suit specific scenarios. For example, if modeling a newly planted urban forest, the simulation could emphasize smaller trees by selecting lower percentiles and increasing the probability assigned to the small tree category.

To simulate new tree cover, a point is randomly placed within the plantable area, maintaining a minimum distance (default 5 m) from existing tree points. A tree height is then selected based on the fixed probability distribution described above. Next, a tree crown polygon is randomly drawn from the set of existing trees with that same height category. The selected crown geometry is copied and centered over the new tree point. This process is

repeated until the desired outcome is achieved—whether that is meeting the technical, achievable, or program potential, or fully covering the plantable area.

We use a random placement approach rather than systematic spacing because plantable areas often have irregular shapes and constraints (e.g., curved sidewalks, fragmented open space) that make uniform placement impractical without detailed local design logic. Random placement, combined with spacing rules and realistic crown geometries, provides a flexible and scalable method that preserves spatial realism without overfitting to complex geometries. While the outcome of each simulation is nondeterministic, we find that repeated runs produce consistent overall coverage and spatial patterns.

We present methods for modeling a program designed to meet a primary objective of improving shade access in pedestrian areas by planting trees alongside roads likely to have pedestrian traffic. For street trees, we exclude major highways (motorway and primary OpenStreetMap road category types; see Table 4) from the road right-of-way and further restrict the plantable area to pixels not within 5 m of a building or 9 m of an intersection and classified in the OpenUrban data as green space (other), built-up (other), barren, or public open space. These distances were derived from a review of urban planning documents (Leff 2016; City of Cape Town's Urban Forest Policy 2025) and conversations with members of the Smart Surfaces Coalition; they can be considered reasonable default parameters for estimating where street trees can be planted. Excluded from the plantable area are the 1 m pixels covered by existing tree canopy.

Using the achievable potential as the target value for tree cover of the pedestrian area, we simulate trees in the plantable area until either the target achievable tree cover value is reached or all of the plantable area within the pedestrian area is covered by trees. The program potential scenario maps the estimated tree cover after the tree planting program has been implemented.

The achievable target (90th percentile) for street trees is 19.8 percent. Planting 619 additional trees along roads in the Cape Town AOI results in a program potential of 9.5 percent tree cover, compared with a baseline of 4.8 percent. The program potential is higher than the achievable potential for street trees because the achievable potential is calculated as a proportion of the plantable ground area, whereas the program scenario simulates tree placements whose canopies may extend beyond that area, resulting in greater total canopy cover. The scenario map of this program is shown in Figure 9.

Additionally, we present methods for modeling a program designed to meet a primary objective of expanding the urban forest by planting trees in public open spaces to the level of

28 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

**Figure 9 | Street tree planting program to local best practice levels on all nonhighway roads**

![img-13.jpeg](img-13.jpeg)

Note: The program increases the tree cover in the area of interest from 4.8% to the program potential of 9.5% by planting 619 trees. Some trees appear to overlap buildings due to viewing geometry effects in satellite imagery.

Source: WRI authors.

the most-forested parks. This level is defined by the achievable target. To estimate the plantable area for public open space, we use the open space polygons from OSM (Table 4). We begin by dissolving all open space polygons into a single unified geometry to ensure that overlapping or adjacent features are treated as one. We then remove any areas labeled as “pitch” or “recreation ground” (the OSM terms for sports fields), “playground,” and “golf course,” which are typically unsuitable for tree planting. After excluding pitches, we split the unified geometry back into distinct, nonoverlapping polygons. This approach ensures that contiguous open space is treated as a single area, while parks with multiple geographically separate sections are represented as individual polygons. We follow this process because we want to avoid double counting overlapping areas, which could otherwise inflate estimates of available space for tree planting. We then mask from the plantable area any pixels classified as water, parking, roads, or buildings in the OpenUrban LULC data and any pixels currently covered by trees. We simulate trees in the plantable area of public open spaces until the tree cover in each park reaches the achievable target.

The achievable target (90th percentile) for tree cover in public open spaces is 29.5 percent. Planting 18 additional trees in the two Cape Town parks within the AOI results in a pro-

**Figure 10 | Park tree planting program to local best practice levels in all public open spaces**

![img-14.jpeg](img-14.jpeg)

Note: The program increases the tree cover in the AOI from 4.8% to the program potential of 5.0% from planting 18 trees.

Source: WRI authors.

gram potential of 5.0 percent tree cover, compared with a baseline of 4.8 percent. The scenario map of this program is shown in Figure 10.

We expect to model additional program scenarios to meet the following objectives:

- Maximizing shade accessibility by setting a threshold for maximum spacing between street trees
- Improving equitable access to tree shade by increasing the percentage of tree canopy in areas with the least amount of tree cover
- Increasing tree cover in areas with limited shade cover

## Cool roofs

These methods estimate the change in roof albedo if cool roof materials are implemented. We derive albedo potential for the slope and building type definitions (Table 11) from the American Society of Heating, Refrigerating, and Air Conditioning Engineers (ASHRAE) model codes, which are widely adopted in the United States (ASHRAE 2025). Low-slope roofs are those with a pitch of 2/12 or less and can either be coated or reroofed with a single-ply membrane to achieve higher albedo

TECHNICAL NOTE | March 2026 | 29

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

performance. Steep-slope roofs have a pitch greater than 2/12 and can be surfaced with lighter-colored asphalt shingles, metal roofing, or tile to achieve higher albedo performance. We relate these categories to the building class categories in the OpenUrban dataset of residential and nonresidential (commercial) in cities outside the United States for which the OpenUrban data do not have a roof slope classification.

A range of aged albedo values is defined for each combination of roof slope and building use case (Table 11).$^{1}$ We use aged rather than initial albedo values because aged values reflect the effects of weathering and environmental exposure and are more representative of long-term performance. These values are measured according to standardized testing protocols (American National Standards Institute / International Organization for Standardization) that simulate natural weathering over three years, producing maintainable and policy-relevant benchmarks for long-term reflectivity.

The regulatory values in our analysis represent the lower bound of realistic performance targets. For low-slope roofs, they reflect the aged albedo requirements in model green building codes such as IgCC/ASHRAE 189.1 (ASHRAE 2020);$^{2}$ for steep-slope roofs, we use the aged albedo required under the residential cool roof ordinance in the City of Los Angeles—one of the first and most comprehensive programs of its kind. We consider these values to be a reasonable minimum benchmark for increasing roof reflectivity, while acknowledging that appropriate targets may differ by region depending on the availability of compliant products and local construction practices.

The average albedo values used in our model represent a more ambitious but still attainable target. These are calculated from the top decile of aged albedo values in each product category

(e.g., coatings, asphalt shingles, metal roofing) as reported in the Cool Roof Rating Council's Rated Products Database. We focus on top-performing products rather than taking the overall average because the database includes many materials that do not qualify as cool roofs. The high-end values are the average of the five highest-aged albedos in each product category. While we report the full range of values—from regulatory minimums to the highest-performing products—our scenarios in this technical note use only the average values, as they represent a realistic yet ambitious target; the other values are provided to support modeling reflectivity improvements possible under different policy or market conditions and can easily be substituted as targets in the analysis.

There are two approaches for mapping albedo increases from cool roofs: pixel-based and building-footprint-based. The pixel-based method updates the albedo of all OpenUrban pixels classified as roofs using only the LULC and albedo datasets. It provides a fast and efficient way to estimate the impact of cool roofs and simply increases the albedo of any pixel identified as a building whose current value is below the target. This approach does not estimate albedo at the level of individual buildings. The building-footprint method is more involved and is used in program scenarios where implementation is modeled by selecting specific buildings. In this approach, we calculate the median rooftop albedo for each building footprint—using the median because it is less sensitive to outliers—and update the albedo only for buildings whose median value falls below the target. The pixel-based method is well suited for area-wide potential estimates and is used for the technical and achievable scenarios, whereas the footprint-based method is applied in program scenarios that require modeling specific implementation decisions at the building level.

**Table 11 | Cool roof material potential**

|  BUILDING TYPE | ROOF SLOPE | COMMON COOL ROOF OPTIONS | REGULATORY | AGED ALBEDO VALUES  |   |
| --- | --- | --- | --- | --- | --- |
|   |   |   |   |  Average | High-end  |
|  Residential (single-family home, under 5-unit multifamily home) | Low slope | Membrane (TPO, PVC), coating | n/a | 0.62 | 0.86  |
|   |  Steep slope | Asphalt shingle, tile, metal | 0.25 | 0.28 | 0.35  |
|  Commercial, industrial, multifamily | Low slope | Membrane (TPO, PVC), coating | 0.56 | 0.62 | 0.86  |
|   |  Steep slope | Asphalt shingle, tile, metal | 0.27 | 0.28 | 0.35  |

Notes: n/a = not available; PVC = polyvinyl chloride; TPO = thermoplastic polyolefin.

30 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

## TECHNICAL SCENARIO FOR COOL ROOFS

The technical cool roof scenario represents the area-wide surface albedo that would result if all building roofs were converted to cool roofing materials. To support integration with the OpenUrban dataset, the baseline albedo data—originally calculated at 10 m resolution from cloud-masked Sentinel-2 surface reflectance imagery—are downscaled to 1 m using nearest-neighbor resampling. While this downscaling does not capture true subpixel variability, the resulting data are used exclusively for computing spatially aggregated albedo values rather than pixel-scale analyses. Sentinel-2-derived albedo estimates exhibit regression toward the mean, whereby dark surfaces are slightly overestimated and bright surfaces slightly underestimated (Fork et al. 2025); as a result, the native 10 m albedo values already represent spatially smoothed reflectance. Downscaling therefore preserves area-averaged albedo and has minimal influence on the aggregated estimates used in this analysis.

Using building footprint data from Overture Maps (used in the OpenUrban generation process) together with baseline albedo values, we first compute the median albedo for each building footprint. We then estimate the change in albedo that would occur if each building were updated to its corresponding cool roof material potential (Table 11). In cities where roof-slope classification is available in OpenUrban (currently limited to the United States), we assign target albedo values of 0.62 for low-slope roofs and 0.28 for high-slope roofs, reflecting typical aged performance of widely available cool roofing materials. In cities outside the United States, where roof-slope information is unavailable, all roofs are assumed to be low-slope and assigned a target albedo of 0.62. This assumption may overestimate potential albedo increases in cities with a substantial share of high-slope roofs. However, because global building typologies vary widely and no reliable data or models exist to estimate roof slope consistently at the global scale, this approach is appropriate for a technical scenario intended to represent an upper bound on potential albedo change.

Technical cool roof potential is calculated as the area-wide mean albedo resulting from full adoption of cool roofs across all buildings. Using the OpenUrban dataset, baseline albedo values are updated for building pixels whose existing albedo does not already exceed the target value, and the mean albedo of the AOI is then recomputed to represent the technical potential under complete implementation.

The Cape Town AOI has a building footprint area of 0.122 km². Because the OpenUrban data do not contain slope classifications, we assume all roofs are low slope. Taking 100 percent of the roofs currently below the target to the technical target albedo of 0.62 (average aged albedo for low-slope roofs

from Table 11) results in a technical potential of 31.4 percent reflectivity (0.314 albedo) compared to the baseline reflectivity of 20.4 percent.

## ACHIEVABLE SCENARIO FOR COOL ROOFS

The achievable scenario for cool roofs represents the area-wide albedo if all roofs were updated to have albedo values matching the most reflective roofs already present in a city. We determine this potential using existing roof albedo values from Sentinel-2 imagery to identify the upper range of roof reflectivity observed locally. Not all cool roofing materials are available or widely used in all contexts, so we use locally derived albedo values to establish more realistic targets than those presented in the technical potential for each city. These locally observed values provide benchmarks for what could feasibly be achieved more broadly, reflecting local construction practices, material availability, and policy context. In places where adoption of reflective materials is limited, achievable potential may represent only modest improvements, but it still offers a meaningful benchmark: an estimate of what citywide albedo would look like if all roofs performed like the most reflective existing ones.

We use the downscaled 1 m albedo to calculate zonal statistics, estimating typical albedo values for low-slope and high-slope buildings, if defined explicitly in the OpenUrban dataset for US cities. Specifically, we treat each slope class of building pixels as a zone and summarize the albedo values within that zone. For buildings without slope classification (non-US cities) we summarize albedo values within a single zone representing all buildings. While some albedo pixels may contain rooftops mixed with other elements—such as heating, ventilation, and air conditioning equipment; skylights; or adjacent nonroof surfaces that may have albedos different than the rooftops—summarizing the albedo distribution across all pixels within each building slope class helps mitigate the influence of these mixed pixels and provides a more robust estimate of typical roof reflectivity. We use the 90th percentile of the building albedo distribution (or 90th percentile per building slope category) to define the target for achievable potential, capturing the high end of current performance while excluding outliers that may result from rooftop features or residual cloud contamination.

We calculate the achievable potential as the area-wide percentage reflectivity that results from 100 percent of buildings having albedos equal to the achievable target values. We use the OpenUrban dataset to update the baseline albedo map with the achievable target albedo values where there are building pixels that do not already have albedos exceeding the target value. We then calculate the achievable potential for cool roofs as the mean albedo of the AOI resulting from full implementation of

TECHNICAL NOTE | March 2026 | 31

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

cool roofs with albedo values specified by the achievable targets. Because many areas have not seen widespread adoption of cool roofs, roofing materials are evolving rapidly, and albedo can be improved relatively quickly through resurfacing or coatings, this approach likely provides a conservative estimate. To reflect more ambitious adoption pathways, the technical scenario and some program scenarios (discussed next) apply more aggressive albedo assumptions for converted roofs.

We calculate the achievable target albedo as the 90th percentile of existing roof albedos in the city—for the Cape Town urban extent this value is 0.27. Taking 100 percent of the roof pixels currently below the target in the Cape Town AOI to the achievable target albedo results in an achievable potential of 21.7 percent reflectivity (0.217 albedo) compared to the baseline reflectivity of 20.4 percent.

#### PROGRAM SCENARIOS FOR COOL ROOFS

Program scenarios for cool roofs represent the area-wide albedo if a cool roof program were implemented. We present methods for modeling a program focused on maximizing albedo gains and minimizing effort by targeting the largest buildings, where applying cool materials can achieve significant area-wide impact while involving a potentially smaller number of buildings, institutions, and decision-makers and offering greater opportunities for economies of scale. Additionally, we present methods for modeling a program focused on maximum implementation that targets all buildings. The program scenarios map the estimated surface albedo and estimate the potential that results from full implementation of the cool roof programs.

The building footprint data from Overture Maps, used both in the OpenUrban dataset and in our scenario analyses, does not include parcel- or ownership-level information. As a result, features such as a block of rowhouses may appear as a single, continuous building footprint even though each unit is owned and maintained separately. This has practical implications for cool-roof implementation, as the ability to convert an entire connected roof area may depend on multiple individual ownership decisions unless coordinated or mandated through city policy.

#### Cool roofs on large buildings

Resurfacing large roofs is more efficient in terms of time and cost than treating many smaller roofs and can result in a larger total increase in citywide albedo for the same number of installations. Following the European Parliamentary Research Service, which states that for the purposes of measuring energy performance large buildings are those with a useful floor area greater than 2,000 m², we adopt 2,000 m² as our threshold for

large buildings (Dulian 2024). This is approximately the size of five basketball courts. Using building footprint data from Overture Maps (used in the OpenUrban data generation process), we identify buildings that meet these criteria and that intersect the AOI, convert the polygons to a raster, and mask out all buildings smaller than the size threshold. For all buildings above this area threshold and with existing median albedos lower than the target, we update the albedo map using the average albedo value (Table 11) for low-slope cool roofs.

In the Cape Town AOI, 15 buildings with footprint areas greater than 2,000 m² intersect the AOI, none of which have existing median albedos greater than 0.62. The total area of those buildings within the AOI is 0.075 km². Updating these roof areas to an albedo of 0.62 results in a program potential for reflectivity of 29.1 percent (0.291 albedo) compared to a baseline reflectivity of 20.4 percent. The scenario map for this program is shown in Figure 11.

#### Cool roofs on all buildings

Targeting all buildings for cool roof implementation produces maximum albedo change and is a scenario in which cities have expressed specific interest. To ensure a more conservative estimate than if we assumed all buildings are low-slope, we infer slope for non-US cities based on a classification tree that classifies roof slope based solely on building footprint area. This predictive model was developed from the US building slope data (see “Buildings class” in “OpenUrban land use and land cover mapping”) and uses a threshold of 821 m² to distinguish roof types: buildings with footprints below this threshold are treated as high-slope and assigned an albedo of 0.28, while larger buildings are considered low-slope and assigned an albedo of 0.62. While this threshold reflects US building morphology and may not generalize globally, it anchors material assumptions to observed building size and produces a more conservative estimate than assigning all buildings the low-slope value. The program potential scenario for cool roofs on all buildings maps the estimated surface albedo after the cool roof program has been implemented.

In the Cape Town AOI, 15 buildings (2,000 m²) with footprint areas less than or equal to 821 m² and 27 buildings (0.088 km²) with footprint areas greater than 821 m² intersect the AOI, none of which have existing median albedos greater than 0.28 and 0.62 (aged albedo values for high- and low-slope roofs; see Table 11), respectively. Updating these roof areas results in a program potential for reflectivity of 31.1 percent (0.311 albedo) compared to a baseline reflectivity of 20.4 percent. The scenario map for this program is shown in Figure 12.

32 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

Figure 11 | Map for program scenario cool roofs on large buildings

Baseline Albedo

![img-15.jpeg](img-15.jpeg)

Updated Albedo

![img-16.jpeg](img-16.jpeg)

Albedo

![img-17.jpeg](img-17.jpeg)

Note: All buildings with footprints greater than 2,000 m² in area are updated to albedos of 0.62. The program potential for reflectivity for this scenario is 21.7%.

Source: WRI authors.

Figure 12 | Map for program scenario cool roofs on all buildings

Baseline Albedo

![img-18.jpeg](img-18.jpeg)

Updated Albedo

![img-19.jpeg](img-19.jpeg)

Albedo

![img-20.jpeg](img-20.jpeg)

Note: All buildings with footprints greater than 821 m² in area are updated to albedos of 0.62; buildings below this threshold are updated to albedos of 0.28. The program potential for reflectivity for this scenario is 31.1%.

Source: WRI authors.

TECHNICAL NOTE

March 2026

33

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

While we present methods for two program scenarios, our methods are flexible: albedo improvements can be modeled for all buildings or any subset of buildings, based on programmatic or policy goals. Similarly, target albedo values can be assigned using any of the defined cool roof material potential values in Table 11—regulatory, average, or high-end—or using the achievable potential derived from local albedo distributions.

We anticipate modeling additional program scenarios to meet the following objectives:

- Targeting the darkest roofs, where the potential for increasing reflectivity is greatest
- Targeting all roofs, maximizing temperature reductions

Reflective pavements

We assume that most urban roads are paved with asphalt, a low-albedo material. Reflectivity can be increased either by converting asphalt roads to concrete or by resurfacing them, though large-scale asphalt-to-concrete conversion is uncommon due to high costs and major infrastructure disruptions. A more feasible strategy—especially for low-traffic residential roads—is to apply lighter-colored seal coats, which offer a cost-effective and scalable approach already in use in cities such as Phoenix and Los Angeles (ASU Urban Climate Research Center 2021). Although the initial albedo of asphalt and concrete differs substantially, their values tend to converge over time as asphalt lightens and concrete darkens with use (NCAT 2016).

Unlike for cool roofs, there is no widely accepted standard for estimating aged pavement albedo, so we have to derive our own values. Therefore, our assumptions are based on peer-reviewed studies that provide the best available empirical evidence:

- **Untreated asphalt** is assumed to have an initial albedo of 0.05, which increases over time due to weathering. Using the aging model from Sen and Roesler (2016), we estimate that albedo rises quickly in the first year of installation and plateaus around 0.15 after approximately 10 years.
- **Seal-coated asphalt** is assumed to start with a high albedo (0.34) but degrades more rapidly. Reflective seal coatings lose albedo over time due to traffic abrasion and accumulation of dirt and pollutants that darken and roughen the surface. Extrapolating longitudinal field measurements taken by a team at Arizona State University (Middel et al. 2024), we estimate that seal-treated asphalt will reach the same aged albedo as untreated asphalt (0.15) within four to five years.
- **Concrete** begins with an albedo of 0.35 and gradually declines based on the model developed by Alleman and Heitzman (2019), which synthesizes data from seven field studies across diverse climates. The aged albedo after 10 years is estimated at 0.27–0.28, with an estimate average over the 10-year period of 0.31.

Although these values are drawn from a limited number of locations (Midwest, Southwest, and southern United States), they represent the most-robust longitudinal data currently available and provide a conservative basis for modeling.

Table 12 | OSM road category types used to classify road traffic volume

|  TRAFFIC VOLUME | OSM ROAD CATEGORY TYPES  |
| --- | --- |
|  Low | Busway, living street, mini roundabout, passing place, residential, road, secondary, secondary link, service, tertiary, tertiary link, trunk, trunk link, turning circle, turning loop, unclassified  |
|  High | Motorway, motorway junction, motorway link, primary, primary link  |

Table 13 | Material options for reflective pavements based on traffic volume

|  VOLUME | MATERIAL OPTIONS | NEW | 10-YEAR FINAL | 10-YEAR AVERAGE  |
| --- | --- | --- | --- | --- |
|  Low-volume traffic, parking lots | Seal coat | 0.34 | 0.16 | 0.20  |
|  High-volume traffic | Transition to concrete | 0.35 | 0.28 | 0.31  |

Note: The 10-year average albedo is obtained by creating annual albedo estimates using the methods described in the studies cited above and averaging over a 10-year period.

34 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

Albedo interventions vary based on traffic volume. For low-volume roads, we use the 10-year average albedo (0.305) of reflective seal coats—currently the most common treatment for increasing pavement reflectivity. While formulations vary, most seal coat products have similar initial albedos and degrade at comparable rates. For high-volume roads, viable interventions are more limited. Some products for both road types offer cooling through photocatalysis rather than albedo change; these are excluded from our analysis.

We categorize roads into traffic volume classes using Open-StreetMap road category types (Table 12) and include parking lots from OpenUrban in the low-volume category. Table 12 summarizes the materials and associated albedo values by traffic volume. Our default approach uses the 10-year average albedo to reflect long-term potential under full implementation. However, alternate time horizons (e.g., five years) could be applied to model shorter-term resurfacing campaigns.

#### TECHNICAL SCENARIO FOR REFLECTIVE PAVEMENTS

To model the technical scenario for reflective pavements, we begin by filtering the OSM road vector data for the AOI into traffic volume categories, following the classification and processing methods used in estimating the plantable area for trees (see “Trees” above). We rasterize the roads (1 m resolution) into a categorical layer distinguishing low- and high-traffic-volume roads, retaining the high-traffic class where categories overlap. Parking lots are selected from the OpenUrban LULC data and included in the low-traffic category.

We update the baseline albedo data—calculated at 10 m resolution from cloud-masked Sentinel-2 surface reflectance imagery and downscaled to 1 m using nearest-neighbor resampling to match the resolution of the OpenUrban data—with values from Table 13 where there are roads. While vehicle presence can affect pavement reflectivity at specific times of day, these dynamic effects are beyond the scope of this analysis. We assign the 10-year average albedo value for seal coat of 0.195 to all low-traffic roads and parking lots and the 10-year average albedo value for concrete of 0.305 to all high-traffic roads. Because albedos degrade over time, we apply the target albedo to all low-volume roads regardless of current albedo levels. Although large-scale concrete conversion has low feasibility, we included it here because it is technically possible. The technical potential for reflectivity of reflective pavements is quantified as the mean albedo in the AOI after full implementation of the technical scenario.

The Cape Town AOI has a high-traffic-volume road area of 4,400 m² and a low-traffic-volume road area of 4,920 m². Taking 100 percent of the roads to their respective technical target albedos

dos of 0.305 and 0.195 (10-year average albedo from Table 13) results in a technical potential of 21.4 percent reflectivity (0.214 albedo) compared to the baseline reflectivity of 20.4 percent.

#### ACHIEVABLE SCENARIO FOR REFLECTIVE PAVEMENTS

The achievable scenario reflects what could reasonably be implemented based on current city conditions. Using OpenUrban and the downscaled 1 m baseline albedo, we calculate the pixel-wise 90th percentile of existing albedo values for roads (including parking lots). Because large-scale concrete conversion has low feasibility, we do not make the distinction between low- and high-traffic-volume roads when creating the achievable scenario. To minimize the influence of tree shade on albedo estimates, we first mask all road pixels that are overlapped by tree canopy. Future work will also incorporate building shade, an important factor in the effectiveness of reflective pavements. Although this approach includes some mixed pixels along road edges, the use of percentile-based statistics helps minimize their impact on the resulting albedo estimates. We use these values as class-specific targets for reflective pavement implementation in lieu of the values in Table 13.

We then update the albedo values in the baseline map where there are roads, including parking lots using the achievable target. Because albedos degrade over time, we apply the target albedo to all roads regardless of current albedo levels. This approach aligns with how we estimate the achievable potential for other infrastructure types, though road albedos typically show less variation than implementation levels of other infrastructures because they are generally centrally managed by public works departments.

Although few cities have widely implemented reflective pavement programs, the achievable potential provides a benchmark for progress by showing what the city could look like if all pavements were as reflective as the most reflective ones currently in place. In cities with limited or no existing programs, this benchmark may significantly underestimate the true potential that could be achieved through broader implementation. The achievable potential for albedo of reflective pavements is quantified as the mean albedo of the AOI after applying the target value to all roads (including parking lots).

We calculate the achievable target albedo for reflective pavements as the 90th percentile of existing road albedos in the city—for the Cape Town urban extent this value is 0.17. Taking 100 percent of roads (5,360 m²) in the Cape Town AOI to the achievable target albedo results in an achievable potential of 20.7 percent reflectivity (0.207 albedo) compared to the baseline reflectivity of 20.4 percent.

TECHNICAL NOTE | March 2026 | 35

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

# PROGRAM SCENARIO FOR REFLECTIVE PAVEMENTS

Program scenarios for reflective pavements represent the area-wide albedo if a reflective pavement program were fully implemented. Because reflective pavement materials are more widely available for low-traffic-volume roads and reflective pavements are most effective when implemented at a large scale (Schneider et al. 2023), we model a scenario that increases reflectivity on all low-traffic-volume roads to the available technology levels. To create this scenario, we follow the methods for the technical potential for reflective pavements (see “Technical scenario for reflective pavements”) but only update the albedo of low-traffic-volume roads.

The Cape Town AOI has 4,920 m² of low-traffic-volume road area. Updating these road areas results in a program potential for reflectivity of 21.4 percent (0.214 albedo) compared to a baseline reflectivity of 20.4 percent. The scenario map for this program is shown in Figure 13.

We expect to model additional program scenarios to meet the following objectives:

- Targeting roads with less pedestrian activity to reduce the impact of reflected sunlight on thermal comfort

- Maximizing the effect of increasing reflectivity by targeting roads with low existing tree cover
- Prioritizing benefits to thermal comfort by targeting roads with high pedestrian activity and high tree cover

# Shade structures

Shade structures provide an adaptable way to reduce heat exposure in cities, offering immediate relief in places where tree planting is not feasible or where additional shade is needed. Shade structures can incorporate cool roofing materials or be outfitted with solar photovoltaic panels. Our methods are flexible and can be applied across the urban landscape, allowing us to create scenarios to match city goals—from cooling transit stops to enhancing comfort in parks or pedestrian corridors.

We generate a 1 m resolution binary raster of shade by combining tree and building shade (see “Shade” in “Heat relevant surface characteristics”). Because shade varies throughout the day, we use the noontime shade map, representing the time of lowest shade availability. This map allows us to quantify shade coverage for any area of interest. Here we focus on public open spaces and pedestrian zones—areas where people are most exposed to heat. For these areas we quantify shade availability.

Figure 13 | Map for program scenario reflective pavements on all low-traffic roads

Baseline Albedo

![img-21.jpeg](img-21.jpeg)

Updated Albedo

![img-22.jpeg](img-22.jpeg)

Albedo

![img-23.jpeg](img-23.jpeg)

Note: All low-traffic-volume roads were updated to albedos of 0.195. The program potential for reflectivity for this scenario is 21.4% compared to a baseline reflectivity of 20.4%.
Source: WRI authors.

36 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

For public open spaces, we calculate the percentage shade per polygon as the mean of the binary raster, where 0 indicates no shade and 1 indicates full shade. The mean is weighted by the proportion of each pixel that intersects with the polygon to account for partial overlaps. Since the raster is binary, there are no partially shaded pixels—only shaded or not. We exclude areas labeled as “pitch” (e.g., athletic fields), which are typically found within large parks and are not suitable for shade structures due to their use for sports and recreation that require open, unobstructed space. For the remaining area, we calculate the total area available for shade structures (unshaded area) and the percentage of shade.

Open spaces vary widely in size, use, and existing natural shade, and cities may differ in recreational preferences and ecological context. For smaller spaces, which we define as one acre (approximately 4,047 m²) or less in area, it is feasible to set a target minimum shade percentage. For larger spaces, which we define as greater than one acre in area, we focus instead on access to shade—defined by the maximum distance to shaded areas. Maximum distance highlights the worst-case access gaps and helps set clear, inclusive policy thresholds (e.g., “no one should be more than 50 m from shade”), making it a strong tool for ensuring minimum levels of service.

For pedestrian zones (defined above in “Trees”), we calculate both the percentage shade and the total unshaded area. The percentage of shade is useful for evaluating current conditions and setting policy targets (e.g., a goal of 40 percent shade coverage), while the total unshaded area represents the space available for additional shade structures. To assess the spatial variation in pedestrian shade, we also create a 100 m grid across the entire AOI and calculate the percentage of shaded pedestrian area within each grid cell.

#### TECHNICAL SCENARIO FOR SHADE STRUCTURES

The technical scenario for shade identifies shaded and unshaded areas within areas suitable for implementing shade structures like public open spaces and pedestrian zones. Although full implementation is unlikely, mapping these areas and quantifying available space for shade structures helps set realistic goals. We define the technical potential for shade cover as the shade coverage in the entire AOI if all suitable areas were 100 percent shaded at noon. We calculate the technical potential for public open spaces, but additional scenarios that model the technical potential of pedestrian areas or all areas suitable for shade structures (combination of public open spaces and pedestrian zones) can be created.

The Cape Town AOI has 0.122 km² of suitable public open spaces. Shading 100 percent of this area results in a technical

potential of 31.4 percent shade cover compared to the baseline shade cover of 26.9 percent.

#### ACHIEVABLE SCENARIO FOR SHADE STRUCTURES

The achievable potential for shade estimates high but locally informed benchmarks for shade coverage, based on the existing conditions in the shadiest parts of the city. These empirically derived values serve as achievable targets based on what is already implemented in the city, capturing a mix of tree, building, and structural shade. For public open spaces, we calculate the percentage of shade cover within each polygon and define the target as the 90th percentile of the distribution of shade cover in public open spaces.

Here, we calculate the achievable shade potential for public open spaces. The same framework can also be applied to other spatial domains, such as pedestrian areas, or to a combined domain that includes both public open spaces and pedestrian zones. For example, achievable shade potential for pedestrian areas could be estimated by overlaying a 100 m grid across the AOI, calculating the percentage of shaded pedestrian area within each grid cell, and defining the achievable target as the 90th percentile of this distribution.

We calculate the achievable target for shade cover as the 90th percentile of existing shade cover in public open spaces in the city—for the Cape Town urban extent this value is 45.5 percent. Taking 100 percent of the public open spaces (0.122 km²) currently below the target in the Cape Town AOI to the achievable target results in an achievable potential of 27.1 percent shade cover compared to the baseline shade cover of 26.9 percent.

#### PROGRAM POTENTIAL FOR SHADE STRUCTURES

Shade structures for public open spaces are modeled using currently available products (temporary structure, permanent structure), with a standard 5 m × 5 m (16.4 × 16.4 feet) unit selected as a practical midsize option that accommodates about 25 people, assuming 1 m² per person. Different sizes or shapes of shade structures are also possible to model.

To increase access to shade, a policy might set program goals for ensuring minimum shade levels in public open spaces. Because park sizes vary significantly, we apply different metrics for large and small spaces: for small parks, we set a minimum shade coverage of 25 percent, and for large parks, a maximum distance to shade of 50 m. These thresholds are chosen to balance meaningful shade provision with flexibility for recreational uses—the 50 m distance is equal to half the length of a standard soccer field, ensuring that shade remains accessible without overly constraining park design.

TECHNICAL NOTE | March 2026 | 37

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

For small public open spaces, we identify potential locations for shade structures by masking the 1 m unshaded raster with polygons of small parks that are not classified as “pitches.” Each unshaded pixel is then converted to its centroid, representing a candidate location for placement. The target shaded area is calculated by multiplying the difference between the target shade percentage and the park’s existing shade percentage by the total park area. Shade structures are placed through an iterative process. A candidate point is randomly selected and checked to ensure that it meets two criteria: adequate spacing from previously placed structures and full containment within the park boundary. While a more systematic placement may be desirable in some cases, random placement offers the most flexibility in terms of applicability of the methods to many cities, and small parks often have limited placement options. If valid, a square buffer (with half the shade structure’s width as the buffer radius) is drawn around the point to represent the structure. After placement, the total shaded area is recalculated and compared to the target. This process repeats until the shaded area meets or exceeds the target, with a maximum of five restarts allowed. If the target cannot be met under the defined spacing rules, the script terminates after the final attempt, preventing infinite loops while still achieving a reasonable approximation of the target.

For larger public open spaces, we place shade structures in unshaded areas until the target of a maximum of 50 m distance to shade is met. First, the shade raster is cropped to the park boundary, and larger contiguous shaded zones—those equal to or greater than the size of a shade structure (25 m²)—are identified. Although small shaded spots still offer value, larger areas of shade provide more accessibility. We measure the distance from each pixel within the park to the nearest shaded zone; if there are areas where the maximum distance to shaded zones exceeds the target, we place a new structure in the unshaded area where the distance to shade is greatest. This process is repeated—recalculating distances and adding structures—until the distance from any pixel within the park to the nearest shade zone falls below the target distance. The program potential is quantified as the total shaded area in public open spaces if these policy-based shade structures were implemented.

The Cape Town AOI includes two small parks (less than 1 acre). Four shade structures were added to each park to bring the shade cover to a minimum of 25 percent. There was no baseline shade cover in either park. Adding these structures results in a program potential for shade cover of 27.0 percent compared to a baseline shade cover of 26.9 percent. It is worth noting, however, that the program potential for shade cover within the public open space area is 18.5 percent compared to the baseline shade cover within the public open space area of 0 percent. The shade

**Figure 14 | Map for program scenario shade cover increase to ensure minimum target level**

![img-24.jpeg](img-24.jpeg)

*Note:* Shade structures were added to the small parks (less than 1 acre in size) until there was at least 25% shade cover. The program potential for shade cover is 27.0% compared to the baseline shade cover of 26.9%. The program potential for shade cover within the public open space area is 18.5% compared to the baseline shade cover within the public open space area of 0%.

*Source:* WRI authors.

cover did not reach 25 percent because no more structures could be added with the specific spacing rules. The scenario map for this program is shown in Figure 14.

We expect to model additional program scenarios to meet the following objectives:

- Improving access to shade for transit riders by requiring that all bus stops have shade structures
- Ensuring a maximum distance between shaded areas in pedestrian zones

## Combinations

Cities have emphasized the importance of understanding how multiple interventions interact when implemented together. To address this, our methods allow the creation of program scenarios that combine different types of heat-resilient infrastructure. These combined program scenarios are constructed by overlaying scenario maps for each intervention, with the restriction that infrastructures are mutually exclusive at the pixel level (e.g., a tree and a shade structure cannot occupy the same location).

It may be necessary to generate multiple scenario maps for each combined program scenario—for instance, in a combined street tree and cool roofs scenario it would be necessary to create both

38 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

**Figure 15 | Combination of street tree and cool roof program scenarios**

![img-25.jpeg](img-25.jpeg)

Note: The albedo scenario map for cool roofs has been updated with existing tree albedo values where there are new trees.

Source: WRI authors.

tree cover and albedo maps. To do so, we assign representative albedo values to nonreflective infrastructures. For trees we preserve realistic variability by updating the albedo map where new trees are added using values randomly sampled from the interquartile range of albedo values of existing tree-covered pixels (Figure 15). Shade structures are assigned an albedo of 0.28, under the assumption that they can be constructed with cool roofing materials suitable for high-slope roofs (see “Shade structures”). Likewise, when combining trees and shade structures, we use the tree cover scenario map as a proxy for shade under the assumption that at noon the shade from a tree is approximately equal to the footprint of the tree cover.

While combined scenarios allow cities to explore potential synergies, the cooling effects of multiple interventions may not be fully additive. Increased shading from trees or surrounding structures can reduce solar exposure on roofs, thereby diminishing the marginal cooling benefit of reflective surfaces in some contexts; our approach partially captures this interaction by updating albedo values where new tree cover is introduced, including locations where tree canopy overlaps buildings.

This framework supports scenario designs that model the kinds of strategies cities are most interested in pursuing. For example, a combined scenario of cool roofs and street tree planting can demonstrate how reflective surfaces lower overall albedo-driven heat while expanded canopy improves shade access for pedestrians.

By modeling combinations, cities can explore synergies and evaluate how layered strategies might achieve greater cooling benefits than single interventions alone.

## Limitations

There are several important limitations to this framework and these methods. First, the methods do not yet incorporate population exposure or vulnerability measures, which are essential for prioritizing interventions where they will provide the greatest benefits. Integrating exposure and vulnerability data represents an important direction for future development. The framework also does not incorporate the costs of implementation and maintenance, or the long-term financial benefits associated with avoided heat-related impacts.

Second, the analyses rely on the best globally available datasets, which—like all data—contain uncertainty and may be incomplete in some areas. Many sources used here, such as OpenStreetMap, are crowd-sourced and therefore vary in coverage, accuracy, and data standards. While locally sourced datasets may offer higher accuracy, they are often costly or time-intensive to produce and may not be available in many cities. By contrast, global open datasets are freely available and immediately usable, lowering barriers to participation in urban heat resilience planning. Where possible, we report accuracy metrics for key

TECHNICAL NOTE | March 2026 | 39

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

input datasets to enable users to assess trade-offs between data availability and precision.

Several simplifying assumptions are required to apply the framework consistently across cities. For example, in locations outside the United States where roof-slope information is unavailable, all roofs are assumed to be low-slope for the purposes of estimating cool roof potential. Within the United States, residential buildings are assumed to have high-slope roofs based on the most accurate classification available from the training data. These assumptions are necessary to support global scalability but may introduce localized error, particularly in areas where building typologies differ from these general patterns.

Additional uncertainty arises from spatial resampling and downscaling. Some surface characteristics, such as albedo, are derived from coarser-resolution inputs and downscaled to finer spatial grids to support integration with other datasets. While downscaling does not represent true subpixel variability, these data are used only in aggregated form, and their influence on area-averaged estimates is expected to be limited.

Finally, the framework does not explicitly account for the effects of building or tree shade on the performance of reflective surfaces. Shading can reduce solar exposure on roofs and pavements and thereby diminish the marginal cooling benefit of high-albedo materials in some contexts. While some of this interaction is implicitly represented where new tree cover overlaps built surfaces in combined scenarios, these effects are not modeled explicitly and remain an important area for future refinement.

The purpose of the scenario potentials and maps is not to provide project-level precision tools. As Gabrys and Pritchard (2018) argue, accuracy alone is not the sole criterion by which data should be judged. By lowering data barriers, the framework enables a broader set of cities to visualize possibilities, compare strategies, and initiate informed discussions about priorities and trade-offs. The methods are likely to perform best for comparative, exploratory analyses and for identifying relative opportunities within and across cities, and less well for detailed site-level design or implementation planning.

While intentionally general and not exhaustive, the scenario potentials and maps provide a practical starting point for aligning urban heat adaptation efforts with decision-making. They are best understood as resources for identifying opportunities, sparking dialogue, and motivating more detailed, locally calibrated analyses and implementation.

## Findings

Cities around the world are seeking practical ways to reduce rising urban temperatures, yet many lack the data, tools, or analytical capacity to identify where heat-resilient infrastructure can be deployed and what scale of impact is achievable. The work presented in this technical note provides a structured, globally scalable methodology to help fill that gap. Using only globally available datasets and an openly accessible code base, we developed a consistent framework for mapping heat-relevant surface characteristics, quantifying technical and achievable potentials, and generating spatially explicit program scenarios for four major forms of passive heat-resilient infrastructure—trees, cool roofs, reflective pavements, and shade structures.

A central accomplishment of this work is the distillation of a complex set of biophysical processes and infrastructure constraints into a simple, defensible, and low-burden analytical workflow. The methods require few inputs, minimize user decisions, and rely on defaults carefully chosen to preserve information content while remaining transparent and customizable. This design ensures that cities with limited data or technical capacity can still generate meaningful, policy-relevant estimates of opportunity and visualize a range of implementation pathways. The resulting potentials and scenario maps offer a common evidence base upon which planners, policymakers, and community stakeholders can begin structured conversations about scale, trade-offs, priorities, and feasibility. Integrated into the Cool Cities Lab, they provide cities with an accessible starting point for identifying opportunities, testing policy options, and aligning adaptation strategies with local goals.

Through these scenarios, cities can

- quantify where opportunities for cooling exist and how much change different interventions could produce;
- visualize alternative implementation pathways, seeing how trees, cool roofs, reflective pavements, or shade structures would reshape local conditions;
- compare intervention types consistently, understanding their relative impacts across the same geographic and analytical frame;
- assess impacts and synergies when interventions are layered or targeted to different areas; and
- ground planning and policy conversations in shared evidence, enabling clearer communication across departments and with communities.

40 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

## Conclusions

Taken together, the methods presented here offer cities a clear starting point and a replicable process for advancing heat-resilient infrastructure planning. By lowering data barriers, simplifying analytical choices, and providing a transparent structure for comparing intervention types, the framework supports more informed, coordinated, and ultimately actionable pathways toward cooler and more resilient urban environments.

## Endnotes

1. Aged solar reflectance is calculated using the ANSI/CRRC S100 Standard that calls for exposure and weathering of materials for three years in representative climatic zones.
2. The International Green Construction Code (IgCC) uses the Solar Reflectance Index, a composite metric that includes both solar reflectance and thermal emittance. We calculate albedo requirements by assuming a thermal emittance of 0.9, a very common value for nonmetal roofing materials.

## References

Akbari, H., M. Pomerantz, and H. Taha. 2001. “Cool Surfaces and Shade Trees to Reduce Energy Use and Improve Air Quality in Urban Areas.” *Solar Energy* 70 (3): 295–310. https://doi.org/10.1016/S0038-092X(00)00089-X.

Akbari, H., S. Menon, and A. Rosenfeld. 2009. “Global Cooling: Increasing World-wide Urban Albedos to Offset CO₂.” *Climatic Change* 94 (3–4): 275–86. https://doi.org/10.1007/s10584-008-9515-9.

Alhazmi, M., D.J. Sailor, and R. Levinson. 2023. “A Review of Challenges, Barriers, and Opportunities for Large-Scale Deployment of Cool Surfaces.” *Energy Policy* 180 (September): 113657. https://doi.org/10.1016/j.enpol.2023.113657.

Alleman, J., and M. Heitzman. 2019. *Quantifying Pavement Albedo: Final Report*. National Concrete Pavement Technology Center.

Angel, S., E. Mackres, and B. Guzder-Williams. 2024. “Measuring Change in Urban Land Consumption: A Global Analysis.” *Land* 13 (9): 1491. https://doi.org/10.3390/land13091491.

Arsht-Rockefeller Foundation. 2023. “Extreme Heat Resilience Alliance.” https://onebillionresilient.org/project/extreme-heat-resilience-alliance/.

ASHRAE (American Society of Heating, Refrigerating and Air-Conditioning Engineers). 2020. *Standard 189.1-2020: Standard for the Design of High-Performance Green Buildings except Low-Rise Residential Buildings*. https://www.ashrae.org/technical-resources/bookstore/standard-189-1.

ASHRAE. 2025. “Codes and Standards.” In *2025 ASHRAE Handbook—Fundamentals*.

ASU (Arizona State University) Urban Climate Research Center. 2021. *Cool Pavement Pilot Program*. ASU Urban Climate Research Center.

Bonafoni, S., and A. Sekertekin. 2020. “Albedo Retrieval from Sentinel-2 by New Narrow-to-Broadband Conversion Coefficients.” *IEEE Geoscience and Remote Sensing Letters* 17 (9): 1618–22. https://doi.org/10.1109/LGRS.2020.2967085.

Bowler, D.E., L. Buyung-Ali, T.M. Knight, and A.S. Pullin. 2010. “Urban Greening to Cool Towns and Cities: A Systematic Review of the Empirical Evidence.” *Landscape and Urban Planning* 97 (3): 147–55. https://doi.org/10.1016/j.landurbplan.2010.05.006.

Brown, C.F., S.P. Brumby, B. Guzder-Williams, et al. 2022. “Dynamic World, Near Real-Time Global 10 m Land Use Land Cover Mapping.” *Scientific Data* 9 (1): 251. https://doi.org/10.1038/s41597-022-01307-4.

Buo, I., V. Sagris, J. Jaagus, and A. Middel. 2023. “High-Resolution Thermal Exposure and Shade Maps for Cool Corridor Planning.” *Sustainable Cities and Society* 93 (June): 104499. https://doi.org/10.1016/j.scs.2023.104499.

Campra, P., M. Garcia, Y. Canton, and A. Palacios-Orueta. 2008. “Surface Temperature Cooling Trends and Negative Radiative Forcing Due to Land Use Change toward Greenhouse Farming in Southeastern Spain.” *Journal of Geophysical Research: Atmospheres* 113 (D18): 2008JD009912. https://doi.org/10.1029/2008JD009912.

Carlson, T.N., and D.A. Ripley. 1997. “On the Relation between NDVI, Fractional Vegetation Cover, and Leaf Area Index.” *Remote Sensing of Environment* 62 (3): 241–52. https://doi.org/10.1016/S0034-4257(97)00104-1.

City of Cape Town. 2025. City of Cape Town’s Urban Forest Policy.

Croce, S., and D. Vettorato. 2021. “Urban Surface Uses for Climate Resilient and Sustainable Cities: A Catalogue of Solutions.” *Sustainable Cities and Society* 75 (December): 103313. https://doi.org/10.1016/j.scs.2021.103313.

Dalponte, M., and D.A. Coomes. 2016. “Tree-centric Mapping of Forest Carbon Density from Airborne Laser Scanning and Hyperspectral Data.” *Methods in Ecology and Evolution* 7 (10): 1236–45. https://doi.org/10.1111/2041-210X.12575.

Dulian, M. 2024. *Revision of the Energy Performance of Buildings Directive*. EPRS Briefing PE 698.901. European Parliamentary Research Service (EPRS), European Parliament. https://www.europarl.europa.eu/RegData/etudes/BRIE/2022/698901/EPRS_BRI(2022)698901_EN.pdf.

Eisenman, T.S., G. Churkina, S.P. Jariwala, et al. 2019. “Urban Trees, Air Quality, and Asthma: An Interdisciplinary Review.” *Landscape and Urban Planning* 187 (July): 47–59. https://doi.org/10.1016/j.landurbplan.2019.02.010.

Engel, R.A., K. Cartier, H. Joh, Z. Wang, T. Wong, and X. Li. 2026. “Modeling Hyperlocal Heat Exposure with Open-Source Data.” World Resources Institute.

TECHNICAL NOTE | March 2026 | 41

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

EPA (US Environmental Protection Agency). 2007. Guide for Conducting Energy Efficiency Potential Studies. National Action Plan for Energy Efficiency. EPA and US Department of Energy. https://www.epa.gov/sites/default/files/2015-08/documents/potential_guide_0.pdf.

European Space Agency. 2017. "Sentinel-2 MSI: MultiSpectral Instrument, Level-2A Surface Reflectance." https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR.

Fork, D., E.J. Wesley, S. Banerjee, et al. 2025. "Estimating High-Resolution Albedo for Urban Applications." arXiv:2509.25096. Preprint, September 29. https://doi.org/10.48550/arXiv.2509.25096.

Gabrys, J., and H. Pritchard. 2018. "Just Good Enough Data and Environmental Sensing: Moving beyond Regulatory Benchmarks toward Citizen Action." International Journal of Spatial Data Infrastructure Research (13): 4–14.

Gao, L., X. Wang, B.A. Johnson, et al. 2020. "Remote Sensing Algorithms for Estimation of Fractional Vegetation Cover Using Pure Vegetation Index Values: A Review." ISPRS Journal of Photogrammetry and Remote Sensing 159 (January): 364–77. https://doi.org/10.1016/j.isprsjprs.2019.11.018.

Gillies, R.R., and T.N. Carlson. 1995. "Thermal Remote Sensing of Surface Soil Water Content with Partial Vegetation Cover for Incorporation into Climate Models." Journal of Applied Meteorology 34 (4): 745–56. https://doi.org/10.1175/1520-0450(1995)034<0745:TRSOSS>2.0.CO;2.

Hawker, L., P. Uhe, L. Paulo, et al. 2022. "A 30 m Global Map of Elevation with Forests and Buildings Removed." Environmental Research Letters 17 (2): 024016. https://doi.org/10.1088/1748-9326/ac4d4f.

Hersbach, H., B. Bell, P. Berrisford, et al. 2020. "The ERA5 Global Reanalysis." Quarterly Journal of the Royal Meteorological Society 146 (730): 1999–2049. https://doi.org/10.1002/qj.3803.

Hewitt, V., E. Mackres, and K. Shickman. 2014. Cool Policies for Cool Cities: Best Practices for Mitigating Urban Heat Islands in North American Cities. American Council for an Energy-Efficient Economy and Global Cool Cities Alliance.

IEA (International Energy Agency). 2024. CO₂ Emissions in 2023. https://www.iea.org/reports/co2-emissions-in-2023.

Jain, G., and J. Espey. 2022. "Lessons from Nine Urban Areas Using Data to Drive Local Sustainable Development." Npj Urban Sustainability 2 (1): 7. https://doi.org/10.1038/s42949-022-00050-4.

Kamath, H.G., M. Singh, N. Malviya, et al. 2024. "GLObal Building Heights for Urban Studies (UT-GLOBUS) for City- and Street-Scale Urban Simulations: Development and First Applications." Scientific Data 11 (1): 886. https://doi.org/10.1038/s41597-024-03719-w.

Kappou, S., M. Souliotis, S. Papaefthimiou, et al. 2022. "Cool Pavements: State of the Art and New Technologies." Sustainability 14 (9): 5159. https://doi.org/10.3390/su14095159.

Keith, L., and S. Meerow. 2022. Planning for Urban Heat Resilience. PAS Report 600. American Planning Association.

Krayenhoff, E.S., and J.A. Voogt. 2010. "Impacts of Urban Albedo Increase on Local Air Temperature at Daily-Annual Time Scales: Model Results and Synthesis of Previous Work." Journal of Applied Meteorology and Climatology 49 (8): 1634–48. https://doi.org/10.1175/2010JAMC2356.1.

Krayenhoff, E.S., A.M. Broadbent, L. Zhao, et al. 2021. "Cooling Hot Cities: A Systematic and Critical Review of the Numerical Modelling Literature." Environmental Research Letters 16 (5): 053007. https://doi.org/10.1088/1748-9326/abdcf1.

Leff, M. 2016. The Sustainable Urban Forest. US Department of Agriculture, Forest Service.

Levinson, R., M. Alhazmi, J. Becce, et al. 2023. United States Cool Surfaces Deployment Plan. None, 1988535, Ark:/13030/qt6xf9k8d0. https://doi.org/10.2172/1988535.

Li, H., Y. Zhao, R. Bardhan, A. Kubilay, D. Derome, and J. Carmeliet. 2023. "Time-Evolving Impact of Trees on Street Canyon Microclimate." Journal of Physics: Conference Series 2654 (1): 012145. https://doi.org/10.1088/1742-6596/2654/1/012145.

Li, H., Y. Zhao, C. Wang, D. Ürge-Vorsatz, J. Carmeliet, and R. Bardhan. 2024. "Cooling Efficacy of Trees across Cities Is Determined by Background Climate, Urban Morphology, and Tree Trait." Communications Earth and Environment 5 (1): 754. https://doi.org/10.1038/s43247-024-01908-4.

Lindberg, F., C.S.B. Grimmond, T. Sun, and Y. Tang. 2020. UMEP Manual Documentation. Manual. University of Gothenburg and University of Reading. https://umep-docs.readthedocs.io/en/latest/.

Middel, A., V.K. Turner, F.A. Schneider, Y. Zhang, and M. Stiller. 2020. "Solar Reflective Pavements: A Policy Panacea to Heat Mitigation?" Environmental Research Letters 15 (6): 064016. https://doi.org/10.1088/1748-9326/ab87d4.

Middel, A., S. AlKhaled, F.A. Schneider, B. Hagen, and P. Coseo. 2021. "50 Grades of Shade." Bulletin of the American Meteorological Society 102 (9): E1805–20. https://doi.org/10.1175/BAMS-D-20-0193.1.

Middel, A., J. Vanos, K. Kaloush, et al. 2024. City of Phoenix Cool Pavement Pilot Program. Arizona State University.

NACTO (National Association of City Transportation Officials). 2025. "Urban Street Design Guide: Lane Width." https://nacto.org/publication/urban-street-design-guide/street-design-elements/lane-width.

Naik, B., G. Matlack, I. Khoury, G. Sinha, and D.S. McAvoy. 2017. Effects of Tree Canopy on Rural Highway Pavement Condition, Safety, and Maintenance. Ohio Department of Transportation, Office of Statewide Planning and Research.

NCAT (National Center for Asphalt Technology). 2016. "Quantifying Pavement Albedo." https://www.eng.auburn.edu/research/centers/ncat/newsroom/2016-fall/pavement-albedo.html.

NYU (New York University), UN-Habitat, and Lincoln Institute of Land Policy. 2016. "Atlas of Urban Expansion." http://www.atlasofurbanexpansion.org/.

42 | WORLD RESOURCES INSTITUTE

Mapping scenarios and estimating the potential for heat-resilient infrastructure in cities

OpenStreetMap Contributors. 2025. "OpenStreetMap." OpenStreetMap Foundation. https://www.openstreetmap.org.

Overture Maps Foundation. 2025. "Overture Maps." https://overturemaps.org.

Pasquarella, V.J., C.F. Brown, W. Czerwinski, and W.J. Rucklidge. 2023. "Comprehensive Quality Assessment of Optical Satellite Imagery Using Weakly Supervised Video Learning." Paper presented at 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW), 2125–35.

Pesaresi, M., and P. Politis. 2018. "GHS-BUILT-H R2023A—GHS Building Height, Derived from AW3D30, SRTM30, and Sentinel-2 Composite." European Commission, Joint Research Centre. https://doi.org/10.2905/85005901-3A49-48DD-9D19-6261354F56FE.

Potapov, P., X. Li, A. Hernandez-Serna, et al. 2021. "Mapping Global Forest Canopy Height through Integration of GEDI and Landsat Data." Remote Sensing of Environment 253 (February): 112165. https://doi.org/10.1016/j.rse.2020.112165.

Santamouris, M. 2014. "Cooling the Cities: A Review of Reflective and Green Roof Mitigation Technologies to Fight Heat Island and Improve Comfort in Urban Environments." Solar Energy 103 (May): 682–703. https://doi.org/10.1016/j.solener.2012.07.003.

Schneider, F.A., J. Cordova Ortiz, J.K. Vanos, D.J. Sailor, and A. Middel. 2023. "Evidence-Based Guidance on Reflective Pavement for Urban Heat Mitigation in Arizona." Nature Communications 14 (1): 1467. https://doi.org/10.1038/s41467-023-36972-5.

Sen, S., and L. Khazanovich. 2021. "Limited Application of Reflective Surfaces Can Mitigate Urban Heat Pollution." Nature Communications 12 (1): 3491. https://doi.org/10.1038/s41467-021-23634-7.

Sen, S., and J. Roesler. 2016. "Aging Albedo Model for Asphalt Pavement Surfaces." Journal of Cleaner Production 117 (March): 169–75. https://doi.org/10.1016/j.jclepro.2016.01.019.

Simpson, C.H., O. Brousse, T. Taylor, et al. 2024. "Modeled Temperature, Mortality Impact and External Benefits of Cool Roofs and Rooftop Photovoltaics in London." Nature Cities 1 (11): 751–59. https://doi.org/10.1038/s44284-024-00138-1.

Strahler, A.H., L. Boschetti, G.M. Foody, et al. 2006. Global Land Cover Validation: Recommendations for Evaluation and Accuracy Assessment of Global Land Cover Maps. Report No. 25. GOFC-GOLD, Global Observation of Forest Cover and Land Cover Dynamics. https://gofcgold.umd.edu/sites/default/files/docs/ReportSeries/GOLD_25.pdf.

Tan, H., R. Kotamarthi, J. Wang, Y. Qian, and T.C. Chakraborty. 2023. "Impact of Different Roofing Mitigation Strategies on Near-Surface Temperature and Energy Consumption over the Chicago Metropolitan Area during a Heatwave Event." Science of the Total Environment 860 (February): 160508. https://doi.org/10.1016/j.scitotenv.2022.160508.

TNC (The Nature Conservancy). 2016. "Planting Healthy Air: A Global Analysis of the Role of Urban Trees in Addressing Particulate Matter Pollution and Extreme Heat." https://www.nature.org/content/dam/tnc/nature/en/documents/20160825_PHA_ExSummary_Final.pdf.

Tolan, J., H.-I. Yang, B. Nosarzewski, et al. 2024. "Very High Resolution Canopy Height Maps from RGB Imagery Using Self-Supervised Vision Transformer and Convolutional Decoder Trained on Aerial Lidar." Remote Sensing of Environment 300 (January): 113888. https://doi.org/10.1016/j.rse.2023.113888.

TPL (The Trust for Public Land). 2025. "ParkServe." https://www.tpl.org/ParkServe/About.

Turner, V. K., E.M. French, J. Dialesandro, et al. 2022. "How Are Cities Planning for Heat? Analysis of United States Municipal Plans." Environmental Research Letters 17 (6): 064054. https://doi.org/10.1088/1748-9326/ac73a9.

Ukkusuri, S.V., S.U. Park, S. Mittal, et al. 2024. "We Need to Prepare Our Transport Systems for Heatwaves: Here's How." Nature 632 (8024): 253–56. https://doi.org/10.1038/d41586-024-02538-8.

United Nations. 2021. Beating the Heat: A Sustainable Cooling Handbook for Cities.

USGS (US Geological Survey). 2021. "Landsat 8 Surface Reflectance Tier 1 Collection 2." https://developers.google.com/earth-engine/data-sets/catalog/LANDSAT_LC08_C02_T1_L2.

Winbourne, J.B., T.S. Jones, S.M. Garvey, et al. 2020. "Tree Transpiration and Urban Temperatures: Current Understanding, Implications, and Future Research Directions." BioScience 70 (7): 576–88. https://doi.org/10.1093/biosci/biaa055.

WorldPop. 2023. "WorldPop Global Project." https://www.worldpop.org/.

Yaghoobian, N., and J. Kleissl. 2012. "Effect of Reflective Pavements on Building Energy Use." Urban Climate 2 (December): 25–42. https://doi.org/10.1016/j.uclim.2012.09.002.

Zeng, X., R.E. Dickinson, A. Walker, M. Shaikh, R.S. DeFries, and J. Qi. 2000. "Derivation and Evaluation of Global 1-Km Fractional Vegetation Cover Data for Land Modeling." Journal of Applied Meteorology 39 (6): 826–39. https://doi.org/10.1175/1520-0450(2000)039<0826:DAEOGK>2.0.CO;2.

Ziter, C.D., E.J. Pedersen, C.J. Kucharik, and M.G. Turner. 2019. "Scale-Dependent Interactions between Tree Canopy Cover and Impervious Surfaces Reduce Daytime Urban Heat during Summer." Proceedings of the National Academy of Sciences 116 (15): 7575–80. https://doi.org/10.1073/pnas.1817561116.

TECHNICAL NOTE

March 2026

43

## Acknowledgments

We are pleased to acknowledge our institutional strategic partners that provide core funding to WRI: the Netherlands Ministry of Foreign Affairs, Royal Danish Ministry of Foreign Affairs, and Swedish International Development Cooperation Agency.

We would like to thank Google.org for supporting this work. Ruth Engel, Reynolds Kihura, Chris Rowe, Lindy Schofield, and Saif Shabou at WRI provided consultation and support during the development of this work. Dean Berkowitz, Sarah Carter, Ruth Engel, Carolina Faccin, Lucy Hutyra, Robin King, Daniel J. Metzger, Gregory Taff, Laura Malaguzzi Valeri, and Gabriela Vidad reviewed this manuscript.

## About the authors

**Elizabeth Jane Wesley** is Data Scientist, Urban Analytics, WRI Ross Center for Sustainable Cities at World Resources Institute.

Contact: elizabeth.wesley@wri.org.

**Eric Mackres** is Senior Manager, Urban Analytics, WRI Ross Center for Sustainable Cities at World Resources Institute.

**Kurt Shickman** is Senior Fellow, WRI Ross Center for Sustainable Cities at World Resources Institute.

**Clemens Janssen** is User Research & Engagement Lead at World Resources Institute.

**Madeline Mulder** is Cartographer at Environmental Systems Research Institute Inc.

**Theodore Wong** is Research and Project Associate, Urban Analytics, WRI Ross Center for Sustainable Cities at World Resources Institute.

Elizabeth Jane Wesley conceived and designed the analyses and wrote the technical note. Eric Mackres contributed substantially to the intellectual framework. Kurt Shickman, Clemens Janssen, and Theodore Wong provided intellectual contributions, while Madeline Mulder contributed data analysis.

## About WRI

World Resources Institute works to improve people's lives, protect and restore nature, and stabilize the climate. As an independent research organization, we leverage our data, expertise, and global reach to influence policy and catalyze change across systems like food, land and water; energy; and cities. Our 2,000+ staff work on the ground in more than a dozen focus countries and with partners in over 50 nations.

creative commons

Copyright 2026 World Resources Institute. This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of the license, visit https://creativecommons.org/licenses/by/4.0/

WORLD RESOURCES INSTITUTE

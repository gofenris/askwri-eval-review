---
doc_id: modeling-hyperlocal-heat-exposure-with-open-source-data
source_pdf: documents/modeling-hyperlocal-heat-exposure-with-open-source-data.pdf
extraction_method: postgres-full-text
parse_backend: mistral
parse_model: mistral-ocr-latest
char_count: 147096
title: Modeling Hyperlocal Heat Exposure With Open-Source Data
title_en: Modeling Hyperlocal Heat Exposure With Open-Source Data
authors: Ruth A. Engel; Kenn Cartier; Hyeji Joh; Zhuoyue Wang; Theodore Wong; Xiaojiang Li
date_published: 2026-03-17
year_published: 2026
article_type: Technical Note
wri_primary_office: WRI Global
language: en
languages: [en]
doi: 10.46830/writn.25.00018
status: searchable
summary: "This technical note models the Universal Thermal Climate Index (UTCI) at 1-meter resolution to help cities assess local heat exposure, using the SOLWEIG model and open-access data, achieving a mean absolute error of 0.39°C against LiDAR-based validation. Developed under WRI's Cool Cities Lab, it generates high-resolution UTCI, shade, and land-use data to guide the design and prioritization of heat-resilient infrastructure. The approach is applied to compare planning scenarios—such as tree planting, shade structures, and cool surfaces—by measuring their cooling potential in air temperature and UTCI across diverse urban settings."
---

![img-0.jpeg](img-0.jpeg)

WORLD
RESOURCES
INSTITUTE

TECHNICAL NOTE

# Modeling hyperlocal heat exposure with open-source data

Ruth A. Engel, Kenn Cartier, Hyeji Joh, Zhuoyue Wang, Theodore Wong, and Xiaojiang Li

CONTENTS

Abstract...1
Introduction...1
Modeling methods...3
Open-source input data...10
Results of open-source data use...13
Discussion...21
Conclusions...23
Appendix A...23
Appendix B...25
Appendix C...28
Abbreviations...33
Endnotes...33
Glossary...33
References...34
Acknowledgments...38
About the authors...38

Technical notes document the research or analytical methodology underpinning a publication, interactive application, or tool.

Suggested Citation: Engel, R.A., K. Cartier, H. Joh, Z. Wang, T. Wong, and X. Li. 2026. "Modeling hyperlocal heat exposure with open-source data." Technical Note. Washington, DC: World Resources Institute. Available online at doi.org/10.46830/writn.25.00018.

Abstract

Extreme heat is among the deadliest climate hazards worldwide, and its effects grow each year as cities become both hotter and more populous. For policymakers to design effective interventions to mitigate the effects of extreme heat, they require local-scale data on heat exposure. It is difficult and expensive to produce high-resolution intra-urban heat data, and many cities lack sufficient data to support heat-resilient planning. Here, we present a fully open-source method, usable worldwide, for modeling 1-meter thermal comfort in cities. We calculate the Universal Thermal Climate Index (UTCI) and other related metrics, such as shade cover and air temperature, using the open-source SOlar and LongWave Environmental Irradiance Geometry (SOLWEIG) model supported by freely available data sets. We model baseline heat conditions and also incorporate into the model achievable infrastructure changes to improve heat resilience. Our open-source UTCI results have a mean absolute error of 0.39°C when validated against modeled runs supported by lidar-derived data sets. This modeling approach can support realistic, actionable heat-resilience planning in cities globally.

Introduction

As global temperatures rise, cities are warming by about 4°C more than their surrounding regions (Zhao et al. 2021). Heat is consistently the deadliest environmental disaster, and expected harm is magnified as urban populations continue to grow (Brimicombe et al. 2024; Tong et al. 2021). In the face of this threat, cities are deploying urban design interventions, such as cool roofs, tree planting, and shade structures, to mitigate the effects of extreme heat (Gago et al. 2013). These methods can be effective both in lowering citywide temperatures and in providing local-scale heat protection for residents, leading to improved health outcomes (Macintyre and Heaviside 2019; Turner et al. 2023).

The role of local-scale heat data is critical in evaluating the need for and cooling potential of urban infrastructure interventions to mitigate the effects of

WORLD RESOURCES INSTITUTE

TECHNICAL NOTE | Version 1.0 | March 2026 | 1

extreme heat. Because heat fluxes and exposure can vary widely across and within cities, and because cities themselves vary greatly in numerous climatic, physical, and social dimensions, local data are necessary to understand the heat burden on people in the places where they live, work, and move (Guardaro 2023; Keith et al. 2021). Although high-quality, high-resolution heat data sets exist, they tend to be either proprietary or created from specific local data in an analysis particular to one place (Li et al. 2024; VITO n.d.). Land surface temperature (LST) can be calculated from freely available global data sets, including Landsat (1981–present; 30 meter [m]), the Ecosystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS; 2018–present, 70 m) by the National Aeronautics and Space Administration (NASA), and a collection of European Space Agency (ESA) satellites (1995–2020; 1 kilometer [km]). These LST products can be used to compare areas that emit different levels of heat from surfaces (ESA 2022; Landsat Missions n.d.; NASA 2025). LST is an incomplete metric to use in health analyses, though, because it provides a view of heat that is insufficient to demonstrate the connections between temperature and health (Muse et al. 2024; Guyer et al. 2021). Although air temperature can be a valuable metric (among several, including humidity, wind, and both natural and built environmental features) for understanding how people experience intra-urban heat, it is usually measured or calculated at a low spatial resolution (about 1 km) (Middel et al. 2021). Thermal comfort data are suitable for heat-health analysis, but global open-access products are only available at a very low spatial resolution (0.25 degrees) and exclude urban development parameters such as the effects of buildings and surfaces (Di Napoli et al. 2020). As such, there is no globally available open-access data set on local-scale heat suitable for understanding human heat exposure and guiding intervention design.

This critical gap in access to high-resolution heat exposure data can be bridged by deploying a thermal comfort model. *Thermal comfort* or *thermal sensation*, terms for any of several metrics expressing the combined contributions of multiple heat sources acting upon a person standing in space, are suited to very high-resolution analyses because of the emphasis on the conditions surrounding a human body (e.g., the effects of three-dimensional [3D] urban form on heat exposure through shade, surfaces, and changes to airflow) (Li et al. 2023; Middel and Krayenhoff 2019). In examining these data, we can assess the heat exposure of people in their 3D urban settings and therefore understand how hot they feel given their local conditions. Until recently, large-scale thermal comfort analyses have been unfeasible both because the modeling is complex and expensive and because input data must be very high resolution (greater than 5 m) and include 3D urban form data (Buo et al. 2023; Li et al.

2024). Recent advancements in both the development of models and the availability of very high-resolution global data have made it possible to model thermal comfort across multiple cities (Li et al. 2024).

Local-scale modeling of thermal comfort includes an evaluation of air temperature, which can also provide critical insights into heat exposure and variability across urban spaces; likewise, urban features like trees and surfaces can change the overall temperature in a neighborhood (Ballinas and Barradas 2016; Smith et al. 2025). Although these changes are often small—on the order of one or two degrees—even small changes in air temperature can affect the Universal Thermal Climate Index (UTCI), which is a metric of human-scale thermal exchange between people and their environment, and mean radiant temperature (Tmrt), which represents the cumulative thermal load on a human body in 3D space (Bunker et al. 2016; Kephart et al. 2022; Montiero dos Santos et al. 2024). High-resolution thermal comfort models rely on neighborhood-scale air temperature data sets, producing output data that can describe ambient air temperature and local heat exposure (which includes not only air temperature but also radiation, wind, and humidity) through the modeling process (Li et al. 2024).

Here, we present what is, to our knowledge, the first global open-source, high-resolution thermal comfort and heat-mitigation modeling framework. We combine robust, established scientific methods with globally available input data and novel scenario planning to demonstrate heat exposure risk and the potential for mitigating extreme urban heat through realistic interventions. This approach will make scientific data available worldwide for use in heat-resilience planning and policy.

We calculate UTCI at a 1 m resolution in urban areas. We focus on the afternoon, modeling UTCI at 12:00 (noon), 15:00 (3 p.m.), and 18:00 (6 p.m.) to capture a range of air temperature, radiative exposure, and shade across both the hottest and busiest parts of the day in most cities. By default, we calculate UTCI for the hottest day in the previous five-year period.

To produce UTCI, we employ a fully open-source implementation of the SOlar and LongWave Environmental Irradiance Geometry (SOLWEIG) model in a python framework (Li et al. 2024; Lindberg et al. 2018). SOLWEIG is a physical model that is widely used to calculate thermal comfort in cities worldwide. We first compile and standardize model input data sets (digital elevation model [DEM], building and ground digital surface model [DSM], tree canopy, land use, albedo, and meteorology) and then run SOLWEIG to produce the thermal comfort metric across the study area. We calculate UTCI from Tmrt using a statistical conversion that parameterizes air temperature

2 | ![World Resources Institute logo]() WORLD RESOURCES INSTITUTE

Modeling hyperlocal heat exposure with open-source data

(Tair) with Tmrt, humidity, and wind speed (Bröde et al. 2011; Thorsson et al. 2014). This process comprises a baseline assessment of hyperlocal (e.g., at a block scale or smaller) thermal comfort. We then take model outputs from several generalized scenarios for heat-resilient infrastructure interventions and calculate UTCI values for each of the scenarios (Wesley et al. 2026). In total, our analysis produces spatial shade location estimates and UTCI estimates at a 1 m resolution across three daily time steps and demonstrates how shade and UTCI values would change given identical meteorological conditions but different infrastructure. We also include methods for estimating the air temperature impacts of local infrastructure change (Krayenhoff et al. 2021) and use these air temperature changes to physically model estimated thermal comfort change based on local infrastructure changes. The full process is shown in Figure 1. Future work will build on these initial methods to develop a more complex coupled model framework to evaluate connections between infrastructure, air temperature, and thermal comfort (see “Further research” in the “Discussion” section). A glossary is also included that defines technical terms.

This technical note begins with an overview of the modeling framework, including the SOLWEIG model, the postprocessing conversion from Tmrt to UTCI, and the incorporation of heat-resilient infrastructure scenarios into the model. It then details the open-source data sets used as model inputs and discusses comparisons of both the input data sets and the modeled temperature data to lidar-derived data. Finally, the technical note provides information on data access and utility.

## Modeling methods

Our modeling setup relies on the SOLWEIG model, an open-source, physically based calculation of Tmrt (Lindberg et al. 2011a, 2018). We use SOLWEIG to produce estimates of heat exposure by calculating shade, Tmrt, and UTCI. SOLWEIG can be run in a python environment or through QGIS for a graphical interface. We also use SOLWEIG to estimate locations of tree and building shadows throughout our study areas using various input data sets (see Table 4). We use the SOLWEIG model’s output rasters to calculate UTCI through a statistical conversion from Tmrt and present both the UTCI rasters and the shadow rasters that are used to produce UTCI. Ultimately, we show a suite of metrics that provides local-scale information on heat exposure and the potential for implementing heat-resilient interventions (Table 1). Each metric is produced for three time steps (12:00, 15:00, and 18:00 local time, including consideration of daylight savings) on the hottest day in the five-year period before assessment to demonstrate change as air temperature, radiation, and shade shift over the

Table 1 | Metrics concerning outdoor heat exposure

|  METRIC | DESCRIPTION  |
| --- | --- |
|  Pedestrian-area UTCI | Mean UTCI in areas of the AOI that are not buildings or water  |
|  Park UTCI | Mean UTCI of park area within the AOI  |
|  Pedestrian-area shadows | Total shade area from buildings and trees in areas that are not buildings or water within the AOI, including all roads and private land  |
|  Park shadows | Total shade area from buildings and trees in parks within the AOI  |
|  Air temperature | Mean air temperature within the AOI  |
|  Air temperature change: reflective surfaces | Mean air temperature change associated with albedo increase from deployment of reflective surfaces within the AOI  |
|  UTCI change: reflective surfaces | Mean UTCI change associated with albedo increase from deployment of reflective surfaces within the AOI  |
|  Air temperature change: trees | Mean air temperature change associated with transpiration increase from tree planting within the AOI  |
|  UTCI change: trees | Mean UTCI change associated with shade from tree canopy and transpiration increase from tree planting within the AOI  |
|  Shade access | Mean distance from shade within the AOI  |

Notes: AOI = area of interest. UTCI = Universal Thermal Climate Index.

Source: WRI authors.

course of an afternoon within an area of interest (AOI)—either a high-priority neighborhood or a whole city.

The full modeling schematic is shown in Figure 1. This process involves the acquisition of open-source data; the assembly of model input layers; the modeling process, including preprocessing and postprocessing steps; and the model output data. All data sets align at a 1 m resolution in the locally appropriate Universal Transverse Mercator (UTM) projection. Each part of the process is detailed in this publication. Details on the creation of the input data sets for the infrastructure intervention scenario data can be found in the Wesley et al. (2026) publication by World Resources Institute (WRI).

TECHNICAL NOTE | March 2026 | 3

Figure 1 | Modeling schematic

![img-1.jpeg](img-1.jpeg)

Notes: The process involves acquiring open-source modeled input data as well as infrastructure scenario data (Wesley et al. 2026) and running the SOLWEIG model to ultimately produce shade and UTCI data in an AOI. Data from this process are published on the Cool Cities Lab platform. AOI = area of interest. DSM = digital surface model. ERA5 = European Centre for Medium-Range Weather Forecasts Reanalysis, version 5. FABDEM = Forest And Buildings removed Copernicus Digital Elevation Model. SOLWEIG = SOIar and LongWave Environmental Irradiance Geometry. Tair = air temperature. Tmrt = mean radiant temperature. UTCI = Universal Thermal Climate Index. UT-GLOBUS = University of Texas-GLOBAL Building Heights for Urban Studies. WRI = World Resources Institute.

Source: WRI authors.

## The SOLWEIG model

To model high-resolution thermal comfort, we deploy SOLWEIG, a physically based framework for calculating hyperlocal Tmrt (Lindberg et al. 2011a). The model uses urban form (ground, building, and tree elevation) as well as land use and meteorological forcing parameters to calculate Tmrt, a measure of the radiative exchange between a standardized representation of a human body and the environment around it (Gál and Kántor 2020).

We run the SOLWEIG model at a 1 m resolution supported by entirely open-source, globally available data sets to calculate human thermal comfort. We validate the model in Amsterdam, the Netherlands; Cape Town, South Africa; Monterrey, Mexico; and Rio de Janeiro, Brazil, and find a mean UTCI absolute error of 0.39°C at a pixel level across all comparison areas and times of day (see “Results of open-source data use”). We validate our

open-source thermal comfort results against results calculated from lidar-derived high-resolution data sets because we do not have access to in situ measurements that could support the validation. These cities were selected because they provide diverse urban environments, they have freely available lidar data that allow for accuracy assessments, and we have relationships with officials in these cities who can review the modeling outputs for their relevance to planning purposes. This model is particularly useful for cities that lack expensive and complex high-resolution 3D urban data. We display the output data sets for all cities on WRI’s Cool Cities Lab interactive application. We publish our code and methods to enable replicability. Independently, we examine accuracy of our input data sets, considering how errors in urban feature input data affect our results (e.g., poor building height estimates leading to erroneous estimates of shadow locations). For this comparison assessment, see “Results of open-source data use.”

4 | WORLD RESOURCES INSTITUTE

Modeling hyperlocal heat exposure with open-source data

We focus our analysis on the afternoon, examining results at 12:00, 15:00, and 18:00 to understand the change in shade and thermal comfort across the hottest parts of the day. This approach is consistent with other studies that examine heat exposure when both solar radiation and reradiated heat from surfaces are highest, and it also aligns with studies showing that heat model performance is strongest in the midday through afternoon (Gál and Kántor 2020; Middel and Krayenhoff 2019).

## Model input and output variables

The SOLWEIG model calculates Tmrt in a 3D urban space using several input and intermediate data sets (Lindberg et al. 2018). It requires raster files of a DEM and a building/ground DSM that show, respectively, the elevation of the earth's surface without and with built features. We create this building/ground DSM from an open-access ground DEM and a combination of multiple open-access building data sets (see 'Building footprint and height data'). These, in addition to a separate raster tree canopy height layer from a WRI/Meta global 1 m data set (Tolan et al. 2024), provide information on 3D forms and space (see 'Tree canopy and height'). A land use/land cover raster provides surface data that are used to calculate model

parameters for albedo, emissivity, and vegetation cover based on SOLWEIG's five categories: paved, buildings, grass, bare soil, and water (Lindberg et al. 2011b). Meteorological input data are compiled in a text file for the whole domain and include air temperature, incoming long- and shortwave radiation, wind speed (10 m height), relative humidity, local time of measurements, and offset from Coordinated Universal Time so that local time can be correctly calculated in the model. We use meteorological data from the hottest day in the five-year period before our assessment, and we use data from 12:00, 15:00, and 18:00 to support our analysis. SOLWEIG requires the DEM, building/ground DSM, and the meteorological data. It is designed to accept the tree canopy and land use data, but they are optional data sets—the model can be run with or without them. Wall albedo is handled in bulk, with a single parameter for each model run. Following the Li et al. (2023, 2024) implementation of SOLWEIG, we additionally include a raster albedo layer.

During model preprocessing, two intermediate data sets are produced using open-source tools released as part of the SOLWEIG package (Lindberg et al. 2011b). The first tool maps the height and aspect (angle) of building walls to create data sets that support shadow mapping. These maps are based

Note: Tmrt = mean radiant temperature.

|  VARIABLE | PURPOSE | FORMAT | STAGE OF USE  |
| --- | --- | --- | --- |
|  Digital elevation model (DEM) | Elevation of ground, without buildings or trees | Raster | Input  |
|  Digital surface model (DSM) of buildings and ground | Elevation of ground and buildings, without trees | Raster | Input  |
|  Tree canopy height and footprint | Elevation and area of tree canopy | Raster | Input  |
|  Land use | Surface characteristics | Raster | Input  |
|  Albedo | Surface characteristics (via Li et al. implementation) | Raster | Input  |
|  Meteorology | Air temperature, relative humidity, wind speed, incoming short- and longwave radiation, time, Coordinated Universal Time offset assessed at 12:00, 15:00, and 18:00 on the hottest day in the five-year period before assessment | Text derived from raster | Input  |
|  Sky view factor | Amount of sky visible across a day | Raster (daily) | Intermediate  |
|  Wall height and aspect | Wall data for calculation of shadows | Raster | Intermediate  |
|  Shadow | Shade from green and artificial sources | Raster | Output  |
|  Tmrt | Mean radiant temperature | Raster | Output  |

Note: Tmrt = mean radiant temperature.

Source: WRI authors.

TECHNICAL NOTE | March 2026 | 5

on the DEM and DSM, and they are not used outside of the creation of shadow maps within the modeling framework. The second tool calculates the sky view factor: the percentage of the sky directly visible from each pixel across the day based on the DEM, building/ground DSM, and tree canopy data sets. Sky view factor data are used to support and expedite shadow mapping in the final modeling process by creating preprocessed shade data for a whole day so that it does not need to be calculated each time the model is run.

We use two SOLWEIG output data sets: shade and Tmrt, each produced for the time steps at which the model is run. The shade layer contains pixels categorized as no shade, shade from buildings, and shade from trees from the time of analysis (Lindberg et al. 2018). Where building and tree shadows overlap, the model considers the pixels to be shaded by buildings; buildings let less light through to the ground than trees, so the shadows are more robust. The Tmrt layer shows estimated mean radiant temperature for each pixel.

All variables have the same spatial resolution and extent (Table 2). In this implementation of the model, we run data at a 1 m spatial resolution, and data sets are all resampled to match the same 1 m raster grid in an initial preprocessing step. Error is introduced because the DEM and albedo layers are a lower resolution than other input data sets, but the impact on the modeled UTCI is very minor (the error from the DEM is included in our comparison to lidar-derived data; see “Results of open-source data use”). To improve accuracy, lidar-derived elevation data or locally collected and validated high-resolution data sets for albedo, land use, or tree canopy can be used. For a full description of our input layers and their spatial resolutions and extents, see “Open-source input data.”

Following Li et al. (2023, 2024), we implement a Python setup of SOLWEIG. This implementation mirrors the physically based modeling dynamics and algorithms of the open-source QGIS-based implementation (Lindberg et al. 2011b, 2018) and is primarily a more efficient computing setup. The Li et al. implementation additionally accepts as input data a raster albedo layer that shows surface albedo. Previous instances of the model had hard-coded parameters that defined albedo values for each land use type. In this model implementation, we further expand on this framework to incorporate raster air temperature that allows for spatial variation in air temperature for each time step (12:00, 15:00, 18:00) on the day of analysis. At present, we deploy SOLWEIG with a single European Centre for Medium-Range Weather Forecasts Reanalysis, version 5, land data set (ERA5-Land) air temperature value from the appropriate time and date of analysis for the baseline run, as is customary for previous versions of the model, but we implement the air tem-

temperature raster capability to support future development efforts (see “Further research” in the “Discussion” section). We can thus assess UTCI across an area that has variable air temperature, such as a large city or a region where physical features create microclimates, in cases where higher-resolution air temperature data are available (though for this comparison process we use 0.1 degree resolution ERA5-Land air temperature value per study area).¹

While it may be possible to incorporate raster inputs for other climate variables in the future, we have not implemented this approach and still use one value in a text file for the whole study area as meteorological model inputs. There is currently no suitable data available for moderate-resolution meteorology and radiation data. The impact of gridded meteorology on modeled thermal comfort would be very minor.

## Calculating UTCI

Although Tmrt is a scientifically accepted measurement of human-scale thermal comfort, it is not a metric easily understood in policy because of its high value range when compared to air temperature: Tmrt can be between 40°C and 60°C when both Tair and UTCI are between 20°C and 35°C (Buo et al. 2023). UTCI is a similar metric of human-scale thermal comfort that quantifies the energy exchange between the human body and its surrounding environment (Fiala et al. 2012; Havenith et al. 2012). UTCI can be calculated from Tmrt through a statistical adjustment parameterized by wind speed, relative humidity, and air temperature (Bröde et al. 2011). The adjustment algorithm is widely used as a means of producing UTCI for large data sets (Bröde et al. 2021; Prasad and Satyanarayana 2024; van der Schrier 2021) and parameterizes an air temperature value using a sixth order approximating polynomial,

$$UTCI(Tair, Tmrt, va, rh) = Tair + offset(Tair, Tmrt, va, rh)$$

where $Tair$ is air temperature in degrees Celsius, $Tmrt$ is mean radiant temperature in degrees Celsius, $va$ is wind speed measured at 10 m elevation in meters per seconds, and $rh$ is relative humidity. The offset function is long, but it is available in papers concerning the development of UTCI (Bröde et al. 2011; Prasad and Satyanarayana 2024). We obtain these variables from the same source and at the same time as our meteorological variables for the SOLWEIG model.

6 | WORLD RESOURCES INSTITUTE

Modeling hyperlocal heat exposure with open-source data

## Modeling changes based on modeled heat-resilient interventions

We consider three different interventions for mitigating heat exposure—defined as infrastructure changes that use physical mechanisms to modify the energy balance—and we model shade and UTCI for each intervention. Our interventions include tree canopy expansion, shade structure construction, and surface albedo increase from cool roofs. Details on the design and assembly of some specific implementation scenarios for infrastructure interventions can be found in Wesley et al. (2026); they are derived from the same input data that are used to support the thermal comfort model and are designed to be relevant to and representative of existing heat resilience policies and heat action plans in a variety of cities. Our approach to modeling these interventions (e.g., shade structures) can be applied to a broad variety of deployment contexts (e.g., shade structures in parks, shade at transit stops, shade in market squares). We incorporate updated infrastructure data sets based on the scenarios in Wesley et al. (2026) that model tree planting, shade structures, and reflective surfaces. For each intervention, we change model input data to reflect the modeled changes made by Wesley et al. (2026) to physical infrastructure. We model tree canopy expansion using a new tree layer and updated air temperature values (for the current implementation, one updated air temperature value per AOI) due to the small cooling effect from increased evapotranspiration (see “Tree planting”). We model shadows and the change in UTCI from shade structures in an independent model run and merge the results with the shadows and UTCI from existing buildings and trees in postprocessing (see “Shade structures”). We use a statistical parameterization to calculate the change in air temperature from increased surface albedo and run SOLWEIG with new air temperature data (see “Surface albedo change due to implementation of cool roofs”). Table 3

describes the pre- and postprocessing of data to model potential infrastructure interventions using thermal comfort modeling.

For each intervention, we compare the updated UTCI and shade to the current baseline conditions by computing the average percentage of shade coverage and UTCI within pedestrian areas as well as the distance from shade for each 1 m pixel within parks. We note that, for the surface albedo intervention, shade does not change.

## Tree planting

Planting trees is a heat-resilience intervention that produces cooling benefits in two different ways. Most of the cooling contributions are due to additional shade from increased tree canopy (Middel et al. 2021). But trees can also lower daytime air temperature through evapotranspiration from the canopy (Meili et al. 2021). To account for increased shaded area, we run the model using an updated tree canopy layer, which includes additional trees drawn from a random sampling of the middle 50 percent of existing tree canopy profiles within a 100 m area (Wesley et al. 2026). This approach allows for flexible tree planting scenarios with various numbers and areas of modification depending on local conditions and policies. The updated model output demonstrates estimated changes to shadows and UTCI as a result of the altered tree canopy. To account for modified air temperature, we use values from Krayenhoff et al. (2021), a review paper examining the effects of albedo and tree canopy on air temperature, to parameterize expected changes to local-scale air temperature based on increased tree cover. We use the review’s median value of vegetative cooling efficiency calculated from 17 studies, and we reduce air temperature by 0.33°C per 0.1 fractional increase in tree canopy coverage over a given neighborhood or city. Although this value can vary across cities based on aridity and by neighborhood based on typical phenol-

Table 3 | Process of incorporating heat-resilient infrastructure interventions into thermal comfort modeling

|  INTERVENTION | PREPROCESSING OF INPUT DATA FOR THE SOLWEIG MODEL | POSTPROCESSING AFTER THE SOLWEIG MODEL  |
| --- | --- | --- |
|  Tree canopy | Tree canopy height and footprint; air temperature value | No postprocessing steps  |
|  Shade structures | Shade structure height and footprint | Integration of shade from structures with shade from buildings and trees  |
|  Surface albedo | Air temperature value | No postprocessing steps  |

Note: SOLWEIG = SOlar and LongWave Environmental Irradiance Geometry.

Source: WRI authors.

TECHNICAL NOTE | March 2026 | 7

Figure 2 | Schematic for modeling artificial shade structure shadows and UTCI with SOLWEIG

![img-2.jpeg](img-2.jpeg)

Infrastructure

- Buildings
- Trees
- Shade structures

SOLWEIG shadow value

- 0
- 0.03

Notes: The process involves the following:

a. Assembling baseline model input layers, including buildings and trees.
b. Running the SOlar and LongWave Environmental Irradiance Geometry (SOLWEIG) model to calculate baseline shade and the Universal Thermal Climate Index (UTCI) from buildings (transmissivity = 0) and trees (transmissivity = 0.03).
c. Modeling shade structure placement (Wesley et al. 2026).
d. Running SOLWEIG to calculate shade and UTCI from buildings (transmissivity = 0) and shade structures (transmissivity = 0), using shade structures as an alternative, opaque "tree canopy" layer (without including the actual tree canopy layer) to capture a roof with no walls.
e. Running SOLWEIG (again without the actual tree canopy layer) to calculate shade from buildings (transmissivity = 0) and shade structures (transmissivity = 0.03), producing a mask layer that allows shade structure shadows to be differentiated from building shadows.
f. Clipping shade structure shadows and UTCI (transmissivity = 0) from layer (d) using the mask layer (e).
g. Adding the shade and UTCI results from shade structure shadows (transmissivity = 0) into the baseline layer with results from buildings and trees.
Our approach is cumbersome but effective in allowing for SOLWEIG runs with three different types of features that create shade (buildings, trees, and shade structures).
Source: WRI authors.

8 | WORLD RESOURCES INSTITUTE

Modeling hyperlocal heat exposure with open-source data

ogy, the variations are small and there is not currently a method for assessing relationships between tree canopy and air temperature in individual cities using globally available open-access data.

## Shade structures

Shade structures create cool refuges in public spaces. The types of shade structures we model are based on existing structures deployed in parks globally at relatively low cost (Wesley et al. 2026). A constraint of the SOLWEIG model is that it can only accept buildings that have walls; any human-constructed feature in the building/ground DSM input layer will be seen by the model as a structure with four walls. To overcome this obstacle and model shade from structures that have a roof but no walls, we use a raster showing the height and footprint of shade structures as an alternate “tree canopy” input layer within the model separately from input tree data, creating features that have a square, flat roof but no walls.

We run SOLWEIG without the tree canopy layer and instead use the input map of the modeled shade structures from Wesley et al. (2026) as a tree canopy layer with the transmissivity of light through the canopy set to a value of 0, indicating that no light passes through the roof of the shade structure. In this way, we can approximate a roof in the form of an opaque tree, allowing for the calculation of shade below and around the structure without interference from walls. We note that, unlike additional trees in the tree canopy intervention, shade structures do not produce any change to air temperature, so meteorological input data remain unchanged.

The most complex part of incorporating shadows from structures is isolating them from existing building and tree shade in order to integrate them back into a shade map that has both trees and buildings without introducing additional errors (Figure 2). In particular, it is difficult to isolate shade structure shadows from building shadows because both show a value of 0 in the shade layer produced by SOLWEIG, indicating that no light permeates the canopy. To achieve the best results, it is important to include buildings alongside the shade structures; therefore, if a pixel is shaded by buildings as well as the shade structure at any point during the day, we can capture its diurnal sun exposure. To isolate the individual areas shaded by our shade structures, we create a mask layer that shows the exact same shadows (again, without the actual tree layer) but has a different value in the SOLWEIG shade output layer. This mask layer is achieved by running the model again but treating the shade structures as trees with a canopy that allows for sunlight transmissivity; we use the model default value of 3 percent (0.03), thereby ensuring that the SOLWEIG shade layer will have a value of 0 for building shade and 0.03 for shade structure

shade. We note that, because 0.03 is only intended for masking, any transmissivity value could have been used. The purpose of this step is only to create a mask layer of all shadows from shade structures. This approach is cumbersome because it involves running the model twice: once for the actual shadow and UTCI values and once for the mask layer. However, it ensures that we can integrate shadows from the shade structures, and the UTCI values within those shadows, with the baseline data with building and tree shadows to get the model output that includes shade structures. Ultimately, we can use SOLWEIG, a model that traditionally only accepts walled buildings and trees, to achieve results for a landscape with walled buildings, trees, and shade structures (Figure 2).

Once we have both the actual shadow and UTCI data for shade structures and the mask layer showing shadows from the shade structures as being differentiable from building shadows, we join the shade structure shadows and UTCI (derived from the run where transmissivity = 0) to the original model run with the original tree canopy layer, showing shadows from buildings and trees in the area. We therefore achieve a landscape showing baseline shade from buildings and trees as well as additional shade from modeled shade structures. Where shade structure shadows overlap tree shadows, we prioritize shade structure shadows because the quality of shade is higher from an opaque roof than from a permeable tree canopy (Lindberg et al. 2011b). Where shade structure shadows and building shadows overlap, the quality of the shade is equal, and the model considers how long the pixels have been shaded.

## Surface albedo change due to implementation of cool roofs

High-albedo rooftops reflect more radiation and absorb less radiation than low-albedo materials; therefore, they retain less heat to reradiate into the lower atmosphere. Through the albedo raster layer, SOLWEIG captures changes to radiation and thermal comfort at a rooftop level, but it does not adjust air temperature based on large-scale urban albedo change. Following Krayenhoff et al. (2021), we use changes in roof albedo to parameterize the modeled change in air temperature for the meteorological data that we use as input to the SOLWEIG model, collected from ERA5 reanalysis on the hottest day in the five-year period before assessment (Hersbach et al. 2020). Drawing on values from the review by Krayenhoff et al., we estimate air temperature at noon according to albedo change within a neighborhood from cool roof deployment—the time of day for which there is comparative data collected and published (Krayenhoff et al. 2021). We follow the median value from the review by Krayenhoff et al., which is a 0.6°C decrease in air tem-

TECHNICAL NOTE | March 2026 | 9

perature per 0.1 increase in average albedo across a study area. The range of albedo impact in the review shows a 0.17–0.87°C decrease in air temperature per 0.1 increase in average albedo, so our assumption does not run the risk of large deviations from the most extreme parameter estimates, even across cities with different amounts of sunlight or urban compositions.

We parameterize this noon value to estimate values for 15:00 and 18:00 based on results from the Weather Research and Forecasting (WRF) model's Building Effect Parameterization calculation examining interactions between rooftop albedo and air temperature at different times of day (Broadbent et al. 2020; Krayenhoff et al. 2021; Skamarock and Klemp 2008). Our time step parameterizations are as follows,

$$dT_{15:00} = 0.935315 * dT_{12:00}$$
$$dT_{18:00} = 0.646853 * dT_{12:00}$$

where $dT$ is the change in air temperature at a particular time of day from the measured baseline air temperature to the air temperature with changed albedo. We adjust the input air temperature to the SOLWEIG model using the calculated change, and we rerun the model with the adjusted air temperature values. The updated results demonstrate modified UTCI resulting directly from the albedo change of surfaces and indirectly from the air temperature change due to albedo modification. This parameterization introduces errors across cities because of differences in solar azimuth based on longitude and date of calculation. Because the changes are extremely small, and in anticipation of an updated air temperature/albedo model within six months, we use this methodology to show a proof of concept for modeling the effects of albedo change in SOLWEIG.

## Open-source input data

This approach constitutes—to the best of our knowledge—the first implementation of a thermal comfort model run using only globally available open-source data. Because our goal is to provide the most complete and highest-quality data possible, we set and evaluated four criteria for input data selection: use the highest spatial resolution possible, get the best accuracy possible, require global or near-global coverage, and ensure open-source licensing (Table 4).

### Ground elevation

For a ground DEM, we use the Forest And Buildings removed Copernicus DEM (FABDEM) void-filled data set derived from the Copernicus 30-meter Global (GLO30) DEM (Hawker et

al. 2022). The data set is produced using a random forest model to remove noise and features, such as trees and human settlements, from the Copernicus DEM, itself a 30 m global DEM based on the 2011–15 TanDEMX survey and found to be the most recent, high-resolution, and accurate DEM of globally available products (ESA 2024; Grohmann 2018; Guth and Geoffroy 2021).

The absolute mean error of FABDEM in urban environments is 1.12 m, and it has proved to be more accurate than both the Copernicus data set from which it is derived and other comparable DEM data sets, including the Advanced Land Observing Satellite (ALOS) Phased Array L-band Synthetic Aperture Radar (PALSAR) and the 30 m NASA DEM (Meadows et al. 2024; Osama et al. 2023). We note that, as of publication, no global open-source DEM data sets exist at a resolution higher than 30 m.

To resample the DEM to 1 m, we use linear convolutional gaussian blurring to interpolate between the centroids of pixels (Abdalla and Elmahal 2016; Pathmanabhan and Dinesh 2007). This approach accounts for variation in pixel clusters and avoids bias toward peaks and valleys while interpolating linearly between neighboring pixels.

Ground elevation data sets are an independent input into SOLWEIG, but they also form the basis for the building/ground DSM. We use the DEM's surface as a baseline upon which building footprints and heights can be added to construct the building/ground DSM. The 30 m DEM can introduce errors in high-slope areas because a single value will be assumed for a 30 m area. Because the DEM is used as a ground surface upon which shadows are cast, however, these errors will only be relevant in particularly high-slope places.

### Building footprint and height data

To produce building data, we combine building footprint polygons with building height information. For each building, we assume one height, as no data sets currently support more complex roof design. We gather building footprints from Overture Maps, a nonprofit organization that compiles building data from OpenStreetMap, Google Open Buildings, and Microsoft Building Footprints (Overture Maps 2025). Overture Maps compiles the most complete and up-to-date building footprint data set globally (Wesley et al. 2026).

For building heights, we use multiple data sources to obtain the best available data. Our primary source of building height data is the University of Texas–GLOba Building heights for Urban Studies (UT-GLOBUS) data set. UT-GLOBUS applies a random forest classifier, trained on lidar data, to Ice,

10 | WORLD RESOURCES INSTITUTE

Modeling hyperlocal heat exposure with open-source data

Table 4 | Open-source SOLWEIG input data sets

|  VARIABLE | DATA SET | DATA FORMAT | YEAR | EXTENT | SOURCE  |
| --- | --- | --- | --- | --- | --- |
|  Ground elevation | Forest And Buildings removed Copernicus Digital Elevation Model (FABDEM) | 1 arc second raster | 2015 | Global | Hawker et al. 2022  |
|  Building footprints | Overture Maps Foundation (primarily OpenStreetMap; Google Open Buildings; Microsoft Building Footprints combined by Overture Maps) | Polygons | 2024 | Global | Overture Maps 2025  |
|  Building heights | University of Texas-GLOBAL Building heights for Urban Studies (UT-GLOBUS); Overture Maps Foundation (OpenStreetMap; Google Open Buildings; Microsoft Building Footprints); Global Human Settlement Average Net Building Height (GHS ANBH) | Polygons (UT-GLOBUS, Overture Maps); 30 meter (m) raster (Global Human Settlement Layer) | 2024; 2018 | 12,000 cities^{a}; global | Kamath et al. 2024; Overture Maps 2025; Pesaresi and Politis 2023  |
|  Tree canopy height and footprint | World Resources Institute (WRI)/Meta Global Canopy Height Maps | 1 m raster | 2020 | Global | Tolan et al. 2024  |
|  Land use | WRI OpenUrban | 1 m raster | 2024 | 50 cities^{b} | Wesley et al. 2026  |
|  Albedo | Sentinel-2 | 10 m raster | 2017–present | Global | Saunier et al. 2022  |
|  Meteorology | European Centre for Medium-Range Weather Forecasts Reanalysis, version 5 (ERA5) | 0.1 degree raster | 1950–present | Global | Hersbach et al. 2020  |

Notes:

a. UT-GLOBUS coverage is currently being expanded.

b. OpenUrban data coverage is currently being expanded and can be generated in cities globally.

Sources: Hawker et al. 2022; Hersbach et al. 2020; Kamath et al. 2024; Overture Maps 2025; Pesaresi and Politis 2023; Tolan et al. 2024; Wesley et al. 2026.

Cloud, and land Elevation Satellite 2 (ICESat-2) and Global Ecosystem Dynamics Investigation (GEDI) altimetry data to produce building heights in more than 1,200 cities with a root mean squared vertical error of 9.1 m when compared to lidar data (Kamath et al. 2024). Our analyses show that the data set is the most complete and accurate building height currently available across a large number of cities, and it is currently being expanded to more cities (see analyses in Appendix B). It is specifically designed to support urban climate analyses, and it mentions SOLWEIG as a primary application of the data (Kamath et al. 2024). Although UT-GLOBUS does include building footprints as well as heights, its data set is less robust than Overture Maps. In particular, UT-GLOBUS takes the maximum footprint of buildings without accounting for complex building features, like interior courtyards, which can usually be found in Overture footprints.

To create unified building footprint and height polygons, we combine Overture footprints with our building heights. We first

filter building polygons to eliminate spatially invalid polygons that constitute errors in the source data set. We then rasterize UT-GLOBUS polygons to a 1 m resolution. For each Overture polygon, we select a building height by taking the mode value of UT-GLOBUS building heights that overlap the polygon. Where UT-GLOBUS does not have data, we use building height data from Overture Maps. These building heights, like Overture's building footprints, are a composite of data from Google Open Buildings, Microsoft Building Footprints, and OpenStreetMap. We draw from two sources of building height from Overture: where possible, we use the building height; otherwise, we use the number of building stories and multiply the value by 3.5 m to obtain an estimated building height (CTBUH n.d.). For buildings under 50 m² that lack height data from either UT-GLOBUS or Overture, we assume one story and assign a height of 3.5 m (CTBUH n.d.). For larger buildings that lack height data, we use the Global Human Settlement Average Net Building Height (GHS ANBH), calculated at 30 m from ALOS World 3D and Shuttle Radar Topography

TECHNICAL NOTE | March 2026 | 11

Figure 3 | Building height selection process

![img-3.jpeg](img-3.jpeg)

Notes: The building height is added to ground elevation to achieve the building and ground digital surface model used by the SOlar and LongWave Environmental Irradiance Geometry (SOLWEIG) model. GHS = Global Human Settlement layers. UT-GLOBUS = University of Texas-GLOBAL Building heights for Urban Studies.

Source: WRI authors.

Mission (SRTM) data (Pesaresi and Politis 2023). Accordingly, we can obtain global coverage of building heights using the best available data. Figure 3 shows the process of selecting a building height.

The mean absolute error of our data on building heights across all comparison cities is 2.38 m when compared to lidar data in five diverse urban neighborhoods (for a full description of lidar data and comparison AOIs, see “Results of open-source data use”). The mean bias error is 1.17 m across our data sets, indicating a general overestimation of building height, likely due to a tendency in the UT-GLOBUS data to prefer the highest point of a building in estimations. On average among our comparison areas, 90 percent of buildings fall within an error range of 7.78 m (Table 5). Building heights show more variability in Amsterdam and Rio de Janeiro, where our data include an urban core, than in Monterrey. Monterrey II, a wealthier AOI with more residential buildings, has a much lower average error than other regions. Overall, building heights are accurate on most buildings, but occasionally very inaccurate. Errors are most common in downtown or commercial areas.

## Tree canopy and height

We use the 1 m resolution WRI/Meta Global Canopy Height Maps to provide data on tree canopy extent and height (Tolan et al. 2024). The data set was created by training the Self-Distillation with NO Labels version 2 (DiNOv2) deep learning model on high-resolution aerial Maxar imagery collected between 2009 and 2020, with 80 percent of data obtained between 2018 and 2020. It has a mean absolute vertical error of 2.8 m. This data set is the only one of its kind that currently exists.

## Land use and albedo

To assess land use, we rely on the 1 m resolution WRI OpenUrban land use/land cover data set (Wesley et al. 2026). The data set derives primarily from OpenStreetMap land use categories, with supporting definitions from ESA’s WorldCover, WRI’s Intra-Urban Land Use classifications (Guzder-Williams et al. 2023), and the GHS ANBH. The OpenUrban data set has an 83 percent overall accuracy across global cities.

To incorporate OpenUrban data into the model, we aggregate land use to match the SOLWEIG land use categories. Accordingly, land use classification accuracy likely improves, compared to the standard OpenUrban classes, as the data are grouped:

Table 5 | Average error in the open-source building height data compared to lidar-derived building heights

|  CITY | MEAN ERROR (M) | MEAN BIAS ERROR (M) | ERROR RANGE-90% OF DATA (M)  |
| --- | --- | --- | --- |
|  Amsterdam | 3.96 | 1.89 | 10.43  |
|  Monterrey I | 3.00 | 0.51 | 6.05  |
|  Monterrey II | 1.61 | 1.24 | 6.01  |
|  Monterrey III | 2.13 | 1.19 | 5.74  |
|  Rio de Janeiro | 8.39 | 1.05 | 10.65  |
|  **Average** | **3.82** | **1.18** | **7.78**  |

Source: WRI authors.

12 | WORLD RESOURCES INSTITUTE

Modeling hyperlocal heat exposure with open-source data

**Table 6 | Reclassification of OpenUrban to match SOLWEIG land cover input**

|  SOLWEIG CATEGORY | OPENURBAN CATEGORIES  |
| --- | --- |
|  Paved | Roads, parking, built up (other)  |
|  Buildings | Residential buildings, nonresidential buildings, unclassified buildings  |
|  Grass | Public open space, green space  |
|  Bare soil | Barren  |
|  Water | Water  |

Note: SOLWEIG = SOlar and LongWave Environmental Irradiance Geometry.

easily confused categories, such as open and green space or parking and built-up area, are combined into broader classes. Table 6 shows how we aggregate the OpenUrban land use data.

*Land use* in SOLWEIG excludes the presence of trees because tree canopy is included separately in its own layer. Rather, *land use* applies to ground conditions—the areas underneath and around trees—to provide information on urban surfaces. The model's land use categories allow for bulk handling of surface materials and their emissivity. To further improve the model's handling of surface reflectance in addition to the basic parameters drawn from land use, we follow Li et al. (2024) and include an input albedo raster separately from our land use raster. We use Sentinel-2 albedo (10 m) calculated using the narrow-to-broad band coefficients from Bonafoni and Sekertekin (2020) during summer months (June–August in the northern hemisphere; December–February in the southern hemisphere), resampled to match our 1 m input data.

## Meteorology

We use Copernicus ERA5-Land reanalysis data at 0.1 degree resolution (about 9 km at the equator) to force the model (Hersbach et al. 2020). SOLWEIG is designed to accept one value for each meteorological variable per AOI. If an AOI crosses ERA5 pixels, we take the value from the pixel with maximum coverage to form the single input value. ERA5 is available globally from 1950–present and provides a wide array of estimated meteorological variables. We use air temperature, relative humidity, incoming short- and longwave radiation, and wind speed at 10 m elevation at each of three time steps: 12:00, 15:00, and 18:00. ERA5 data sets have $R^2$ values between 0.85 and 0.91 when compared to sensor data, and they outperform similar

data sets (Kara and Elbir 2025). Meteorological conditions can be selected by using any number of parameters based on the goals of the modeling run. For our default parameter selection, designed to demonstrate extreme but realistic heat conditions, we obtain air temperature data for the last five years (2020–25) and choose the day with the hottest average temperature. We use meteorology from that day as forcing data for the model.

## Results of open-source data use

Our open-source modeling approach is suitable for incorporation into planning processes, to aid in understanding of heat exposure across a neighborhood or city, and to evaluate the potential impacts of heat-resilient infrastructure changes. Our UTCI and shade products provide valuable insights into trends within and across cities, comprising a more robust and high-resolution heat data set than has been previously available in any city lacking lidar data. The data are not suitable for siting individual interventions that depend on the accuracy of individual urban features (e.g., specific tree points). Accordingly, we do not expect the accuracy of our data to match or exceed the accuracy of lidar-supported modeling approaches; rather, we aim to verify that our data are useful for citywide or neighborhood-scale analyses.

SOLWEIG has been validated by numerous hyperlocal studies to investigate accuracy across diverse climatic and urban conditions (Buo et al. 2023; Chen et al. 2016; Gál and Kántor 2020; Jin et al. 2021; Kim et al. 2022; Thom et al. 2016). Currently, SOLWEIG is often deployed without independent, measured validation and is sometimes used as a point of comparison for novel methods (Colaninno et al. 2024; Ding et al. 2024; Evola et al. 2021; Jänicke et al. 2016; Kong et al. 2022; Li et al. 2024; Thorsson et al. 2014; Wallenberg et al. 2020). Accordingly, we rely on the widely accepted use of the model to produce our data without independent ground-truth comparison data for each study area. In independent validation against in situ measurements, SOLWEIG produces results with $R^2$ values greater than 0.9 (Briegel et al. 2023; Chen et al. 2016; Gál and Kántor 2020; Lau et al. 2016). It is not possible in this case to obtain observed validation data for our model implementation; no observed thermal comfort data sets are available for comparison, and collecting new observations for this is expensive and was beyond the scope of this study. See Appendix A for a more detailed discussion.

The primary obstacle to SOLWEIG's accuracy is the accuracy of input data, particularly specific 3D urban form variables. While SOLWEIG is widely used in the field of heat modeling, it is highly dependent on input data, which significantly

TECHNICAL NOTE | March 2026 | 13

affects the level of accuracy of model predictions. When urban feature data sets contain errors in the placement or completeness of buildings, trees, or land use, modeled temperature output is similarly prone to error (Li et al. 2024). Likewise, accuracy can be impeded by poor input meteorological data from weather stations, which can be placed far from a study site, or from reanalysis products, which often have a resolution greater than 1 km (Lau et al. 2016). In the three cities (Amsterdam, Monterrey, and Rio de Janeiro) we examine the accuracy of both open-source building input data and modeled UTCI against lidar-derived products and UTCI to understand model performance and utility with imperfect input data (“Comparison to lidar-derived datasets” and “Comparison of shade data”).

## User engagement

This modeling process was developed in collaboration with partners in city governments across seven countries who met regularly with WRI team members to discuss goals, data gaps, and critical questions related to urban heat resilience. Local partners have contributed to assessments of the utility and local relevance of data. The user engagement team has worked with 27 heat experts and 170 potential data users in more than 10 countries through workshops and one-on-one meetings.

Our approach is, therefore, in part supported by the user engagement process that has enabled methods development, quality assurance, and validation in partnership with cities. In meetings with city officials throughout the development process, we clarified their goals in obtaining and interpreting heat data that can be met by this project, including the acquisition of higher-resolution intra-urban heat data that was previously available, a way to connect temperature data to health outcomes, and obtaining data to support both planning for heat-resilient interventions and ways to pitch these strategies to other city officials. For three months following a closed-beta launch of the data sets, we met with city officials to provide them access to the data and to interview them about whether the data sets clearly addressed the identified needs.

This process allowed for confirmation that the data are suitable for their intended uses, ensuring that our data products and descriptions of metrics enabled an understanding of heat exposure and the potential for heat-resilience planning without implying endorsement of site-specific intervention placement. Users identified multiple applications of the data. Some considered that it is useful to understand the UTCI impacts of interventions, such as the cooling potential of trees versus shade structures, so that the utility of heat action planning can be anticipated and quantified. Others reported that the data could be used at a neighborhood scale to identify high-priority

areas for various types of interventions. Several users said that the data could be helpful in justifying and securing funding for heat action planning. Most users described the baseline UTCI assessment as important for understanding how hot a person feels in the sun, in the shade, and across different types of urban spaces. In consultation with city officials, we developed specific map visualizations and metrics that supported appropriate use of the data.

Users clarified that UTCI and shade are most useful when shown in pedestrian areas within or across high-priority neighborhoods where cities know that residents are exposed to heat. They also expressed that complex scientific metrics, notably albedo, are difficult to understand, and so infrastructure might be best described more simply (e.g., “area of increased cool roof coverage” rather than “increased roof albedo”). Finally, users contributed substantially to the order in which we show different data sets, presenting infrastructure changes such as shade structures, then the effects infrastructure change can have on the physical environment like shaded areas, and then the effects of infrastructure change on people through UTCI. This flow of data allows users to understand the mechanisms of change deriving from infrastructure (e.g., that shade structures provide cooler, consistently shaded areas that people can use as refuges from heat) and connect data layers to one another.

Most importantly, this user research process provided validation that the data were legible enough to be useful to diverse audiences and that our presentation clearly communicated ways in which the data are intended (and are not intended) for use.

## Comparison to lidar-derived data sets

The SOLWEIG model is traditionally run using 3D urban form data derived from high-resolution lidar data that provide ground and building elevation—and, in some cases, tree canopy elevation—at a horizontal spatial resolution less than or equal to 5 m (Buo et al. 2023; Li et al. 2024). High-resolution lidar data are expensive to acquire and difficult to process; thus, such data are only gathered infrequently in certain cities or parts of cities and predominantly exist in developed countries. We have gathered lidar data showing ground and building elevations in areas of interest in three cities: Amsterdam, Rio de Janeiro, and Monterrey. Our AOIs are in cities engaged on heat work and comprise areas that are suitable for intra-urban heat action analyses as determined by user engagement. We have one comparison area in Amsterdam and one area in Rio de Janeiro where lidar data have been rasterized to 1 m, each in a high-priority area of the city for heat-resilience planning. In Monterrey, though, we have consulted with WRI Mexico’s user engagement team to select three AOIs for heat interventions with different urban

14 | ![World Resources Institute logo]() WORLD RESOURCES INSTITUTE

Modeling hyperlocal heat exposure with open-source data

Figure 4 | Shadows in Rio de Janeiro at 12:00, 15:00, and 18:00 at a 1 m resolution derived from the open-source data and lidar-derived data

![img-4.jpeg](img-4.jpeg)

Notes: Differences in building footprint and height can produce different shadow patterns. Where building and tree shadows overlap, the model prioritizes building shade because it is more robust.

Source: WRI authors.

TECHNICAL NOTE | March 2026 | 15

characteristics because we have more abundant lidar data that the WRI Mexico team has rasterized to a 1 m resolution. In these five AOIs, we validate our open-source building height data used as input for the SOLWEIG model as well as shade and UTCI output data by comparing model runs based on our open-source data to ones based on the lidar-derived DSMs (all of which had classified building, tree, and ground points, allowing for extraction of building heights).

We perform comparisons in these five AOIs, selected from available lidar data provided by cities to demonstrate diversity in region, urban form, and socioeconomic status. The Rio de Janeiro AOI is a dense neighborhood near the water and an airport that has dense development and substantial tree cover.

The Amsterdam AOI is a mixed-use neighborhood with lower-rise buildings and serves as a model for an older European style of development. Monterrey I is an area in the city's downtown business district. It comprises some residential buildings as well as high rises, a park, and a large cemetery. This district represents substantial diversity in its built environment. Monterrey II is a high-income residential part of the city, with abundant tree coverage. Identified as an AOI because of its existing good practices for heat resilience, Monterrey II can serve as a region to understand a more homogeneous, upper-class neighborhood with lower-rise buildings. Monterrey III is a lower-income part of the city, with both residential and low-lying commercial buildings. It also has informal settlements and can therefore

Table 7 | User's and producer's accuracy with kappa scores for 12:00, 15:00, and 18:00 in each city

|  TIME | SHADE TYPE | METRIC | RIO DE JANEIRO | MONTERREY I | MONTERREY II | MONTERREY III | AMSTERDAM | MEAN  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  12:00 | Building shade | U_accuracy | 0.70 | 0.15 | 0.25 | 0.33 | 0.68 | 0.42  |
|   |   |  P_accuracy | 0.51 | 0.07 | 0.12 | 0.07 | 0.69 | 0.29  |
|   |  Tree shade | U_accuracy | 0.90 | 0.91 | 0.91 | 0.77 | 0.72 | 0.84  |
|   |   |  P_accuracy | 0.92 | 0.92 | 0.91 | 0.82 | 0.57 | 0.83  |
|   |  No shade | U_accuracy | 0.85 | 0.94 | 0.95 | 0.91 | 0.79 | 0.89  |
|   |   |  P_accuracy | 0.93 | 0.97 | 0.97 | 0.97 | 0.90 | 0.95  |
|  15:00 | Building shade | U_accuracy | 0.78 | 0.27 | 0.25 | 0.36 | 0.84 | 0.50  |
|   |   |  P_accuracy | 0.56 | 0.17 | 0.20 | 0.15 | 0.60 | 0.33  |
|   |  Tree shade | U_accuracy | 0.89 | 0.86 | 0.89 | 0.74 | 0.77 | 0.83  |
|   |   |  P_accuracy | 0.92 | 0.89 | 0.89 | 0.80 | 0.90 | 0.88  |
|   |  No shade | U_accuracy | 0.86 | 0.92 | 0.93 | 0.91 | 0.83 | 0.89  |
|   |   |  P_accuracy | 0.95 | -0.95 | 0.94 | 0.97 | 0.93 | 0.57  |
|  18:00 | building shade | U_accuracy | 0.86 | 0.50 | 0.58 | 0.60 | 0.89 | 0.68  |
|   |   |  P_accuracy | 0.76 | 0.46 | 0.56 | 0.50 | 0.67 | 0.59  |
|   |  Tree shade | U_accuracy | 0.78 | 0.64 | 0.82 | 0.52 | 0.76 | 0.70  |
|   |   |  P_accuracy | 0.81 | 0.72 | 0.83 | 0.64 | 0.90 | 0.78  |
|   |  No shade | U_accuracy | 0.73 | 0.80 | 0.84 | 0.75 | 0.78 | 0.78  |
|   |   |  P_accuracy | 0.86 | 0.80 | 0.84 | 0.80 | 0.91 | 0.84  |
|   |   | **Kappa score** | **0.830** | **0.832** | **0.864** | **0.814** | **0.785** | **0.825**  |

Notes: The unweighted kappa coefficient averaged across all times of day is 0.825, and the average kappa coefficient weighted by sample count is also 0.825. P = producer. U = user.
Source: WRI authors.

16 | WORLD RESOURCES INSTITUTE

Modeling hyperlocal heat exposure with open-source data

**Table 8 | Percentage of shade coverage across nonbuilding, nonwater land at 12:00, 15:00, and 18:00 in each comparison AOI using open-source data and lidar-derived data**

|  AREA OF INTEREST | OPEN SOURCE: 12:00 | LIDAR: 12:00 | OPEN SOURCE: 15:00 | LIDAR: 15:00 | OPEN SOURCE: 18:00 | LIDAR: 18:00  |
| --- | --- | --- | --- | --- | --- | --- |
|  Rio de Janeiro | 44.13 | 38.92 | 44.35 | 38.59 | 68.33 | 63.03  |
|  Monterrey I | 18.64 | 16.12 | 21.63 | 18.92 | 41.02 | 40.49  |
|  Monterrey II | 17.74 | 15.77 | 20.38 | 18.93 | 38.80 | 38.16  |
|  Monterrey III | 15.27 | 9.95 | 17.90 | 12.62 | 40.78 | 37.03  |
|  Amsterdam | 62.39 | 57.01 | 52.08 | 46.30 | 61.05 | 54.73  |

Source: WRI authors.

serve as an indicator of how data might look when buildings are irregular and difficult to assess with global data.

## Comparison of shade data

We validate the performance of models in each city individually and aggregate the results against the ground truth of the lidar-derived data (Table 7). We consider the accuracy of our data across the course of the afternoon as both overall solar radiation and the size and locations of shadows change. Because our shade data are categorical (no shade; building shade; tree shade), we employ a confusion matrix to assess the accuracy of our classification of shade data. Where a pixel is shaded both by a building and a tree, the model prioritizes building shade because it is more robust. We calculate the user's and producer's accuracy for each shade type at each time step to look at the likelihood that our predicted shade type is accurate and the likelihood that each shade type will be accurately predicted. We then calculate a kappa coefficient weighted by coverage of each shade type to show comparisons between observed and expected accuracy beyond random chance (Vieira et al. 2010). Figure 4 shows examples of our shade data from Rio de Janeiro to demonstrate discrepancies between building footprints and heights across the open-source versus lidar-derived data sets and ways in which they can result in shadow errors.

Our shade comparison is conducted for all 1 m pixels of our comparison area that are not buildings or water; in other words, we assess the land area in which people might plausibly spend time. We eliminate water and buildings from the analysis because they are large and often unshaded, and they might inflate our comparative statistics.

Averaged across the comparison AOIs, our kappa score for shade type assessed at 1 m resolution is 0.825 with all comparison areas weighted equally, where 0 indicates no agreement and 1 indicates perfect agreement (Table 7). The average kappa score, if comparison areas are weighted by sample count, is also 0.825. These values indicate a strong predictive capacity for shadows across the afternoon. Our model performance is highest for areas with no shade for both producer's accuracy (representing errors of omission) and user's accuracy (representing errors of commission). The data are weakest in assessing building shade: both user's and producer's accuracy for building shade are lower during the times of day with the smallest building shadows, and errors grow as the shaded area shrinks. The data on the presence of building shade are accordingly least accurate when the sun is highest and shade is almost nonexistent. In Monterrey I, for instance, building shade accuracy is very low at 12:00 (user's accuracy of 0.15 and producer's accuracy of 0.07), but the nonbuilding land area is only 5 percent building shade: individual shadows are each very small and line the edges of buildings. By contrast, Amsterdam has a much higher building shade accuracy at 12:00 (user's accuracy of 0.68 and producer's accuracy of 0.69) because the nonbuilding land area is 39.97 percent building shade. Individual confusion matrices for each comparison area can be found in Appendix C.

We evaluated the difference in shaded areas for each city, testing whether there was agreement between the amount of total shade over the course of an afternoon (Table 8). The results show an average 3.86 percent difference in shaded area. The primary source of error is building shade, particularly when shadows are very small. Our data overestimate shade, likely due in part because our building heights are too tall on average.

TECHNICAL NOTE | March 2026 | 17

## Comparison of UTCI data

For each city, we calculate the mean absolute error among all 1 m pixels in the AOI for UTCI as well as the mean error of UTCI and standard deviation in the sun and in the shade as determined by the lidar-derived data at 12:00, 15:00, and 18:00 on the day of analysis—the hottest day of the five-year period before assessment. We validate our thermal comfort data, like the shade data, in nonbuilding land areas. We assess the mean error and standard deviation in degrees Celsius for our thermal

comfort data to show what the temperature differences might be between our open-source UTCI data and estimates derived from lidar data. We note additionally that lidar-derived UTCI estimates vary by +/- 1.0–1.5°C from ground truth depending on urban form and meteorological data sources (Appendix A). Our mean absolute error represents an additional uncertainty compared to observed ground truth. Figure 5 provides an example of UTCI data from Rio de Janeiro to demonstrate discrepancies between open-source and lidar-derived data.

Figure 5 | UTCI in Rio de Janeiro at 12:00, 15:00, and 18:00 at a 1 m resolution

![img-5.jpeg](img-5.jpeg)

Note: Differences in building footprint and height can produce different Universal Thermal Climate Index (UTCI) patterns.
Source: WRI authors.

18 | WORLD RESOURCES INSTITUTE

Modeling hyperlocal heat exposure with open-source data

**Table 9 | Assessment of mean absolute error between UTCI results from open-source versus lidar-derived data in nonbuilding land areas**

|  AREA OF INTEREST | 12:00 MEAN UTCI ERROR (°C) | 15:00 MEAN UTCI ERROR (°C) | 18:00 MEAN UTCI ERROR (°C) | 12:00 UTCI STANDARD DEVIATION | 15:00 UTCI STANDARD DEVIATION | 18:00 UTCI STANDARD DEVIATION  |
| --- | --- | --- | --- | --- | --- | --- |
|  Rio de Janeiro | 0.45 | 0.45 | 0.12 | 3.66 | 2.85 | 0.85  |
|  Monterrey I | 0.42 | 0.49 | 0.32 | 1.66 | 1.51 | 0.51  |
|  Monterrey II | 0.47 | 0.50 | 0.22 | 1.59 | 1.42 | 0.44  |
|  Monterrey III | 0.54 | 0.53 | 0.29 | 1.49 | 1.28 | 0.46  |
|  Amsterdam | 0.39 | 0.33 | 0.27 | 3.34 | 2.51 | 1.71  |
|  **Average** |  | **0.39** |  |  | **1.69** |   |

Note: UTCI = Universal Thermal Climate Index.

Source: WRI authors.

The mean absolute error between our open-source UTCI and the lidar-derived UTCI is 0.39°C (we slightly underestimate temperature) across the nonbuilding, nonwater pixels in the study area (Table 9). On average across all times and comparison areas, 90 percent of our data falls within 2.56°C of the lidar-derived data. The differences are greater at noon, when shadows are smaller and, accordingly, more difficult to predict because of their close spatial clustering around individual features. The (unweighted) average of the standard deviations is 2.20, and standard deviation is also highest when shadows are shorter, so more area is predicted erroneously as shaded or unshaded.

Additionally, we assess the accuracy of our thermal comfort data without the effects of discrepancies in shadows (e.g., pixels that are shaded in one data set but unshaded in another). This process involves computing the mean error and standard deviation in 1 m pixels between our open-source data and the lidar-derived data using equivalent shade type classes. Accordingly, we conduct comparisons for areas where both data sets indicate building shade, both indicate tree shade, and both indicate no shade. Any differences in these data result from either discrepancies in the ground elevation DEM or in small differences created by shading earlier in the day; for instance, a pixel that is shaded at 10 a.m. will still be slightly cooler at noon than a fully

**Table 10 | Error and standard deviation in 1 m pixels where the shade type is consistent across our open-source data and the lidar-derived data**

|  AREA OF INTEREST | MEAN ERROR: BUILDING SHADE (°C) | MEAN ERROR: TREE SHADE (°C) | MEAN ERROR: UNSHADED (°C) | STANDARD DEVIATION: BUILDING SHADE | STANDARD DEVIATION: TREE SHADE | STANDARD DEVIATION: UNSHADED  |
| --- | --- | --- | --- | --- | --- | --- |
|  Rio de Janeiro | 0.022 | 0.016 | 0.017 | 0.21 | 0.26 | 0.36  |
|  Monterrey I | 0.067 | 0.074 | 0.014 | 0.20 | 0.22 | 0.19  |
|  Monterrey II | 0.14 | 0.15 | 0.13 | 0.22 | 0.15 | 0.15  |
|  Monterrey III | 0.13 | 0.052 | 0.031 | 0.23 | 0.28 | 0.19  |
|  Amsterdam | 0.036 | 0.027 | 0.080 | 0.17 | 0.17 | 0.26  |
|  **Average** |  | **0.066** |  |  | **0.22** |   |

Note: The table shows disparities in the Universal Thermal Climate Index from sources that are not shade classification discrepancies at the time of our observation.

Source: WRI authors.

TECHNICAL NOTE | March 2026 | 19

unshaded pixel. Thus, we evaluate the total differences caused by factors *other than* discrepancies in shade classification at the time of assessment.

We conduct this analysis over the whole study area (including on rooftops and in areas with water); because we have removed shade classification discrepancies, the large unshaded rooftop areas no longer introduce bias into our comparison process. We are therefore able to assess minor sources of discrepancy across the entire comparison AOI.

The mean error in areas where shade types are the same for our open-source data and the lidar-derived data (Table 10) are significantly smaller than overall error: 0.066°C compared to 0.39°C, with a standard deviation of 0.22 averaged across all comparison areas. These results confirm that errors in our open-source UTCI data are primarily the product of feature placement and height: the distribution and length of shadows create deviations between the open-source and lidar-derived data sets. Discrepancies here are instead caused either by the ground elevation DEM or by inaccurate shade placement earlier in the day, which would lead to lingering temperature differences.

## Applications for scenario planning

Our application of SOLWEIG can be used to support evaluations of modeled urban infrastructure change. Drawing on information provided by policymakers (e.g., a plan for tree planting or a design for a new park) or other researchers, we can adjust the inputs to SOLWEIG to evaluate changes to shade and thermal comfort (see “Modeling methods”). In the following section, we show modeled analyses of tree planting, shade structure construction, and surface albedo increase from cool roofs. Details on these specific heat-resilient infrastructure scenarios can be found in Wesley et al. (2026). Derived from the same input data that are used to support the thermal comfort model, they are designed to be relevant to and representative of existing heat-resilience policies and heat action plans in a variety of cities.

Tree planting lowers UTCI locally, primarily through increased shade area but slightly through transpiration (Buo et al. 2023). To demonstrate the use of this modeling framework, we show how planting additional trees in Rio de Janeiro can change shade and UTCI along roads (Figure 6).

Shade structures lower temperature through additional shaded area (Middel et al. 2021). While the area of intervention is hyperlocal—temperatures are only reduced in areas that gain shade—the reduction in UTCI means that newly shaded areas can serve as a resource for people spending time outdoors. As an

example of how this scenario looks in practice, we show modeled shade structure construction in a small “pocket” park in Rio de Janeiro at 15:00 (Figure 7).

Cool roofs reduce UTCI slightly by lowering the overall air temperature; high-albedo surfaces reflect solar radiation rather than absorb it and reradiate it slowly during the afternoon (Broadbent et al. 2020). To demonstrate what a cool roof scenario looks like using our data, we show a modeled implementation of cool roofs on large buildings in Rio de Janeiro at 15:00 (Figure 8). We note that cool roofs do not change shade, so we show infrastructure and UTCI.

**Figure 6 | Modeled infrastructure, shade, and UTCI at 15:00 with a scenario for tree planting in pedestrian areas along roads in Rio de Janeiro**

![img-6.jpeg](img-6.jpeg)

Notes: More information on the development of the infrastructure scenario can be found in Wesley et al. (2026). UTCI = Universal Thermal Climate Index.

Sources: Wesley et al. 2026; WRI authors.

20 | WORLD RESOURCES INSTITUTE

Modeling hyperlocal heat exposure with open-source data

Figure 7 | Modeled infrastructure, shade, and UTCI at 15:00 with a scenario for shade structure construction in a small park in Rio de Janeiro

![img-7.jpeg](img-7.jpeg)

Park area
Tree canopy

![img-8.jpeg](img-8.jpeg)

Park area
Tree canopy
Shade structure

![img-9.jpeg](img-9.jpeg)

Shade structure additions

![img-10.jpeg](img-10.jpeg)

Building shade
Tree shade

![img-11.jpeg](img-11.jpeg)

Building shade
Tree shade

![img-12.jpeg](img-12.jpeg)

Change in building shade

![img-13.jpeg](img-13.jpeg)

UTCI (°C)
23 33

![img-14.jpeg](img-14.jpeg)

UTCI (°C)
23 33

![img-15.jpeg](img-15.jpeg)

UTCI change (°C)
-6.5 0

Notes: More information on the development of the infrastructure scenario can be found in Wesley et al. (2026). UTCI = Universal Thermal Climate Index.

Source: Wesley et al. 2026; WRI authors.

## Discussion

This novel approach to modeling 1 m thermal comfort using an entirely open-source process allows cities without adequate intra-urban heat data to access and use realistic, useful data on current heat exposure. It also elucidates the potential for mitigating that heat exposure through infrastructure change. Existing high-resolution urban heat data sets are often difficult or expensive to obtain, and they can require expert analyses to interpret.

Current open-access global temperature data sets are insufficient to examine human heat exposure and the impact of implementing heat-resilient infrastructure; though LST is readily available

at 30 m resolution, it lacks a relationship to the human body's experience of heat. Air temperature and humidity are available at a 1 km or 0.1 degree resolution through global reanalysis products or with incomplete coverage from weather stations; therefore, they lack sufficient spatial resolution or coverage to support local analyses.

This approach meets the needs of cities that are planning for urban heat resilience, providing guidance on what areas are hot, what types of urban forms exacerbate or mitigate human-scale thermal comfort, and how infrastructure changes might protect residents from the effects of heat. It also enables comparison of heat-resilient infrastructure interventions, giving visual and quantitative estimates of how cities can meet diverse goals surrounding heat reduction across different urban environments.

Our collaborators and beta testers identified several use cases for which these data sets might fill gaps that can contribute to decision-making. The data can be used at a hyperlocal scale to

Figure 8 | Modeled infrastructure and UTCI at 15:00 with a scenario for cool roofs on large buildings in Rio de Janeiro

![img-16.jpeg](img-16.jpeg)

![img-17.jpeg](img-17.jpeg)

![img-18.jpeg](img-18.jpeg)

![img-19.jpeg](img-19.jpeg)

![img-20.jpeg](img-20.jpeg)

![img-21.jpeg](img-21.jpeg)

Notes: More information on the development of the infrastructure scenario can be found in Wesley et al. (2026). UTCI = Universal Thermal Climate Index.

Sources: Wesley et al. 2026; WRI authors.

TECHNICAL NOTE | March 2026

21

provide information on neighborhood-specific relationships between urban infrastructure and heat exposure. For instance, showing that shade from shade structures reduces UTCI—and by how much—can elucidate the potential impacts of adding shade to a neighborhood, even if our data are not suitable for guiding specific siting of that shade. The data can also be used to determine high-priority areas for placing heat interventions by identifying neighborhoods or urban spaces, such as downtown pedestrian areas, that have high baseline UTCI or the potential for UTCI reduction through heat interventions. Importantly, both use cases can also support heat adaptation planning and fundraising efforts, using data to explain the impacts of heat-resilient infrastructure. Our data are locally grounded but consistent across cities, allowing us to evaluate different UTCI baselines as well as the potential effects of heat intervention scenarios in different environmental and urban conditions globally at a neighborhood scale.

These use cases sometimes consider relationships at a hyperlocal level, but they never rely on site-specific planning; instead, they are about the effects of urban forms on heat and can inform and guide policy. The use cases are often most relevant at a neighborhood scale, using data to consider the distributions and hazards of intra-urban heat. Often, our data support use cases that consider relative changes to UTCI, either across time, space, or types of heat-resilient infrastructure. Accordingly, feature-based discrepancies in our data sets matter less than they do for absolute UTCI assessments because the important conclusions rest on changes to UTCI rather than site-specific heat exposure estimates.

Our modeling implementation is general enough to provide insights into urban heat exposure across the globe and potential cooling interventions, drawing on relationships documented over a decade of research in cities around the world. It is also highly specific to each city, using very high-resolution data to examine local conditions. We found that 90 percent of our UTCI estimates were within 2.56°C of the lidar-derived UTCI. There is an added uncertainty of about 1.0–1.5°C of the lidar-derived data compared to ground-truth data (Appendix A). Where appropriate, the approach could be easily adapted or expanded to inform city-specific infrastructure changes without introducing new methods (e.g., augmenting pedestrian shade via artificial structures in arid cities or through tree-planting in water-rich ones).

An online portal, the Cool Cities Lab, will enable interactivity with the data and its applicability to use cases defined with city stakeholders.² The online data portal can support exploration from both expert scientific viewers and policymakers or residents hoping to explore heat within their city. Raster maps and sum-

summary statistics will also be available for download via a public Amazon Web Services S3 repository.

## Limitations

The primary limitation of this open-source modeling approach is the difference in UTCI created by input data sets. Both shadow and UTCI data are heavily influenced by the placement, extent, and height of trees and buildings. A reliance on open-source, global data sets with varied accuracy produces a range of misplaced, missing, or erroneous shadows that, accordingly, affect UTCI. For albedo, we currently have a 10 m data set; scaling to the 1 m pixel level leads to unavoidable local discrepancies at this scale. At a very high resolution, an expert local viewer will see features that they know are wrong or missing in the maps. This limitation may also occur (but to a lesser degree) when using lidar-derived data: because it is static in time, lidar data cannot reflect new development. Our approach is significantly less accurate at a local scale, but it can be updated with the release of newer data sets at a lower cost.

Accordingly, we recommend that results from our modeling be used to estimate the impact of interventions at large scale (neighborhood or larger) to guide urban planning, substantiate funding proposals, prioritize areas for intervention, and develop policies. We do not recommend that the data be used at the individual feature level or to guide site-specific interventions. The UTCI values across a neighborhood in sun, tree shade, and building shade, as well as on varied urban surfaces, are realistic and can be compared to other neighborhoods and used to understand the dynamics of hyperlocal urban heat and infrastructure. They also sufficiently demonstrate the spatial variability of urban heat. These values, and the metrics calculated across a neighborhood or city, can be used to support and guide policy.

The clearest way to strengthen the model's performance is to include more accurate input data, particularly building height and footprint data. Although our data set represents the best globally available open-access data at the time of publication, it carries substantial discrepancies that propagate through shade and UTCI estimates. Our meteorological data inputs are likewise the best globally available open-access data at the time of publication, but the spatial resolution on ERA5 (about 28 km at the equator) means that intra-urban temperature or meteorological variations are not captured in our model. This same effect holds for the modeled infrastructure scenarios: the modeled temperatures will only be as strong as input data, so differences in potential tree placement or roof albedo will propagate into UTCI results.

22 | WORLD RESOURCES INSTITUTE

Modeling hyperlocal heat exposure with open-source data

Accordingly, we will strengthen the model as new or updated input data sets become available. In 2026 we anticipate the publication of new high-resolution (1 m) albedo and medium-resolution (200 m) air temperature data; we have designed our modeling pipeline to accommodate updates when these data sets become available. Other input data can also be updated following new releases. Many of our input data sets are static, including our DSM, tree canopy data, and building data (see Table 4). Although these data sets were current at the time of publication, they will become outdated, particularly in cities that are developing or in areas like informal settlements, which have high rates of change. Regular updates to input data sets can help our work stay relevant and high quality.

## Further research

The model relies on the best open-source data available at the time of publication. Going forward, we can update the model using newer or more accurate data sets as they are released, pending validation and review. Additionally, our modeling framework enables the integration of local lidar data or feature data sets when it—and sufficient human resources—are available. In particular, we note that building height data, which can be difficult to observe in areas with small buildings, informal development, or abundant tree cover, cause the majority of errors in our shade and UTCI data (Kamath et al. 2024). Fortunately, building height data are being improved regularly, both through the augmentation of large data sets such as OpenStreetMap and Google Open Buildings (which released a substantial update in 2024 and is included in Overture Maps) and the development of new methods such as UT-GLOBUS. We anticipate improvements to our approach as building height data become more widely available and accurate.

We can also update our approaches to incorporating heat-resilient infrastructure interventions into the model. We recognize that the current parameterizations to estimate neighborhood-scale air temperature change from the addition of trees and cool surfaces are limited by their simplicity and are generalized from a survey of global values. Accordingly, we are exploring the use of a statistical model that would enable modification of air temperature from changes to albedo and vegetation at about 200 m resolution (Smith et al. 2025). We believe that the work will be suitable for updating the handling of the albedo and air temperature parameterization based on cool roofs and tree planting. As the statistical model is finalized, we can couple it with SOLWEIG to create a joint mesoscale air temperature–hyperlocal thermal comfort model (Ding et al. 2024).

## Conclusions

We present here a novel method for calculating 1 m UTCI using exclusively globally available open-source data. Our approach, suitable for exploring heat exposure and the potential for mitigating heat risk in cities, has been validated against lidar-supported models with a mean absolute error of 0.39°C. We produce UTCI and shade data sets that are suitable for evaluating baseline heat exposure across neighborhoods or cities as well as for considering the cooling potential of heat-resilient infrastructure interventions in various urban settings. Going forward, we will improve our assessments of heat-resilient infrastructure interventions and continue to improve the modeling framework by integrating new, better input data. This approach bridges the gap between scientific assessments of urban heat and heat-resilient policy in areas that lack sufficient local data to plan, design, and implement urban planning interventions to protect residents from extreme heat.

TECHNICAL NOTE | March 2026 | 23

## Appendix A: Validation of SOLWEIG in literature

The SOLWEIG model is a physically based framework for calculating human-scale thermal comfort—how hot a person feels while standing outdoors at a given time and place. The model uses 3D urban forms (ground, building, and tree height/footprint) as well as land use and meteorological background conditions (temperature, relative humidity, radiation, wind) to calculate Tmrt, a measure of “the short- and longwave radiation exchange of a standard human body in terms of Celsius degree” (Gál and Kántor 2020).

Validation is one of the biggest hurdles in thermal comfort modeling because collecting on-site measured Tmrt data can be expensive and cumbersome (equipment alone often costs more than $15,000). Accordingly, three physically based models that have been used and peer-reviewed for years are often employed without independent validation or are even used as points of comparison for novel methods. Here, we demonstrate that SOLWEIG is the most appropriate of these three models for our analysis, and it is accepted within peer-reviewed scientific literature as an acceptable thermal comfort calculation tool without on-the-ground validation. We present studies that have independently validated SOLWEIG, establishing a baseline, and studies that use SOLWEIG without validation.

### Validation of the SOLWEIG model

**Gál and Kántor (2020)** compare SOLWEIG, RayMan, and ENVI-met, the three primary physical thermal comfort models, in a park in Hungary. They find that

“since daytime Tmrt model errors are at their minimum around noon and in the afternoon, SOLWEIG is ideal for thermal comfort and heat mitigation studies that are generally concerned with the warmest period of the day, suggesting that SOLWEIG is the ideal model for this work. However, the tendency of the model to overestimate Tmrt when the sites are in shade and underestimate them when they are sunlit means that heat mitigation studies might likely underestimate the impact of shading” (Gál and Kántor 2020).

We will use the SOLWEIG model to calculate afternoon Tmrt, but we will not use the model during nighttime or early morning periods, when the errors are greatest. Additionally, we prefer to slightly underestimate the utility of shade, and explain error ranges accordingly, when recommending shade as a heat mitigation strategy.

**Chen et al. (2016)** validated SOLWEIG in a variety of urban environments in Shanghai, finding that “*modeled Tmrt values showed good agreement with measured values, with R2 higher than 0.9.*” They found that the model slightly underestimated Tmrt on the sunniest days directly next to reflective buildings, and it slightly overestimated it away from buildings. In both the square and canyon environments, this validation of SOLWEIG found an error of +/- 3°C for Tmrt, which translates in practice to about 1.2°C for UTCI.

**Buo et al. (2023)** compare SOLWEIG to high-quality measurements taken by a suite of micrometeorological observation equipment in Tempe, Arizona (Middel and Krayenhoff 2019). They find that the overall *R* value is 0.9, though SOLWEIG slightly overestimates Tmrt in the sun and slightly underestimates Tmrt in the shade. This result indicates that thermal comfort measurements to evaluate potential heat mitigation infrastructure (e.g., tree planting) would slightly underestimate the cooling impact of shade, ensuring that our simulations produce conservative estimates of how much cooling is possible from infrastructure change.

**Lau et al. (2016)** evaluate Tmrt in Hong Kong, finding an *R*² value of 0.93 for SOLWEIG. They note the possibility of error due to differences between local air temperature and measured air temperature at the nearest available weather station, which might be used as forcing data for the model. Our use of ERA5 data comes with different risks and benefits; ERA5 is generalized across a large area but is also less subject to microclimatic shifts than individual weather station data.

**Briegel et al. (2023)** use SOLWEIG as the industry standard Tmrt model in comparison to a novel deep learning framework. They validate both approaches against a network of sensors in Freiburg, Germany, and find SOLWEIG to have an *R*² of 0.92 (slightly higher than the deep learning model).

Other studies validating SOLWEIG include Chen et al. (2014), Jin et al. (2021), Kim et al. (2022), Lindberg and Grimmond (2011a), Lindberg et al. (2008), and Thom et al. (2016).

### Use of the SOLWEIG model without validation

The SOLWEIG model has become a standard within the field of heat modeling. It is quite common among heat-modeling researchers to utilize the SOLWEIG model without validation. Here, we present several such examples.

**Colaninno et al. (2024)** use SOLWEIG to calculate Tmrt and subsequently use that Tmrt data to calculate UTCI to identify high-risk sidewalk segments for heat stress. They note that SOLWEIG “is a well-established tool available in QGIS through the open-source Urban Multi-scale Environmental Predictor (UMEP) plugin. . . . Several studies have reported on the reliability of the SOLWEIG model in estimating radiative fluxes in the urban environment” (Colaninno et al. 2024).

**Li et al. (2024)** deploy SOLWEIG across American cities with diverse climatic characteristics to explore vulnerability to heat stress.

**Yi et al. (2025)** evaluate relationships between urban form and heat stress in Los Angeles, using SOLWEIG to train a deep learning model and relying on the fact that the model “has been widely validated across diverse climatic zones.”

**Thorsson et al. (2014)** use SOLWEIG to model Tmrt in comparison to air temperature as a metric for assessing heat-related mortality risk, finding that it is more precise than air temperature in identifying both

24 | WORLD RESOURCES INSTITUTE

Modeling hyperlocal heat exposure with open-source data

harmful heat events and sites at risk for heat exposure. They do no independent validation of the model, instead relying on the original SOLWEIG publications (Lindberg et al. 2008, 2018).

**Li et al. (2023)** note that SOLWEIG “has been validated worldwide in different climate zones with high accuracy” and do not conduct further validation for their comparison between Tmrt and LST in Philadelphia.

**Ding et al. (2024)** couple SOLWEIG with a mesoscale air temperature and radiation model (WRF–Urban Canopy Model) and validate the unified model setup without examining each individual piece, noting that SOLWEIG has undergone sufficient validation to be combined into a modeling pipeline without additional testing.

Other studies presenting SOLWEIG without validation include Evola et al. (2021), Jänicke et al. (2016), Kong et al. (2022), Lindberg and Grimmond (2011b), and Wallenberg et al. (2020).

## Appendix B: Building height analysis

The objective of this comparative process is to analyze the accuracy, extent, and resolution of several global and regional building height data sets available at the time of publication to assess which might serve as a primary building height data set for thermal comfort modeling. Specifically, we assess data sets from European building stock characteristics in a common and open database (EUBUCCO), UT-GLOBUS, and 3D Global Building Footprints (3D-GloBFP) in comparison to lidar data from Amsterdam, which had the highest

spatial overlap with all city data sets for which we had available lidar data (AHN 2023a, 2023b, n.d.; Che et al. 2024; Kamath et al. 2024; Milojevic-Dupont et al. 2023). Table B-1 shows the testing and comparison data sources.

EUBUCCO is derived from open-access lidar data and OpenStreetMap throughout Europe. Although its input data sources are high quality, EUBUCCO data have a limited area of coverage. UT-GLOBUS is derived from spaceborne altimetry (ICESat-2 and GEDI) data and uses a random forest model to estimate building heights. It has a wide coverage of major cities worldwide. The 3D-GloBFP data set uses an eXtreme Gradient Boosting (XGBoost) regression on digital elevation and terrain data from multiple open data sources, notably OpenStreetMap, Microsoft Building Footprints, China’s Baidu Maps, and the US Geological Survey, in diverse urban environments to estimate building heights globally.

Building height is a key data set in thermal comfort modeling as an input for shadows and urban surfaces. While the production of building height and footprint data is a growing field of work, most current global data sets have an insufficient resolution or extent to support our 1 m resolution modeling. We require data that is open-access, globally available, and of a sufficient spatial resolution to show shadows within dense urban areas. Many high-quality global data sets, such as the World Settlement Footprint 3D data (90 m) have an insufficient resolution to support a microclimate analysis (Esch et al. 2020).

**Table B-1 | Data sources for building height data sets and comparison data sets**

|  DATA SET | SPATIAL COVERAGE | DATA TYPE/SPATIAL RESOLUTION | PRODUCTION YEAR | CITATION  |
| --- | --- | --- | --- | --- |
|  EUBUCCO | Europe | Polygons | 2023 | Milojevic-Dupont et al. 2023  |
|  UT-GLOBUS | Major cities globally. (See the details for coverage at its website.) | Polygons | 2024 | Kamath et al. 2024  |
|  3D-GloBFP | Global | Polygons | 2024 | Che et al. 2024  |
|  AHN - lidar | Netherlands | Point cloud | 2023 | AHN n.d.  |
|  Ground truth data-AHN5 - DSM | Netherlands | 1 m | 2023 | AHN 2023a  |
|  AHN - DTM | Netherlands | 0.5 m | 2023 | AHN 2023b  |

Notes: AHN = Actueel Hoogtebestand Nederland. DSM = digital surface model. DTM = digital terrain model. EUBUCCO = European building stock characteristics in a common and open database. 3D-GloBFP = 3D Global Building Footprints. UT-GLOBUS = University of Texas-Global Building heights for Urban Studies.

Source: WRI authors.

TECHNICAL NOTE | March 2026 | 25

Figure B-1 | EUBUCCO distribution in Amsterdam compared to our urban extent of Amsterdam building height data

![img-22.jpeg](img-22.jpeg)

Note: EUBUCCO = European building stock characteristics in a common and open database.

Sources: AHN n.d.; Milojevic-Dupont et al. 2023; WRI authors.

Spatial extent is a limiting factor for some data sets. In the first round of assessment, we determined that EUBUCCO could not support our modeling work because it covers only parts of urban extents (Milojevic-Dupont et al. 2023). Notably, a narrow urban extent is drawn within Amsterdam for the data set, and our tests showed gaps in other cities across Europe (Figure B-1).

The UT-GLOBUS data set, a product that has been created with a global extent, is available in 1,200 cities with a concentration in the Global North and gaps in Africa, China, and South America (Kamath et al. 2024). This data set is complete in cities that have coverage, and new data are being produced and released to improve global coverage.

Below, we assess the accuracy of building height (vertical accuracy) in three open-access building data sets to determine what building

height data might be suitable for our 1 m resolution thermal comfort modeling.

To examine the vertical accuracy of the data sets, we construct parallel raster data from both the open-access data sets and the lidar data and compare those rasters. We begin by rasterizing polygons from our testing data sets and align those rasters with ones created from the lidar point clouds. We standardized all rasters to local UTM projection and coordinate systems. We then check to see if the centroid of each 1 m raster cell is within the boundary of a building footprint polygon taken from Overture Maps (Overture Maps 2025). We average the heights of all cells with a centroid inside a building's footprint for both the testing data sets and the lidar-derived data sets, and then we compare the two average building heights. Because we are analyzing only cells with a centroid inside buildings rather than simply clipping the building height rasters to building footprint

26 | WORLD RESOURCES INSTITUTE

Modeling hyperlocal heat exposure with open-source data

**Table B-2 | Vertical accuracy of building height data sets compared to lidar-derived data**

|  DATA SETS | MEAN ABSOLUTE ERROR (M) | STANDARD DEVIATION  |
| --- | --- | --- |
|  EUBUCCO | 0.366 | 2.483  |
|  UT-GLOBUS | -5.370 | 6.679  |
|  3D-GloBFP | -8.409 | 6.065  |

Notes: EUBUCCO = European building stock characteristics in a common and open database. 3D-GloBFP = 3D Global Building Footprints. UT-GLOBUS = University of Texas-GLOBAL Building heights for Urban Studies.

Sources: AHN n.d.; Che et al. 2024; Kamath et al. 2024; Milojevic-Dupont et al. 2023; WRI authors.

polygons, we avoid testing cells that have a centroid on the ground but an edge inside the building.$^{3}$

The EUBUCCO data set, which is derived partly from lidar data, had the highest accuracy. UT-GLOBUS showed an overall underestimation of building heights but a stronger performance than 3D-GloBFP (Table B-2). The statistical distribution of UT-GLOBUS data was likewise more normal than that of 3D-GLoBFP (Figure B-2).

Of available building height data, UT-GLOBUS is the most suited to serving as a primary input data set for our thermal comfort model. Its combination of a wide geographic distribution and a higher accuracy compared to the other primary global data set makes it the best option available. We note, however, that several new building height data sets are currently in development, so this analysis may be updated as better data become available.

Ultimately, our combined building height data sets produced the lowest uncertainty of any possible building height data available at the time of writing. Our data show more variability in downtown urban centers than in residential areas, likely because of the diversity of buildings and roof profiles.

**Figure B-2 | Distributions of differences in building height between model data and lidar-derived data**

# **A. EUBUCCO building height differences from lidar data**

![img-23.jpeg](img-23.jpeg)

# **B. 3D-GloBFP building height differences from lidar data**

![img-24.jpeg](img-24.jpeg)

# **C. UT-GLOBUS building height differences from lidar data**

![img-25.jpeg](img-25.jpeg)

Notes: EUBUCCO = European building stock characteristics in a common and open database. 3D-GloBFP = 3D Global Building Footprints. UT-GLOBUS = University of Texas-GLOBAL Building heights for Urban Studies.

Sources: AHN n.d.; Che et al. 2024; Kamath et al. 2024; Milojevic-Dupont et al. 2023; WRI authors.

TECHNICAL NOTE | March 2026 | 27

## Appendix C: Comparison of shade and UTCI data in individual AOIs

For each AOI, we calculate the user's and producer's accuracy across all nonbuilding, nonwater pixels (1 m resolution) to examine the accuracy of predicted shadows at 12:00, 15:00, and 18:00. We look at the accuracy of unshaded, building shade, and tree shade pixels.

### Rio de Janeiro

In the Rio de Janeiro AOI on December 31, 2022, the average kappa score is 0.830 (Table C-1). The accuracy for areas without shade is highest (average user's accuracy of 0.83 and producer's accuracy of 0.92 across the three time steps). Our assessment of tree shade

is strong (average user's accuracy of 0.86 and producer's accuracy of 0.89 for the three time steps). The accuracy of building shade is weakest when there is very little building shade (user's accuracy of 0.70 and producer's accuracy of 0.51 at 12:00 when the nonbuilding pedestrian area within the AOI is only 12.4 percent building shade). However, the accuracy becomes stronger as building shadows increase (user's accuracy of 0.86 and producer's accuracy of 0.76 at 18:00 when the nonbuilding pedestrian area within the AOI is 41.3 percent building shade). Building shade is nonetheless the weakest area for predictions, likely because the building data set is the weakest input data set.

**Table C-1 | User's and producer's accuracy for shade in Rio de Janeiro, showing the accuracy of building, tree, and no shade across 1 m pixels for 12:00, 15:00, and 18:00**

|  12:00 | BUILDING SHADE (LIDAR) | TREE SHADE (LIDAR) | NO SHADE (LIDAR) | TOTAL | U_ACCURACY  |
| --- | --- | --- | --- | --- | --- |
|  Building shade | 218,717 | 24,795 | 69,461 | 312,973 | 0.70  |
|  Tree shade | 41,151 | 422,860 | 6,739 | 470,750 | 0.90  |
|  No shade | 169,333 | 11,748 | 10,48962 | 1,230,043 | 0.85  |
|  Total | 429,201 | 459,403 | 1,125,162 | 2,013,766 |   |
|  **P_accuracy** | **0.51** | **0.92** | **0.93** |  | **0.839**  |

|  15:00 | BUILDING SHADE (LIDAR) | TREE SHADE (LIDAR) | NO SHADE (LIDAR) | TOTAL | U_ACCURACY  |
| --- | --- | --- | --- | --- | --- |
|  Building shade | 255,605 | 21,238 | 52,635 | 329,478 | 0.78  |
|  Tree shade | 43,472 | 397,892 | 6,244 | 447,608 | 0.89  |
|  No shade | 160,941 | 13,925 | 1,061,814 | 1,236,680 | 0.86  |
|  Total | 460,018 | 433,055 | 1,120,693 | 2,013,766 |   |
|  **P_accuracy** | **0.56** | **0.92** | **0.95** |  | **0.852**  |

|  18:00 | BUILDING SHADE (LIDAR) | TREE SHADE (LIDAR) | NO SHADE (LIDAR) | TOTAL | U_ACCURACY  |
| --- | --- | --- | --- | --- | --- |
|  Building shade | 789,987 | 50,660 | 82,612 | 923,259 | 0.86  |
|  Tree shade | 66,230 | 270,932 | 8,805 | 345,967 | 0.78  |
|  No shade | 184,129 | 13,978 | 546,433 | 744,540 | 0.73  |
|  Total | 1,040,346 | 335,570 | 637,850 | 2,013,766 |   |
|  **P_accuracy** | **0.76** | **0.81** | **0.86** |  | **0.798**  |

Notes: The weighted kappa score for the region is 0.830. P = producer. U = user.

Source: WRI authors.

28 | ![World Resources Institute logo]() WORLD RESOURCES INSTITUTE

Modeling hyperlocal heat exposure with open-source data

## Monterrey I

Our Monterrey analysis was run on June 21, 2023. Shade data in Monterrey I shows an average kappa score of 0.832 for the region (Table C-2). Our accuracy is high for areas without shade (average user's accuracy of 0.90 and producer's accuracy of 0.92). Tree shade also has a relatively high accuracy (average user's accuracy of 0.80 and producer's accuracy of 0.84), demonstrating that the WRI/Meta

tree canopy data set can predict shade well in most areas. Building shade has a low accuracy but a very low coverage area—27.6 percent of area at 18:00. Because of the lower accuracy of building data and the small footprint of the shadows themselves, our predictive power for shade is weak.

**Table C-2 | User's and producer's accuracy for shade in Monterrey I, showing the accuracy of building, tree, and no shade across 1 m pixels for 12:00, 15:00, and 18:00**

|  12:00 | BUILDING SHADE (LIDAR) | TREE SHADE (LIDAR) | NO SHADE (LIDAR) | TOTAL | U_ACCURACY  |
| --- | --- | --- | --- | --- | --- |
|  Building shade | 26,076 | 28,847 | 118,212 | 173,135 | 0.15  |
|  Tree shade | 46,475 | 952,512 | 48,795 | 1,047,782 | 0.91  |
|  No shade | 308,876 | 48,497 | 5,993,290 | 6,350,663 | 0.94  |
|  Total | 381,427 | 1,029,856 | 6,160,297 | 7,571,580 |   |
|  **P_accuracy** | **0.07** | **0.92** | **0.97** |  | **0.921**  |

|  15:00 | BUILDING SHADE (LIDAR) | TREE SHADE (LIDAR) | NO SHADE (LIDAR) | TOTAL | U_ACCURACY  |
| --- | --- | --- | --- | --- | --- |
|  Building shade | 111,180 | 57,170 | 239,593 | 407,943 | 0.27  |
|  Tree shade | 99,514 | 879,954 | 45,463 | 1,024,931 | 0.86  |
|  No shade | 436,934 | 52,651 | 5,649,121 | 6,138,706 | 0.92  |
|  Total | 647,628 | 989,775 | 5,934,177 | 7,571,580 |   |
|  **P_accuracy** | **0.17** | **0.89** | **0.95** |  | **0.877**  |

|  18:00 | BUILDING SHADE (LIDAR) | TREE SHADE (LIDAR) | NO SHADE (LIDAR) | TOTAL | U_ACCURACY  |
| --- | --- | --- | --- | --- | --- |
|  Building shade | 966,681 | 204,902 | 761,843 | 1,933,426 | 0.50  |
|  Tree shade | 289,106 | 726,441 | 116,604 | 1,132,151 | 0.64  |
|  No shade | 835,323 | 83,497 | 3,587,183 | 4,506,003 | 0.80  |
|  Total | 2,091,110 | 1,014,840 | 4,465,630 | 7,571,580 |   |
|  **P_accuracy** | **0.46** | **0.72** | **0.80** |  | **0.697**  |

Notes: The weighted kappa score for the region is 0.832. P = producer. U = user.

Source: WRI authors.

TECHNICAL NOTE | March 2026 | 29

## Monterrey II

In Monterrey II on June 21, 2023, our data yield a kappa score of 0.864 (Table C-3). Again, areas with no shade (average user's accuracy of 0.91 and producer's accuracy of 0.93) and tree shade (average user's accuracy of 0.87 and producer's accuracy of 0.88) showed high accuracy; the model is predicting areas correctly, and unshaded or

tree-shaded areas are being correctly predicted. Building shade has a very low accuracy (average user's accuracy of 0.51 and producer's accuracy of 0.44), but again, this is partly due to its low coverage area and strong proximity to building footprints.

**Table C-3 | User's and producer's accuracy for shade in Monterrey II, showing the accuracy of building, tree, and no shade across 1 m pixels for 12:00, 15:00, and 18:00**

|  12:00 | BUILDING SHADE (LIDAR) | TREE SHADE (LIDAR) | NO SHADE (LIDAR) | TOTAL | U_ACCURACY  |
| --- | --- | --- | --- | --- | --- |
|  Building shade | 2,676 | 393 | 7,772 | 10,841 | 0.25  |
|  Tree shade | 637 | 77,532 | 7,166 | 85,335 | 0.91  |
|  No shade | 19,295 | 7,673 | 486,817 | 513,785 | 0.95  |
|  Total | 22,608 | 85,598 | 501,755 | 609,961 |   |
|  **P_accuracy** | **0.12** | **0.91** | **0.97** |  | **0.930**  |

|  15:00 | BUILDING SHADE (LIDAR) | TREE SHADE (LIDAR) | NO SHADE (LIDAR) | TOTAL | U_ACCURACY  |
| --- | --- | --- | --- | --- | --- |
|  Building shade | 7,701 | 1,452 | 21,497 | 30,650 | 0.25  |
|  Tree shade | 2,413 | 75,785 | 6,603 | 84,801 | 0.89  |
|  No shade | 29,299 | 7,655 | 457,556 | 494,510 | 0.93  |
|  Total | 39,413 | 84,892 | 485,656 | 609,961 |   |
|  **P_accuracy** | **0.20** | **0.89** | **0.94** |  | **0.887**  |

|  18:00 | BUILDING SHADE (LIDAR) | TREE SHADE (LIDAR) | NO SHADE (LIDAR) | TOTAL | U_ACCURACY  |
| --- | --- | --- | --- | --- | --- |
|  Building shade | 80,985 | 6,875 | 51,380 | 139,240 | 0.58  |
|  Tree shade | 10,465 | 76,489 | 6,540 | 93,494 | 0.82  |
|  No shade | 53,093 | 8,728 | 315,406 | 377,227 | 0.84  |
|  Total | 144,543 | 92,092 | 373,326 | 609,961 |   |
|  **P_accuracy** | **0.56** | **0.83** | **0.84** |  | **0.775**  |

Notes: The weighted kappa score for the region is 0.864. P = producer. U = user.

Source: WRI authors.

30 | ![World Resources Institute logo]() WORLD RESOURCES INSTITUTE

Modeling hyperlocal heat exposure with open-source data

## Monterrey III

In Monterrey III on June 21, 2023, the average kappa score across the three time steps is 0.814 (Table C-4). Patterns for shade classification accuracy are consistent with other AOIs, with unshaded predictions yielding the strongest results (average user's accuracy of 0.92 and

producer's accuracy of 0.87), tree shade prediction slightly weaker (average user's accuracy of 0.76 and producer's accuracy of 0.68), and building shade prediction substantially weaker (average user's accuracy of 0.37 and producer's accuracy of 0.56).

**Table C-4 | User's and producer's accuracy for shade in Monterrey III, showing the accuracy of building, tree, and no shade across 1 m pixels for 12:00, 15:00, and 18:00**

|  12:00 | BUILDING SHADE (LIDAR) | TREE SHADE (LIDAR) | NO SHADE (LIDAR) | TOTAL | U_ACCURACY  |
| --- | --- | --- | --- | --- | --- |
|  Building shade | 2,924 | 465 | 5,487 | 8,876 | 0.33  |
|  Tree shade | 3,335 | 39,714 | 8,746 | 51,795 | 0.77  |
|  No shade | 38,198 | 8,503 | 502,589 | 549,290 | 0.91  |
|  Total | 44,457 | 48,682 | 516,822 | 609,961 |   |
|  **P_accuracy** | **0.07** | **0.82** | **0.97** |  | **0.894**  |

|  15:00 | BUILDING SHADE (LIDAR) | TREE SHADE (LIDAR) | NO SHADE (LIDAR) | TOTAL | U_ACCURACY  |
| --- | --- | --- | --- | --- | --- |
|  Building shade | 9,255 | 1,411 | 15,278 | 25,944 | 0.36  |
|  Tree shade | 5,457 | 37,639 | 7,945 | 51,041 | 0.74  |
|  No shade | 47,294 | 8,142 | 477,540 | 532,976 | 0.90  |
|  Total | 62,006 | 47,192 | 500,763 | 609,961 |   |
|  **P_accuracy** | **0.15** | **0.80** | **0.95** |  | **0.860**  |

|  18:00 | BUILDING SHADE (LIDAR) | TREE SHADE (LIDAR) | NO SHADE (LIDAR) | TOTAL | U_ACCURACY  |
| --- | --- | --- | --- | --- | --- |
|  Building shade | 104,551 | 6,992 | 63,751 | 175,294 | 0.60  |
|  Tree shade | 16,894 | 26,202 | 7,458 | 50,554 | 0.52  |
|  No shade | 86,071 | 8,045 | 289,997 | 384,113 | 0.75  |
|  Total | 207,516 | 41,239 | 361,206 | 609,961 |   |
|  **P_accuracy** | **0.50** | **0.64** | **0.80** |  | **0.690**  |

Notes: The weighted kappa score for the region is 0.814. P = producer. U = user.

Source: WRI authors.

TECHNICAL NOTE | March 2026 | 31

## Amsterdam

The average kappa score across the three time steps in Amsterdam on July 8, 2023, is 0.785, the weakest result of our comparison areas (Table C-5). Notably, the accuracy of tree shade is weaker in Amsterdam than in other cities (average user's accuracy of 0.75 and producer's accuracy of 0.77). Building shade accuracy is stronger

in Amsterdam than in Monterrey (average user's accuracy of 0.78 and producer's accuracy of 0.66), likely due to the taller buildings in the urban core, which produce longer shadows and more building shade overall—even at 15:00, the nonbuilding area is 22.36 percent building shade.

**Table C-5 | User's and producer's accuracy for shade in Amsterdam, showing the accuracy of building, tree, and no shade across 1 m pixels for 12:00, 15:00, and 18:00**

|  12:00 | BUILDING SHADE (LIDAR) | TREE SHADE (LIDAR) | NO SHADE (LIDAR) | TOTAL | U_ACCURACY  |
| --- | --- | --- | --- | --- | --- |
|  Building shade | 543,543 | 200,665 | 55,455 | 799,663 | 0.68  |
|  Tree shade | 98,781 | 291,189 | 12,226 | 402,196 | 0.72  |
|  No shade | 146,152 | 17,996 | 606,456 | 770,604 | 0.79  |
|  Total | 788,476 | 509,850 | 674,137 | 1,972,463 |   |
|  **P_accuracy** | **0.69** | **0.57** | **0.90** |  | **0.731**  |

|  15:00 | BUILDING SHADE (LIDAR) | TREE SHADE (LIDAR) | NO SHADE (LIDAR) | TOTAL | U_ACCURACY  |
| --- | --- | --- | --- | --- | --- |
|  Building shade | 337,355 | 19,398 | 43,968 | 400,721 | 0.84  |
|  Tree shade | 79,608 | 332,007 | 17,547 | 429,162 | 0.77  |
|  No shade | 148,737 | 16,383 | 797,460 | 962,580 | 0.83  |
|  Total | 565,700 | 367,788 | 858,975 | 1,792,463 |   |
|  **P_accuracy** | **0.60** | **0.90** | **0.93** |  | **0.818**  |

|  18:00 | BUILDING SHADE (LIDAR) | TREE SHADE (LIDAR) | NO SHADE (LIDAR) | TOTAL | U_ACCURACY  |
| --- | --- | --- | --- | --- | --- |
|  Building shade | 496,089 | 16,331 | 47,638 | 560,058 | 0.89  |
|  Tree shade | 84,188 | 320,947 | 15,808 | 420,943 | 0.76  |
|  No shade | 157,729 | 18,986 | 634,747 | 811,462 | 0.78  |
|  Total | 738,006 | 356,264 | 698,193 | 1,792,463 |   |
|  **P_accuracy** | **0.67** | **0.90** | **0.91** |  | **0.810**  |

Notes: The weighted kappa score for the region is 0.785. P = producer. U = user.

Source: WRI authors.

32 | ![World Resources Institute logo]() WORLD RESOURCES INSTITUTE

Modeling hyperlocal heat exposure with open-source data

## Abbreviations

|  **AHN** | Actueel Hoogtebestand Nederland  |
| --- | --- |
|  **ALOS** | Advanced Land Observing Satellite  |
|  **AOI** | area of interest  |
|  **DEM** | digital elevation model  |
|  **DSM** | digital surface model  |
|  **DTM** | digital terrain model  |
|  **ERA5** | European Centre for Medium-Range Weather Forecasts Reanalysis, version 5  |
|  **EUBUCCO** | European building stock characteristics in a common and open database  |
|  **FABDEM** | Forest And Buildings removed Copernicus Digital Elevation Model  |
|  **GEDI** | Global Ecosystem Dynamics Investigation  |
|  **GHS ANBH** | Global Human Settlement Average Net Building Height  |
|  **ICESat-2** | Ice, Cloud, and land Elevation Satellite 2  |
|  **LST** | land surface temperature  |
|  **NASA** | National Aeronautics and Space Administration  |
|  **P** | producer  |
|  **SOLWEIG** | SOlar and LongWave Environmental Irradiance Geometry  |
|  **SRTM** | Shuttle Radar Topography Mission  |
|  **Tair** | air temperature  |
|  **3D** | three-dimensional  |
|  **3D-GloBFP** | 3D Global Building Footprints  |
|  **Tmrt** | mean radiant temperature  |
|  **U** | user  |
|  **UTCI** | Universal Thermal Climate Index  |
|  **UT-GLOBUS** | University of Texas–GLObal Building heights for Urban Studies  |
|  **UTM** | Universal Transverse Mercator  |
|  **WRF** | Weather Research and Forecasting  |

## Endnotes

1. Full access to model code can be found at https://github.com/wri/cities-thermal-comfort-modeling.
2. To learn more about the Cool Cities Lab (launching 2026), see https://coolcities.wri.org.
3. For more detail on the process and code, see https://github.com/wri/cities-heat-workspace/tree/building-height.

## Glossary

**air temperature (Tair):** The ambient air temperature, as it might be described on the news. Tair is freely available at a low resolution (0.1 degrees) in global reanalysis products, or it can be observed from sensors or weather stations.

**albedo:** A unitless measure of how much radiation is reflected by a surface, ranging from 0 (very dark) to 1 (very bright).

**area of interest (AOI):** The geographic area selected for an analysis.

**building footprint:** The two-dimensional area of a building on the ground.

**building height:** The height of a building from ground level. In this analysis, we use a single building height for each building.

**Coordinated Universal Time:** A standard time used to determine time zones globally.

**digital elevation model (DEM):** A rasterized data set of ground elevation, without features like trees or buildings.

**digital surface model (DSM):** A rasterized data set of ground and feature elevations. Here, we use a building and ground DSM, which includes the ground and buildings but no trees.

**kappa score:** A value used to represent statistical agreement between two data sets, ranging from 0 (no agreement) to 1 (perfect agreement).

**land cover:** The composition of land as described by its physical features (e.g., grass, water, pavement, etc.).

**land surface temperature (LST):** The “skin temperature” of the earth as observed from satellites, showing how hot surfaces are, including rooftops and the tops of trees, which are visible from above. LST is widely available from satellite data and can be useful in understanding heat across different parts of a city, but it correlates poorly with indicators of human heat exposure.

**land use:** The composition of land as described by its purpose (e.g., parks, buildings, parking lots, etc.).

**lidar:** Light detection and ranging; a method of remote sensing whereby light pulses are used to generate a 3D view of the earth’s shape and surfaces. Lidar data collection is the most accurate way to create ground and feature elevation data sets.

**mean absolute error:** The average of all errors from the actual values, regardless of direction; positive and negative errors are included together, so that they do not cancel each other out. Units are the same as in the data set that the error describes.

**mean bias error:** The difference between predicted and actual values, representing direction from zero. A positive error indicates overestimation, whereas a negative error means underestimation.

**mean radiant temperature (Tmrt):** A metric describing the thermal exchange between a standardized representation of a human body and all the surfaces that surround it. Tmrt can be calculated

TECHNICAL NOTE | March 2026 | 33

using measurements of sunlight, surfaces, vegetation, and local meteorology. It is more sensitive to radiation than UTCI.

**producer's accuracy:** A value used to represent errors of omission, or false negatives, in a data set.

**sky view factor:** A term describing how much of the sky is visible from a point on average across a whole day. It is useful in describing how much sunlight the point receives on average.

**SOlar LongWave Environmental Irradiance Geometry (SOLWEIG):** An open-source physical model commonly used to calculate Tmrt and shade.

**standard deviation:** A statistical measure of how clustered a data set is around the mean. A low standard deviation means that a data set has lower variability.

**tree canopy:** A data set showing the canopy area, and sometimes the canopy height, of trees. In this analysis, our tree canopy data set does include height.

**Universal Thermal Climate Index (UTCI):** A metric describing the thermal exchange between a standardized representation of a human body and its environment, including sunlight, surfaces, vegetation, and local meteorology. It is more sensitive to meteorological variables than Tmrt. A UTCI over 46 often indicates extreme heat stress, 38–46 indicates very strong heat stress, 32–38 indicates strong heat stress, 26–32 indicates moderate heat stress, and 9–26 indicates no thermal stress.

**user's accuracy:** A value used to represent errors of commission, or false positives, in a data set.

**wall aspect:** The orientation of walls in space that shows where their shadows will fall. Here, wall aspect is an intermediate processing data set used by the SOLWEIG model.

**wall height:** The height of a building's walls. Here, wall height is an intermediate processing data set used by the SOLWEIG model.

## References

Abdalla, A., and A.-E. Elmahal. 2016. "Augmentation of Vertical Accuracy of Digital Elevation Models Using Gaussian Linear Convolution Filter." In *2016 Conference of Basic Sciences and Engineering Studies (SGCAC)*, edited by S.F. Babiker and K. Badawi, 206–10. New York: Institute of Electrical and Electronic Engineers. https://doi.org/10.1109/SGCAC.2016.7458031.

AHN (Actueel Hoogtebestand Nederland). 2023a. "Data Feed: Digital Surface Model (DSM) 0.5m." April 12. https://service.pdok.nl/rws/ahn/atom/dsm_05m.xml.

AHN. 2023b. "Data Feed: Digital Terrain Model (DTM) 0.5m." April 12. https://service.pdok.nl/rws/ahn/atom/dtm_05m.xml.

AHN. n.d. "Products." https://www.ahn.nl/producten. Accessed February 17, 2026.

Ballinas, M., and V.L. Barradas. 2016. "Transpiration and Stomatal Conductance as Potential Mechanisms to Mitigate the Heat Load in Mexico City." *Urban Forestry & Urban Greening*, 20 (December): 152–59. https://doi.org/10.1016/j.ufug.2016.08.004.

Bonafoni, S., and A. Sekertekin. 2020. "Albedo Retrieval from Sentinel-2 by New Narrow-to-Broadband Conversion Coefficients." *IEEE Geoscience and Remote Sensing Letters* 17 (9): 1618–22. https://doi.org/10.1109/LGRS.2020.2967085.

Briegel, F., J. Wehrle, D. Schindler, and A. Christen. 2023. "High-Resolution Multi-scaling of Outdoor Human Thermal Comfort and Its Intra-urban Variability Based on Machine Learning." Preprint discussion paper. *Geoscientific Model Development*, July 26. https://doi.org/10.5194/gmd-2023-122.

Brimicombe, C., J.D. Runkle, C. Tuholske, D.I.V. Domeisen, C. Gao, J. Toftum, and I.M. Otto. 2024. "Preventing Heat-Related Deaths: The Urgent Need for a Global Early Warning System for Heat." *PLOS Climate* 3 (7): e0000437. https://doi.org/10.1371/journal.pclm.0000437.

Broadbent, A.M., E.S. Krayenhoff, and M. Georgescu. 2020. "Efficacy of Cool Roofs at Reducing Pedestrian-Level Air Temperature during Projected 21st Century Heatwaves in Atlanta, Detroit, and Phoenix (USA)." *Environmental Research Letters* 15 (8): 084007. https://doi.org/10.1088/1748-9326/ab6a23.

Bröde, P. 2021. "Issues in UTCI Calculation from a Decade's Experience." In *Applications of the Universal Thermal Climate Index UTCI in Biometeorology: Latest Developments and Case Studies*, edited by E.L. Krüger, 13–21. Cham, Switzerland: Springer. https://doi.org/10.1007/978-3-030-76716-7_2.

Bröde, P., D. Fiala, K. Błażejczyk, I. Holmér, G. Jendritzky, B. Kampmann, B. Tinz, and G. Havenith. 2012. "Deriving the Operational Procedure for the Universal Thermal Climate Index (UTCI)." *International Journal of Biometeorology* 56 (3): 481–94. https://doi.org/10.1007/s00484-011-0454-1.

34 | WORLD RESOURCES INSTITUTE

Modeling hyperlocal heat exposure with open-source data

Bunker, A., J. Wildenhain, A. Vandenberg, N. Henschke, J. Rocklöv, S. Hajat, and R. Sauerborn. 2016. "Effects of Air Temperature on Climate-Sensitive Mortality and Morbidity Outcomes in the Elderly: A Systematic Review and Meta-analysis of Epidemiological Evidence." eBioMedicine 6 (April): 258–68. https://doi.org/10.1016/j.ebiom.2016.02.034.

Buo, I., V. Sagris, J. Jaagus, and A. Middel. 2023. "High-Resolution Thermal Exposure and Shade Maps for Cool Corridor Planning." Sustainable Cities and Society 93 (June): 104499. https://doi.org/10.1016/j.scs.2023.104499.

Che, Y., X. Li, X. Liu, Y. Wang, W. Liao, X. Zheng, X. Zhang, X. Xu, Q. Shi, J. Zhu, H. Zhang, H. Yuan, and Y. Dai. 2024. "3D-GloBFP: The First Global Three-Dimensional Building Footprint Dataset." Earth System Science Data 16 (11): 5357–74. https://doi.org/10.5194/essd-16-5357-2024.

Chen, L., B. Yu, F. Yang, and H. Mayer. 2016. "Intra-urban Differences of Mean Radiant Temperature in Different Urban Settings in Shanghai and Implications for Heat Stress under Heat Waves: A GIS-Based Approach." Energy and Buildings 130 (October): 829–42. https://doi.org/10.1016/j.enbuild.2016.09.014.

Chen, Y.-C., T.-P. Lin, and A. Matzarakis. 2014. "Comparison of Mean Radiant Temperature from Field Experiment and Modelling: A Case Study in Freiburg, Germany." Theoretical and Applied Climatology 118 (January): 535–51. https://doi.org/10.1007/s00704-013-1081-z.

Colaninno, R.B., M. Hossei, L.L. Alhassan, and A. Sevtsuk. 2024. "A Sidewalk-Level Urban Heat Risk Assessment Framework Using Pedestrian Mobility and Urban Microclimate Modeling." Environment and Planning B: Urban Analytics and City Science 52 (5): 1071–90. https://journals.sagepub.com/doi/full/10.1177/23998083241280746.

CTBUH (Council on Tall Buildings and Urban Habitat). n.d. "Tall Building Height Calculator." https://store.ctbuh.org/PDF_Previews/Posters/Criteria_2010_Preview.pdf. Accessed February 17, 2026.

Di Napoli, C., C. Barnard, C. Prudhomme, H. Cloke, and F. Pappenberger. 2020. "Thermal Comfort Indices Derived from ERA5 Reanalysis." Copernicus Climate Change Service Climate Data Store. https://cds.climate.copernicus.eu/datasets/derived-utci-historical?tab=overview.

Ding, X., Y. Zhao, D. Strebel, Y. Fan, J. Ge, and J. Carmeliet. 2024. "A WRF-UCM-SOLWEIG Framework for Mapping Thermal Comfort and Quantifying Urban Climate Drivers: Advancing Spatial and Temporal Resolutions at City Scale." Sustainable Cities and Society 112 (October): 105628. https://doi.org/10.1016/j.scs.2024.105628.

ESA (European Space Agency). 2022. "Dataset Collection: ESA Land Surface Temperature Climate Change Initiative (LST_cci): Collection 1." Centre for Environmental Data Analysis. https://catalogue.ceda.ac.uk/uuid/57cfc8b38d914abc8de02b647e879e66/.

ESA. 2024. "Copernicus GLO-30 Digital Elevation Model." OpenTopography. https://portal.opentopography.org/raster?opentopold=OTS_DEM.032021.4326.3.

Esch, T., J. Zeidler, D. Palacios-Lopez, M. Marconcini, A. Roth, M. Mönks, B. Leutner, et al. 2020. "Towards a Large-Scale 3D Modeling of the Built Environment: Joint Analysis of TanDEM-X, Sentinel-2 and Open Street Map Data." Remote Sensing 12 (15): 2391. https://doi.org/10.3390/rs12152391.

Evola, G., V. Costanzo, L. Marletta, F. Nocera, M. Detommaso, and A. Urso. 2021. "An Investigation on the Radiant Heat Balance for Different Urban Tissues in Mediterranean Climate: A Case Study." Journal of Physics: Conference Series 2042 (1): 012046. https://doi.org/10.1088/1742-6596/2042/1/012046.

Fiala, D., G. Havenith, P. Bröde, B. Kampmann, and G. Jendritzky. 2012. "UTCI-Fiala Multi-node Model of Human Heat Transfer and Temperature Regulation." International Journal of Biometeorology 56 (May): 429–41. https://doi.org/10.1007/s00484-011-0424-7.

Gago, E.J., J. Roldan, R. Pacheco-Torres, and J. Ordóñez. 2013. "The City and Urban Heat Islands: A Review of Strategies to Mitigate Adverse Effects." Renewable and Sustainable Energy Reviews 25 (September): 749–58. https://doi.org/10.1016/j.rser.2013.05.057.

Gál, C.V., and N. Kántor. 2020. "Modeling Mean Radiant Temperature in Outdoor Spaces: A Comparative Numerical Simulation and Validation Study." Urban Climate 32 (June): 100571. https://doi.org/10.1016/j.uclim.2019.100571.

Grohmann, C.H. 2018. "Evaluation of TanDEM-X DEMs on Selected Brazilian Sites: Comparison with SRTM, ASTER GDEM and ALOS AW3D30." Remote Sensing of Environment 212 (June): 121–33. https://doi.org/10.1016/j.rse.2018.04.043.

Guardaro, M. 2023. "Strengthening Heat Action Plans in the United States." American Journal of Public Health 113 (5): 465–67. https://doi.org/10.2105/AJPH.2023.307260.

Guth, P.L., and T.M. Geoffroy. 2021. "LiDAR Point Cloud and IC-ESat-2 Evaluation of 1 Second Global Digital Elevation Models: Copernicus Wins." Transactions in GIS 25 (5): 2245–61. https://doi.org/10.1111/tgis.12825.

Guyer, H., M. Georgescu, D.M. Hondula, F. Wardenaar, and J. Vanos. 2021. "Identifying the Need for Locally-Observed Wet Bulb Globe Temperature across Outdoor Athletic Venues for Current and Future Climates in a Desert Environment." Environmental Research Letters 16 (12): 124042. https://doi.org/10.1088/1748-9326/ac32fb.

Guzder-Williams, B., E. Mackres, S. Angel, A.M. Blei, and P. Lamson-Hall. 2023. "Intra-urban Land Use Maps for a Global Sample of Cities from Sentinel-2 Satellite Imagery and Computer Vision." Computers, Environment and Urban Systems 100 (March): 101917. https://doi.org/10.1016/j.compenrupsys.2022.101917.

Havenith, G., D. Fiala, K. Blazejczyk, M. Richards, P. Bröde, I. Holmér, H. Rintamaki, Y. Benshabat, and G. Jendritzky. 2012. "The UTCI-Clothing Model." International Journal of Biometeorology 56 (May): 461–70. https://doi.org/10.1007/s00484-011-0451-4.

Hawker, L., P. Uhe, L. Paulo, J. Sosa, J. Savage, C. Sampson, and J. Neal. 2022. "A 30 m Global Map of Elevation with Forests and Buildings Removed." Environmental Research Letters 17 (2): 024016. https://doi.org/10.1088/1748-9326/ac4d4f.

Hersbach, H., B. Bell, P. Berrisford, S. Hirahara, A. Horányi, J. Muñoz-Sabater, J. Nicolas, et al. 2020. "The ERA5 Global Reanalysis." Quarterly Journal of the Royal Meteorological Society 146 (730): 1999–2049. https://doi.org/10.1002/qj.3803.

TECHNICAL NOTE | March 2026 | 35

Jänicke, B., F. Meier, F. Lindberg, S. Schubert, and D. Scherer. 2016. "Towards City-Wide, Building-Resolving Analysis of Mean Radiant Temperature." Urban Climate 15 (March): 83–98. https://doi.org/10.1016/j.uclim.2015.11.003.

Jin, L., S. Schubert, D. Fenner, M.H. Salim, and C. Schneider. 2022. "Estimation of Mean Radiant Temperature in Cities Using an Urban Parameterization and Building Energy Model within a Mesoscale Atmospheric Model." Meteorologische Zeitschrift 31 (1): 31–52. https://doi.org/10.1127/metz/2021/1091.

Kamath, H.G., M. Singh, N. Malviya, A. Martilli, L. He, D. Aliaga, C. He, et al. 2024. "GLOBAL Building heights for Urban Studies (UT-GLOBUS) for City- and Street-Scale Urban Simulations: Development and First Applications." Scientific Data 11 (1): 886. https://doi.org/10.1038/s41597-024-03719-w.

Kara, G.T., and T. Elbir. 2025. "Seasonal and Spatial Variability in the Accuracy of Hourly ERA5 and MERRA-2 Reanalysis Datasets: A 14-Year Comparison with Observed Meteorological Data in Türkiye." Atmospheric Research 325 (October): 108233. https://doi.org/10.1016/j.atmosres.2025.108233.

Keith, L., S. Meerow, D. Hondula, V.K. Turner, and J.C. Arnott. 2021. "Deploy Heat Officers, Policies and Metrics." Nature 598 (7879): 29–31. https://doi.org/10.1038/d41586-021-02677-2.

Kephart, J.L., B.N. Sánchez, J. Moore, L.H. Schinasi, M. Bakhtsiyarava, Y. Ju, N. Gouveia, et al. 2022. "City-Level Impact of Extreme Temperatures and Mortality in Latin America." Nature Medicine 28 (8): 1700–05. https://doi.org/10.1038/s41591-022-01872-6.

Kim, E.-S., S.-H. Yu, C.-Y. Park, H.-K. Heo, and D.-K. Lee. 2022. "Estimation of Mean Radiant Temperature in Urban Canyons Using Google Street View: A Case Study on Seoul." Remote Sensing 14 (2): 260. https://www.mdpi.com/2072-4292/14/2/260.

Kong, F., J. Chen, A. Middel, H. Yin, M. Li, T. Sun, N. Zhang, et al. 2022. "Impact of 3-D Urban Landscape Patterns on the Outdoor Thermal Environment: A Modelling Study with SOLWEIG." Computers, Environment and Urban Systems 94 (June): 101773. https://doi.org/10.1016/j.compenvurbsys.2022.101773.

Krayenhoff, E.S., A.M. Broadbent, L. Zhao, M. Georgescu, A. Middel, J.A. Voogt, A. Martilli, D.J. Sailor, and E. Erell. 2021. "Cooling Hot Cities: A Systematic and Critical Review of the Numerical Modelling Literature." Environmental Research Letters 16 (5): 053007. https://doi.org/10.1088/1748-9326/abdc1.

Landsat Missions. n.d. "Landsat Collection 2 Surface Temperature." US Geological Survey. https://www.usgs.gov/landsat-missions/landsat-collection-2-surface-temperature. Accessed April 14, 2025.

Lau, K.K.-L., C. Ren, J. Ho, and E. Ng. 2016. "Numerical Modelling of Mean Radiant Temperature in High-Density Sub-tropical Urban Environment." Energy and Buildings 114 (February): 80–86. https://doi.org/10.1016/j.enbuild.2015.06.035.

Li, X., T. Chakraborty, and G. Wang. 2023. "Comparing Land Surface Temperature and Mean Radiant Temperature for Urban Heat Mapping in Philadelphia." Urban Climate 51 (September): 101615. https://doi.org/10.1016/j.uclim.2023.101615.

Li, X., G. Wang, B. Zaitchik, A. Hsu, and T. Chakraborty. 2024. "Sensitivity and Vulnerability to Summer Heat Extremes in Major Cities of the United States." Environmental Research Letters 19 (9): 094039. https://doi.org/10.1088/1748-9326/ad6c64.

Lindberg, F., B. Holmer, and S. Thorsson. 2008. "SOLWEIG 1.0: Modelling Spatial Variations of 3D Radiant Fluxes and Mean Radiant Temperature in Complex Urban Settings." International Journal of Biometeorology 52 (June): 697–713. https://doi.org/10.1007/s00484-008-0162-7.

Lindberg, F., and C.S.B. Grimmond. 2011a. "The Influence of Vegetation and Building Morphology on Shadow Patterns and Mean Radiant Temperatures in Urban Areas: Model Development and Evaluation." Theoretical and Applied Climatology 105 (3): 311–23. https://doi.org/10.1007/s00704-010-0382-8.

Lindberg, F., and C.S.B. Grimmond. 2011b. "Nature of Vegetation and Building Morphology Characteristics across a City: Influence on Shadow Patterns and Mean Radiant Temperatures in London." Urban Ecosystems 14 (June): 617–34. https://doi.org/10.1007/s11252-011-0184-5.

Lindberg, F., C.S.B. Grimmond, A. Gabey, B. Huang, C. Kent, T. Sun, N.E. Theeuwes, et al. 2018. "Urban Multi-scale Environmental Predictor (UMEP): An Integrated Tool for City-Based Climate Services." Environmental Modelling and Software 99 (January): 70–87. https://doi.org/10.1016/j.envsoft.2017.09.020.

Macintyre, H. L., and C. Heaviside. 2019. "Potential Benefits of Cool Roofs in Reducing Heat-Related Mortality during Heatwaves in a European City." Environment International 127 (June): 430–41. https://doi.org/10.1016/j.envint.2019.02.065.

Meadows, M., S. Jones, and K. Reinke. 2024. "Vertical Accuracy Assessment of Freely Available Global DEMs (FABDEM, Copernicus DEM, NASADEM, AW3D30 and SRTM) in Flood-Prone Environments." International Journal of Digital Earth 17 (1): 2308734. https://doi.org/10.1080/17538947.2024.2308734.

Meili, N., G. Manoli, P. Burlando, J. Carmeliet, W.T.L. Chow, A.M. Coutts, M. Roth, E. Velasco, E.R. Vivoni, and S. Faticchi. 2021. "Tree Effects on Urban Microclimate: Diurnal, Seasonal, and Climatic Temperature Differences Explained by Separating Radiation, Evapotranspiration, and Roughness Effects." Urban Forestry & Urban Greening 58 (March): 126970. https://doi.org/10.1016/j.ufug.2020.126970.

Middel, A., and E.S. Krayenhoff. 2019. "Micrometeorological Determinants of Pedestrian Thermal Exposure during Record-Breaking Heat in Tempe, Arizona: Introducing the MaRTy Observational Platform." Science of The Total Environment 687 (October): 137–51. https://doi.org/10.1016/j.scitotenv.2019.06.085.

Middel, A., S. AlKhaled, F.A. Schneider, B. Hagen, and P. Coseo. 2021. "50 Grades of Shade." Bulletin of the American Meteorological Society 102 (9): E1805–20. https://doi.org/10.1175/BAMS-D-20-0193.1.

Milojevic-Dupont, N., F. Wagner, F. Nachtigall, J. Hu, G.B. Brüser, M. Zumwald, F. Biljecki, et al. 2023. "EUBUCCO v0.1: European Building Stock Characteristics in a Common and Open Database for 200+ Million Individual Buildings." Scientific Data 10 (1): 147. https://doi.org/10.1038/s41597-023-02040-2.

36 | WORLD RESOURCES INSTITUTE

Modeling hyperlocal heat exposure with open-source data

Monteiro dos Santos, D., R. Libonati, B.N. Garcia, J.L. Geirinhas, B. Bresani Salvi, E. Lima e Silva, J.A. Rodrigues, et al. 2024. "Twenty-First-Century Demographic and Social Inequalities of Heat-Related Deaths in Brazilian Urban Areas." PLOS One 19 (1): e0295766. https://doi.org/10.1371/journal.pone.0295766.

Muse, N., A. Clement, and K.J. Mach. 2024. "Daytime Land Surface Temperature and Its Limits as a Proxy for Surface Air Temperature in a Subtropical, Seasonally Wet Region." PLOS Climate 3 (10): e0000278. https://doi.org/10.1371/journal.pclm.0000278.

NASA (National Aeronautics and Space Administration). 2025. "ECOSTRESS Tiled Land Surface Temperature and Emissivity Instantaneous L2 Global 70 m V002." Earthdata. https://cmr.earthdata.nasa.gov/search/concepts/C2076090826-LPCLOUD.html.

Osama, N., Z. Shao, and M. Freeshah. 2023. "The FABDEM Outperforms the Global DEMs in Representing Bare Terrain Heights." Photogrammetric Engineering & Remote Sensing 89 (10): 613–24. https://doi.org/10.14358/PERS.23-00026R2.

Overture Maps. 2025. "Overview." https://docs.overturemaps.org/guides/buildings/#overview.

Pathmanabhan, A., and S. Dinesh. 2007. "The Effect of Gaussian Blurring on the Extraction of Peaks and Pits from Digital Elevation Models." Discrete Dynamics in Nature and Society 2007 (1): 062137. https://doi.org/10.1155/2007/62137.

Pesaresi, M., and P. Politis. 2023. "GHS-BUILT-H R2023A: GHS Building Height, Derived from AW3D30, SRTM30, and Sentinel2 Composite (2018)." European Commission, Joint Research Centre. https://doi.org/10.2905/85005901-3A49-48DD-9D19-6261354F56FE.

Prasad, P.S.H., and A.N.V. Satyanarayana. 2024. "Assessment of Universal Thermal Climate Index (UTCI) Using the WRF-UCM Model over a Metropolitan City in India." International Journal of Biometeorology 68 (September): 1857–70. https://doi.org/10.1007/s00484-024-02714-5.

Saunier, S., B. Pflug, I.M. Lobos, B. Franch, J. Louis, R. de los Reyes, V. Debaecker, et al. 2022. "Sen2Like: Paving the Way towards Harmonization and Fusion of Optical Data." Remote Sensing 14 (16): 3855. https://doi.org/10.3390/rs14163855.

Skamarock, W.C., and J.B. Klemp. 2008. "A Time-Split Nonhydrostatic Atmospheric Model for Weather Research and Forecasting Applications." Journal of Computational Physics 227 (7): 3465–85. https://doi.org/10.1016/j.jcp.2007.01.037.

Smith, I.A., D. Li, D.K. Fork, G.A. Wellenius, and L.R. Hutyra. 2025. "Integrated Tree Canopy Expansion and Cool Roofs Can Optimize Air Temperature and Heat Exposure Reductions in Boston." Communications Earth & Environment 6 (July): 507. https://doi.org/10.1038/s43247-025-02462-3.

Thom, J.K., A.M. Coutts, A.M. Broadbent, and N.J. Tapper. 2016. "The Influence of Increasing Tree Cover on Mean Radiant Temperature across a Mixed Development Suburb in Adelaide, Australia." Urban Forestry & Urban Greening 20: 233–42. https://doi.org/10.1016/j.ufug.2016.08.016.

Thorsson, S., J. Rocklöv, J. Konarska, F. Lindberg, B. Holmer, B. Dousset, and D. Rayner. 2014. "Mean Radiant Temperature: A Predictor of Heat Related Mortality." Urban Climate 10 (December): 332–45. https://doi.org/10.1016/j.uclim.2014.01.004.

Tolan, J., H.-I. Yang, B. Nosarzewski, G. Couairon, H.V. Vo, J. Brandt, J. Spore, et al. 2024. "Very High Resolution Canopy Height Maps from RGB Imagery Using Self-Supervised Vision Transformer and Convolutional Decoder Trained on Aerial Lidar." Remote Sensing of Environment 300 (January): 113888. https://doi.org/10.1016/j.rse.2023.113888.

Tong, S., J. Prior, G. McGregor, X. Shi, and P. Kinney. 2021. "Urban Heat: An Increasing Threat to Global Health." BMJ 375 (October): n2467. https://doi.org/10.1136/bmj.n2467.

Turner, V.K., A. Middel, and J.K. Vanos. 2023. "Shade Is an Essential Solution for Hotter Cities." Nature 619 (7971): 694–97. https://doi.org/10.1038/d41586-023-02311-3.

van der Schrier, G. 2021. Development of R-Based Scripts and Manual to Calculate Daily Maps of the Universal Thermal Climate Index (UTCI). Reading, UK: Copernicus Climate Change Service, European Centre for Medium-Range Weather Forecasts. https://surfobs.climate.copernicus.eu/documents/C3S_D31la_Lot4.3.1.10_script_and_manual_UTCI_v1.pdf.

Vieira, S.M., U. Kaymak, and J.M.C. Sousa. 2010. "Cohen's Kappa Coefficient as a Performance Measure for Feature Selection." Paper prepared for the International Conference on Fuzzy Systems, Barcelona, Spain, July 18–23. https://doi.org/10.1109/FUZZY.2010.5584447.

VITO (Vlaamse Instelling voor Technologisch Onderzoek). n.d. "UrbSim, the Urban Climate Simulator." https://vito.be/en/applications/urbsim-urban-climate-simulator. Accessed February 17, 2026.

Wallenberg, N., F. Lindberg, B. Holmer, and S. Thorsson. 2020. "The Influence of Anisotropic Diffuse Shortwave Radiation on Mean Radiant Temperature in Outdoor Urban Environments." Urban Climate 31 (March): 100589. https://doi.org/10.1016/j.uclim.2020.100589.

Wesley, E.J., E. Mackres, T. Wong, K. Shickman, C. Janssen, and M. Mulder. 2026. "Mapping Scenarios and Estimating the Potential for Heat-Resilient Infrastructure in Cities." Technical Note. Washington, DC: World Resources Institute.

Yi, S., X. Li, C. Ma, R. Wang, Y. Zhou, Q. Xu, and T. Zhao. 2025. "Assessing the Differential Impact of Vegetated and Built-up Areas on Heat Exposure Environment: A Case Study of Los Angeles." Building and Environment 271 (March): 112538. https://doi.org/10.1016/j.build-env.2025.112538.

Zhao, L., K. Oleson, E. Bou-Zeid, E.S. Krayenhoff, A. Bray, Q. Zhu, Z. Zheng, C. Chen, and M. Oppenheimer. 2021. "Global Multi-model Projections of Local Urban Climates." Nature Climate Change 11 (2): 152–157. https://doi.org/10.1038/s41558-020-00958-8.

TECHNICAL NOTE | March 2026 | 37

## Acknowledgments

We would like to thank Google.org for supporting this work. We would also like to thank Dr. Lucy Hutyra, Dr. Ian Smith, and Leeza Moldavchuk at Boston University for their thoughtful advice. Reynolds Kihura, Eric Mackres, Chris Rowe, Lindy Schofield, Saif Shabou, Elizabeth Wesley, and Weiqi Zhou at WRI provided consultation and support during the development of this work. Isaac Buo, Sarah Carter, Carolina Faccin, Sahana Goswami, Jean Claude Iradukunda, Robin King, Amit Kumar, Anne Maassen, Katrina McLaughlin, Oscar Pozos, Rhiannon Leigh Rognstad, Gregory Taff, and Elizabeth Wesley reviewed this manuscript. Our thanks to the cities of Monterrey, Mexico; Rio de Janeiro, Brazil; Amsterdam, the Netherlands; and Cape Town, South Africa for their collaboration and for providing locally-collected lidar data.

## About the authors

**Ruth A. Engel** is the Extreme Heat and Environmental Health Data Scientist for the WRI Ross Center for Sustainable Cities at WRI.

**Kenn Cartier** is a Geospatial Data Engineer at WRI.

**Hyeji Joh** is a Geospatial Data Science Intern at WRI.

**Zhuoyue Wang** is a Geospatial Data Urban Heat Intern at WRI.

**Theodore Wong** is a Research and Project Associate, Urban Analytics, at WRI Ross Center for Sustainable Cities at WRI.

**Xiaojiang Li** is an Assistant Professor of Urban Spatial Analytics at the Weitzman School of Design, University of Pennsylvania.

Ruth A. Engel conceived and designed the analyses and wrote the paper. Xiaojiang Li and Kenn Cartier created the tools to perform the analysis and contributed substantially to the intellectual framework. Hyeji Joh and Zhuoyue Wang contributed data analyses. Theodore Wong provided intellectual contributions during revisions.

## About WRI

World Resources Institute works to improve people's lives, protect and restore nature, and stabilize the climate. As an independent research organization, we leverage our data, expertise, and global reach to influence policy and catalyze change across systems like food, land and water; energy; and cities. Our 2,000+ staff work on the ground in more than a dozen focus countries and with partners in over 50 nations.

---![Creative Commons logo]() creativecommons

Copyright 2026 World Resources Institute. This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of the license, visit <https://creativecommons.org/licenses/by/4.0/>

![World Resources Institute logo]() WORLD RESOURCES INSTITUTE

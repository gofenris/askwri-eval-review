---
doc_id: FINAL_Working Paper_Just Transition_1905
source_pdf: documents/FINAL_Working Paper_Just Transition_1905.pdf
extraction_method: postgres-full-text
parse_backend: mistral
parse_model: mistral-ocr-latest
char_count: 121909
title: "Driving a Just EV Transition in India: Supply Chain Practices for Large Automotive Manufacturing Enterprises"
title_en: "Driving a Just EV Transition in India: Supply Chain Practices for Large Automotive Manufacturing Enterprises"
authors: Priya Bansal; Priyal Shah; Tavleen Singh; Chaitanya Kanuri; Ashwini Hingne; Anuradha Ranganath
date_published: 2026-05-29
year_published: 2026
article_type: Working Paper
wri_primary_office: WRI India
language: en
languages: [en]
doi: 10.46830/wriwp.25.00053
status: searchable
summary: This working paper examines how India’s rapid EV transition—targeting 30% of vehicle sales by 2030 and projected to reach 50–65% by 2035—will reshape automotive supply chains and disproportionately affect micro, small, and medium enterprises (MSME) component suppliers. MSMEs currently produce 75–80% of ICEV component volumes but lack capacities for EV parts, while 60–70% of EV components are imported. The authors find a clear business case for original equipment manufacturers (OEMs) and large Tier‑1 suppliers to adopt a “partner” approach that supports MSMEs to ensure a just transition and strengthen supply‑chain resilience. Benefits for large enterprises include long‑run cost efficiencies, better quality/cost/delivery control, accelerated innovation and R&D, sustained export competitiveness, and alignment with localization mandates. MSME barriers identified include financing shortfalls, tooling and testing costs, skill and technology gaps, and uncertain demand. Recommended practices include supplier capability programs, technology transfer and contract R&D, financing and de‑risking mechanisms, digital integration for visibility, demand aggregation, and practical steps like embedded engineering support and standardized guide drawings.
---

WRI INDIA

WORKING PAPER

# Driving a just electric vehicle transition in India

Supply-chain practices for large automotive manufacturing enterprises

Priya Bansal, Priyal Shah, Tavleen Singh, Chaitanya Kanuri, Ashwini Hingne, and Anuradha Ranganath

CONTENTS

Highlights ... 1
Executive Summary ... 2
Background ... 6
Context ... 7
Study Design and Methodology ... 9
Research Findings ... 14
Conclusion & Recommendations ... 26
Appendix A ... 27
Abbreviations ... 28
Glossary ... 29
Endnotes ... 29
References ... 30
Acknowledgments ... 34
About the authors ... 34

Working Papers contain preliminary research, analysis, findings, and recommendations. They are circulated to stimulate timely discussion and critical feedback, and to influence ongoing debate on emerging issues.

Suggested Citation: Bansal, P., P. Shah, T. Singh, C. Kanuri, A. Hingne, and A. Ranganath. 2026. “Driving a just electric vehicle transition in India: Supply-chain practices for large automotive manufacturing enterprises”. Working Paper. New Delhi: WRI India. Available online at doi.org/10.46830/wriwp.25.00053.

Highlights

- India’s projected transition to electric vehicles (EVs) will produce major changes across its automotive manufacturing sector, given fundamental differences in how internal combustion engine vehicles (ICEVs) and EVs are manufactured.
- These changes risk disrupting the relationship between large enterprises (comprising original equipment manufacturers [OEMs] and large Tier-1 automotive component manufacturers [ACMs]) and ACMs that are micro, small, and medium enterprises (MSMEs).
- Currently, over 75–80 percent of ICEV components (by volume) are manufactured by domestic MSMEs and supplied to large enterprises. However, about 60–70 percent of EV components are imported because MSMEs lack the capacities and technological capabilities to produce them. Thus, accelerating the transition risks inequity by leaving MSMEs behind.
- There is a strong interdependence among OEMs, large Tier-1 ACMs, and MSMEs in the current ICEV ecosystem, where supply chain risks and benefits are shared. A business case can thus be made for OEMs and large Tier-1 ACMs to help their MSME suppliers diversify to EV component production.
- Based on the secondary literature and industry consultations, this paper identifies a clear business case and outlines practices for large enterprises to support a just EV transition for their MSME suppliers.

WRI INDIA

WORKING PAPER | May 2026 | 1

## Executive summary

### Context

India has embarked on an ambitious EV transition, targeting a 30 percent share of EVs in total vehicle sales by 2030 (PIB 2021). The Government of India (GoI) has allocated over INR 673.33 billion (Sen et al. 2025) to EV promotion, driving a compound annual growth rate of 84.9 percent in EV sales between 2020 and 2024. By 2035, the share of EVs in total automobile sales in India is projected to reach 50–65 percent (IEA 2024). The projected transition has significant implications for ACMs, primarily MSMEs. EV manufacturing differs from ICEV manufacturing due to changes in component systems, especially the powertrain: the components that generate power to thrust the vehicle into motion (Anilan and Vij 2024; Dash 2023; Sen et al. 2025). Moreover, EVs require only one-seventh of the mechanical powertrain components needed for ICEVs (PwC 2019), creating challenges for India's ACMs, due to substantial reductions in production volumes.

MSMEs constitute 75–80 percent of the ACM industry's production volume and generate over half the ICEV sector's turnover (CRISIL Research 2024; IBEF 2025). Although OEMs and large Tier-1 ACMs (hereafter referred to as "large enterprises") are diversifying portfolios to capitalize on EV demand, MSMEs require support to participate in this market equitably. Currently, large enterprises import 60–70 percent of EV components because there is a lack of local supply-chain production capacities and technological capabilities to manufacture these components (Seetharaman et al. 2023). Research suggests that 47 percent of automotive MSMEs are expected to experience moderate to high transition impacts on their business due to the projected EV transition (iForest 2024). An inequitable EV transition poses two critical risks. First, in the long term, it will negatively impact MSMEs and the millions of semiskilled and contractual workers they employ. Second, MSMEs' lack of domestic EV component manufacturing capabilities would result in a continued reliance on imports, making supply chains vulnerable to geopolitical tensions while undermining India's ability to control the pace and sustainability of its EV transition.

Building economic competitiveness and supply-chain resilience and achieving an equitable EV transition are complementary objectives. Although government and industry associations provide policy frameworks and financial incentives, large enterprises are uniquely positioned to unlock MSMEs' potential through their technological expertise, market access, and financial resources. This can help bridge the capability gaps facing MSME suppliers while simultaneously strengthening India's position as a global automotive producer.

As part of the same supply chain, large automotive enterprises and MSMEs share certain benefits and risks.

A mutually beneficial outcome can be achieved using a

“partner” approach in which large enterprises adopt practices that support their suppliers’ transitions, especially specific types of MSME suppliers, in advancing electric mobility (Said et al. 2025). However, from the perspective of an enterprise, a clear business case for this approach must exist. At present, this business case remains poorly understood.

### About this paper

This paper contributes to a limited body of literature by examining the business case for large automotive enterprises to support their MSME suppliers' EV transition and laying out the practices they can adopt to advance mutually beneficial outcomes. The study addresses three research questions (RQ \( _{2} \) ):

RQ1: What is the business case for OEMs and large Tier-1 ACMs to support a just \( ^{1} \) EV transition for their automotive supply chain, especially MSMEs, in India?
RQ2: What are the challenges that MSMEs face due to the projected EV transition?
RQ3: What examples, Indian or global, could guide a partner approach between large automotive enterprises and MSMEs to manage India's projected EV transition?

The study employs a mixed-methods approach, combining primary research (through semi-structured key-informant interviews and focused group discussions) with secondary research. The primary research adopted a pan-India approach, covering India's major automotive clusters (Haryana, Maharashtra, Karnataka, and Tamil Nadu). Purposive sampling \( ^{2} \) was employed. Data were collected from 73 respondents comprising 12 OEMs and 61 ACMs (with ACMs comprising both large Tier-1 enterprises and MSMEs) across different tiers, sizes, and product portfolios (see Table ES-1). The sample included enterprises holding a significant market share, with OEMs possessing a 40 percent or greater share across vehicle segments in EV manufacturing.

### Key findings

In the traditional Indian automotive industry, MSME suppliers often serve as extended arms of their customer OEMs and large Tier-1 ACMs. Their customers define the product specifications and oversee the quality, pricing, and other terms of contract, thus allowing them to exert considerable influence over how the market is driven. While MSMEs are typically resource strapped and lack access to formal credit, their customers possess technological expertise, market access, and financial resources. MSME suppliers thus adhere to their customers' specifications in relation to purchase orders for automotive component requirements. Meeting customer specifications becomes critical for them to ensure product

2

[Non-Text]

WRI INDIA

Driving a just electric vehicle transition in India: Supply-chain practices for large automotive manufacturing enterprises

performance, safety certifications, and regulatory adherence in automotive systems. As part of this customer–supplier relationship, large enterprises either explicitly require their suppliers to make changes to their manufacturing processes and/or infrastructure to cater to their requirements (the “push” model) or impose procurement conditions that suppliers must meet to be selected for a new component supply (the “pull” model) (Said et al. 2025).

There is a clear business case for large Indian automotive enterprises to adopt a partner approach with their MSME suppliers during the projected EV transition. In this approach, they adopt practices that support their suppliers' transitions, especially specific types of MSME suppliers. This approach will help large enterprises achieve the following five objectives: enabling long-run cost efficiencies; gaining greater control over quality, cost, delivery, and service; spurring innovation and enhancing R&D capacities; sustaining export competitiveness; and effectively leveraging the GoI's EV localization mandates. This approach will also help large enterprises ensure a just EV transition for their own supply chain by preventing the reinforcement of challenges that can arise between

large enterprises and MSMEs. These challenges can be directly attributed to the lack of a partner approach during the transition (see Figure ES-1). Traditional push or pull models work effectively with foreign suppliers and local large Tier-1 ACMs, which are well positioned to make investments in changing processes and/or infrastructure or can meet the required global procurement conditions. However, such models automatically eliminate most local MSMEs, which are unable to do so.

■ Five key parameters underpin the business case for large Indian automotive enterprises to adopt a partner approach:

Long-run cost efficiencies: Local sourcing can enable cost reductions in the long run through greater economies of scale. As part of localization efforts, large enterprises will ensure standardization across suppliers in manufacturing child \( ^{3} \) parts for EV components. This will help them better plan investments in infrastructure, technology, and capacity-building for MSMEs because standardization drives consistency in product quality. This, in turn, will aid in cost reduction.

Table ES-1 | Profile of respondent enterprises by market segment and enterprise size

|  CATEGORY OF RESPONDENT ENTERPRISE | NUMBER OF RESPONDENT ENTERPRISES | ENTERPRISE SIZE | % OUT OF TOTAL SAMPLE  |
| --- | --- | --- | --- |
|  OEMs  |   |   |   |
|  ICEV and EV | 6 | Large enterprises | 8%  |
|  BORN-EV | 6 | 2 Large enterprises3 Medium enterprises1 Small enterprise | 8%  |
|  ACMs  |   |   |   |
|  TIER-1 | 29 | 8 Large enterprises21 MSMEs | 40%  |
|  TIER-2 | 20 | MSMEs | 27%  |
|  TIER-3 | 12 | MSMEs | 16%  |
|  TOTAL | 73 |  | 100%  |

Notes: ACM = automotive component manufacturer. EV = electric vehicle. ICEV = internal combustion engine vehicle. MSME = micro, small, and medium enterprise. OEM = original equipment manufacturer.

ICEV and EV OEMs refer to legacy ICEV OEMs diversifying into EVs. Within ACMs, Tier-1 suppliers supply components primarily to OEMs, Tier-2 supply to Tier-1, and Tier-3 supply to Tier 2 and Tier 1. Tier-1 ACMs comprise both large enterprises and MSMEs. MSMEs are spread across Tier-1, Tier-2, and Tier-3 ACMs.

In the Indian context, enterprises are classified into different sizes based on their annual turnover (PIB 2025a) in INR as follows:

Micro-sized enterprises: Turnover < 100 million

Small-sized enterprises: Turnover ≥ 100 million and < 1 billion

Medium-sized enterprises: Turnover ≥ 1 billion and ≤ 5 billion

Large-sized enterprises: Turnover > 5 billion.

Source: WRI India authors.

WORKING PAPER | May 2026

3

**Figure ES-1 | Reinforcement of challenges across the value chain in the absence of a “partner” approach for the projected EV transition**

![img-0.jpeg](img-0.jpeg)

Note: ACM = automotive component manufacturer. EV = electric vehicle. MSME = micro, small, and medium enterprise.

Source: WRI India authors.

- ☐ **Greater control over quality, cost, delivery, and service:** Local sourcing enables better quality management through seamless data linkage across the supply chain, faster delivery schedules, and elimination of logistics-related costs (including inventory costs and import duties).
- ☐ **Spurring innovation and enhancing R&D capacities:** Large enterprises and MSMEs can co-create innovative EV components, boosting revenues for both. Successful examples include suppliers sharing their knowledge and expertise in their areas of core competence with their customers (large enterprises).
- ☐ **Sustaining export competitiveness:** Localization can help India sustain its export competitiveness in the automotive sector. India’s automotive component exports reached US$12.8 billion in FY24. Europe and some states in the United States are setting targets to reduce ICEV sales by 2035 while also seeking alternatives for de-risking and diversifying their supply chains. India can invest in MSMEs’ capabilities to enable them to match global standards of product competitiveness and delivery.
- ☐ **Leveraging the GoI’s EV localization mandates:** Sourcing EV components through local MSME suppliers (provided they have the requisite capabilities and capacities) would enable large enterprises to leverage the benefits of localization mandates.

- ■ **MSMEs face recurring challenges that hinder their EV transition preparedness, in contrast to their customer OEMs and large Tier-1 ACMs, which are well-placed to transition.** Financial constraints—high capital expenditure, tooling costs, competing ICEV–EV priorities, prohibitive testing costs, and limited access to government incentives—emerge as the most significant barrier. Technical know-how and skilling gaps exist, with EV manufacturing demanding higher precision, automation, and co-development approaches; it is estimated that 31 percent of ICEV jobs will be affected by the EV transition (iForest 2024). Competition from well-funded EV start-ups and Chinese imports (benefiting from more advanced technology and economies of scale) creates intense pressure. Technology access limitations, R&D constraints, import dependence (with 5–40 percent duties), and the absence of clear roadmaps and assured markets prevent informed investment decisions. Many of these challenges persist because EV investments must be made while existing ICEV programs continue, creating simultaneous cash-flow and capacity pressures for MSMEs.
- ■ **Our research documents concrete practices that large enterprises can implement to address these challenges.** These practices are organized into five categories: strategic supplier development and capability-building programs, technology transfer and innovation partnerships, financial support and risk mitigation, digital integration and supply-chain visibility, and market access (see Table ES-2).

4 | WRI INDIA

Driving a just electric vehicle transition in India: Supply-chain practices for large automotive manufacturing enterprises

Table ES-2 | Examples of strategic interventions by large automotive enterprises to resolve their MSME suppliers' EV transition challenges

|  S.NO. | CATEGORIES OF INTERVENTIONS (BY LARGE AUTOMOTIVE ENTERPRISES), WITH EXAMPLES | MSME CHALLENGE THAT THE INTERVENTION ADDRESSES  |
| --- | --- | --- |
|  1. | Strategic supplier development and capability building programs  |   |
|   | Technical training and/or skill development programsQuality management and/or certification programs | Lack of systems for scalabilityLack of technical know-how, technology, R&D and skilling gaps  |
|  2. | Technology transfer and innovation partnerships  |   |
|   | Strategic technology transfer protected through exclusive contractsStrategic, non-exclusive technology transferExposure visits to global automotive facilitiesEstablishment of shared R&D centersStrategic joint ventures (JVs)Contract R&D arrangements for access to MSMEs' specialized skillsets and EV start-ups' niche technologiesMoving from build-to-print (BTP) to co-creation of products through supplier hackathons | Lack of technical know-how, technology, R&D and skilling gapsFinancial constraints and lack of transition capital  |
|  3. | Financial support and risk mitigation  |   |
|   | Bulk procurement of components with cost arbitrage passed to MSMEsAssured long-term offtake agreementsPartnerships with financial institutions creating tailored loan products | Financial constraints and lack of transition capital  |
|  4. | Digital integration and supply chain visibility  |   |
|   | Cloud-based supplier portals for real-time access to production schedules and demand forecasts | Competition from EV start-ups and importsTrust deficit in domestic MSME capabilities  |
|  5. | Market access  |   |
|   | Demand aggregation through Manufacturing-as-a-Service platformsWhite-labeling arrangements with OEMs and large Tier-1 ACMs for EV component manufacturing | Missing roadmaps and lack of assured market and linkagesCompetition from EV start-ups and importsTrust deficit in domestic MSME capabilities  |

Note: ACM = automotive component manufacturer. EV = electric vehicle. MSME = micro, small, and medium enterprise. OEM = original equipment manufacturer.
Source: WRI India authors.

### Key recommendations

Based on these findings, the study recommends five priority interventions for large Indian automotive enterprises:

Facilitate knowledge-sharing and hands-on training for EV component manufacturing: Large enterprises could enable knowledge-sharing with MSME suppliers for EV component manufacturing by providing embedded engineering support - placing their engineers at supplier facilities for extended periods; creating digital knowledge platforms; facilitating their MSME suppliers' visits to global automotive

facilities; and providing them exposure to the final product requirements of end users.

Create guide drawings and technical specification documents for manufacturing EV child parts to enable standardization across MSME suppliers: This entails developing detailed parameters with standardized tolerances that MSMEs can follow, establishing quality certification processes and testing protocols aligned with automotive standards, and creating material specification guidelines to ensure consistency in product quality across suppliers.

WORKING PAPER | May 2026

5

**Facilitate access to infrastructure financing for MSMEs through de-risking mechanisms:** Large enterprises can support MSMEs with financial resources needed for acquisition of machinery and equipment that may either not be available locally or may be available but cannot enable manufacturing at scale or deliver the quality needed. Reasonable payback plans and risk sharing would enable MSMEs to adopt technology faster and expand their markets by using the same infrastructure for other customers.

**Facilitate contract R&D in EV component manufacturing:** Large enterprises can establish joint development agreements or sponsored research contracts with their MSME suppliers for specialized skillsets (in areas such as winding for motors), and with EV start-ups for access to niche EV technologies. Sharing of costs, risks, and intellectual property can be decided upon based on feasibility.

**Enable demand aggregation for EV component requirements at the large enterprise level:** Unlike large enterprises, sub-tier suppliers often produce common components such as seals and materials for heat dissipation. If a group of large enterprises collectively aggregates demand for specific EV components and engages with MSMEs for their supply, these suppliers will find it easier to make investment decisions due to increased order visibility and risk diversification.

## Background

To accelerate a transition to electric vehicles (EVs) and thus reduce India's dependence on oil imports as well as emissions from the road transport sector, the Government of India (GoI) has instituted a wide range of policy frameworks, ambitious EV targets—a 30 percent share of EVs in total vehicles sold by 2030 (PIB 2021)—and financial support. In particular, EV promotion schemes have registered a consolidated outlay of more than INR 673.33 billion (PIB 2025c; Sen et al. 2025). As a result, India registered a compound annual growth rate (CAGR) of 84.9 percent in EV sales between 2020 and 2024 (MoRTH 2025), and the country's EV sales share is expected to reach one-third of the total vehicle sales by 2030, dominated by the two- and three-wheeler segments (IEA 2025).

Accelerating the EV transition is important for decarbonizing the road transport sector; however, it also has significant implications for India's automotive manufacturing industry. EV manufacturing differs from traditional internal combustion engine vehicle (ICEV) manufacturing due to fundamental changes in component systems, especially the powertrain, which comprises the components that generate power to thrust the vehicle into motion (Anilan and Vij 2024; Dash 2023; Sen et al. 2025). Moreover, EVs require only a seventh of the mechanical powertrain components required in ICEVs (PwC 2019). These changes entail a restructuring of

automotive supply chains, as well as investments in retooling manufacturing facilities and reskilling automotive workers.

Original equipment manufacturers (OEMs) and large Tier-1 automotive component manufacturers (ACMs) are diversifying their portfolios to leverage the growing demand for EVs, both domestically and globally. However, studies find that micro, small, and medium enterprises (MSMEs), which account for 75–80 percent of the production volume of ACMs (CRISIL Research 2024; IBEF 2025), are largely unable to take advantage of the emerging opportunities, due to a lack of access to finance, technology, infrastructure, and skilled labor, alongside other systemic barriers (Dash 2023; Sen et al. 2025; Bansal et al. 2024). Research suggests that nearly 47 percent of MSME ACMs are expected to experience moderate to large impacts on their business due to the projected EV transition (iForest 2024). At the same time, large automotive enterprises currently rely on imports for approximately 60–70 percent of EV components (by value) (Seetharaman et al. 2023); in contrast, only 10–20 percent of ICEV components are imported. This situation risks diminishing the global competitiveness of India's automotive industry, resulting in adverse socioeconomic impacts.

**First, in the long term, an inequitable EV transition will negatively impact MSMEs and the millions of semiskilled and contractual workers they employ.** Because MSMEs are strapped for resources and lack access to formal credit—only 19 percent of their credit demand was met through formal sources in FY21 (NITI Aayog 2025b)—they are largely unable to innovate independently and diversify into EV component manufacturing. Although government initiatives such as production-linked incentive schemes have been introduced to boost local manufacturing, MSMEs were unable to access them due to their stringent eligibility criteria (Khan 2021). The continued albeit slower growth of ICEV production will mask the negative impacts of the EV transition on automotive sector MSMEs in the short term. However, without appropriate support, the transition could deepen precarity among vulnerable enterprises and their workers in the automotive supply chain, and exacerbate regional inequalities in traditional automotive clusters—issues that are central to the concept of a just transition (ILO 2022).

**Second, the lack of domestic EV component manufacturing capabilities among MSMEs would result in continued reliance on imports.** The current uptake of EVs in India has been accompanied by an increase in imports (Mehra and Malik 2025). This heavy import reliance not only makes supply chains vulnerable to geopolitical tensions and price volatility (Dash 2023) but also undermines India's ability to control the pace and sustainability of its EV transition.

In this context, it is clear that the objectives of building economic competitiveness and supply-chain resilience in the automotive sector and achieving an equitable EV transition are complementary in nature. Strengthening MSMEs, which constitute the bulk of India's automotive supply chain, is

6

WRI INDIA

Driving a just electric vehicle transition in India: Supply-chain practices for large automotive manufacturing enterprises

central to attaining these objectives. Although governments and industry associations play an important role in strengthening MSMEs through policy frameworks, financial incentives, and skill development programs, large automotive enterprises are uniquely positioned to unlock MSMEs' potential in the projected transition. With their technological expertise, market access, and financial resources, OEMs and large Tier-1 ACMs can help bridge the capability gaps facing MSME suppliers while simultaneously strengthening India's position as a global automotive producer.

More importantly, a “partner” approach, in which large enterprises adopt practices that support their suppliers’ transitions, especially specific types of MSME suppliers, can generate mutual value for large enterprises and MSMEs because they are part of the same supply chain and share certain benefits and risks (Said et al. 2025). Therefore, large enterprises that adopt this approach with their MSME suppliers can maximize their own business benefits while reducing overall transition risks. However, the business case for a partner approach in this context is currently not well understood.

This working paper focuses on establishing this business case for large enterprises to take a partner approach with their MSME suppliers in supporting their diversification to EV component manufacturing. It explores the specific challenges faced by MSMEs, highlighting examples of current practices featuring the partner approach adopted by large enterprises and MSMEs in navigating the projected EV transition.

This paper aims to answer the following research questions (RQ2):

What is the business case for automotive OEMs and large Tier-1 ACMs to support a just EV transition for their automotive supply chain, especially MSMEs, in India? (RQ1)

What are the challenges that MSMEs face due to the projected EV transition? (RQ2)
What examples, Indian or global, could guide a partner approach between large enterprises and MSMEs to manage the projected transition to EVs in India? (RQ3)

The rest of the paper is organized as follows: the following section sets the context, and the next two sections describe the methodology employed and the research findings, respectively. The concluding section offers recommendations that large enterprises can use to help their MSME suppliers overcome transition challenges.

### Context

This section discusses the importance of building domestic EV manufacturing capabilities, examines supply-chain interdependencies in the Indian automotive industry, and identifies the gaps in the existing literature that this paper aims to address.

### The macro-economic imperative of building domestic capabilities for EV manufacturing

The conventional ICEV powertrain primarily consists of an engine, transmission, and driveshaft. In contrast, a battery electric vehicle (BEV) powertrain has a different set of component systems such as battery, motor, and a host of other electronic components including the control unit, battery management system, and thermal management system (Figure 1). The ICEV industry has been able to achieve component localization levels of 85–90 percent through consistent efforts over the last few decades (Khurana et al. 2025).

Figure 1 | Key differences between ICEV and BEV powertrains

![img-1.jpeg](img-1.jpeg)

Note: BEV = battery electric vehicle. ICEV = internal combustion engine vehicle.

Source: APRC n.d.

WORKING PAPER | May 2026

7

However, without timely measures, India's projected EV transition could lead to significant import dependence, especially for high-value technological components (Dhairiyasamy and Gabiriel 2025; YES BANK and ACMA 2021).

Estimates indicate a potential to replace around \$18 billion worth of EV imports with local components, representing about 80 percent of the anticipated market size of \$22 billion for new EVs and their components by 2030 (BCG et al. 2022). However, the current concentration of supply sources exposes the domestic manufacturing ecosystem, especially the EV battery value chain, to geopolitical risks such as currency fluctuations and tariff and non-tariff barriers.

Strengthening the existing local automotive MSME ecosystem for EV component manufacturing is one of the effective ways to reduce import dependence. The country's extensive MSME network has traditionally demonstrated adaptability and innovation capacity across various automotive applications due to its operational flexibility, cost competitiveness, and deep understanding of local market dynamics (Madgavkary et al. 2024). With appropriate support, MSMEs can build capabilities in EV technologies, thereby driving localization and creating mutual value for them and large enterprises.

Table 1 | Structure and composition of the Indian automotive value chain

|  TYPE OF ENTERPRISE | SIZE BASED ON GOI'S TURNOVER CLASSIFICATION | CORE BUSINESS | CUSTOMERS | RELATIONSHIP WITH THE CUSTOMERS  |
| --- | --- | --- | --- | --- |
|  OEMs (Lead enterprises) | Primarily large-sizedSome medium-sized or small-sized (comprising start-ups) | Carry out vehicle assembly using final component assemblies; sometimes manufacture key powertrain components as well | Consumers who buy finished vehicles directly or through dealershipsVehicle manufacturers who purchase components from OEMs to assemble into new vehicles | Formal and generally long-term relationship for vehicle usage, service, repair, disposal and end of life  |
|  Tier-1 enterprises | Primarily large- and medium-sized, with very few specialized players that are small-sized | Carry out final component assemblies using child parts and small assemblies | OEMs | Formal and generally a mid to long-term relationship for the project duration of about 5-7 years for supply of specific parts strategic for business  |
|  Tier-2 enterprises | Micro-, small-, and medium-sized | Manufacture child parts and carry out small sub-assemblies | Tier-1; sometimes supply to OEMs as well, either through direct sourcing or technology-binding contracts. | Formal and long-term relationship formed, in some cases, for spare parts supply through OEM channels or independent after-market channels  |
|  Tier-3 enterprises | Micro-, small-, and medium-sized | Provide raw materials, child parts or process-based services (such as forging, die-casting, etc.); cater to the domestic replacement market as well | Tier-2; sometimes directly supply to Tier-1 and OEMs | No formal relationships in place, in many cases; rather, an informal, long-term understanding is formed, with manufacturing and supply of parts done based on monthly orders placed  |
|  Job-work units | Micro-, small-, and medium-sized | Specialize in specific processes like machining, foundry/casting, heat treatment, and forging | Tier-1, Tier-2, Tier-3 | No formal relationships in place, in many cases; rather, an informal, long-term understanding is formed, with manufacturing and supply of parts done based on monthly orders placed  |

Note: GoI = Government of India. OEM = original equipment manufacturer.

In the Indian context, enterprises are classified into different sizes based on their annual turnover (PIB 2025a) in INR as follows:

Micro-sized enterprises: Turnover < 100 million

Small-sized enterprises: Turnover ≥ 100 million and < 1 billion

Medium-sized enterprises: Turnover ≥ 1 billion and ≤ 5 billion

Large-sized enterprises: Turnover > 5 billion.

Source: Kerswell and Pratap 2019; PIB 2025a; Riat 2019; Uchikawa 2011.

8

[Non-Text]

WRI INDIA

Driving a just electric vehicle transition in India: Supply-chain practices for large automotive manufacturing enterprises

## Supply-chain interdependencies in the Indian automotive industry

Traditionally, OEMs and large Tier-1 ACMs drove MSME action through work orders and clear-cut manufacturing processes, with MSME suppliers often being their extended arms (Said et al. 2025). The inability of MSME suppliers to make adequate investments in the skills, people, equipment, and processes needed to adapt to industry transitions limits their capacity to fulfill their customer requirements satisfactorily. Table 1 presents the structure and composition of the Indian automotive value chain, highlighting the interdependencies.

The aforementioned interdependencies indicate that in addition to government support, MSMEs need support from their customer OEMs and large Tier-1 ACMs to be able to localize EV component manufacturing in a meaningful manner.

## Just transition pathways for the Indian automotive supply chain

In addition to the economic imperative for localizing EV component manufacturing, the Indian automotive supply chain has about 35,000–45,000 MSMEs currently manufacturing over 2,000 ICEV components that are supplied domestically and abroad. Because these MSMEs are significant employment generators for the Indian automotive sector, it is imperative to enable a just EV transition for them. According to the International Labour Organization (ILO 2022), “Just transition (JT), as a concept, seeks to ensure that the substantial benefits of a green economy transition are shared widely, while also supporting those who stand to lose economically.” Globally, several inter-governmental organizations have published various guidelines for a low-carbon just transition focused on achieving equitable economies for all (ILO 2015; OECD 2023; UNDP 2022; UN Global Compact 2022). At the same time, there is an ongoing discourse on just transition, globally and in India, that focuses on industry-specific low-carbon transitions such as the energy transition or the ICEV-to-EV transition (Agora Verkehrswende 2022; iForest 2024; Saha et al. 2023). Research shows that the EV transition will have positive impacts on net employment; however, regional disparities may arise (Agora Verkehrswende 2022; CLEPA 2021; WRI India 2022). According to India-specific studies (iForest 2024; Sen et al. 2025), powertrain ACMs are expected to be affected.

However, most of the literature on enterprise-level actions focuses on business sustainability practices (Franco and Karamally 2024; Roth 2025; WBA 2023). Although several companies have set up dedicated sustainability teams, they are yet to integrate just transition in business planning. There is some literature on enterprise-level JT strategies, but it

primarily emphasizes supporting workers and communities (ERM Sustainability Institute 2024; Robins et al. 2021; SSE 2024). Specifically, there is very little consideration of supply-chain stakeholders such as MSMEs. Given the massive employment generated by MSMEs, it is essential to support them through technological transitions by implementing localization strategies. However, there is a scarcity of literature addressing whether large Indian automotive enterprises are helping MSME suppliers resolve transition challenges, and if so, how they are providing this assistance.

Although large enterprises in the ICEV sector have employed various supplier engagement models, these may not be adequate for fulfilling the needs of the projected EV transition. Large enterprises face challenges due to the lack of local supply-chain capacities and capabilities for the projected transition. Their MSME suppliers face adaptational challenges due to financial and technological constraints, which prevent them from scaling up capacities or investing in capability-building. Hence, large enterprises can create the right enabling conditions for MSMEs’ projected EV transition, thereby creating mutual value (Madgavkar et al. 2024). However, the business case for this approach is not well understood.

Our paper is aimed at assessing this business case. It also provides a set of practices, using learnings from various sectors and geographies, that large enterprises can refer to and apply when preparing their own supplier engagement strategies as they move toward a low-carbon future.

## Study Design and Methodology

To answer our RQs, we employ a mixed-methods approach, combining primary research (conducted through semi-structured key-informant interviews (KIIs) and focused group discussions (FGDs)) and secondary research.

## Search strategy and selection criteria for secondary research

The secondary research component was primarily used to derive research findings through a sector- and geography-agnostic lens, while ensuring the applicability and feasibility of various case studies to the Indian automotive industry’s EV transition.

We comprehensively reviewed the academic and gray literature, focusing on specific themes relevant to the research from the past 10 years, during which the global energy transition picked up pace significantly. We also reviewed selected seminal work on supply-chain dynamics prior to 2015. To study diverse policy environments (the level of proactiveness of a country’s government and/or industries in driving green initiatives or supplier-centric initiatives) and industrial interests (countries with large automotive

WORKING PAPER | May 2026 | 9

manufacturing and/or assembly industries versus countries that are largely importers), the geographic focus of our review was wide, spanning India, Japan, Europe, China, and the United States. The sectoral coverage primarily focused on the automotive sector, while also considering renewable energy, electronics, and heavy manufacturing.

In terms of literature sources and classification, we reviewed about 8–10 research articles and 15–20 reports from reputable publishers. We studied articles published on government websites and widely circulated national newspapers primarily to understand the changing EV localization dynamics, and new opportunities for India’s manufacturing industry. Given the EV industry’s nascency, these articles helped provide the latest information.

- The first step of the search strategy was to identify the keywords. Four keywords were defined from the RQ2: “electric vehicles”, “automotive manufacturing”, “just transition” and “supply-chain practices”. These were then expanded to larger sets of keywords using multiple synonyms and related words (see Appendix A). Google Scholar was the chosen database. We then conducted a systematic review by examining the titles, abstracts and/or summaries, and keywords of articles and reports of the entire list derived from Google Scholar, applying the following exclusion criteria:
- Reviews older than last 10 years
- Reviews of enterprise initiatives in the areas of corporate social responsibility (CSR) or Environmental, Social, and Governance (ESG) guidelines

Figure 2 | Sample size distribution of automotive enterprises covered across India

![img-2.jpeg](img-2.jpeg)

Note: The size of the circle represents the state-wise sample size of the number of enterprises.

Source: WRI Authors.

DISCLAIMER: This map is for illustrative purpose and does not imply the expression of any opinion on the part of WRI India, concerning the legal status of any country or territory or concerning the delimitation of frontiers or boundaries.

10 | WRI INDIA

Driving a just electric vehicle transition in India: Supply-chain practices for large automotive manufacturing enterprises

■ Reviews centered on demand-side EV interventions
■ Reviews of workforce-focused or mandatory labor-law-compliance-linked initiatives

### Study location, sampling strategy, and distribution for primary research

The primary research aimed to document practices through first-hand interactions with large automotive enterprises. The documented practices were either under consideration or in development to support suppliers, especially MSMEs, during the EV transition. To ensure cross-pollination of information, consultations with MSMEs were conducted. Research papers exploring similar themes (Dash 2023; Khurana et al. 2025; Sen et al. 2025) use this approach as well.

To capture a representative sample of perspectives, this working paper adopts a pan-India approach covering India's major automotive clusters. The Indian automotive industry is spread across four primary clusters: Delhi–Gurgaon–Faridabad in the North, Mumbai–Pune–Nashik–Aurangabad in the West, Chennai–Bengaluru–Hosur in the South, and Jamshedpur in the East (Sen et al. 2025). Because more than 95 percent \( ^{4} \) of the enterprises are concentrated in northern, southern, and western clusters, the KIIs and FGD covered these regions. The respondent enterprises were located in four states (Figure 2): Haryana (Cluster 1: North), Maharashtra (Cluster 2: West), and Karnataka–Tamil Nadu (Cluster 3: South). Collectively, these regions account for over 3,900 automotive enterprises, representing a substantial portion of the national total, which exceeds 5,000. \( ^{4} \)

Table 2 | Characteristics used for sample development

|  RESEARCH QUESTIONS | CHARACTERISTICS  |   |   |
| --- | --- | --- | --- |
|   |  ENTERPRISES' SIZE | ENTERPRISES' MARKET SHARE | ENTERPRISES' PRODUCT PORTFOLIO  |
|  RQ1: What is the case for OEMs and large Tier-1 ACMs to support a just EV transition for the automotive value chain, especially MSMEs, in India? | The sample includes large- and medium-sized OEMs (n=11) and large Tier-1 ACMs (n=8), because they typically have access to resources, expertise, and knowledge, given their size. The sample also includes a few small and micro-sized enterprises that are part of larger groups or conglomerates and hence have access to varied resources for a seamless transition. | The sampling design ensures adequate representation from OEMs with a market share of at least 40% across key EV segments in India, i.e., 2Ws, 3Ws, 4Ws, and buses. This sampling design ensures that perspectives are captured from enterprises that tend to influence the market dynamics significantly through their sales dominance. | The sample includes legacy ICEV enterprises that have already diversified into EVs and/or their component manufacturing as well as born-EV companies that manufacture only EVs and/or EV components. This sampling design ensures a comprehensive assessment of perspectives.  |
|  RQ2: What examples, Indian or global, could guide a "partner" approach between large enterprises and MSMEs to manage India's projected EV transition?  |   |   |   |
|  RQ3: What are the challenges that MSMEs face in the projected EV transition? | The sample includes automotive MSMEs as well as those from other sectors (n=53) across different tiers of the supply chain. | N/A | The sample includes traditional ICEV MSMEs that have diversified into EV components and born-EV enterprises from the automotive and non-automotive sectors. This sampling design ensures a holistic assessment of the transitioning automotive industry in India, because the projected transition is expected to pose different challenges for ICEV and EV component manufacturing enterprises as well as those from other sectors venturing into EV manufacturing.  |

Note: ACM = automotive component manufacturer. EV = electric vehicle. MSME = micro, small, and medium enterprise. N/A = not applicable.

OEM = original equipment manufacturer. RQ = research question.

In the Indian context, enterprises are classified into different sizes based on their annual turnover (PIB 2025a) in INR as follows:

Micro-sized enterprises: Turnover < 100 million

Small-sized enterprises: Turnover ≥ 100 million and < 1 billion

Medium-sized enterprises: Turnover ≥ 1 billion and ≤ 5 billion

Large-sized enterprises: Turnover > 5 billion.

Source: WRI India authors.

WORKING PAPER

May 2026

11

Table 3 | Sample distribution by enterprise segment and size

|  CATEGORY OF RESPONDENT ENTERPRISE | NO. OF RESPONDENT ENTERPRISES | ENTERPRISE SIZE | % OF TOTAL SAMPLE  |
| --- | --- | --- | --- |
|  OEMs  |   |   |   |
|  ICEV and EV | 6 | Large enterprises | 8%  |
|  BORN-EV | 6 | 2 large enterprises3 medium enterprises1 small enterprise | 8%  |
|  ACMs  |   |   |   |
|  TIER 1 | 29 | 8 large enterprises21 MSMEs | 40%  |
|  TIER 2 | 20 | MSMEs | 27%  |
|  TIER 3 | 12 | MSMEs | 16%  |
|  TOTAL | 73 |  | 100%  |

Notes: ACM = automotive component manufacturer. EV = electric vehicle. ICEV = internal combustion engine vehicle. MSME = micro, small, and medium enterprise. OEM = original equipment manufacturer.

In the Indian context, enterprises are classified into different sizes based on their annual turnover (PIB 2025) in INR as follows:

Micro-sized enterprises: Turnover < 100 million

Small-sized enterprises: Turnover ≥ 100 million and < 1 billion

Medium-sized enterprises: Turnover ≥ 1 billion and ≤ 5 billion

Large-sized enterprises: Turnover > 5 billion.

Source: WRI India authors.

Table 4 | Sample distribution by enterprise size

|  SIZE OF RESPONDENT ENTERPRISE | NO. OF RESPONDENT ENTERPRISES | % OF TOTAL SAMPLE  |
| --- | --- | --- |
|  Large | 16 | 22%  |
|  Medium | 18 | 25%  |
|  Small | 20 | 27%  |
|  Micro | 19 | 26%  |
|  TOTAL | 73 | 100%  |

Note: In the Indian context, enterprises are classified into different sizes based on their annual turnover (PIB 2025) in INR as follows:

Micro-sized enterprises: Turnover < 100 million

Small-sized enterprises: Turnover ≥ 100 million and < 1 billion

Medium-sized enterprises: Turnover ≥ 1 billion and ≤ 5 billion

Large-sized enterprises: Turnover > 5 billion.

Source: WRI India authors.

A purposive sampling strategy was used to identify respondents for the primary research, which relies on researchers' judgment in choosing participants based on certain characteristics (Etikan et al. 2016). Specifically, we used a maximum variation sampling strategy (Suri 2011) to ensure sample diversity in terms of geographic scope, market share, size of operations, and vehicle or component categories. We also employed snowball

sampling through industry connections to recruit respondents when it was difficult to establish direct contact. The sample was developed based on the characteristics shown in Table 2.

Tables 3 to 5 and Figure 3 represent the sample distribution. All these tables and the figure refer to the same sample (n=73) but classify them in different ways based on the study's use case: by enterprise segment, size, product portfolio, and market share.

12

[NO TEXT]

WRI INDIA

Driving a just electric vehicle transition in India: Supply-chain practices for large automotive manufacturing enterprises

Table 5 | Sample distribution by enterprise product portfolio

|  ENTERPRISE CATEGORY BY PRODUCT PORTFOLIO | NO. OF RESPONDENT ENTERPRISES | % OUT OF TOTAL SAMPLE  |
| --- | --- | --- |
|  ICEV/EV 2W OEM | 4 | 5%  |
|  ICEV/EV 3W OEM | 4 | 5%  |
|  ICEV/EV 4W OEM | 1 | 1%  |
|  ICEV/EV BUS OEM | 3 | 4%  |
|  ICEV - Powertrain and Non-Powertrain | 22 | 30%  |
|  ICEV and EV - Powertrain and Non-Powertrain | 27 | 37%  |
|  EV - Powertrain and Non-Powertrain | 6 | 8%  |
|  ICEV/EV Electricals and Electronics | 6 | 8%  |
|  **TOTAL** | **73** | **100%**  |

Note: EV = electric vehicle. ICEV = internal combustion engine vehicle. OEM = original equipment manufacturer.

Source: WRI India authors.

Figure 3 | Sample distribution based on market share of OEMs

![img-3.jpeg](img-3.jpeg)

Note: E-2W = electric two-wheeler. E-3W = electric three-wheeler. E-4W = electric four-wheeler. OEM = original equipment manufacturer.

Source: WRI India authors.

## Data Collection and Analysis

For primary research, data was collected through KIIs and FGDs with 73 enterprise respondents (for the enterprise categories, see Tables 3–5) during March–August 2025, all of whom are C-suite executives, proprietors, or senior staff members. Table 6 highlights the thematic focus of the research. These qualitative data were analyzed using thematic

coding (Saldana 2015) to identify common patterns. The responses pertaining to the identified research themes were compared to derive trends and inferences. Details on enterprise segment, size, product portfolio, and market share were used to develop enterprises' category-wise narratives.

WORKING PAPER

May 2026

13

### Limitations

Because the study uses a non-probabilistic purposive sampling strategy and is based on a limited set of KIIs and FGDs conducted in specific geographical clusters, the findings cannot be generalized. Further, because we received responses from only 67 percent of the respondents we reached out to (n = 120), participation bias may have impacted the findings. Some large enterprises were unable to participate due to multiple internal protocols for data sharing. Finally, while the projected EV transition may also have a wide range of impacts on the workforce, including increased precarity of automotive sector jobs, it is beyond the scope of this paper to cover this topic due to its enterprise-level focus.

### Research findings

#### Business case for large Indian automotive enterprises to support a just EV transition for their MSME suppliers

The benefits that accrue to a large enterprise's business when it effectively leverages supply-chain interdependencies have been reviewed extensively across different sectors globally (Brandes et al 2013; Aoki and Lennerfors 2013; ILO 2024; Madgavkar et al. 2024; McKinsey 2020, 2021; UN Global Compact 2023). A global, sector-wide survey of more than 100 large enterprises found that those enterprises that regularly collaborated with their suppliers demonstrated higher growth, lower operating costs, and greater profitability than their industry peers (ILO 2024; McKinsey 2020, 2021; UN Global Compact 2023).

Table 6 | Thematic focus of the research

|  RESEARCH QUESTION | FOCUS AREAS  |
| --- | --- |
|  RQ1: What is the business case for OEMs and large Tier-I ACMs to support a just EV transition for the automotive video chain, especially MSMEs in India? | Perceptions of large enterprises regarding whether they have a role to play in ensuring a just EV transition for their MSME suppliers in IndiaBusiness benefits from effectively leveraging supply-chain interdependencies  |
|  RQ2: What are the challenges that MSMEs face in the projected EV transition? | Challenges encountered by Indian MSMEs in diversifying into EV manufacturingSupport expected from customers  |
|  RQ3: What examples, Indian or global, could guide a “partner” approach between large enterprises and MSMEs to manage India’s projected EV transition? | Measures being considered to support suppliers through the projected EV transitionApplying learnings from other transitioning sectors  |

Note: ACM = automotive component manufacturer. EV = electric vehicle. MSME = micro, small, and medium enterprise. OEM = original equipment manufacturer.

RQ = research question.

Source: WRI India authors.

Figure 4 | Reasons for large enterprises' dependency on suppliers

![img-4.jpeg](img-4.jpeg)

Source: Brandes et al. 2013.

Figure 5 | Reasons for suppliers' dependency on large enterprises

![img-5.jpeg](img-5.jpeg)

Source: Brandes et al. 2013.

14

[Non-Text]

WRI INDIA

Driving a just electric vehicle transition in India: Supply-chain practices for large automotive manufacturing enterprises

In the global automotive sector, research demonstrates that automakers that secured wins in the 21st century are those that successfully organized long-term collaborative partnerships with their lower-tiered suppliers and outsourced a large part of their technical development to them. (Brandes et al. 2013; McKinsey 2021). During technological transitions and/or economy- or industry-wide disruptions, leveraging such interdependencies assumes even greater importance. Figures 4 and 5 depict the reasons underlying the existing supply-chain interdependencies in the Indian automotive industry.

In the ICEV sector, large enterprises employ supplier engagement models that require suppliers to produce components based on detailed engineering designs and specifications that are provided to them. However, globalization is leading to increased interdependence and integration among markets of different countries while India is also slowly

losing cost competitiveness to other countries. Continuing with conventional methods of supplier engagement is thus likely to subject India's EV sector to continued geopolitical risks and slower growth rates. An example of this risk is the recent crisis involving rare earth magnets used in EV motors whose exports were restricted by foreign suppliers; these magnets were 100 percent imported (Charan 2025). To prevent such crises, large enterprises can enable MSME participation in the projected EV transition, thereby creating mutual value (Madgavkar et al. 2024). However, the business case supporting the adoption of the partner approach by large enterprises is not well understood.

Drawing from the approach elaborated in Said et al. (2025), where the authors differentiate between goals designed to push or pull suppliers to meet a large enterprise's interests and those designed to create mutual value, we attempt to understand the supply-chain dynamics in the context of the Indian automotive industry's EV transition (Figure 6).

Figure 6 | Understanding supply-chain dynamics in India's EV transition

Push: Customers explicitly ask or require suppliers to make changes to their processes to help the customers manufacture a specific EV part.

Pull: Customers establish a procurement condition that suppliers must meet to be selected for supply of EV parts.

Partner: Customers adopt practices that support specific types of suppliers or suppliers' EV transition in their enterprise's supply chain.

Note: EV = Electric vehicle.

Source: Adapted from Said et al. (2025) by WRI India authors.

Figure 7 | Perception of large Indian automotive enterprises on supporting a just EV transition for their MSME suppliers (n=16)

![img-6.jpeg](img-6.jpeg)

Note: EV = electric vehicle. MSME = micro, small, and medium enterprise.
Source: WRI India authors.

#### 13%

Using "partner" approach for current EV manufacturing requirements and aim to sustain it over mid to long-term.

#### 13%

Using "partner" approach for current EV manufacturing requirements but viewing it as temporary or short-term.

#### 25%

Using a 'push' or 'pull' approach for EV manufacturing requirements, and perceive a "partner" approach to not be very necessary.

#### 50%

Using a 'push' or 'pull' approach for EV manufacturing requirements, but the perception is that a "partner" approach will yield business benefits.

WORKING PAPER

May 2026

15

**Figure 8 | Perception of large Indian automotive enterprises on supporting a just EV transition for their MSME suppliers – Classification by product portfolio (n=16)**

![img-7.jpeg](img-7.jpeg)

■ Using “Partner” approach for current EV manufacturing requirements and aim to sustain it over mid-to long-term.

■ Using “partner” approach for current EV manufacturing requirements but viewing it as temporary or short-term.

■ Using a ‘push’ or ‘pull’ approach for EV manufacturing requirements, and perceive a “partner” approach to not be very necessary.

■ Using a ‘push’ or ‘pull’ approach for EV manufacturing requirements, but the perception is that a “partner” approach will yield business benefits.

*Note:* ACM = automotive component manufacturer. EV = electric vehicle. ICEV = internal combustion engine vehicle. OEM = original equipment manufacturer.

Although the sample size of large enterprises covered is small (16), their market share highlights their sales dominance (see Figure 3). Hence, despite the smaller sample size, their views hold weight because any measure they undertake is likely to influence the market significantly.

*Source:* WRI India authors.

Our interviews show that 4 of the 16 respondent large enterprises were already using a partner approach with their MSME suppliers for their EV component manufacturing requirements, though 2 of them were using it as a short-term measure (for detailed examples, see the section titled “Examples of a partner approach between large enterprises and MSMEs to manage India’s projected EV transition”). Although eight interviewed large-enterprise representatives shared that their enterprises were still employing a push or pull approach, they believed a partner approach would help them reap business benefits (Figure 7).

In terms of enterprise classification by product portfolio, while a majority of the legacy OEMs had not started using a partner approach for the projected transition, they did see a business case emerging, and a few of the legacy OEMs as well as EV-born OEMs were already observed to be using it, albeit as a short-term measure to potentially capitalize on the first-mover advantage in a nascent technology. ICEV and EV powertrain ACMs were almost equally divided in their thinking: some had already begun using the partner approach and aimed to continue to do so, a few did not use the approach but saw a business case for it, and the perceptions of others varied depending on their product portfolio (Figure 8).

The push and pull approach works out well with foreign suppliers and large local Tier-1 ACMs, which typically

have the tools, knowledge, and resources to support customer requirements. However, it automatically eliminates the majority of local MSME suppliers, which either cannot make changes to their processes and infrastructure with their limited capacity or cannot meet the required global procurement conditions. To encourage the partner approach in India’s projected EV transition, there is a need to understand the underlying business case for customer OEMs and large Tier-1 ACMs. Five parameters underpin this business case, which are discussed below.

### Long-run cost efficiencies

Our interviews and studies confirm that lower costs and shorter lead times are the primary reason for outsourcing the supply of EV powertrain components to foreign suppliers (Brandes et al. 2013; Goel et al. 2024; NITI Aayog 2025a). Higher local component costs are mainly attributed to the lack of scale in the production of EV components in India (BCG et al. 2022; The Secretariat 2024). Achieving economies of scale will entail significant investments in infrastructure upgrades, technological innovation, and technical capacity-building of local MSME suppliers (Dash 2023; PwC 2022; Sen et al. 2025; Govardan 2025; Bansal et al. 2024).

Research indicates that one of the key barriers to scaling up capacities is the lack of standardization across MSME

16 | WRI INDIA

Driving a just electric vehicle transition in India: Supply-chain practices for large automotive manufacturing enterprises

suppliers for child parts manufacturing of key EV powertrain components, which hinders the commercial viability of the product (PwC 2022). This leads to inconsistencies in the product quality across different suppliers, preventing smooth infrastructure upgrades and technical capacity-building (ACMA 2018). According to an interviewed legacy 4W OEM representative, automotive MSMEs and emerging start-ups perform well up to the proof-of-concept level. However, the lack of a clear understanding of compliance standards prevents them from scaling up. This points to the need for large enterprises’ intervention to provide guide drawings and technical specification documents for EV child parts manufacturing, which can help scale up capacities over time, thus delivering cost efficiencies. These documents could ensure consistency in product quality through clearly defined quality certification processes and testing protocols aligned with automotive standards and lay out material specification guidelines.

### Greater control over quality, cost, delivery, and service

Interviews with Tier-1 powertrain ACM representatives highlighted that local sourcing could give them flexibility over delivery schedules and service by reducing the procurement lead time of EV components (the current cycle is about 40–45 days), facilitating smaller inventories and simplifying logistics planning. It was also shared that imported EV components require 100 percent advance payment with no credit facility. Here, local sourcing can help eliminate logistics-related costs (including inventory costs and import duties) while providing credit facility (Dash 2023; McKinsey 2021). Further, traceability of imported components is not guaranteed, thus compromising component reliability and durability. An interviewed legacy 4W OEM representative underscored the importance of local sourcing in helping companies better manage the quality of production operations. This is achieved through seamless data integration of production process parameters, test results, and transport and storage conditions for component parts throughout the supply chain (McKinsey 2021).

### Spurring innovation and enhancing R&D capacities

An interviewed legacy bus OEM representative highlighted that they shared their future visions with their suppliers and collaboratively identified and addressed problems by deploying joint teams, emphasizing that EV innovations require a cohesive ecosystem. Another interviewed legacy 4W OEM representative stated that its large Tier-1 ACM supplier had transferred technical know-how and technology to its MSME supplier. The MSME operated in a component segment where

it lacked the capacity to invest in R&D. Their R&D capacity enhancement was driven by the partnership (McKinsey 2020).

### Sustaining export competitiveness

Our interviews highlighted that the majority of industry representatives, including MSMEs, have traditionally been automotive product exporters. This is in line with the secondary literature, which indicates that about 25 percent of the annually produced automotive components are exported to Europe, North America, and Asia (PIB 2025c). Among these, major economies such as Europe and some states in the United States are setting targets to reduce ICEV sales by 2035. Given the shift predicted in global automobile markets, India’s automotive industry needs to gear up for EV manufacturing.

Additionally, global enterprises in Europe and the United States are keen on diversifying their supply chain across sectors, including EVs (Govardan 2025). India is one of the front-line contenders as global enterprises seek to de-risk their supply chains. However, India needs to evaluate the parameters that have led to success in other countries: reliability, low cost, good quality, and timely delivery (Kumar 2022). Local enterprises will need to invest in sufficient production capacity to earn the trust of foreign customers regarding their ability to deliver quality products in large volumes. This is essential to ensure economic viability and enhance credibility in the global market. Thus, a partner approach (ACMA 2018) will be required to help India maintain the momentum in export competitiveness.

### Leveraging the GOI’s EV localization mandates

The GoI’s EV localization mandates demonstrate national efforts to incentivize domestic EV production. India enjoys significant national competitive advantages (a huge customer base, low labor costs, a strong network of supporting industries) in the automotive sector, unlike countries such as Indonesia, Australia, and Malaysia, which have failed to establish viable industries in this sector (Anilan and Vij 2024). Nearly half the large-enterprise representatives interviewed highlighted that if they could source the majority of EV components locally, they would be able to leverage the benefits of localization mandates, which currently benefit only a few select players.

In conclusion, our interviews showed that using a partner approach in the projected EV transition can prevent the reinforcement of challenges that can arise between large enterprises and MSMEs due to a lack of this approach (Figure 9).

WORKING PAPER | May 2026 | 17

Figure 9 | Reinforcement of challenges across the value chain in the absence of a “partner” approach for the projected EV transition

![img-8.jpeg](img-8.jpeg)

Note: ACM = automotive component manufacturer. EV = electric vehicle. MSME = micro, small, and medium enterprise.

Source: WRI India authors.

Table 7 | Sample distribution of MSMEs by tier and product portfolio

|  CATEGORIES BY TIERS-MSMEs | NO. OF MSMEs | % OF OVERALL SAMPLE  |
| --- | --- | --- |
|  Tier - 1 | 21 | 29%  |
|  Tier - 2 | 20 | 27%  |
|  Tier - 3 | 12 | 16%  |
|  Sample size (with only MSMEs) | 53 | 73%  |
|  Overall sample total | 73 | 100%  |
|  CATEGORIES BY PRODUCT PORTFOLIO - MSMES | NO. OF MSMEs | % OF OVERALL SAMPLE  |
|  EV Powertrain & Non-Powertrain | 6 | 8%  |
|  ICEV and EV Powertrain & Non-Powertrain | 41 | 56%  |
|  ICEV/EV Electricals and Electronics | 6 | 8%  |
|  Sample size (with only MSMEs) | 53 | 73%  |
|  Overall sample total | 73 | 100%  |

Note: ACM = automotive component manufacturer. EV = electric vehicle. ICEV = internal combustion engine vehicle. MSME = micro, small, and medium enterprise.

Source: WRI India authors.

### Challenges faced by Indian automotive MSMEs due to the projected EV transition

Large enterprises and MSMEs are interdependent, and the latter form a critical foundation for local job creation and innovation (Khurana et al. 2025). As the automotive industry transitions to EV production, fewer parts will be needed to make the same number of vehicles. The transition will also require different production capabilities. Although the EV supply chain holds business potential, our interviews with

53 MSME representatives highlighted a set of recurring challenges that not only impede their transition preparedness but also hinder the growth of large enterprises, which could benefit from collaboration with MSMEs (Table 7).

#### Financial constraints and lack of transition capital

MSMEs face significant financial pressures and competing priorities, which are further exacerbated by the high cost of entering the EV market. Consequently, access to capital emerges as a major hurdle (Dash 2023). Our interviews

18

[Non-Text]

WRI INDIA

Driving a just electric vehicle transition in India: Supply-chain practices for large automotive manufacturing enterprises

highlighted that high capital expenditure was a major bottleneck in adapting manufacturing lines and acquiring new technologies or land. The issue is compounded by ongoing struggles with working capital management. Allocating resources to EV production, which is still in its nascent stage, directly competes with the demands of their expanding ICEV business, owing to financial constraints.

An EV-born start-up owner highlighted a challenge the company faced in securing a loan to develop an indigenous technology. A major requirement of banks is that the applicant’s business should be profitable for three consecutive years. Although the start-up had sufficient revenue, the investments it had already made in developing the technology up to that point were categorized as an expense rather than an asset, making it challenging to develop local technologies without the support of large enterprises. Product development also entailed other prohibitive costs, with private testing labs charging around INR 200,000 per component in some cases. This limits MSMEs’ ability to certify and validate EV components, because they lack shared infrastructure that could lower testing costs. MSMEs that cater to domestic and export markets bear the additional costs of obtaining multiple certifications for all the markets they operate in. The EV sector is dynamic, and rapidly changing products — even minor changes — add to costs, such as the costs of tooling, software, and worker training. These costs are often absorbed by MSMEs owing to their limited bargaining power; otherwise, they risk losing orders to larger enterprises. Along with these myriad financial challenges, the lack of clarity regarding revenue cycles and payback periods for these investments inhibits MSMEs from assuming such financial risks, hindering their participation.

### Lack of technical know-how, technology, R&D, and skills

The ICEV sector has adopted a top-down manufacturing approach in which MSMEs are given detailed engineering drawings by large enterprises to build products. Unlike the ICEV sector, the EV ecosystem is taking a co-product-development approach, because technologies are emerging and dynamic. However, MSMEs are known to typically prioritize tangible assets more than R&D (NITI Aayog 2025b).

EV manufacturing demands higher precision, automation, and safety standards than ICEV manufacturing. About 31 percent of ICEV jobs are likely to be significantly affected by the transition, because EV manufacturing requires different skillsets, and the MSME workforce will require skilling to deliver quality products on time (iForest 2024; Saha et al. 2025). MSMEs largely rely on in-house on-the-job training of workers, often resulting in inadequately skilled workers. One of the challenges facing resource-constrained MSMEs—as highlighted by a micro-unit—is that they are bogged down by tight and often

unrealistic deadlines from OEMs, leaving no time for adequate quality control or structured training. Additionally, due to high worker turnover, MSMEs hesitate to invest in training workers because they may leave after getting trained, leading to a loss on their training investment. Although large enterprises have initiated some skill development initiatives, coverage remains fragmented and inaccessible to MSMEs.

### Trust deficit in domestic MSME capabilities

Interviews with large Tier-1 and MSME ACM representatives highlighted a lack of trust in Indian MSMEs and a preference for either imports or large brands, even when comparable products and technology are available locally. This trend limits the growth and development of the local ecosystem. These MSME owners mentioned that opportunities for locally developed technologies are hardly available owing to barriers in reaching large enterprises. A motor-manufacturing MSME owner highlighted how its technology was not considered because it had not previously worked with the automotive industry. Trust deficit is a significant hurdle for MSMEs not only while trying to secure meetings with large enterprises but even after they win contracts. An interviewed MSME representative started working with a large Tier-1 ACM, but a change in management at the ACM triggered a decision to work only with large enterprises, ending their collaboration. The concerned MSME had to absorb the developmental costs already incurred by it. The absence of trust, which could be overcome with the right efforts, stems from a mix of perceived risk, capability gaps, and ecosystem-level inefficiencies.

### Competition from EV start-ups and imports

The emergence of well-funded EV start-ups and the continued reliance on imports creates intense competition, leaving MSMEs struggling to match the cost, scale, and speed of these players. The interviewed MSME representatives observed that EV start-ups with deep pockets can not only invest in new technology and infrastructure and hire good talent, but they can do so for longer gestation periods than themselves, giving these players a relative advantage. Additionally, foreign suppliers benefit from technology investments and economies of scale, making it difficult for Indian MSMEs to compete without strategic support (Dash 2023). Interviewed MSME representatives also highlighted the lack of robust verification mechanisms to accurately identify cheap imports which are falsely labelled as locally made. This makes it particularly difficult for domestic MSMEs to compete fairly in the market.

WORKING PAPER | May 2026 | 19

## Lack of systems for scalability

Individual MSMEs are often a minor participant in a large enterprise's massive ecosystem, so they mostly respond to the requirements of the latter's systems and processes but seldom have their own. EV manufacturing is fast-paced and requires precision, and deviations from these standards lead to product rejections. MSMEs not only need the capacity to manufacture the required number of products but also the capability to fulfill orders as planned. Systems and processes play a key role in enabling efficient delivery of products through better working capital management and resource planning. They enable accurate production estimations, timely delivery, and conformance with quality assurance. An example of the above given by an interviewed powertrain ACM representative was that if an electric motor MSME fails to meet design requirements by even a few microns, the deviation has implications for the air gap between the EV stator and rotor, affecting the motor's performance and efficiency.

## Missing roadmaps and assured market and linkages

A unanimous challenge expressed by the interviewed MSME representatives was the absence of a clear roadmap from large enterprises of their transition pathways and product requirements. This information serves as a critical input for MSMEs when they make decisions regarding investment and production, and its absence hinders their ability to proactively build EV capacities. A non-powertrain MSME ACM representative emphasized the importance of buyer–seller meets to identify potential customers and their specific needs. There are very few opportunities for structured dialogue platforms that facilitate the exchange of roadmaps and alignment in planning between large enterprises and MSMEs.

## Examples of a "partner" approach between large enterprise-MSMEs to manage India's projected EV transition

This section documents the concrete, actionable practices that some large enterprises from the automotive sector and other sectors are implementing to directly address MSMEs' challenges.

## Strategic supplier development and capability-building programs

A direct approach to strengthening the supply chain is through intentional, structured programs designed to improve supplier capabilities (Figure 10).

### TECHNICAL TRAINING AND SKILL DEVELOPMENT PROGRAMS

Hyundai, a leading global 4W OEM, exemplifies proactive supplier transition support for business diversification through its global partnership center and its collaborative program with the Korea Automotive Technology Institute and Foundation of Korea Automotive Parts Industry Promotion, thus helping ICEV component suppliers proactively respond to future vehicle market changes (Table 8) (Hyundai 2024).

A large respondent Tier-1 powertrain ACM exemplifies this through its "Gurukul" skill development program, which goes beyond safety training to build the technical capabilities suppliers need to participate in EV manufacturing. Through structured modules on EV systems, component assembly, and quality assurance, the program helps the supplier workforce acquire new competencies and upgrade existing skills for high-voltage environments.

**Table 8 | Summary of key capability-building initiatives by Hyundai to help suppliers adapt to future mobility**

|  **Global Partnership Center** | Support suppliers in enhancing their competencies and competitiveness through training programs for Tier-1 and Tier-2 levels.  |
| --- | --- |
|  **Foundation of Korea Automotive Parts Industry Promotion** | Strengthen automotive part suppliers' overall capabilities in the areas of quality, technology, and management.  |
|  **Technical Training** | Provides technical training to help both metal suppliers and non-metal suppliers to improve their parts' quality and productivity.  |
|  **Management consulting** | Offers management consulting to suppliers, free of charge, through which they share professional experiences and know-how so that suppliers can strengthen their management capabilities in the area of R&D, production, quality, logistics, cost, and management activities.  |

Source: Hyundai 2024.

20 | WRI INDIA

Driving a just electric vehicle transition in India: Supply-chain practices for large automotive manufacturing enterprises

Figure 10 | "Partner" approach between large enterprises and MSMEs to enable strategic supplier development and capability building

![img-9.jpeg](img-9.jpeg)

Note: 2W = two-wheeler. ACM = automotive component manufacturer. EV = electric vehicle. MSME = micro, small, and medium enterprise. OEM = original equipment manufacturer.

Source: WRI India authors.

The accompanying “License to Work” system ensures that workers are certified before they can operate on EV lines, linking skill enhancement with safety assurance. This integrated approach not only safeguards production but also enables a wider range of suppliers to transition by meeting evolving technical and quality benchmarks.

### QUALITY MANAGEMENT AND/OR CERTIFICATION PROGRAMS

Our interviews show that leading enterprises are implementing rigorous quality management systems tailored for EVs. An interviewed EV non-powertrain MSME representative shared that with the support of a customer, the MSME introduced “Shopfloor Automation Processing” to track manufacturing efficiency and standardize manufacturing processes, representing a shift toward data-driven quality management that provides transparency and continuous improvement capabilities.

Large OEMs are establishing dedicated academies and technical centers to train MSME suppliers on EV-specific requirements. The training focuses on precision manufacturing for components such as battery enclosures, motor housings, and power electronics trays. In comparison with ICEV parts, these EV components have different material properties and higher precision. The Tata Motors Supplier Quality & Development team runs extensive programs to help suppliers achieve certifications such as Advanced Product Quality Planning, Production Part Approval Process, and Failure Mode and Effects Analysis.

These quality frameworks are even more critical for EV components, where safety failures in high-voltage systems can have severe consequences, making such certifications non-negotiable (Tata Motors 2023).

An interviewed EV 2W OEM representative shared that the OEM invested directly in building supplier capacity at multiple levels of the supply chain. In one case, a Tier-2 vendor manufacturing casted parts lacked proper machining processes, jigs, and fixtures, relying only on manual work. The OEM deployed its own supply quality expert on-site to train the vendor in establishing systematic processes through optimization methods. By mentoring vendors, the OEM ensured fewer rejections during assembly and also improved the vendor's efficiency and long-term competitiveness.

### Technology transfer and innovation partnerships

Our interviews show that successful EV localization initiatives depend fundamentally on systematic technology transfer programs that not only share technical specifications but also build the underlying engineering expertise and manufacturing know-how.

An interview with a large Tier-1 powertrain ACM representative demonstrated how large enterprises can serve as technology intermediaries, reducing risk and cost for MSMEs while ensuring capability development.

WORKING PAPER

May 2026

21

**Figure 11 | "Partner" approach between large enterprises and MSMEs to enable technology transfer and innovation partnerships**

![img-10.jpeg](img-10.jpeg)

Source: WRI Authors, (HBR 2013).

#### STRATEGIC TECHNOLOGY TRANSFER PROTECTED THROUGH EXCLUSIVITY CONTRACTS

The aforementioned company obtained technology for multi-layer printed circuit boards (PCBs) used in EV motor controllers from abroad. Subsequently, it transferred this technology to one of its MSME suppliers under a confidentiality agreement that mandated technology protection for three years, after which the supplier could use the technology for its other customers. Through this intervention, the company helped its suppliers make multi-layer PCB boards that met global reliability and quality standards. It was shared that building MSMEs' expertise in skill-based work, such as laminations, can enable cost optimization through economies of scale and process efficiency. This approach has the potential to reduce PCB assembly costs to 8–10 percent of the overall bill-of-materials cost versus 18–20 percent in the case of procurement through large electronics ACMs.

#### STRATEGIC, NON-EXCLUSIVE TECHNOLOGY TRANSFER

The same large Tier-1 ACM employed technology transfer using a non-exclusive approach by purchasing expensive high-speed carbide tools from abroad to enable its MSME suppliers to manufacture e-motor lamination pieces at scale. The cost of the foreign tools was more than three times that of the local tools; however, the latter precluded high-volume manufacturing. The ACM also permitted its supplier to use the same tools for other customers, thus fostering positive externalities.

#### EXPOSURE VISITS TO GLOBAL AUTOMOTIVE FACILITIES

Recognizing that the mere sharing of drawings or tools does not help build MSMEs' capabilities, this ACM went beyond equipment provision to develop technological expertise. It facilitated an overseas visit for its supplier for hands-on technological training. This addressed critical knowledge gaps, such as the discipline required for weekly maintenance of high-speed carbide tools, a practice not commonly followed in India but essential to prevent tool breakage and ensure optimal performance.

#### ESTABLISHMENT OF SHARED R&D CENTRES

Large enterprises can also learn from the Japanese Keiretsu method of involving suppliers in technology development (Aoki and Lennerfors 2013). An example is Toyota's establishment of shared R&D centers.

#### STRATEGIC JOINT VENTURES (JVS)

An interviewed Tier-2 MSME ACM representative mentioned that the company, which transitioned into EV powertrain manufacturing to leverage its expertise in motor manufacturing for the non-automotive sector, had adopted a strategic partnership model with a large Tier-1 ACM through a white-labeling arrangement. This arrangement enabled the MSME to secure larger orders and effectively addressed the market entry barriers faced by them. This example demonstrates how intermediate partnership models can serve as stepping stones for MSMEs entering the EV market.

22 | WRI INDIA

Driving a just electric vehicle transition in India: Supply-chain practices for large automotive manufacturing enterprises

An interviewed EV 2W OEM representative shared that the company actively nurtured its supply chain by gradually localizing charger production. It partnered with local suppliers to develop plastic covers, casing, cables, connectors, and later PCB assembly. The company also worked closely with Tier-1 vendors, jointly negotiating with Chinese partners to enable technology transfer and local assembly. This collaboration helped suppliers build capabilities in advanced components (e.g., magnetics and epoxy potting materials).

## CONTRACT R&D ARRANGEMENTS

Our FGDs suggest that large enterprises are increasingly recognizing that R&D capacity shortages can be addressed through contract R&D arrangements with MSME suppliers for specialized skillsets (in areas such as winding for motors and wiring harnesses) and with emerging start-ups that possess specialized expertise in niche EV technologies, thereby democratizing access to innovation opportunities across the supplier ecosystem.

## MOVING FROM BUILD-TO-PRINT (BTP) TO CO-CREATION

Progressive companies are transitioning from BTP models to “co-creation” approaches that leverage suppliers’ engineering expertise and design capabilities in product development. Our interviews indicate that supplier innovation challenges are emerging; for example, a legacy OEM hosted hackathons inviting suppliers to develop solutions for specific components, with winning solutions receiving funding and guaranteed purchase orders. This represents a fundamental shift from passive execution to active contribution, where suppliers bring their technical knowledge and innovative solutions to address complex EV challenges rather than simply following predetermined blueprints.

These supplier development initiatives (Figure 11) have demonstrably broadened the supplier base, with a large powertrain ACM respondent reporting that its traditional ICEV suppliers successfully transitioned to EV component manufacturing; for example, gear box shaft suppliers became motor shaft suppliers, sheet metal suppliers became lamination suppliers, and die-casting suppliers became motor-casing suppliers. The relatively lower volumes and controlled quality requirements during the early EV adoption phases enabled MSMEs to participate more easily than in the mature, stringent ICEV supply chains, effectively democratizing access to the EV ecosystem.

## Financial support and risk mitigation

Our interviews indicate that leading enterprises have developed innovative financial support mechanisms for the projected transition (Figure 12).

## BULK PROCUREMENT OF EV SUB-COMPONENTS

An interviewed Tier-1 powertrain ACM representative shared that the company imported EV components in bulk and distributed them to its suppliers for cost reduction. Their bulk procurement approach leveraged the purchasing power differential between large enterprises and MSMEs: global suppliers considered the long-term trajectory of the large Tier-1 ACM and offered it better pricing than that offered to MSMEs, given their relatively unfavorable financial standing. This cost arbitrage was then passed on to MSME suppliers, effectively reducing their component costs and improving their competitiveness. Sometimes, when required, the large Tier-1 ACM also pitched in for procurement-related discussions, further strengthening the negotiating position.

Figure 12 | “Partner” approach between large enterprises and MSMEs to enable provision of financial support

![img-11.jpeg](img-11.jpeg)

Note: EV = electric vehicle, MSME = micro, small, and medium enterprise. NBFC = non-banking financial company. OEM = original equipment manufacturer. SIDBI = Small Industries Development Bank of India.

Source: Primary and secondary research (SIDBI 2021) by WRI India authors.

WORKING PAPER

May 2026

23

**Figure 13 | "Partner" approach between large enterprises and MSMEs to enable digital integration and supply chain visibility**

![img-12.jpeg](img-12.jpeg)

Note: ACM = automotive component manufacturer. EV = electric vehicle. MSME = micro, small, and medium enterprise. OEM = original equipment manufacturer.
Source: WRI India authors.

#### ASSURED LONG-TERM OFFTAKE AGREEMENTS

Our research indicates that successful financial support requires long-term commitment structures. Recognizing the capital expenditure hurdle, leading players are creating innovative models such as assured offtake agreements that provide long-term purchase commitments spanning 5-7 years, giving suppliers the confidence to invest in new machinery and technology. These agreements de-risk investment for MSMEs while ensuring a reliable supply chain for OEMs.

#### OEM PARTNERSHIPS WITH FINANCIAL INSTITUTIONS

Partnerships with financial institutions represent another emerging trend, where large enterprises partner with banks and non-banking financial companies to create tailored loan products for their suppliers. The Auto OEM – SIDBI Sustainable Finance Scheme provides such a framework, though OEMs can create bilateral versions of this approach (SIDBI 2021).

**Figure 14 | "Partner" approach between large enterprises and MSMEs to enable market access**

![img-13.jpeg](img-13.jpeg)

Note: ACM = automotive component manufacturer. EV = electric vehicle. MSME = micro, small, and medium enterprise. OEM = original equipment manufacturer.
Source: WRI India authors.

24 | WRI INDIA

Driving a just electric vehicle transition in India: Supply-chain practices for large automotive manufacturing enterprises

### Digital integration and supply-chain visibility

Recognizing the importance of end-to-end visibility and sophisticated coordination capabilities, progressive OEMs are implementing digital enablement programs that extend beyond their own operations to empower their entire supplier network (Figure 13).

Our interviews show that some OEMs are deploying integrated cloud-based supplier portals that provide suppliers with access to real-time production schedules and demand

forecasts, as well as electronic payment systems for improved cash-flow predictability. These platforms serve as digital bridges that reduce information asymmetry and minimize supply-chain disruptions.

### Market access enablers

Our interviews reveal innovative approaches that large enterprises use to address market access challenges (Figure 14).

Table 9 | Examples of strategic interventions by large automotive enterprises to resolve their MSME suppliers' EV transition challenges

|  S.NO. | CATEGORIES OF INTERVENTIONS(BY LARGE AUTOMOTIVE ENTERPRISES), WITH EXAMPLES | MSME CHALLENGE THAT THE INTERVENTION ADDRESSES  |
| --- | --- | --- |
|  1. | Strategic supplier development and capability building programs  |   |
|   | Technical training and/or skill development programsQuality management and/or certification programs | Lack of systems for scalabilityLack of technical know-how, technology, R&D and skilling gaps  |
|  2. | Technology transfer and innovation partnerships  |   |
|   | Strategic technology transfer protected through exclusive contractsStrategic, non-exclusive technology transferExposure visits to global automotive facilitiesEstablishment of shared R&D centersStrategic joint ventures (JVs)Contract R&D arrangements for access to MSMEs' specialized skillsets and EV start-ups' niche technologiesMoving from build-to-print (BTP) to co-creation of products through supplier hackathons | Lack of technical know-how, technology, R&D and skilling gapsFinancial constraints and lack of transition capital  |
|  3. | Financial support and risk mitigation  |   |
|   | Bulk procurement of components with cost arbitrage passed to MSMEsAssured long-term offtake agreementsPartnerships with financial institutions creating tailored loan products | Financial constraints and lack of transition capital  |
|  4. | Digital integration and supply chain visibility  |   |
|   | Cloud-based supplier portals for real-time access to production schedules and demand forecasts | Competition from EV start-ups and importsTrust deficit in domestic MSME capabilities  |
|  5. | Market access  |   |
|   | Demand aggregation through Manufacturing-as-a-Service platformsWhite-labeling arrangements with OEMs and large Tier-1 ACMs for EV component manufacturing | Missing roadmaps and lack of assured market and linkagesCompetition from EV start-ups and importsTrust deficit in domestic MSME capabilities  |

Note: ACM = automotive component manufacturer. EV = electric vehicle. MSME = micro, small, and medium enterprise. OEM = original equipment manufacturer. R&D = research and development.

Source: WRI India authors.

WORKING PAPER

May 2026

25

## WHITE-LABELING ARRANGEMENTS

An MSME, supported by their customers, has adopted a dual market access strategy: engaging with start-ups to supply components while building strategic partnerships with large Tier-1 ACMs for securing larger orders and overcoming high market entry barriers by way of white labelling arrangements.

## DEMAND AGGREGATION

Another strategy to prevent market access frictions is the use of demand aggregation platforms that aggregate component manufacturing demand from OEMs using a cloud manufacturing platform and connects them with a network of contract manufacturers, including MSMEs, for common services like precision machining etc. This serves a dual purpose, supporting large enterprises to find capable MSMEs that may not have been easily identifiable, while also making it easier for suppliers to make investment decisions due to order visibility and risk diversification.

## Conclusions and Recommendations

This study highlights that large automotive enterprises have a strong business case for adopting a partner approach with their MSME suppliers to support a just EV transition. Challenges are reinforced across the value chain in the absence of a partner approach between large enterprises and MSMEs for the projected transition (Figure 9). Using this approach, large enterprises can play a vital role in addressing MSMEs' transition challenges through a set of practices (Table 9), thus creating mutual value.

Based on our research insights, we suggest the following recommendations for large Indian automotive enterprises:

- **Facilitate knowledge-sharing and hands-on training:** Large enterprises can undertake measures that facilitate knowledge-sharing with MSME suppliers in EV component manufacturing. They can **provide embedded engineering support** by placing their engineers at supplier facilities for extended periods to help transfer tacit knowledge that may be difficult to document (troubleshooting techniques, process optimization, and quality control practices) and help their suppliers build repeatable processes, adopt advanced quality systems, and progress toward higher capability levels. They can also **create digital knowledge platforms** with technical documentation, design guidelines, and video tutorials, making knowledge accessible to a wider set of suppliers. They can **facilitate visits to global automotive facilities** for their suppliers for hands-on training in EV component manufacturing. Further, they can **enable mechanisms to provide their suppliers visibility into the final product requirements of end users**; currently, MSMEs do not have visibility into the final product.

- **Create guide drawings and technical specification documents for EV child part manufacturing to enable standardization:** Large enterprises can develop detailed parameters with standardized tolerances that MSMEs can follow, establishing quality certification processes and testing protocols aligned with automotive standards, and creating material specification guidelines that ensure consistency in product quality across suppliers. These documents should also align with long-term strategies so that suppliers can invest with confidence, reduce rework cycles, and ensure interoperability.

- **Facilitate access to infrastructure financing for MSMEs through de-risking mechanisms:** Large enterprises should support MSMEs with the financial resources needed for acquisition of machinery and equipment that may either not be available locally or may be available but preclude manufacturing at scale or delivering the required quality. Certain MSMEs may lack the up-front financial resources needed for investment. However, implementing reasonable payback plans and establishing risk-sharing arrangements with large enterprises could facilitate faster technology adoption among MSMEs. Our interviews establish that such practices can not only help scale up production capacities that enable cost reduction but also help suppliers expand their markets by using the same infrastructure for other customers. Other support mechanisms could include bulk procurement of EV components, long-term offtake agreements and OEM partnerships with financial institutions.

- **Facilitate contract R&D in EV component manufacturing:** Contract R&D arrangements need to be established between large enterprises and their MSME suppliers (including EV start-ups) to enhance their collective innovation capabilities while addressing their own R&D capacity shortages. This could be facilitated through joint development agreements that allow both parties to share costs, risks, and intellectual property (IP) rights for specific projects. In these arrangements, large enterprises contribute market knowledge and testing facilities, while MSMEs offer specialized technical skills (in areas such as coil winding for chargers and winding for motors and wiring harnesses), and EV start-ups offer niche innovations.

- **Enable demand aggregation for EV component requirements at the large enterprise level:** Unlike large enterprises, which compete on proprietary technologies, sub-tier suppliers often produce common components such as seals, materials for heat dissipation, or other specialized parts essential for EV powertrains. If a group of large enterprises collectively aggregates demand for specific EV components and engages with MSME suppliers to fulfill this demand, the suppliers will find it easier to take investment decisions due to order visibility and risk diversification.

26 | WRI INDIA

Driving a just electric vehicle transition in India: Supply-chain practices for large automotive manufacturing enterprises

## Appendix A

Table A-1 | Search criteria used for this research

|  KEYWORD | ALTERNATIVE KEYWORD  |   |
| --- | --- | --- |
|   |  SYNONYMS | ABBREVIATIONS  |
|  Electric vehicles | Alternative fuel vehicles, zero emission vehicles, electric cars, electromobility | EV, BEV, ZEV  |
|  Supply-chain practices | Supply network operations, value chain operations, supply-chain management |   |
|  Just transition | Equitable climate transition, fair green shift, inclusive decarbonization, social justice |   |
|  Automotive manufacturing | Automaker, motor vehicle manufacturer, auto assembly, automotive sector |   |

Note: BEV = battery electric vehicle. EV = electric vehicle. ZEV = zero emission vehicle.

Source: WRI India authors.

WORKING PAPER

May 2026

27

## Abbreviations

|  **2W** | two-wheeler | **KII** | key-informant interview  |
| --- | --- | --- | --- |
|  **3W** | three-wheeler | **FGD** | focused-group discussion  |
|  **4W** | four-wheeler | **FY** | financial year  |
|  **ACM** | auto component manufacturer | **ITI** | industrial training institute  |
|  **ACMA** | Automotive Component Manufacturers' Association | **ICEV** | internal combustion engine vehicle  |
|  **ASDC** | Automotive Skills Development Council | **JV** | joint venture  |
|  **ASI** | Annual Survey of Industries | **MHI** | Ministry of Heavy Industries  |
|  **BAU** | business-as-usual | **MoRTH** | Ministry of Road Transport and Highways  |
|  **BEV** | battery electric vehicle | **MSME** | Micro-, small-, and medium-enterprise  |
|  **BTP** | build-to-print | **MHDV** | medium-and-heavy-duty vehicles  |
|  **BMS** | battery management system | **NBFC** | non-banking financial companies  |
|  **CAGR** | compounded annual growth rate | **OEM** | original equipment manufacturer  |
|  **CAPEX** | capital expenditure | **PCB** | printed circuit board  |
|  **CCC21** | construction of cost competitiveness in the 21st century | **PIB** | press information bureau  |
|  **CSR** | corporate social responsibility | **PLI** | production-linked incentive  |
|  **e-DRIVE** | electric drive | **QCDS** | quality-cost-delivery-service  |
|  **ESG** | environmental-social-governance | **R&D** | research and development  |
|  **EV** | electric vehicle | **SIDBI** | Small Industries Development Bank of India  |
|  **FAME** | faster adoption and manufacturing of electric vehicles | **SME** | small and medium enterprise  |
|  **GDP** | gross domestic product | **ZEV** | zero-emission vehicle  |

28 | WRI INDIA

Driving a just electric vehicle transition in India: Supply-chain practices for large automotive manufacturing enterprises

## Glossary

**Battery electric vehicle (BEV):** A BEV is defined as a type of electric vehicle (EV) that exclusively uses energy from a battery to power an electric motor, without relying on other energy sources such as internal combustion engines or hydrogen fuel cells.

**Born-EV:** This refers to new companies being launched or new products being made to specifically cater to EVs.

**Child Parts:** It is a term used for smaller parts that are assembled to create a bigger part of the vehicle.

**Cluster:** A cluster is a group of similar entities (here, automotive industry enterprises) that are co-located and also linked by inter-enterprise relations. The co-location of enterprises in the automotive industry generates benefits, including sharing of sector-specific inputs, skilled labor and knowledge, intra-industry linkages, infrastructure, and opportunities for efficient subcontracting.

**Powertrain:** It is the set of components that generate power to thrust the vehicle into motion.

**Semiskilled workers:** These are workers with skills gained through experience on the job and capable of applying it under the supervision or guidance of a skilled employee. They may also supervise unskilled workers.

**Thermal management:** It refers to the tools and technologies used to maintain a system within its operating temperature range.

**Unskilled workers:** These are workers with no specialized skills and who require experience in operating machinery or equipment.

## Endnotes

1. "Just transition (JT), as a concept, seeks to ensure that the substantial benefits of a green economy transition are shared widely, while also supporting those who stand to lose economically" (ILO 2022).
2. Purposive sampling is a non-probability method in which researchers intentionally select participants with specific traits or experiences relevant to the study's goals, rather than randomly selecting participants.
3. Child part is a term used for smaller parts that are assembled to create a bigger vehicle component. Examples include busbars and battery modules for battery pack assembly, and bearings for electric motors.
4. MarkLines. Database. 2024. https://www.marklines.com/en/automotive-industry-keywords/country/india.

WORKING PAPER

May 2026

29

## References

ACMA (Automotive Component Manufacturers Association of India). 2018. *Study on Xev Market and Opportunities for Xev Component Suppliers*. New Delhi: ACMA. https://www.acma.in/uploads/docmanager/EV%20Study_2018.pdf.

Agora Verkehrswende. 2022. *Powering the Automotive Jobs of the Future*. Berlin: Agora Verkehrswende. https://www.agora-verkehrswende.de/fileadmin/Projekte/2021/BCG-Jobstudie/70_Jobef-fekte_EN.pdf.

Anilan, V., and A. Vij. 2024. "Taking the Wheel: Systematic Review of Reviews of Policies Driving BEV Adoption." *Transportation Research Part D: Transport and Environment* 136: 104424. https://doi.org/10.1016/j.trd.2024.104424.

Aoki, K., and T.T. Lennerfors. 2013. "The New, Improved Keiretsu." *Harvard Business Review*. https://hbr.org/2013/09/the-new-improved-keiretsu.

APRC (Automotive Policy Research Centre). n.d. "From ICEVs to BEVs." https://automotivepolicy.ca/fromicevstobevs/. Accessed September 21, 2025.

BCG (Boston Consulting Group), ADB (Asian Development Bank, and NITI Aayog. 2022. *Promoting Clean Energy Usage through Accelerated Localization of E-Mobility Value Chain*. Boston, United States: BCG; Manila, Philippines: ADB; New Delhi: NITI Aayog. https://www.niti.gov.in/sites/default/files/2023-07/Niti-Aayog_Report-VS_compressed_compressed.pdf.

Bansal, P., T. Sen, and C. Kanuri. 2024. "Creating Holistic and Skilled Enterprises for a Smooth and Just Transition to Electric Mobility." Conference Proceedings. New Delhi: WRI India. https://wri-india.org/sites/default/files/Just-EV-Transition_Conference-Proceeding_WRI-India-website.pdf.

Brandes, O., S. Brege, and P.-O. Brehmer. 2013. "The Strategic Importance of Supplier Relationships in the Automotive Industry." *International Journal of Engineering Business Management* 5: 17. https://doi.org/10.5772/56257.

Castellino, C. 2024. "Standardisation Gaps, High Cost, Lack of Scale Undermine India's Potential to Become a Global EV Hub," March 5. The Secretariat. https://thesecretariat.in/article/standardisation-gaps-high-cost-lack-of-scale-undermine-india-s-potential-to-become-a-global-ev-hub.

Charan, P. 2025. "India's Rare Earth Magnets Crisis: What Lies Ahead for the EV Sector?" Mint. June 11. https://www.livemint.com/industry/indias-rare-earth-magnets-crisis-what-s-next-for-the-ev-sector-11749616024940.html.

CLEPA (European Association of Automotive Suppliers). 2021. *Electric Vehicle Transition Impact Assessment Report 2020-2040: A Quantitative Forecast of Employment Trends at Automotive Suppliers in Europe*. Etterbeek, Belgium: CLEPA. https://www.clepa.eu/wp-content/uploads/2021/12/Electric-Vehicle-Transition-Impact-Report-2020-2040.pdf.

CRISIL Research. 2024. "CRISIL SME Tracker: Uptick in Output Volume to Benefit Auto Component SMES." *Business Standard*. October 22. https://www.business-standard.com/economy/news/crisil-sme-tracker-uptick-in-output-volume-to-benefit-auto-component-smes-124102201423_1.html.

Dash, A. 2023. "Adapting to Electric Vehicles Value Chain in India:

The MSME Perspective." *Case Studies on Transport Policy* 12: 100996. https://doi.org/10.1016/j.cstp.2023.100996.

Dhairiyasamy, R., and D. Gabriel. 2025. "Sustainable Mobility in India: Advancing Domestic Production in the Electric Vehicle Sector." *Discover Sustainability* 6 (1). Springer: 52. https://doi.org/10.1007/s43621-025-00844-3.

ERM Sustainability Institute. 2024. *Embedding Just Transition into Corporate Climate Action Strategies*. London: ERM Sustainability Institute. https://www.sustainability.com/globalassets/sustainability.com/reports/tl_just_transition_briefing_v7_2409a.pdf.

Etikan, I., S.A. Musa, and R.S. Alkassim. 2016. "Comparison of Convenience Sampling and Purposive Sampling." *American Journal of Theoretical and Applied Statistics* 5 (1): 1–4. https://www.science-publishinggroup.com/article/10.11648/j.ajtas.20160501.11.

Franco, N., and N. Karamally. 2024. *Corporate Low-Carbon Transition Planning: Best Practices & Recommendations to Support*. Washington, DC: Center for Climate and Energy Solutions (C2ES). https://www.c2es.org/wp-content/uploads/2024/07/Corporate-Low-Carbon-Transition-Planning-Best-Practices-Recommendations-to-Support-Credible-Action.pdf.

Goel, S., T. Moerenhout, and R. Bollini. 2024. *Unlocking Supply Chains for Localizing Electric Vehicle Battery Production in India*. Geneva: IISD (International Institute for Sustainable Development). https://www.iisd.org/system/files/2024-11/electric-vehicle-battery-production-india.pdf.

Govardan, D. 2025. "China+1 = Coimbatore." *The Times of India*. April 6. https://timesofindia.indiatimes.com/city/chennai/china1coimbatore/articleshow/120042000.cms.

Hyundai. 2024. *Sustainability Report: 2024 Sustainability Report*. Seoul: Hyundai. https://www.hyundai.com/content/dam/hyundai/kr/ko/data/company-report/2024/07/16/hmc-sr-en-2024.pdf.

IBEF (India Brand Equity Foundation). 2025. "Auto Components Industry in India," November. https://www.ibef.org/industry/autocomponents-india.

IEA. 2025. Global EV Outlook 2025: *Expanding sales in diverse markets*: IEA. https://iea.blob.core.windows.net/assets/7ea38b60-3033-42a6-9589-71134f4229f4/GlobalEVOutlook2025.pdf

iForest (International Forum for Environment, Sustainability and Technology). 2024. *ICEV to EV: Challenges, Opportunities, and the Roadmap for Just Transition in India's Automobile Sector*. Noida, India: iForest. https://iforest.global/event/report-release-conference-from-ice-to-ev-opportunities-and-challenges-for-just-transition-in-indian-automobile-sector/.

ILO (International Labour Organization). 2015. "Guidelines for a Just Transition towards Environmentally Sustainable Economies and Societies for All." Geneva: ILO. https://www.ilo.org/sites/default/files/wcmsp5/groups/public/%40ed_emp/%40emp_ent/documents/publication/wcms_432859.pdf.

ILO. 2022. "How MSMES Can Contribute to and Benefit from a Just Transition." Just Transition Policy Brief. Geneva: ILO. https://www.ilo.org/sites/default/files/wcmsp5/groups/public/@ed_emp/@emp_ent/documents/publication/wcms_858855.pdf.

ILO. 2024. *The Business Case for Just Transition: An Overview of*

30 | WRI INDIA

Driving a just electric vehicle transition in India: Supply-chain practices for large automotive manufacturing enterprises

the Economic Benefits of the Transition to a Sustainable Economy. Geneva: ILO. https://www.ilo.org/sites/default/files/2024-11/ILO-ACTEMP-The-Business-Case-for-Just-Transition-RGB-21NOV.pdf.

Kerswell, T., and S. Pratap. 2019. "Informality in the Indian Automobile Industry." In Globalization, Labour Market Institutions, Processes and Policies in India: Essays in Honour of Lalit K. Deshpande, edited by K.R. Shyam Sundar, 187-209. Singapore: Springer Nature Singapore. https://doi.org/10.1007/978-981-13-7111-0_7.

Khan, N.A. 2021. "PLI Scheme Draft Offers Benefit to Big Auto Manufacturers Only; Here is Why." The Economic Times. July 2. https://auto.economictimes.indiatimes.com/news/industry/etauto-exclusive-pli-scheme-draft-offers-benefit-to-big-auto-manufacturers-only-here-is-why/79751658.

Khurana, S., M. Kumar, S. Sundaravaradan, K.S. Kumar, and R. Sethi. 2025. Navigating the EV Shift: Opportunities and Challenges for Automotive MSMEs. New Delhi: Climate Policy Initiative (CPI). https://www.climatepolicyinitiative.org/wp-content/uploads/2025/06/Navigating-the-EV-Shift-Opportunities-and-Challenges-for-Automotive-MSMEs.pdf.

Kumar, K.B. 2022. "China-PLUS-One is an Opportunity for Indian Firms." The Hindu. May 22. https://www.thehindu.com/business/china-plus-one-is-an-opportunity-for-indian-firms/article65443033.ece.

Madgavkar, A., M. Piccitto, O. White, M.J. Ramirez, J. Mischke, and K. Chockalingam. 2024. "A Microscope on Small Businesses: Spotting Opportunities to Boost Productivity," May 2. McKinsey. https://www.mckinsey.com/mgi/our-research/a-microscope-on-small-businesses-spotting-opportunities-to-boost-productivity.

McKinsey. 2020. "Taking Supplier Collaboration to the Next Level," July 7. https://www.mckinsey.com/capabilities/operations/our-insights/taking-supplier-collaboration-to-the-next-level.

McKinsey. 2021. "Overcoming Barriers to Multitier Supplier Collaboration," July 7. https://www.mckinsey.com/capabilities/operations/our-insights/overcoming-barriers-to-multitier-supplier-collaboration.

Mehra, S., and A. Malik 2025. "From Imports to Made-in-India: Why Localising EV Manufacturing Is Key," April 9. Grant Thornton. https://www.grantthornton.in/en/insights/articles/from-imports-to-made-in-india-why-localising-ev-manufacturing-is-key/.

MoRTH (Ministry of Road Transport & Highways). 2025. "Vahan Dashboard." https://vahan.parivahan.gov.in/vahan4dashboard/vahan/dashboardview.xhtml.

NITI Aayog. 2025a. Automotive Industry: Powering India's Participation in Global Value Chains. New Delhi: NITI Aayog. https://www.niti.gov.in/sites/default/files/2025-06/Automotive%20Industry%20Powering%20India%E2%80%99s%20participation%20in%20GVC_Non%20Confidential.pdf.

NITI Aayog. 2025b. "Enhancing MSME Competitiveness in India."

NITI Aayog. 2025c. "Unlocking $200 Billion Opportunity: Electric Vehicles in India."

OECD (Organisation for Economic Co-operation and Development). 2023. OECD Guidelines for Multinational Enterprises on Responsible Business Conduct. Paris: OECD Publishing. https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/06/oecd-guidelines-for-multinational-enterprises-on-responsible-business-conduct_a0b49990/81f92357-en.pdf.

PIB (Press Information Bureau). 2021. "Round Table to Promote Electric Vehicles," December 1. Press Release. Ministry of Heavy Industries, Government of India. https://www.pib.gov.in/PressReleaseFramePage.aspx?PRID=1776734.

PIB. 2025a. "Investment and Turnover Limits for Classification of All MSMES to Be Enhanced to 2.5 and 2 Times, Respectively," February 1. Press Release. Ministry of Finance, Government of India. https://www.pib.gov.in/PressReleasePage.aspx?PRID=2098389&reg=3&lang=2.

PIB. 2025b. "PM e-DRIVE AND PLI Schemes." https://www.pib.gov.in/PressReleasePage.aspx?PRID=2147042.

PIB. 2025c. "Revolutionizing Mobility: The Make in India Auto Story." https://www.pib.gov.in/PressReleaseDetailm.aspx?PRID=2114919.

PwC. 2019. "Merge Ahead: Electric Vehicles and the Impact on the Automotive Supply Chain." https://www.pwc.com/us/en/industries/industrial-products/library/electric-vehicles-supply-chain.html.

PwC. 2022. "Winning the EV Race through Localisation: An India Perspective." https://www.pwc.in/assets/pdfs/industries/automotive/localisation-of-ev-component-supply-chain-in-india.pdf.

Riat, R.S. 2019. "Rationalization & Tierization of Indian Automotive Industry: Challenges for Indian Tier 2/3 Suppliers." https://www.aims-international.org/aims16/16ACD/PDF/A-224-Final.pdf.

Robins, N., S. Muller, and K. Szwarc. 2021. From the Grand to the Granular: Translating Just Transition Ambitions into Investor Action. London: Grantham Research Institute on Climate Change and the Environment and Centre for Climate Change Economics and Policy, London School of Economics and Political Science. https://www.lse.ac.uk/granthaminstitute/wp-content/uploads/2021/07/From-the-Grand-to-the-Granular_translating-just-transition-ambitions-into-investor-action.pdf.

Roth, J. 2025. Assessing the 'Just' in Corporate Transition Plans: Framework and Guidance. Amsterdam: WBA (World Benchmarking Alliance). https://assets.worldbenchmarkingalliance.org/app/uploads/2025/04/Assessing-the-Just-in-corporate-transition-plans-framework-and-guidance.pdf.

Saha, D., R. Shrestha, N. Hunt, and E. Kim. 2025. US Automotive Manufacturing Workers in the Transition to Battery Electric Vehicles: An Assessment of the Impact and Opportunities. Report. Washington, DC: World Resources Institute. https://files.wri.org/d8/s3fs-public/2025-11/us-automotive-manufacturing-workers-transition-battery-electric-vehicles.pdf?VersionId=sWr_FDlcn8SRNHpE3fPM.m6KUGc.F0q_.

Saha, D., J. Jaeger, S. Rajpurohit, E. Said, and J.A. Laitner. 2023. "A Roadmap for Michigan's EV Future: An Assessment of the Employment Effects and Just Transition Needs." Washington, DC: World Resources Institute. https://files.wri.org/d8/s3fs-public/2023-05/roadmap-michigan-ev-future.pdf.

Said, E., G. Flynn, E. Metzger, and S. Chattaraj. 2025. Elephant in the Boardroom: People Are Missing in Corporate Supply Chain Goals. Working Paper. Washington, DC: World Resources Institute. https://files.wri.org/d8/s3fs-public/2025-08/elephant-in-the-boardroom-people-are-missing-in-corporate-supply-chain-goal.pdf.

WORKING PAPER | May 2026

31

Sakkab, L.H., and N.Y. 2006. Connect and Develop: Inside Procter & Gamble's New Model for Innovation. *Harvard Business Review*. https://hbr.org/2006/03/connect-and-develop-inside-procter-gambles-new-model-for-innovation.

Saldana, J.M. 2015. *The Coding Manual for Qualitative Researchers*. SAGE Publications. https://hbr.org/2006/03/connect-and-develop-inside-procter-gambles-new-model-for-innovation.

Seetharaman, M., M. Sampat, P.K. Addepalli, P. Sagi, A. Agarwal, and V. Modi. 2023. "India Electric Vehicle Report 2023," December 7. *Bain & Company*. https://www.bain.com/insights/india-electric-vehicle-report-2023/.

Sen, T., P. Bansal, P. Kulkarni, and C. Kanuri. 2025. "The Projected EV Transition in the Indian in the Indian Automotive Manufacturing Industry: Perceptions and Enterprise-Level Strategies." Working Paper. New Delhi: WRI India. https://wri-india.org/sites/default/files/2025-09/The%20projected%20EV%20transition%20in%20the%20Indian%20automotive%20manufacturing%20industry%20online%20%281%29.pdf.

SIDBI (Small Industries Development Bank of India). 2021. *Annual Report 2021-22*. Lucknow, India: SIDBI. https://www.sidbi.in/annualreport/AnnualReport202122/pdf/SIDBI_AR_Final-file.pdf.

SSE (Scottish and Southern Energy). 2024. *Embedding a Just Transition: Strategy Update*. Perth, Scotland: SSE. https://www.sse.com/media/4qfjgvu/just-transition-strategy-update.pdf.

Suri, H. 2011. "Purposeful Sampling in Qualitative Research Synthesis." *Qualitative Research Journal* 11 (2): 63–75. https://doi.org/10.3316/QRJ1102063.

Tata Motors. 2023. "Business Responsibility & Sustainability Report." Tata Motor Financials. https://www.tatamotors.com/financials/79-ar-html/pdf/tata-motor-IAR-2023-24-BRSR.pdf.

Uchikawa, S. 2011. "Small and Medium Enterprises in the Indian Auto-Component Industry." *Economic and Political Weekly* 46 (25), 51–59. https://www.head-fi.org/threads/dac-or-amp-fiio-e11k-amp-or-e10k-dac.743708/.

UN Global Compact. 2022. *Just Transition for Climate Adaptation: A Business Brief*. https://unglobalcompact.org/library/6099.

UN Global Compact. 2023. *Just Transition in Supply Chains: A Business Brief*. https://unglobalcompact.org/library/6145.

UNDP (United Nations Development Programme). 2022. "What Is Just Transition? And Why Is It Important?" November 3. https://climatepromise.undp.org/news-and-stories/what-just-transition-and-why-it-important.

WBA (World Benchmarking Alliance). 2023. *Moving from Pledges to Implementation: A Guide for Corporate Just Transition Action*. Amsterdam: WBA. https://assets.worldbenchmarkingalliance.org/app/uploads/2023/11/Moving-from-pledges-to-implementation-a-guide-for-corporate-just-transition-action.pdf.

WRI India. 2022. "Just Transition and Skill Development in the Electric Vehicle Industry." Conference Proceedings. https://www.wri.org/research/just-transition-and-skill-development-electric-vehicle-industry.

YES BANK and ACMA (Automotive Component Manufacturers Association of India). 2021. *EV Landscape: Opportunities for India's Auto Component Industry*. Mumbai: YES BANK and New Delhi: ACMA. https://www.acma.in/uploads/otherdocmanager/ACMA_YES_Bank_Report_EV_Landscape_Opportunities_for_Indias_Auto_Component_Industry.pdf.

32 | WRI INDIA

THIS PAGE IS INTENTIONALLY LEFT BLANK

WRI INDIA

## Acknowledgments

We are grateful to senior executives from automotive OEMs and ACMs for permitting us to conduct one-on-one discussions with them at their premises and for providing their insights about the supply-chain practices being considered or undertaken for enabling a just EV transition in India's automotive industry.

This paper was vastly improved by feedback and comments from internal and external reviewers. Ordered alphabetically by first name, we would like to thank Aloke Mukherjee (Program Lead—Research and Cities, WRI India), Anil Kumar (President and Managing Director, SEG Automotive India Private Limited), Devashree Saha (Director – US Clean Energy Economy Program, World Resources Institute), Eliot Metzger (Director – Sustainable Business & Innovation, World Resources Institute), Manu Mathai (Director, Research, Data & Impact, WRI India), Meenakshi Sundaram (Chief Technology Officer – Amalgamations Components Group, India), Pawan Mulukutla (Executive Program Director – Integrated Transport, Clean Air & Hydrogen, WRI India), Purva Sharma (Lead - Research, Data & Impact, WRI India), Ulka Kelkar (Executive Director – Climate, Economics and Finance, WRI India), and two anonymous reviewers, whose valuable suggestions and insights helped improve this paper.

We would also like to thank Supratheesh T. (former Senior Program Associate, Climate, Economics and Finance, WRI India), Debojyoti Hazra (former Intern, Electric Mobility, WRI India), Anuja Ramugade (Program Associate, Electric Mobility, WRI India), Abhishek Mahajan (Program Associate, Electric Mobility, WRI India), Kishor Veer (former Junior Program Associate, Climate, Economics and Finance, WRI India), Saket Singh (Senior Program Associate, Climate, Economics and Finance, WRI India), and Pranusha Kulkarni (former Senior Program Associate, Electric Mobility, WRI India) who supported the authors with primary data collection and analysis. Finally, we would like to express our gratitude to Allison Meyer, Renee Pineda, Robin Infant Raj Devadoss, Karthikeyan Shanmugam, Santhosh Matthew Paul, Ankita Rajeshwari, Ankita Saxena, Safia Zahid, Safa Fathim, Rama Thoopal and the Zebra Kross team for administrative, editorial, and design support.

## About the authors

**Priya Bansal** is a Program Manager of Electric Mobility in the Sustainable Cities Program at WRI India.

Contact: priya.bansal@wri.org

**Priyal Shah** is a Program Manager in the Climate, Economics and Finance Program at WRI India.

Contact: priyal.shah@wri.org

**Tavleen Singh** is a Senior Program Associate of Electric Mobility in the Sustainable Cities Program at WRI India.

Contact: tavleen.singh@wri.org

**Chaitanya Kanuri** is a Program Director of Electric Mobility in the Sustainable Cities Program at WRI India.

Contact: chaitanya.kanuri@wri.org

**Ashwini Hingne** is a Program Director in the Climate, Economics and Inclusive Transitions Program at WRI India.

Contact: ashwini.hingne@wri.org

**Anuradha Ranganath** is a Program Lead of Electric Mobility in the Sustainable Cities Program at WRI India.

Contact: anuradha.ranganath@wri.org

## About WRI India

WRI India, an independent knowledge organisation registered as India Resources Trust, provides objective information and practical proposals to foster environmentally sound and socially equitable development. Through research, analysis, and recommendations, WRI India puts ideas into action to build transformative solutions to protect the earth, promote livelihoods, and enhance human well-being.

Know more: wri-india.org

Creative Commons

Copyright 2026 WRI India. This work is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-nd/4.0/

WRI INDIA

---
doc_id: 25May_Battery Aadhaar For India_Expert Note
source_pdf: documents/25May_Battery Aadhaar For India_Expert Note.pdf
extraction_method: postgres-full-text
parse_backend: mistral
parse_model: mistral-ocr-latest
char_count: 30911
title: "Battery Aadhaar for India: Potential Pathways for a Domestic Battery Data Management Framework"
authors: Parveen Kumar; Chaitanya Kanuri
date_published: 2026-05-25
year_published: 2026
article_type: Expert Note
wri_primary_office: WRI India
language: en
doi: 10.46830/wrien.25.00072
status: searchable
---

WRI INDIA

EXPERT NOTE

# Battery Aadhaar for India

## POTENTIAL PATHWAYS FOR A DOMESTIC BATTERY DATA MANAGEMENT FRAMEWORK

Parveen Kumar and Chaitanya Kanuri

### Introduction

Batteries are central to India's clean energy transition, supporting electric mobility, renewable energy integration, and grid stability. With the annual demand projected to reach 160 GWh by 2030, strengthening domestic manufacturing capacity is vital for energy security (NITI Aayog and GGEF TCF 2022). However, battery production remains heavily dependent on imported critical minerals including lithium, nickel, cobalt, graphite, and phosphorus, exposing the supply chain to global disruptions and price volatility. Limited reuse and recycling further exacerbate these vulnerabilities, resulting in material losses and forgone economic value.

Addressing these challenges requires a shift towards a circular battery value chain that improves resource efficiency, reduces import dependence, and lowers environmental impacts. However, progress toward circularity is constrained by limited visibility across the battery lifecycle. In this context, a robust battery data-sharing system, such as a battery passport, emerges as a key enabler, supported by clear standards and regulations to ensure safety, sustainability, and traceability across the battery lifecycle.

Such a system can provide essential information on material origin, carbon footprint, and battery performance, enabling regulators to strengthen oversight, manufacturers to improve design and quality, and downstream actors such as refurbishers and recyclers to make informed decisions across the battery lifecycle.

This expert note explores the concept of a "Battery Aadhaar," a digital identity system for end-to-end battery lifecycle traceability in India. While global initiatives such as the EU Battery Passport offer guidance, India requires a tailored approach that reflects its policy environment, market landscape, and development goals.

### CONTENTS

1 Introduction
2 Battery data for a circular economy
4 Pathways to build a Battery Aadhaar for India
9 References
12 Acknowledgments

Suggested Citation: Kumar, P., and C. Kanuri. 2026. "Battery Aadhaar for India: Potential Pathways for a Domestic Battery Data Management Framework." Expert Note. New Delhi: WRI India. Available online at: https://doi.org/10.46830/wrien.25.00072

Expert notes provide timely, focused, and concise information for urgent challenges, based on expert perspectives.

Expert Note | May 2026 | 1

## Battery data for a circular economy

Battery supply chains generate a wide range of data, spanning critical mineral sourcing, cell chemistry, battery design, and operational performance. When fragmented or inaccessible, these data offer limited value. When systematically shared and analyzed, however, they enable responsible sourcing of raw materials, enhanced battery safety and performance, extended battery life, reverse logistics tracking, informed reuse vs. recycling decisions, and reductions in lifecycle emissions. Potential use cases for electric vehicle (EV) batteries, which are projected to account for over three-quarters of battery demand by 2030 (IEA 2023), span the battery lifecycle, from sourcing and manufacturing to use, reuse, and end-of-life management. These use cases, illustrated in Figure 1, depend on effective data sharing among key stakeholders in a battery value chain, including EV and battery manufacturers, battery users (such as EV fleet owners), as well as refurbishers and recyclers.

A battery passport is a digital record that links a battery to a standardized set of data about its origin, composition, and performance. As a form of a product passport, which is a policy mechanism typically used to enable circular business models (King et al. 2023), it assigns a unique digital identity to each battery. This identity enables transparency and traceability across the battery's lifecycle, supporting informed consumer choices, regulatory compliance monitoring, and efficient battery reuse, repurposing, and recycling—all of which are essential to advancing a circular economy.

A battery passport can also drive accelerated clean energy adoption, by improving access to finance for batteries, enabling battery-as-a-service business models, and supporting more predictable resale value of batteries (Battery Pass 2024).

**FIGURE 1 | Key EV battery data use cases and their benefits across stakeholders in the battery ecosystem**

![img-0.jpeg](img-0.jpeg)

Source: WRI India authors.

2 | WRI-INDIA.ORG

Expert Note

## Shared battery data frameworks across the globe

Globally, countries are advancing efforts to enable battery data sharing, primarily through battery labelling and traceability requirements (Figure 2). These labels typically include information on battery type, capacity, hazardous substances, and safe disposal methods. Such measures improve transparency and support safer handling, transportation, and end-of-life management of batteries.

For instance, Japan and South Korea mandate safety certification labels, while the US and Japan require additional labels for lithium battery transport. In Japan, battery labelling and recycling requirements are governed under the Act on the Promotion of Effective Utilization of Resources, first introduced in April 2001 and subsequently updated (METI 2001). A few countries, including China and South Korea, require unique identification numbers (UINs) for battery traceability. China has introduced its national EV battery traceability management system in February 2018 through the Interim Measures for the Management of Recycling and Utilization of New Energy Vehicle Power Batteries (MIIT 2018), requiring UIN registration and lifecycle data reporting. Since August 2018, China has mandated UIN registration for all EV batteries, with lifecycle data updates uploaded to a centralized traceability platform. South Korea introduced UIN-based tracking for EV batteries in February 2025 under the amended Motor Vehicle Management Act (MOLIT 2025). The European Union, through its EU Battery Regulation 2023/1542 concerning batteries and concerning batteries and end-of-life battery management, adopted in July 2023, has mandated digital battery passports that store standardized information on battery origin, composition, performance, and lifecycle attributes for certain types of batteries sold in the EU, with effect from February 2027 (Regulation (EU) 2019/1020).

**FIGURE 2 | Government interventions across the globe on battery data frameworks (Battery Pass consortium 2024)**

![img-1.jpeg](img-1.jpeg)

**DISCLAIMER:** All the maps in this expert note are for illustrative purposes and do not imply the expression of any opinion on the part of WRI India, concerning the legal status of any country or territory or concerning the delimitation of frontiers or boundaries.

Source: WRI India authors.

Battery Aadhaar for India | 3

The EU battery passport will be required for all EV, light motor transport (LMT), and industrial batteries over 2 kWh, with different levels of information access for the public, relevant battery stakeholders, and regulatory authorities. In addition to physical labelling requirements on the battery, the digital battery passport must provide standardized information on the source of critical minerals, the manufacturing carbon footprint, dismantling information, and performance, durability and safety data, among other data parameters as required by regulation.

The regulation also defines the responsibility for economic operators for compliance and management of the battery passport, and emphasizes the need for open data standards, interoperability across systems, data integrity, and robust security and privacy safeguards. While still under development, the EU battery passport provides a useful reference as India moves towards creating its own “*Battery Aadhaar*” digital identity system for battery traceability and circularity.

## Status of battery data sharing in India

India’s battery data sharing ecosystem is evolving incrementally. India’s Battery Waste Management Rules (BWMR), August 2022, introduced extended producer responsibility (EPR), requiring producers to disclose key details of their batteries and to share data on compliance with meeting collection, recovery, and recycled-content targets. Amendments to the BWMR in February 2025 permitted producers to use quick response (QR) codes or barcodes on batteries for EPR registration, to enable digital identification and tracking of batteries under the EPR framework (Kumar, et al. 2024).

More recently, in December 2025, the Ministry of Road Transport and Highways (MoRTH) released draft Guidelines for Implementation of Battery Pack Aadhaar System (MoRTH 2025), with a focus on EV batteries. The MoRTH guidelines propose the assignment of a Battery Pack Aadhaar Number (BPAN), propose potential static and dynamic data requirements, and distinguish between public and private data accessibility.

Among industry stakeholders, EV manufacturers now use telematics based on battery management systems (BMS) to share battery usage data with customers and collaborate with refurbishers and recyclers to assess battery health and value. Digital battery passport solutions are emerging from technology service providers, to serve the European market and for captive use by EV fleets (Tata Elxsi 2025; Gupta 2024).

However, non-standardized data formats and protocols, weak stakeholder coordination, and lack of data sharing mandates hinder interoperability between solutions and prevent traceability across the lifecycle of batteries. A unified Battery Aadhaar framework can address these gaps by establishing common standards for battery data generation, sharing, and verification, enabling much needed transparency, interoperability, and traceability to unlock economic value and lower the environmental footprint across the battery value chain.

## Pathways to build a Battery Aadhaar for India

The need for a Battery Aadhaar for India, first highlighted in the eMobility R&D Roadmap for India report by the Office of the Principal Scientific Advisor to the Government of India (PSA 2024), arises amidst growing adoption of digital public infrastructure (DPI), which refers to foundational digital systems that enable public and private services to function at scale. Typically developed to fulfil functions of digital authentication, digital transactions, and data exchange, DPI systems can enable the scaling up of adoption, interoperability, transparency, accountability, safety and security, inclusion, and improved coordination across the sector (Fetter et al. 2025, Mukherjee, et al. 2025).

Named after India’s ubiquitous Aadhaar identification system, a well-known global archetype of DPI, the Battery Aadhaar can be envisioned as a DPI for universal authentication of battery packs and standardized battery data exchange among relevant stakeholders across the battery lifecycle.

India’s battery ecosystem and digital infrastructure create a unique context requiring tailored digital solutions. The dominance of electric two- and three-wheelers increases the prevalence of small-format batteries, many under 2 kWh (the threshold of battery packs requiring the EU battery passport), while uneven digital connectivity, particularly in rural and lower-income regions, proposes additional challenges. Consequently, the Battery Aadhaar must be designed to suit India’s diverse market structure, technology landscape, and infrastructure conditions. The country’s deep experience in operationalizing fit-for-context DPI systems will need to be leveraged in developing the Battery Aadhaar.

The following section outlines the essential components and considerations for developing a Battery Aadhaar tailored to India’s needs. The analysis draws on global literature on digital product and battery passports, insights from India’s DPI experiences, and perspectives gathered from consultations with Indian battery industry stakeholders (Bansal et al. 2024).

4 | WRI-INDIA.ORG

Expert Note

## Components of a Battery Aadhaar system

Developing a Battery Aadhaar requires clarity on its components, India-specific needs, and contextual challenges. Key elements include identifying priority use cases and defining corresponding battery data requirements, establishing governance and a secure technology stack, creating supportive policies for universal adoption, and designing viable business models to drive market participation and long-term sustainability.

### Data requirements and availability

A key step in developing the Battery Aadhaar is defining the objectives and using cases it must serve, along with the associated data requirements. This can follow a top-down approach, as in the EU Battery Regulation (Battery Pass 2023), or a bottom-up approach driven by stakeholder needs (Berger et al. 2022; Berger et al. 2023).

Regulators require data to ensure safety, sustainability, and responsible sourcing, while OEMs, refurbishers, and recyclers need performance insights to extend battery life and improve reuse and recycling. For India, the Battery Aadhaar should additionally prioritize context-specific needs such as enforcing EPR compliance, verifying the quality of imported battery cells, and enabling lifecycle traceability of batteries in the domestic market.

Identifying these priority use cases will help determine the essential data attributes required for the Battery Aadhaar system. An indicative list of data attributes for a battery passport, drawn from existing research, is provided in Figure 3.

Designing the Battery Aadhaar framework requires accounting for varied data availability, formats, and connectivity across regions, as well as access to real-time battery performance data. It should define fit-for-purpose static and dynamic data needs, protect intellectual property, manage costs, and allow voluntary data inputs to support emerging, market-driven applications (Bansal et al. 2024). The framework must also remain adaptable, allowing for the inclusion of new data categories as regulatory and industry needs evolve.

**FIGURE 3 | Data requirements and availability for a battery passport**

![img-2.jpeg](img-2.jpeg)

Source: Berger et al. 2023

Battery Aadhaar for India | 5

## Data and platform governance structure

The governance structure of battery passports comprises both data and platform governance. Data governance is broadly defined as a system of rights and responsibilities that determines who can take what actions concerning data and information within the product passport (Ducuing & Reich 2023). Further, platform governance defines the standards and protocols to be followed for collecting, handling, storing, and accessing the data within the product passport.

A strong governance structure is essential for Battery Aadhaar to ensure transparency, accountability, and interoperability. It should define stakeholder roles, standardize data formats and access protocols, while safeguarding ownership and security through encryption and verification. India's DPI models such as Unified Payments Interface (UPI) and Open Network for Digital Commerce (ONDC) provide useful templates for decentralized, role-based governance (Kumar, Meena, & Aggarwal 2025). Figure 4 provides an overview of an indicative data governance structure, with data and information flows between value chain stakeholders.

**FIGURE 4 | Overview of the digital battery passport ecosystem including the value chain participants and the other stakeholders**

![img-3.jpeg](img-3.jpeg)

Source: Ducuing & Reich 2023.

6 | WRI-INDIA.ORG

Expert Note

## Data management technologies

Emerging digital technologies will play a central role in implementing and governing the Battery Aadhaar, supporting transparent, traceable, and circular battery value chains. Distributed and decentralized systems can support interoperability and wider stakeholder participation, while advanced computing enables efficient processing of granular battery data. Although multiple technologies exist for data collection and management, their cost, scalability, and connectivity needs must be assessed (Langley et al. 2023). Given the sensitivity of supply chain and recycled material data, domestic data storage and management provisions may also be required to ensure data security and regulatory oversight.

**Data collection and handling:** Static battery data are easier to gather, while dynamic data often has gaps. Using BMS data covering temperature, voltage, current, gas detection, and coolant breaches addresses this. Decentralized identifiers (DIDs), combined with self-sovereign identities (SSIs) and verifiable credentials (VCs), enhance secure, privacy-focused data handling. Internet of things (IoT) enables real-time, continuous data collection (Langley et al. 2023).

**Data curation, processing, and sharing:** Battery Aadhaar will manage vast data volumes using advanced technologies. Cloud computing provides scalable storage and processing, while blockchain technologies can ensure secure, decentralized data sharing. Data analytics, machine learning, and artificial intelligence (AI) extract insights, enabling value-added services for refurbishers, recyclers, energy aggregators, and other battery management stakeholders (Langley et al. 2023).

**Data exploitation and use:** Battery Aadhaar data can help enhance battery design and inform decisions on usage, reuse, and end-of-life management. Digital twins simulate performance and monitor real-time data, aiding optimization. Additionally, digital marketplaces leverage this data to enable trading of physical and digital assets, fostering circular economy practices throughout the battery value chain (Langley et al. 2023, Lambha et al, 2024).

## Policy and regulatory frameworks

Effective implementation of Battery Aadhaar requires strong regulations, harmonized standards, and reliable data certification to ensure credibility. A clear legal foundation must mandate traceable UINs, minimum data disclosure, access protocols, and interoperable formats. Multiple ministries, such as the Ministry of Mines, Ministry of Road Transport and Highways, and the Ministry of Environment, Forests and Climate Change, will need to coordinate and align efforts with existing policies like the Battery Waste Management Rules and the BPAN guidelines. Integrating data platforms like Vahan can strengthen the system. Regulations should proactively address inconsistent standards and data confidentiality challenges (Rizos & Urban 2024). The framework should also comply with the Digital Personal Data Protection Act (DPDPA) 2023, ensuring data privacy and intellectual property protection (Digital Personal Data Protection Act, 2023).

Given the global nature of battery supply chains and material flows, the Battery Aadhaar policy framework must also enable alignment with requirements arising from digital traceability and product passport initiatives in other parts of the world.

## Business models

Developing and maintaining the Battery Aadhaar system will involve considerable compliance costs for the stakeholders responsible for the system. These include costs for data collection and standardization, user interfaces for data sharing, secure data storage, advanced analytics, and robust digital infrastructure and protocols to ensure verifiable and credible data exchange. For medium and small-sized enterprises (MSMEs) in the battery value chain, these costs could pose a significant barrier. Moreover, shifting these expenses to end consumers would reduce the viability of circular business models.

However, improved battery data availability can enhance efficiency across the value chain, lowering compliance costs, enabling predictive maintenance, extending battery life, supporting battery reuse, and boosting material recovery from recycling. A study of the European Union's battery passport determines that battery data can reduce procurement costs for used batteries by 2–10%, and costs for pre-processing and treatment in recycling by 10–20% (Battery Pass 2024).

The value generated from these efficiencies can help offset the cost of Battery Aadhaar through innovative business models. Further, public research and development (R&D) support can offset development costs, while policy incentives, such as tax benefits or performance-linked incentive (PLI) linked rewards, can encourage adoption of Aadhaar-enabled batteries. Fee-based access to non-public data and value-added analytics services by third parties can generate revenue, support cost recovery, and strengthen the long-term sustainability of the Battery Aadhaar system.

Battery Aadhaar for India | 7

## Approach for effective development

Developing a robust Battery Aadhaar system for India requires a collaborative approach that takes into account the considerations of all stakeholders. It also needs pilot demonstrations and impact assessments to ensure reliability and measure impacts. In addition, awareness and capacity building initiatives are required for preparing the ecosystem (Bansal et al. 2024; BEPA 2023; Kwak and Kang 2025).

**Involve all relevant stakeholders to inform the Battery Aadhaar framework:** Designing the Battery Aadhaar must be an inclusive process, involving all key stakeholders across India's battery value chain. Building consensus among regulators, data providers (such as battery and EV manufacturers), and data users (including operators, recyclers, and refurbishers) is crucial to fostering trust, ensuring collaboration, and enabling effective implementation.

**Facilitate testing and impact assessments of the proposed system:** The Battery Aadhaar framework must be tested and validated to ensure system and stakeholder readiness before full-scale deployment. Cost-benefit analyses will demonstrate the potential impacts and highlight possible business models for implementation. A consortium-based approach can leverage cross-functional teams with diverse expertise to test various aspects of implementation and potential impacts of the Aadhaar, while also identifying unintended consequences that could hinder progress toward a sustainable battery value chain.

**Undertake awareness and capacity building initiatives:** Awareness and capacity building initiatives are vital to enable stakeholders to effectively use battery data for enhanced transparency, safety, and informed decision-making across the battery's lifecycle. Targeted efforts may include dashboards highlighting analyses of public Battery Aadhaar data, case study compilations highlighting value chain impacts, and development of eco-labelling frameworks for responsibly sourced or energy-efficient batteries. Such initiatives clearly communicate the value of Battery Aadhaar for different stakeholders and can drive widespread understanding and adoption.

The Battery Aadhaar can advance India's circular economy for batteries, provided it is built collaboratively with a decentralized, interoperable, technology-neutral design, supported by continuous research and inclusive stakeholder consultation.

8 | WRI-INDIA.ORG

Expert Note

## References

Bansal, P, Meshram, A, Kanuri, C, & Kumar, P. (2024). *Development of data frameworks for battery circularity in India*. WRI India. https://wri-india.org/research/development-data-frameworks-battery-circularity-india

Battery Pass Consortium. (2024, November). *Unlocking the value of the battery passport*. https://thebatterypass.eu/assets/images/value-assessment/pdf/2024_BatteryPassport_Value_Assessment.pdf

Batteries European Partnership Association (BEPA). (2023). Getting the general ID: What projects are supporting the development of the battery passport? https://bepassociation.eu/getting-the-general-id-what-projects-are-supporting-the-development-of-the-battery-passport/

Berger, K, Baumgartner, R. J, Weinzerl, M, Bachler, J, Preston, K, & Schöggl, J.-P. (2023). Data requirements and availabilities for a digital battery passport – A value chain actor perspective. *Cleaner Production Letters*, 4, 100032. https://doi.org/10.1016/j.clpl.2023.100032

Berger, K, Schöggl, J.-P, & Baumgartner, R. J. (2022). Digital battery passports to enable circular and sustainable value chains: Conceptualization and use cases. *Journal of Cleaner Production*, 353, 131492. https://doi.org/10.1016/j.jclepro.2022.131492

Ducuing, C, & Reich, R. H. (2023). Data governance: Digital product passports as a case study. *Competition and Regulation in Network Industries*, 24(1), 3–23. https://doi.org/10.1177/17835917231152799

European Commission. (2023). *Regulation (EU) 2023/1542 of the European Parliament and of the Council of 12 July 2023 concerning batteries and waste batteries, amending Directive 2008/98/EC and Regulation (EU) 2019/1020 and repealing Directive 2006/66/EC*. EUR-Lex. https://eur-lex.europa.eu/eli/reg/2023/1542/oj

Fetter, J, Rao, K, & Eaves, D. (2025). *2025 State of digital public infrastructure report: A look at measurement and prevalence as DPI transitions from experiment to scale*. UCL Institute for Innovation and Public Purpose. https://www.ucl.ac.uk/bartlett/publications/2025/nov/2025-state-digital-public-infrastructure-report

Gupta, U. (2024, October 17). BatX Energies partners LW3 on battery passports. *PV Magazine India*. https://www.pv-magazine-india.com/2024/10/17/batx-energies-partners-lw3-on-battery-passports/

Government of India. (2023, August 11). *The Digital Personal Data Protection Act, 2023* (No. 22 of 2023). Ministry of Law and Justice. https://www.meity.gov.in/static/uploads/2024/06/2bff0e9f04e6fb4f8fef35e82c42aa5.pdf

International Energy Agency (IEA). (2023). *Global EV Outlook 2023*. IEA, Paris. https://www.iea.org/reports/global-ev-outlook-2023

King, M. R, Timms, P. D, & Mountney, S. (2023). A proposed universal definition of a Digital Product Passport Ecosystem (DPPE): Worldviews, discrete capabilities, stakeholder requirements and concerns. *Journal of Cleaner Production*, 384, 135538. https://doi.org/10.1016/j.jclepro.2022.135538

Kumar, P, Sahoo, M, Meshram, A, & Mudholkar, L. (2024). *Battery circularity in India: Policy, regulations, and implementation strategies*. WRI India. https://wri-india.org/research/battery-circularity-india-policy-regulations-and-implementation-strategies

Kumar, S, Meena, S, & Aggarwal, R. (2025, January 2). Revolutionizing digital commerce: The ONDC initiative. Press Information Bureau, Government of India. https://pib.gov.in/PressReleaseFramePage.aspx?PRID=2090097

Battery Aadhaar for India | 9

Kwak, J., & Kang, Y. (2025). From standard to strategy: Digital battery passports building sustainability paradigm of global supply chains. SSRN. https://doi.org/10.2139/ssrn.5346556

Langley, D. J., Rosca, E., Angelopoulos, M., Kamminga, O., & Hooijer, C. (2023). Orchestrating a smart circular economy: Guiding principles for digital product passports. Journal of Business Research, 169, 114259. https://doi.org/10.1016/j.jbusres.2023.114259

Lambha, R., & Kamath, N. (2024, January 29). How data transparency & battery twin can help boost EV adoption in India. EV Reporter. https://evreporter.com/how-data-transparency-battery-digital-twin-can-help-boost-ev-adoption-in-india/

Ministry of Economy, Trade and Industry (METI), Japan. (2001). Act on the Promotion of Effective Utilization of Resources (Act No. 113 of 2000, enforced April 1, 2001). Government of Japan. https://www.japaneselawtranslation.go.jp/en/laws/view/3819/en

Ministry of Land, Infrastructure, Transport and Tourism (MOLIT), South Korea. (2025). Amendment to the Motor Vehicle Management Act introducing unique identification number (UIN)-based tracking for EV batteries. Government of the Republic of Korea.

Ministry of Road Transport and Highways. (2025, December 30). Draft Guidelines for implementation of Battery Pack Aadhaar System. Government of India. https://www.psa.gov.in/CMS/web/sites/default/files/publication/Battery%20Pack%20Aadhaar%20Guideline.pdf

Mukherjee, A., & Joshi, A. (2025). Digital public infrastructure as a catalyst for private sector innovation: Lessons from the fintech sector in India (Background Paper No. 29). ORF America. https://orfamerica.org/newresearch/dpi-catalyst-private-sector-innovation

NITI Aayog & Green Growth Equity Fund Technical Cooperation Facility. (2022). Advanced chemistry cell battery reuse and recycling market in India. https://www.niti.gov.in/sites/default/files/2022-07/ACC-battery-reuse-and-recycling-market-in-India_Niti-Aayog_UK.pdf

Office of the Principal Scientific Advisor to the Government of India. (2024). eMobility R&D roadmap for India. https://www.psa.gov.in/CMS/web/sites/default/files/psa_custom_files/Printing%20Updated%20eMobility%20R%26D%20Roadmap%20document_11072024.pdf

Rizos, V., & Urban, P. (2024). Barriers and policy challenges in developing circularity approaches in the EU battery sector: An assessment. Resources, Conservation and Recycling, 209, 107800. https://doi.org/10.1016/j.resconrec.2024.107800

Tata Elxsi. (2025, January 21). Tata Elxsi and Minespider partner to launch MOBIUS+ for battery lifecycle traceability. https://www.tataelxsi.com/news-and-events/news/tata-elxsi-and-minespider-partner-to-launch-mobius-for-battery-lifecycle-traceability

10 | WRI-INDIA.ORG

Expert Note

THIS PAGE IS INTENTIONALLY LEFT BLANK

Battery Aadhaar for India | 11

## Acknowledgments

The authors would like to thank WRI India colleagues Deepak Krishnan, Sneha Malhotra, Prashanth Varanasi, Anjali Singh, and Pawan Mulukutla for their insightful suggestions that helped improve this note. Additionally, we express our gratitude to Ke Wang from the WRI Global Energy Program for her valuable inputs.

## For more information

**Dr. Parveen Kumar** is the Program Head – Sustainable Batteries with the Sustainable Cities & Transport program at WRI India.
Contact: Parveen.Kumar@wri.org

**Chaitanya Kanuri** is the Program Director – Electric Mobility & Batteries with the Sustainable Cities & Transport program at WRI India.
Contact: chaitanya.kanuri@wri.org

## About WRI India

WRI India, an independent knowledge organisation registered as India Resources Trust, provides objective information and practical proposals to foster environmentally sound and socially equitable development. Through research, analysis, and recommendations, WRI India puts ideas into action to build transformative solutions to protect the earth, promote livelihoods, and enhance human well-being.

Know more: wri-india.org

creative commons

Copyright 2026 WRI India. This work is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-nd/4.0/

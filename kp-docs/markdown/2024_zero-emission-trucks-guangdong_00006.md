---
doc_id: 2024_zero-emission-trucks-guangdong_00006
source_pdf: kp-docs/CN-KPs-PDF/2024_zero-emission-trucks-guangdong_00006.pdf
extraction_method: postgres-full-text
parse_backend: mistral
parse_model: mistral-ocr-latest
char_count: 173901
title: 新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例
title_en: "Techno-Economic Feasibility Analysis of Zero-Emission Trucks in Urban and Regional Delivery Use Cases: A Case Study of Guangdong Province, China"
authors: Chen, Ke; Xue, Xuelu
year_published: 2024
article_type: Report
wri_primary_office: WRI China
language: zh
doi: 10.46830/wrirpt.24.00006
status: needs_review
---

WRI CHINA

# 新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

TECHNO-ECONOMIC FEASIBILITY ANALYSIS  
OF ZERO-EMISSION TRUCKS IN URBAN AND  
REGIONAL DELIVERY USE CASES: A CASE STUDY  
OF GUANGDONG PROVINCE, CHINA

陈轲 薛雪露

WRI.ORG.CN

## 致谢

本研究是国家自主贡献亚洲交通倡议项目 (NDC Transport Initiative for Asia, NDC-TIA) 的产出。该项目支持中国、印度、越南以及全球各国全面开展交通减排战略研究，提升交通低碳发展的雄心。国家自主贡献亚洲交通倡议项目是国际气候倡议 (IKI) 的一部分。德国联邦经济和气候保护部 (BMWK) 根据德国联邦议院决议，为国际气候倡议提供支持。该项目中国部分实施方包括德国国际合作机构 (GIZ)、国际清洁交通委员会 (ICCT) 和世界资源研究所 (WRI)，项目也得到德国交通转型智库 (AGORA) 在德国的支持。欲了解更多项目信息，请访问项目网站 https://www.ndctransportinitiativeforasia.org/。

作者感谢有关机构和专家为本研究提供的支持和意见，感谢深圳市协力新能源与智能网联汽车创新中心、佛山环境与能源研究院对本研究调研的大力支持。

另外，作者也感谢为本报告的撰写提供了宝贵专业建议的专家和同事 (排名不分先后)：

|  任焕焕 | 中国汽车技术研究中心有限公司  |
| --- | --- |
|  郝春晓 | 中国环境科学研究院机动车排污监控中心  |
|  谢海明 | 深圳市协力新能源与智能网联汽车创新中心  |
|  林镇宏 | 华南理工大学  |
|  Matteo Craglia | 国际运输论坛  |
|  Owen MacDonnell | CALSTART  |
|  Elizabeth Connelly | 国际能源署  |
|  张秀丽 | Energy Innovation  |
|  赵 曦 | 世界银行  |
|  Stephanie Ly | 世界资源研究所  |
|  Pawan Mulukutla | 世界资源研究所  |
|  Sharvari Patki | 世界资源研究所  |
|  Cristina Albuquerque | 世界资源研究所  |
|  周伟琪 | 世界资源研究所  |
|  张黛阳 | 世界资源研究所  |

上述专家的审阅并不代表完全认同本报告内容，对于本报告中的任何错误疏漏，皆由作者承担相关责任。

感谢世界资源研究所方莉博士、刘哲博士、苗红、Adriana Kocomik-Mina、Anne Maassen对报告提供的中肯意见和专业指导。

支持机构：

Federal Ministry
for Economic Affairs
and Climate Action

INTERNATIONAL
CLIMATE
INITIATIVE

on the basis of a decision
by the German Bundestag

引用建议：

陈轲、薛露露. 2024. 新能源货车在城市运输和区域运输场景中的技术与经济可行性分析：以中国广东省为例. 世界资源研究所研究报告. https://doi.org/10.46830/wrirpt.24.00006

校对 | 谢亮 hippie@163.com

设计与排版 | 张烨 harryzy5204@gmail.com

# 目录

V 执行摘要

XVII Executive Summary

1 引言

5 研究方法

6 运输场景的定义

9 新能源货车关键零部件参数设置方法

14 新能源货车购置成本的计算方法

16 新能源货车 TCO 的计算方法

21 研究结果

21 2022 年各场景结果

26 MY2022—MY2030 各场景结果

30 本文结论的适用性

59 结论与建议

63 附录 A. 广东省部分城市新能源货车优先路权政策

64 附录 B. 本研究开展的调研说明

65 缩略词

66 注释

67 参考文献

75 关于作者

# 图目录

|  图 1 | 运输企业新能源货车购置决策变量与影响决策变量的四项措施之间的关系 | 5  |
| --- | --- | --- |
|  图 2 | 本文与现有文献对MY2030纯电动货车与氢燃料电池货车能量消耗量的预测 | 10  |
|  图 3 | 本文针对新能源货车关键零部件质量与成本的假设及数据来源 | 15  |
|  图 4 | 2022年4.5吨轻型普通货车的TCO：深圳市和佛山市城市运输场景 | 24  |
|  图 5 | 2022年31吨氢燃料电池自卸汽车的TCO：深圳市、佛山市和北京市大兴区城市运输场景 | 25  |
|  图 6 | 2022年42吨半挂牵引车的TCO：深圳市与中国其他城市港口内运输场景 | 25  |
|  图 7 | 纯电动半挂牵引车BET200在集疏港运输场景的不同运营与充电方案 | 26  |
|  图 8 | MY 2025和MY2030纯电动货车的电池容量 | 27  |
|  图 9 | MY2025和MY2030纯电动货车相较燃油货车的载质量损失 | 29  |
|  图 10 | MY2025和MY2030氢燃料电池货车的车载储氢系统容量 | 30  |
|  图 11 | MY2025和MY2030氢燃料电池货车与燃油货车载质量损失 | 32  |
|  图 12 | MY2022—MY2030不同运输场景新能源货车的直接制造成本 | 33  |
|  图 13 | 部分场景下MY2025新能源货车与燃油货车的购置成本差异 | 35  |
|  图 14 | 部分场景下MY2030新能源货车与燃油货车购置成本差异 | 35  |
|  图 15 | 无政策激励时，不同运输场景新能源货车实现与燃油货车TCO平价的年份 | 37  |
|  图 16 | MY2025和MY2030部分场景下纯电动货车与氢燃料电池货车的TCO构成 | 38  |
|  图 17 | MY 2025新能源货车与燃油货车TCO差价与能效比的敏感性分析：以42吨半挂牵引车为例 | 41  |
|  图 18 | 部分运输场景纯电动货车与燃油货车实现TCO平价年份与能源价格敏感性分析 | 42  |
|  图 19 | 部分运输场景氢燃料电池货车（纯氢模式）与燃油货车实现TCO平价年份与能源价格敏感性分析 | 44  |
|  图 20 | MY2025纯电动货车与燃油货车各成本要素的差价 | 46  |
|  图 21 | 部分运输场景中技术进步对MY2022—MY2030新能源货车TCO下降的贡献 | 47  |
|  图 22 | 八项政策下新能源货车实现与燃油货车TCO平价的年份 | 53  |
|  图 23 | 深圳市和唐山市集疏港运输场景中新能源半挂牵引车与柴油半挂牵引车实现TCO平价年份的对比 | 57  |

II

WRI.org.cn

# 表目录

|  表 1 | 中国新能源货车推广的国家政策及地方（深圳市和佛山市）政策 | 3  |
| --- | --- | --- |
|  表 2 | 2022年货车车型分类及各车型在深圳市和佛山市货车保有量中的占比 | 6  |
|  表 3 | 本文中深圳市、佛山市的典型行驶工况说明 | 7  |
|  表 4 | 2019年中国及主要地区不同货类的货运量占比 | 8  |
|  表 5 | 本文覆盖的典型运输场景及说明 | 8  |
|  表 6 | 本文中不同运输场景纯电动货车与氢燃料电池货车的能效比 | 11  |
|  表 7 | 本文针对新能源货车关键零部件质量与成本的假设及数据来源 | 12  |
|  表 8 | 本文及现有文献中涉及的新能源货车TCO成本要素 | 16  |
|  表 9 | 本文中燃油货车、纯电动货车与氢燃料电池货车的维保成本、保险成本及相关税费说明 | 18  |
|  表 10 | 广东省燃油货车、纯电动货车和氢燃料电池货车的高速收费 | 19  |
|  表 11 | 2022年新能源货车的技术参数 | 22  |
|  表 12 | 2022年政策激励下新能源货车与燃油货车的TCO差价 | 23  |
|  表 13 | 为弥合新能源货车与燃油货车TCO差价，政府与行业可考虑采取的措施 | 50  |
|  附表 A-1 | 广东省部分城市新能源货车优先路权政策 | 63  |
|  附表 B-1 | 本研究开展的调研说明 | 64  |

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

III

T

# 执行摘要

## 亮点

- 为加速新能源货车的推广，特别是在小微运输企业的推广应用，本文以广东省典型城市（深圳市与佛山市）为例，分析2022—2030年新能源货车在城市运输与区域运输场景中的技术与经济可行性。
- 研究结果显示，如果无政策激励，本文分析的集疏港运输、港口内运输与城市运输场景中，纯电动半挂牵引车有望在车型年份（Model Year，以下简称MY）2025之前，与燃油货车实现总拥有成本（Total cost of ownership，以下简称TCO）的平价，成为近期最具电动化潜力的场景与车型。在区域运输场景中，新能源货车与燃油货车实现TCO平价时间更晚。但上述结论受能源价格、电池包价格等影响较大。
- 相较无政策激励的情况，在本文假设的政策组合下，多数场景中，纯电动货车与燃油货车实现TCO平价的时间有望提前到MY2025之前，早于氢燃料电池货车。
- 除政策激励以外，在集疏港运输等场景下，运输企业还可通过选择小电池容量的纯电动半挂牵引车，提高车辆年运营里程，加速实现纯电动货车与燃油货车的TCO平价。为支持小容量电池，相关企业应部署足够数量的快充基础设施，保障充足的停车位与电网容量，运营企业也需对运营做出优化（包括提高车辆年运营里程）。
- 尽管在多数场景中，新能源货车有望在MY2030之前与燃油货车实现TCO平价，但新能源货车的购置成本在MY2022—MY2030期间仍高于燃油货车。因而，有必要考虑推广新能源货车租赁、车电分离等商业模式，降低新能源货车初期购买时的一次性费用。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

V

## 研究问题

新能源货车推广对降低交通领域碳排放与空气污染物排放都发挥着重要的作用（Xue and Liu 2022）。与公交车和私家车不同，中国的货运行业主要依赖于小微运输企业（TUC 2022a），所以，未来新能源货车的推广应关注需求侧对成本更敏感、对新能源货车技术了解有限的小微运输企业。

运输企业在决定是否购买新能源货车时，通常考虑三个维度：一是新能源货车在运营中能否克服续航里程不足或载质量损失等问题；二是新能源货车的购置成本（即车辆市场售价）与初期购买时的一次性费用支出（包括购置成本、税费与融资成本等）是否可负担；三是新能源货车是否能够实现与同类型燃油货车的TCO平价（Tol et al. 2022）。

因此，本文从上述影响运输企业购置新能源货车决策的变量出发，试图回答以下问题：一是目前城市运输与区域运输场景下，新能源货车在技术与成本上面临哪些挑战？二是近期应重点在哪些运输场景推广新能源货车？这些运输场景适宜采取哪种新能源技术路线？三是政府与企业应采取哪些措施——包括政策激励、技术进步、商业模式推广与运营优化，才能解决新能源货车的技术与成本挑战？

## 研究方法

为回答这些问题，本研究以中国新能源货车推广先进地区——广东省深圳市与佛山市——为研究对象，定量分析了2022—2030年新能源货车（本文仅考虑纯电动货车与氢燃料电池货车²）在城市运输与区域运输场景中的技术与经济可行性。

考虑新能源货车在不同运输场景中的技术与成本差异性，本文根据货车车型、行驶工况、货物类型，将两个城市的城市运输与区域运输场景细分成14个场景，包括：

- 货车车型：微面中面、4.5吨轻型普通货车、18吨载货汽车、31吨自卸汽车和42吨半挂牵引车。
- 行驶工况：城市运输（urban delivery, 以下或简称UD）、港口内运输（port operation, 以下或简称PO）、集疏港运输（drayage duty cycle, 以下或简称DDC）、区域运输（regional delivery, 以下或简称RD, 不含集疏港运输）。
- 货物类型：轻抛货、重货。

本文对新能源货车在不同场景下技术和经济可行性的分析，主要围绕小微运输企业在新能源货车购置决策中所考虑的三个变量展开（Hunter et al. 2021; Tol et al. 2022）：

![img-0.jpeg](img-0.jpeg)

- ■ 新能源货车的技术与运营可行性：本文分别分析现状新能源货车技术可行性，以及未来如何通过设置新能源货车关键零部件的参数（如电池包额定容量、电机峰值功率等），满足MY2022—MY2030期间不同运输场景差异化的运营要求。
- ■ 新能源货车购置成本：本文基于关键零部件（如电池包、电驱动系统、燃料电池系统和储氢瓶等）的现状与未来预测成本，“自下而上”地计算新能源货车MY2022—MY2030的购置成本。其中，新能源货车关键零部件成本预测主要基于各零部件的学习曲线（Yelle 1979）（即随着各零部件累计产量的增长，其单位生产成本相应下降）。基于文献与行业预测，本文进一步验证并调整关键零部件与车辆购置成本的预测结果。
- ■ 新能源货车与燃油货车的TCO差异：本文所指的TCO包括车辆的购置成本、运营成本、维保成本、关键零部件（如电池包）更换成本，以及新能源货车因载质量损失产生的机会成本。由于数据可得性限制，本文未考虑因补能时长产生的额外成本以及车辆残值。基于不同场景新能源货车与燃油货车实现TCO平价的年份预测，本文识别了近期具备新能源货车推广潜力的场景，并分析不同措施——包括政策激励、技术进步、商业模式推广与运营优化——对新能源货车提前实现与燃油货车的TCO平价所发挥的作用。此外，本文也通过案例分析，说明本研究的结论对于中国其他区域的适用性，并讨论本文分析方法的局限性、结果的不确定性与未来调整方向。

## 研究结果

一、即便无政策激励，港口内运输、集疏港运输和城市运输场景中，新能源货车有望在MY2027之前实现与燃油货车的TCO平价，早于区域运输场景中新能源货车的TCO平价时间。

1. 无政策激励时，港口内运输、集疏港运输和城市运输场景中，纯电动货车（除自卸汽车外）将于MY2027之前实现与燃油货车的TCO平价，早于氢燃料电池货车的TCO平价时间。这些场景中，纯电动货车能够较早实现TCO平价的原因是：纯电动货车在这些场景中需要频繁启停和怠速，实现比燃油货车更低的能量消耗量。具体结果如下：

- ■ 在港口内运输、集疏港运输和城市运输场景中，42吨纯电动半挂牵引车在MY2025之前，有望实现与燃油货车的TCO平价，成为近期最具电动化潜力的场景。此处，本文假设深圳市与佛山市的42吨半挂牵引车主要运输轻拋货，不存在新能源货车载质量损失导致

![img-1.jpeg](img-1.jpeg)

较高TCO的问题。值得指出的是，在集疏港运输场景中，若纯电动半挂牵引车与柴油货车在MY2025之前实现TCO平价，运输企业需要协同纯电动半挂牵引车的参数配置、充电基础设施规划与车辆运营，包括为纯电动半挂牵引车配置更小容量的电池包、部署相应数量的快充基础设施、协调纯电动半挂牵引车的运营与充电时间（如在装卸货等待时间、进港等待时间或司机休息时间进行日间补电）、提高纯电动半挂牵引车的年运营里程。

- ■ 在城市运输场景中，4.5吨纯电动轻型普通货车与18吨纯电动载货汽车有望在MY2027之前实现与燃油货车的TCO平价。其中，在运输轻拋货时，这些纯电动货车在近期（即MY2022—MY2023）就能实现与燃油货车的TCO平价；但在运输重货时，由于受到新能源货车载质量损失的影响，这些纯电动货车的TCO平价时间将推迟至MY2025—MY2027。
- ■ 31吨纯电动自卸汽车存在突出的载质量损失问题，相较同场景的其他车型，更晚才能实现与燃油货车的TCO平价（在MY2029左右）。

相较之下，在区域运输场景中，新能源货车与燃油货车实现TCO平价的时间比城市运输、港口内运输与集疏港运输场景更晚，在MY2028—MY2030左右。其中，氢燃料电池货车是具备TCO竞争力的新能源货车技术——其与燃油货车实现TCO平价的时间比纯电动货车更早。其原因是燃油货车在高速工况的能量消耗量比城市工况更低；相反，纯电动货车在高速工况上的能量消耗量比城市工况更高，因此，纯电动货车在区域运输场景中（以高速工况为主）的能效优势较小。但值得注意的是，受数据限制，本文未区分氢燃料电池货车在城市与高速工况的能量消耗量，因此，可能给予氢燃料电池货车在区域运输中更大的能效与成本优势。无政策激励时，不同运输场景新能源货车实现与燃油货车TCO平价的年份如图ES-1所示。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

VII

# 图 ES-1 | 无政策激励时, 不同运输场景新能源货车实现与燃油货车TCO平价的年份

● BET ▲ FCET (混合) ● FCET (纯氢)

|  货车车型 | 行驶工况 | 货物类型 | 日行驶里程 (千米) | 2022 | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 | 2030年后  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  4.5 吨 轻型 普通 货车 | UD | 轻抛货 | 200 | ● |  |  |  |  |  |  |  |  | ▲●  |
|   |   |   |  300 | ● |  |  |  |  |  |  | ▲ | ● |   |
|   |   |  重货 | 200 |  |  |  | ● |  |  |  |  |  | ▲●  |
|   |   |   |  300 |  |  |  |  |  | ● |  |  | ▲● |   |
|   |  RD | 轻抛货 | 300 |  |  |  |  | ● |  |  |  | ▲ | ●  |
|   |   |   |  400 |  |  |  |  | ● |  |  | ▲ | ● |   |
|   |   |   |  500 |  |  |  |  | ● |  | ▲ | ● |  |   |
|   |   |  重货 | 300 |  |  |  |  |  |  |  |  |  | ●▲●  |
|   |   |   |  400 |  |  |  |  |  |  |  |  | ▲● | ●  |
|   |   |   |  500 |  |  |  |  |  |  |  | ▲ | ● | ●  |
|  18 吨 载货 汽车 | UD | 轻抛货 | 200 |  | ● |  |  |  |  |  |  |  | ▲●  |
|   |   |   |  300 |  | ● |  |  |  |  |  | ▲● |  |   |
|   |   |  重货 | 200 |  |  |  | ● |  |  |  | ▲ | ● |   |
|   |   |   |  300 |  |  |  | ● |  | ▲ | ● |  |  |   |
|   |  RD | 轻抛货 | 300 |  |  |  |  |  |  |  |  | ▲● | ●  |
|   |   |   |  400 |  |  |  |  |  |  |  | ▲● | ● |   |
|   |   |   |  500 |  |  |  |  |  |  | ▲ | ● | ● |   |
|   |   |  重货 | 300 |  |  |  |  |  |  |  | ▲● |  | ●  |
|   |   |   |  400 |  |  |  |  |  |  | ▲● |  |  | ●  |
|   |   |   |  500 |  |  |  |  |  | ▲ | ● |  |  | ●  |
|  31 吨自卸 汽车 | UD | 重货 | 200 |  |  |  |  |  |  |  | ● |  | ▲●  |
|   |   |   |  300 |  |  |  |  |  |  |  | ▲ | ●● |   |
|  42 吨 半挂 牵引车 | PO_TRIP | 轻抛货 | 200 | ● |  |  |  |  |  |  |  |  |   |
|   |   |   |  300 | ● |  |  |  |  |  |  |  |  |   |
|   |  PO_DVKT |   | 200 | ● |  |  |  | ▲ | ● |  |  |  |   |
|   |   |   |  300 | ● |  |  | ▲ | ● |  |  |  |  |   |
|   |  DDC_TRIP |   | 200 |  |  |  |  |  |  |  |  |  | ●  |
|   |   |   |  300 |  |  |  | ● |  |  |  |  |  |   |
|   |   |   |  400 | ● |  |  |  |  |  |  |  |  |   |
|   |   |   |  500 |  |  |  | ● |  |  |  |  |  |   |
|   |  DDC_DVKT |   | 200 |  |  |  |  |  |  |  |  |  | ●▲●  |
|   |   |   |  300 |  |  |  |  |  |  |  |  | ▲● | ●  |
|   |   |   |  400 |  |  |  |  |  |  |  | ▲● |  | ●  |
|   |   |   |  500 |  |  |  |  |  |  | ▲ | ● |  | ●  |
|   |  UD |   | 200 |  |  | ● |  |  |  |  | ▲ | ● |   |
|   |   |   |  300 |  | ● |  |  |  |  | ▲● |  |  |   |
|   |  RD |   | 300 |  |  |  |  |  |  |  |  | ▲● | ●  |
|   |   |   |  400 |  |  |  |  |  |  |  | ▲● |  | ●  |
|   |   |   |  500 |  |  |  |  |  |  | ▲ | ● |  | ●  |

说明: 基于 Pers.Comm. (2023a), 本文假设 31 吨自卸汽车的使用年限为五年, 而其他车型的使用年限为六年。

缩略词: TDD= 总拥有成本; BET= 纯电动货车; FCET= 氢燃料电动货车; K2V= 燃油汽车; 混合= 链电式混合动力模式; 纯氢= 纯氢模式; UD= 城市运输; RD= 区域运输; PO_TRIP= 港口内运输 (“单程运输”法); PO_DVKT= 港口内运输 (“日行驶里程”法); DDC_TRIP= 集疏港运输 (“单程运输”法); DDC_DVKT= 集疏港运输 (“日行驶里程”法)。

来源: 作者计算。

VIII

WRI.org.cn

## 2. 能源价格对新能源货车实现与燃油货车TCO平价的时间有较大影响。

上述新能源货车与燃油货车实现TCO平价时间的结论，建立在特定的能源价格前提下，包括2022—2030年，柴油价格维持在2022年8.1元/升的年均水平，充电价格（含电价与充电服务费）维持在1.2元/千瓦时的水平，氢气价格则从2022年的55元/千克线性下降至2030年的30元/千克。

然而，如果未来能源价格发生任何波动，上述新能源货车的TCO平价年份也将发生变化。例如，如果未来柴油价格降至2019年平均水平（即6.5元/升），而充电价格上升至1.4元/千瓦时，集疏港运输场景与城市运输场景中，42吨纯电动半挂牵引车与18吨纯电动载货汽车与燃油货车实现TCO平价的时间将推迟至MY2030左右。类似地，如果柴油价格降至2019年平均水平（即6.5元/升），即便氢气价格保持不变，区域运输场景中，氢燃料电池货车也无法在MY2030之前与燃油货车实现TCO平价。

因此，如果未来燃油价格下降，有关部门有必要考虑取消现行燃油补贴（Black et al. 2023），增加燃油税（OECD 2022），提供新能源货车充电或加氢补贴，以维持新能源货车的TCO成本竞争力。如果2030年氢气价格高于30元/千克，有必要在上述措施基础上考虑提供氢燃料电池货车加氢补贴。

二、采取本文假设的政策组合，新能源货车在多数场景中将提前与燃油货车实现TCO平价；同时，这些政策组合对缩短纯电动货车的TCO平价时间更为有效。本文分析的政策组合是可量化的（国家和地方）政策，包括：新能源货车购置补贴（仅针对氢燃料电池货车）、税费减免、能源（充电与加氢）补贴、碳价、新能源货车优先路权、减免新能源货车高速收费、提高新能源货车最大设计总质量，以及降低新能源货车融资成本（即给予新能源货车更优惠的贷款利率）。

1. 与单项政策相比，在本文的政策组合下，新能源货车能更快实现与燃油货车的TCO平价。多数场景中，纯电动货车在MY2025之前就能实现与燃油货车的TCO平价，比无政策激励的情况提前0~9年。相较之下，氢燃料电池货车与燃油货车的TCO平价时间提前幅度有限；即便提供比纯电动货车更多的补贴，氢燃料电池货车与燃油货车实现TCO平价的时间也只能在MY2028之前，比无政策激励的情况仅提前3~6年。在多数场景中，纯电动货车实现TCO平价的时间比氢燃料电池货车要早0~6年，成为政策激励下最有成本竞争力的新能源技术选项。

2. 本文中假设的新能源货车税费减免、能源（充电与加氢）补贴、优先路权、减免高速收费、降低融资成本与提高最大设计总质量等政策，都有助于降低新能源货车的TCO。鉴于中国目前的碳价较低，只有碳价政策对缩短新能源货车与燃油货车TCO平价时间的作用有限。

各项政策对降低新能源货车TCO的作用与运输场景相关，具体如下：

- 本文中假设的新能源货车购置税、车船税减免与能源（充电与加氢）补贴政策，对弥合新能源货车与燃油货车的TCO之差有显著作用，且这些政策适用于多数运输场景；
- 新能源货车优先路权政策对区域运输、集疏港运输场景更有效。这是因为本文假设优先路权政策有助于减少新能源货车的绕行，进而降低其行驶里程。由于区域运输、集疏港运输这两个场景中的车辆行驶里程都较长，因此，优先路权政策更有效；
- 减免新能源货车高速收费，对区域运输和集疏港运输场景中，降低42吨半挂牵引车TCO有更好的效果。这是因为42吨半挂牵引车在这两个场景中的高速行驶里程占总里程的比例较大，且因轴数较多，单位里程的高速收费更高；
- 提高新能源货车最大设计总质量政策（即给予新能源货车的车货总重一定程度的豁免）能够有效降低新能源货车在重货运输场景下的TCO；
- 降低新能源货车融资成本（即给予新能源货车更优惠的贷款利率）有助于城市运输场景下缩短新能源货车实现与燃油货车TCO平价的时间。

3. 对氢燃料电池货车，在本文假设的所有政策中，购置补贴对降低其TCO最为有效。但有关部门应避免购置补贴导致的货车运力过剩问题。在本文假设的氢燃料电池货车购置补贴政策下，所有场景中的氢燃料电池货车都将有望在MY2026—MY2030实现与燃油货车的TCO平价，最多比无政策激励的情况提前2年。值得注意的是，若政府提供大量购置补贴刺激新车销售，可能扰乱货车运力供给，降低新能源货车的成本竞争力（Pers. Comm. 2023a）。因此，政府应避免提供高额购车补贴，而应考虑置换补贴或其他非补贴措施（如新能源货车优先路权政策）。

八项政策下新能源货车实现与燃油货车TCO平价的年份如图ES-2所示。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

IX

图 ES-2 | 八项政策下新能源货车实现与燃油货车TCO平价的年份

a. 18 吨载货汽车

![img-2.jpeg](img-2.jpeg)

X

WRI.org.cn

图 ES-2 | 八项政策下新能源货车实现与燃油货车TCO平价的年份(续)

# b. 31 吨自卸汽车

● 重货 - 200 千米 ● 重货 - 300 千米

![img-3.jpeg](img-3.jpeg)

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

XI

图 ES-2 | 八项政策下新能源货车实现与燃油货车TCO平价的年份(续)

# C.42 吨半挂牵引车

● 轻抛货 - 200 千米 ● 轻抛货 - 500 千米 ● 轻抛货 - 200 千米 ● 轻抛货 - 500 千米

![img-4.jpeg](img-4.jpeg)

说明：对于 42 吨半挂牵引车，DDC 表示纯电动货车的 DDC_TRF 场景和氢燃料电池货车的 DDC_DWT 场景。

缩略词：BET=纯电动货车；FCET=氢燃料电池货车；纯氢=纯氢模式；UD=城市运输；RD=区域运输；DDC=集疏港运输；DDC_TRF=集疏港运输（“单程运距”法）；DDC_DWT=集疏港运输（“日行使里程”法）。

来源：作者计算。

XII

WRI.org.cn

### 三、除政策激励外，技术进步、商业模式推广与运营优化对降低新能源货车TCO也同样重要。

#### 1. 创新商业模式（如新能源货车租赁模式）推广有助于降低新能源货车初期购买时的一次性费用。

尽管在多数运输场景中，新能源货车将在MY2030前实现与燃油货车的TCO平价，但其购置成本仍高于燃油货车。例如，本研究表明，到MY2030，新能源货车的购置成本仍比燃油货车高出53%~322%。

为减轻运输企业（特别是小微运输企业）新能源货车初期购买时的一次性费用，并将购置与持有风险分摊给适宜的主体（如新能源货车租赁企业及平台、主机厂、金融机构等），可考虑推广新能源货车经营性租赁等创新商业模式。

未来，如果在更多场景中推广新能源货车创新商业模式，政府部门与金融机构等应采取更多支持性的措施，包括但不限于：帮助租赁平台降低新能源货车贷款首付比例，提供贷款利率优惠并延长贷款期限，鼓励绿色金融或混合融资，为其租赁业务提供税收优惠与灵活折旧等，以及考虑为小微运输企业的租赁业务提供第一损失担保，

对冲相关风险等（Sankar et al. 2022; Kok et al. 2023; Coyne et al. 2023）。部分场景下MY2030新能源货车与燃油货车的购置成本差异如图ES-3所示。

#### 2. 在集疏港运输等场景下，运输企业可通过选择小容量电池、日间充电与运营优化等措施，降低纯电动货车的TCO。

由于集疏港运输场景中的起始点/目的地以及运营时刻表相对固定，车辆会定期返回港口（或港口附近停车场），并在相对较小的区域范围内运营，因而，具备条件的运输企业可选择电池容量较小的纯电动半挂牵引车，并部署足够多的快充基础设施，实现“一天多充”，从而降低纯电动货车购置成本与TCO。

为支持小容量电池的纯电动货车，相关企业需要对充电基础设施布局与运营分别进行优化，包括在运输的起始地/目的地、中途、工厂停车场与物流场站部署足够数量的快充基础设施，保障充足的停车位数量与电网容量（Kotz et al. 2022）；此外，运输企业也需要协调纯电动半挂牵引车的运营与充电时间（如利用装卸货等待时间、进港等待时间或司机休息时间进行日间补电），并提高纯电动半挂牵引车的运营效率（包括年运营里程）。

图 ES-3 | 部分场景下MY2030新能源货车与燃油货车购置成本差异

■ BET ■ FCET

#### a. 4.5吨轻型普通货车

![img-5.jpeg](img-5.jpeg)

#### b. 42吨半挂牵引车

![img-6.jpeg](img-6.jpeg)

说明：百分比表示新能源货车与同等燃油货车购置成本差异以燃油货车购置成本所得的值，即（BEV/CEV）/CEV。百分比为零，表示新能源货车购置成本与燃油货车相同。这里，购置成本不考虑任何政策影响，包括新能源货车购置补贴或燃油货车购置税对购置成本的影响。

缩略词：BET=纯电动货车；FCET=氢燃料电池货车；NEV=新能源汽车；ICEV=燃油汽车；UD=城市运输；RD=区域运输；PO_TRIP=港口内运输（“单程运输”法）；DDC_DVKT=集疏港运输（“日行便里程”法）；DDC_TRIP=集疏港运输（“单程运输”法）。

来源：作者计算。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

XIII

**3. 加快技术进步也有助于降低新能源货车的TCO。**未来，纯电动货车TCO下降将主要依靠电池成本下降、新能源货车能量消耗量改进以及载质量损失改善，氢燃料电池货车TCO下降将主要依靠燃料电池系统成本与氢气价格的下降。

**4. 设计广泛适用的纯电动货车。**不同场景下，纯电动货车所需电池容量的巨大差异，为主机厂生产纯电动货车以及运输企业采购适合的纯电动货车带来挑战，尤其是考虑到运输企业（特别是小微运输企业）通常需要跨场景运营的情况（TUC 2022b）。因此，主机厂有必要设计广泛适用的纯电动货车，以满足常见场景的大部分运营要求。为设计广泛适用的纯电动货车，建议有关部门收集目前在运营的燃油货车分车型、分场景的日行驶里程信息，并与主要的行业相关方（如主机厂）分享，用于车辆设计。

#### 四、以数据驱动，制定全面且精细化的新能源货车推广政策。

**1. 良好的货运统计数据基础，对新能源货车推广政策的制定有重要意义。**本文分析显示，未来新能源货车的能

量消耗量（包括新能源货车与燃油货车的能效比）对其实现TCO平价的时间有较大影响，因此，建议有关部门收集新能源货车不同场景、不同工况下的实际能量消耗量数据，并考虑出台针对新能源货车能量消耗量的标准。此外，目前在运营的燃油货车分场景的日/年行驶里程信息、道路流量信息、货车停车信息等数据，对识别近期适宜新能源货车推广的场景，规划充电/加氢基础设施、配置新能源货车参数都起到重要作用，因此，建议有关部门收集这些统计数据并与行业相关方分享，以支持精细化的政策制定与企业投资。

**2. 除新能源货车的运营可行性、购置成本与TCO外，现实中，运输企业在新能源货车购置决策过程中，也会衡量以下因素，包括：货主企业对使用新能源货车的要求、行业的盈利情况、新能源货车的安全性与可靠性、运输企业对新能源货车技术的认识水平（QTLC and MOV3MENT 2022）等。**因此，除本文涉及的政策组合以外，有关部门还应统筹考虑其他政策，包括针对货主企业的“重点行业大气污染防治绩效分级”政策、改善新能源货车残值的措施，以及组织宣传与试驾活动（特别是针对小微运输企业）等。

![img-7.jpeg](img-7.jpeg)

**五、本文的研究结论仅适用于与深圳市、佛山市具有近似特征的城市，包括使用相同货车车型、运输相同类型货物、在类似行驶工况和环境温度下行驶等。读者应谨慎将文中结论用于中国其他城市。**例如，本文分析显示，同为集疏港运输场景，唐山市49吨BET100半挂牵引车在MY2022就已实现与柴油半挂牵引车的TCO平价，比本文中深圳市42吨BET200半挂牵引车实现TCO平价的时间更早，如图ES-4所示。

图 ES-4 | 深圳市和唐山市集疏港运输场景中新能源半挂牵引车与柴油半挂牵引车实现TCO 平价年份的对比

| 货车车型 | 行驶工况 | 货物类型 | 日行驶里程 (千米) | 2022 | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 | 2030年后 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 49吨半挂牵引车 (唐山) | DDC_TRIP | 重货 | 200 |  |  |  | ● |  |  |  |  |  |  |
| 300 | ● |  |  |  |  |  |  |  |  |  |
| 400 | ● |  |  |  |  |  |  |  |  |  |
| 500 | ● |  |  |  |  |  |  |  |  |  |
| DDC_DVKT | 200 |  |  |  | ● |  |  |  |  | ▲● |  |  |
| 300 |  |  |  |  | ● |  |  |  | ▲● |  |  |
| 400 |  |  |  |  |  | ● |  |  | ▲● |  |  |
| 500 |  |  |  |  |  |  | ● |  | ▲● |  |  |
| 42吨半挂牵引车 (深圳) | DDC_TRIP | 轻抛货 | 200 |  |  |  |  |  |  |  |  |  | ● |
| 300 |  |  |  | ● |  |  |  |  |  |  |
| 400 | ● |  |  |  |  |  |  |  |  |  |
| 500 |  |  |  | ● |  |  |  |  |  |  |
| DDC_DVKT | 200 |  |  |  |  |  |  |  |  |  |  | ●▲● |
| 300 |  |  |  |  |  |  |  |  | ▲● | ● |  |
| 400 |  |  |  |  |  |  |  | ▲● |  | ● |  |
| 500 |  |  |  |  |  |  | ▲ | ● |  | ● |  |

说明：本文假设唐山市集疏港运输场景的单程运距为100千米，深圳市集疏港运输场景的单程运距为200千米。此外，MY2022唐山市49吨柴油半挂牵引车的能量消耗量为64升/100千米，而纯电动半挂牵引车的能量消耗量为230千瓦时/100千米，氢燃料电池半挂牵引车的能量消耗量为31千瓦/100千米。

缩略词：BET=纯电动货车；F2ET=氢燃料电池货车；混合=插电式混合动力模式；纯氢=纯氢模式；DDC_TRIP=集疏港运输（“单程运距”法）；DDC_DVKT=集疏港运输（“日行驶里程”法）。
来源：作者计算。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

XV

华穗路 广州大道中
Huaxia Rd Guangzhou Ave N
华夏路(南) 华夏路(北)
Huaxia Rd (S) Huaxia Rd (N)

# EXECUTIVE SUMMARY

## HIGHLIGHTS

- To tackle small fleet operators' concerns and accelerate zero-emission truck (ZET) adoption, we assessed the techno-economic feasibility of ZETs over the time frame of 2022-2030 across use cases in different model years (MYs) for Shenzhen and Foshan in Guangdong Province.
- The promotion of battery electric trucks (BET) in urban delivery, port operation, and drayage duty cycles should be prioritized because their total cost of ownership (TCO) parity with diesel trucks will be reached before MY2025, particularly with comprehensive policy incentives.
- Proposed comprehensive policies in this study are effective to move ZET TCO parity years with diesel trucks earlier than MY2025 in most use cases. BETs benefited more from the comprehensive policies in TCO parity year reduction than fuel-cell electric trucks (FCETs).
- Choosing BETs with smaller batteries, ensuring that charging facilities are sufficiently available, and adjusting operation schedules to allow for multiple within-day charges are important to reduce BETs' TCO.
- Gaps in purchase costs between ZETs and internal combustion engine vehicles (ICEVs) remain large by MY2030, although TCO parity is reached in most use cases. Therefore, financing mechanisms like leasing are essential to ease ZETs' up-front cost burdens.
- Given the day-to-day operational variability of small fleet operators, it is critical to design BETs to ensure operational flexibility, cost effectiveness, and mass production.

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

XVII

## About this report

To reduce carbon and air pollutant emissions, promoting ZETs—referring to battery electric trucks and fuel-cell electric trucks—is important (Xue and Liu 2022). Unlike buses and private cars, the trucking industry is dominated by small- and medium-sized enterprises (SMEs) in China (TUC 2022a). Currently, ZETs in Chinese cities were primarily adopted by large fleet operators that were less cost-sensitive. Now, to further promote ZETs, addressing the demand side, particularly more cost-conscious and less technology-savvy SMEs’ concerns, is critical for ZETs’ future uptake. From the demand perspective, small fleet operators are often concerned about the following issues related to ZET transition: (1) whether the operation of ZETs is technologically feasible where range constraints or payload loss can be avoided; (2) whether purchase cost gaps between ZETs and ICEVs are acceptably small; and (3) whether TCO parity with equivalent ICE trucks can be reached (Tol et al. 2022).

To tackle demand-side concerns and ramp up ZET adoption, it is important to understand the current operational and cost challenges of ZETs, what interventions are effective in overcoming the challenges, and which use case and zero-emission technology to prioritize and when.

To address the questions mentioned earlier, this study chooses one of China’s front-runner regions

of ZET transition, Guangdong Province, as an example. To reduce the data collection efforts, we choose the cities of Shenzhen and Foshan in Guangdong for in-depth analysis. The two cities are not only leading ZET transitions in Guangdong, but also set ambitious goals for ZET adoption.

We assessed the techno-economic feasibility of ZETs over the time frame of 2022–2030 across different use cases and MYs. The base year is set to 2022 where the most recent data are available. The analysis was carried out for 14 localized use cases:

- Five truck segments, including delivery vans, 4.5-t (ton) light-duty trucks (LDTs), 18-t straight trucks, 31-t dump trucks, and 42-t tractor trailers.
- Four duty cycles, namely, urban delivery (UD), regional delivery (RD), port operation (PO), and drayage duty cycles (DDC).
- Two types of goods transported, including light cargo and heavy cargo.

In this study, the techno-economic feasibility of ZETs is assessed in different use cases, based on three variables essential for small fleet operators to decide if ZET transition is feasible (Hunter et al. 2021; Tol et al. 2022):

- ZETs’ operational feasibility. In this study, operational feasibility is evaluated by the

![img-8.jpeg](img-8.jpeg)

sizes of key components for ZETs, including energy storage capacities, peak power outputs, and curb weights, to meet the ranges and wheel power demands in different use cases during MY2022 and MY2030. The resulting component sizing is useful to find the proper ZET models for the given use case that can come at a reasonable cost and meet the day-to-day operational requirements.

- Differences of purchase costs between ZETs and ICEVs. Here, ZETs' purchase costs are projected based on the technology progress of key components (such as battery packs, electric drives, fuel cell (FC) systems, and hydrogen storage tanks) characterized by the learning curve outlined by Yelle (1979) in which the reduction in unit costs of each key component is a function of accumulated production volumes. We further employed existing literature and market predictions to validate and adjust the projections.
- TCO gaps between ZETs and ICEVs. TCO was evaluated by adding up the capital, operation, and maintenance expenditure of the vehicles; the mid-life replacement costs of key components (such as battery packs); and the opportunity costs of the loss in ZETs' payload capacity. Due to limited data availability, costs such as vehicle residual values and refueling labor costs are not considered in this study.

The use cases with near-term opportunities for ZET transition are identified, based on ZETs' TCO parity years with ICEVs. Further, we evaluate the possible roles played by different interventions—including technological development, policy incentives, operational improvements, and business models—in affecting the previously mentioned decision variables and in accelerating the achievement or advances of TCO parity years relative to diesel trucks. Further, we used an example to illustrate if the conclusions could be applied to other cities and discussed the caveats and uncertainties of the analysis.

## Research findings

**A. Without ZET incentives, BET promotion in PO, DDC, and urban delivery (UD) could be prioritized, given that the TCO parity**

**with ICE trucks in these use cases will be reached earlier than other use cases.**

**1. BETs, except for dump trucks, have TCO cost advantages in PO, DDC, and UD in absence of ZET incentives.** In these use cases, BETs will reach TCO parity relative to ICEV counterparts before MY2027. This is because BETs are much more energy efficient than ICEVs in PO and UD by taking advantage of frequent stop-and-goes to recoup energies from regenerative braking. By contrast, battery electric dump trucks are less cost advantageous, because of the prominent payload loss issue. Particularly in two instances:

- Battery-electric 42-t tractor trailers in PO, DDC, and UD will reach TCO parity with diesel tractor trailers before MY2025, representing one of the most promising truck segments to be electrified at the moment. This is because: (1) BET tractor trailers in Shenzhen and Foshan mostly carry lightweight goods and (2) operational optimization measures taken by fleet operators in DDC—including using small battery capacities to fulfill the operation and matching BET configurations with charging facility availability—are helpful for BET to reach TCO parity early, relative to diesel trucks.
- Battery-electric 4.5-t LDTs and straight trucks in UD will reach TCO parity relative to their diesel counterparts by MY2027. Particularly, when carrying lightweight goods, both vehicle segments have achieved cost parity now (MY2022–2023), whereas when transporting heavy goods, the parity years will be postponed to MY2025–2027 after being penalized for the payload losses.

**By contrast, FCETs' TCO are lower than BETs in RD.** In RD, ZETs' TCO cost parity relative to ICEVs will be achieved around MY2028–2030, much later than UD. BETs are less cost advantageous in RD because: (1) ICEVs are relatively more energy-efficient for high-speed highway driving than urban driving; (2) for simplicity, this study does not differentiate FCETs' energy efficiency between UD and RD; therefore, we may have given FCETs more cost advantages in RD.

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

XIX

Figure ES-1 | ZET TCO parity relative to ICEVs for all use cases

![img-9.jpeg](img-9.jpeg)

![img-10.jpeg](img-10.jpeg)

Note: This study assumes that the useful life of the 31-t dump truck is five years and that of other vehicle segments are six years based on Pers. Comm. (2023a).

Abbreviations: TCO=total cost of ownership; BET=battery electric truck; FCET=fuel cell electric truck; ICEV=internal combustion engine vehicle;  \( H_{2} \) -only=hydrogen-only mode; hybrid=hybrid mode; VKT=vehicle kilometers traveled; UD=urban delivery; RD=regional delivery; PO_TRIP=port operation (using the trip distance method); PO_DVKT=port operation (using the daily VKT method); DDC_TRIP=drayage duty cycle (using the trip distance method); DDC_DVKT=drayage duty cycle (using the daily VKT method).

Source: WRI authors' calculation.

XX

WRI.org.cn

**2. Changes in energy prices will greatly affect ZETs' parity years with ICE trucks in some use cases.** The previously mentioned conclusion on TCO parity years is valid when the diesel price is at the 2022 level of 8.1 Chinese Yuan (CNY)/liter and the charging cost is fixed at 1.2 CNY/kWh. If diesel prices drop to the 2019 and 2021 average price of 6.5 CNY/L, and charging costs rises to 1.4 CNY/kWh and above (due to widespread adoption of ultra-fast chargers), battery electric trucks will achieve TCO parity with diesel trucks at a much later time for 42-t tractor trailers in DDC (parity year=~MY2030) and 18-t ton straight trucks in UD with light goods transportation (parity year=~MY2030). Similarly, for FCETs, if the diesel prices remain at the 2022 level, the break-even green hydrogen price in MY2030 is around 30 CNY/kg. However, if the diesel prices drop to the 2021 average price, FCETs are unlikely to achieve TCO parity with diesel trucks at any time before MY2030.

Therefore, **with lower diesel prices, removal of diesel subsidies (Black et al. 2023), increased taxes on diesel prices (OECD 2022), or alternative energy incentives (on electricity and hydrogen) should be considered**, to maintain the cost competitiveness of ZETs.

**B. Comprehensive policies are effective to move ZET TCO parity years with ICE trucks earlier, especially for BETs.** In this study, we focus on the comprehensive (national and local) policies the impacts of which on TCO can be quantified under this study's TCO methodology framework, including purchase subsidy, tax exemption, energy (electricity/hydrogen fuel) incentives, carbon pricing on conventional fuels, road access privileges, reduction of expressway road tolls, increases of maximum authorized weights of ZETs (also known as ZET weight allowance), and financing cost reductions.

**1. There is no silver bullet. Comprehensive policy incentives are more effective to bringing forward ZETs' TCO parity years to an earlier date than single measures.** BETs' TCO parity years benefit more from the proposed comprehensive policies in this study. Under the combination of the proposed policies in this

study (without a BET purchase subsidy), BETs will reach TCO parity with diesel counterparts in most use cases before MY2025, zero to nine years earlier than the case without policy incentives. By contrast, even with greater amounts of subsidies (including an FCET purchase subsidy), FCETs will reach TCO parity with diesel counterparts before MY2028, three to six years earlier than the case without policy incentives. Overall, with the eight proposed policy incentives, the TCO parity years of BETs are zero to six years earlier than FCETs in most use cases, making BETs the most cost-competitive ZET option.

**2. The impacts of policies on ZETs' TCO parity years and TCO reduction are use-case-specific.** ZETs benefit from the proposed policies of tax exemption, energy incentives, road access privileges, reduction of expressway road tolls, financing cost reduction, and increases of maximum authorized vehicle weights in this study in TCO reduction. The improvement in cost parity is not significant when applying the carbon pricing measure due to China's current low carbon prices. Specifically,

- the proposed purchase and ownership tax exemption and energy incentives are essential to bridge the TCO gaps between ZETs and ICEVs, for most use cases;
- road access privileges for ZETs are more effective in RD and DDC because we assume that the policy works on vehicle kilometers traveled (VKTs), and both use cases have long VKTs;
- the reduction of expressway road tolls is more influential for 42-ton tractor trailers' RD and DDC because the two use cases have large shares of VKTs on expressways and high toll rates;
- the ZET weight allowance is useful for heavy goods transportation; and
- the financing cost reduction is conducive to moving forward TCO parity years in UD.

**3. The FCET purchase subsidy analyzed in this study is found to be one of the most influential policy interventions for FCETs' TCO reduction; but governments**

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

XXI

should refrain from using large purchase subsidies to boost ZET adoption to avoid oversupply of truck capacities in the market. With the purchase subsidy assumed in this study, FCETs' time to TCO parity is reduced by zero to two years for all use cases, achieving TCO parity with its diesel counterpart by MY2026–2030. Of note, considering that large

public subsidies to promote ZETs would distort the market supply of truck capacities and reduce ZETs' cost competitiveness (Pers. Comm. 2023a), governments should refrain from using large purchase subsidies to stimulate ZET adoption. Instead, scrappage subsidies or other non-subsidy measures such as road access privileges offer viable alternatives.

Figure ES-2 | ZET TCO parity relative to ICEVs with policy incentives

a. 18-t straight truck

![img-11.jpeg](img-11.jpeg)

XXII

WRI.org.cn

Figure ES-2 | ZET TCO parity relative to ICEVs with policy incentives (cont.)

b. 31-t dump truck

![img-12.jpeg](img-12.jpeg)

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

XXIII

Figure ES-2 | ZET TCO parity relative to ICEVs with policy incentives (cont.)

c. 42-t tractor trailer

![img-13.jpeg](img-13.jpeg)

Note: For a 42-t tractor trailer, DDC denotes the DDC_TRIP use cases for BETs and the DDC_DVKT use cases for FCETs.

Source: WRI authors' calculation.

XXIV

WRI.org.cn

# **C. Apart from policies, financing mechanisms, operational optimization, and technology improvements are also essential to accelerate the adoption of ZETs.**

**1. Financing mechanisms are essential to ease ZETs' up-front purchase costs.** Although the TCO parity with ICE trucks is reached in most use cases by MY2030, tremendous gaps in purchase costs between ZETs and ICEVs remain. By MY2030, the purchase costs of ZETs are still 53 to 322 percent higher than those of ICEVs in all use cases examined by this study.

To ease fleet operators' burden on costly up-front expenses of ZETs—particularly for small fleet operators—and allocate the risks of ZET transition to appropriate stakeholders, it is necessary for private and public players to take actions, including reducing the minimum down payment requirements on ZET loans; encouraging ZET leasing or battery swapping; unlocking green

finance (through reduced interested rates and extended repayment terms) and blended finance for ZET financing; and providing tax benefits, flexible depreciation, or first loss guarantees for new business models.

**2. Operational optimization is a necessary measure to reduce costs and improve operational feasibility.** As in the case of DDC, choosing BETs with smaller batteries, ensuring charging facilities are sufficiently available, and adjusting operation schedules to allow BETs for more than one charge a day are important to reduce BETs' TCO.

For this type of operation to work, it is crucial to have: (1) broad availability of (ultra)-fast charging facilities, parking spaces, and grid capacities at the DDC's customer locations (Kotz et al. 2022); and (2) BETs' operation schedules that allow for sufficient charging time windows—for example, timing charging with loading (or unloading) of trucks or break times of drivers.

Figure ES-3 | Percentage differences in purchase costs between ZETs and ICEVs for MY2030

![img-14.jpeg](img-14.jpeg)

Note: The percentage represents the difference in the purchase costs between ZETs and comparable ICEVs divided by the purchase costs of ICEVs, that is, (ZET-ICEV)/ICEV. Zero percent indicates no difference between the purchase costs of ZETs and ICEVs. No purchase subsidy or tax is considered for the purchase costs.

Abbreviations: BET=battery electric truck; FCET=fuel cell electric truck; ICEV=internal combustion engine vehicle; VKT=vehicle kilometers traveled; UD=urban delivery; RD=regional delivery; PO_TRIP=port operation (using the trip distance method); DDC_DVKT=drayage duty cycle (using the daily VKT method); DDC_TRIP=drayage duty cycle (using the trip distance method).

Source: WRI authors' calculation.

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

XXV

### **3. Accelerating technology developments is essential to reduce ZET's TCO and move its parity years to an earlier date.**

Battery cost reduction, vehicle energy-efficiency improvement, and battery energy density increases are critical for reducing BETs' TCO, while the cost reduction of the FC systems and green hydrogen prices are essential to bring down FCETs' TCO (FC system costs are more influential for UD, while hydrogen prices are more important for RD).

**4. It is important to design BETs with flexibility.** Significant variations in BET battery capacities exist. For example, even within the same-use case, the differences in battery capacities of BETs examined in this study could vary by 51 kWh to 322 kWh in MY2025. Given the day-to-day operational variability of small fleet operators, designing a broadly applicable BET that is capable of meeting the majority operation (in terms of ranges) in an often-applied use case is critical. This means both Original Equipment Manufacturers (OEMs) and fleet operators should have a thorough understanding of existing diesel fleets' daily mileage profiles.

### **D. Data-driven and multi-dimensional policymaking is necessary.**

#### **1. Data on ZETs' energy efficiency and existing diesel truck fleets' mileage are important to improve the TCO estimation and to inform policymaking.**

Energy efficiency would greatly affect ZETs' parity years and determine which use case to prioritize ZET promotion. Further, truck fleets' mileage profiles are also critical to the design of broadly applicable ZETs. Therefore, it is important for governments to gather ZETs' real-world energy-efficiency and ICEVs' mileage data by use case and share among key stakeholders, such as OEMs.

**2. Fleet operators in reality would also take multiple factors into consideration, such as the safety and security of ZETs, shippers' requirements, market demands and profitability, and customers' awareness of the recent development of ZETs when**

deciding if ZET transition is feasible (QTLC and MOV3MENT 2022). Therefore, **it is also necessary to go beyond the policies examined in this study to consider more policy options**, such as enhancing ZETs' fire safety, enforcing air pollution prevention policies, improving ZETs' residual values, and organizing public education campaigns (particularly for small fleet operators).

**E.** The conclusions from the study would be applicable to cities with similar use case characteristics, including truck segment deployed, type of goods transported, driving cycles, and ambient temperature. **Cities with different characteristics should be cautious when applying this study's conclusions.** For example, a 49-ton BET100 tractor trailer in Tangshan's DDC had reached TCO parity with its diesel counterpart in MY2022, earlier than Shenzhen examined in this study. This is because tractor trailers in Tangshan do not require large battery capacities (trip distances within 100 km) and have a large proportion of the daily VKTs performed near docks or in the urban environment (Mao et al. 2023).

![img-15.jpeg](img-15.jpeg)

XXVI

WRI.org.cn

Figure ES-4 | ZETs' TCO parity years relative to ICE trucks for the DDC use case in Shenzhen and Tangshan

BET FCET (hybrid) FCET (H₂-only)

| VEHICLE | DUTY CYCLE | CARGO TYPE | DAILY VKT (KM) | 2022 | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 | Above 2030 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 49-t tractor trailer (Tangshan) | DDC_TRIP | Heavy goods | 200 |  |  |  | ● |  |  |  |  |  |  |
| 300 | ● |  |  |  |  |  |  |  |  |  |
| 400 | ● |  |  |  |  |  |  |  |  |  |
| 500 | ● |  |  |  |  |  |  |  |  |  |
| DDC_DVKT | 200 |  |  |  | ● |  |  |  |  | ▲● |  |  |
| 300 |  |  |  |  | ● |  |  |  | ▲● |  |  |
| 400 |  |  |  |  |  | ● |  |  | ▲● |  |  |
| 500 |  |  |  |  |  |  | ● |  | ▲● |  |  |
| 42-t tractor trailer (Shenzhen) | DDC_TRIP | Light goods | 200 |  |  |  |  |  |  |  |  |  | ● |
| 300 |  |  |  | ● |  |  |  |  |  |  |
| 400 | ● |  |  |  |  |  |  |  |  |  |
| 500 |  |  |  | ● |  |  |  |  |  |  |
| DDC_DVKT | 200 |  |  |  |  |  |  |  |  |  | ●▲● |  |
| 300 |  |  |  |  |  |  |  |  | ▲● | ● |  |
| 400 |  |  |  |  |  |  |  | ▲● |  | ● |  |
| 500 |  |  |  |  |  |  | ▲ | ● |  | ● |  |

Note: This study assumes that the trip distance for Tangshan's DDC use case is 100 km, while that for Shenzhen is 200 km. Further, the energy consumption of a MY2022 49-t diesel tractor trailer is 64L/100 km, a BET is 230kWh/100 km, and an FCET is 18kg/100 km.

Abbreviations: BET=battery electric truck; FCET=fuel cell electric truck; ICEV=internal combustion engine vehicle; DDC_TRIP=drayage duty cycle (using the trip distance method).

Source: WRI authors' calculation.

![img-16.jpeg](img-16.jpeg)

廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣
廣東省廣東縣

第一章

# 引言

2020年，中国货车产生的二氧化碳、氮氧化物和颗粒物排放在道路运输领域二氧化碳、氮氧化物和颗粒物排放中的占比，分别达到52%、84%与91%（Xue and Liu 2022; MEE 2021）。所以，推广新能源货车³对减少碳排放和空气污染物排放至关重要（Xue and Liu 2022）。

中国货运行业通常由成本更敏感的小微运输企业——包括小微承运商、个体司机、挂靠在公司下的个体司机——构成。据统计，2020年，小微运输企业约占中国货运运输企业⁴总数的75%（TUC 2022a）。其中，78%的个体司机年收入与2020年中国人均年收入⁵相当（SINOIOV and Chang'an University 2022）。相较之下，2020年美国牵引车司机的年收入中位数比美国人均年收入高出38%（USBLS 2020; USCB 2020）。所以，为推广新能源货车，中国城市应侧重需求侧运输企业的需求，特别是对成本更敏感、对新能源技术了解有限的小微运输企业的需求。

运输企业决定购买新能源货车时，通常从三个维度考虑：一是新能源货车在运营中能否化解续航里程不足与载质量损失等问题；二是新能源货车的购置成本（即车辆市场售价）与初期购买时的一次性费用支出（包括购置成本、税费与融资成本等）是否可负担；三是新能源货车能否与燃油货车实现TCO平价（Tol et al. 2022）。为此，本文侧重分析新能源货车面临的技术挑战、与燃油货车购置成本的差异，以及与燃油货车实现TCO平价的时间。

此外，为化解新能源货车技术与成本挑战，政府与企业也应采取相应措施。本文主要考虑三类措施在新能源货车推广中的作用：

- 政策激励：随着国家新能源汽车购置补贴的退出，中国仍有必要考虑出台一系列政策，以保持新能源货车的增长势头。
- 技术进步：与燃油货车相比，新能源货车仍面临成本高、续航里程有限、载质量损失、电机峰值功率不足、由于充电与车辆维保时间长而导致的运营效率损失等技术挑战（QTLC and MOV3MENT 2022）。因此，本文也试图回答技术进步何时以及在多大程度上能够解决上述挑战。
- 商业模式推广与运营优化：尽管新能源货车存在技术与政策缺口，但得益于换电等商业模式，新能源货车正快速推广（Shen and Mao 2023; Z. Wang et al. 2020）。2022年，中国换电重卡的年销量达12431辆，高于充电重型货车的年销量（Sohu 2023）。换电模式受欢迎的原因是在“车电分离、电池租赁”模式下，运输企业只需支付无电池车身的价格（几乎与燃油货车价格相同）；此外，通过将换电重卡的运营组织与换电站的布局相协同，换电重卡可在5分钟内完成换电，几乎不存在运营效率的损失（Ren et al. 2024）。然而，由于换电站建设成本高、标准不统一，换电重卡也面临增速放缓的问题（evpartner 2023）。未来，商业模式推广与运营优化对新能源货车推广是否仍然有效，尚有待研究。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

1

此外，货车使用场景众多，政府部门与企业也有必要识别哪些场景是优先侧重的场景。例如，2019年，深圳市将纯电动自卸汽车作为推广重点，为每辆车提供80万元的购置补贴，推广了约4200辆纯电动自卸汽车（约占其自卸汽车保有量的三分之一）（NEICV 2022）。然而，受纯电动自卸汽车成本高、运力过剩等因素影响（Pers. Comm. 2023a），深圳市不再将自卸汽车全面电动化作为重点，转而推动港口内运输场景牵引车的电动化（Shenzhen MTB 2021）。因此，识别场景是推广新能源货车的第一步。由于新能源货车在长途运输场景（日里程500千米以上）仍存在技术与成本挑战，所以，本文侧重城市运输与区域运输两个场景。

本文以中国新能源货车推广先进地区之一——广东省为例，试图回答以下问题：

- 目前新能源货车推广面临哪些技术与成本上的挑战？
- 近期应重点在哪些运输场景推广新能源货车？推广的关键时间节点是什么？
- 各运输场景适宜哪种新能源技术路线？
- 哪些措施（政策激励、技术进步、商业模式推广与运营优化）有助于解决新能源货车在技术和成本上面临的挑战？
- 基于广东省的研究结论是否适用于中国其他地区？

广东省一直是中国新能源货车推广的“领头羊”。2022年，广东省的新能源货车销售量在中国31个省份（不含港澳台地区）中排名第一（Niu et al. 2023）。为降低数据量，本文仅选择广东省两个典型城市——深圳市和佛山市——进行分析。2021年，深圳市、佛山市的轻型货车与重型货车保有量分别占广东省轻型货车与重型货车保有量的27%和30%（Guangdong Stats 2023）。6 另外，两个城市也制定了较高的新能源货车推广目标：

- 作为全国首批公共领域车辆全面电动化先行区之一，深圳市计划在2023—2025年期间，实现城市物流配送领域新增及更新车辆中80%为新能源汽车的目标，并计划到2025年，深圳港港口内运营的牵引车基本更新为清洁能源货车（MIIT et al. 2023; Shenzhen MEEB 2022）。
- 佛山市为广东省氢燃料电池汽车示范城市群的牵头城市。该示范城市群计划到2025年推广1万辆以上的氢燃料电池汽车（Guangdong DRC et al. 2022）。

由于广东省率先在一些场景中试点新能源货车，其推广经验对中国其他地区也具有一定参考意义。因此，本文也通过案例分析探讨分析结果在中国其他地区的适用性。中国新能源货车推广的国家政策及地方（深圳市和佛山市）政策见表1。

![img-17.jpeg](img-17.jpeg)

![img-18.jpeg](img-18.jpeg)

表 1 | 中国新能源货车推广的国家政策及地方(深圳市和佛山市)政策

|   | 纯电动微面、 中面 | 纯电动轻型货车 | 纯电动重型货车 | 氢燃料电池货车  |
| --- | --- | --- | --- | --- |
|  **国家政策**  |   |   |   |   |
|  **车辆购置税和 车船税减免** | 新能源货车在2025年底前免征车辆购置税，在2026—2027年减半征收车辆购置税；新能源货车免征车船税（MOF, STA, and MIIT 2023, 2018）  |   |   |   |
|  **购置补贴** | X | X | X | 按照燃料电池系统的额定功率补贴3000元/千瓦，单车补贴最大功率不超过110千瓦（Guangdong DRC et al. 2022）  |
|  **新能源货车充电、 加氢补贴** | 新能源货车免需量电费（State Council 2023） |   |   | 3～12元/千克加氢补贴（MOF, MIIT, MOST, NDRC, and NEA 2020）  |
|  **地方政策：深圳**  |   |   |   |   |
|  **购置补贴（或置换补贴）** | X | X | 对深圳港港口内燃油牵引车置换为新能源牵引车进行资助，单车补贴50000～70000元（Shenzhen MTB 2023）  |   |
|  **运营补贴** | X | X | 对深圳港港口内运营的新能源牵引车进行资助，纯电动牵引车每月补贴5000元，氢燃料电池牵引车每月补贴3000元（Shenzhen MTB 2023）  |   |
|  **新能源货车充电、 加氢补贴** |  | X | 针对站内电解水制氢，允许使用蓄冷电价（Shenzhen DRC 2022）  |   |
|  **优先路权** | 在深圳市中心设立16个绿色物流区，全天禁止轻型柴油货车进出。此外，部分区域在特定时间段禁止燃油货车进入，但允许新能源轻型货车和新能源中型货车进出（Shenzhen PSB 2022, 2023a, 2023b, 2023c）（见附录A）  |   |   |   |
|  **地方政策：佛山**  |   |   |   |   |
|  **置换补贴** | X | X | X | 单车补贴30000～70000元（Foshan Nanhai Government 2021）  |
|  **运营补贴** | 0.2～0.4元/千米（上限为每年30000千米）（Foshan MTB 2022） | 0.6元/千米（上限为每年30000千米）（Foshan MTB 2022） | X | 轻型货车为1.5元/千米（上限为每年50000千米）（Foshan MTB 2022）  |
|  **新能源货车充电、 加氢补贴** |  | X | 18元/千克加氢补贴（Foshan Nanhai Government 2022）  |   |
|  **优先路权** | 在佛山市中心设立4个绿色物流区，全天禁止轻型柴油货车进出市中心（部分区域还禁止燃油重型货车进出）。此外，部分区域在特定时间段禁止燃油货车进入，但允许新能源轻型货车和新能源中型货车进出。南海中心城区“原则上不允许燃油市政工程车辆以及物流车进入开展工程”，但允许氢燃料电池车辆进入（Foshan MEEB and Foshan PSB 2022; Foshan Nanhai Government 2021）（见附录A）  |   |   |   |

说明：购置补贴是广东省氢燃料电池汽车示范城市群国家和地方购置补贴之和，如无政策。

来源：作者汇总。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

3

93 2073

## 第二章

# 研究方法

本文研究范围与研究方法说明如下：

- ■ 时间范围：根据最新数据的可得性，本文的基准年为2022年。由于本研究侧重新能源货车近期的推广潜力，所以，预测年份最远至2030年。
- ■ 货车技术路线：考虑到新能源技术的减排潜力，本文在技术路线上仅涵盖纯电动汽车、氢燃料电池汽车两种路线，以及常见传统燃料汽车——汽柴油汽车。由于数据限制以及缺乏相关技术的应用，插电式混合动力汽车、低碳燃料内燃机汽车（如甲醇内燃机汽车）与天然气汽车等不在本研究分析范畴。
- ■ 新能源货车的购置决策变量：本文侧重量化运输企业购置新能源货车过程中的三个决策变量，即新能源货车的运营可行性（即技术适配性）、新能源货车购置成本与初期购买时的一次性费用支出，及新能源货车与燃油货车的TCO差异（Tol et al. 2022）。基于文献的常规做法（Basma et al. 2023; CARB 2019; Hunter et al. 2021; Mao et al. 2021; Tol et al. 2022），本文根据新能源货车实现与传统燃油货车TCO平价的年份，识别近期具备新能源货车推广潜力的运输场景。其他决策变量（如车辆安全性等）由于难以量化，故不在本研究分析范畴。

此外，本文也分析了不同措施（包括政策激励、技术进步、商业模式推广与运营优化）可能对上述三个决策变量产生的影响——特别是这些措施在助力新能源

货车更早实现与燃油货车TCO平价方面所发挥的作用。其他难以量化的措施（如货主企业对新能源货车使用的要求）不在本文讨论范畴。另外，为分析本文研究结论的适用性，本文还进行了同一场景下不同地区新能源货车经济性对比分析，并讨论了本文分析的局限性与未来的调整方向。运输企业新能源货车购置决策变量与影响决策变量的四项措施之间的关系如图1所示。

图 1 | 运输企业新能源货车购置决策变量与影响决策变量的四项措施之间的关系

![img-19.jpeg](img-19.jpeg)

来源：作者绘制。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

5

## 2.1 运输场景的定义

本文基于影响新能源货车技术和经济性的因素——包括货车车型、行驶工况与运输货物类型——将深圳市与佛山市常见的城市运输与区域运输场景，细分成为14个运输场景。其具体说明如下：

**货车车型：**根据《广东统计年鉴2023》、2022年颁布的各批次《免征车辆购置税的新能源汽车车型目录》（以下简称《车型目录》）（MIIT 2022）与本研究对运输企业的调研（Pers. Comm. 2023a），本文选取了深圳市、佛山市常见的货车车型（见表2），车辆保有量少且新能源车型有限的货车车型（如冷藏货车和中型货车）不在本文分析范畴。

**行驶工况：**本文基于对运输企业的调研（Pers. Comm. 2023a），将城市运输与区域运输场景细分成四个工况，即城市运输、港口内运输、集疏港运输与区域运输（不含集疏港）。由于新能源货车在长途运输场景（日里程500千米以上）仍存在挑战，且深圳市和佛山市90%的货车日行驶里程在500千米以内（Pers. Comm. 2023a），所以，日行驶里程超过500千米的长途运输场景不在本文分析范畴。

本文基于对运输企业的调研（Pers. Comm. 2023a）获得的深圳、佛山典型行驶工况，以及货车日行驶里程、年运营天数、年行驶里程与货车使用年限等信息，如表3所示。

表 2 | 2022年货车车型分类及各车型在深圳市和佛山市货车保有量中的占比

|   | 最大设计总质量 (吨) | 2022年深圳各类车型占货车保有量的比例 | 2022年佛山市各类车型占货车保有量的比例 | 2022年《车型目录》中新能源货车车型数量 | 本研究范围  |
| --- | --- | --- | --- | --- | --- |
|  **微型货车**  |   |   |   |   |   |
|  普通货车 | GVW≤1.8 | 0.2% | 0.05% | X | 保有量很少， 不考虑  |
|  冷藏货车 | GVW≤1.8 |   |   | X  |   |
|  **轻型货车**  |   |   |   |   |   |
|  微面、中面 | 1.8<GVW<4.5 | 75% | 78% | X | √  |
|  普通货车 | 4.2<GVW<4.5 |   |   | 372 | √  |
|  冷藏货车 | 2.2<GVW<4.5 |   |   | 47 | 保有量很少， 不考虑  |
|  自卸汽车 | 2.2<GVW<4.5 |   |   | 1 | 保有量很少且新能源货车车型有限， 不考虑  |
|  **中型货车**  |   |   |   |   |   |
|  普通载货汽车 | 4.5≤GVW<12 | 2% | 4% | 14 | 保有量很少且新能源货车车型有限， 不考虑  |
|  冷藏货车 | 4.5≤GVW<12 |   |   | 11  |   |
|  自卸汽车 | 4.5≤GVW<12 |   |   | 5  |   |
|  **重型货车**  |   |   |   |   |   |
|  普通载货汽车 | 12≤GVW≤31 | 23% | 18% | 25 | √  |
|  半挂牵引车 | 31≤GCW≤49 |   |   | 192 | √  |
|  自卸汽车 | 16≤GVW≤31 |   |   | 126 | √  |
|  冷藏货车 | 14≤GVW≤31 |   |   | 10 | 保有量很少且新能源货车车型有限， 不考虑  |

说明：X= 由于车型数量少或较难识别，本文未统计该车型的车型数量。

缩略词：GVW/GCW= 最大设计总质量。

来源：作者基于 Guangdong Stats 2023、MIIT 2022、Pers. Comm. 2023a 和 SAC/TC576 的汇总。

6

WRI.org.cn

基于不同场景日行驶里程分布，本文假设城市运输的日行驶里程不超过300千米，区域运输的日行驶里程为300~500千米（Pers. Comm. 2023a）。

集疏港运输与区域运输的日行驶里程类似，但区分为两个工况的原因如下：相较于区域运输，集疏港运输采用的货车车型、起始点/目的地与运营时刻表相对可预测，因此，可更精细化地分析新能源货车的技术与成本可行性。作为2022年中国集装箱吞吐量第三大港口（Xinhua Finance 2023），深圳港约有23000辆集疏港半挂牵引车，以4×2牵引车（最大设计总质量为42吨）为主（Pers. Comm. 2023a）。其中，港口76%的集装箱来自邻近的东莞市、惠州市等城市，单程运距在

200千米以内（Wang et al. 2024）。由于港口预约系统仅允许每辆货车每天预约一次，所以，半挂牵引车每天可在港口与目的地之间往返1~1.5个来回（NEICV 2022），日行驶里程为200~500千米（Pers. Comm. 2023a）。

考虑到货车的日行驶里程与年行驶里程对新能源货车造型与TCO有较大影响，本文在计算中以每100千米日行驶里程为间隔，测算同一场景、每100千米日里程段下，新能源货车（如BET200、BET300等）的技术参数配置、购置成本与TCO。此外，由于数据限制，本文还假设货车年行驶里程不会随货车使用年限的增加而减少，且新能源货车与燃油货车的年行驶里程、使用年限均相同。

表 3 | 本文中深圳市、佛山市的典型行驶工况说明

|  行驶工况 | 货车车型 | 货物类型 | 工况说明  |
| --- | --- | --- | --- |
|  UD | 微面、中面 | 快递 （轻抛货） | · 单次往返运距：30~100千米 · 每日往返次数：2~4次 · 日行驶里程：60~200千米  |
|   |  4.5吨轻型普通货车 | 快递 （轻抛货） | 同城配送中心之间配送： · 单次往返运距：50~80千米 · 每日往返次数：2~4次 · 日行驶里程：100~300千米  |
|   |   |  饮品 （重货） | 同城仓库与商超之间配送： · 单次往返运距：40~200千米 · 每日往返次数：1次（循环取货） · 日行驶里程：40~200千米  |
|   |  31吨自卸汽车 | 建筑材料/废弃物 （重货） | 建筑工地到港口（运送到周边城市）、同城的回收利用点或城市周边的收纳点： · 单次往返运距：60~80千米 · 每日往返次数：2~3次 · 日行驶里程：120~240千米  |
|  RD | 18吨载货汽车/42吨 半挂牵引车 | 快递 （轻抛货） | 城际运输（例如佛山市和广州市的配送中心之间）： · 单次往返运距：150~200千米 · 每日往返次数：2次 · 日行驶里程：300~400千米  |
|   |   |  饮品 （重货） | 工厂和仓库之间的城际运输： · 单次往返运距：150~200千米 · 每日往返次数：2次 · 日行驶里程：300~400千米  |
|  PO | 42吨半挂牵引车 | 集装箱 （轻抛货） | 港口码头与集装箱堆场之间的集装箱运输： · 每天低速行驶17小时，急速时间长且频繁加减速 · 日行驶里程：120~240千米  |
|  DDC | 42吨半挂牵引车 | 集装箱 （轻抛货） | 港口与仓库之间的市内运输和城际运输： · 单次往返运距：200~400千米 · 每日往返次数：1~1.5次 · 日行驶里程：200~500千米  |

说明：4.5吨轻型普通货车指最大设计总质量（GMW）为4.490~4.495吨的轻型货车，18吨载货汽车指最大设计总质量（GMW）为18吨的载货汽车，31吨自卸汽车指最大设计总质量（GMW）为31吨的自卸汽车，42吨半挂牵引车指最大设计总质量（GMW）为42吨的半挂牵引车。

缩略词：UD=城市运输；RD=区域运输；PO=港口内运输；DDC=集疏港运输。

来源：作者基于对运输企业的调研总结（Pers. Comm. 2023a，见附录B）。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

7

**货物类型：**本文基于货物密度将货物划分成两个类型，即轻抛货和重货。货物密度小于210千克/立方米的$^{7}$（如小型家用电器）为轻抛货，货物密度大于等于210千克/立方米的（如煤炭和饮品）为重货（CATARC 2017）。在重货运输中，由于电池包、燃料电池系统质量大，新能源货车会面临载质量损失问题；而在轻抛货运输中，新能源货车在达到货车质量限值之前，往往先达到体积限值，所以，不存在载质量损失问题。

目前，由于中国（如广东省）仍有一些重货运输需求（见表4），新能源货车通常会面临载质量损失问题。例如，由于基础设施建设需求较高，广东省珠三角地区2019年货运量有较大比例（32.7%）为建筑材料与水泥（Lin et al. 2021），因

此，需要充分考虑重货运输场景下的新能源货车载质量损失问题。另外，在深圳港，由于电子器械等轻抛货运量大（Pers. Comm. 2023a），因此，港口内运输与集疏港运输中，多采用42吨半挂牵引车，新能源货车较少面临载质量损失问题。

综上所述，本文识别并构建了深圳市与佛山市的14个典型的城市运输与区域运输场景（见表5），涵盖了五种货车车型（即微面中面、4.5吨轻型普通货车、18吨载货汽车、31吨自卸汽车与42吨半挂牵引车）、四种行驶工况（城市运输、区域运输、港口内运输、集疏港运输），以及两种货物类型（即轻抛货和重货）。由于数据可得性限制，本文分析的场景不一定能覆盖深圳市与佛山市所有场景，但尽可能包括本地化的典型场景。

表 4 | 2019年中国及主要地区不同货类的货运量占比

|  货物类型 | 中国 | 京津冀地区 | 江浙沪地区 | 广东省 | 珠三角地区  |
| --- | --- | --- | --- | --- | --- |
|  煤炭相关产品 | 12.6% | 21.0% | 2.0% | 2.4% | 2.2%  |
|  金属和矿产品 | 7.1% | 16.3% | 3.4% | 1.7% | 1.3%  |
|  建筑材料和水泥 | 38.7% | 24.9% | 35.3% | 43.6% | 32.7%  |
|  机械设备 | 6.7% | 6.0% | 13.3% | 8.2% | 11.5%  |
|  轻工业品 | 7.9% | 5.8% | 14.5% | 14.1% | 18.4%  |
|  生鲜食品 | 5.9% | 5.7% | 2.6% | 2.9% | 2.4%  |
|  其他 | 21.1% | 20.3% | 28.9% | 27.1% | 31.5%  |
|  合计 | 100% | 100% | 100% | 100% | 100%  |

说明：红色表示货运量高，绿色表示货运量低。

来源：Lin et al. 2021。

表 5 | 本文覆盖的典型运输场景及说明

|  编号 | 货车车型 | 行驶工况 | 货物类型 | 日行驶里程（千米） | 货运前天性和车辆使用年限 | 年行驶里程（千米）  |
| --- | --- | --- | --- | --- | --- | --- |
|  1 | 微面、中面 | UD | 跨货类 | 200、300 | 310天、6年 | 62000 ~ 93000  |
|  2-3 | 4.5吨轻型普通货车 | UD | 轻抛货、重货 | 200、300 | 310天、6年 | 62000 ~ 93000  |
|  4-5 |   | RD | 轻抛货、重货 | 300、400、500 |   | 93000 ~ 155000  |
|  6 | 31吨自卸汽车 | UD | 重货 | 200、300 | 270天、5年 | 54000 ~ 81000  |
|  7-8 | 18吨载货汽车 | UD | 轻抛货、重货 | 200、300 | 320天、6年 | 64000 ~ 96000  |
|  9-10 |   | RD | 轻抛货、重货 | 300、400、500 |   | 96000 ~ 160000  |
|  11 | 42吨半挂牵引车 | UD | 轻抛货 | 200、300 | 310天、6年 | 62000 ~ 93000  |
|  12 |   | PO | 轻抛货 | 200、300 |   | 62000 ~ 93000  |
|  13 |   | DDC | 轻抛货 | 200、300、400、500 |   | 62000 ~ 155000  |
|  14 |   | RD | 轻抛货 | 300、400、500 |   | 93000 ~ 155000  |

说明：由于新能源货车在日行驶里程 100 千米以内的运输场景（按T100 和 FCE100）下几乎无技术限制，因此，本文在所有场景中，未考虑日行驶里程 100 千米以内的情况。

缩略词：UD=城市运输；RD=区域运输；PO=港口内运输；DDC=集疏港运输。

来源：作者基于对运输企业的调研总结（Pers. Comm. 2023a，见附录 5）。

8

WRI.org.cn

## 2.2 新能源货车关键零部件参数设置方法

本文中，新能源货车的运营可行性（即技术适配性）分析侧重新能源货车现状与未来的技术参数设置，包括电池容量、储氢容量、电机峰值功率、车辆整备质量等，以确保新能源货车在技术上能够满足不同场景下的运营需求。由于数据可得性限制，本文未考虑新能源货车充电时间损失、车辆安全性等技术指标。

本文针对新能源货车参数设置的原则，说明如下：

- ■ 基准年（2022年）新能源货车的参数设置为实际参数配置，即《车型目录》（MIIT 2022）中新能源货车参数配置的中位数（如电池容量中位数），旨在分析目前各场景中新能源货车因技术不成熟而面临的运营限制。
- ■ MY2022—MY2030期间新能源货车的参数设置为假设配置，即随着未来技术进步，新能源货车的设置将能满足不同运输场景下续航里程、电机峰值功率的要求。这与目前文献的假设相符（Hunter et al. 2021; Mao et al. 2021），旨在识别满足不同场景运营需要的新能源货车参数配置。

值得注意的是，本文中2022年与 MY2022 新能源货车的参数设置存在差异。其中，2022年新能源货车为实际的参数配置，未必满足所有场景的运营需求，而MY2022 新能源货车为假设的参数设置，能够满足所有场景对新能源货车续航里程与电机峰值功率的要求。

### 新能源货车的电池容量与储氢容量

根据行驶里程与货车实际能量消耗量，本文计算了MY2022—MY2030期间新能源货车为满足各场景运营要求所需的储能装置容量，包括纯电动货车的电池额定容量（简称电池容量）与氢燃料电池货车储氢瓶的额定容量（简称储氢容量）（见公式1）：

$$E_{u,t} = \frac{VKT_u \times EE_{u,t}}{100 \times DoD} \quad (\text{公式1})$$

其中：

$E_{u,t}$ 表示电池容量或储氢容量（千瓦时或千克）；

$VKT_u$ 表示日行驶里程或单程运距（千米），以100千米为间隔表示，如区域运输场景日行驶里程包括300千米、400千米和500千米；

$EE_{u,t}$ 表示纯电动货车或氢燃料电池货车的能量消耗量（千瓦时/100千米或千克/100千米）；

$DoD$ 表示纯电动货车的电池放电深度或氢燃料电池货车储氢系统的可用容量（%），本文假设纯电动货车的电池放电深度为80%（Mao et al. 2021; Nykvist and Olsson 2021; Phadke et al. 2021; Wu et al. 2015; Zhao et al. 2018），氢燃料电池货车储氢系统的可用容量为85%（Danebergs 2019）；

$u$ 表示运输场景，$t$ 表示车型年份。

为设置新能源货车的电池容量或储氢容量，本文采用两种方法，即纯电动货车充满电或氢燃料电池货车加满氢气后，可支持“日行驶里程”或“单程运距”的里程需求。值得注意的是，不同配置方法不仅会导致新能源货车储能容量的区别，也会带来充电技术选择与充电（加氢）基础设施布局的差异：

- ■ 日行驶里程法，即基于新能源货车日行驶里程设定其储能容量的方法。该方法对应纯电动货车“一天一充”或氢燃料货车“一天一次加氢”的情况。采用该方法配置的纯电动货车（如BET200）可通过在货运场站的夜间慢充（depot charging），满足日行驶里程200千米以内场景的运营要求。
- ■ 单程运距法，即基于新能源货车单程（或往返）运距设定其储能容量的方法。该方法对应纯电动货车“一天多充”的情况，即除货运场站的夜间充电外，车辆也需要在中途、装卸货等待或司机休息期间进行日间补电。因此，采用该方法配置的纯电动货车（如BET200）可通过日间补电完成更长的日行驶里程（300～400千米）。但是，为确保日间补电不影响车辆运营效率，运输企业通常需要优化纯电动货车的运营调度（如协调充电时间、装卸货等待时间与司机休息时间），并采用快充（或换电）模式（IEA 2023b），减少对运营的影响。

本文中，城市运输场景、区域运输场景中的新能源货车使用“日行驶里程”法，港口内运输场景和集疏港运输场景中的纯电动货车同时采用“日行驶里程”法和“单程运距”法。方法选择的说明，详见“MY2022—MY2030各场景结果”一节。

值得注意的是，虽然氢燃料电池货车可“多天加一次氢”，但为了降低其储氢系统的成本，本文假设加氢站布局能满足车辆每天加氢的需要$^{8}$，因此，所有场景下，氢燃料电池货车仍采用“日行驶里程”法设置车载储氢系统的容量。

除行驶里程外，新能源货车实际能量消耗量也影响其电池容量或储氢容量。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

9

首先，2022年深圳市与佛山市新能源货车的实际能量消耗量由作者通过对运输企业的调研获得（Pers. Comm. 2023a，见附录B）。值得注意的是，即便货车车型相同，不同工况的实际能量消耗量也有较大差异。本文根据不同行驶工况（包括城市道路工况、高速公路工况）与货物类型（包括轻抛货、重货运输），区分不同场景下货车的实际能量消耗量。以42吨纯电动半挂牵引车为例，基于深圳市近期新能源货车示范结果，本文假设2022年42吨纯电动半挂牵引车在城市运输（轻抛货运输）场景中的能量消耗量约为110千瓦时/100千米，在区域运输（以高速公路、国道为主）场景中的能量消耗量约为118千瓦时/100千米（Pers. Comm. 2023a）。对于重货运输，本文假设在城市运输和区域运输中，轻型货车的能量消耗量会较轻抛货运输增加3%~5%，而重型货车的能量消耗量会增加13%~18%（Alonso-Villar et al. 2023）。港口内运输场景的货车能量消耗量则直接来自对运输企业的调研（Pers. Comm. 2023a，见附录B）。

其次，本文基于文献汇总得到MY2022—MY2030新能源货车的能量消耗量，并假设燃油货车能量消耗量将维持在2022年水平。考虑到现有文献的能耗与行驶工况、货物类型紧密相关，不具备可比性，本文采用新能源货车与燃油货车的能效比（EER）对MY2022—MY2030不同场景下新能源货车的能量消耗量进行交叉验证（见图2）。新能源货车与燃油货车的能效比是指，在相同的行驶工况中，驱动燃油货车所消耗的能量与驱动新能源货车所消耗的能量之比。能效比越高，说明该工况下新能源货车相对燃油货车的能效优势越大。我们调整了文献中新能源货车能量消耗量的预测值，确保各场景的能效比与现有文献（CARB 2018）中相同场景的能效比相当。本文中不同运输场景纯电动货车与氢燃料电池货车的能效比见表6。

在措施上，新能源货车的运营优化与技术进步有助于降低不同场景新能源货车的储能容量。其中，在运营优化方面，完善充电基础设施的覆盖度、优化新能源货车调度并与充电时间协同，可以降低纯电动货车搭载的电池容量；在技术进步方面，降低新能源货车的能量消耗量，也有助于降低其储能容量。

图 2 | 本文与现有文献对MY2030纯电动货车与氢燃料电池货车能量消耗量的预测

■ 重型半挂牵引车（RD） ■ 重型载货汽车（跨场景） ● 本研究

a. 纯电动货车

![img-20.jpeg](img-20.jpeg)

b. 氢燃料电池货车

![img-21.jpeg](img-21.jpeg)

说明：虽然本文在成本计算中区分了当吨载货汽车和42吨半挂牵引车在不同场景、货物类型与行驶工况下的能量消耗量，但由于文献未作区分，因此，图中我们仅对相同货车车型的能量消耗量进行对比。

缩略词：UD=城市运输；RD=区域运输。

来源：作者基于 Basma et al. 2023、Burke and Sinha 2020、Burnham et al. 2021、CARB 2019、Hunter et al. 2021、Mao et al. 2021、Rout et al. 2022、Rui et al. 2020、Tol et al. 2022、Transport and Environment 2021 的总结。

10

WRI.org.cn

表 6 | 本文中不同运输场景纯电动货车与氢燃料电池货车的能效比

|  运输场景 | 货物类型 | 纯电动货车 |   | 氢燃料电池货车  |   |
| --- | --- | --- | --- | --- | --- |
|   |   |  MY2022 | MY2030 | MY2022 | MY2030  |
|  **4.5吨轻型普通货车**  |   |   |   |   |   |
|  UD | 轻抛货 | 3.2 | 3.7 | 1.6 | 2.0  |
|   |  重货 | 3.1 | 3.6 | 1.7 | 2.0  |
|  RD | 轻抛货 | 2.6 | 2.9 | 1.5 | 1.8  |
|   |  重货 | 2.6 | 2.9 | 1.5 | 1.8  |
|  **13吨载货汽车**  |   |   |   |   |   |
|  UD | 轻抛货 | 2.9 | 3.1 | 1.4 | 1.5  |
|   |  重货 | 2.9 | 3.1 | 1.6 | 1.8  |
|  RD | 轻抛货 | 2.3 | 2.4 | 1.3 | 1.4  |
|   |  重货 | 2.3 | 2.5 | 1.4 | 1.6  |
|  **31吨自卸汽车**  |   |   |   |   |   |
|  UD | 重货 | 2.9 | 3.1 | 1.5 | 1.6  |
|  **42吨半挂牵引车**  |   |   |   |   |   |
|  PO | 轻抛货 | 4.0 | 4.2 | 1.7 | 1.8  |
|  UD | 轻抛货 | 2.9 | 3.1 | 1.5 | 1.6  |
|  RD | 轻抛货 | 2.3 | 2.5 | 1.3 | 1.4  |
|  DDC | 轻抛货 | 2.3 | 2.5 | 1.3 | 1.4  |

缩略词：UD=城市运输；RD=区域运输；PO=港口内运输；DDC=集疏港运输。

来源：作者基于 Burke and Sinha 2020, Burnham et al. 2021, CARB 2019, Gilleon et al. 2022, Giuliano et al. 2021, Hunter et al. 2021, Katz et al. 2022, Lane et al. 2022, Mao et al. 2021, Rout et al. 2022, Ruf et al. 2020, Sato et al. 2022, Tol et al. 2022, Transport and Environment 2021 的计算和汇总。

## 新能源货车电机峰值功率与燃料电池系统峰值功率

本文假设，MY2022—MY2030期间新能源货车配备与同类型燃油货车输出功率相同的电驱动系统与零部件，以满足各场景运营需要。

值得指出的是，对氢燃料电池货车而言，除电机峰值功率外，设置燃料电池系统的功率（其对氢燃料电池货车的购置成本与TCO有较大影响）也至关重要。燃料电池系统的功率由氢燃料电池货车的车辆构型决定，目前，氢燃料电池货车有两种构型（Marcinkoski et al. 2016; Zhao et al. 2018）：一种构型是混合动力系统，即氢燃料电池货车在燃料电池系统的基础上，还配置一个大容量电池包。其中，燃料电池系统的功率能满足稳态工况（如常用车速）下的功率需求，电池包作为燃料电池系统的补充，用于满足峰值功率输出的要求。此外，电池包还发挥增程器的作用，即氢燃料电池货车既可以从燃料电池系统与电池包获得能量。另一

种构型为全功率系统，即大功率燃料电池系统结合小容量的（功率型）电池包。其中，燃料电池系统的功率能满足最高车速下的功率要求，并用于提供能量，而电池包用于补充峰值功率与实现制动能量回收。

目前在中国市场上，混合动力系统的氢燃料电池货车在市场占据主导地位，且由于其成本低，也将是未来城市与区域运输场景中的主力构型（Zhao et al. 2018; Pers. Comm. 2023c）。为此，本文假设MY2022—MY2030期间，氢燃料电池货车仍使用混合动力系统。针对混合动力系统，由于氢燃料电池货车的电池包容量已基本实现了标准化（MIIT 2022），所以，本文假设MY2022—MY2030期间：氢燃料电池重型货车选择容量为100千瓦时、充放电倍率为2C$^{2}$的电池包；氢燃料电池轻型货车选择容量为30千瓦时、充放电倍率为1C的电池包，辅助氢燃料电池货车在加速、爬坡等工况下的峰值功率输出。对上述混合动力构型的氢燃料电池轻型与重型货车而言，燃料电池系统的功率等于电机峰值功率减去电池功率。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

11

值得指出的是，本文中假设的氢燃料电池货车混合动力的构型未经优化；未来还需要改进其参数配置，以便在满足运输场景峰值功率需求的同时，削减不必要的电池容量。

### 新能源货车的整备质量与载质量损失

与燃油货车相比，新能源货车增加的电池容量、储氢容量和燃料电池系统等将增加新能源货车的整备质量，导致其载质量与载货体积下降（Basma et al. 2023; Rout et al. 2022）。本文着重讨论新能源货车的载质量损失问题，载货体积损失留待未来分析。

本文计算并预测MY2022—MY2030期间，新能源货车在重货运输场景下的整备质量与载质量损失。其计算方法为，从传统燃油货车的整备质量中减去燃油动力总成的质量，再加上新能源货车关键零部件的质量，得到新能源货车的整备质量。其中：

- 纯电动货车关键零部件的质量包括电池包、电驱系统（含电机、逆变器和变速箱）及配套零部件的质量；
- 氢燃料电池货车关键零部件的质量包括燃料电池系统（含燃料电池辅助系统）、储氢系统、电池包、电驱动系统以及配套零部件的质量。

本文针对新能源货车关键零部件质量与成本的假设及数据来源见表7。以纯电动货车的电池包为例，其质量由电池包能量密度、电池包额定容量决定（其中，上节已解释电池包额定容量的预测方法）。目前，由于中国90%的新能源商用车使用磷酸铁锂（LFP）电池（CALB 2022），本文选取《车型目录》（MIIT 2022）中2022年磷酸铁锂电池包能量密度的中位数（160瓦时/千克）作为2022年基线水平。未来，随着新材料（如固态电池）与电池成组技术的发展，电池包能量密度（成本、安全性及循环寿命等）将得到大幅改善（Berckmans et al. 2017; EC 2021）。本文基于文献综述，假设2030年电池包能量密度将上升至238瓦时/千克，比2022年水平提高49%（Qiu et al. 2021）。在该假设下，区域运输场景42吨BET500半挂牵引车的电池包质量将从MY2022的4.6吨降至MY2030的2.9吨。值得注意的是，本文采取技术中立的方法，仅假设未来电池性能参数取值，不考虑未来电池将采取哪种技术路线。

为验证新能源货车关键零部件质量的相关假设，本文将测算的MY2022新能源货车整备质量与《车型目录》同等配置新能源货车整备质量进行比较，结果显示，二者整备质量之差介于0%~2%，这表明上述计算方法与数据假设具备一定的可靠性。

表7 | 本文针对新能源货车关键零部件质量与成本的假设及数据来源

|  质量 |   |   |   | 成本  |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  指标 | MY2022 | MY2030 | 数据来源 | 指标 | MY2022 | MY2030 | 数据来源  |
|  **燃油动力总成和无动力车身**  |   |   |   |   |   |   |   |
|  燃油动力总成质量（千克） | 因货车车型而异 | 与MY2022相同 | MY2022轻型货车的计算基于Pers. Comm. (2023c)，MY2022重型货车的计算基于Mao et al. (2021) | 无动力车身成本（元） | 燃油货车车辆成本的60% | 与MY2022相同 | MY2022的成本基于Macquarie (2021)  |
|  **电池包**  |   |   |   |   |   |   |   |
|  电池包能量密度（瓦时/千克） | 160 | 238 (+49%) | MY2022的数值取《车型目录》（MIIT 2022）的中位数 MY2030的预测基于Qiu et al. (2021) 通过使用新的正负极材料、提升电池的成组效率，提高电池包的能量密度（Berckmans et al. 2017; EC 2021） | 电池包的单位成本（元/千瓦时） | 930 | 680 (-27%) | MY2022的成本基于《节能与新能源汽车技术路线图2.0》（以下简称路线图）（China SAE 2021） MY2030的预测基于12%的学习率（Hsieh et al. 2019）和文献中累计产量（Xue and Liu 2022）。预测结果与China SAE (2024)校核 通过使用新材料、改进电池集成技术，降低电池包的成本（Sharpe and Basma 2022）  |

12

WRI.org.cn

表 7 | 本文针对新能源货车关键零部件质量与成本的假设及数据来源(续)

|  质量 |   |   |   | 成本  |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  指标 | MY2022 | MY2030 | 数据来源 | 指标 | MY2022 | MY2030 | 数据来源  |
|  **电驱动系统**  |   |   |   |   |   |   |   |
|  电驱动系统的质量(千克) | 因货车车型而异 | 因货车车型而异 (-20%) | **MY 2022**数值基于Pers. Comm. (2023c) **MY 2030**相较MY2022下降的比例基于路线图(China SAE 2021)的设定 通过提升电驱动系统的集成度并采用轻量化材料,降低电驱动系统质量(EUCAR 2019) | 电驱动系统的单位成本(元/千瓦) | 430 | 296 (-32%) | **MY 2022**的成本基于ICCT(Mao et al. 2021) **MY 2030**的预测基于15%的学习率和文献中累计产量(Xue and Liu 2022)。预测结果与Mao et al. (2021)校核 通过优化集成技术、简化电驱动系统以及规模化生产,降低电驱动系统的成本(U.S. DRIVE 2017a)  |
|  **燃料电池系统**  |   |   |   |   |   |   |   |
|  燃料电池质量功率密度(瓦/千克) | 600 | 900 (+50%) | **MY 2022**数值和**MY 2030**的预测都基于Pers. Comm. (2023c) 通过提升关键零部件(如膜电极、双极板等)性能与燃料电池系统集成度,提高燃料电池的质量功率密度(APCUK and Austin Power 2022; U.S. DRIVE 2017b) | 燃料电池系统的单位成本(元/千瓦) | 4120 | 891 (-78%) | **MY 2022**的成本基于Sinosynergy(2022) **MY 2030**的预测基于20%的学习率(Ajanovic and Haas 2018; IEA 2015)和路线图中氢燃料电池货车的累计产量(China SAE 2021) 通过增加功率密度,降低催化剂担载量与改进制造工艺,降低燃料电池系统的成本(DOE 2023)  |
|  **储氢系统**  |   |   |   |   |   |   |   |
|  质量储氢密度 | 4.5% | 6.5% (+43%) | **MY 2022**数值基于作者对该领域专家的调研(Pers. Comm. 2023c) **MY 2030**的预测基于路线图(China SAE 2021) 通过推广IV型储氢瓶(或液氢技术),提高储氢系统的质量储氢密度 | 储氢系统的单位成本(元/千克氮气) | 4000 | 1560 (-61%) | **MY 2022**的成本基于路线图(China SAE 2021) **MY 2030**的预测基于15%的学习率(Qiu et al. 2021)和路线图中氢燃料电池货车的累计产量(China SAE 2021)。预测结果与China SAE(2024)校核 通过量产和自动化技术,降低储氢系统的成本(Hydrogen Council 2020)  |
|  **配套零部件**  |   |   |   |   |   |   |   |
|  单位成本(元/千瓦) | 因货车车型而异 | 因货车车型而异 | 基于车辆整备质量与其他关键零部件的质量,核验该质量 | 单位成本(元/千瓦) | 486 (OBC) 与MY 389 (DC/DC 转换器) 同 |  | **MY 2022**车载充电机(OBC)的成本基于Mao et al. (2021), DC/DC转换器的成本基于Nair et al. (2022)  |

说明: * 燃油动力总成包括发动机、变速箱、油箱和尾气后处理装置等。为了简化,本文假设 MY2022~MY2030 期间,燃油货车动力总成质量不变。

* 无动力车身包括货车车厢和底盘,其成本通过从货车购置成本中减去燃油动力总成的成本得到。本文假设燃油货车、纯电动货车和氢燃料电池货车具有相同的无动力车身成本。

* 电池总是由多个单体电芯集合而成,加上电池管理系统、热管理系统等形成的能量储存单元。本文假设纯电动货车与氢燃料电池货车均采用能量型电池,且电池总能量密度相同。

* 电驱动系统包括电机、逆变器和变速箱。电驱动系统的质量根据电机的功率以及电驱动系统的功率密度(千瓦/千克)计算得到。

* 燃料电池系统由燃料电池电堆、燃料电池辅助系统(balance of plant)和DC/DC 转换器组成。燃料电池系统的质量由其质量功率密度决定。

* 储氢系统包括储氢瓶、阀门和传感器。储氢系统的质量取决于其质量储氢密度,即储存系统中可用氢的数量除以储存系统的总质量所得的值(USDOE t.d.)。

来源:作者基于 APCUK and Austin Power 2022、Beckmann et al. 2017、Cheng et al. 2024、China SAE 2021 和 2024、EC 2021、EUCAR 2019、Hsieh et al. 2019、Hydrogen Council 2020、IEA 2016、Macquarie 2021、Mast et al. 2021、MIT 2022、Nair et al. 2022、Pers. Comm. 2023c、Qiu et al. 2021、Sharpe and Basma 2022、Sinosynergy 2022、USDOE 2023、U.S. DRIVE 2017a 和 2017b、Xue and Liu 2022 的汇总。

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

13

## 2.3 新能源货车购置成本的计算方法

本文采用“自下而上”法，通过主要零部件的直接制造成本（DMC）、间接成本乘数（ICM）与增值税（VAT），计算新能源货车的购置成本（见公式2）。为简化计算，本文假设传统燃油货车的购置成本在未来十年保持不变。

$$Vehicle_{u,t} = Glider_u + DMC_{u,t} \times (1 + ICM\%) \times (1 + VAT\%)$$

$$DMC_{BET,u,t} = Battery\ cost_t \times E_{u,t}$$
$$+ Electric\ drive\ cost_t \times rated\ power_{u,t}$$
$$+ Other\ electrical\ component\ cost_u$$

$$DMC_{FCET,u,t} = Fuel\ cell\ system\ cost_t \times rated\ power_{u,t}$$
$$+ Hydrogen\ storage\ cost_t \times E_{u,t}$$
$$+ Electric\ drive\ cost_t \times rated\ power_{u,t}$$
$$+ Other\ electrical\ components\ cost_u$$

（公式2）

其中：

$Vehicle_{u,t}$ 表示车辆购置成本（元）；

$Glider_u$ 表示无动力车身成本（元）；

$DMC_{u,t}$ 表示新能源货车的直接制造成本（不含无动力车身）（元）；

$ICM$ 表示间接成本乘数（%）；

$VAT$ 表示增值税税率，本文采用13%（MOF, STA, and GACC 2019）；

$u$ 表示运输场景，$t$ 表示车型年份；

$E_{u,t}$ 表示电池容量或储氢容量（千瓦时或千克），见“新能源货车的电池容量与储氢容量”章节，了解计算方法和来源；

$Battery\ cost_t$、$Electric\ drive\ cost_t$、$Fuel\ cell\ system\ cost_t$、$Hydrogen\ storage\ cost_t$ 分别表示电池、电驱动系统、燃料电池系统、储氢系统的单位成本（元/千瓦时、元/千瓦、元/千瓦或元/千克），数据来源见表7；

$rated\ power_{u,t}$ 表示电驱动系统或燃料电池系统的额定功率（千瓦）；

$Other\ electrical\ components\ cost_u$ 表示其他零部件的成本，如车载充电机（OBC）、DC/DC转换器（元）$^{10}$。

技术进步对降低新能源货车的购置成本有重要作用。为反映技术进步（与规模效应）对降低新能源货车DMC的影响，本文采用学习曲线预测新能源货车各关键零部件的单位成本下降趋势。学习曲线为一类指数函数，可用于描述各零部件单位成本如何随累计产量的增长而快速下降。本文将各关键零部件单位成本的预测结果与文献进行对比、验证，

并调整预测结果。表7列出了各关键零部件的（如电池包、电驱动系统、燃料电池系统等）学习率曲线及单位成本的相关假设与数据来源。其中，本文中各关键零部件单位成本的学习率均取自文献。以电池包单位成本为例，2022年磷酸铁锂电池包单位成本为930元/千瓦时（China SAE 2021），比三元锂电池包便宜约20%（BNEF 2022）。在预测中，我们利用12%的电池包学习率（Hsieh et al. 2019），预测2030年电池包单位成本为680元/千瓦时，比2022年的水平下降27%。该预测结果处于现有研究预测值的中间水平，与《商用车碳中和技术路线图1.0》（China SAE 2024）以及美国环境保护署的《重型车辆第三阶段温室气体排放标准》（USEPA 2024）2030年预测值大致相当（见图3）。

ICM为间接成本乘数，包括研发费用和利润率等。ICM水平因国家、车辆技术路线而异，从2%到45%不等（Rogozhin et al. 2010）。虽然ICM也随技术进步而降低，但考虑到中国新能源货车主机厂的利润水平有限（FitchRatings 2022），本文采用16%的ICM（Orient Securities 2019），并假设该数值在MY2022—MY2030期间保持不变。

根据DMC与ICM的乘积，本文得到MY2022—MY2030新能源货车的购置成本。根据深圳市和佛山市相同配置新能源货车的建议零售价$^{11}$（Pers. Comm. 2023b），我们校验了本文测算的MY2022新能源货车购置成本，二者差异在10%以内，这表明上述计算方法与数据假设具备一定的可靠性。

在购置成本基础上，本文进一步计算MY2022—MY2030期间各场景购置新能源货车的一次性费用（包括车辆购置成本、税费与融资成本等）。值得指出的是，商业模式推广有助于缓解运输企业（尤其是利润较低、信用评级不高的小微运输企业）购置新能源货车的一次性费用，并将购置与持有新能源货车的风险，分摊给适宜承担这些风险的主体。因此，本文也简要分析了新能源货车商业模式对降低其初期一次性支出的作用。但由于数据限制，本文未评估商业模式推广对新能源货车TCO的影响。

14

WRI.org.cn

图 3 | 本文与现有文献中新能源货车关键零部件单位成本的预测

# a. 电池包

![img-22.jpeg](img-22.jpeg)

# b. 燃料电池系统

![img-23.jpeg](img-23.jpeg)

说明：红色虚线表示本文的预测，绿色和黄色曲线分别表示学术机构与企业的预测，紫色曲线表示政府部门与行业协会制定的目标。

来源：作者总结。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

15

## 2.4 新能源货车TCO的计算方法

新能源货车能否与同类燃油货车实现TCO平价，也是运输企业选择新能源货车的一个重要决策变量。因此，在计算新能源货车购置成本的基础上，本文进一步测算了MY2022—MY2030期间不同运输场景中新能源货车的TCO。

测算新能源货车TCO时，本文采用终端用户（即购车个人或企业）的视角，而非全社会的视角，因此，考虑了税费减免等政策对TCO的影响。基于分场景TCO预测结果，本文进一步分析新能源货车在近期推广过程中应优先考虑的运输场景、推广时间、新能源技术路线，以及有望将新能源货车与燃油货车实现TCO平价的时间提前的措施。

此外，考虑到中国货运行业高度分散、小微运输企业与个体司机众多的特点（TUC 2022a），本文选择从小微运输企业的角度测算TCO：一是本文中新能源货车的购置成本以小规模采购价格为准，而非大型企业采用的批量采购价格；二是货车融资成本与保险费用均设定在较高水平，以反映与小微运输企业的高风

险溢价（CFLP 2022）。最后，由于中国市场上的新能源货车以一手车为主，运输企业较少考虑购买二手或三手货车（Mihelic et al. 2020），所以，本文仅计算与对比一手货车的TCO。

值得注意的是，在中国新能源货车TCO成本要素选择方面，本文与现有文献（CATARC 2022; Mao et al. 2021）存在差异（见表8），特别是本文量化了载质量损失对应的成本以及关键零部件中期更换的成本。具体而言，本文测算的TCO涉及直接成本（如车辆购置成本、运营和维保成本、关键零部件中期更换成本）与机会成本（如载质量损失对应的成本）（见公式3）。由于数据可得性限制，其他诸如车辆残值和因补能时长带来的额外成本等，均未予考虑。

$$TCO_{p,u,t} = CAPEX_{p,u,t} + OPEX_{p,u,t} + Key\ component\ replacement_{p,u,t} + Payload_{p,u,t} = CAPEX_{p,u,t} + \sum_i [OPEX_{p,u,t,i}/(1+r)^{i-t}] + Key\ component\ replacement_{p,u,t} + Payload_{p,u,t} \quad (\text{公式3})$$

表 8 | 本文及现有文献中涉及的新能源货车TCO成本要素

|  TCO成本要素 |   | 是否常见 | 现有文献 | 本文范围  |
| --- | --- | --- | --- | --- |
|  车辆初期购买时的一次性费用支出 (CAPEX_{p,u,t}) | 购置成本(Vehicle_{p,u,t}) | 是 | 本文参考的文献都考虑这些成本要素 | √  |
|   |  融资成本(Financing_{p,u,t}) | 是 |   | √  |
|   |  购置税(Purchase tax_{p,u,t}) | 是 |   | √  |
|  运营成本 (OPEX_{p,u,t}) | 能源成本(Energy_{p,u,t}) | 是 |   | √  |
|   |  高速收费成本(Road charge_{p,u,t}) | 是 |   | √  |
|   |  维保成本(Maintenance_{p,u,t}) | 是 |   | √  |
|   |  保险成本(Insurance_{p,u,t}) | 是 |   | √  |
|   |  车船税(Ownership tax_{p,u,t}) | 是 |   | √  |
|   |  因补能带来的额外成本 | 否 | Hunter et al. (2021) | ×  |
|   |  车辆残值 | 否 | Ruf et al. (2020)、CARB (2019)、Basma et al. (2023)、Mao et al. (2021) | ×  |
|  关键零部件更换成本(Key component replacement_{p,u,t}) |   | 否 | CARB (2019)、Rout et al. (2022) | √  |
|  载质量损失成本(Payload_{ZET,u,t}) |   | 否 | Tol et al. (2022)、Hunter et al. (2021) | √  |
|  车辆使用年限(N) |   | 是 | 本文参考的文献都考虑这些成本要素 | √  |
|  贴现率(r) |   | 是 |   | √  |
|  年行驶里程(Annual kilometer traveled_{n}) |   | 是 |   | √  |

说明：p表示新能源货车技术路线，u表示运输场景，t表示车型年份。

来源：作者对 Basma et al. 2021 和 2023，Bumham et al. 2021、CARB 2019、CATARC 2022、Chen and Melaina 2019、Danebergs 2019、Hao et al. 2020, 2022、Hunter et al. 2021、Kast et al. 2017、König et al. 2021、Mao et al. 2021、Marcinikowski et al. 2016、Niu et al. 2023、Ouyang et al. 2021、Phadke et al. 2021、Qiu et al. 2021、Rout et al. 2022、Ruf et al. 2020、Sharpe and Basma 2022、Tol et al. 2022、Transport and Environment 2021、Van Velzen et al. 2019、Wu et al. 2015 和 Xie et al. 2023 等文献的汇总。

16

WRI.org.cn

其中：

$CAPEX_{p,u,t}$ 表示车辆初期购买时的一次性费用支出（元），包括车辆购置成本、购置税与融资成本等；

$OPEX_{p,u,t}$ 表示运营成本（元），包括能源成本、高速收费成本、维保成本、保险成本和车船税；

$Key\ component\ replacement_{p,u,t}$ 表示新能源货车关键零部件的更换成本（元），例如更换电池或燃料电池系统（请参阅“关键零部件更换成本计算方法”章节，了解计算方法和数据来源）；

$Payload_{ZET,u,t}$ 表示新能源货车的载质量损失成本（元），请参阅“新能源货车载质量损失货币化方法”，了解计算方法和数据来源；

$p$ 表示技术路线，$u$ 表示运输场景，$t$ 表示车型年份，$i$ 表示车辆购置年份，$N$ 表示车辆使用年限，$r$ 表示贴现率。

本文中的TCO以净现值形式表示。在贴现率方面，考虑到私营部门通常使用较高的贴现率，而公共部门的贴现率较低（CARB 2019），因此，本文采用了7%的私营部门贴现率（Basma et al. 2023; Hunter et al. 2021; Meszler et al. 2019）。

## 新能源货车载质量损失货币化方法

本文调研的运输企业指出，新能源货车的载质量损失会造成收入损失（甚至客户流失）。本文不考虑运输企业的收入，因此将新能源货车的载质量损失货币化并计入TCO中。

现有文献中，将新能源货车载质量损失对TCO的影响货币化的方法有四种（Hunter et al. 2021），包括购买额外的（新能源）货车、租用额外的（新能源）货车、额外增加（新能源货车）的运营趟次/里程，以及雇用其他（新能源货车）车队等。

本文选择第三种方法，即额外增加新能源货车的运营趟次/里程。其原因是：对小微运输企业而言，相较其他方法，增加运营趟次/里程成本更低廉、更可行（Hunter et al. 2021）。此外，鉴于增加的额外运营趟次/里程中，新能源货车并非总是满载运行，所以，本文采用文献中不同货车车型的空驶率（27%~36%）（TUC 2022b），以更准确地反映新能源货车载质量损失对TCO的影响（见公式4）。

$$Payload_{u,t} = \left[ \frac{PC_{ICEV}}{PC_{ZET}} \times (1 - M_u) + M_u - 1 \right] \times (Energy_{u,t} + Road\ charge_{u,t} + Maintenance_{u,t}) \quad (\text{公式4})$$

其中：

$Payload_{ZET,u,t}$ 表示新能源货车载质量损失对应的成本（元）；$PC_{ICEV}$ 表示燃油货车的载质量（千克），$PC_{ZET}$ 表示新能源货车的载质量（千克），具体计算方法与数据

来源请参阅“新能源货车的整备质量与载质量损失”章节；

$M_u$ 表示空驶率（%）；

$Energy_{u,t}$、$Road\ charge_{u,t}$、$Maintenance_{u,t}$ 表示新能源货车的能源成本、高速收费成本和维保成本（元），具体数据来源请参阅“其他成本要素的测算方法”章节；

$u$ 表示运输场景，$t$ 表示车型年份。

## 关键零部件更换成本计算方法

新能源货车的关键零部件不仅价格高，且使用寿命有限，因此，在测算新能源货车TCO时，需要考虑使用周期内关键零部件的更换成本。

在计算关键零部件更换成本时，首先需确定是否要更换零部件以及零部件的更换费用由哪一方承担。对于燃油货车而言，由于中国市场上燃油货车的使用年限较短（5~6年）（Pers. Comm. 2023a），本文不考虑燃油货车使用中期维修与零部件更换的费用。对于纯电动货车而言，根据MOF et al.（2018）的要求，主机广必须提供五年或最高200,000千米的质保，比本文纯电动货车的使用年限（5~6年）和累计行驶里程（250,000~900,000千米）更短，因此，使用过程中可能需要为更换一次电池。对于氢燃料电池货车而言，虽然氢燃料电池货车也需要中期翻新或更换燃料电池电堆，但主机厂与燃料电池系统集成商为加强市场竞争力，通常会主动承担这部分成本（Pers. Comm. 2023c）。因此，本文未考虑氢燃料电池货车的关键零部件更换成本。

针对纯电动货车，本文使用3000~4000等效全区间循环次数（EFC）作为电池更换的阈值。研究表明，如果环境温度和充放电倍率适中，磷酸铁锂电池可以维持3000~4000等效全区间循环次数（Jenu et al. 2018, 2022; Xue et al. 2020）。所以，如果日充电一到两次$^{12}$，纯电动货车的等效全区间循环次数为1440~2880次（假设放电深度为80%），不会触发电池更换。只有在每天充电次数超过两次时，纯电动货车才可能需要更换电池。为简化计算，本文中的电池更换成本等于购置纯电动货车时电池包的成本$^{13}$。

## 其他成本要素的测算方法

**能源成本** 通过车辆能量消耗量及能源价格进行测算。其中，本文对燃油价格、充电价格与氢气价格的假设如下：

- 充电价格包括电价与充电服务费，二者分别取决于当地电价机制与充电基础设施的交付机制。在电价方面，深圳市、佛山市的工商业及大工业电价均采用峰谷电价；此外，两个城市也免除了新能源货车充电的

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

17

需量电费（Guangdong DRC 2018）。在充电服务费方面，不同的充电桩投资与交付机制会产生不同的充电服务费，本文主要考虑新能源货车常见充电场所（公共充电桩）的充电服务费，即考虑第三方投资建设、运营成本与利润。为获得本地平均充电价格（含电费与充电服务费），本文在高德地图$^{14}$上随机选择深圳市和佛山市的50个可供新能源货车充电的公共充电站，记录了其一天中不同时间的充电价格，得到平均充电价格为1.2元/千瓦时。在此基础上，本文将该充电价格与运输企业调研的充电价格进行对比（Pers. Comm. 2023a）。我们假设该充电价格在MY2022—MY2030保持不变$^{15}$。

- 本文假设氢气的枪口端加氢价格已包含加氢站以及相关基础设施的投资。考虑到广东省2022年的灰氢枪口价格为55~70元/千克（Pers. Comm. 2023a），本文中，2022年氢气价格设置为55元/千克。本文进一步假设到2030年，氢气价格将线性下降至30元/千克。值得注意的是，由于2030年可再生能源电解水制氢的价格难以达到30元/千克，所以，与燃油货车相比，使用灰氢的氢燃料电池货车未必能降低碳排放（WEF 2023）。
- 广东省2022年的柴油年平均价格为8.1元/升（Eastmoney 2022），本文假设此价格在未来保持不变。

值得注意的是，采用混合动力系统的氢燃料电池货车可在纯氢模式或插电式混合动力两种模式下运行，这两种模式对应的能源成本不同（Pers. Comm. 2023c）。在纯氢模式下，氢燃料电池货车仅从储氢瓶中获取能量，因此，能源成本仅为加氢成本。而在插电式混合动力模式下，氢燃料电池货车同时从储氢瓶和电池中获取能量，因此，能源成本包括加氢成本和充电成本。为此，针对混动氢燃料货车，本文测算了其在两种模式的TCO；其中，对插电式混合动力模式，我们假设氢燃料电池货车每天会耗尽电池能量并会再次充满电。

本文中车辆**维保成本与保险成本**分别按行驶距离与使用年限计算，并随货车车型与货车技术路线而异。尽管目前在一些情况下，新能源货车的维保成本高于燃油货车（Pers. Comm. 2023a），但未来，其维保成本将低于燃油货车（Burnham et al. 2021）。本文中，新能源货车的维保成本取调研中较低的水平，以反映新能源货车更低的维保成本（Pers. Comm. 2023a; 2023b）。与维保成本不同，由于受损部件的维修成本较高，加之保险公司评估新能源货车风险和损失的数据不足（CARB 2021a），新能源货车的保险成本将始终高于燃油货车的保险成本。本文中，新能源货车保险成本同样来自运输企业调研，并比燃油货车高出2000至10000元（Pers. Comm. 2023a）。本文假设两项成本在未来保持不变。

**车辆税费和高速收费**如表9和表10所示。

表 9 | 本文中燃油货车、纯电动货车与氢燃料电池货车的维保成本、保险成本及相关税费说明

|  货车车型 | 技术 | 维保成本（元/100千米） | 保险成本（元/年） | 车船税（元/吨/年） | 购置税（元）  |
| --- | --- | --- | --- | --- | --- |
|  4.5吨轻型普通货车 | ICEV | 20 | 13,000 | 16 | 车辆购置成本 / （1+增值税%） × 10%  |
|   |  BET | 18 | 16,000  |   |   |
|   |  FCET | 18 | 20,000  |   |   |
|  18吨载货汽车 | ICEV | 67 | 17,500  |   |   |
|   |  BET | 50 | 24,000  |   |   |
|   |  FCET | 50 | 24,000  |   |   |
|  31吨自卸汽车 | ICEV | 70 | 20,000  |   |   |
|   |  BET | 65 | 30,000  |   |   |
|   |  FCET | 65 | 30,000  |   |   |
|  42吨半挂牵引车 | ICEV | 67 | 20,000  |   |   |
|   |  BET | 50 | 30,000  |   |   |
|   |  FCET | 50 | 30,000  |   |   |
|  来源 |   | 作者对运输企业和货车经销商的调研 （Pers. Comm. 2023a; 2023b） |   | 广东省车船税政策 （Guangdong Government 2022） | 《中华人民共和国车辆购置税法》 （NPC 2018）  |

说明：本表未含该车装置的车船税。

缩略词：ICEV=燃油汽车；BET=纯电动货车；FCET=氢燃料电池货车。

18

WRI.org.cn

表 10 | 广东省燃油货车、纯电动货车和氢燃料电池货车的高速收费

|  货车车型 | 轴数 | 行驶工况 | 高速收费（元/千米） | 高速公路行驶里程占比（%）  |
| --- | --- | --- | --- | --- |
|  4.5吨轻型普通货车 | 2 | UD | 0.52 | 20%  |
|   |   |  RD |   | 40%  |
|  18吨载货汽车 | 2 | UD | 1.09 | 20%  |
|   |   |  RD |   | 50%  |
|  31吨自卸汽车 | 4 | UD | 1.95 | 0%  |
|  42吨半挂牵引车 | 5 | UD | 2.01 | 20%  |
|   |   |  RD |   | 60%  |
|   |   |  DDC |   | 60%  |
|  来源 |   |   | 《广东省收费公路收费标准》（Guangdong DOT 2020） | 《重型商用车辆燃料消耗量测量方法》（GB 27840—2011）（AQSIQ and SAC 2011）  |

说明：高速收费的货车不同车辆的技术路线而异。

缩略词：UD=城市运输；RD=区域运输；DDC=集疏港运输。

**融资成本**根据车辆购置成本计算得出。考虑到银行贷款是目前中国较常见的货车融资方式，因此，本文根据中国人民银行和中国银行业监督管理委员会规定的最低首付比例，确定燃油货车贷款的首付款为车价的30%，新能源货车贷款的首付款为车价的25%（PBC and CBIRC 2017）。考虑小微运输企业融资成本高，所以，本文将货车贷款利率设为10%，贷款期限为三年（Pers. Comm. 2023b）。

值得注意的是，本文假设除氢气价格外，其他成本或费率不会随时间而变化。考虑到能源成本占新能源货车TCO的比例较高，且能源价格随时间波动（NDRC 2021），因此，本文也采用敏感度分析，计算能源价格变化对新能源货车实现TCO平价时间的影响。

**政策影响：**鉴于政策有助于缩小新能源货车与燃油货车的TCO差距，本文也量化各种政策（含已出台或尚未出台的政策）对降低新能源货车TCO所发挥的作用。

基于政策文件和文献总结，本文梳理了国家与地方政府以及行业可能采取的激励新能源货车推广的措施，包括经济激励、政策法规与基础设施配套措施等。出于简化，我们侧重本文TCO框架可量化的国家与地方的八项政策，包括购置补贴、税费减免、能源（充电/加氢）补贴、碳价、优先路权、减少高速收费、提高最大设计总质量与降低融资成本。

本文以减少政府财政支出为原则，结合实际情况，假设未来这八项政策的力度。除补贴政策外，本文对纯电动货车与氢燃料电池货车设定了相同的政策与力度，以便比较同一政策对两种新能源技术的不同影响。考虑到氢燃料电池货车尚处于推广的初期阶段，本文为氢燃料电池货车设置了更高的购置补贴与加氢补贴。

值得注意的是，本文只评估各政策措施对新能源货车提前实现与燃油货车TCO平价年份的影响，但无法评估其对提高新能源货车市场渗透率的影响。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

19

## 第三章

# 研究结果

### 3.1 2022年各场景结果

#### 2022年新能源货车各场景的运营可行性

本文对2022年《车型目录》(MIIT 2022)中主流新能源货车技术参数(见表11)的分析显示,2022年,新能源货车仅能满足部分城市运输场景的运营要求,在一些场景(如区域运输场景)中,新能源货车仍面临续航里程不足、载质量损失与电机峰值功率不足的问题:

#### ■ 续航里程不足

在城市运输场景中,纯电动货车可满足短日行驶里程的运营要求,但日行驶里程更长时(如200~300千米),仍面临续航里程的限制。为此,在实际应用中,一些运输企业通过调整运营组织,如将纯电动货车部署到日行驶里程较短的路线(而在较长的路线中仍使用燃油货车),实现部分电动化;另一些运输企业尽管实现了城市运输场景的全面电动化,但无法实现纯电动货车与燃油货车的一比一替代,即需要更多的纯电动货车,才能满足与燃油车队相同的运营要求(Pers. Comm. 2023a)。

氢燃料电池货车的实际续航里程比纯电动货车更长,能满足所有城市运输场景的运营需求,但在区域运输场景仍有瓶颈。例如,4.5吨轻型燃料电池货车的续航里程约为348千米,无法满足区域运输场景300~500千米日行驶里程的要求。

#### ■ 载质量损失

2022年,正向开发的新能源货车车型数量少$^{16}$,因此,其参数配置并未经过优化,面临突出的载质量损失问题(Pers. Comm. 2023c)。本研究分析显示,相较于重型货车,4.5吨轻型普通货车的载质量损失问题更为严重:新能源4.5吨轻型普通货车的载质量比同类型燃油货车低26%~42%。其中,氢燃料电池货车的载质量损失最显著——载质量仅为同类型燃油货车的一半左右。

随着最大设计总质量的增加,新能源货车载质量损失的问题将逐渐得到缓解。例如,新能源18吨载货汽车的载质量比燃油18吨载货汽车低15%,而新能源42吨半挂牵引车的载质量仅比燃油42吨半挂牵引车低5%。

#### ■ 电机峰值功率不足

除燃料电池自卸汽车外,多数2022年的新能源货车能满足运输场景的峰值功率需求。由于国家氢燃料电池汽车示范城市群项目的购置补贴与燃料电池系统的额定功率挂钩(补贴上限为110千瓦)(Guangdong DRC et al. 2022),燃料电池系统功率多不超过110千瓦(MIIT 2022),以最大限度地获得补贴并降低制造企业的成本。本研究对运输企业调研显示,2022年,配备110千瓦燃料电池系统与127千瓦时电池包(2C充放电倍率)的自卸汽车,电机峰值功率可达364千瓦。但在一些情况下,该车型无法满足建筑工地或建筑垃圾消纳场满载爬坡的峰值功率要求(Pers. Comm. 2023a)。

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

21

表 11 | 2022年新能源货车的技术参数

|  货车车型 | 最大设计总质量(千克) | 纯电动货车 |   |   |   |   | 氢燃料电池货车  |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   |   |  电池容量(千瓦时) | 电机额定/峰值功率(千瓦) | 最大载荷量(千克)^{1} | 实际续航里程(千米)^{2} | 运输场景 | 储氢容量(千克) | 电池容量(千瓦时) | 燃料电池系统额定功率(千瓦) | 最大载荷量(千克)^{3} | 实际续航里程(千米)^{2} | 运输场景  |
|  微面、中面 | 3,495 (4×2) | 42~50 | 30/60 | 960~1,315 | 161~186 | 部分UD | N.A. | N.A. | N.A. | N.A. | N.A. | N.A.  |
|  轻型普通货车 | 4,495 (4×2) | 81 | 60/120 | 1,251 (-26%) | 185~196 | UD | 9 | 30 | 84 | 978 (-42%) | 约348 | UD和部分RD  |
|  载货汽车 | 18,000 (4×2) | 247 | 90/171 | 7,927 (-15%) | 195~228 | UD | 30 | 105 | 102 | 7,952 (-15%) | 约464 | UD和部分RD  |
|  自卸汽车 | 31,000 (8×4) | 423 | 270/405 | 12,230 (-20%) | 约200 | UD | 40 | 127 | 110 | 13,193 (-14%) | 约358 | UD  |
|  半挂牵引车^{4} | 42,000 (4×2) | 282 | 250/360 | 25,257 (-5%) | 134~205 | UD、部分DDC和PO | 36 | 100 | 110 | 25,489 (-4%) | 255~471 | UD、PO、部分RD和DDC  |

说明：$^{1}$ 拥号中的百分比表示新能源货车的载重量损失占燃油货车最大载荷量的比例。

$^{2}$ 纯电动货车的实际续航里程根据电池容量、纯电深度与纯电动货车载荷消耗量计算得到；氢燃料电池货车的实际续航里程根据储氢容量、氢燃料电池货车的可用容量与纯氢模式下的能量消耗量计算得到。

$^{3}$ 在深圳港港口内运输的场景中，纯电动半挂牵引车采用的是换电货车。

缩略词：UD=城市运输；RD=区域运输；DDC=集疏港运输；N.A.=不适用。

来源：作者基于对运输企业的调研（Pers. Comm. 2023a，见附表B）和《车型目录》（MIT 2022）总结。

## 2022年新能源货车购置成本与TCO

根据货车经销商平台的公开数据（360che n.d.）与本研究对运输企业的调研（Pers. Comm. 2023a），本文计算了2022年新能源货车与燃油货车购置成本的差异（基于表11的技术参数）。结果显示，2022年，各场景下，纯电动货车的购置成本比燃油货车高58%~113%，而氢燃料电池货车的购置成本更昂贵，比燃油货车高272%~482%（见表12）。然而，如果采用换电重卡的“车电分离、电池租赁”模式，则纯电动货车无电池车身的购置成本与燃油货车几乎相当。

基于购置成本，本文进而计算了2022年新能源货车在城市运输、港口内运输与集疏港运输场景中的TCO（假设日行驶里程均为200千米）。考虑到2022年新能源货车无法满足区域运输场景的运营要求，因此，本研究未计算该场景的TCO。此外，计算中，本文也考虑了深圳市和佛山市目前的新能源货车推广政策对TCO的影响。其结果显示：

对纯电动货车而言，在港口内运输场景以及城市运输场景的轻微货运输时，纯电动货车的TCO已低于或接近燃油货车TCO；而在城市运输场景的重货运输及集疏港运输场景时，纯电动货车的TCO仍高于燃油货车。

对氢燃料电池货车而言，即使考虑到广东省氢燃料电池汽车示范城市群的购置补贴与运营补贴，2022年氢燃料电池货车的TCO仍然比燃油货车高出55万至60万元（港口内运输场景除外），其主要原因如下：一是氢燃料电池货车的购置成本较高；二是氢气价格高（2022年55元/千克）；三是非正向开发的氢燃料电池汽车面临较高的载质量损失；四是广东省的氢燃料电池汽车示范城市群补贴金额有限（见图4、图5和图6）。例如，北京市大兴区31吨氢燃料电池自卸汽车可获得的国家、市级和区级补贴总计约200万元（Beijing Daxing Government 2022; Beijing MEITB 2022），比佛山市的补贴金额高出150%。在这一补贴水平下，北京市大兴区2022年氢燃料电池自卸汽车的TCO比燃油车低65万元（见图5）。

另外，值得注意的是：

- ■ 首先，深圳市和佛山市政府的纯电动货车补贴多应用于接近TCO平价或已实现TCO平价的场景，如城市运输场景的4.5吨轻型普通货车、港口内运输场景的42吨半挂牵引车。其中，佛山市的运营补贴（单车约5.4万元）有助于降低城市运输场景的重货运输中纯电动轻型货车与燃油轻型货车的TCO差价。由

22

WRI.org.cn

于纯电动半挂牵引车在港口内运输场景中已实现与燃油货车的TCO平价，因此，深圳市为港口内运输场景提供的纯电动半挂牵引车购置补贴（单车5万元）有助于降低纯电动半挂牵引车的购置成本。

■ 其次，尽管纯电动18吨载货汽车与纯电动42吨半挂牵引车已在城市运输（轻抛货运输）中实现与燃油货车的TCO平价，但其实际应用有限（Pers. Comm. 2023a）。其原因可能是：一是新能源货车的车型有限（MIT 2022）；二是这些新能源货车面临跨场景运输需要，而其在跨场景运输中仍存在技术与成本阻碍。

表 12 | 2022年政策激励下新能源货车与燃油货车的TCO差价

|  运输场景 | 货物类别 | 纯电动货车与燃油货车的TCO差价 (元) |   | 氢燃料电池货车与燃油货车的TCO差价 (元)  |   |
| --- | --- | --- | --- | --- | --- |
|   |   |  深圳市 | 佛山市 | 深圳市 | 佛山市^{1}  |
|  **桶面、中面**  |   |   |   |   |   |
|  UD | 跨货类 | -65,703 (-19%) | -83,703 (-24%) | N.A. | N.A.  |
|  **4.5吨轻型普通货车**  |   |   |   |   |   |
|  UD | 轻抛货 | -43,572 (-8%) | -97,572 (-17%) | 279,989 (49%) | 54,989 (10%)  |
|   |  重货 | 24,051 (4%) | -29,949 (-5%) | 403,833 (70%) | 178,833 (31%)  |
|  **18吨载货汽车**  |   |   |   |   |   |
|  UD | 轻抛货 | -6,157 (-1%) | -6,157 (-1%) | 478,911 (40%) | 448,911 (38%)  |
|   |  重货 | 32,327 (3%) | 32,327 (3%) | 462,616 (36%) | 432,616 (33%)  |
|  **31吨自卸汽车**  |   |   |   |   |   |
|  UD | 重货 | 238,931 (15%) | 238,931 (15%) | 574,447 (36%) | 504,447 (32%)  |
|  **42吨半挂牵引车**  |   |   |   |   |   |
|  UD | 轻抛货 | 11,234 (1%) | -11,234 (1%) | 476,719 (30%) | 406,719 (26%)  |
|  PO | 轻抛货 | -392,009 (-17%) | -142,009 (-6%) | -11,606 (-1%) | 166,394 (7%)  |
|  DDC | 轻抛货 | 202,150 (12%) | 202,150 (12%) | 596,407 (35%) | 596,407 (35%)  |

说明：$^{1}$ 拓号中的比例代表新能源货车TCO与燃油货车TCO之差占燃油货车TCO的比例。

$^{2}$ 表中假设所有运输场景的日行数里程为200千米；除31吨自卸汽车的使用年限为五年以外，其他所有车型的使用年限均为六年（Pers. Comm. 2023a）。

$^{3}$ 佛山市没有港口，因此在计算港口内运输场景和集疏港运输场景中的TCO时，使用了中国其他港口城市的数据，以反映不实地任何新能源货车推广政策时的TCO。

缩略词：UD=城市运输；PO=港口内运输；DDC=集疏港运输；N.A.=不适用。

来源：作者计算。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

23

图 4 | 2022年4.5吨轻型普通货车的TCO:深圳市和佛山市城市运输场景

■ 成本要素 ■ 未实行政策激励时的新能源货车TCO ■ 政策激励 ■ 实行政策激励后的新能源货车TCO ■ 燃油货车TCO

# 1) 轻抛货

# a. 纯电动货车

![img-24.jpeg](img-24.jpeg)

# b. 氢燃料电池货车

![img-25.jpeg](img-25.jpeg)

# 2) 重货

# a. 纯电动货车

![img-26.jpeg](img-26.jpeg)

# b. 氢燃料电池货车

![img-27.jpeg](img-27.jpeg)

说明：图中假设所有运输场景的日行便里程均为 200 千米，轻型货车使用年限为六年（Pers.Comm.2023a）。
来源：作者计算。

24

WRI.org.cn

图 5 | 2022年31吨氢燃料电池自卸汽车的TCO:深圳市、佛山市和北京市大兴区城市运输场景

![img-28.jpeg](img-28.jpeg)

说明：图中假设所有运输场景的日行驶里程均为 200 千米，31 吨自卸汽车的使用年限为五年（Pers Comm 2023a）。
来源：作者计算。

图 6 | 2022年42吨半挂牵引车的TCO:深圳市与中国其他城市港口内运输场景

![img-29.jpeg](img-29.jpeg)

说明：图中假设所有运输场景的日行驶里程均为 200 千米，42 吨半挂牵引车的使用年限为六年（Pers Comm 2023a）。
来源：作者计算。

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

25

## 3.2 MY2022—MY2030各场景结果

# MY2022—MY2030新能源货车关键零部件参数设置

在“新能源货车关键零部件参数设置方法”的基础上，本节设置了各场景新能源货车关键零部件的技术参数——包括电池容量、燃料电池系统的功率与储氢容量，以满足MY2022—MY2030不同运输场景的续航里程与电机峰值功率的要求。在此基础上，本文也考虑技术进步与运营优化对新能源货车关键零部件参数设置的影响。

纯电动货车零部件参数设置：电池容量的增加加剧载质量损失

2022年，纯电动货车只能满足部分的城市运输场景运营要求，因此，需要通过增加电池容量，才能满足各运输场景MY2022—MY2030的运营要求。

“新能源货车关键零部件参数设置方法”提出了两种配置纯电动货车电池容量的方法，不同运输场景选择配置方法的依据如下：

对于城市运输场景和区域运输场景，本文采用“日行驶里程”法，因为城市运输场景和区域运输场景下，起始地与目的地众多，具有不确定性，加之运营时刻表不固定，且短时间内市场难以在较大区域部署充足的充电基础设施。因此，纯电动货车需要采用“日行驶里程”法配置电池容量，即每天在物流场站或停车场进行一次（夜间）充电，保证一天的运营需求。

对于港口内运输场景和集疏港运输场景，本文采用“日行驶里程”法和“单程运距”法两种方法。采用“单程运距”法是由于这些场景中的起始点/目的地以及运营时刻表相对固定，车辆会定期返回港口，并在相对较小的区域范围内运营。因此，除“日行驶里程”法外，运输企业也可根据“单程运距”法配置电池容量，并在港口附近、客户工厂停车场、物流节点等关键地点部署充电基础设施，优化运营时刻表，确保纯电动货车在不影响运营的条件下，有足够的时间窗充电。

例如，在集疏港运输场景中，若在中途、港口或工厂停车场附近安装快充桩，一辆续航里程为200千米的纯电动半挂牵引车（BET200）利用中途休息时间、进港口等待时间、

图 7 | 纯电动半挂牵引车BET200在集疏港运输场景的不同运营与充电方案

a. DDC_TRIP（日行驶里程=200千米）：
一天一充

![img-30.jpeg](img-30.jpeg)

b. DDC_TRIP（日行驶里程=400千米）：
一天两充

![img-31.jpeg](img-31.jpeg)

c. DDC_TRIP（日行驶里程=500千米）：
一天三充

![img-32.jpeg](img-32.jpeg)

缩略词：按7：纯电动货车；DDC_TRIP：集疏港运输（“单程运距”法）。
来源：作者基于对运输企业的调研总结（Pers.Comm.2023a，见附表8）。

26

WRI.org.cn

装卸货等待时间进行日间1~2次快速补电，日行驶里程可达到约400~500千米（见图7）。考虑到深圳港集疏港运输场景中，多数半挂牵引车的单程运距不超过200千米（Wang et al. 2024），本文假设在港口内运输场景、集疏港运输场景中使用“单程运距”法时，纯电动货车的续航里程为200千米（即采用BET200）。

基于上述纯电动货车电池容量配置的方法，纯电动货车在MY2022—MY2030的电池容量设置如下：

在采用“日行驶里程”法的城市运输场景与区域运输场景中，纯电动货车MY2022—MY2030电池容量将较2022年显著增加。以4.5吨轻型普通货车为例，在城市运输场景中，其电池容量将从2022年的81千瓦时增加至MY2025的88~139千瓦时，比2022年增加了8%~71%；而在区域运输场景中，其电池容量将比城市运输场景更高，达到148~255千瓦时，较2022年增加83%~215%。

随着电池容量增加，纯电动货车的载质量损失问题也更加突出。尽管技术进步（如电池能量密度与车辆能量消耗量的改善）能在一定程度上缓解纯电动货车的载质量损失问题，但在一些场景中，因电池容量增加而加重的电池质量，

正抵消技术进步减轻的电池质量，导致更突出的载质量损失问题。其中，纯电动轻型货车的载质量损失问题在区域运输场景中尤为明显。例如，区域运输场景中，MY2025纯电动轻型货车（电池容量为148~255千瓦时）的载质量将比燃油轻型货车少36%~69%。然而，随着最大设计总质量增加，纯电动货车的载质量损失问题将得到缓解。例如，同样在区域运输场景中，MY2025的42吨纯电动半挂牵引车的载质量仅比同类燃油车辆少3%~8%。

在港口内运输和集疏港运输场景中，“日行驶里程”法和“单程运距”法会对纯电动货车的电池容量和载质量损失产生不同影响。“单程运距法”通过设置较小容量的电池，能较好缓解纯电动货车的载质量损失问题。以集疏港运输为例，如果采用“单程运距”法，MY2025的42吨半挂牵引车搭载288千瓦时电池时，即可实现300~500千米的日行驶里程，与燃油货车相比无载质量损失。而采用“日行驶里程”法，MY2025的42吨半挂牵引车则需要432~720千瓦时的电池容量才能完成运营要求，相对燃油货车的载质量损失达3%~8%。

MY 2025和MY2030纯电动货车的电池容量如图8所示，MY2025和MY2030纯电动货车相较燃油货车的载质量损失如图9所示。

图 8 | MY2025和MY2030纯电动货车的电池容量

a. 4.5吨轻型普通货车

![img-33.jpeg](img-33.jpeg)

b. 18吨载货汽车

![img-34.jpeg](img-34.jpeg)

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

27

图 8 | MY2025和MY2030纯电动货车的电池容量 (续)

# c. 31吨自卸汽车

![img-35.jpeg](img-35.jpeg)

# d. 42吨半挂牵引车

![img-36.jpeg](img-36.jpeg)

|   | MY2025 |   | MY2030  |   |
| --- | --- | --- | --- | --- |
|   |  与2022年的差异^{a} | 同一场景内差异 (千瓦时) | 与2022年的差异^{a} | 同一场景内差异 (千瓦时)  |
|  **轻型普通货车**  |   |   |   |   |
|  UD | 8%~71% | 51 | -1%~57% | 47  |
|  RD | 83%~215% | 107 | 67%~189% | 98  |
|  **重型载货汽车**  |   |   |   |   |
|  UD | -15%~51% | 160 | -17%~46% | 156  |
|  RD | 51%~181% | 322 | 46%~172% | 311  |
|  **重型自卸汽车**  |   |   |   |   |
|  UD | -5%~42% | 201 | -9%~36% | 192  |
|  **重型半挂牵引车**  |   |   |   |   |
|  UD | -4%~43% | 135 | -8%~38% | 130  |
|  RD | 53%~155% | 288 | 47%~145% | 277  |
|  PO_DVKT | 46%~119% | 206 | 41%~111% | 198  |
|  PO_TRIP | 46% | 0 | 41% | 0  |
|  DDC_DVKT | 2%~155% | 432 | -2%~145% | 415  |
|  DDC_TRIP | 2% | 0 | -2% | 0  |

说明：$^{a}$“与2022年的差异”一词中百分比代表 MY2025 或 MY2030 纯电动货车的电池容量与 2022 年之差较 2022 年水平的比值。

$^{b}$对于 PO_TRIP 和 DDC_TRIP，单程运距固定在 200 千米，因此，根据 200 千米的续航里程配置电池容量。

附略词：BET=纯电动货车；UD=城市运输；RD=区域运输；PO_DVKT=港口内运输（“日行便里程”法）；PO_TRIP=港口内运输（“单程运距”法）；DDC_DVKT=集疏港运输（“日行便里程”法）；DDC_TRIP=集疏港运输（“单程运距”法）。

来源：作者计算。

28

WRI.org.cn

图 9 | MY2025和MY2030纯电动货车相较燃油货车的载质量损失

# a. 4.5吨轻型普通货车

![img-37.jpeg](img-37.jpeg)

# b. 18吨载货汽车

![img-38.jpeg](img-38.jpeg)

# c. 31吨自卸汽车

![img-39.jpeg](img-39.jpeg)

# d. 42吨半挂牵引车

![img-40.jpeg](img-40.jpeg)

缩略词：BET=纯电动货车；UD=城市运输；RD=区域运输；PO_DVKT=港口内运输（“日行便里程”法）；PO_TRIP=港口内运输（“单程运距”法）；DDC_DVKT=集疏港运输（“日行便里程”法）；DDC_TRIP=集疏港运输（“单程运距”法）。

来源：作者计算。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

29

氢燃料电池货车的零部件参数设置：储氢容量几乎不需要增加，且载质量损失有限

与纯电动货车不同，氢燃料电池货车的车载储氢系统在MY2022—MY2030期间，几乎不需要增加太多容量（MY2025相较2022年增加2%~34%），即可满足所有运输场景的要求。例如，对区域运输场景中的18吨载货汽车而言，储氢容量只需从30千克增加为31千克，即可满足500千米的日行驶里程要求（储氢容量的增幅仅为4%）。唯一需要大幅增加储氢容量的场景是区域运输场景中的4.5吨轻型普通货车；其储氢容量需从2022年的9千克增加到MY2025的12千克，才能满足500千米的日行驶里程要求（储氢容量的增幅达34%）。

除了储氢容量外，燃料电池系统的功率也需要提升，才能满足个别场景的要求——特别是氢燃料电池自卸汽车的场景。本文假设MY2022—MY2030期间，如果氢燃料电池自卸汽车仍配备127千瓦时电池（充电倍率为2C），那么，其

燃料电池系统的额定功率需要从110千瓦提升到151千瓦，才能满足一些自卸货车运输场景405千瓦电机峰值功率的需求（Pers. Comm. 2023a）。

与纯电动货车不同，增加储氢容量与燃料电池系统功率，对氢燃料电池货车载质量损失的影响有限。随着未来车辆正向开发（Mauro Erriquez et al. 2017）、车身结构材料轻量化、储氢系统的质量储氢密度提高，氢燃料电池货车的载质量损失将得到大幅缓解。虽然氢燃料电池轻型货车在区域运输场景中的载质量损失仍最高，但到MY2030，区域运输场景中，氢燃料电池轻型货车较燃油轻型货车的载质量损失将降至8%~14%，较2022年42%有较大改善。另外，值得注意的是，到MY2030，氢燃料电池重型货车（如自卸汽车、半挂牵引车）将不再面临任何载质量损失问题。

MY2025和MY2030氢燃料电池货车的车载储氢系统容量如图10所示，MY2025和MY2030氢燃料电池货车与燃油货车载质量损失如图11所示。

图 10 | MY2025和MY2030氢燃料电池货车的车载储氢系统容量

■ 2022 ■ UD ■ PO_DVKT ■ RD ■ DDC_DVKT

a. 4.5吨轻型普通货车

![img-41.jpeg](img-41.jpeg)

b. 18吨载货汽车

![img-42.jpeg](img-42.jpeg)

30

WRI.org.cn

图 10 | MY2025和MY2030氢燃料电池货车的车载储氢系统容量(续)

# c. 31吨自卸汽车

![img-43.jpeg](img-43.jpeg)

# d. 42吨半挂牵引车

![img-44.jpeg](img-44.jpeg)

|   | MY2025 |   | MY2030  |   |
| --- | --- | --- | --- | --- |
|   |  与2022年的差异 | 同一场景内差异 (千克) | 与2022年的差异 | 同一场景内差异 (千克)  |
|  **轻型普通货车**  |   |   |   |   |
|  UD | -46%~-20% | 2.4 | -53%~-29% | 2.2  |
|  RD | -31%~34% | 4.8 | -29%~18% | 4.2  |
|  **重型载货汽车**  |   |   |   |   |
|  UD | -59%~-38% | 6.2 | -61%~-42% | 5.8  |
|  RD | -38%~4% | 12.4 | -42%~-3% | 11.7  |
|  **重型自卸汽车**  |   |   |   |   |
|  UD | -45%~-18% | 11.0 | -47%~-21% | 10.6  |
|  **重型半挂牵引车**  |   |   |   |   |
|  UD | -59%~-39% | 7.4 | -62%~-43% | 6.9  |
|  PO_DVKT | -23%~15% | 13.8 | -26%~11% | 13.4  |
|  RD | -39%~2% | 14.7 | -4%~-43% | 13.8  |
|  DDC_DVKT | -59%~2% | 22.1 | -62%~-4% | 20.7  |

说明：“与 2022 年的差异”一词中的百分比分别代表 MY2025 或 MY2030 氢燃料电池货车的车载储氢系统容量与 2022 年之差较 2022 年水平的比值。

缩略词：FCET=氢燃料电池货车；UD=城市运输；RD=区域运输；PO_DVKT=港口内运输（“日行驶里程”法）；DDC_DVKT=集疏港运输（“日行驶里程”法）。

来源：作者计算。

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

31

图 11 | MY2025和MY2030氢燃料电池货车与燃油货车载质量损失

■ 2022 ■ UD ■ PO_DVKT ■ RD ■ DDC_DVKT

a. 4.5吨轻型普通货车

![img-45.jpeg](img-45.jpeg)

b. 18吨载货汽车

![img-46.jpeg](img-46.jpeg)

c. 31吨自卸汽车

![img-47.jpeg](img-47.jpeg)

d. 42吨半挂牵引车

![img-48.jpeg](img-48.jpeg)

缩略词：FCET=氢燃料电池货车；UD=城市运输；RD=区域运输；DDC_DVKT=集疏港运输（“日行驶里程”法）；PO_DVKT=港口内运输（“日行驶里程”法）。
来源：作者计算。

32

WRI.org.cn

## 有必要设计广泛适用的新能源货车 (特别是纯电动货车)

基于上述分析结果,本文进而对比了MY2022—MY2030期间同一场景内、不同场景间新能源货车参数设置的差异。其结果显示(见图8和图10),即便在同一运输场景下,在MY2025,纯电动货车额定电池容量之差跨度较大,从城市运输场景下纯电动轻型货车(包括BET200和BET300)的51千瓦时,到区域运输场景下纯电动载货汽车(包括BET300、BET400和BET500)的322千瓦时。其中,纯电动货车额定电池容量的差异在区域运输场景中尤为显著。此外,不同场景下,纯电动货车的电池容量差异更大。例如,区域运输(BET500)场景中18吨纯电动载货汽车MY2022—MY2030的电池容量与城市运输(BET200)场景中18吨纯电动载货汽车相差388~453千瓦时。

纯电动货车所需电池容量的巨大差异,给主机厂生产纯电动货车以及运输企业采购适合的纯电动货车带来了显著挑战,尤其是考虑到货车往往需要跨场景运营(TUC 2022b)。针对这一挑战,目前纯电动货车电池容量有两种配置方案(Tol et al. 2022; Tetra Tech and GNA 2022):

- ■ 一种配置方案是设计广泛适用的纯电动货车,以满足常见场景的大部分运营要求。此方案有助于主机厂实现同一配置新能源货车的规模化量产,降低其制造成本,同时保障新能源货车二手车的残值收益。然而,由于电池容量更大(以及载质量重损失更多),对运输企业而言,购买广泛适用的新能源货车可能会增加购置成本与TCO。

- ■ 另一种配置方案是为具体运输场景量身定制纯电动货车。与广泛适用的纯电动货车相比,为特定目的设计的纯电动货车能够确保运输企业以较低的价格购入车辆,但车辆的运营灵活性也受到限制。此外,这一方案可能会削弱主机厂大规模量产新能源货车的能力,并影响新能源货车的残值收益。

为满足小微运输企业对运营灵活性的需求,本文建议其考虑广泛适用的纯电动货车。对于大型运输车队,为具体运输场景定制的纯电动货车较适合,因为这些企业通常会与货主企业签订长期合同物流,且在车辆调度上积累了丰富的经验。对于小微运输企业而言,定制化的解决方案并不可行,因为这些企业通常货源不稳定,需要依赖网络货运平台寻找货源,可能跨越多个场景运营,且可调度车辆数量有限。为设计广泛适用的纯电动货车,建议有关部门收集目前在运营的燃油货车分车型、分场景的日行驶里程信息,并与主要的行业相关方(如主机厂)共享这些信息,便于车辆设计。

### MY2022—MY2030新能源货车购置成本

基于MY2022—MY2030新能源货车的参数设置,本文计算了MY2022—MY2030期间新能源货车的购置成本,结果如下:

新能源货车购置成本在MY2022—MY2030期间快速下降(见图12)。与MY2022相比,MY2030的新能源货车购置成本下降了22%~64%。其中,氢燃料电池货车购置成

图 12 | MY2022—MY2030不同运输场景新能源货车的直接制造成本

■ 电池包 ■ 燃料电池 ■ 储氢系统 ■ 电驱动系统 ■ 其他零部件

a. 4.5吨轻型普通货车(UD,日行驶里程为200千米;RD,日行驶里程为500千米)

![img-49.jpeg](img-49.jpeg)

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

33

图 12 | MY2022—MY2030不同运输场景新能源货车的直接制造成本(续)

# b. 42吨半挂牵引车 (DDC, 日行驶里程为400千米)

![img-50.jpeg](img-50.jpeg)

缩略词：按T=纯电动货车；FCET=氢燃料电池货车；H2V=燃油汽车；UD=城市运输；RD=区域运输；DDC_DVKT=集疏港运输（“日行驶里程”法）；DDC_TRIP=集疏港运输（“单程运距”法）。来源：作者计算。

本的降速最快：各场景下，MY2030氢燃料电池货车的购置成本较MY2022下降了53%~64%，而同期纯电动货车的购置成本仅下降22%~30%。到MY2030，氢燃料电池货车将成为多数场景中最便宜的新能源货车购置选项（城市运输场景中的4.5吨轻型普通货车除外）。氢燃料电池货车的购置成本之所以迅速下降，主要得益于以下两个方面：一是其最昂贵的零部件——燃料电池系统——的成本未来将快速下降（2030年，燃料电池系统单位成本将较2022年降低75%~80%），二是氢燃料电池货车混合动力的构型设计有助于降低燃料电池系统的功率，从而降低其购置成本。

尽管MY2022—MY2030新能源货车购置成本迅速降低，但仍高于燃油货车：本研究分析的所有场景中，到MY2030，新能源货车购置成本仍比燃油货车高出53%~322%。部分原因在于中国市场燃油货车的购置成本较低。例如，2022年，中国42吨柴油半挂牵引车的建议零售价格（manufacturer's suggested retail price, MSRP）$^{17}$约为33万元，为美国Class 8柴油牵引车建议零售价格的三分之一（Xie et al. 2023）。$^{18}$所以，即便采用“单程运距”法，集疏港运输场景42吨纯电动半挂牵引车（BET200）在MY2030的购置成本已处于较低水平（约为56万元）——低于美国Class 8柴油牵引车的购置成本，但在中国市场上，其仍是柴油牵引车购置成本的两倍。氢燃料电池货车也存在类似问题：虽然在多数运输场景中，MY2030氢燃料电池货车的购置成本已低于纯电动货车的

购置成本，但仍比同等燃油车车型高出60%~140%。部分场景下MY2025新能源货车与燃油货车的购置成本差异如图13所示，部分场景下MY2030新能源货车与燃油货车购置成本差异如图14所示。

为降低新能源货车高昂的初期购置一次性支出费用（特别是对小微运输企业而言），同时将购置与持有新能源货车的风险分摊给适宜承担这些风险的主体（如新能源货车租赁企业及平台、主机厂、金融机构等），政府与私营部门需要共同推广新能源货车经营性租赁等商业模式。例如，在新能源货车经营性租赁模式中，运输企业只需按月或按里程向租赁企业支付租金，而租赁企业则负责购置与持有新能源货车，并承担保险与维修保养费用（Pers. Comm. 2023a）。尽管经营性租赁等商业模式在中国已广泛实践（Shen and Mao 2023; Z. Wang et al. 2020），但其应用仅限于部分场景或地区。例如，在广东省，经营性租赁模式常见于4.5吨纯电动轻型普通货车与氢燃料电池货车（Z. Wang et al. 2020）。

未来，如果要在更多场景中推广新能源货车的商业模式，政府部门与金融机构等应采取更多支持性的措施，包括但不限于：帮助租赁平台降低货车贷款首付比例，提供贷款利率优惠与延长贷款期限，鼓励绿色金融或混合融资，为其租赁业务提供税收优惠与灵活折旧等政策支持，以及考虑为小微运输企业的租赁业务提供第一损失担保，对冲相关风险等（Sankar et al. 2022; Kok et al. 2023; Coyne et al. 2023）。

34

WRI.org.cn

## 图 13 | 部分场景下MY2025新能源货车与燃油货车的购置成本差异

■ BET ■ FCET

### a. 4.5吨轻型普通货车

![img-51.jpeg](img-51.jpeg)

### b. 42吨半挂牵引车

![img-52.jpeg](img-52.jpeg)

说明：百分比表示新能源货车与同等燃油货车购置成本差除以燃油货车购置成本所得的值，即（NEW-ICEV）/ICEV。百分比为零，表示新能源货车购置成本与燃油货车相同。这里，购置成本不考虑任何政策影响，包括新能源货车购置补贴或燃油货车购置税的影响。

缩略词：BET=纯电动货车；FCET=氢燃料电池货车；NEW=新能源汽车；ICEV=燃油汽车；UD=城市运输；RD=区域运输；PO_TRIP=港口内运输（“单程运距”法）；DDC_DVKT=集疏港运输（“日行便里程”法）；DDC_TRIP=集疏港运输（“单程运距”法）。

来源：作者计算。

## 图 14 | 部分场景下MY2030新能源货车与燃油货车购置成本差异

■ BET ■ FCET

### a. 4.5吨轻型普通货车

![img-53.jpeg](img-53.jpeg)

### b. 42吨半挂牵引车

![img-54.jpeg](img-54.jpeg)

说明：百分比表示新能源货车与同等燃油货车购置成本差除以燃油货车购置成本所得的值，即（NEW-ICEV）/ICEV。百分比为零，表示新能源货车购置成本与燃油货车相同。这里，购置成本不考虑任何政策影响，包括新能源货车购置补贴或燃油货车购置税的影响。

缩略词：BET=纯电动货车；FCET=氢燃料电池货车；NEW=新能源汽车；ICEV=燃油汽车；UD=城市运输；RD=区域运输；PO_TRIP=港口内运输（“单程运距”法）；DDC_DVKT=集疏港运输（“日行便里程”法）；DDC_TRIP=集疏港运输（“单程运距”法）。

来源：作者计算。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

35

## MY2022—MY2030新能源货车TCO

无政策激励时，新能源货车将在近期，在城市运输、港口内运输和集疏港运输场景中，实现与燃油货车的TCO平价

本文进一步计算了在无政策激励时，新能源货车MY2022—MY2030期间的TCO，并分析了不同场景下，新能源货车实现与燃油货车TCO平价的年份（见图15），以及更具TCO竞争力的新能源技术。由于氢燃料电池货车可在纯氢与插电式混合动力两种模式下运行，因此，本文计算并比较了氢燃料电池货车在两种运行模式下的TCO。

本文计算结果显示，无政策激励时，新能源货车相对于燃油货车的TCO平价将在近十年内实现。然而，在不同的运输场景中，TCO平价年份与具备TCO竞争力的新能源技术存在差异：

- ■ 在城市运输、港口内运输和集疏港运输场景中，纯电动货车（除自卸汽车外）将在MY2022—MY2027实现与燃油货车的TCO平价，早于氢燃料电池货车。

在城市运输场景中，纯电动4.5吨轻型普通货车与纯电动18吨载货汽车将在MY2022—MY2027实现与燃油货车的TCO平价。平价时间跨度大是运输货类不同所致：如果运输轻抛货，两种车型现阶段（MY2022—MY2023）就已实现TCO平价；但如果运输重货，受新能源货车载质量损失的影响，两种车型的TCO平价时间将推迟至MY2025—MY2027。

在港口内运输、集疏港运输和城市运输场景中，纯电动42吨半挂牵引车将在近期（MY2022—MY2025）与柴油半挂牵引车实现TCO平价，成为近期最具电动化潜力的场景。到MY2030，纯电动42吨半挂牵引车的TCO甚至会比同等柴油货车低30万元左右。具体原因如下：一是本研究中，港口内运输场景与集疏港运输场景的纯电动半挂牵引车大多运输轻抛货，不存在载质量损失问题；二是采用“单程运距”法，港口内运输场景与集疏港运输场景中，纯电动半挂牵引车搭载的电池额定电量更小，能更早实现与柴油货车的TCO平价（见下文解释）。

纯电动31吨自卸汽车将在MY2029—MY2030实现与柴油货车的TCO平价，与氢燃料电池31吨自卸汽车TCO平价时间大致相同。但由于纯电动31吨自卸汽车（特别是BET300）的载质量损失较大，其MY2030的TCO要比氢燃料电池31吨自卸汽车更高（高出5~10万元）。

![img-55.jpeg](img-55.jpeg)

- ■ 对于区域运输场景，多数新能源货车将在MY2028—MY2030实现与燃油货车的TCO平价，比城市运输场景要晚一些。此外，与城市运输场景、港口内运输场景和集疏港运输场景有所不同，区域运输场景中最具有TCO竞争力的新能源技术以氢燃料电池技术为主。

在区域运输场景中，受运输货类影响，纯电动4.5吨轻型普通货车的TCO平价年份跨度较大；如果运输轻抛货，其可在MY2026左右实现与燃油货车的TCO平价；此时，纯电动技术为最具成本竞争力的技术选项。当运输重货时，新能源4.5吨轻型普通货车将在MY2029—MY2030才能实现与燃油货车的TCO平价，届时氢燃料电池技术成为最具成本竞争力的技术选项（因为载质量损失更低）。因此，如果用于区域运输场景的跨货类运输，氢燃料电池4.5吨轻型普通货车可能是更好的选择。

在区域运输场景中，氢燃料电池18吨载货汽车与氢燃料电池42吨半挂牵引车将在MY2028—MY2030实现与柴油货车的TCO平价，早于纯电动货车。在区域运输场景中，纯电动货车TCO比氢燃料电池货车更高，例如，MY2030纯电动半挂牵引车与载货汽车的TCO比氢燃料电池货车高出7000至650000元。具体原因如下：一是纯电动货车在区域运输场景中的能量消耗量要高于城市运输场景（Al-Wreikat, Serrano, and Sodré 2021; Singer et al. 2023）；二是本文未区分氢燃料电池货车在城市运输场景和区域运输场景中的能量消耗量，可能会给予区域运输场景中的氢燃料电池货车更多成本优势。此外，在区域运输场景下，插电混合动力模式氢燃料电池货车比纯氢模式氢燃料电池货车的TCO低30000至40000元，比纯氢模式氢燃料电池货车提前一年左右实现TCO平价。MY2025和MY2030部分场景下纯电动货车与氢燃料电池货车的TCO构成如图16所示。

36

WRI.org.cn

图 15 | 无政策激励时,不同运输场景新能源货车实现与燃油货车TCO平价的年份

● BET ▲ FCET(混合) ● FCET(纯氢)

|  货车车型 | 行驶工况 | 货物类型 | 日行驶里程 (千米) | 2022 | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 | 2030年后  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  4.5 吨 轻型 普通 货车 | UD | 轻抛货 | 200 | ● |  |  |  |  |  |  |  |  | ▲●  |
|   |   |   |  300 | ● |  |  |  |  |  |  | ▲ | ● |   |
|   |   |  重货 | 200 |  |  |  | ● |  |  |  |  |  | ▲●  |
|   |   |   |  300 |  |  |  |  |  | ● |  |  | ▲● |   |
|   |  RD | 轻抛货 | 300 |  |  |  |  | ● |  |  |  | ▲ | ●  |
|   |   |   |  400 |  |  |  |  | ● |  |  | ▲ | ● |   |
|   |   |   |  500 |  |  |  |  | ● |  | ▲ | ● |  |   |
|   |   |  重货 | 300 |  |  |  |  |  |  |  |  |  | ●▲●  |
|   |   |   |  400 |  |  |  |  |  |  |  |  | ▲● | ●  |
|   |   |   |  500 |  |  |  |  |  |  |  | ▲ | ● | ●  |
|  18 吨 载货 汽车 | UD | 轻抛货 | 200 |  | ● |  |  |  |  |  |  |  | ▲●  |
|   |   |   |  300 |  | ● |  |  |  |  |  | ▲● |  |   |
|   |   |  重货 | 200 |  |  |  | ● |  |  |  | ▲ | ● |   |
|   |   |   |  300 |  |  |  | ● |  | ▲ | ● |  |  |   |
|   |  RD | 轻抛货 | 300 |  |  |  |  |  |  |  |  | ▲● | ●  |
|   |   |   |  400 |  |  |  |  |  |  |  | ▲● | ● |   |
|   |   |   |  500 |  |  |  |  |  |  | ▲ | ● | ● |   |
|   |   |  重货 | 300 |  |  |  |  |  |  |  | ▲● |  | ●  |
|   |   |   |  400 |  |  |  |  |  |  | ▲● |  |  | ●  |
|   |   |   |  500 |  |  |  |  |  | ▲ | ● |  |  | ●  |
|  31 吨自卸 汽车 | UD | 重货 | 200 |  |  |  |  |  |  |  | ● |  | ▲●  |
|   |   |   |  300 |  |  |  |  |  |  |  | ▲ | ●● |   |
|  42 吨 半挂 牵引车 | PO_TRIP | 轻抛货 | 200 | ● |  |  |  |  |  |  |  |  |   |
|   |   |   |  300 | ● |  |  |  |  |  |  |  |  |   |
|   |  PO_DVKT |   | 200 | ● |  |  |  | ▲ | ● |  |  |  |   |
|   |   |   |  300 | ● |  |  | ▲ | ● |  |  |  |  |   |
|   |  DDC_TRIP |   | 200 |  |  |  |  |  |  |  |  |  | ●  |
|   |   |   |  300 |  |  |  | ● |  |  |  |  |  |   |
|   |   |   |  400 | ● |  |  |  |  |  |  |  |  |   |
|   |   |   |  500 |  |  |  | ● |  |  |  |  |  |   |
|   |  DDC_DVKT |   | 200 |  |  |  |  |  |  |  |  |  | ●▲●  |
|   |   |   |  300 |  |  |  |  |  |  |  |  | ▲● | ●  |
|   |   |   |  400 |  |  |  |  |  |  |  | ▲● |  | ●  |
|   |   |   |  500 |  |  |  |  |  |  | ▲ | ● |  | ●  |
|   |  UD |   | 200 |  |  | ● |  |  |  |  | ▲ | ● |   |
|   |   |   |  300 |  | ● |  |  |  |  | ▲● |  |  |   |
|   |  RD |   | 300 |  |  |  |  |  |  |  |  | ▲● | ●  |
|   |   |   |  400 |  |  |  |  |  |  |  | ▲● |  | ●  |
|   |   |   |  500 |  |  |  |  |  |  | ▲ | ● |  | ●  |

说明: 基于 Pers.Comm. (2023a), 本文假设 31 吨自卸汽车的使用年限为五年, 而其他车型的使用年限为六年。

缩略词: TCO= 总拥有成本; BET= 纯电动货车; FCET= 氢燃料电动货车; KEV= 燃油汽车; 混合= 核电式混合动力模式; 纯氢= 纯氢模式; UD= 城市运输; RD= 区域运输; PO_TRIP= 港口内运输 (“单程运输”法); PO_DVKT= 港口内运输 (“日行驶里程”法); DDC_TRIP= 集疏港运输 (“单程运输”法); DDC_DVKT= 集疏港运输 (“日行驶里程”法)。

来源: 作者计算。

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

37

图 16 | MY2025和MY2030部分场景下纯电动货车与氢燃料电池货车的TCO构成

■ 购置成本 ■ 融资成本 ■ 税费 ■ 能源成本 ■ 高速收费成本 ■ 维保成本 ■ 保险成本 ■ 载质量损失成本

# 1) 4.5吨轻型普通货车

a. UD (日行驶里程为200千米)

![img-56.jpeg](img-56.jpeg)

b. RD (日行驶里程为500千米)

![img-57.jpeg](img-57.jpeg)

# 2) 18吨载货汽车

a. UD (日行驶里程为200千米)

![img-58.jpeg](img-58.jpeg)

38

WRI.org.cn

图 16 | MY2025和MY2030部分场景下纯电动货车与氢燃料电池货车的TCO构成(续)

■ 购置成本 ■ 融资成本 ■ 税费 ■ 能源成本 ■ 高速收费成本 ■ 维保成本 ■ 保险成本 ■ 载质量损失成本

b. RD (日行驶里程为500千米)

![img-59.jpeg](img-59.jpeg)

### 3) 31吨自卸汽车

a. UD (日行驶里程为200千米)

![img-60.jpeg](img-60.jpeg)

### 4) 42吨半挂牵引车

a. PO_TRIP (日行驶里程为200千米)、UD (日行驶里程为200千米) 和DDC_TRIP (日行驶里程为400千米)

![img-61.jpeg](img-61.jpeg)

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

39

图 16 | MY2025和MY2030部分场景下纯电动货车与氢燃料电池货车的TCO构成(续)

![img-62.jpeg](img-62.jpeg)

说明: 本文假设当吨自卸汽车的使用年限为五年, 而其他车型的使用年限为六年 (Pers. Comm. 2023a)。

缩略词: TCO=氢拥有成本; BET=纯电动货车; FCET=氢燃料电动货车; ICEV=燃油汽车; 纳氢=纯氢模式; 混合=插电式混合动力模式; UD=城市运输; RD=区域运输; PD_TWP=港口内运输(“单程运输”法); DDC_TWP=集疏港运输(“单程运输”法)。

来源: 作者计算。

### 新能源货车与燃油货车的TCO平价时间受车辆能量消耗量与能源价格变化的影响

新能源货车能源成本——包括新能源货车与燃油货车能效比(EER)以及能源价格——在TCO中的占比较大, 所以, 能源成本变化对新能源货车的TCO平价时间有着重要影响。

本文以42吨半挂牵引车轻拗货运输为例, 计算了新能源货车与燃油货车能效比(EER)与新能源货车TCO平价时间的关系(见图17)。虽然本文测算TCO过程中, 考虑了新能源货车未来能量消耗量随技术进步而呈现的下降趋势, 但由于新能源货车在不同行驶工况下, 能量消耗量有较大差异, 加之技术发展的不确定性 (Al-Wreikat, Serrano, and Sodré 2021), 本文采用敏感度分析的方法, 测算新能源货车与燃油货车TCO差价(及TCO平价年份)如何随其能效比而变化。为简化分析, 本文仅考虑氢燃料电池货车在纯氢模式下的TCO。

敏感度分析结果表明, 新能源货车与燃油货车能效比越高, 新能源货车越能及早实现与燃油货车的TCO平价。

■ 对于纯电动货车而言, 在能效比较高的场景中, 如港口内运输(EER=4.0)和城市运输(EER=3.0)场景, 纯电动半挂牵引车实现与燃油货车TCO平价的时间(MY2022—MY2024)要比区域运输场景更早。这是因为: 一是在港口内运输和城市运输场景中, 纯电动货车可以利用频繁加减速实现制动能量回收。相反, 在这些工况下, 燃油货车的燃料消耗量处于较高水平。在区域运输场景中, 燃油货车通常在高速工况下更容易保持匀速行驶, 速度更接近“经济

时速”(即达到最佳燃油经济性的发动机负荷率), 因而更高效。相反, 该工况下, 纯电动半挂牵引车能量消耗量更高 (CARB 2018), 与柴油货车的能效比更低, 仅为2.4。因此, 在区域运输场景中, 纯电动货车实现与燃油货车TCO平价的时间也要更晚(在MY2030之后)。

■ 氢燃料电池货车也呈现类似趋势。氢燃料电池半挂牵引车在港口内运输场景中能更早实现与燃油货车的TCO平价, 平价时间为MY2026—MY2027。但在城市运输和区域运输场景中, 氢燃料电池半挂牵引车与柴油货车的TCO平价时间要更晚, 为MY2028—MY2030。其原因是港口场景下, 氢燃料电池半挂牵引车相对柴油货车的能效更高(EER=1.7), 而城市运输和区域运输场景中, 其能效比较低(EER=1.3~1.5)¹⁰。此外, 本文未区分氢燃料电池货车在城市运输场景和区域运输场景中的能量消耗量, 可能会给予区域运输场景中的氢燃料电池货车更多成本优势。

此外, 本文也计算了新能源货车与燃油货车的TCO之差(与TCO平价年份)对不同能源价格(包括燃油价格、充电价格和氢气价格)的敏感性。虽然本文测算TCO的一个重要假设是未来充电价格将保持在1.2元/千瓦时, 燃油价格保持在2022年平均水平(8.1元/升), 且氢气价格将从2022年的55元/千克降至2030年的30元/千克, 但由于能源供需波动(Ma et al. 2022)、快充基础设施普及、充电与加氢基础设施利用率变化(He 2021), 能源价格在未来将呈现较强的波动性与不确定性, 进而影响新能源货车TCO与平价年份。

敏感度分析结果表明, 能源价格将影响新能源货车与燃油货车的TCO平价年份。

40

WRI.org.cn

图 17 | MY2025新能源货车与燃油货车TCO差价与能效比的敏感性分析:以42吨半挂牵引车为例

# a. 纯电动 42 吨半挂牵引车

![img-63.jpeg](img-63.jpeg)

# b. 氢燃料电池 42 吨半挂牵引车

![img-64.jpeg](img-64.jpeg)

说明:图中假设所有运输场景的日行驶里程为 300 千米。半挂牵引车的使用年限为六年(Pers Comm.2023a)。氢燃料电池货车 TCO 为纯氢模式下的 TCO。
缩略词: EER=能效比; UD=城市运输; RD=区域运输; PO_DVKT=港口内运输(“日行驶里程”法); TCO=总拥有成本。
来源:作者计算。

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

41

对纯电动货车而言，在其具有TCO竞争力的场景中（港口内运输、城市运输和集疏港运输），如果未来柴油价格保持不变，纯电动货车的充电价格区间为1.3~1.8元/千瓦时，就能在MY2025前达到与燃油货车的TCO平价。但如果柴油价格从2022年的8.1元/升下降到6.5元/升（即2019年的平均水平）（Eastmoney 2022），在上述运输场景中，纯电动货车的充电价格需要下降至0.9~1.5元/千瓦时，才能在MY2025前达到与燃油货车的TCO平价（见图18）。如果燃油价格从2022年的8.1元/升下降到6.5元/升，而充电价格从1.2元/千瓦时上升到1.4元/千瓦时，则纯电动货车与燃油货车实现TCO平价的时间将大幅推迟；集疏港运输场景（采用“单程运距”法）纯电动42吨半挂牵引车以及城市运输场景（轻抛货运输）纯电动18吨载货汽车与同类型柴油货车实现TCO平价的时间，都将推迟至MY2030左右。

对氢燃料电池货车而言，如果未来柴油价格保持不变，MY2030达到TCO平价的加氢价格区间在20~40元/千克（见图19）。在氢燃料电池货车具有TCO竞争力的场景中（即区域运输场景），枪口加氢价格需要达到30元/千克左右，才能在MY2030达到与柴油货车的TCO平价。但如果柴油价格下降到2019年的平均水平（即6.5元/升），只有在氢气价格达到20~25元/千克时，氢燃料电池货车才能在MY2030前实现与柴油货车的TCO平价。

图 18 | 部分运输场景纯电动货车与燃油货车实现TCO平价年份与能源价格敏感性分析

a. PO_TRIP（日行驶里程为200千米）场景中的42吨半挂牵引车（BET200）

|  9.00 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  8.75 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022  |
|  8.50 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022  |
|  8.25 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022  |
|  8.00 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022  |
|  7.75 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023  |
|  7.50 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024  |
|  7.25 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2025  |
|  7.00 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2025 | 2026  |
|  6.75 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2025 | 2026 | 2028  |
|  6.50 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2025 | 2026 | 2028 | 2030  |
|  6.25 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2025 | 2026 | 2028 | 2030 | >2030  |
|  6.00 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2025 | 2026 | 2028 | 2030 | >2030 | >2030  |
|  5.75 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2025 | 2026 | 2028 | 2030 | >2030 | >2030 | >2030  |
|  5.50 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2025 | 2026 | 2028 | 2030 | >2030 | >2030 | >2030 | >2030  |
|  5.25 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2025 | 2026 | 2028 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  5.00 | 2022 | 2022 | 2022 | 2023 | 2024 | 2025 | 2026 | 2028 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 | 1.1 | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 | 1.7 | 1.8  |

充电价格（元/千瓦时）

42

WRI.org.cn

图 18 | 部分运输场景纯电动货车与燃油货车实现TCO平价年份与能源价格敏感性分析(续)

# b. DDC\_TRIP(日行驶里程为400千米)场景中的42吨半挂牵引车(BET200)

|  柴油价格(元/升) | 9.00 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2026 | 2029  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   |  8.75 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2024 | 2025 | 2028 | >2030  |
|   |  8.50 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2025 | 2027 | 2030 | >2030  |
|   |  8.25 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2026 | 2028 | >2030 | >2030  |
|   |  8.00 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2025 | 2027 | 2030 | >2030 | >2030  |
|   |  7.75 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2026 | >2030 | >2030 | >2030 | >2030  |
|   |  7.50 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2024 | 2025 | 2028 | >2030 | >2030 | >2030 | >2030  |
|   |  7.25 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2027 | 2030 | >2030 | >2030 | >2030 | >2030  |
|   |  7.00 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2024 | 2026 | 2028 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  6.75 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2025 | 2027 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  6.50 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2026 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  6.25 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2025 | 2028 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  6.00 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2026 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  5.75 | 2022 | 2022 | 2022 | 2022 | 2024 | 2025 | 2028 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  5.50 | 2022 | 2022 | 2022 | 2023 | 2025 | 2027 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  5.25 | 2022 | 2022 | 2022 | 2024 | 2026 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  5.00 | 2022 | 2022 | 2023 | 2025 | 2028 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |   |
|   | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 | 1.1 | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 | 1.7 | 1.8  |   |

充电价格(元/千瓦时)

# c. UD(日行驶里程为200千米,轻抛货运输)场景中的18吨载货汽车(BET200)

|  柴油价格(元/升) | 9.00 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2025 | 2026 | 2027  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   |  8.75 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2023 | 2024 | 2025 | 2027 | 2029  |
|   |  8.50 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2023 | 2024 | 2025 | 2026 | 2028 | 2030  |
|   |  8.25 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2025 | 2026 | 2028 | 2030 | >2030  |
|   |  8.00 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2025 | 2026 | 2027 | 2029 | >2030 | >2030  |
|   |  7.75 | 2022 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2023 | 2024 | 2025 | 2027 | 2029 | >2030 | >2030 | >2030  |
|   |  7.50 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2023 | 2024 | 2025 | 2026 | 2028 | 2030 | >2030 | >2030 | >2030  |
|   |  7.25 | 2022 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2025 | 2026 | 2028 | 2030 | >2030 | >2030 | >2030 | >2030  |
|   |  7.00 | 2022 | 2022 | 2022 | 2022 | 2023 | 2024 | 2024 | 2026 | 2027 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  6.75 | 2022 | 2022 | 2022 | 2023 | 2023 | 2024 | 2025 | 2027 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  6.50 | 2022 | 2022 | 2022 | 2023 | 2024 | 2025 | 2026 | 2028 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  6.25 | 2022 | 2022 | 2023 | 2024 | 2025 | 2026 | 2028 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  6.00 | 2022 | 2023 | 2023 | 2024 | 2026 | 2027 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  5.75 | 2023 | 2023 | 2024 | 2025 | 2027 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  5.50 | 2023 | 2024 | 2025 | 2026 | 2028 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  5.25 | 2024 | 2025 | 2026 | 2028 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  5.00 | 2024 | 2026 | 2027 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |   |
|   | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 | 1.1 | 1.2 | 1.3 | 1.4 | 1.5 | 1.6 | 1.7 | 1.8  |   |

充电价格(元/千瓦时)

说明: 本文假设半挂牵引车和载货汽车的使用年限为六年 (Pers. Comm. 2023a)。绿色表示 MP2022 时纯电动货车与燃油货车实现 TCO 平价, 黄色和橙色表示 MP2023—MP2029 时纯电动货车与燃油货车实现 TCO 平价, 红色表示 MP2030 或 MP2030 后纯电动货车与燃油货车实现 TCO 平价。

缩略词: TCO= 总拥有成本; UD= 城市运输; PO_TRIP= 港口内运输 ( “单程运距” 法); DDC_TRIP= 集疏港运输 ( “单程运距” 法)。

来源: 作者计算。

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

43

图 19 | 部分运输场景氢燃料电池货车(纯氢模式)与燃油货车实现TCO平价年份与能源价格敏感性分析

# a. RD (日行驶里程为500千米, 重货运输) 场景中的4.5吨轻型普通货车 (BET500)

|  柴油价格(元/升) | 9.00 | 2027 | 2028 | 2029 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   |  8.75 | 2027 | 2028 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  8.50 | 2027 | 2028 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  8.25 | 2027 | 2029 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  8.00 | 2028 | 2029 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  7.75 | 2028 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  7.50 | 2028 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  7.25 | 2029 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  7.00 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  6.75 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  6.50 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  6.25 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  6.00 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  5.75 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  5.50 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  5.25 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  5.00 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |   |
|   | 20 | 25 | 30 | 35 | 40 | 45 | 50 | 55 | 60 |   |

氢气价格(元/千克)

# b. RD (日行驶里程为500千米) 场景中的42吨半挂牵引车 (BET500)

|  柴油价格(元/升) | 9.00 | 2024 | 2025 | 2027 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   |  8.75 | 2024 | 2026 | 2028 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  8.50 | 2024 | 2026 | 2028 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  8.25 | 2025 | 2026 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  8.00 | 2025 | 2027 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  7.75 | 2025 | 2027 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  7.50 | 2026 | 2028 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  7.25 | 2026 | 2028 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  7.00 | 2027 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  6.75 | 2027 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  6.50 | 2028 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  6.25 | 2028 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  6.00 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  5.75 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  5.50 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   |  5.25 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  5.00 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |   |
|   | 20 | 25 | 30 | 35 | 40 | 45 | 50 | 55 | 60 |   |

氢气价格(元/千克)

44

WRI.org.cn

# 图 19 | 部分运输场景氢燃料电池货车(纯氢模式)与燃油货车实现TCO平价年份与能源价格敏感性分析(续)

# c. RD (日行驶里程为500千米, 重货运输) 场景中的18吨载货汽车(BET500)

|  3.00 | 2024 | 2025 | 2026 | 2028 | >2030 | >2030 | >2030 | >2030 | >2030  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  8.75 | 2024 | 2025 | 2027 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  8.50 | 2024 | 2025 | 2027 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  8.25 | 2024 | 2026 | 2028 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  8.00 | 2025 | 2026 | 2028 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  7.75 | 2025 | 2027 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  7.50 | 2025 | 2027 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  7.25 | 2026 | 2027 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  7.00 | 2026 | 2028 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  6.75 | 2026 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  6.50 | 2027 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  6.25 | 2027 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  6.00 | 2028 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  5.75 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  5.50 | 2029 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  5.25 | 2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|  5.00 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030 | >2030  |
|   | 20 | 25 | 30 | 35 | 40 | 45 | 50 | 55 | 60  |

氢气价格(元/千克)

说明: 本文假设半挂牵引车和载货汽车的使用年限为六年(Pers. Comm. 2023a)。氢燃料电池货车的TCO是纯氢模式的结果。与此前分析不同, 本文的敏感性分析中, 氢燃料电池货车使用年限内的氢气价格保持不变。绿色表示MY2024—MY2026时氢燃料电池货车与燃油货车实现TCO平价, 黄色和橙色表示MY2027—MY2029时氢燃料电池货车与燃油货车实现TCO平价, 而红色表示MY2030或MY2030后氢燃料电池货车与燃油货车实现TCO平价。

缩略词: TCO=总拥有成本; ND=区域运输。

来源: 作者计算。

# 运营优化与技术进步有助于新能源货车提前实现TCO平价

无政策激励时, 运营优化与技术进步是推动新能源货车TCO下降的重要措施。

首先, 针对纯电动货车而言, 企业有必要采取运营优化等措施, 包括协同纯电动货车参数设置与充电设施的部署, 协调纯电动货车的运营与充电时间, 并采取措施提高新能源货车的运营效率。

本文的分析表明, 在港口内运输和集疏港运输场景中, 选择电池容量较小的纯电动货车、确保快充基础设施的全面部署, 以及调整运营时刻表允许纯电动货车实现“一天多充”, 对降低纯电动货车购置成本与TCO能发挥一定作用。例如, 在MY2025, 在集疏港运输场景中, 如果运输企业采用“单程运距”法, 需要一辆搭载288千瓦时电池的纯电动半挂牵引车(即BET200), 通过日间1~2次补电, 完成日行驶里程200~500千米的运营要求; 而运输企业采用“日行

“日行驶里程”法时, 需要一辆搭载576~720千瓦时电池的纯电动半挂牵引车(即BET400或BET500), 才能完成同样的运营要求。在MY2025, BET200的购置成本比BET400与BET500便宜30万~44万元, TCO平价时间比BET400与BET500更早——有望在MY2022—MY2025就实现与柴油货车的TCO平价, 而BET400与BET500的TCO平价时间则要在MY2030以后。

为支撑集疏港运输场景中采用较小的电池容量, 相关企业应在纯电动货车服务的港口、中途、工厂停车场附近部署足够数量的快充桩, 降低频繁充电对运营的影响。采用(大功率)快充会影响新能源货车的TCO, 具体体现在以下几个方面: 一是加速电池衰减, 导致使用中的关键零部件(电池)需要更换, 二是高峰时段充电, 导致能源成本的增加。然而, 根据本文测算, 小容量电池所节省的新能源货车购置成本, 可抵消运维环节增加的成本, 实现TCO的下降(见图20)。为支持小容量电池, 需要对充电基础设施与运营做出调整, 包括在港口、中途、工厂停车场与物流场站部

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

45

署足够数量的快充基础设施、保障充足的停车位数量与电网容量（Kotz et al. 2022），以及协调纯电动货车的运营与充电时间，如在装卸货等待时间、进港等待时间或中途司机休息时间进行补电。

此外，提高运营里程与效率也有助于缩小新能源货车与燃油货车的TCO差距。由于纯电动货车的能源成本一般低于燃油货车，所以，纯电动货车的日行驶里程越长，其与燃油货车的TCO差距就越小。然而，目前，货车（含新能源货车）的日/年行驶里程较短（Pers. Comm. 2023a），可能导致新能源货车无法与燃油货车实现TCO平价。货车行驶里程低的原因可能包括运输企业运营效率低，市场需求不足导致运力过剩，以及大量新能源货车补贴造成运力过剩。所以，为提高新能源货车利用率，运输企业应持续优化车队资产管理、路线规划与运营调度（Mišić et al. 2022），政府有关部门应避免推行过高的新能源货车购车补贴政策，刺激车队规模过度扩张或引入过多市场参与者，造成行业运力供给过剩。

另外，加快新能源货车关键零部件的技术研发，对降低新能源货车的TCO也发挥着重要的作用。本文分析了不同技术对降低MY2022—MY2030新能源货车TCO的作用，其结果显示（见图21）。

对于纯电动货车而言，TCO下降主要得益于以下几点：一是电池包成本下降；二是纯电动货车能效提升，如采用更高效的热管理系统、优化车辆空气动力系统，以及采用低滚动阻力轮胎与车身轻量化设计（National Petroleum Council 2012; Yang 2018）；三是纯电动货车载质量损失降低，包括提高电池能量密度、更好地集成“三电”系统，以及使用轻量化结构材料（EUCAR 2019）。

技术进步对纯电动货车TCO下降的贡献因运输场景而异，受货物类型的影响尤为显著。例如，在轻抛货运输中，电池成本与能量消耗量是影响TCO的决定性因素，对纯电动货车MY2022—MY2030的TCO下降分别贡献了46%~65%和18%~42%。然而，在重货运输中，提高电池能量密度更

图 20 | MY2025纯电动货车与燃油货车各成本要素的差价（以 DDC_TRIP 和 DDC_DVKT 场景中的 42 吨半挂牵引车为例）

![img-65.jpeg](img-65.jpeg)

缩略词：TCO=总拥有成本；BET=纯电动货车；DDC_TRIP=集疏港运输（“单程运距”法）；DDC_DVKT=集疏港运输（“日行驶里程”法）。
来源：作者计算。

46

WRI.org.cn

重要,对纯电动货车MY2022—MY2030的TCO下降贡献了12%~78%。实际上,由于小微运输企业运输的货物种类繁多(既运输重货,也运输轻抛货),所以,上述三类技术进步对降低纯电动货车TCO都不可或缺。

对于氢燃料电池货车而言,TCO下降主要归功于以下几点:一是燃料电池系统成本下降,二是氢气价格下降(如可再生能源成本降低或电解槽能效提升(IRENA 2020)。

同样地,技术进步对氢燃料电池货车TCO下降的贡献也因运输场景而异。在城市运输场景中,燃料电池系统成本对TCO下降的影响最大,对氢燃料电池货车MY2022—MY2030的TCO下降贡献了50%~70%。而在区域运输场景中,氢气价格则发挥了更重要的作用,在氢燃料电池货车MY2022—MY2030的TCO下降中贡献了16%~40%,其作用随着氢燃料电池货车的日行驶里程增加而越发凸显。

图 21 | 部分运输场景中技术进步对MY2022—MY2030新能源货车TCO下降的贡献

a. 纯电动货车

|  货车类型 | 货物类型 | 技术进步 | UD |   | RD |   | DOC_TRIP  |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   |   |   |  200千米 | 300千米 | 300千米 | 500千米 | 200千米 | 500千米  |
|  4.5吨轻型普通货车 | 轻抛货 | 电池成本(元/千瓦时) | 40% | 48% | 43% | 51% | N.A.  |   |
|   |   |  电驱动系统成本(元/千瓦) | 17% | 12% | 11% | 7%  |   |   |
|   |   |  能量消耗量(千瓦时/100千米) | 37% | 40% | 40% | 42%  |   |   |
|   |  重货 | 电池成本(元/千瓦时) | 29% | 21% | 17% | 1% | N.A.  |   |
|   |   |  电驱动系统成本(元/千瓦) | 10% | 5% | 4% | 0%  |   |   |
|   |   |  能量消耗量(千瓦时/100千米) | 28% | 23% | 20% | 9%  |   |   |
|   |   |  电池能量密度(瓦时/千克) | 24% | 40% | 47% | 78%  |   |   |
|   |   |  结构材料轻量化 | 10% | 12% | 12% | 12%  |   |   |
|  18吨载货汽车 | 轻抛货 | 电池成本(元/千瓦时) | 56% | 60% | 62% | 65% | N.A.  |   |
|   |   |  电驱动系统成本(元/千瓦) | 22% | 16% | 14% | 9%  |   |   |
|   |   |  能量消耗量(千瓦时/100千米) | 22% | 24% | 24% | 26%  |   |   |
|   |  重货 | 电池成本(元/千瓦时) | 42% | 39% | 36% | 24% | N.A.  |   |
|   |   |  电驱动系统成本(元/千瓦) | 14% | 9% | 7% | 3%  |   |   |
|   |   |  能量消耗量(千瓦时/100千米) | 18% | 18% | 16% | 13%  |   |   |
|   |   |  电池能量密度(瓦时/千克) | 12% | 20% | 25% | 43%  |   |   |
|   |   |  结构材料轻量化 | 13% | 14% | 16% | 17%  |   |   |
|  42吨半挂牵引车 | 轻抛货 | 电池成本(元/千瓦时) | 54% | 60% | 58% | 63% | 53% | 58%  |
|   |   |  电驱动系统成本(元/千瓦) | 28% | 20% | 19% | 12% | 26% | 15%  |
|   |   |  能量消耗量(千瓦时/100千米) | 18% | 20% | 23% | 25% | 21% | 27%  |

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

47

图 21 | 部分运输场景中技术进步对MY2022—MY2030新能源货车TCO下降的贡献(续)

# b. 氢燃料电池货车

|  货车车型 | 货物类型 | 技术进步 | UD | RO  |
| --- | --- | --- | --- | --- |
|   |   |   |  200千米 | 500千米  |
|  4.5 吨 轻型 普通 货车 | 轻抛货 | 燃料电池系统成本（元/千瓦） | 70% | 51%  |
|   |   |  储氢系统成本（元/千克） | 3% | 6%  |
|   |   |  电池成本（元/千瓦时） | 2% | 1%  |
|   |   |  电驱动系统成本（元/千瓦） | 2% | 2%  |
|   |   |  能量消耗量（千克/100 千米） | 9% | 16%  |
|   |   |  氢燃料价格（元/千克） | 14% | 24%  |
|   |  重货 | 燃料电池系统成本（元/千瓦） | 58% | 33%  |
|   |   |  储氢系统成本（元/千克） | 3% | 4%  |
|   |   |  电池成本（元/千瓦时） | 2% | 1%  |
|   |   |  电驱动系统成本（元/千瓦） | 2% | 1%  |
|   |   |  能量消耗量（千克/100 千米） | 10% | 16%  |
|   |   |  氢燃料价格（元/千克） | 15% | 25%  |
|   |   |  储氢系统的质量储氢密度（wt%） | 1% | 4%  |
|   |   |  燃料电池质量功率密度（瓦/千克） | 1% | 2%  |
|   |   |  电池能量密度（瓦时/千克） | 1% | 2%  |
|   |   |  结构材料轻量化 | 7% | 12%  |
|  18 吨 载货 汽车 | 轻抛货 | 燃料电池系统成本（元/千瓦） | 55% | 35%  |
|   |   |  储氢系统成本（元/千克） | 5% | 8%  |
|   |   |  电池成本（元/千瓦时） | 4% | 3%  |
|   |   |  电驱动系统成本（元/千瓦） | 4% | 2%  |
|   |   |  能量消耗量（千克/100 千米） | 8% | 12%  |
|   |   |  氢燃料价格（元/千克） | 25% | 38%  |
|   |  重货 | 燃料电池系统成本（元/千瓦） | 50% | 30%  |
|   |   |  储氢系统成本（元/千克） | 5% | 7%  |
|   |   |  电池成本（元/千瓦时） | 4% | 2%  |
|   |   |  电驱动系统成本（元/千瓦） | 3% | 2%  |
|   |   |  能量消耗量（千克/100 千米） | 8% | 12%  |
|   |   |  氢燃料价格（元/千克） | 25% | 38%  |
|   |   |  储氢系统的质量储氢密度（wt%） | 1% | 2%  |
|   |   |  燃料电池质量功率密度（瓦/千克） | 0% | 0%  |
|   |   |  电池能量密度（瓦时/千克） | 1% | 2%  |
|   |   |  结构材料轻量化 | 3% | 5%  |
|  42 吨 半挂 牵引车 | 轻抛货 | 燃料电池系统成本（元/千瓦） | 53% | 33%  |
|   |   |  储氢系统成本（元/千克） | 6% | 9%  |
|   |   |  电池成本（元/千瓦时） | 4% | 2%  |
|   |   |  电驱动系统成本（元/千瓦） | 5% | 3%  |
|   |   |  能量消耗量（千克/100 千米） | 8% | 13%  |
|   |   |  氢燃料价格（元/千克） | 25% | 40%  |

说明：蓝色文字表示有助于“减少新能源货车载质量损失”的技术参数。

缩略词：UD=城市运输；RO=区域运输；DDC_TMP=氢能源运输（“单程运距”法）；MA=不适用。

来源：作者计算。

48

WRI.org.cn

在政策激励下，纯电动货车有望提前至MY2022—MY2025实现TCO平价

除运营优化与技术进步外，政策激励对降低新能源货车的TCO也发挥了重要作用。本文根据对文献（C40 2020; Concept Consulting Group 2022; WEF 2021）总结出国家与地方政府以及行业可采取的新能源货车推广措施，包括经济激励、政策法规与基础设施配套措施等（见表13）。其中，本文侧重分析购置补贴（仅针对氢燃料电池货车）、税费减免、能源（充电/加氢）补贴、碳价、优先路权、减免高速收费、提高最大设计总质量与降低融资成本这八项政策。

本文以尽量减少政府财政支出为原则，结合实际情况，假设未来这八项政策在2022—2030年的实施力度：

- ■ **新能源货车购置补贴：** 自2023年起，国家关于新能源汽车的购置补贴已全面退出，仅有五个“氢燃料电池汽车示范城市群”还有针对氢燃料电池汽车的购置补贴（MOF et al. 2020; 2021）。基于此，本文假设2022—2030年期间，纯电动货车将无任何购置补贴；而由于氢燃料电池货车未来购置成本与TCO仍较高，本文假设2022—2030年期间，广东省氢燃料电池汽车示范城市群的购置补贴仍将保留，但补贴额度将降至2022年的20%，即600元/千瓦。根据本文对燃料电池系统功率的假设（见“MY2022—MY2030各场景结果”一节），氢燃料电池货车的购置补贴为50400～90000元/车，相当于2030年氢燃料电池货车购置成本的11%～22%。
- ■ **新能源货车税费减免：** 目前，燃油货车需缴纳购置税（税率为不含增值税车辆购置成本的10%）与车船税（税率因城市而异），而新能源货车在2025年底前可免征购置税，在2026—2027年期间可获得50%的购置税减免，车船税将继续全额免征（MOF et al. 2018; 2023）。出于简化，本文假设自2026年起，新能源货车全额免缴购置税与车船税。
- ■ **能源（充电/加氢）补贴：** 目前，中国不仅已免除新能源货车充电的需量电费，一些地区也为充电、加氢基础设施的建设与运维提供了补贴。例如，福建省和江苏省为使用公共充电桩的纯电动货车提供0.1至0.3元/千瓦时的充电补贴，佛山市为氢燃料电池货车提供18元/千克的加氢补贴（Changzhou Government 2024; Foshan Nanhai Government 2022; Fujian DRC et al. 2022）。此外，河南省按照公共充电站充电设备投资的40%提供建设补贴（Henan Government 2020; Otog Government 2023）。基于此，本文假设，除继续免除新能源货车充电的需量电费外，地方政府还将

在2022—2030年期间提供以下能源补贴：一是为纯电动货车充电提供0.1元/千瓦时的充电补贴；二是为氢燃料电池货车提供1至20元/千克不等的加氢补贴，以保证枪口加氢价格在2022—2030年期间维持在30元/千克的水平，即广东省氢燃料电池汽车示范城市群提出的2025年示范期末加氢价格目标（Guangdong DRC et al. 2022）。

- ■ **针对传统燃料的碳价：** 中国尚未对交通领域燃料使用实施碳定价。本文假设，2022—2030年期间，以目前广东省区域碳市场的配额价格对柴油货车征收碳税，即2022年平均成交价80元/吨二氧化碳，比2022年全国碳市场的配额平均成交价高出45%（Jinan University 2022）。
- ■ **减免新能源货车高速收费：** 中国高速公路通常为收费公路。为推广新能源货车，部分省市出台了减免新能源货车高速公路通行费的政策。例如，甘肃省对省内高速公路通行的新能源汽车免除15%的高速费，天津市更是对进出天津港的新能源半挂牵引车（即集疏港运输场景）全额免除高速费（Gansu DOT et al. 2021; Tianjin MTC and Tianjin DRC 2021）。考虑到高速收费是弥补其建设、运营与维护成本的重要资金来源（Reja et al. 2013），本文假设，2022—2030年期间，新能源货车仅享受15%的高速费减免优惠，以确保高速公路运维资金的可持续性。
- ■ **新能源货车的优先路权政策：** 为缓解交通拥堵，许多中国城市对货车实施了严格的限行政策。例如，深圳市部分高速公路全天禁止大型货车通行（见附录A）。但为激励新能源货车推广，一些城市也放宽了新能源货车的限行要求（但仍保留燃油货车的限行政策）。此举相当于减少了新能源货车的日行驶里程（延长营运时间），并增加了其运营收入。为量化新能源货车优先路权政策的成本效益，并出于简化，本文仅考虑该措施对减少新能源货车行驶里程的作用。根据本文测算，深圳市放开新能源货车高速公路通行限制的作用相当于新能源货车的日行驶里程较柴油货车减少4%～6%。所以，本文假设，在优先路权政策下，新能源货车的日行驶里程将比同类型燃油货车少5%。
- ■ **提高新能源货车最大设计总质量限值：** 为化解新能源货车载质量损失问题，欧盟出台《重量和尺寸指令》（EU 2019），允许新能源货车的最大设计总质量限值提升2吨（柴油货车保持不变），而关于最大设计总质量额外提高4吨的提案也在讨论中（Soone 2023）。相反，中国目前并未放宽类似标准，仅部分省份规定：如果货车的车货总重（包括新能源货车和燃油货车）未超出其最大设计总质量限值的10%，可免于超载处罚（Henan People's Congress 2023）。本文

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

49

假设，有关政府部门将允许，在满足最大轴荷的前提下，新能源轻型货车的最大设计总质量限值提升500千克，新能源重型货车的最大设计总质量限值提升2吨。

- ■ **降低新能源货车的融资成本：**中国的货运运输企业通常选择贷款购车，而贷款利率受运输企业的规模大小与信用影响。以三年期贷款为例，大型运输企业可享受较低的年利率（4%~7%），而小微运输企业与个体司

机则面临较高的年利率（7%~10%）（Pers. Comm. 2023b）。本文假设，有关政府部门将允许小微运输企业以4.2%的贷款基准利率（Loan prime rate）贷款购买新能源货车（Bank of China n.d.），比此前分析中使用的贷款利率（10%）更低。

实施本文假设的上述八项政策后，新能源货车与燃油货车实现TCO平价时间的变化（见图22）如下：

表 13 | 为弥合新能源货车与燃油货车TCO差价，政府与行业可考虑采取的措施

|  措施 |   | 全球案例 | 中央政府 | 地方政府 | 行业企业  |
| --- | --- | --- | --- | --- | --- |
|  供给侧 | 经济激励 | 新能源货车积分政策或新能源货车碳排放标准 • **加利福尼亚州：**到2035年，不同类别新能源汽车渗透率分别达到40%（牵引车）、55%（2b-3类货车）、75%（4-8类载货汽车）和100%（集疏港拖车）（CARB 2021b, 'Advanced Clean Trucks'; 2023, 'Advanced Clean Fleets'） • **欧盟：**2035年后，新售微面、中面的二氧化碳排放量减少100%，并为新售重型车辆拟定2030年（-45%）、2035年（-65%）和2040年（-90%）的减排目标（EU 2023a） • **中国：**暂无 | ○ |  |   |
|   |   |  研发 • **欧盟：**“地平线欧洲”（Horizon Europe）计划中的零排放货运生态系统（ZEFES n.d.） • **中国：**国家重点研发计划（HTRDC n.d.） | √ | √ | √  |
|  需求侧 | 经济激励 | 购置补贴（或置换补贴） • **加利福尼亚州：**为港口牵引车提供高达20万美元/车的补贴（CARB n.d., 'Clean Off-Road Equipment Vouchers'） • **德国：**补贴新能源货车与同等柴油货车购置成本差价的80%（BALM 2022） • **中国：**仅在五个氢燃料电池汽车示范城市群提供氢燃料电池汽车购置补贴（MOF et al. 2020; 2021） | √ | √ |   |
|   |   |  税费减免 • **美国：**提供高达4万美元/车的清洁能源车辆税费减免（USDOT n.d., 'Commercial Clean Vehicle Credit'） • **德国：**纯电动汽车与氢燃料电池汽车免征机动车税（German Bundestag 2012） • **中国：**新能源汽车在2025年之前免征购置税，2026年和2027年间免税50%；新能源货车免征车船税（MOF et al. 2018; 2023） | √ |  |   |
|   |   |  碳定价 • **加利福尼亚州：**出台低碳燃料标准，基于交通燃料的全生命周期碳强度，实施燃料的积分交易机制（CARB n.d., 'Low Carbon Fuel Standard'） • **中国：**暂无 | ○ | ○ |   |

50

WRI.org.cn

表 13 | 为弥合新能源货车与燃油货车TCO差价，政府与行业可考虑采取的措施(续)

| 措施 | 全球案例 | 中央政府 | 地方政府 | 行业企业 |
| --- | --- | --- | --- | --- |
| 需求侧 | 减免高速收费 | - **德国：**新能源汽车免征高速费 - **中国：**中国部分地区为新能源货车减免15%~100%的高速收费（Gansu DOT et al. 2021; Tianjin MTC and Tianjin DRC 2021） |  | √ |  |
| 创新商业模式 | - **行业：**美国实行纯电动货车租赁（Penske 2023），瑞士和德国实行按使用付费模式，鼓励租赁氢燃料电池货车（Hyundai n.d.; Shell 2023） - **中国：**中央政府推出新能源汽车换电模式应用试点方案（MIIT 2021） | √ | √ | √ |
| 提高运营效率 | - **行业：**企业进行配送路线优化（AnyLogic n.d.） |  |  | √ |
| 残值担保 | - **美国：**新能源汽车可获得其购置成本30%（最高4000美元）的残值担保（USDOT n.d., 'Used Clean Vehicle Credit'） - **行业（中国）：**地上铁针对个别新能源货车车型，提供“保价回购”服务（evpartner 2023） | ○ | ○ | √ |
| 降低融资成本 | - **加利福尼亚州：**针对小微运输企业建立专项的贷款减值准备金（loan loss reserves），确保其获得更低的融资利率（CARB n.d., 'Zero-Emission Truck Loan Pilot Project'） | ○ | ○ |  |
| 法规 | 优先路权 | - **美国和欧盟：**洛杉矶、圣莫尼卡、鹿特丹、阿姆斯特丹、奥斯陆等城市在市中心设立了近零排放货运区（Xue et al. 2023） - **中国：**部分城市已放宽对新能源货车的道路通行限制（Xue et al. 2023） |  | √ |  |
| 提高新能源货车最大设计总质量限值 | - **欧盟：**新能源货车最大设计总质量可额外增加2吨（或最大设计总质量），并提议针对长途运输的新能源货车，最大设计总质量可额外提升4吨（EU 2019） - **美国：**新能源货车最大设计总质量可额外增加2000磅 - **中国：**暂无 | ○ | ○ |  |
| 基础设施保障 | 替代燃料和新能源汽车充电/加氢基础设施的激励政策 | - **美国：**提供资金，用于在公路沿线部署重型新能源汽车专用的充电与加氢基础设施（FHWA 2024; USEPA 2022） - **中国：**免收需量电费（State Council 2023），为充电与加氢基础设施提供建设与运营补贴（Henan Government 2020; Otog Government 2023） | √ | √ |  |

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

51

表 13 | 为弥合新能源货车与燃油货车TCO差价,政府与行业可考虑采取的措施(续)

|  措施 |   | 全球案例 | 中央政府 | 地方政府 | 行业企业  |
| --- | --- | --- | --- | --- | --- |
|  需求侧 | 基础设施保障 物流配送中心 | - 底特丹: 优化物流配送中心布局, 提高物流效率 (City of Rotterdam 2020) - 中国: 佛山和苏州等城市计划在市中心建立多级物流枢纽, 提高物流效率 (JLL 2021) |  | √ | √  |

说明: 表中措施按照中国国家与地方新能源货车推广的事权进行划分。绿色表示本文已对该措施对TCO的影响进行了量化评估。“○”表示中国尚未采取此政策或措施。“√”表示中国已采取此政策或措施。

来源: 作者基于 C40 2020。Concept Consulting Group 2022。WEF 2021 的汇总。

与单项政策相比, 上述八项政策组合能更有效地推动新能源货车更早实现与燃油货车的TCO平价。其中, 该政策组合对纯电动货车提早实现TCO平价的作用更明显。如果实施这八项政策, 纯电动货车在多数运输场景中将在MY2022 — MY2025期间就实现与燃油货车的TCO平价, 比无政策激励时的TCO平价时间提前了0~9年。相比之下, 即便有更多的补贴(特别是购置补贴), 氢燃料电池货车在多数场景下将在MY2022—MY2028期间实现与燃油货车的TCO平价, 比无政策激励时的TCO平价时间提前3~6年。总之, 实施这八项政策组合后, 多数场景中, 纯电动货车的TCO平价时间比氢燃料电池货车早0~6年, 使得纯电动货车成为最具成本竞争力的新能源货车。

对纯电动货车而言, 不同政策在不同运输场景下, 对其实现TCO平价的时间有不同的影响。其中, 除碳价政策20外, 其他政策对纯电动货车提早实现TCO平价时间的作用都较明显。具体而言:

- 新能源货车税费减免与充电补贴是所有运输场景中, 缩小纯电动货车与燃油货车TCO差价的重要措施之一。与无政策的情况相比, 新能源货车税费减免或充电补贴可将纯电动货车的TCO平价时间提前0~3年。其中, 税费减免对纯电动重型货车的作用尤为明显。实际上, 由于纯电动重型货车所享受的税费减免可高达10万元/车, 足以缩小纯电动货车与柴油重型货车的TCO差价, 使得纯电动货车提前2~3年就能实现与柴油货车的TCO平价(即MY2026—MY2028)。
- 降低新能源货车融资成本, 对城市运输场景的纯电动货车提前实现与燃油货车的TCO平价, 效果更为显著。如果实施该政策, 纯电动货车可提前0~2年实现与燃油货车的TCO平价。
- 在日行驶里程较长的运输场景(包括区域运输场景与集疏港运输场景)中, 优先路权政策对纯电动半挂

牵引车更为有效。因为本文假设该政策的影响施加在货车的日行驶里程上, 而在这些场景中, 半挂牵引车的高速路行驶里程占总行驶里程的比例比较高, 且因轴数多, 单位里程的高速收费更高。在优先路权政策下, 区域运输场景中, 42吨纯电动半挂牵引车将提前3年实现与柴油半挂牵引车的TCO平价。

- 减免新能源货车高速收费, 对区域运输场景与集疏港运输场景中的42吨纯电动半挂牵引车的影响更大。这是因为在这两个场景中, 42吨半挂牵引车的高速路行驶里程占比大且单位里程高速收费更高, 更容易受到高速收费政策的影响。在该政策下, 区域运输和集疏港运输场景中, 42吨纯电动半挂牵引车将提前0~4年实现TCO平价。
- 提高新能源货车最大设计总质量对重货运输场景作用更明显, 可将该运输场景的纯电动货车TCO平价时间提前0~4年。尽管这一措施未能将一些重货运输场景中的TCO平价时间提前至MY2030以前(如区域运输场景中的18吨载货汽车BET5000), 但仍是降低重货运输场景中纯电动货车TCO最有效的方法。例如, 如果将新能源货车最大设计总质量限值提升2吨, 18吨BET500载货汽车的TCO将降低33万元, 相比之下, 其他政策只能将其TCO降低4~11万元。

对氢燃料电池货车而言, 在所有运输场景中, 这八项政策对TCO平价时间的影响大致相当, 只能将氢燃料电池货车的TCO平价时间提前0~1年。但在不同的运输场景中, 这八项政策对降低氢燃料电池货车TCO的影响也有所差异, 具体如下:

- 虽然在没有购置补贴的情况下, 纯电动货车仍具有成本竞争力, 但本文分析显示, 氢燃料电池货车购置补贴为所有运输场景中, 降低氢燃料电池货车TCO最为有效的措施。该措施在城市运输场景尤为有效, TCO降幅最大。然而, 由于氢燃料电池货车和燃油货车的TCO差距仍较大, 氢燃料电池货车的购置补贴对提前

52

WRI.org.cn

实现TCO平价的效果有限；所有运输场景中，氢燃料电池货车的TCO平价时间仅提前0~2年。

- 新能源货车税费减免和降低新能源货车融资成本两项措施，对缩小城市运输场景中氢燃料电池货车的TCO格外有效，对降低TCO发挥的作用仅次于购置补贴。但是，随着日行驶里程的增加，这两项政策的作用将逐渐弱化。
- 在区域运输和集疏港运输等长距离运输场景中，新能源货车优先路权政策与减免高速收费政策成为降低氢燃料电池货车TCO最有效的措施，而提高最大设计总质量对重货运输场景（尤其是区域运输场景）更为有效。
- 尽管在多数场景中，加氢补贴未能对缩短氢燃料电池货车TCO平价时间发挥明显作用，但其仍是氢燃

料电池货车推广初期的重要政策。由于本文假设加氢补贴下，MY2022—MY2030枪口加氢价格维持在30元/千克，所以，加氢补贴政策与对降低氢燃料电池货车TCO的作用会随时间推移而下降。例如，区域运输场景中，18吨FCET500载货汽车的加氢补贴会从MY2026的约10万元/车迅速下降至MY2030的0元/车，补贴额度不足以填补MY2026—MY2030氢燃料电池货车与燃油货车的TCO差距。相反，在氢燃料电池货车推广早期（MY2022—MY2025），在多数运输场景中加氢补贴是八项政策中对降低氢燃料电池货车TCO最为有效的政策。

- 与纯电动货车类似，由于本文采用的碳价较低，因此，碳价对推动氢燃料电池货车TCO下降的作用有限。

图 22 | 八项政策下新能源货车实现与燃油货车TCO平价的年份

a. 4.5 吨轻型普通货车

![img-66.jpeg](img-66.jpeg)

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

53

图 22 | 八项政策下新能源货车实现与燃油货车TCO平价的年份(续)

# b.18 吨载货汽车

![img-67.jpeg](img-67.jpeg)

54

WRI.org.cn

图 22 | 八项政策下新能源货车实现与燃油货车TCO平价的年份 (续)

# c. 31 吨自卸汽车

● 重货 - 200 千米 ● 重货 - 300 千米

![img-68.jpeg](img-68.jpeg)

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

55

图 22 | 八项政策下新能源货车实现与燃油货车TCO平价的年份(续)

# d. 42 吨半挂牵引车

![img-69.jpeg](img-69.jpeg)

说明: 对于42吨半挂牵引车, DDC表示纯电动货车的DDC_THP场景和氢燃料电池货车的DDC_DWT场景。

缩略词: BET=纯电动货车; FCET=氢燃料电池货车; 纯氢=纯氢模式; UD=城市运输; RD=区域运输; DDC=集疏港运输; DDC_THP=集疏港运输(“单程运距”法); DDC_DWT=集疏港运输(“B行驶里程”法)。

来源: 作者计算。

### 3.3 本文结论的适用性

值得注意的是, 即便在相同运输场景下, 不同城市使用的货车车型、运输的货物类型与行驶工况也会有差异。因此, 读者将本文的结论应用于中国其他城市时, 应持谨慎态度。

以集疏港运输场景为例, 深圳市的集疏港运输场景与其他地区相比, 在货车车型、运输货类、行驶工况与TCO方

面均存在较大差异。例如, 河北省唐山市有世界第二大散货港 (Hebei Government 2023)。与深圳港通常使用42吨半挂牵引车运输集装箱不同, 唐山港使用49吨半挂牵引车运输铁矿石、钢材等重货 (Mao et al. 2023)。在运距方面, 唐山部分集疏港半挂牵引车的单程运距在100千米以内 (Mao et al. 2023), 因此, 多采用49吨BET100纯电动半挂牵引车; 而深圳市集疏港的运距更远, 需要至少采用42吨BET200纯电动半挂牵引车。此外, 在行驶工况方面, 唐

56

WRI.org.cn

图 23 | 深圳市和唐山市集疏港运输场景中新能源半挂牵引车与柴油半挂牵引车实现TCO 平价年份的对比

| 货车车型 | 行驶工况 | 货物类型 | 日行驶里程 (千米) | 2022 | 2023 | 2024 | 2025 | 2026 | 2027 | 2028 | 2029 | 2030 | 2030年后 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 49吨半挂牵引车 (唐山) | DDC_TRIP | 重货 | 200 |  |  |  | ● |  |  |  |  |  |  |
| 300 | ● |  |  |  |  |  |  |  |  |  |
| 400 | ● |  |  |  |  |  |  |  |  |  |
| 500 | ● |  |  |  |  |  |  |  |  |  |
| DDC_DVKT | 200 |  |  |  | ● |  |  |  |  | ▲● |  |  |
| 300 |  |  |  |  | ● |  |  |  | ▲● |  |  |
| 400 |  |  |  |  |  | ● |  |  | ▲● |  |  |
| 500 |  |  |  |  |  |  | ● |  | ▲● |  |  |
| 42吨半挂牵引车 (深圳) | DDC_TRIP | 轻抛货 | 200 |  |  |  |  |  |  |  |  |  | ● |
| 300 |  |  |  | ● |  |  |  |  |  |  |
| 400 | ● |  |  |  |  |  |  |  |  |  |
| 500 |  |  |  | ● |  |  |  |  |  |  |
| DDC_DVKT | 200 |  |  |  |  |  |  |  |  |  |  | ●▲● |
| 300 |  |  |  |  |  |  |  |  | ▲● |  | ● |
| 400 |  |  |  |  |  |  |  | ▲● |  |  | ● |
| 500 |  |  |  |  |  |  | ▲ | ● |  |  | ● |

说明：本文假设唐山市集疏港运输场景的单程运距为100千米，深圳市集疏港运输场景的单程运距为200千米。此外，MY2022唐山市49吨柴油半挂牵引车的能量消耗量为64升/100千米，而纯电动半挂牵引车的能量消耗量为230千瓦时/100千米，氢燃料电池半挂牵引车的能量消耗量为18千克/100千米。

附略例：BET=纯电动货车；FCET=氢燃料电池货车；混合=插电式混合动力模式；纯氢=纯氢模式；DDC_TRIP=集疏港运输（“单程运距”法）；DDC_DVKT=集疏港运输（“日行驶里程”法）。
来源：作者计算。

山市49吨BET100纯电动半挂牵引车多在港口附近或城市工况运行（Mao et al. 2023），而深圳市则不乏一些高速和国道工况。所以，唐山市纯电动货车与柴油货车的能效比（EER=2.8）可能比深圳市（EER=2.3）更高，即唐山市的集疏港纯电动半挂牵引车比深圳市更节能。因此，根据本文测算，唐山市集疏港运输场景中，49吨BET100纯电动半挂牵引车在MY2022就实现与柴油货车的TCO平价，比深圳市集疏港运输场景的TCO平价时间更早（见图23）。

因此，本文的研究结论仅适用于与深圳市、佛山市有近似特征的城市，包括使用同类货车、运输同类货物、具有近似运距，以及在相似行驶工况和环境温度下行驶等。

值得注意的是，本文采用的新能源货车技术与成本分析方法虽具有普适性，但仍为现实的简化版。本文的研究范围与研究方法存在局限性，研究结论也有不确定性，这些都有待未来改进，具体包括以下几点：

第一，除新能源货车的运营可行性、购置成本与TCO外，运输企业在购置新能源货车的决策过程中，也会衡量以下因素，包括货主企业对使用新能源货车要求、货运行业的盈利情况、货运市场运力的供需情况、新能源货车的安全性与可靠性、运输企业对新能源技术的认识水平（QTLC and

MOV3MENT 2022）等。此外，在全球供应链中，关键原材料与关键零部件价格的波动也会影响新能源货车的成本（BNEF 2022）。这些因素有待在未来研究中加以考虑。

第二，除本文考虑的TCO成本要素外，影响小微运输企业决策的TCO成本要素更多元，包括新能源货车较燃油货车更低的残值、因新能源货车充电或维保而产生的额外成本、低温环境或爬坡工况对新能源货车能源成本的影响等。未来，在测算新能源货车TCO时，仍有必要量化这些成本，以便提出更全面的新能源货车推广建议。

第三，良好的货运行业统计数据基础，也对制定新能源货车推广政策与指导企业投资，有着重要作用。例如，本研究显示，新能源货车能量消耗量（新能源货车与燃油货车的能效比）对新能源货车TCO平价年份有较大的影响，进而影响对近期最具新能源货车推广潜力场景的识别。因此，我们建议有关部门收集新能源货车不同场景、不同工况的实际能量消耗量，并考虑出台针对新能源货车能量消耗量的标准。此外，目前在用的燃油货车分场景的日/年行驶里程统计、道路流量数据、货车停车信息，对识别近期适宜新能源货车推广的场景、规划充电/加氢基础设施、配置新能源货车参数都起到重要作用。因此，我们建议有关部门收集并与行业相关方分享这些统计数据，以支持精细化的政策制定与企业投资。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

57

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

76

77

78

79

80

81

82

83

84

85

86

87

88

89

90

91

92

93

94

95

96

97

98

99

100

# 第四章

# 结论与建议

本文评估了2022—2030年广东省深圳市与佛山市14个城市运输与区域运输场景中，新能源货车的技术与经济可行性。

研究结果表明，政策激励、技术进步、商业模式推广与运营优化等措施都将对新能源货车的推广发挥重要的作用。为加速新能源货车的推广，政府及私营部门应通力合作。

首先，即便无政策激励，港口内运输、集疏港运输和城市配送场景中，新能源货车有望在MY2027之前实现与燃油货车的TCO平价，早于区域运输场景中新能源货车的TCO平价时间。无政策激励时，技术进步、商业模式推广与运营优化都有助于新能源货车尽早实现与燃油货车的TCO平价：

- 运输企业可通过选择小容量电池，降低纯电动货车的TCO。为支持小容量电池，运输企业、主机厂和地方政府需要对车型设计、充电基础设施与运营做出调整。有关部门需要部署足够数量的快充基础设施，保障充足的停车位与电网容量。运营企业也需对运营做出优化，如在装卸货等待时间、进港等待时间或司机休息时间进行补电。近期，运营优化可首先考虑集疏港运输场景，因为该场景中的起始点/目的地以及运营时刻表相对固定，车辆会定期返回港口（或港口附近停车场），并在相对较小的区域范围内运营。中长期，随着高速公路沿线充电设施的完善，运营优化可推广到区域运输场景中，从而推动新能源货车TCO的下降。

- 加速技术进步——包括主机厂、关键零部件制造商的技术研发与规模化量产——均有助于降低新能源货车的TCO。对于纯电动货车，TCO下降主要依赖电池成本的下降、新能源货车能量消耗量的改进以及载质量损失的改善。而对于氢燃料电池货车，TCO下降需要降低燃料电池系统的成本与氢气的价格。此外，鉴于小微运输企业通常会有“跨场景”运输的需求，主机厂需要设计广泛适用的纯电动货车，以满足运输企业多种场景的运营需求。

- 商业模式（如新能源货车租赁模式）推广有助于降低新能源货车初期购买时的一次性费用支出。为此，政府部门、金融机构和投资者需助力新能源货车创新商业模式推广方式。

其次，政策激励不仅对弥合新能源货车和燃油货车的TCO之差有突出作用，也有助于释放商业模式推广与运营优化的潜力。

- 在本文假设的政策组合下，多数场景中，纯电动货车比氢燃料电池货车要更早实现与燃油货车的TCO平价，成为最有成本竞争力的新能源技术选项。

- 除碳价外，本文假设的多数政策均有助于降低新能源货车TCO，且各项政策对降低新能源货车TCO的作用与运输场景相关。同时，相较于单项措施，政策组合下，新能源货车能更快实现与燃油货车的TCO平价。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

59

- ■ 在本文假设的政策中，购置补贴对降低氢燃料电池货车TCO最为有效。但是，政府应避免因购置补贴过高带来的货车运力过剩问题。
- ■ 能源价格对新能源货车实现与燃油货车TCO平价的时间有较大影响。因此，在燃油价格较低的情况下，有必要考虑取消现行燃油补贴（Black et al. 2023），增加燃油税（OECD 2022），或提供新能源货车能源（充电/加氢）补贴，以维持新能源货车的成本竞争力。
- ■ 新能源货车能量消耗量对其TCO平价年份有较大的影响，因此，建议有关部门收集新能源货车不同场景、不同工况的实际能量消耗量，并考虑出台针对新能源货车能量消耗量的标准。
- ■ 为支持纯电动货车运营优化，有关政府部门有必要支持公共充电桩建设，包括及早规划相应土地，保障充足的停车位与电网容量，结合市场主流新能源货车参数配置部署足够数量的快充基础设施，以及提供新能源货车充电补贴。为引导充电基础设施投资，运输企业、充电运营服务商与有关部门应就充电桩选址（如港口附近、运输中途、客户仓库、物流节点等）进行车辆运行数据（或道路流量数据、货车停车数据等）信息共享，并开展相关研究。
- ■ 为在更多场景中推广新能源货车的创新商业模式，政府部门与金融机构等应采取支持性的措施，包括帮助租赁平台降低货车贷款首付比例、提供贷款利率优惠与延长贷款期限、鼓励绿色金融或混合融资、为其租赁业务提供税收优惠与灵活折旧等政策支持，以及考虑为小微运输企业的租赁业务提供第一损失担保。
- ■ 新能源货车能量消耗量数据（新能源货车与燃油货车的能效比）对决策者制定新能源货车推广政策和主机厂设计新能源货车至关重要。因此，我们建议有关部门应收集新能源货车在不同场景、不同工况下的实际能量消耗量，并与主机厂等关键利益相关方分享，支持改善新能源货车的设计。
- ■ 此外，在本文探讨的政策基础上，我们建议读者考虑多种政策的可能，包括针对货主企业的“重点行业大气污染防治绩效分级”政策、改善新能源货车残值的措施以及组织宣传与试驾活动（特别是针对小微运输企业）等。

最后，本文的研究结论仅适用于与深圳市、佛山市具有近似特征的城市，包括使用同类货车、运输同类货物、具有近似运距，以及在相似行驶工况和环境温度下行驶等。读者将本文的结论用于中国其他城市时，应持谨慎态度。

![img-70.jpeg](img-70.jpeg)

60

WRI.org.cn

400-659-0066

![img-71.jpeg](img-71.jpeg)

![img-72.jpeg](img-72.jpeg)

![img-73.jpeg](img-73.jpeg)

![img-74.jpeg](img-74.jpeg)

B

A

B

C

1

# 附录

## 附录A. 广东省部分城市新能源货车优先路权政策

附表 A-1 | 广东省部分城市新能源货车优先路权政策

■ 所有区域全天限行 ■ 部分区域全天限行 ■ 部分区域日间限行 ■ 部分区域早晚高峰限行 ■ 所有区域均不限行
☑ 取得货车通行证后可进入限行区域

|   | 佛山市 |   |   |   | 深圳市 |   |   |   |   | 广州市 |   |   |   | 东莞市  |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   |  燃油货车 |   | 新能源货车 |   | 燃油货车 |   | 新能源货车 |   |   | 燃油货车 |   | 新能源货车 |   | 燃油货车 |   | 新能源货车  |   |
|   |  轻微、部分中型^{a} | 中重型 | 轻微、部分中型^{a} | 中重型 | 轻微型 | 中重型 | 轻微型 | 部分中重型^{b} | 中重型^{b} | 轻微、中型 | 重型 | 轻微、中型 | 重型 | 轻微型 | 中重型 | 轻微型 | 中重型  |
|  绿色物流区^{c} |  |  |  |  |  |  |  |  |  | X | X | X | X | ☑ | ☑ |  |   |
|  中心城区 | ☑ | ☑ |  | ☑ |  |  |  |  |  |  |  |  |  | ☑ | ☑ |  |   |
|  其他区域 |  | ☑ |  | ☑ |  |  |  |  |  |  |  |  |  |  |  |  |   |

说明：$^{a}$ 在佛山市，针对燃油货车，车长不超过 6 米、总质量不超过 8 吨的中型厢式货车，参照轻型货车通行政策管理；针对在广东省注册的新能源货车，核定载质量 5 吨（含）以下新能源号牌载货汽车（含轻微型货车），以及车长不超过 6 米、总质量不超过 8 吨的新能源号牌中型厢式载货汽车，除不符合限高限重通行条件的桥梁、隧道等特殊区域路段外不限行（Foshan MEEB and Foshan PSB 2022）。

$^{b}$ 在深圳市，车长不超过 6 米的纯电动中重型货车，限行的时间和路段与普通燃油轻微型货车相同；车长超过 6 米的纯电动中重型货车，限行的时间和路段与普通燃油中重型货车相同（Shenzhen PSB 2023a）。

$^{c}$ 佛山市四个绿色物流区之中仅核准限制柴油中重型货车通行，其他三个绿色物流区未限制传统燃油中重型货车通行；深圳市绿色物流区未限制传统燃油中重型货车通行，此处参照中心城区相关限行措施（Shenzhen PSB 2023b）。

$^{d}$ 表中不含外埠货车相关限行措施。

来源：作者汇总。

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

63

## 附录B. 本研究开展的调研说明

附表 B-1 | 本研究开展的调研说明

|  受访者 | 抽样方法 | 受访者数量 | 调研问题  |
| --- | --- | --- | --- |
|  不同规模的运输企业 | 根据运输场景采用便捷抽样法 | - 10家使用4.5吨轻型普通货车从事城市运输和区域运输的企业 - 3家使用31吨自卸汽车从事城市运输的企业 - 7家使用42吨半挂牵引车从事集疏港运输的企业 - 2家从事港口内运输的企业 - 7家使用42吨半挂牵引车从事区域运输和长途运输的企业 - 5家使用18吨载货汽车从事城市运输和区域运输的企业 | 典型运输场景、新能源货车应用现状及面临的挑战、能量消耗量、购置成本、TCO（如维保成本）  |
|  货车经销商 | 便捷抽样法 | - 3家货车经销商 | 能量消耗量、购置成本、TCO（如贷款和保险成本）  |
|  新能源货车专家 | 无 | - 2位新能源货车领域专家 | 关键零部件的质量和成本、主流新能源货车设计、TCO（如关键零部件更换成本）  |

来源：作者总结。

64

WRI.org.cn

## 缩略词

|  BET | 纯电动货车  |
| --- | --- |
|  BEV | 纯电动汽车  |
|  CNY | 人民币元  |
|  DDC | 集疏港运输  |
|  DMC | 直接制造成本  |
|  EER | 能效比  |
|  FC | 燃料电池  |
|  FCET | 氢燃料电池货车  |
|  FCEV | 氢燃料电池汽车  |
|  HDT | 重型货车  |
|  ICEV | 燃油汽车  |
|  ICM | 间接成本乘数  |
|  GVW | 最大设计总质量  |
|  GCW | 最大设计总质量  |
|  LDT | 轻型货车  |
|  MY | 车型年份  |
|  NEV | 新能源汽车  |
|  PO | 港口内运输  |
|  RD | 区域运输  |
|  TCO | 总拥有成本  |
|  UD | 城市运输  |
|  VKT | 车辆行驶里程  |

新能源汽车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

65

## 注释

1. 车型年份指车辆生产（或购买）的年份。
2. 见第二章“研究方法”，本文不考虑插电式混合动力汽车。
3. 新能源汽车（NEV）包括纯电动汽车（BEV）、插电式混合动力汽车（PHEV）和燃料电池电动汽车（FCEV）。
4. 本文中，运输企业指承运商、自有车队的第三方物流企业和自有车队的货主企业。
5. 具体指2020年城镇非私营单位就业人员年平均工资。
6. 清洁能源汽车包括新能源汽车与天然气汽车。
7. 货物密度指货物质量除以货物体积所得的值。
8. 假定FCET使用纯氢模式。
9. C-rate是指电池相对于其最大容量的放电速率。
10. 假设OBC的成本为486元/千瓦，DC/DC转换器的成本为389元/千瓦。本文假设这些成本不随时间而变化。
11. 假设深圳市和佛山市的车辆购置成本相同。
12. 当使用“单程运距”法设置电池容量时，BET通常需要每天充电两次以上。
13. 这意味着未来电池包成本的下降没有被考虑在内。
14. 高德地图的充电地图：https://auto.amap.com/travel。
15. 这意味着，在没有政策激励的情况下新能源货车也免除了需量电费。
16. 非正向开发的新能源货车是指使用燃油汽车现有平台开发的纯电动货车或氢燃料电池货车，而正向开发的新能源货车是指基于纯电平台设计的纯电动货车或氢燃料电池货车。
17. 该成本是牵引车的购置成本，不含挂车的价格。
18. 汇率：1美元=7.0元人民币。
19. 由于缺少实证证据，本研究未区分氢燃料电池汽车在城市运输（Urban delivery）和区域运输（Regional delivery）场景中的能量消耗量。
20. 碳价政策不显著的原因在于目前中国的碳价较低。

66

WRI.org.cn

## 参考文献

360che. n.d. “卡车之家-看车-买车-养车-聊车的商用车服务平台.” https://www.360che.com/. Accessed October 27, 2023.

Ajanovic, A., and R. Haas. 2018. “Economic Prospects and Policy Framework for Hydrogen as Fuel in the Transport Sector.” Energy Policy 123 (December): 280–88. doi:10.1016/j.enpol.2018.08.063.

Alonso-Villar, A., B. Davíðsdóttir, H. Stefánsson, E.J. Ásgeirsson, and R. Kristjánsson. 2023. “Electrification Potential for Heavy-Duty Vehicles in Harsh Climate Conditions: A Case Study Based Technical Feasibility Assessment.” Journal of Cleaner Production 417 (September): 137997. doi:10.1016/j.jclepro.2023.137997.

Al-Wreikat, Y., C. Serrano, and J.R. Sodré. 2021. “Driving Behaviour and Trip Condition Effects on the Energy Consumption of an Electric Vehicle under Real-World Driving.” Applied Energy 297 (September): 117096. doi:10.1016/j.apenergy.2021.117096.

AnyLogic. n.d. Electric Vehicle Route Optimization: Plan Delivery with Simulation Software. https://www.anylogic.com/resources/case-studies/electric-vehicle-route-optimization-delivery-with-simulation-software/. Accessed January 18, 2024.

APCUK (Advanced Propulsion Centre UK) and Austin Power. 2022. Reducing the Cost of Fuel Cells: How Can It Be Done? https://www.apcuk.co.uk/wp-content/uploads/2022/07/Reducing-the-cost-of-fuel-cells-how-can-it-be-done-report.pdf.

AQSIQ (General Administration of Quality Supervision, Inspection and Quarantine) and SAC (Standardization Administration of China). 2011. GB-T 27840-2011 Fuel Consumption Test Methods for Heavy-Duty Commercial Vehicles. http://www.camra.org.cn/static/uploadfile/content/standard/GB-T%2027840-2011.pdf.

BALM (Federal Logistics and Mobility Office). 2022. Zur Förderung von Klimaschonenden Nutzfahrzeugen Und Dazugehöriger Tank- Und Ladeinfrastruktur (06/2022). https://www.balm.bund.de/SharedDocs/Downloads/DE/Foerderprogramme/KsNI/2_Foerderaufruf/2_Foerderaufruf_KsNI_Fahrzeuge_Infrastruktur_Teil1.pdf?__blob=publicationFile&v=5.

Bank of China. n.d. “Loan Prime Rate (LPR).” https://www.bankofchina.com/fimarkets/lilv/fd32/201310/t20131031_2591219.html. Accessed February 1, 2024.

Basma, H., C. Buysse, Y. Zhou, and F. Rodríguez. 2023. Total Cost of Ownership of Alternative Powertrain Technologies for Class 8 Long-Haul Trucks in the United States. https://theicct.org/wp-content/uploads/2023/04/tco-alt-powertrain-long-haul-trucks-us-apr23.pdf.

Basma, H., A. Saboori, and F. Rodríguez. 2021. Total Cost of Ownership for Tractor-Trailers in Europe: Battery Electric Versus Diesel. https://theicct.org/wp-content/uploads/2021/11/tco-bets-europe-1-nov21.pdf.

Beijing Daxing Government. 2022. Interim Measures for Promoting the Development of the Hydrogen Energy Industry in Daxing District (Revised Edition 2022). https://www.bjdx.gov.cn/bjsdxqrz/zwfw/zfwj67/zfwj/1933672/index.html. Accessed August 17, 2023.

Beijing MEITB (Municipal Bureau of Economy and Information Technology). 2022. “Notice on the Implementation of the 2021-2022 Beijing Fuel Cell Vehicle Demonstration and Application Project Application Process.” https://www.beijing.gov.cn/fuwu/lqfw/gggs/202204/t20220408_2670154.html. Accessed August 17, 2023.

Berckmans, G., M. Messagie, J. Smekens, N. Omar, L. Vanhaverbeke, and J. Van Mierlo. 2017. “Cost Projection of State of the Art Lithium-Ion Batteries for Electric Vehicles Up to 2030.” Energies 10 (9): 1314. doi:10.3390/en10091314.

Black, S., A.A. Liu, I. Parry, and N. Vernon. 2023. “IMF Fossil Fuel Subsidies Data: 2023 Update.” IMF Working Papers 2023 (169): 1. doi:10.5089/9798400249006.001.

BNEF (BloombergNEF). 2022. “Lithium-Ion Battery Pack Prices Rise for First Time to an Average of $151/kWh.” Blog. December 6. https://about.bnef.com/blog/lithium-ion-battery-pack-prices-rise-for-first-time-to-an-average-of-151-kwh/.

BNEF. 2023. “2023 Hydrogen Levelized Cost Update: Green Beats Gray.” Blog. July 25. https://about.bnef.com/blog/2023-hydrogen-levelized-cost-update-green-beats-gray/.

Burke, A., and A.K. Sinha. 2020. Technology, Sustainability, and Marketing of Battery Electric and Hydrogen Fuel Cell Medium-Duty and Heavy-Duty Trucks and Buses in 2020–2040. Davis, CA; UC Davis. doi:10.7922/G2H993FJ.

Burnham, A., D. Gohlke, L. Rush, T. Stephens, Y. Zhou, M. Delucchi, A. Birky, et al. 2021. Comprehensive Total Cost of Ownership Quantification for Vehicles with Different Size Classes and Powertrains. Lemont, IL: Argonne National Laboratory. doi:10.2172/1780970.

C40. 2020. “Zero-Emission Freight: Vehicle Market and Policy Development Briefing for C40 Cities.” https://www.c40knowledgehub.org/s/article/Zero-emission-freight-Vehicle-market-and-policy-development-briefing-for-C40-cities?language=en_US. Accessed August 17, 2023.

CALB (China Aviation Lithium Battery Technology). 2022. CALB Global Offering. https://invest.calb-tech.com/upload/file/20220923/20220923075324.pdf.

CARB (California Air Resources Board). 2018. Battery Electric Truck and Bus Energy Efficiency Compared to Conventional Diesel Vehicles. https://www2.arb.ca.gov/sites/default/files/2018-11/180124hdbevefficiency.pdf.

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

67

CARB. 2019. "Advanced Clean Trucks Total Cost of Ownership Discussion Document." https://www2.arb.ca.gov/sites/default/files/2020-06/190225tco_ADA.pdf.

CARB. 2021a. "Draft Advanced Clean Fleets Total Cost of Ownership Discussion Document." 2021. https://www2.arb.ca.gov/sites/default/files/2021-08/210909costdoc_ADA.pdf.

CARB. 2021b. "Advanced Clean Trucks." https://www2.arb.ca.gov/our-work/programs/advanced-clean-trucks. Accessed January 18, 2024.

CARB. 2023. "Advanced Clean Fleets Regulation—Drayage Truck Requirements." https://www2.arb.ca.gov/resources/fact-sheets/advanced-clean-fleets-regulation-drayage-truck-requirements. Accessed January 18, 2024.

CARB. n.d. "Clean Off-Road Equipment Vouchers." https://www2.arb.ca.gov/our-work/programs/clean-off-road-equipment-voucher-incentive-project. Accessed January 18, 2024.

CARB. n.d. "Low Carbon Fuel Standard." https://www2.arb.ca.gov/our-work/programs/low-carbon-fuel-standard. Accessed January 17, 2024.

CARB. n.d. "Zero-Emission Truck Loan Pilot Project | California Air Resources Board." https://www2.arb.ca.gov/our-work/programs/zero-emission-truck-loan-pilot/about. Accessed December 14, 2023.

California Constitution. 2019. "Vehicle Code - VEH." 2019. https://leginfo.legislature.ca.gov/faces/codesTOCSelected.xhtml?tocCode=VEH&tocTitle=+Vehicle+Code+-+VEH. Accessed August 18, 2023.

CATARC (China Automotive Technology and Research Center). 2017. Assessment of Freight System in China. https://theicct.org/wp-content/uploads/2022/01/%E4%B8%AD%E5%9B%BD%E8%B4%A7%E4%BD%93%E7%B3%BB%E8%AF%84%E4%BC%B0%E9%A1%B9%E7%9B%AE%E6%8A%A5%E5%91%8A-201711.9.pdf.

CATARC. 2022. Research on TCO of Commercial Vehicles in China and Comparison between China and US. https://www.efchina.org/Reports-zh/report-ctp-20220701-zh. Accessed February 1, 2024.

CFLP (China Federation of Logistics and Purchasing). 2022. Report on the Small- and Medium-Sized Logistics Enterprises. http://www.chinawuliu.com.cn/lhhzq/202205/16/577968.shtml. Accessed February 1, 2024.

Changzhou Government. 2024. "Changzhou City Implements Subsidies for New Energy Vehicle Charging Services." https://www.changzhou.gov.cn/ns_news/12170433319906. Accessed February 1, 2024.

Chen, Y., and M. Melaina. 2019. "Model-Based Techno-Economic Evaluation of Fuel Cell Vehicles Considering Technology Uncertainties." Transportation Research Part D: Transport and Environment 74 (September): 234–44. doi:10.1016/j.trd.2019.08.002.

Cheng, Q., R. Zhang, Z. Shi, and J. Lin. 2024. "Review of Common Hydrogen Storage Tanks and Current Manufacturing Methods for Aluminium Alloy Tank Liners." International Journal of Lightweight Materials and Manufacture 7 (2): 269–84. doi:10.1016/j.ijlmm.2023.08.002.

China SAE (China Society of Automotive Engineers). 2021. Technology Roadmap for Energy Saving and New Energy Vehicles 2.0. Beijing, China: China Machine Press.

China SAE. 2024. Technology Roadmap for Carbon Neutrality of Commercial Vehicles 1.0." Beijing, China: China Machine Press.

City of Rotterdam. 2020. Covenant-Zero-Emission-City-Logistics-Rotterdam.Pdf. https://logistiek010.nl/app/uploads/2022/03/Covenant-Zero-Emission-City-Logistics-Rotterdam.pdf.

Concept Consulting Group. 2022. Policies to Incentivize the Uptake of Zero-Emission Trucks. https://www.concept.co.nz/uploads/1/2/8/3/128396759/policies_to_incentivise_the_uptake_of_zero-emission_trucks.pdf.

Coyne, R.G., G.J. Vera, M. Monterrubio, J. Jiménez, A. Cerezo, and T. Garduño. 2023. Expanding Access to Financing for Zero-Emission Trucks in Latin America and the Caribbean. https://globaldrivetozero.org/site/wp-content/uploads/2023/11/Expanding-Access-to-Financing-for-Zero-Emission-Trucks-in-Latin-America-and-the-Caribbean.pdf.

Danebergs, J. 2019. "Techno-Economic Study of Hydrogen as a Heavy-Duty Truck Fuel." Master's thesis. https://kth.diva-portal.org/smash/get/diva2:1372698/FULLTEXT01.pdf.

Eastmoney. 2022. "National and Local Gasoline/Diesel Price Data." 2022. https://data.eastmoney.com/cjsj/oil_default.html. Accessed February 1, 2024. EU (European Union). 2019. Regulation (EU) 2019/1242 of the European Parliament and of the Council of 20 June 2019 Setting CO2 Emission Performance Standards for New Heavy-Duty Vehicles and Amending Regulations (EC) No 595/2009 and (EU) 2018/956 of the European Parliament and of the Council and Council Directive 96/53/EC (Text with EEA Relevance)Text with EEA Relevance. http://data.europa.eu/eli/reg/2019/1242/2019-07-25/eng. Accessed January 18, 2024.

EU. 2023a. Proposal for a REGULATION OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL Amending Regulation (EU) 2019/1242 as Regards Strengthening the CO₂ Emission Performance Standards for New Heavy-Duty Vehicles and Integrating Reporting Obligations, and Repealing Regulation (EU) 2018/956. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=COM:2023:88:FIN. Accessed January 18, 2024.

68

WRI.org.cn

EU. 2023b. Regulation (EU) 2023/851 of the European Parliament and of the Council of 19 April 2023 Amending Regulation (EU) 2019/631 as Regards Strengthening the CO2 Emission Performance Standards for New Passenger Cars and New Light Commercial Vehicles in Line with the Union's Increased Climate Ambition (Text with EEA Relevance). OJ L. Vol. 110. http://data.europa.eu/eli/reg/2023/851/oj/eng. Accessed January 18, 2024.

EUCAR (European Council for Automotive R&D). 2019. "Battery Requirements for Future Automotive Applications." https://eucar.be/wp-content/uploads/2019/08/20190710-EG-BEV-FCEV-Battery-requirements-FINAL.pdf.

EC (European Commission). 2021. Roadmap on Advanced Materials for Batteries. 2021. https://energy.ec.europa.eu/system/files/2021-12/vol-3-008-2.pdf.

evpartner. 2023. "3年5万保价回购!地上铁开启新能源物流车资产价值时代-电车资源." 2023. https://www.evpartner.com/news/34/detail-69784.html. Accessed January 19, 2024.

evpartner. 2023. "换电重卡增长不如预期原因何在?" 2023. https://www.evpartner.com/news/234/detail-69597.html. Accessed July 23, 2024.

FHWA (Federal Highway Administration). 2024. Charging and Fueling Infrastructure Discretionary Grant Program. https://www.fhwa.dot.gov/environment/cfi/. Accessed January 17, 2024.

FitchRatings. 2022. "Few Chinese EV Makers Are Profitable Despite Volume Boost." September 9. https://www.fitchratings.com/research/corporate-finance/few-chinese-ev-makers-are-profitable-despite-volume-boost-13-09-2022.

Foshan MEEB (Municipal Bureau of Ecology and Environment) and Foshan PSB (Municipal Bureau of Public Security). "Announcement on the Adjustment of Truck Road Access Regulations and the Expansion of Restricted Areas for National Emission Standard III Diesel Trucks (Third Public Solicitation of Opinions)." https://www.foshan.gov.cn/hdj/pt/yjz/answer/24446. Accessed February 1, 2024.

Foshan MTB (Municipal Bureau of Transport). 2022. "Management Measures of the Operation Subsidy for New Energy Urban Delivery Trucks in Foshan." http://www.foshan.gov.cn/zwgk/zfgb/szfgfxwj/content/post_5228496.html. Accessed January 31, 2024.

Foshan Nanhai Government. 2021. "Implementation Plan for the Promotion and Application of New Energy (Hydrogen Fuel Cell) Municipal and Logistics Vehicles in Nanhai District, Foshan City (2021-2025)." http://www.nanhai.gov.cn/fsnhq/zwgk/fggw/zfgb/content/post_5065191.html. Accessed February 1, 2024.

Foshan Nanhai Government. 2022. "Promotion of Hydrogen Refueling Stations' Construction and Operation, and Support Measures for Hydrogen Fuel Cell Vehicles' Operation in Nanhai District, Foshan City (Revised in 2022)." http://www.nanhai.gov.cn/gkmlpt/content/5/5485/post_5485351.html#1975. Accessed February 1, 2024.

Fujian DRC (Development and Reform Commission, Fujian DIIT (Department of Industry and Information Technology), and Fujian DOF (Department of Finance). 2022. "Action Plan for Promoting Stable Growth of Industrial Economy in Fujian Province." https://www.fujian.gov.cn/zwgk/ztzl/yqfk/skjn/s/202204/t20220413_5890232.htm. Accessed February 1, 2024.

Gansu DOT (Department of Transport), Gansu DRC (Development and Reform Commission), and Gansu DOF (Department of Finance). 2021. "Implementation Plan for Differentiated Tolls on Expressways in Gansu Province." https://jtys.gansu.gov.cn/jtys/c106442/202202/1973069.shtml. Accessed February 1, 2024.

German Bundestag. 2012. "Gesetz Zur Änderung Des Versicherungsteuergesetzes Und Des Kraftfahrzeugsteuergesetzes (Verkehrsteueränderungsgesetz – VerkehrStÄndG)." Bundesgesetzblatt Teil I, no. 57 (December): 2431.

Gilleon, S., M. Penev, and C. Hunter. 2022. Powertrain Performance and Total Cost of Ownership Analysis for Class 8 Yard Tractors and Refuse Trucks. Washington, DC: U.S. Department of Energy, National Renewable Energy Laboratory. doi:10.2172/1899989.

Giuliano, G., M. Dessouky, S. Dexter, J. Fang, S. Hu, and M. Miller. 2021. "Heavy-Duty Trucks: The Challenge of Getting to Zero." Transportation Research Part D: Transport and Environment 93 (April): 102742. doi:10.1016/j.trd.2021.102742.

Guangdong DOT (Department of Transportation). 2020. "Guangdong Tolled Roads' Charge Standard." 2020. https://td.gd.gov.cn/zcwj_n/tzgg/content/post_2987954.html. Accessed January 31, 2024.

Guangdong DRC (Development and Reform Commission). 2018. "Notice on the Electricity Price for New Energy Vehicles in Guangdong Province." http://drc.gd.gov.cn/spjg/content/mpost_846681.html. Accessed February 1, 2024.

Guangdong DRC, Guangdong DOST (Department of Science and Technology), Guangdong DIIT (Department of Industry and Information Technology), Guangdong DOF (Department of Finance), Guangdong DOHURD (Department of Housing and Urban-Rural Development), Guangdong DEM (Department of Emergency Management), Guangdong AMR (Administration for Market Regulation), and Guangdong EA (Energy Administration). 2022. "Action Plan for Accelerating the Construction of Fuel Cell Vehicle Demonstration City Cluster in Guangdong Province (2022-2025)." https://drc.gd.gov.cn/ywtz/content/post_3993253.html. Accessed February 1, 2024.

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

69

Guangdong Government. 2022. “Notice on the Continued Implementation of Vehicle and Vessel Tax Rate.” http://czt.gd.gov.cn/czfg/content/post_4028829.html. Accessed January 31, 2024.

Guangdong Stats. 2023. Guangdong Statistical Yearbook. http://tjnj.gdstats.gov.cn:8080/tjnj/2023/index.html. Accessed January 31, 2024.

Hao, X., Z. Lin, H. Wang, S. Ou, and M. Ouyang. 2020. “Range Cost-Effectiveness of Plug-in Electric Vehicle for Heterogeneous Consumers: An Expanded Total Ownership Cost Approach.” Applied Energy 275 (October): 115394. doi:10.1016/j.apenergy.2020.115394.

Hao, X., S. Ou, Z. Lin, X. He, J. Bouchard, H. Wang, and L. Li. 2022. “Evaluating the Current Perceived Cost of Ownership for Buses and Trucks in China.” Energy 254 (September): 124383. doi:10.1016/j.energy.2022.124383.

He, N. 2021. “Overview of China EV Charging Station Industry in 2021.” MOKOSmart #1 Smart Device Solution in China. Blog. November 11, 2021. https://www.mokosmart.com/ev-charging-station-industry/.

Hebei Government. 2023. “Tangshan’s Cargo Throughput in 2022 Ranks Second in World.” https://www.hebei.gov.cn/columns/9033927e-cc80-4b5e-a266-a6a6e888c1d3/202308/23/4ded287e-cd71-4000-8a56-262d56ee2893.html. Accessed February 1, 2024.

Henan Government. 2020. “Measures to Accelerate the Construction of Electric Vehicle Charging Infrastructure in Henan Province.” https://fgw.henan.gov.cn/2020/08-06/1751577.html. Accessed February 1, 2024.

Henan People’s Congress. 2023. “Decision on Amending the ‘Regulations on the Overloading and Over-Dimension of Trucks in Henan Province.’ Draft. https://www.henanrd.gov.cn/2023/04-19/156710.html. Accessed August 17, 2023.

Hsieh, I.-Y.L., M.S. Pan, Y.-M. Chiang, and W.H. Green. 2019. “Learning Only Buys You so Much: Practical Limits on Battery Price Reduction.” Applied Energy 239 (April): 218–24. doi:10.1016/j.apenergy.2019.01.138.

HTRDC (High Technology Research and Development Center). n.d. “National Key R&D Program.” https://www.htrdc.com/gjszx/23/index.shtml. Accessed January 31, 2024.

Hunter, C., M. Penev, E. Reznicek, J. Lustbader, A. Birky, and C. Zhang. 2021. Spatial and Temporal Analysis of the Total Cost of Ownership for Class 8 Tractors and Class 4 Parcel Delivery Trucks. Washington, DC: U.S. Department of Energy, National Renewable Energy Laboratory. doi:10.2172/1821615.

Hydrogen Council. 2020. Path to Hydrogen Competitiveness: A Cost Perspective. https://hydrogencouncil.com/wp-content/uploads/2020/01/Path-to-Hydrogen-Competitiveness_Full-Study-1.pdf.

Hyundai. n.d. Hyundai Hydrogen Mobility. https://hyundai-hm.com/en/. Accessed January 16, 2024.

IEA (International Energy Agency). 2015. Technology Roadmap Hydrogen and Fuel Cells. https://www.iea.org/reports/technology-roadmap-hydrogen-and-fuel-cells. Accessed February 1, 2024.

IEA. 2023a. Global Hydrogen Review 2023. https://www.iea.org/reports/global-hydrogen-review-2023. Accessed April 16, 2024.

IEA. 2023b. Global EV Outlook 2023: Catching up with Climate Ambitions. https://www.iea.org/reports/global-ev-outlook-2023. Accessed April 26, 2023.

IEA. n.d. “Global EV Data Explorer—Data Tools.” https://www.iea.org/data-and-statistics/data-tools/global-ev-data-explorer. Accessed February 1, 2024.

IRENA (International Renewable Energy Agency). 2020. Green Hydrogen Cost Reduction: Scaling up Electrolysers to Meet the 1.50C Climate Goal. https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2020/Dec/IRENA_Green_Hydrogen_cost_2020.pdf?rev=95b8c10569874148a44e1d17b301d263.

IRENA. 2021. Making the Breakthrough: Green Hydrogen Policies and Technology Costs. https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2020/Nov/IRENA_Green_Hydrogen_breakthrough_2021.pdf.

Jenu, S., A. Hentunen, J. Haavisto, and M. Pihlatie. 2022. “State of Health Estimation of Cycle Aged Large Format Lithium-Ion Cells Based on Partial Charging.” Journal of Energy Storage 46 (February): 103855. doi:10.1016/j.est.2021.103855.

Jenu, S., A. Manninen, S. Tuurala, and A. Hentunen. 2018. “Simplified State of Health Diagnostics Tool.” https://h2020invade.eu/wp-content/uploads/2017/06/D6.3-Simplified-state-of-health-diagnostics-tool.pdf.

Jinan University. 2022. “Carbon Price in the Guangdong, National, and EU ETS Market.” https://lcerc.jnu.edu.cn/2023/0302/c36583a737697/page.htm. Accessed February 1, 2024.

JLL (Jones Lang LaSalle). 2021. “White Paper on China’s Logistics Real Estate Market.” April 10, 2021. https://www.joneslanglasalle.com.cn/zh/trends-and-insights/research/china-logistics-report. Accessed February 1, 2024.

Kast, J., R. Vijayagopal, J.J. Gangloff, and J. Marcinkoski. 2017. “Clean Commercial Transportation: Medium and Heavy Duty Fuel Cell Electric Trucks.” International Journal of Hydrogen Energy 42 (7): 4508–17. doi:10.1016/j.ijhydene.2016.12.129.

Kok, I., M.R. Bernard, Y. Xie, and T. Dallmann. 2023. Accelerating ZEV Adoption in Fleets to Decarbonize Road Transportation. https://theicct.org/wp-content/uploads/2023/05/ZEVTC_fleets-briefing_final.pdf.

König, A., L. Nicoletti, D. Schröder, S. Wolff, A. Waclaw, and M. Lienkamp. 2021. “An Overview of Parameter and Cost for Battery Electric Vehicles.” World Electric Vehicle Journal 12 (1): 21. doi:10.3390/wevj12010021.

70

WRI.org.cn

Kotz, A., K. Kelly, J. Lustbader, S. Cary, and B. Oakleaf. 2022. Port of New York and New Jersey Drayage Electrification Analysis. Washington, DC: U.S. Department of Energy, National Renewable Energy Laboratory. doi:10.2172/1908569.

Lane, B., M.M. Kinnon, B. Shaffer, and S. Samuelsen. 2022. "Deployment Planning Tool for Environmentally Sensitive Heavy-Duty Vehicles and Fueling Infrastructure." Energy Policy 171 (December): 113289. doi:10.1016/j.enpol.2022.113289.

Lin, X., H. Zhu, P. Lin, C. Lin, H. He, Y. He, and Z. Chen. 2021. Data Analysis and Recommendations on Special Survey of Road Freight Transportation Volume in Guangdong Province. https://106.3.149.173/Search/get/167866?db=cats_qikan_glys. Accessed February 1, 2024.

Ma, S.-C., B.-W. Yi, and Y. Fan. 2022. "Research on the Valley-Filling Pricing for EV Charging Considering Renewable Power Generation." Energy Economics 106 (February): 105781. doi:10.1016/j.eneco.2021.105781.

Macquarie. 2021. "Macquarie Group Limited | Global Financial Services." 2021. https://content.macquarie.com/macquarie-capital/asia/2021/events/indo-mining-mar/Global%20auto%20and%20battery%20demand_Quantifying%20metal%20demand.pdf.

Mao, S., H. Basma, P.-L. Ragon, Y. Zhou, and F. Rodríguez. 2021. Total Cost of Ownership for Heavy Trucks in China: Battery-Electric, Fuel Cell Electric, and Diesel Trucks. https://theicct.org/publication/total-cost-of-ownership-for-heavy-trucks-in-china-battery-electric-fuel-cell-and-diesel-trucks/. Accessed December 27, 2023.

Mao, S., T. Niu, F. Rodríguez, C. Hao, S. Wang, and Z. Zhang. 2023. Real-World Use Cases for Zero-Emission Trucks: A Comparison of Electric and Diesel Tractors in Tangshan, China. https://theicct.org/wp-content/uploads/2023/09/real-world-zero-emission-trucks-tangshan-sept23.pdf.

Marcinkoski, J., R. Vijayagopal, J. Kast, and A. Duran. 2016. "Driving an Industry: Medium and Heavy Duty Fuel Cell Electric Truck Component Sizing." World Electric Vehicle Journal 8 (1): 78-89. doi:10.3390/wevj8010078.

Mauro Erriquez, Thomas Morel, Pierre-Yves Moulière, and Philip Schäfer. 2017. "Trends in Electric-Vehicle Design | McKinsey." https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/trends-in-electric-vehicle-design. Accessed February 1, 2024.

MEE (Ministry of Ecology and Environment). 2021. China Mobile Source Environmental Management Annual Report. https://www.mee.gov.cn/hjzl/sthjk/ydyhgl/202109/W020210910400449015882.pdf.

Meszler, D., O. Delgado, and L. Yang. 2019. Heavy-Duty Vehicles in China: Cost-Effectiveness of Fuel-Efficiency and CO2 Reduction Technologies for Long-Haul Tractor-Trailers in the 2025–2030 Timeframe. https://theicct.org/wp-content/uploads/2021/06/China_HDV_long-haul_efficiency_cost_20190312.pdf.

Mihelic, R., M. Roeth, K. Otto, and J. Lund. 2020. Making Sense of Heavy-Duty Hydrogen Fuel Cell Tractors. North American Council for Freight Efficiency. https://www.researchgate.net/profile/Rick-Mihelic/publication/347463378_Making_Sense_of_Heavy-Duty_Hydrogen_Fuel_Cell_Tractors/links/5fdcc8fa299bf1408822763d/Making-Sense-of-Heavy-Duty-Hydrogen-Fuel-Cell-Tractors.pdf.

MIIT (Ministry of Industry and Information Technology). 2021. "NEV Battery Swapping Mode Application and Demonstration." https://www.miit.gov.cn/xwdt/gxdt/sjdt/art/2021/art_c73f1ade7759456fa18586114b555238.html. Accessed February 29, 2024.

MIIT. 2022. Catalogue of New Energy Vehicle Models Exempt from Vehicle Purchase Tax. https://www.miit.gov.cn/zwgk/zcwj/wjfb/gg/art/2022/art_056bdde01c9642a8bcd2977e3125b1dc.html. Accessed January 31, 2024.

MIIT, MOT (Ministry of Transport), NDRC (National Development and Reform Commission), MOF (Ministry of Finance), MEE (Ministry of Ecology and Environment), MOHURD (Ministry of Housing and Urban-Rural Development), NEA (National Energy Administration), and SPB (State Post Bureau). 2023. "Notice on Launching the Pilot Program for the Full Electrification of Vehicles in Public Services." 2023. https://www.gov.cn/zhengce/zhengceku/2023-02/03/content_5739955.htm. Accessed January 31, 2024.

Mišić, J., V. Popović, and M. Stanković. 2022. "Fleet Management and Vehicle Fleet Optimization." KNOWLEDGE—International Journal 52 (3): 385-92.

MOF, MIIT, MOST (Ministry of Science and Technology), and NDRC (National Development and Reform Commission). 2021. "Notice on the Financial Subsidy for the Promotion and Application of New Energy Vehicles in 2022." https://www.gov.cn/zhengce/zhengceku/2021-12/31/content_5665857.htm. Accessed June 6, 2023.

MOF, MIIT, MOST, NDRC, and NEA (National Energy Administration). 2020. "Notice on Launching Fuel Cell Vehicle Demonstration Projects." https://www.gov.cn/zhengce/zhengceku/2020-10/22/content_5553246.htm. Accessed August 17, 2023.

MOF, STA (State Taxation Administration), and GACC (The General Administration of Customs of the People's Republic of China). 2019. "Announcement on Relevant Policies for Deepening the Value-Added Tax Reform." https://www.chinatax.gov.cn/n810341/n810755/c4160283/content.html. Accessed January 31, 2024.

MOF, STA, and MIIT (Ministry of Industry and Information Technology). 2018. "Notice on the Preferential Ownership Tax for Energy-Saving and New-Energy Vehicles and Vessels." https://www.gov.cn/zhengce/zhengceku/2019-10/25/content_5445047.htm. Accessed January 31, 2024.

MOF, STA, and MIIT. 2023. "Announcement on the Extension of Preferential Purchase Tax for New Energy Vehicles." https://www.gov.cn/zhengce/zhengceku/202306/content_6887734.htm. Accessed January 31, 2024.

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

71

Nair, V., S. Stone, G. Rogers, and S. Pillai. 2022. "Medium and Heavy-Duty Electrification Costs for MY 2027–2030." https://blogs.edf.org/climate411/wp-content/blogs.dir/7/files/2022/02/EDF-MDHD-Electrification-v1.6_20220209.pdf.

National Petroleum Council. 2012. Light-Duty Engines & Vehicles. https://www.energy.gov/sites/default/files/2022-10/Chapter_9-LD_Engines-Vehicles.pdf.

NDRC (National Development and Reform Commission). 2021. "Notice on Further Improving the Time-of-Use Electricity Pricing Mechanism." https://www.ndrc.gov.cn/xxgk/zcfb/tz/202107/t20210729_1292067.html. Accessed February 1, 2024.

Niu, T., Y. Ma, and Y. Zhang. 2023. Real-World Use Cases for Zero-Emission Trucks: Market Review and Policy Suggestions for Guangdong Province. https://theicct.org/wp-content/uploads/2023/10/ZETs-Guangdong-working-paper-22-A4-70074-v4.pdf.

NPC (National People's Congress). 2018. China Vehicle Purchase Tax Law. https://www.chinatax.gov.cn/n810341/n810755/c3987147/content.html. Accessed January 31, 2024.

Nykvist, B., and O. Olsson. 2021. "The Feasibility of Heavy Battery Electric Trucks." Joule 5 (4): 901–13. doi:10.1016/j.joule.2021.03.007.

OECD (Organisation for Economic Co-operation and Development). 2022. Pricing Greenhouse Gas Emissions: Key Findings for China. https://www.oecd.org/tax/tax-policy/carbon-pricing-china.pdf.

Orient Securities. 2019. Electric Vehicle Cost Reduction and Profitability Analysis. https://pdf.dfcfw.com/pdf/H3_AP20190411318176636_1.pdf.

Otog Government. 2023. "Notification on the Initiative to Promote Green Transportation in Qiemeng Region by Otog." http://www.eq.gov.cn/zwgk/zdxxgk/zcfg_97667/fzb_gfxwj/202312/t20231214_3542292.html. Accessed February 1, 2024.

Ouyang, D., S. Zhou, and X. Ou. 2021. "The Total Cost of Electric Vehicle Ownership: A Consumer-Oriented Study of China's Post-Subsidy Era." Energy Policy 149 (February): 112023. doi:10.1016/j.enpol.2020.112023.

PBC (People's Bank of China) and CBIRC (China Banking and Insurance Regulatory Commission). 2017. "Notice on the Adjustment of Policies Related to Auto Loans." https://www.gov.cn/xinwen/2017-11/09/content_5238240.htm.

Penske. 2023. "Penske Electric Trucks and Vehicles—Penske Truck Leasing." https://www.pensketruckleasing.com/full-service-leasing/leasing-services/electric-vehicles/. Accessed February 1, 2024.

Pers. Comm. (Personal communication). 2023a. Personal communication between the authors and 38 fleet operators and freight internet platforms in Shenzhen and Foshan, February–October.

Pers. Comm. 2023b. Personal communication between the authors and three truck dealers, February–October.

Pers. Comm. 2023c. Personal communication between the authors and two new energy truck experts, October.

Phadke, A., A. Khandekar, N. Abhyankar, D. Wooley, and D. Rajagopal. 2021. "Why Regional and Long-Haul Trucks Are Primed for Electrification Now." https://www.osti.gov/servlets/purl/1834571/. Accessed August 30, 2023.

Qi T. 2022. "Economic Analysis of Heavy Truck Battery Swap Mode," Commercial Vehicle 5: 46–48.

Qiu, B., R. Yu, Y. Liu, D. Zhao, and J. Song. 2021. "A Comparative Study on Economy of Battery and Fuel Cell Electric Vehicles of Different Application Scenarios Based on Learning Rate." Automotive Engineering 43 (2): 296–304. doi: 10.19562/j.chinasae.qcgc.2021.02.019.

QTLC (Queensland Transport and Logistics Council) and MOV3MENT. 2022. Addressing Barriers to Zero Emission Trucks in Queensland to 2025. https://www.qtlc.com.au/wp-content/uploads/2022/02/QTLC-EV-Report-2022.pdf.

Reja, B., Paul Amos, and Fan Hongye. 2013. China Road Tolls Policy: Past Achievements and Future Directions. https://www.worldbank.org/en/news/opinion/2013/06/14/china-road-tolls-policy-past-achievements-and-future-directions.

Ren, H., L. Xia, and P. Li. 2024. "Economic Analysis of Battery Electric Vehicle Fast Charging Mode and Battery Swapping Mode in China." In Proceedings of the 2023 4th International Conference on Management Science and Engineering Management (ICMSEM 2023), edited by S.H.B.D.M. Zailani, K. Yagapparaj, and N. Zakuan, 259:1226–35. Advances in Economics, Business and Management Research. Dordrecht, Netherlands: Atlantis Press International BV. doi:10.2991/978-94-6463-256-9_125.

RMI (Rocky Mountain Institute). 2022. China Green Hydrogen New Era 2030: China Renewable Hydrogen 100GW Roadmap. https://rmi.org.cn/wp-content/uploads/2022/07/Chinas-Green-Hydrogen-New-Era-2030-Chinas-Renewable-Hydrogen-100GW-Roadmap.pdf.

Rogozhin, A., M. Gallaher, G. Helfand, and W. McManus. 2010. "Using Indirect Cost Multipliers to Estimate the Total Cost of Adding New Technology in the Automobile Industry." International Journal of Production Economics 124 (2): 360–68. doi:10.1016/j.ijpe.2009.11.031.

Rout, C., H. Li, V. Dupont, and Z. Wadud. 2022. "A Comparative Total Cost of Ownership Analysis of Heavy Duty On-Road and Off-Road Vehicles Powered by Hydrogen, Electricity, and Diesel." Heliyon 8 (12): e12417. doi:10.1016/j.heliyon.2022.e12417.

Ruf, Y., T. Zorn, J. Rehberger, M. Baum, and A. Menzel. 2020. Study on Fuel Cells Hydrogen Trucks. https://www.clean-hydrogen.europa.eu/media/publications/study-fuel-cells-hydrogen-trucks_en. Accessed February 1, 2024.

72

WRI.org.cn

SAC/TC576. 2019. "GA 802-2019 Road traffic management-Types of motor vehicles." https://std.samr.gov.cn/hb/search/stdHBDetailed?id=A699B8B2410A1628E05397BE0A0A69CF. Accessed January 31, 2024.

Sankar, N., S. Vasudevan, R. Modwel, A. Khandelia, S.N. Albal, A. Bagga, K. Ayapilla, et al. 2022. Driving Affordable Financing for Electric Vehicles in India. https://www.niti.gov.in/sites/default/files/2023-07/ADB-EV-Financing-Report_VS_compressed.pdf.

Sharpe, B., and H. Basma. 2022. A Meta-Study of Purchase Costs for Zero-Emission Trucks. https://theicct.org/wp-content/uploads/2022/02/purchase-cost-ze-trucks-feb22-1.pdf.

Shell Corporation. 2023. "Germany – Shell Hydrogen Pay-Per-Use." 2023. https://www.shell.com/what-we-do/hydrogen.html. Accessed May 20, 2024.

Shen, C., and S. Mao. 2023. Zero-Emission Bus and Truck Market in China: A 2022 Update. https://theicct.org/wp-content/uploads/2023/12/ID-57-%E2%80%93-ZETs-China_Final.pdf.

Shenzhen DRC (Development Reform Commission). 2022. "Action Plan for Hydrogen Industry Innovation and Development in Shenzhen City (2022-2025)." Draft for comments. http://fgw.sz.gov.cn/hdjlpt/yjzj/answer/21361. Accessed February 1, 2024.

Shenzhen MTB (Municipal Bureau of Transport). 2021. Implementation Rules for the Subsidy of Shenzhen's Green Transportation in the Maritime and Port Areas. http://jtys.sz.gov.cn/zwgk/xgkml/zcfgjjd/gfxwjcx/content/post_9497349.html. Accessed February 1, 2024.

Shenzhen MTB. 2023. Implementation Rules for the Subsidy of Shenzhen's Green Transportation in the Maritime and Port Areas. http://www.sz.gov.cn/zfgb/2023/gb1286/content/post_10605156.html. Accessed January 31, 2024.

Shenzhen MEEB (Municipal Bureau of Ecology and Environment). 2022. "Shenzhen Blue Sustainable Action Plan (2022-2025)." Draft for comments http://meeb.sz.gov.cn/hdjlpt/yjzj/answer/17453. Accessed January 31, 2024.

Shenzhen PSB (Municipal Bureau of Public Security). 2022. "Announcement Regarding Continuing Restrictions on Truck Traffic in Certain Areas and Roads." https://www.sz.gov.cn/cn/xgk/zfxxgj/tzgg/content/post_10254459.html. Accessed February 1, 2024.

Shenzhen PSB. 2023a. "Announcement on Continued Implementation of Preferential Road Access Policies for Battery Electric Logistics Vehicles." http://szjj.sz.gov.cn/gkmlpt/content/10/10666/post_10666420.html#2275. Accessed February 1, 2024.

Shenzhen PSB. 2023b. "Announcement on the Addition of Green Logistics Zones and Implementation of Traffic Management Measures Restricting the Access of Light Diesel Trucks." http://szjj.sz.gov.cn/ZWGK/TZGG/GGJG/content/post_10839610.html. Accessed February 1, 2024.

Shenzhen PSB. 2023c. "Announcement on the Continued Implementation of Traffic Management Measures Restricting the Access of Light Diesel Trucks in Green Logistics Zones." http://szjj.sz.gov.cn/gkmlpt/content/10/10715/post_10715112.html#2275. Accessed February 1, 2024.

NEICV (Shenzhen Xieli Innovation Center of New Energy and Intelligent Connected Vehicle). 2022. Implementation Plan and Comprehensive Benefit Evaluation of Electric Promotion and Application of Heavy Truck Sector in Shenzhen City. https://www.efchina.org/Attachments/Report/report-ctp-20220801-2/%E6%B7%B1%E5%9C%B3%E5%B8%82%E9%87%8D%E5%9E%8B%E8%B4%A7%E8%BD%A6%E7%94%B5%E5%8A%A8%E5%8C%96%E6%8E%A8%E5%B9%BF%E5%BA%94%E7%94%A8%E5%AE%9E%E6%96%BD%E6%96%B9%E6%A1%88%E5%8F%8A%E7%BB%BC%E5%90%88%E6%95%88%E7%9B%8A%E8%AF%84%E4%BC%B0.pdf.

Singer, M., C. Johnson, E. Rose, E. Nobler, and L. Hoopes. 2023. Electric Vehicle Efficiency Ratios for Light-Duty Vehicles Registered in the United States. https://www.nrel.gov/docs/fy23osti/84631.pdf.

SINOIOV and Chang'an University. 2022. Annual Report on Big Data Analysis of Highway Freight Transport in China (2021). https://www.sinoiov.com/news/official/330.html. Accessed February 2, 2024.

Sinosynergy. 2022. "Sinosynergy Global Offering." https://www.sinosynergypower.com/eindex.html. Accessed February 1, 2024.

Sohu. 2023. "Electric Heavy-Duty Truck Sales Surpassed 20,000 in 2022, with Battery Swapping Trucks Taking the Lead." https://www.sohu.com/a/www.sohu.com/a/635,410,189_120063592. Accessed January 31, 2024.

Soone, J. 2023. "Revision of the Weights and Dimensions Directive." https://www.europarl.europa.eu/RegData/etudes/BRIE/2023/754595/EPRS_BRI(2023)754595_EN.pdf.

State Council. 2023. "Guidance on Further Building a High-Quality Charging Infrastructure System." https://www.gov.cn/zhengce/zhengceku/202306/content_6887168.htm. Accessed February 29, 2024.

Tetra Tech and GNA. 2022. "2021 Update: Feasibility Assessment for Drayage Trucks." https://kentico.portoflosangeles.org/getmedia/c4ce-da78-54d5-44ce-bf4c-68c41f8d3a22/draft-2021-update-drayage-truck-feasibility-assessment-update. Accessed February 1, 2024.

Tianjin MTC (Municipal Transportation Commission) and Tianjin DRC (Development Reform Commission). 2021. "Notice Regarding the Adjustment of Differentiated Toll Policies for Expressways in Tianjin City." https://jtys.tj.gov.cn/ZWGK6002/ZCWJ_1/WZFWI/202201/t20220125_5788986.html. Accessed February 1, 2024.

Tol, D., T. Frateur, M. Verbeek, I. Riemersma, and H. Mulder. 2022. Techno-Economic Uptake Potential of Zero-Emission Trucks in Europe. https://www.agora-verkehrswende.de/fileadmin/Veranstaltungen/2022/Elektrische-Lkw/TNO_2022_R11862_Techno-economic_uptake_potential_of_zero-emission_trucks_in_Europe.pdf.

新能源货车在城市和区域运输场景中的技术与经济可行性分析:以中国广东省为例

73

Transport and Environment. 2021. How to Decarbonise Long-Haul Trucking in Germany. An Analysis of Available Vehicle Technologies and Their Associated Costs. https://www.transportenvironment.org/wp-content/uploads/2021/07/2021_04_TE_how_to_decarbonise_long_haul_trucking_in_Germany_final.pdf.

TUC. 2022a. "2022 China Heavy-Duty Truck Total Cost of Ownership Report." https://wetuc.com/article/639ffa6afa85782aba1877e1. Accessed January 31, 2024.

TUC. 2022b. "2022 China Road Capacity Development Data White Paper." 商业新知网. USBLS (U.S. Bureau of Labor Statistics). 2020. "Heavy and Tractor-Trailer Truck Drivers." https://www.bls.gov/. Accessed February 2, 2024.

USCB (U.S. Census Bureau). 2020. "Income in the United States: 2020." https://www.census.gov/. Accessed February 2, 2024.

USDOE (U.S. Department of Energy). 2023. Heavy-Duty Fuel Cell System Cost-2022. 2023. https://www.hydrogen.energy.gov/docs/hydrogenprogramlibraries/pdfs/23002-hd-fuel-cell-system-cost-2022.pdf?Status=Master.

USDOE. n.d. "DOE Technical Targets for Onboard Hydrogen Storage for Light-Duty Vehicles." Energy.Gov. https://www.energy.gov/eere/fuelcells/doe-technical-targets-onboard-hydrogen-storage-light-duty-vehicles. Accessed January 31, 2024.

USDOT (U.S. Department of the Treasury), Internal Revenue Service. n.d. "Commercial Clean Vehicle Credit." https://www.irs.gov/credits-deductions/commercial-clean-vehicle-credit. Accessed January 17, 2024.

USDOT, Internal Revenue Service. n.d. "Used Clean Vehicle Credit." https://www.irs.gov/credits-deductions/used-clean-vehicle-credit. Accessed January 17, 2024.

U.S. DRIVE. 2017a. "Electrical and Electronics Technical Team Roadmap." https://www.energy.gov/eere/vehicles/articles/us-drive-electrical-and-electronics-technical-team-roadmap. Accessed February 28, 2024.

U.S. DRIVE. 2017b. "Fuel Cell Technical Team Roadmap." https://www.energy.gov/eere/vehicles/articles/us-drive-fuel-cell-technical-team-roadmap. Accessed February 28, 2024.

USEPA (U.S. Environmental Protection Agency). 2022. "Clean Heavy-Duty Vehicle Program." Overviews and Factsheets. December 6. https://www.epa.gov/inflation-reduction-act/clean-heavy-duty-vehicle-program.

USEPA. 2024. Greenhouse Gas Emissions Standards for Heavy-Duty Vehicles—Phase 3. https://www.govinfo.gov/content/pkg/FR-2024-04-22/pdf/2024-06809.pdf.

Van Velzen, A., J.A. Annema, G. Van De Kaa, and B. Van Wee. 2019. "Proposing a More Comprehensive Future Total Cost of Ownership Estimation Framework for Electric Vehicles." Energy Policy 129 (June): 1034–46. doi:10.1016/j.enpol.2019.02.071.

Wang, Z., Q. Liu, D. Mullaney, R. McLane, and Y. Zhang. 2020. Putting Electric Logistics Vehicles to Work in Shenzhen. https://rmi.org.cn/wp-content/uploads/2022/07/20210521544365137.pdf.

Wang R., D. Yang, X. Chang, X. Tan, Y. Xing, X. Li, L. Xue, and K. Chen. 2024. Optimizing container ports' transportation and distribution systems toward a low-carbon future: A Shenzhen port case study. Washington, DC: World Resources Institute. https://wri.org.cn/research/Optimizing-container-ports-transportation-and-Distribution-systems-toward-a-low-carbon-future. Accessed May 20, 2024.

https://www.shangyexinzhi.com/article/5081662.html. Accessed January 31, 2024.

WEF (World Economic Forum). 2021. "Road Freight Zero: Pathways to Faster Adoption of Zero-Emission Trucks." https://www.weforum.org/publications/road-freight-zero-pathways-to-faster-adoption-of-zero-emission-trucks/. Accessed August 17, 2023.

WEF. 2023. "Green Hydrogen in China: A Roadmap for Progress." 2023. https://www3.weforum.org/docs/WEF_Green_Hydrogen_in_China_A_Roadmap_for_Progress_2023.pdf.

Wu, G., A. Inderbitzin, and C. Bening. 2015. "Total Cost of Ownership of Electric Vehicles Compared to Conventional Vehicles: A Probabilistic Analysis and Projection across Market Segments." Energy Policy 80 (May): 196–214. doi:10.1016/j.enpol.2015.02.004.

Xie, Y., H. Basma, and F. Rodríguez. 2023. Purchase Costs of Zero-Emission Trucks in the United States to Meet Future Phase 3 GHG Standards. https://theicct.org/wp-content/uploads/2023/03/cost-zero-emission-trucks-us-phase-3-mar23.pdf.

Xinhua Finance. 2023. "The Ranking of National Port Throughput in 2022 Released." https://www.cnfin.com/zs-lb/detail/20230131/3795096_1.html. Accessed January 31, 2024.

Xue, L., and D. Liu. 2022. Decarbonizing China's Road Transport Sector: Strategies toward Carbon Neutrality. Washington, DC: World Resources Institute. doi:10.46830/wrirpt.21.00145.

Xue, L., J. Liu, Y. Wang, X. Liu, and Y. Xiong. 2020. "Action Plans and Policy Recommendations on Vehicle Grid Integration in China." https://files.wri.org/d8/s3fs-public/2022-01/action-plans-policy-recommendations-vehicle-grid-integration-china_0.pdf?VersionId=N_9qVIMgzvUb132BB_px-9MhP7pikbk12. Accessed January 31, 2024.

Yang, Z. 2018. Fuel-Efficiency Technology Trend Assessment for LDVs in China: Vehicle Technology. https://theicct.org/sites/default/files/publications/PV_Tech_Trend_Vehicle_20180917.pdf.

Yelle, L.E. 1979. "The Learning Curve: Historical Review and Comprehensive Survey." Decision Sciences 10 (2): 302–28. doi:10.1111/j.1540-5915.1979.tb00026.x.

74

WRI.org.cn

Yu, Y., Y. Zhang, Q. Wang, H. Wang, Z. Liao, H. Guo, Z. Ruan, et al. 2024. Technology Outlook on Wind and Solar Power toward China's Carbon Neutrality Goal. https://www.efchina.org/Reports-zh/report-snp-20240131-zh. Accessed April 18, 2024.

ZEFES (Zero Emissions Flexible Vehicle Platforms with Modular Powertrains Serving the Long-Haul Freight Eco System). n.d. "ZEFES | Taking Zero-Emission Long-Haul Freight Transport in Europe to the next Level." https://zefes.eu/. Accessed January 19, 2024.

Zhang, G., and Z. Jiang. 2023. "Overview of Hydrogen Storage and Transportation Technology in China." *Unconventional Resources* 3: 291–96. doi:10.1016/j.uncres.2023.07.001.

Zhao, H., Q. Wang, L. Fulton, M. Jaller, and A. Burke. 2018. A Comparison of Zero-Emission Highway Trucking Technologies. https://escholarship.org/uc/item/1584b5z9. Accessed October 30, 2023.

## 作者介绍

**陈轲**，交通分析员，世界资源研究所（美国）北京代表处。邮箱：ke.chen@wri.org

**薛露露**，中国交通项目总监，世界资源研究所（美国）北京代表处。邮箱：l.xue@wri.org

新能源货车在城市和区域运输场景中的技术与经济可行性分析：以中国广东省为例

75

## 关于世界资源研究所

世界资源研究所是一家独立的研究机构，其研究工作致力于寻求保护环境、发展经济和改善民生的实际解决方案。

### 我们的挑战

自然资源构成了经济机遇和人类福祉的基础。但如今，人类正以不可持续的速度消耗着地球的资源，对经济和人类生活构成了威胁。人类的生存离不开清洁的水、丰饶的土地、健康的森林和安全的气候。宜居的城市和清洁的能源对于建设一个可持续的地球至关重要。我们必须在未来十年中应对这些紧迫的全球挑战。

### 我们的愿景

我们的愿景是通过对自然资源的良好管理以建设公平和繁荣的地球。我们希望推动政府、企业和民众联合开展行动，消除贫困并为全人类维护自然环境。

### 我们的工作方法

#### 量化

我们从数据入手，进行独立研究，并利用最新技术提出新的观点和建议。我们通过严谨的分析、识别风险，发现机遇，促进明智决策。我们重点研究影响力较强的经济体和新兴经济体，因为它们对可持续发展的未来具有决定意义。

#### 变革

我们利用研究成果影响政府决策、企业战略和民间社会行动。我们在社区、企业和政府部门进行项目测试，以建立有力的证据基础。我们与合作伙伴努力促成改变，减少贫困，加强社会建设，并尽力争取卓越而长久的成果。

#### 推广

我们志向远大。一旦方法经过测试，我们就与合作伙伴共同采纳，并在区域或全球范围进行推广。我们通过与决策者交流，实施想法并提升影响力。我们衡量成功的标准是，政府和企业的行动能否改善人们的生活，维护健康的环境。

## 图片说明

Cover Pony.ai; pg. i Unsplash/Max Zhang; pg. ii Unsplash/Dmitry Grachyov; pg. vi Pony.ai; pg. vii Unsplash/Joshua Fernandez; pg. xiv Harry Zhang; pg. xvi Unsplash/Focus Pictures; pg. xviii Unsplash/aay; pg. xxvi foshannews.net/Foshan Daily; pg. xxvii Unsplash/Weichao Deng; pg. xxviii Unsplash/Zhu Yunxiao; pg. 2 zhongguangwl.com; pg. 2 电车资源网; pg. 4 Unsplash/Joshua Fernandez; pg. 20 Unsplash/Jason Yuen; pg. 36 电车资源网; pg. 58 Unsplash/Vincent Lin; pg. 60 361cv.com; pg. 62 Jason Yuen.

76

WRI.org.cn

世界资源研究所 (WRI) 出版物，皆为针对公众关注问题而开展的适时性学术性研究。
世界资源研究所承担筛选研究课题的责任，并负责保证作者及相关人员的研究自由，同时积极征求和回应咨询团队及评审专家的指导意见。若无特别声明，出版物中陈述观点的解释权及研究成果均由其作者专属所有。

Creative Commons

Copyright 2024 World Resources Institute. 版权所有
本产品由创用 (Creative Commons) 4.0 许可授权，许可副本参见 http://creativecommons.org/licenses/by/4.0/

![img-75.jpeg](img-75.jpeg)

世界资源研究所
WORLD RESOURCES INSTITUTE

世界资源研究所(美国)北京代表处
北京市东城区东中街9号
东环广场写字楼A座7层K-M室
邮编:100027
电话:+86 10 6416 5697
WWW.WRI.ORG.CN

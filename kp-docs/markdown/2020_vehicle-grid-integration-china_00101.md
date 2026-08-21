---
doc_id: 2020_vehicle-grid-integration-china_00101
source_pdf: kp-docs/CN-KPs-PDF/2020_vehicle-grid-integration-china_00101.pdf
extraction_method: postgres-full-text
parse_backend: mistral
parse_model: mistral-ocr-latest
char_count: 101580
title: 中国电动汽车与电网协同的路线图与政策建议
title_en: Action Plans and Policy Recommendations on Vehicle Grid Integration in China
authors: Xue, Lulu; Liu, Jian; Wang, Ying; Liu, Xiaoshi; Xiong, Ying
article_type: Report
wri_primary_office: WRI China
language: zh
status: needs_review
---

世界资源研究所
WORLD RESOURCES INSTITUTE

新能源汽车如何更友好地接入电网
HOW DO ELECTRIC VEHICLES FRIENDLY INTERACT WITH THE ELECTRIC GRID

# 中国电动汽车与电网协同的路线图与政策建议

ACTION PLANS AND POLICY RECOMMENDATIONS ON VEHICLE
GRID INTEGRATION IN CHINA

薛露露 刘坚 王颖 刘小诗 熊英

WRI.ORG.CN

《新能源汽车如何更友好地接入电网》系列
旨在探讨中国新能源汽车与能源（电网）融合发展的必要性与路线图。该研究系列由两篇报告组成。《中国电动汽车与电网协同的路线图与政策建议》为系列二。

校对：谢亮
hippie@163.com

设计与排版：张烨
harryzy5204@gmail.com

![img-0.jpeg](img-0.jpeg)

# 目录

VII 执行摘要

XV Executive Summary

1 第 1 章 背景

1 电动汽车推广及无序充电对电网的影响日益突出
1 电动汽车为可再生能源发电提供灵活调节的资源

5 第 2 章 电动汽车与电网协同的定义和类型

5 电动汽车的可调度性
7 电动汽车与电网协同的方式
9 电动汽车与电网协同的应用场景

15 第 3 章 国内外电动汽车与电网协同相关实践

15 国际电动汽车与电网协同试点概览
19 加利福尼亚州电动汽车与电网协同路线图
20 中国电动汽车与电网协同实践案例

23 第 4 章 中国电动汽车与电网协同的可行性分析

25 经济可行性分析
34 政策保障缺口分析
42 技术标准可行性分析
49 用户接受度分析

51 第 5 章 未来车网协同路线图与相关建议

56 关于推广有序充电的建议
58 关于推广 V2G 试点的建议

61 附录一 内部收益率和投资回收期计算

62 附录二 车网协同所涉及的软件、硬件升级与改造

63 参考文献

65 注释

# 图目录

|  图 1 | 北京私家车日平均停车、行驶和充电时间分布 | 6  |
| --- | --- | --- |
|  图 2 | 北京电动私家车一天不同时段里平均停车时长、充电时长对比 | 6  |
|  图 3 | 北京电动私家车一天不同时段里停车数量、充电数量占电动汽车总量的比例 | 6  |
|  图 4 | 电动汽车与电网协同的范围界定 | 8  |
|  图 5 | 车网协同的不同应用场景：用户侧、输配电侧与电源侧效益 | 9  |
|  图 6 | 全球V2G项目分布 | 15  |
|  图 7 | 电动汽车与电网协同的目标 | 16  |
|  图 8 | 国际车网协同试点采用直流充电、交流充电与二者兼顾的数量占比 | 18  |
|  图 9 | 车网协同各保障机制间的关系 | 24  |
|  图 10 | 车网协同项目的收支构成 | 25  |
|  图 11 | V2X在车端、桩端、网端的成本构成 | 26  |
|  图 12 | 日产汽车Vehicle to Home (V2H)系统 | 30  |
|  图 13 | 2020年、2030年各应用场景有序充电和V2X经济性对比 | 33  |
|  图 14 | 电池折旧成本和V2X电损对削峰填谷经济性的影响 | 33  |
|  图 15 | 典型城市一般工商业与居民峰谷电价比 | 36  |
|  图 16 | 实现电动汽车与电网协同所需的通信协议、硬件设备与软件系统升级 | 42  |
|  图 17 | 车网协同所需车侧、桩侧、网侧信息 | 42  |
|  图 18 | 支持V2X所需的车辆及充电桩的硬件设备改造 | 43  |
|  图 19 | 以充电运营商为主的有序充电优化控制方式 | 44  |
|  图 20 | 以配电网运营商为主的有序充电优化控制方式 | 45  |
|  图 21 | 不同车型一天内出行时间对比及对V2X潜在接受程度差异 | 49  |
|  图 22 | 中国电动汽车与电网协同路线图 | 52  |

II

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

# 表目录

|  表 1 | 电动汽车作为储能设施与作为出行工具所提供调节电量比较 | 5  |
| --- | --- | --- |
|  表 2 | 基于实现机制的电动汽车与电网协同方式分类 | 7  |
|  表 3 | 火电厂与电动汽车提供调频、调峰和爬坡服务的性能对比 | 11  |
|  表 4 | 国际车网协同主要的应用场景与协同方式 | 16  |
|  表 5 | 国际知名电动汽车与电网协同试点项目概览 | 17  |
|  表 6 | 国际车网协同试点常见阻碍 | 18  |
|  表 7 | 国内典型电动汽车与电网协同试点项目概览 | 20  |
|  表 8 | 中国与国际在车网协同的制度与技术进展上的差异对比 | 23  |
|  表 9 | 不同应用场景下车网协同的收益构成 | 26  |
|  表 10 | 住宅小区：削峰填谷成本收益影响因素（2020年） | 27  |
|  表 11 | 住宅小区削峰填谷：有序充电和V2B的经济性对比 | 28  |
|  表 12 | 基于有序充电和V2B的分布式光伏互动经济性对比 | 29  |
|  表 13 | V2G方式提供调频服务的经济性分析 | 31  |
|  表 14 | 电动汽车通过有序充电和V2X方式参与需求响应的经济性对比 | 32  |
|  表 15 | 中国车网协同政策保障机制的缺口 | 34  |
|  表 16 | 中国36个中心城市居民和工商业峰谷电价执行情况与电价信号传导程度 | 35  |
|  表 17 | 美国圣地亚哥天然气和电力公司（SDG&E）居民用户电动汽车充电峰谷电价（夏季）与深圳、上海夏季居民峰谷电价的比较 | 35  |
|  表 18 | 国内外电力市场比较 | 37  |
|  表 19 | 全国各地电力市场的准入门槛 | 38  |
|  表 20 | 辅助服务与需求响应市场（对电储能的）准入门槛以及对电动汽车的负荷集成要求 | 41  |
|  表 21 | 国际车网协同不同应用场景对响应时间、持续时长的要求 | 47  |
|  表 22 | 动力电池单体与系统性能发展趋势 | 48  |
|  表 23 | 有序充电不同措施效果比较 | 49  |
|  表 24 | 不用车网协同应用适用的场所 | 53  |
|  表 25 | 推广车网协同的主要阻碍、政策建议与优先级汇总 | 54  |
|  表 26 | 有序充电所涉及的软件、硬件和通信协议升级 | 57  |
|  表 27 | V2G所涉及的车-桩-网间通信协议升级 | 58  |

中国电动汽车与电网协同的路线图与政策建议

III

## 词汇表

|  **新能源汽车** | 包含纯电动汽车、插电式混合动力汽车和氢燃料电池汽车，不含混合动力汽车。  |
| --- | --- |
|  **电动汽车** | 指纯电动汽车。  |
|  **乘用车** | 指9座及9座以下乘用车，对应国家标准中的MI类，包括轿车、交叉型乘用车等。根据用途不同，乘用车包括私家车、出租车、公务用车等。  |
|  **电动汽车无序充电** | 指电动汽车用户随时、随地和随机进行充电，不对充电时间和充电功率进行引导与控制。  |
|  **电动汽车单向有序充电** | 简称“有序充电”，指在满足电动汽车充电需求的前提下，运用峰谷电价的经济措施或者智能控制措施，优化调整电动汽车充电时序与功率。  |
|  **电动汽车双向充放电（V2X）** | 指在满足电动汽车充电需求的前提下，将电动汽车视作储能设施，当电网/本地负荷过高时，由电动汽车向电网或本地负荷馈电；当电网/本地负荷过低时，可通过有序充电，调整本地负荷的峰谷差。  |
|  **目录电价** | 指对没有参与电力市场交易的终端用户，政府按照用户类别制定的销售电价。根据终端用户不同，目录电价可分为居住、工商业和大工业目录电价。目录电价由购电成本、输配电成本、输配电损耗、政府性基金等费用构成。  |
|  **电力批发市场** | 指发电企业与大用户、售电商开展直接交易、现货交易和期货等电力衍生品交易的市场，主要特点是交易的电能量大且为发电平衡提供辅助服务。电力批发市场为中长期电能量市场、现货电能量市场、电力辅助服务市场的统称。  |
|  **中长期电能量市场** | 指开展年、月、周等长时间周期的双边交易、集中竞价交易或挂牌交易的电力批发市场，目的是实现市场主体中长期合约签订、偏差调整和价格波动风险管理。  |
|  **现货电能量市场** | 指开展日前、日内或实时现货交易，可采用分时节点电价或边际分时电价的电力批发市场。理想情况下，现货电能量市场能够真实反映电力在不同时间、地理空间的市场价格。  |
|  **电力辅助服务市场** | 指为维护电力系统的安全稳定运行，保证电能质量，除正常电能生产、输送、使用外，由发电企业、电网经营企业和电力用户提供的服务所形成的市场。中国当前的辅助服务市场包括一次调频、自动发电控制、调峰、备用、黑启动等。  |

IV

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

# **自动发电控制（AGC）**

也称二次调频，指发电机组提供足够的可调整容量及一定的调节速率，在允许的调节偏差下实时跟踪频率，以满足电力系统频率稳定的要求。

# **负荷集成商**

指能够集合一定量的电动汽车的实体或平台，以满足电动汽车参与容量或电能量市场的最小容量和持续时间等准入门槛。电网企业、大型用电用户如住宅小区业主或工业园区、集中式充换电站、充电运营服务商、共享出行服务平台等，均具备成为负荷集成商的潜力。

# **虚拟电厂**

指通过先进信息通信和智能技术实现分布式电源、可控负荷和用户侧储能的联合调控，作为电厂参与电力市场和电网运行，实现电源侧调控和负荷侧调控的结合。

中国电动汽车与电网协同的路线图与政策建议

V

# 7

# 执行摘要

## 主要结论

- 未来中国大规模电动汽车和可再生能源推广为车网协同提供了机遇。随着可再生能源在发电结构中的比重大幅提升，在发电侧对大量灵活电源以及在需求侧对可调节负荷资源的需求，都将不断增加。2025年和2030年，全社会的电动汽车在理想情况下能够提供储能容量将相当于2018年中国储能装机总规模的8倍和23倍，具备作为可调节负荷以及灵活电源的潜力。
- 与国际实践从初期就尝试让电动汽车参与高频次、高精度的批发市场交易所不同，当前中国的电动汽车与电网协同试点项目侧重于解决配网侧开放容量不足的问题；绝大多数试点仍处于技术可行性论证阶段，经济激励机制缺失。
- 电动汽车以有序充电方式参与局部削峰填谷，利用峰谷电价差“套利”，具有更可观的经济性；未来电动汽车参与调频辅助服务将具有更高的市场价值。因而，2025年之前，电动汽车可充分发挥其灵活负荷的优势，以有序充电方式参与用户侧的削峰填谷、分布式光伏充电、需求响应、调峰辅助服务、现货市场平衡等应用。随着电力市场改革释放更多红利以及动力电池成本下降、寿命提升，电动汽车可进而发挥分布式电源的作用，结合微电网、虚拟电厂等试点平台，以双向充放电方式提供调频、现货电力平衡等服务，争取在2030年以前形成具有示范意义的模式。
- 要实现车网协同的经济潜力，电价政策、电力市场制度以及车-桩-网充电标准仍需细化，包括：形成针对电动汽车的峰谷电价机制；提供建设、设备改造及运营相关的补贴，鼓励物业公司与业主委员会配合；明确电动汽车在定位上是否属于分布式发电系统、是否可以虚拟电厂身份参与各类电力市场；鼓励整车厂或充电设备制造商在生产中提供软件更新接口支持有序充电；修订车-桩间通讯协议与系统要求，制定桩-网间通讯协议与系统要求，以支持车网协同的各类应用。

中国电动汽车与电网协同的路线图与政策建议

VII

电动汽车的推广可减缓气候变化、减少空气污染，但大规模电动汽车的无序充电也将给发电、输电、配电系统带来挑战。与家用电器等负荷不同，电动汽车负荷具有高度的灵活和可调节性。除了作为灵活负荷，电动汽车还可以作为储能设施进行“放电”，不仅可以降低电动汽车充电对电网的影响，也可为电力系统调控提供新的调度资源，更能避免大量电网和电源相关的投资浪费。目前，电动汽车可以通过有序充电或双向充放电（Vehicle-to-Grid or Vehicle-to-Building，以下简称“V2G”、“V2B”或“V2X”）两种方式，实现与电网协同（见图ES-1）。

国际方面，电动汽车和电网协同的试点项目开展至今已有10年，与电动汽车普及的时间基本相同，其中86%的探索集中在欧美国家。欧美国家已开展的试点显示，电

动汽车参与削峰填谷、分布式光伏充电、需求响应、调频辅助服务、备用服务和缓解输电线路阻塞等应用场景具备技术和经济方面的可行性。美国加利福尼亚州更是出台了《加利福尼亚州电动汽车与电网协同路线图——电动汽车作为电网资源》，从商业模式、政策支持和技术标准等方面为车网协同提供全面保障。

国内方面，与国际实践从初期就尝试让电动汽车参与高频次、高精度的批发市场交易不同，受制于中国电力市场改革进程，当前中国的车网协同试点项目侧重于解决配网侧开放容量不足的问题，尚未出现任何旨在鼓励电动汽车参与电力批发市场交易的试点。此外，绝大多数试点仍处于技术可行性论证阶段，由于经济激励机制缺失，商业可行性未在论证验证之列。

图 ES-1 | 电动汽车与电网协同方式与应用场景

![img-1.jpeg](img-1.jpeg)

说明：虽然两种车网协同方式能够参与各种应用场景，但其必要性存在差异。实践为较为有意义的应用（如有序充电参与用户侧削峰填谷），虚线为缺乏实际推广意义的应用（如有序充电延缓输电线路阻塞）。

VIII

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

未来，中国大规模电动汽车和可再生能源的推广为车网协同提供了机遇。根据国家发展和改革委员会能源研究所与国家可再生能源中心预测（2017），在既定政策情景下，2030年中国可再生能源发电量占比可能会从2019年年底的27.9%上升至51%。可再生能源在发电结构中的比重大幅提升，在发电侧对大量灵活电源（如储能设施）以及在需求侧对可调节负荷资源（如供热电锅炉、建筑空调）等的需求都将不断增加。根据同样研究的预测，截至2025年和2030年，全社会的电动汽车在理想情况下能够提供的储能容量将分别达250GW和730GW，相当于2018年中国储能装机总规模的8倍和23倍，具有可再生能源推广后作为可调节负荷以及灵活电源的潜力。

我国的车网协同虽然起步比欧美国家略晚，但具备后发优势，可借鉴欧美经验，避免对电网和电源的公共投资，辅助可再生能源并网消纳，促进电动汽车推广。探索中国的本地化车网协同实施路径，需要从中国电力市场发展阶段、特有制度机制、技术标准出发，分析不同车网协同应用在中国未来的潜力与阻碍。

在经济潜力上，本文估算在管制的电力市场下，目前电动汽车以有序充电方式参与局部削峰填谷进行峰谷电价差“套利”，具有更可观的经济性，2020年的投资回报率可达23%，这与国际上调频普遍具有更高的经济价值有所

不同；在2030年以后，随着V2X成本的下降，调频将具有更高的市场价值（图ES-2）。受发布频次的影响，需求响应的经济性略低于削峰填谷和调频。考虑到对电池寿命的影响，目前V2X的经济性普遍偏低；但从2030年后，随着电池成本的下降及使用寿命的提升，V2X的经济性将快速得到改善。但这一经济潜力仍为理想值：受电力价格、电力市场准入、充电技术标准的约束，车网协同的经济潜力往往难以在短期内变现。

在制度上，若要实现车网协同的经济潜力，相关政策、市场制度和监管规则仍需细化：第一，分别有28%和50%的中心城市采纳了居民峰谷电价或工商业峰谷电价，由于其他地区峰谷电价的缺失以及转供电加价的问题，电动汽车以有序充电的方式参与的削峰填谷应用缺乏经济激励机制。第二，电动汽车以V2G方式参与调频辅助服务、现货电力市场平衡等应用，不仅受电力市场完善程度的外因影响，也受电力市场准入制度的内因影响——包括电动汽车是否属于分布式发电系统、电动汽车聚合后是否可以虚拟电厂身份参与各类电力市场（即获得发电主体的地位）等问题，均有待明确。

在技术标准上，“车-桩”间标准只需对部分直流通信协议（即国家标准GB/T27930—2015《电动汽车非车载传导式充电机与电池管理系统之间的通信协议（直流

图 ES-2 | 不同车网协同方式及应用在中国的内部收益率（2020年和2030年）

![img-2.jpeg](img-2.jpeg)

中国电动汽车与电网协同的路线图与政策建议

IX

充电)》及系统要求(即国家标准GB/T18487.1—2015《电动汽车传导充电系统 第1部分:通用要求》)进行优化,即可支持有序充电,而支持交流有序充电所需要的修改更多。“充电桩-电网”之间的信息交换相关的通信协议,仍视市场规模、市场主体以及配网信息保密程度而定。最后,V2G更需要克服电动汽车与电网协同工况下对电池衰减的影响。

在用户接受度上,有序充电和V2X对中国用户仍为新鲜事物。现阶段电动汽车推广还存在续航不足、成本过高、充

电桩数量有限等挑战,而车网协同对动力电池寿命以及用户出行刚需的更进一步影响可能会抑制用户接受度。

中国未来推广车网协同的具体路线,需要结合电力市场改革、电池成本下降等外部条件,也需要考虑电动汽车自身优势,分时期、分步骤地探索适宜的应用场景。本研究建议(图ES-3)如下:

- ■ **近期(2025年之前):**电动汽车可充分发挥其灵活负荷的优势,以有序充电方式参与用户侧的削

图 ES-3 | 中国电动汽车与电网协同路线图

■ 电动汽车储能功率(GW) ■ 电动汽车储能电量(GWh)

![img-3.jpeg](img-3.jpeg)

|  应用场景 | ·削峰填谷、缓解配网增容 | ·分布式光伏充电 | ·需求响应 ·调峰辅助服务 ·现货市场平衡 | ·调频辅助服务 ·调峰辅助服务 | ·现货市场平衡 ·爬坡辅助服务 ·备用辅助服务 | ·缓解输电线路阻塞  |
| --- | --- | --- | --- | --- | --- | --- |
|  电力价格与市场机制阻碍 | ·缺乏终端峰谷电价机制或其他经济激励 | - | - | ·调频市场存在参与主体及准入门槛限制 | ·电力现货市场尚未成熟运行和全面推广 ·爬坡辅助服务未推出 | ·电力现货市场节点电价尚未成熟运行和全面推广  |
|  并网限制 | - | - | - | 有限制 | 有限制 | 有限制  |
|  协议标准阻碍 | ·用户自发响应峰谷电价,无技术门槛 ·充电标准稍作优化可支持直流有序充电 | - | ·人工响应,无技术门槛 ·自动响应受标准制约 | ·充电标准不支持V2X | ·充电标准不支持V2X | ·充电标准不支持V2X  |
|  对动力电池的影响 | - | - | - | 可能有影响 | 可能有影响 | 可能有影响  |

来源:电动汽车储能预测来源于国家发展和改革委员会能源研究所与国家可再生能源中心2017

说明:车网协同应用场景中,不同颜色代表不同推广时间阶段,红色(■)代表近期,橙色(■)代表2025年左右,绿色(■)代表2025年后。

X

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

峰填谷、分布式光伏充电、基于人工响应的需求响应、调峰“填谷”辅助服务、现货市场平衡，甚至调频等应用。目前，国网上海市电力公司、国网冀北电力公司已组织电动汽车（充电桩）参与需求响应、调峰辅助服务；在广东现货市场中，大型电动汽车充电站正参与电力现货市场试运行中。未来，随着电动汽车以第三方独立辅助商正式纳入调频辅助市场，将有望以有序充电方式提供调频等更多元的市场服务。

■ 中远期（2025年以后）：随着电力市场改革释放更多的红利以及动力电池成本的下降与寿命的提升，电动汽车可进而发挥其储能与分布式电源的作用，结合微电网、虚拟电厂等试点平台，以V2X方式提供调频、现货电力平衡、爬坡服务，争取在2025—2030年形成具有示范意义的项目与模式。

实现以上规划的路线图，还需要政府部门与行业协会提供重要的制度保障，通过优化政策制度和出台技术标准，撬动车网协同的商业潜力、公共接受度（表ES-1）。具体建议包括：

对有序充电而言，可考虑采取如下措施搭建商业模式，形成支持有序充电的车-桩-网通信协议标准与技术：

- ■ 针对单独计量的电动汽车充电桩——如住宅小区私人桩充电，专门设计针对电动汽车的峰谷电价体系，加大峰谷差。
- ■ 提供有序充电设施的建设补贴及交流桩的直流改造费用；公共充电设施采购中优先要求采购支持灵活智能充电的设施；允许充电运营商通过中长期、现货、调峰和需求响应等电力市场购电或提供相关服务，改善充电基础设施商业模式。
- ■ 鼓励物业企业与业主委员会配合有序充电试点的开展，引导不同主体（电网企业、充电运营服务商）参与有序充电。
- ■ 针对车-桩间充电通信协议：优先修订直流充电国家标准《电动汽车非车载传导式充电机与电池管理系统之间的通信协议》（GB/T27930—2015），支持直流有序充电；鼓励配电开放容量有限的住宅小区对私人交流桩进行改造或新建小功率直流桩，支持直流有序充电；建议第三方机构对不同品牌车辆、充电桩的接口标准执行情况进行检测，以此作为市场准入的标准。
- ■ 针对桩—网间通信协议：鼓励配电网运营商分享本地电动汽车充放电负荷上限等处理后、非敏感的信息，支持多元化实施主体参与创新。

对V2G而言，需要支持V2G试点示范的开展以及提供必要制度和技术标准保障：

- ■ 以科研资金或国家示范项目等形式，鼓励V2G试点开展技术可行性与经济可行性的论证，加强大数据分析、车网协同优化控制软件、可再生能源出力预测等方面的技术储备。
- ■ 分步骤地放宽电力市场对电动汽车的准入限制；鼓励电动汽车参与需求响应、调峰辅助服务市场及电力中长期市场；对电动汽车参与调频辅助服务市场，可先以试点形式参与，待效果得到验证后，再允许全面准入。
- ■ 明确电动汽车作为分布式发电系统的定位，并制定电动汽车接入电网的技术标准、工程规范和相关流程及管理办法。
- ■ 修订电动汽车直流充电国家标准，支持双向充放电；探索充电桩-充电运营服务商-电网间的通信接口、信息交互内容与流程。
- ■ 开展车网协同工况下的动力电池衰减测试，优化电池管理系统及电池双向充放电策略。

中国电动汽车与电网协同的路线图与政策建议

XI

表 ES-1 | 推广车网协同的主要阻碍、政策建议与重要程度汇总

|   | 主要阻碍 | 政策建议 | 重要程度  |
| --- | --- | --- | --- |
|  有序充电  |   |   |   |
|  政策与制度 | 终端用户峰谷电价机制： 部分地区没有居民、工商业的峰谷电价，且受充电服务费、转供电加价影响，峰谷电价传导不畅 | 地方发展和改革部门： ·设置电动汽车（充电桩）专用的峰谷电价 ·提供有序充电设施的建设补贴及交流桩的直流改造费用 ·公共充电设施采购中优先要求采购支持灵活智能充电的设施 ·允许充电运营商通过中长期、现货、调峰和需求响应等电力市场购电或提供相关服务 | 高  |
|  技术与标准 | 车-桩-网通信协议： ·“车-桩”间协议：交流充电协议为支持有序充电所需的改动较大，直流充电协议所需的改动较小 ·“桩-网”间协议：缺乏国家标准，仍需探索不同的实施主体和技术途径下，支持有序充电的通信协议 | 标准制定机构： ·优先修订直流充电国家标准《电动汽车非车载传导式充电机与电池管理系统之间的通信协议》（GB/T27930—2015），支持直流有序充电 | 高  |
|   |   |  地方住房和城乡建设部门、发展和改革部门： ·鼓励物业企业与业主委员会积极配合，引导不同主体（电网企业、充电运营服务商）参与有序充电 | 高  |
|   |   |  标准制定机构、整车生产企业、充电设备制造商： ·委托第三方机构对不同品牌车辆、充电桩的接口标准执行情况进行检测验证，作为市场准入前提 ·鼓励整车生产企业或充电设备制造商在生产中提供软件更新接口，通过低成本的软件更新方式，支持有序充电 | 高  |
|   |   |  地方住房和城乡建设部门、发展和改革部门、负荷集成商： ·鼓励推广小功率直流桩替代交流桩，实现直流有序充电 | 中  |
|   |   |  负荷集成商： ·延续目前第三方信息采集的方式（用户手动输入或接入车端远程监控平台），获取必要信息，实现交流有序充电 | 低  |
|   |   |  发展和改革部门、电网企业： ·鼓励配电网运营商分享本地电动汽车充放电负荷上限等处理后、非敏感信息 | 中  |

XII

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

表 ES-1 | 推广车网协同的主要阻碍、政策建议与重要程度汇总（续）

|   | 主要阻碍 | 政策建议 | 重要程度  |
| --- | --- | --- | --- |
|  **V2G**  |   |   |   |
|  政策与制度 | 电力市场完善程度与准入门槛： 中国电力市场的市场机制有待完善，正经历全面的改革过程——缺口包括竞争性市场机制、市场参与主体范畴、市场准入门槛 | 国家及地方发展和改革部门、能源部门： · 调频辅助服务；可先以试点形式放宽对电动汽车的限制 · 需求响应、调峰、中长期市场；现阶段，鼓励电动汽车作为负荷，参与需求响应、调峰辅助服务及中长期市场、促进可再生能源消纳 | 低  |
|   |  用户侧资源接入电网的管理要求： 《分布式发电管理办法》（国家能源局2018）中未明确电动汽车是否属于分布式发电系统范畴。与分布式光伏、热电冷热联供等分布式发电系统不同，政府部门与电网企业尚未建立关于电动汽车发电接入配电网的运行制度和机制 | 国家及地方发展和改革部门、能源部门： · 制定电动汽车（及充电桩）接入电网的技术标准、工程规范和相关流程及管理意见 | 中  |
|  技术与标准 | 车-桩-网通信协议： · “车-桩”网协议：国家标准不支持V2X | 国家及地方发展和改革部门、能源部门等： · 提供科研资金或政策支持V2G试点，对技术可行性与经济可行性进行论证 | 中  |
|   |  · “桩-网”网协议：缺乏国家标准，仍有待探索不同的实施主体和技术途径下，支持V2X的通信协议 | 标准制定机构： · 研究基于直流充电的双向充放电通信标准，并验证直流充电标准对调频等高精度服务的支持程度 | 中  |
|   |  电池衰减： V2X可能加速动力电池衰减 | 整车生产企业、电池生产企业、研究机构： · 测试车网协同工况下的动力电池衰减情况，优化电池管理系统及相关充放电策略 | 中  |

中国电动汽车与电网协同的路线图与政策建议

XIII

# EXECUTIVE SUMMARY

The widespread adoption of plug-in electric vehicles (PEV) can bring about air quality and climate change benefits. However, the concurrent, unmanaged charging of PEVs will result in surges in power loads and strain power generation, transmissions, and distribution, leading to costly public investments on grid expansions.

Unlike other types of loads, vehicles' charging loads are highly flexible in term of charging time and charging powers. Harnessing PEVs' load flexibility and storage capacity, PEVs can friendly integrate into the grid system, reducing grid capacity augmentation needs.

serving as grid assets and virtual power plants to support large renewable integration. These favourable results are achieved by deploying Vehicle Grid Integration (VGI) measures, where PEVs can smartly import electric powers from the grid (known as Managed Charging) or export electric powers to the grid (known as Vehicle-to-Grid, V2G). VGI can enable an array of services with different values from time-shifting (demand-charge reduction), distribution upgrade deferral, to frequency regulations (including primary reserve and AGC), spinning, non-spinning, and supplemental reserves, ramping supports for renewables, and the more.

**Figure ES-1 | Different VGI methods and applications**

![img-4.jpeg](img-4.jpeg)

中国电动汽车与电网协同的路线图与政策建议

XV

According to the survey conducted by this study, China’s VGI pilots differ from global VGI pilots in many aspects. Compared to global VGI pioneers that can be traced to the early years of PEV adoption, VGI pilots in China are an only recent phenomenon. Unlike global VGI projects that focus on frequency regulation with high commercial values, China’s VGI projects mainly focus on deploying managed charging to defer distribution upgrades where the commercial viability remains unclear. Furthermore, most of the VGI pilots in China led by the National State Grid aims at testing VGI’s technical feasibility.

Renewable energy and electric vehicles are strategic emerging industries had hold great

potential for coordination. Renewable energy accounts for 26.7% of China’s power generation in 2019 and will possibly increase to 51% by 2030. Among the efforts to promote renewable integration considered by Chinese government, electric vehicles can play a prominent role in demand side management and flexible grid assets. As predicted by Energy Research Institute (2017), the total storage capacity of electric vehicles will reach 250 GW and 730 GW respectively in 2025 and 2030, approximately eight and twenty-three times of the installed capacities of the stationary storage systems.

Although China is lagging on VGI exploration, it has late-comer advantages. Given China’s specific

**Figure ES-2 | Economic Potentials of different VGI applications in China (2020 and 2030)**

![img-5.jpeg](img-5.jpeg)

XVI

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

electricity market mechanisms and charging standards, the research performs contextualized analysis on the economic potentials of different VGI applications along with the regulatory and technical hindrances.

As calculated by this study, commercially, under the current regulated market regime, PEV's participating in time-shifting would deliver the highest values to customers with 23% internal return on investments at 2020; the economic returns of frequency regulation will exceed that of time-shifting by 2030. Demand responses provide the third highest values. In recent years, the economic returns of managed charging are considerable, whereas V2G will not be commercially viable until 2030 when the costs of V2G-capable investments (on vehicles, charging points, and grid systems) and the costs of batteries begin to drop. However, PEVs in China can barely capitalize on VGI values provided by time-shifting or the revenues generated through electricity trading and third-party services, because of the regulatory and technical barriers of electricity market access.

First, lack of Time-of-Use (TOU) utility tariffs, the barriers on interconnection and access to electricity markets for distributed resources like PEVs are the main regulatory barriers to implement VGI. Although TOU tariffs can offer an effective approach to manage private PEV's charging loads, they are often absent: cities like Beijing do not opt for residential TOU rates, and commercial tariffs are often fixed rates determined by facility owners. Furthermore, the prevailing interconnection, market access regulations, and equal allocation dispatching mechanisms are designed for large power plants and centralized stationary storages; distributed, behind-the-meter resources like PEVs face considerable entry barriers on electricity trading and third-party services. However, as China launches the electricity market reforms—piloting spot electricity markets in eight regions, these entry barriers will be removed and the economic values of VGI will be unleashed.

Second, technically, communication standards, VGI-capable hardware, and smart battery management system are necessary preconditions

to enable VGI. China's national standard on vehicles and charging points (EVSE) communication protocol (GB/T 27930) does not support managed charging or bi-directional charging. Furthermore, the communication protocols among EVSE, charge point operators (CPO), and distribution system operators (DSO) are widely absent. Apart from communication protocols, PEV, charging points, and distribution systems also face hardware upgrade to enable load management and bidirectional electric flows. Although specific hardware upgrades are often dependent on communication protocols, some basic upgrades are always necessary, like telemetry and bi-directional meters. Last but not the least, battery degradation is major hurdle to the public acceptance of V2G. Battery degradation tests and the design of smart battery management systems should be carried out under various VGI cycles to avoid the impacts.

For VGI to thrive in China, the above regulatory, economic and technical barriers should be overcome by creating synergies among different actors. There are plenty opportunities for growth in VGI amid increasing renewable energy integration, and China can take phased approach to adopt VGI measures on scales.

- From now to 2025, China is ready for a commercial rollout of managed charging. Managed charging is an evitable solution to overcome the prevailing charging infrastructure bottlenecks and provide DSO services, while providing demand-side responses, ancillary peak services, and intra-day balancing services to fill load valleys and match evenings' wind spikes.
- From 2025 onwards, V2G for frequency regulation and other wholesale market services will be feasible with the adoption of V2G-capable technologies and less-regulated electricity market. While private EVs provide largest capacities and energies, public acceptance is a major roadblock for the widespread rollout for V2G. Therefore, small-scale V2G pilots using public and commercial fleets such as government fleets, school buses, urban freight fleets to support renewable integration will be feasible.

中国电动汽车与电网协同的路线图与政策建议

XVII

**Figure ES-3 | Roadmap and action plans of VGI in China**

![img-6.jpeg](img-6.jpeg)

**Source:** the forecasts of EVs' storage capacity and renewable generation ratio are from Energy Research Institute of NDRC (2017)

**Note:** red (■) represents recent, orange (■) represents 2025 or so, blank represents not suitable for VGI.

XVIII

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

To achieve the above-planned roadmap, the following actions are needed to provide essential regulatory and technical safeguards in order to unlock VGI's market potentials and public acceptance. Concrete recommendations include (Table ES-1):

For Managed Charging, the recommendations include:

- Design EV-only TOU tariff for residential chargers and increase the differences between the peak and valley tariffs.
- Subsidize the procurement and installation of managed charging facilities; include managed charging facilities in the public procurement requirement; allow charging service operators to access bulk energy market, inter-day market, and peak ancillary market to create more diverse revenue sources.
- Encourage property owners to collaborate with different aggregators to pilot managed charging.
- Amend GB/T27930 to support direct current (DC) managed charging and encourage the upgrade of alternate-current (AC) chargers to DC chargers to allow for DC managed charging; encourage using cellphone APPs or connecting to national new energy vehicle monitoring platform to gather necessary vehicle information to allow for AC managed charging.
- Hire third-party to certify new energy vehicles to increase EVs compliance to the existing charging standard and remove the charging protective mode to allow for managed charging at the vehicle manufacturing stage.
- Encourage DSO operators to provide non-sensitive load information to enable managed charging conducted by different aggregators.

For V2G, the recommendations include:

- Establish a national research fund and pilot program to encourage V2G pilots that test new business models and technology configurations; increase the technical exploration in travel and charging behaviour analysis and prediction, VGI-capable software development, and renewable generation prediction.
- Make stepwise relaxation for EVs to participate wholesale market.
- Position EVs as a type of distributed energy resource and design interconnection rules for EVs.
- Amend the charging standard to enable bidirectional DC charging.
- Run battery degradation tests in VGI cycles and develop battery management systems to prevent battery degradation.

中国电动汽车与电网协同的路线图与政策建议

XIX

**Table ES-2 | Barriers and Recommendations of realizing VGI in China**

|   | BARRIERS | RECOMMENDATIONS | PRIORITY  |
| --- | --- | --- | --- |
|  **MANAGED CHARGING**  |   |   |   |
|  Regulations | *TOU rates:* Many cities and provinces do not have TOU rates. Some facility owners often mandate fixed rates. | Local Development and Reform Commissions: • EV-only TOU tariff • Managed charging subsidies • Public procurement requirement on managed charging • Allow for access to the wholesale market | High  |
|  Technical aspects | *Charging standards:* • Current charging standard only support DC managed charging, not AC managed charging. • Lack of charging standard among charge points, CPO, and DSO. | Local Construction Bureau and Development and Reform Commissions: • Encourage property owners to collaborate with different aggregators to pilot managed charging | High  |
|   |   |  China Electricity Council, OEMs: • Amend GB/T27930 to support direct current (DC) managed charging • Hire third-party to certify new energy vehicles to increase EVs compliance to the existing charging standard | High  |
|   |   |  Local Construction Bureaus and Development and Reform Commissions: • Encourage the upgrade of AC chargers to DC chargers to allow for managed DC charging | Medium  |
|   |   |  Development and Reform Commissions or grid operators: • Encourage the sharing of the non-sensitive load information to enable managed charging conducted by different aggregators | Medium  |
|   |   |  Aggregators: • Encourage using cellphone APPs or connecting to national new energy vehicle monitoring platform to gather necessary vehicle information to allow for AC managed charging. | Low  |

xx

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

**Table ES-2 | Barriers and Recommendations of realizing VGI in China**

|   | BARRIERS | RECOMMENDATIONS | PRIORITY  |
| --- | --- | --- | --- |
|  **V26**  |   |   |   |
|  Regulations | *Wholesale market entry barriers:* Market access regulations and equal allocation dispatching mechanisms are designed for power plants and centralized stationary storages; distributed, behind-the-meter resources like PEVs face considerable entry barriers for electricity trading and third-party services. | National Development and Reform Commission and National Energy Administration: • Make stepwise relaxation for EVs to participate wholesale market. | Low  |
|   |  *Interconnection barriers:* EVs are not acknowledged as distributed energy, and lack interconnection rules. | National Development and Reform Commission and National Energy Administration: • Define EVs as a type of distributed energy resources • Design interconnection rules for EVs. | Low  |
|  Technical aspects | *Charging standards:* • Current charging standard doesn't support V2X. • Lack of charging standard among charge points, CPO, and DSO. | National Development and Reform Commission and National Energy Administration: • Establish a national research fund or pilot program to support V2G pilots that test new business models and technology configurations | Medium  |
|   |   | China Electricity Council • Amend the charging standard to enable bidirectional DC charging, test the supportiveness of the charging standards to frequency regulation. | Medium  |
|   |  *Battery Degradation:* V2X may accelerate battery degradation | Research Institutes and OEMs: • Run battery degradation tests in VGI cycles, optimize battery management systems | Medium  |

中国电动汽车与电网协同的路线图与政策建议

XXI

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

# 第一章

# 背景

## 1.1 电动汽车推广及无序充电对电网的影响日益突出

新能源汽车的推广对减缓气候变化、降低移动源的空气污染具有重要意义。中国作为全球新能源汽车最大的市场，增长势头强劲。截至2019年年底，中国的新能源汽车总保有量约为381万辆（公安部2020）。根据《新能源汽车产业发展规划（2021—2035年）》（征求意见稿）设定的目标，中国新能源汽车新车销量占比将从2019年的4.7%上升至2025年的25%左右（工业和信息化部等2019）。

中国未来电动汽车规模化的快速增长，将带来车用电量与用电负荷的增长，成为未来用电增长的重要助推力之一：以2050年新能源汽车保有量2.4亿辆（含乘用车和商用车）为基数进行预测，新能源汽车的年用电量将达4,922亿千瓦时，相当于2018年中国全社会用电量的7.2%。这对未来发电侧、输配电侧以及充电桩等的规划布局将产生深远影响。

电动汽车目前无序的充电的方式——即随时、随地与随机的充电，容易导致大量电动汽车在电网负荷高峰时段集中充电，进而增加电网负荷峰值，对发电、输配电的容量提出更高要求。根据世界资源研究所（2019）和国网能源研究院（2018）预测，在汽车高比例电动化和快充普及的情况下，电动汽车无序充电将导致2030年和2035年电网峰值负荷可能增加12%~13.1%。

电动汽车充电不仅会增加电网负荷，也会影响

本地配电网的安全运行。随着新能源汽车的推广，居住区、直流快充的商业楼宇的配电变压器（以下简称“配变”）将存在迫切的扩容需求。例如，根据世界资源研究所（2019）测算，在局部配电网中，私家电动汽车无序充电会显著增加配电变压器负荷峰值，特别是当车辆电动化比例达到50%时，多数住宅小区配变都面临超载风险。根据国家电网的研究（国家电网市场营销部2013），假设车辆电动化比例在2030年达到30%，配电变压器最大负荷将提升至79.6%，直流快充对商业楼宇的配变影响最大。在北京，预计未来300万辆电动汽车的充电负荷不仅将导致本地配变超载，甚至也将对主干网产生压力。城市电网的增容既面临投资成本高的问题，进而可能影响全社会电价，也受制于城市用地空间的约束。如何能既合理满足新能源汽车推广带来的电网改造投资需求，又控制这些投资对电价、电网企业的影响，成为亟待解决的问题。

## 1.2 电动汽车为可再生能源发电提供灵活调节的资源

在新能源高速发展的同时，中国已进入了可再生能源的发展“快车道”，光伏发电装机容量更是位居世界前列。截至2019年年底，我国可再生能源发电装机容量达到7.94亿千瓦，其中，波动性可再生能源——风电和光伏的装机容量分别为2.1亿千瓦和2.04亿千瓦。可再生能源发电（含水电、风电、光伏、生物质）装机容量约占全部电力装机容量的39.5%，可再生能源发电量占全部发电量的比重为27.9%（国家能源局2020）。根据国家发展和改革

中国电动汽车与电网协同的路线图与政策建议

1

委员会能源研究所预测（2017），在既定政策情景下，2030年中国可再生能源发电量占比可能会从2019年年底的27.9%上升至51%。

风电、光伏等可再生能源发电具有随机性和波动性，随着可再生能源在发电结构中的比重大幅提升，电力系统供需平衡将面临巨大挑战。这意味着发电侧对灵活电源（如天然气调峰电厂、储能设施）的需求，以及需求侧对可调节负荷资源（如供热电锅炉、建筑空调）等的需求都将不断增加。

如果不对电动汽车目前的无序充电方式加以引导，会使电力负荷特性更加复杂，加剧电网负荷的峰谷差，并对可再生能源消纳产生挑战（国网能源研究院 2018，国家发展和改革委员会能源研究所 2017）。例如，电动汽车无序充电与光伏出力在时间上的错位——电动汽车夜间充电、光伏白天出力，会影响“弃光”问题的解决。

但值得注意的是，与常规负荷不同，电动汽车既可作为灵活电源，也可作为可调节负荷，不仅可以降低其充电

对电网的负面影响，还在可再生能源高比例渗透下为电力平衡发挥积极作用。一方面，电动汽车的充电负荷具有高度灵活性，可以与供热电锅炉、建筑空调一样参与电力需求响应，扩大全社会可调节负荷的规模，增加负荷侧的灵活性。另一方面，电动汽车可借助其放电功能，作为储能设施或虚拟电厂，提供调峰、调频等辅助服务，缓解光伏和风电发电的波动性。根据国家发展和改革委员会能源研究所等（2017）的预测，截至2025年和2030年，在理想情况下，全社会的电动汽车能够提供的储能容量将分别达250GW和730GW，相当于2018年中国储能装机总规模的8倍和23倍，为未来可再生能源的大规模推广提供灵活调节的资源。

此外，电动汽车与电网的协同对全社会以及相关利益主体也有明显经济效益。电动汽车与电网协同不仅能够节省全社会与电网企业在发电侧、输配电侧扩容的投资成本，电动汽车车主与负荷集成商也能通过提供与电网协同的服务获得可观的收益，降低电动汽车的全生命周期成本，促进电动汽车的应用推广。

**电动汽车无序充电：**简称“无序充电”，指电动汽车用户随时、随地、随机进行充电，不对充电时间、充电功率等进行引导与控制。

**电动汽车有序充电：**简称“有序充电”，指在满足电动汽车充电需求的前提下，运用峰谷电价的经济措施或者智能控制措施，优化调整电动汽车充电时序与功率。

**电动汽车双向充放电（V2X）：**指在满足电动汽车充电需求的前提下，将电动汽车视作储能设施；当电网负荷成本地负荷过高时，由电动汽车向电网负荷成本地负荷增电；当电网负荷成本地负荷过低时，可通过有序充电，调整本地负荷的峰谷差。

2

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

TESLA

Stato

14:08

AUTONOMIA 51 MI

97%

![img-7.jpeg](img-7.jpeg)

AGGIORNATO 13:08

## 第二章

# 电动汽车与电网协同的定义和类型

### 2.1 电动汽车的可调度性

电动汽车除满足出行的刚需外，在充放电容量和充放电时间上，具备相当的调节空间。

**可调度的充放电容量：**在不影响电池衰减的条件下，私家车可提供的储能潜力不可忽视。以搭载45kWh电量的纯电动私家车为例，如果仅作出行使用（假设一天一充，日行驶里程50km），该私家车日充电量为6.7kWh。相对而言，如果私家车发挥储能作用，除满足上述出行需求外，其可提供的日放电

量更高（假设放电深度设定为不低于30%SOC），达到23kWh。若搭载的电量更高（如60kWh），则提供的放电量更大（见表1）。这说明，就目前电动汽车的电量水平而言，除了满足出行刚需外，已具备“富余”容量并可作为储能设施参与电网协同，未来随着续航里程增加，电动汽车可调度的充放电容量将更高。

**可调度的时间：**私家车的充电时长远小于其停车时长，这部分停车时间可视为可调度时间。根据北京私家车出行和充电行为统计（世界资源研究所

表1 | 电动汽车作为储能设施与作为出行工具所提供调节电量比较

|  电池容量 (kWh) | 私家车作为出行工具 |   | 私家车作为储能设施  |   |
| --- | --- | --- | --- | --- |
|   |  日充电量 (kWh) | 电池容量占比 | 日放电量 (kWh) | 电池容量占比  |
|  45 | 6.7 | 15% | 23.0 | 55%  |
|  60 | 6.7 | 11% | 32.4 | 59%  |

说明：假设私家车百公里电耗13kWh，充电损失90%，放电损失90%，最低放电深度为30%SOC。

中国电动汽车与电网协同的路线图与政策建议

5

图 1 | 北京私家车日平均停车、行驶和充电时间分布（24小时时间占比）

![img-8.jpeg](img-8.jpeg)

来源：新能源汽车国家监测与管理中心 2018 年统计数据

2019），纯电动汽车日出行时间平均为1.5小时，94%时间处于停车状态（见图1）。全天22.4小时的停车时间中，约3.4小时为接入电网的充电时间，剩余19个小时为“闲置”的停车时间，这部分时间可视为可调度时间。

从一天不同时段看，私家车的充电时长远小于其停车时长。例如，北京私家电动汽车在夜间18:00以后充电时长通常需要3.5小时，远小于夜间平均11小时的停车时间。在日间（上午9:00至下午16:00），私家电动汽车充电时长大约为1.5小时，小于日间平均停车时长5小时（见图2）。

此外，从接入电网的车辆数量看，一天中不同时段接入电网的电动汽车数量也较少，仅占静止停放的电动汽车数量的3%至10%（见图3）。这意味着，无论日间还是夜间，电动私家车在时间和数量上均具有灵活性；如果充电桩设施充足，私家车在日间、夜间均有条件参与电网协同。

图 2 | 北京电动私家车一天不同时段里平均停车时长、充电时长对比

![img-9.jpeg](img-9.jpeg)

说明：某个时刻的停车时长代表示电动私家车在该时刻开始停车所需的停车时长。某个时刻的充电时长表示私家车在该时刻开始充电所需的充电时长。

来源：新能源汽车国家监测与管理中心 2018 年统计数据

图 3 | 北京电动私家车一天不同时段里停车数量、充电数量占电动汽车总量的比例

![img-10.jpeg](img-10.jpeg)

来源：新能源汽车国家监测与管理中心 2018 年统计数据

6

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

## 2.2 电动汽车与电网协同的方式

利用电动汽车的负荷灵活特性与储能功能，可以实现第1.2节中所述的功能。广义上，实现电动汽车与电网协同（以下或简称“车网协同”）的方式包括：电动汽车有序充电、电动汽车双向充放电（见表2），以及利用退役电池或电动汽车换电站做储能电站。

**电动汽车有序充电（Smart Charging, V1G）：**电动汽车有序充电是指在满足电动汽车充电和出行需求的前提下，运用经济措施或者智能控制方式，调节电动汽车充电时序与功率。电动汽车有序充电可借助三种方式实现：

- ■ 一是基于峰谷电价的有序充电，即通过电价信号，激励电动汽车用户自发响应调整充电时间，实现“削峰填谷”的效果。例如，目前一些充电APP可根据用户设定的出行时间和本地目录电价，优先让车辆在电价低谷时段充电，或由用户设定车辆开始充电的时间。
- ■ 二是基于智能管理的有序充电，即结合配网变压器的负荷状态与开放容量以及用户的出行需求，对电动汽车的充电时间、充电功率进行计划控制或实时控制。
- ■ 三是前两者的结合，即通过峰谷电价方式，鼓励电动汽车车主参与基于智能管理的有序充电。

**电动汽车双向充放电（Vehicle-to-X, V2X）：**在满足电动汽车充电和出行需求的前提下，将电动汽车视作储能设施，当电网负荷过高时，由电动汽车向电网馈电，当电

网负荷过低时，用电动汽车存储过剩的发电量。根据电动汽车馈电的范围不同，双向充放电进而可划分为电动汽车对本地负荷馈电和向电网馈电（其他V2X的分类方式见专栏一）：

- ■ 电动汽车对本地负荷馈电（Vehicle-to-Building, V2B, Vehicle-to-Facility, V2F, 或Vehicle-to-Home, V2H）：即电动汽车作为分布式电源，发挥“自发自用”的作用，抵消本地用电设施产生的负荷，如办公负荷、商业楼宇负荷。电动汽车对本地负荷馈电可以发挥的作用包括：一是降低本地负荷，局部削峰填谷或作为备用电源；二是提供需求响应服务或调峰辅助服务。
- ■ 电动汽车向电网馈电（Vehicle-to-Grid, V2G）：即电动汽车作为分布式电源接入配电网并返送电，不仅降低本地负荷，缓解变压器或配变线路增容压力，而且作为“虚拟电厂”与就近电力用户交易，或参与电力市场交易，提供现货电力平衡、调频、调峰等服务。与前者的主要区别在于：电动汽车馈电并网需要有关部门进行测试、审核并提供准入许可。目前在中国，多数分布式电源（包括电动汽车）在并网管理方面仍面临阻碍。

较之电动汽车有序充电，电动汽车双向充放电在激励机制上有显著差异：除峰谷电价外，电动汽车双向充放电还可以通过参与现货市场、辅助服务市场和需求响应市场，获得相应收益。同时，双向充放电一般需要智能控制，特别对电动汽车作为分布式发电系统并网馈电的情况，更需要严格的申请与调试过程，避免造成本地变压器反向超载、电压变化等问题。

表 2 | 基于实现机制的电动汽车与电网协同方式分类

✓ 存在车网协同的实现机制

|   | 经济激励机制 | 智能控制 | 经济激励机制与 智能控制结合  |
| --- | --- | --- | --- |
|  电动汽车有序充电 | ✓ ·目录电价 | ✓ | ✓ ·目录电价 ·需求响应市场收益 ·辅助服务市场收益 ·现货市场价格信号  |
|  电动汽车双向充放电： 对本地负荷馈电（V2B） | ✓ ·目录电价 | ✓ | ✓ ·目录电价  |
|  电动汽车双向充放电： 向电网馈电（V2G） |  |  | ✓ ·需求响应市场收益 ·辅助服务市场收益 ·现货市场价格信号  |

中国电动汽车与电网协同的路线图与政策建议

7

利用退役电池或**电动汽车换电站作储能电站**：采用换电模式的电动汽车需要集中式的换电站，而该换电站作为固定储能设施，可以兼顾电网调节需求，使储能设施的经济价值最大化。与之类似，电动汽车退役电池也能通过梯次利用方式作为固定储能设施。利用退役电池或电动汽车换电站作储能电站的方式在运营管理上，与目前固定式储能设施的管理方式一致；不仅不受电动汽车出行的约束，而且政策阻碍不大、技术成熟。因此，这两种协同方式不在后文讨论范畴。电动汽车与电网协同的范围界定如图4所示。

图 4 | 电动汽车与电网协同的范围界定

![img-11.jpeg](img-11.jpeg)

# 专栏 1 | 双向充放电——直流充放电的V2X和交流充放电的V2X

根据电动汽车与充电桩之间电能量交换方式不同，电动汽车双向充放电还可分为直流充放电的V2X和交流充放电的V2X。常规的电动汽车充电分成直流充电和交流充电两种方式，二者在电压、充电桩功能规范和车桩间通信协议方面均具有较大的差异，电动汽车V2X因此继承了这些差异。

- 直流充放电的V2X：电动汽车和充电桩之间的电流交换为直流，通常功率较高，充电速度较快。直流充电在公共充电桩中较常见，为支持V2X，需要在桩侧安装功率变换模块（即交直流转换单元）。
- 交流充放电的V2X：电动汽车与充电桩之间的电流交换为交流，通常功率较低，充电速度较慢。住宅小区的私人充电桩中，交流充电较为普遍，为支持V2X，需要在车侧安装功率变换模块。

8

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

## 2.3 电动汽车与电网协同的应用场景

电动汽车与电网协同措施能够在不同应用场景发挥作用（见图5）：

- 用户侧：在峰谷电价或两部制电价政策的地区，通过电动汽车有序充电或V2B，可帮助用户节省电费支出，削减需量电费支出，实现峰谷差套利。此外，电动汽车也能提供需求响应、备用电源，以及支持分布式可再生能源的消纳等功能。
- 输配电侧：在配电侧，通过电动汽车有序充电或V2B，可实现局部配电网负荷的削峰填谷，抵消配电网增容压力；在输电侧，可缓解输电线阻塞，降低输电网投资改造成本。
- 电源侧：电动汽车可以作为分布式电源，或与其他电源、可控负荷等联合调控形成“虚拟电厂”，提供如调峰、调频、备用等辅助服务，实现电网系统负荷的削峰填谷与电力实时平衡，延缓对新建电厂或灵活资源的投资，促进可再生能源消纳。

# 用户侧

在用户侧，电动汽车除出行之外，也能提供包括削峰填谷、需求响应、备用电源、支持分布式可再生能源的消纳等功能：

- 削峰填谷：利用峰谷电价或两部制电价，电动汽车与电网协同可以为电力用户——如工业园区、办公楼和个人用户，提供明显的经济效益，并延缓本地配电系统增容的需要。对执行居民、工商业或大工业峰谷电价的场景，电动汽车用户可通过有序充电在谷时充电，或峰时放电进行自发自用，节省电费支出，实现电价的“峰谷差套利”。对执行两部制电价的场景——如工业园区，电动汽车可以通过在负荷峰时放电，削减需量电费支出，缓解配变增容需要。
- 需求响应：除了为电力用户减少电费支出外，电动汽车可以作为可控负荷，协助电力平衡。依靠新建调峰火电机组或者增加输配电线路投资，满足短暂的尖峰负荷需求，投资成本高，而从负荷侧入手，利用灵活负荷资源，可以较为经济地实

图 5 | 车网协同的不同应用场景：用户侧、输配电侧与电源侧效益

![img-12.jpeg](img-12.jpeg)

来源：根据落基山研究所 2017 年研究修改

中国电动汽车与电网协同的路线图与政策建议

9

现电力平衡（原则上，需求响应覆盖负荷侧和电源侧资源，本节仅从负荷侧进行说明）。随着近几年可再生能源的普及和传统火电机组灵活性改造存在瓶颈，我国对需求响应的定位也在从传统“削峰”（缓解电网的尖峰负荷）向“填谷”（促进可再生能源消纳）转变。需求响应的市场潜力也将不断扩大；目前，部分地区（如江苏）的需求响应可占3%左右的最大用电负荷（国家发展和改革委员会 2017）；未来，随着用户侧储能等技术的普及，需求响应有望减少10%以上的最大用电负荷（国际能源署 2019）。

传统参与需求响应的灵活/可中断负荷包括工业生产以及大型机构商业写字楼的空调和供热系统。由于具有负荷灵活的特点，电动汽车逐渐成为需求响应的重要组成。首先，电动汽车既能在可再生能源出力峰时、系统负荷谷时，通过有序充电实现“填谷”，也可以在系统负荷峰时不充电或者放电，实现“削峰”。此外，对比传统需求侧灵活资源，电动汽车的可调节容量大——在车辆大规模推广下，电动汽车负荷可占电网最大用电负荷的10%左右（世界资源研究所 2019）。此外，电动汽车夜间停车充电时间也是风电出力高的时刻，是消纳风电的理想选择。事实上，电动汽车作为灵活负荷资源，已参与了国内部分地区的需求响应试点。例如，国网电动汽车服务有限公司在天津组织电动汽车（包括公交车、城市快充站）通过竞价方式参与春节时间的“填谷”电力需求响应（国网电动汽车服务有限公司 2019）。

## 输配电侧

在输电侧，一方面，电动汽车作为分布式“虚拟电厂”，降低负荷中心对跨区域输电线路的依赖；另一方面，电动汽车可以在本地用电高峰、区域输电线路阻塞时放电，缓解输电线路阻塞的压力，从而降低输电线路的额外投资。

然而，在中国，电动汽车在缓解跨区域输电线路阻塞方面所能起到的作用，仍无法与大规模跨地区输电基础设施或本地电源投入相提并论。特别是为缓解中国中西部等可再生能源重点开发地区的“弃风弃光”问题，仍有必要在近期加强跨省、跨区输电通道建设，这其中电动汽车作为储能设施能发挥的作用相对有限。

较之输电网，电动汽车的车网协同对配电网的意义更大。配电网受电动汽车无序充电的影响大，而较之高昂的

配电网增容投入，有序充电提供了更经济的解决方式。根据国家电网测算（中国汽车报 2019），按照2030年北京120万辆电动乘用车的规模测算，在无序充电下，需要97亿元配电网增容投资，但为实现有序充电而进行配电网的智能改造投资只需22亿元，节约77%。

## 电源侧

提升电力系统灵活性是实现未来高渗透率可再生能源电力系统的必然选择。为实现《能源生产和消费革命战略（2016—2030）》设定的2030年非化石能源发电占比50%的目标（国家发展和改革委员会、国家能源局 2016），可再生能源电力在中国发电结构中的比重还需大幅提升。然而，风电、光伏等可再生能源发电的随机性和波动性为电力系统供需平衡带来巨大挑战，调频、调峰、爬坡的市场需求也会不断增加。

通过聚合、优化控制与管理大量电动汽车，可以形成规模化运行的“虚拟电厂”，为电网提供灵活调频、调峰、爬坡等辅助服务，并参与电力市场交易。

- ■ **调频：**调频是保障电力系统频率变动保持在允许偏差范围内（$50 \pm 0.2\text{Hz}$）的重要电力辅助服务手段。虽然目前调频市场空间仅为电网峰值负荷的1%~2%，但未来随着波动性可再生能源接入规模的提升，电网调频需求将持续增长。

以往调频服务一般由发电机组提供，且对机组调节速度、调节精度、响应时间等有较高要求，一般一次调频主动持续一小段时间（秒级），待由自动发电控制（AGC）提供二次调频（分钟级）。参与调频的传统燃煤和天然气发电机组需要频繁调节机组发电出力，因此会影响机组气门、锅炉等系统部件寿命，且参与调频的成本也更高。电化学储能系统由于响应速度快，可以实现精细化控制，与传统火电资源相比，更适于调频服务，其未来市场前景可期（专栏二）。

同时，调频对参与的电化学储能设施也有较高要求，退役电池系统较少应用于调频，而电动汽车参与调频的可靠性也有待验证。此外，调频主要以发电侧、电网侧储能为主，用户侧储能资源（如电动汽车）参与调频服务仍有市场准入门槛，且未来参与调频市场还需克服资源分散、控制不易、容量预测不准确等问题。未来，随着电化学储能在调频中的普遍应用，电动汽车参与调频的市场份额会视电动汽车的出行刚需、电池衰减情况，以及调频市场开放程度而定。

10

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

- **调峰：**调峰是我国辅助服务市场中特有的——国际电力市场中，调峰是通过现货市场的分时电价引导发电出力的调整。目前，中国调峰辅助市场主要是为了应对负荷高峰以及辅助可再生能源消纳（即在可再生能源发电功率较高时降低火电机组的出力）；未来，随着可再生能源成为电源结构的主要组成，也需要火电机组或其他电源在可再生能源发电下降的时段，快速爬坡出力（即国外电力市场中的“爬坡”辅助服务）。

调峰的市场主体包括火电机组、抽水蓄能、可中断负荷和电储能设施等。目前，调峰以火电机组和抽水蓄能为主，不仅调峰能力较强，且成本相对更低。但火电机组参与调峰的主要阻碍在于深度调峰能力（即最小技术出力占额定容量比例高）的限制（见表3），且参与调峰对燃料消耗和机组寿命都有一定影响。因此，存量火电机组面临包括深度调峰和热电解耦技术在内的大规模灵活性改造需求。

相较之下，储能设施在其灵活性改造上可发挥一定作用。目前，随着可再生能源消纳的压力提升以及火电机组调节深度的局限增大，储能设施与电动汽车也正在作为负荷侧灵活资源，以有序充电方式参与中国的调峰市场（国家能源局华

北监管局 2019）。但电动汽车以放电方式参与调峰市场仍有先天缺陷：特别是调峰对持续时长有较高要求——持续4小时以上，电化学储能系统参与调峰容易耗尽电池电量，影响动力电池寿命。未来，随着电池成本下降、电池能量密度上升，电化学储能系统（包括电动汽车）放电参与调峰的可行性会得到一定改善。

- **爬坡：**爬坡是美国辅助服务市场产品之一，用于解决集中式光伏并网中，在光伏出力下降的傍晚时间，火电机组响应时间长、爬坡速度有限的问题。灵活爬坡产品和传统的辅助服务产品不同，其需求不是根据电力系统某一个时刻的状态而定，而是依据两个时间点的变化而定。例如，2016年，CAISO在其15分钟和5分钟的实时市场引入“灵活爬坡产品”（Flexible Ramping Product, FRP），辅助发电资源在傍晚时间快速爬坡出力。

这种对持续时间要求较短但对功率变化率要求较高的辅助服务，适合电动汽车的特性。虽然目前中国辅助服务市场中尚无爬坡产品，但随着可再生能源比例提升，爬坡辅助服务的需求可能会不断上升，而电动汽车将在其中扮演一定角色。

表 3 | 火电厂与电动汽车提供调频、调峰和爬坡服务的性能对比

|   | 功率容量 | 爬坡速度 | 调节深度 | 日后停 | 边际成本  |
| --- | --- | --- | --- | --- | --- |
|  纯凝燃煤发电 | GW | 1小时 | 40% ~ 100% | √ | 中  |
|  燃煤热电联产 | GW | 1小时 | 60% ~ 100% | - | 中  |
|  单循环燃气发电 | 0.5GW | 3分钟 | 0% ~ 100% | √ | 低  |
|  联合循环燃气发电 | 0.5GW | 小时 | 15% ~ 100% | √ | 低  |
|  电化学储能 | kW-GW | 毫秒 | 0% ~ 100% | √ | 低-高  |

来源：国家发展和改革委员会能源研究所调研

中国电动汽车与电网协同的路线图与政策建议

11

## 专栏 2 | 电动汽车与常规储能系统的比较

与电动汽车类似，常规储能系统（包括抽水蓄能、储热系统以及固定电化学储能设施）也能够提供上述的调频调峰辅助服务，只是不同储能方式在适用范围上有所差异（见专栏表1）。

- 抽水蓄能、储热系统：参与调频的响应速度有限，但可发挥集中储能电能量大的特点，在跨区域电网中发挥调峰作用。
- 电化学储能设施：固定储能电池作为典型的电化学储能设施，具有快速功率输出和精准跟踪的能力。对比传统火电机组和抽水蓄能系统，更适用于电力调频或可再生能源爬坡、平滑波动的场景。运行中需要考虑电池系统可靠性、使用成本、使用寿命和防火等问题。
- 电动汽车：一方面电动汽车继承了电化学储能的特性，因而应用场景与其高度重合，但由于电动汽车节省了采购成本，即便考虑充电桩等设备投入，其全生命周期成本仍比固定储能低。另一方面，电动汽车较之固定储能，也存在数量多、分散、控制不易、容量难以预测的问题，参与精度较高的应用场景（如调频、爬坡等辅助服务）的精确性有待验证。
- 退役电池：与常规储能系统相比，目前退役后梯次利用的动力电池做集中式储能仍存在一些问题，包括能量不足、性能不稳定等。

中国目前储能装机容量有限，储能设施以抽水蓄能系统为主。截至2018年，已建成的储能装机容量仅占全国发电装机总量的约1.5%，其中抽水蓄能系统的装机规模占比储能总装机规模的96%，电化学储能装机规模仅占3%（中国电力企业联合会 2019）。未来随着可再生能源的大量接入，对储能等灵活资源的需求将不断扩大，而电动汽车作为低成本的储能设施，能够在特定领域如调频、可再生能源爬坡和平滑波动发挥积极作用。

专栏表 1 | 常规储能系统与电动汽车对比

|   | 2018年装机规模 (GW) | 类别 | 储能周期 | 转换效率 | 使用年限 | 综合成本 (元/kWh) | 成熟度 | 适用场景  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  抽水蓄能 | 29.99 | 抽水蓄能系统 | 数小时至数月 | 75% ~ 80% | 40 ~ 60年 | 40 ~ 800 | 成熟 | 调峰  |
|  储热技术 | 0.21 | 熔盐储能系统 | 数小时至数月 | 90%以上 | <20年 | 240 ~ 800 | 示范与应用  |   |
|  电化学储能 | 1.07 | 退役电池 | <4小时 | 90%以上 | <5年 | 300 ~ 800 | 示范与应用 | 未知  |
|   |   |  固定式储能电池 | 4小时 | 90%以上 | <15年 | 1200 ~ 2000 | 示范与应用 | 调峰、爬坡、结束响应  |
|   |   |  电动汽车 | 视出行需求 | 90%以上 | 6 ~ 9年 | 购置成本可不计，运维成本待估 | 示范  |   |

来源：中国电力企业联合会 2019，中关村储能产业技术联盟 2019

12

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

B

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

2

### 第三章

# 国内外电动汽车与电网协同相关实践

## 3.1 国际电动汽车与电网协同试点概览

全球电动汽车和电网协同的实践从2008年开展至今已有十余年，与电动汽车普及的时间基本相同。截至2018年年底，全球有约50个电动汽车与电网协同案例（见图6），其中25个在欧洲，18个在美国，7个在日本和韩国（Everoze等2018）。

国际上开展车网协同试点的目标可总结为：一是

利用提供电网服务的收益，降低电动汽车全生命周期的成本，提升电动汽车推广的规模数量；二是在保障电网系统安全、稳定运行的前提下，利用电动汽车作为电网资源，减少电网、电源和固定式储能设施的投资（见图7）。

虽然电动汽车与电网协同仍为新鲜事物，但从国际案例看，电动汽车与电网协同覆盖了几乎所有可能的应用场景，从局部配网优化到全网应用（Everoze等2018）（见表4）。

图 6 | 全球V2G项目分布

![img-13.jpeg](img-13.jpeg)

中国电动汽车与电网协同的路线图与政策建议

15

图 7 | 电动汽车与电网协同的目标

![img-14.jpeg](img-14.jpeg)

表 4 | 国际车网协同主要的应用场景与协同方式

|   | 应用场景 | 协同方式 | 试点国家  |
| --- | --- | --- | --- |
|  全网侧应用 | **现货市场电力平衡：**测试电动汽车参与现货市场的可行性 | V2G，有序充电 | 荷兰、丹麦  |
|   |  **需求响应：**测试电动汽车参与需求响应的响应程度以及经济可行性 | V2B，有序充电 | 多数国家  |
|   |  **调频：**验证电动汽车提供高频次、高精度调频响应的可行性 | V2G，有序充电 | 多数国家  |
|   |  **旋转备用服务：**测试电动汽车提供备用发电服务的可行性——在系统出力低时放电，系统出力高时充电  |   |   |
|   |  **缓解输电线路阻塞：**测试电动汽车在输电阻塞发生时储存电网电力，在需求高峰时向电网放电的效果 |   | 德国  |
|  配网侧应用 | **削峰填谷、延缓变压增容投资：**引导电动汽车实现局部负荷的削峰填谷，减少配电网增容投资需求，同时节约充电费用 | V2B，有序充电 | 多数国家  |
|   |  **分布式光伏充电：**利用分布式光伏技术为电动汽车充电（“光+充”或“光储充”），节约充电费用，并辅助分布式光伏消纳 | V2B，有序充电 | 多数国家  |
|   |  **备用电源：**测试在断电等紧急情况下，利用电动汽车作为备用电源的可行性 | V2B | 日本  |

来源：根据 Evenze 等 2018 总结

16

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

这些V2X试点具有如下特点（见表5）：

- ■ 涵盖应用场景多、测试内容广：一个V2X试点通常开展针对多个应用场景的测试，如丹麦Pakrer项目既参与调频辅助服务市场，也提供现货市场电力平衡。而在验证内容上，包含了电池衰减测试、车-桩-网通信和技术标准、经济可行性等内容。值得注意的是，除技术可行性外，经济可行性是V2X试点项目重要的测试内容：国际车网协同试点中，41%的试点项目兼顾了对技术、经济可行性的论证（Everoze等 2018）。例如，为分析区域间市场准入制度及收益水平的差异，Parker项目分别在多个区域电力市场开展（Brendlinger 2017）。最后，测试车型也较多元，除纯电动私家车外，更包括轻型货车、公交车、校车、分时租赁车等。
- ■ 参与V2G的主体数量多、类型多元：国际的V2G试点通常不是由一家企业发起，而是电网企业、汽车生产企业、负荷集成商、研究机构等共同发起，从而建立汽车生产企业、充电桩企业、负荷集成商、输配电网企业协同合作的生态圈，促进车-桩-网各主体在技术研发上的协同，以便快速降低前期投资成本。

未来，国际电动汽车与电网协同的发展趋势可总结为以下几个方面：

- ■ 调频服务的试点在数量、经济与技术可行性的成熟度上占据优势。从电动汽车参与全网实践的数量上看，全网的V2G试点数量占绝对优势，但关于延缓配网扩容、提高配网电能质量的试点数量有限。这主要是由于欧美辅助服务市场准入门槛低、市场化水平高，而调频服务不仅适宜电动汽车参与，也能够提供丰厚的回报。例如，根据美国、德国等不同国家电力市场的价格水平测算，一辆电动汽车以V2G方式提供调频服务获得的收益水平为500～2000美元/年，高于需求响应100美元/年的收益（不计成本）（刘坚等 2018）。相较之下，延缓配网扩容的应用场景仍缺乏清晰的商业模式，因此试点项目有限。由于调频试点项目启动早——美国最早展开的车网协同试点均是电动汽车参与辅助服务市场，因而其在技术上（如充电标准）也更成熟（California ISO等 2014）；在欧洲，由于技术成熟，电动汽车参与V2G调频的规模已经从10辆车（丹麦Parker试点项目）向300辆车（英国V2GO项目）迭代。

表5 | 国际知名电动汽车与电网协同试点项目概览

|   | 应用场景 | 协同方式 | 车辆类型 | 发起方  |
| --- | --- | --- | --- | --- |
|  丹麦Parker项目 | 调频、 现货电力平衡 | V2G（直流） | 私家车 | 丹麦科技大学、NUVVE、 日产、三菱、ENEL等  |
|  美国空军基地试点 （多州） | 调频、 需求响应 | V2G（直流） | 乘用车、轻型货车 | 美国国防部、美国东部和西 部各个电力市场调度中心  |
|  美国电动校车试点 （多州） | 调频 | V2G（交流） | 校车 | PIM市场等  |
|  夏威夷Jumpsmart Maui试点 | 需求响应（削峰）、 延缓本地配网增容 | V2H（直流） | 私家车 | 夏威夷州政府、Maui电力公 司、Hitachi公司、夏威夷大 学等  |
|  德国REDISPATCHING 试点 | 缓解输电线路阻塞 | V2G（直流）/有序 充电 | 电网公司运营车辆 | TenneT、Mobility House、日产 汽车  |
|  法国Grid Motion试点 | 调频、 现货电力平衡、 削峰填谷 | V2G（直流）/有序 充电 | 私家车、分时租赁 车辆 | PSA、Enel、Nuvve、DTU等  |

来源：根据 Everoze 等 2018、Brendlinger 等 2017

中国电动汽车与电网协同的路线图与政策建议

17

■ 车-桩-网高频次、高时间精度的通信协议得到验证，直流充电V2G相关的试点数量更多（见专栏一和图8）。由于目前国际V2G试点参与调频服务居多，而调频服务对车-桩-网间通信要求最高，因而验证车-桩-网之间高频次、高时间精度的通信协议是国际上V2G试点的重点之一。经过测试，美国CCS和日本CHAdeMO充电协议都可以支持电动汽车对电网高频、双向的信息传递，特别是CCS充电标准对直流、交流充电都提供支持

（Everoze等 2018）。由于交流的双向充电电需要对车辆侧进行改造——加装逆变器，因此国际上基于直流充电的V2G试点在数量上更占优势。

■ 车网协同与可再生能源消纳结合更为紧密。通过有序充电和V2X，电动汽车能够辅助风能、太阳能等波动性可再生能源的消纳。由于可再生能源发电的波动性与不确定性，电力系统对调频、备用、爬坡服务以及缓解输电线路阻塞的需求会增加。越来越多的车网协同项目已经开始将

图 8 | 国际车网协同试点采用直流充电、交流充电与二者兼顾的数量占比

![img-15.jpeg](img-15.jpeg)

来源：Everoze 等 2018

表 6 | 国际车网协同试点常见阻碍

|   | 常见阻碍 | 解决措施  |
| --- | --- | --- |
|  私家车出行的随机性与用户接受度 | 出行行为差异大，难以预测电动汽车在现货市场或辅助服务市场提供的电能及容量 | 负荷集成商：从私家车之外的营运车辆着手  |
|   |   |  负荷集成商：利用软件建模分析用户出行、充电规律（或事前获得出行行程）  |
|   |  私家车用户参与度有限 | 负荷集成商：从私家车之外的营运车辆着手  |
|   |   |  通过经济激励、一对一的市场宣传，提高参与度  |
|  政策与市场机制 | 用户侧资源接入配电网的阻碍（用户侧资源分散、难以管理） | 允许用户侧资源并网，但需要经过严格、漫长（加利福尼亚州需要接近一年）的项目核准、并网验收和调试过程  |
|  技术与标准 | 车：主流电动汽车品牌不支持V2X | 日产、三菱已经开始支持商业化的V2G产品。日产对每天放电在5kWh内的电动汽车提供质保  |
|   |  充电通信协议：不支持有序充电和V2X | 经过测试，CCS 与 CHAdeMo 2.0 协议可有效支持有序充电和V2X  |
|   |  网：配网设备需要改造 | 针对电动汽车提供服务的不同，对计量等设备进行改造  |
|   |  电池：V2X 可能加速动力电池衰减 | 开展相关动力电池衰减测试，利用电池管理系统进行智能管理  |

来源：根据 Everoze 等 2018 总结。

18

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

辅助可再生能源消纳作为应用领域。例如，德国REDISPATCHING试点将电网企业运营的车辆作为储能设施，缓解输电阻塞问题。此外，一些新的车网协同试点也加入对气象及可再生能源出力的预测机制，使电动汽车能够更主动地支持可再生能源的消纳（太平洋煤电公司PG&E 2018）。

- ■ 电动汽车参与多种应用场景（Value Stacking）越发受到重视。随着调频不断成熟，商业化水平得到验证，一些国际上的V2G实践已经不满足于单一的应用场景，而是集成调频、需求响应，进一步增加车网协同的商业价值。在不久的将来，V2G也有望成为“出行即服务”（Maas）的一部分。

虽然欧美等国在电动汽车与电网协同试点上取得明显进展，但其试点过程中也不乏政策制度、技术标准的阻碍。表6总结了常见的阻碍。

## 3.2 加利福尼亚州电动汽车与电网协同路线图

美国加利福尼亚州既不是电动汽车与电网协同试点最早的地区，也不是参与本地电力市场门槛最低、收益最高的地区（Xu等2016）。但2014年，由加利福尼亚州电力调度中心（CAISO）牵头，加利福尼亚州州长办公室、州能源委员会、州公共事业委员、州空气资源委员会参与编制的《加利福尼亚州电动汽车与电网协同路线图——电动汽车作为电网资源》（以下简称“加利福尼亚州路线图”）（加利福尼亚州电力调度中心等2014），使加利福尼亚州成为美国第一个为车网协同奠定制度基础的州。这使得加利福尼亚州车网协同项目区别其他众多由企业、大学等团体单方面发起的试点项目。

加利福尼亚州路线图的主要初衷是为可再生能源并网提供更多灵活资源。作为美国第二个提出实现高比重清洁能源的州，加利福尼亚州视电动汽车为储能系统，可协助缓解灵活资源的投入。根据《加利福尼亚州可再生能源组合标准方案：温室气体减排》（SB100），在现有配额制机制下，致力于2030年实现可再生能源发电占比60%的目标，并在2045年实现100%可再生能源与其他零碳电源发电的目标。由于可再生能源发电波动性强，实现这一目标也意味着灵活电源和负荷侧资源的投资。对比高昂的灵活资源投入，用户侧的电动汽车既有需求响应功能，也可作为分布式电源，且比传统灵活资源的成本更低、更灵活高效，如果作为灵活电源参与辅助服务、现货市场，也能获得相当回报。

值得注意的是，加利福尼亚州路线图的宗旨在于实现“多赢”。虽然电动汽车的有序充电和V2X对用户电费支出有明显效益，但通过车网协同减少工商业企业的容量电价，或者利用峰谷差电价减少居民的电费支出，并不是加利福尼亚州电力系统支持车网协同的初衷。加利福尼亚州路线图其致力于解决以下问题（加利福尼亚州电力调度中心等2014）：

- ■ **商业模式：**车网协同目前不是在所有应用场景下都具有商业模式，例如在本地配网提供的电压支持，其经济性有限。车网协同的经济价值也会随着时间推移和可再生能源渗透率提高而发生变化。推广车网协同，应识别不同时期下具备商业模式、可实现“多赢”的应用场景。
- ■ **政策支持：**电动汽车参与电力市场面临众多法律层面的“空白”。例如，加利福尼亚州尚未就电动汽车归属储能设施、负荷侧资源，还是发电设施达成共识，因而加利福尼亚州路线图明确未来的能源立法中，应单独说明是否允许电动汽车参与。此外，对于电动汽车并网的阻碍，加利福尼亚州路线图明确了电动汽车的“并网”许可、计量与结算方式。虽然此前，加利福尼亚州从没有表后资源并网参与电力市场的先例，但在加利福尼亚州路线图制定中达成共识（加利福尼亚州公用事业委员会2019），即：
  - □ 对电动汽车接入电网馈电（V2G）的相关接入许可与接入流程，依据美国联邦能源管理委员会（FERC）并网要求《批发市场开放接入价格》（Wholesale Open Access Distribution Tariff-WDAT）执行。由于电动汽车属于新的用户侧资源，所以并网前需要由本地配电网企业与电网调度机构对申请参与电力市场交易的车辆、充电桩逐一进行安全性、稳定性测试，并对试点项目所参与电网的服务进行可靠性测试，只有对达到标准的试点项目才提供并网许可。该流程需要大致一年的时间。
  - □ 对电动汽车对本地负荷馈电（V2B/V2F）的情况，接入前需评估电动汽车放电对本地电压稳定性、三相平衡、配电网谐振等电能质量指标，以及孤岛效应等安全性指标的影响。另行，依据加利福尼亚州公用事业委员会（CPUC）的“Rule 21并网规范”执行，电动汽车车主或负荷集成商向加利福尼亚州公用事业委员会与本地配电网企业提出申请，经过安全性、稳定性测试后才允许接入。

中国电动汽车与电网协同的路线图与政策建议

19

■ **技术及标准：**目前车辆、充电桩技术并不支持电动汽车双向充放电，而高昂的设备（或车辆）改造与研发投入成本影响了V2X的经济性。为降低V2X的成本，仍有待技术创新与市场发挥规模效应。此外，有关V2X的技术标准，如车—桩—网通信协议、车载充放电机的标准等也需统一。最后，加利福尼亚州路线图也特别关注加强研发支持和深化试点内容，为此，加利福尼亚州能源委员会已提供了2530万美元的资金，支持车网协同相关研究与试点的开展。

### 3.3 中国电动汽车与电网协同实践案例

根据本研究不完全统计，中国目前有超过10个车网协同试点（见表7），包括国网电动汽车服务有限公司北京人济大厦的V2B试点、特来电在青岛特锐德工业园进行的光储充项目试点、国网北京公司在北京西八里社区开展的有序充电试点等（见专栏三）。

与国际车网协同试点项目对比，国内的车网协同项目具有如下特点：

第一，中国的车网协同项目数量较少，应用相对单一。与国际实践从初期电动汽车就参与高频次、高精度的批发市场交易不同，当前中国的试点项目侧重于通过有序充电，解决配网侧开放容量不足的问题，除广东省外，尚未出现任何旨在参与现货市场或辅助市场的试点。国内外试点项目在应用场景上的差异，主要源于中外电力市场的差异（见5.1节分析）。对比欧美电力市场，中国电力市场仍在改革进程中，市场化水平有待提高；用户侧储能资源参与电力市场仍为新鲜事物，需要建立相应的准入机制。

第二，绝大多数试点仍处于技术可行性论证阶段。对用户（电动汽车车主或电力用户）的激励机制缺失，商业可行性也未在考虑之列。

第三，与国际V2G项目由多方发起、力图建立产业生态圈不同，中国目前的电动汽车与电网协同试点发起方以电网企业为主。随着未来电力市场的建立、经济激励机制的形成，更多市场主体将可能加入车网协同的探索中。

表7 | 国内典型电动汽车与电网协同试点项目概览

|  试点地点 | 试点内容 | 用户侧激励方式 | 发起方  |
| --- | --- | --- | --- |
|  郑州龙源世纪家园小区 | 有序充电延缓配网扩容 | 无 | 国家电网公司  |
|  北京西八里社区 | 有序充电延缓配网扩容 | 无 | 国家电网公司  |
|  南京北苑之星小区 | 有序充电延缓配网扩容 | 无 | 国家电网公司  |
|  上海瑞和华苑小区 | 有序充电-延缓配网扩容 | 无 | 国家电网公司  |
|  青岛特锐德工业园 | 有序充电-延缓配网扩容、 分布式可再生能源消纳 | -- | 特来电  |
|  北京人济大厦 | 有序充电、V2B-延缓配网扩容、 降低用电成本 | 无 | 国网电动汽车服务有限公司  |
|  上海（规划中） | 需求响应（填谷） | 需求响应市场收益 | 国家电网公司  |
|  广东省 | 现货市场平衡 | 现货市场收益 | 充电运营服务商  |

来源：根据作者调研访谈和国电南瑞科技股份有限公司（2018）总结

20

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

### 专栏 3 | 中国目前典型车网协同试点介绍

#### 有序充电：北京国网公司海淀西八里社区有序充电试点

该项目的设计初衷是局部负荷的削峰填谷，延缓局部变压器增容投资。该试点新建了30个有序控制的交流充电桩，充电功率为7kW。参与有序充电的电动汽车品类多元，涉及比亚迪、荣威、北汽等品牌的多种车型。

整体项目涉及配电网和充电桩改造，加装能源控制器、能源路由器等。项目以国网智慧能源服务系统为主站，可以对小区负荷进行实时监测，根据小区负荷情况，通过加装在充电桩侧的能源路由器，控制调整充电桩输出功率，实现有序充电。同时，项目通过“一桩双充”，实现了临近车位共享充电模式，提高了充电桩利用率。

#### V2X：国网电动汽车服务有限公司人济大厦V2B试点

该项目是国内探索少数电动汽车双向充放电的试点。其设计初衷是实现局部负荷的削峰填谷，达到高峰时段降低用电成本、低谷时段提高变压器负载率的目标。该试点的充放电站由5个交直流双向充放电桩组成，功率范围从7kW到150kW不等，参与充放电的电动汽车为比亚迪e6-400纯电动汽车，部署了站级监控室对V2G充放电站运行情况进行监测，项目总投资约为270万元。

此项目不仅实现了车-桩-网之间双向电流流动，也建立了双向智能控制装置，即当支持V2G技术的车辆接入电网后，车辆可充放电的实时容量、充电状态（SOC）等信息会提供给云端管理系统。车辆的充放电将由云端管理系统控制，该系统根据建筑的实际负荷情况，在负荷低谷时段对电动汽车进行充电，提高变压器负载率，在负荷峰值时段放电，并根据负荷情况调整放电功率。

中国电动汽车与电网协同的路线图与政策建议

21

# FOOTBALL CHALLENGE

## 第四章

# 中国电动汽车与电网协同的可行性分析

未来，中国大规模电动汽车和可再生能源的推广为车网协同提供了机遇。我国的车网协同虽然起步比欧美国家略晚，但具备后发优势，可借鉴欧美经验，避免对电网和电源的公共投资，辅助可再生能源并网消纳。

但对比国际，中国的车网协同实践不仅面临相同的技术阻碍（如V2G对电池衰减的影响），也面临中国特有的电力市场改革、充电标准兼容性挑战（见表8）。因此，探索适合中国的本地化车网协同实施路径，需要从中国现阶段制度环境、技术标准入手，分析不同应用场景下的车网协同在中国未来的潜力与阻碍。

表 8 | 中国与国际在车网协同的制度与技术进展上的差异对比

|   | 主要阻碍 | 国际进展 | 国内进展与差异  |
| --- | --- | --- | --- |
|  政策与制度 | 电力市场完善程度与准入门槛 | 电力市场相对完善，准入门槛（如市场主体、最低额定容量、响应时长）要求不高，允许各类设施接入电力市场并参与交易 | ✎**阻碍有别于国际** · 中国电力市场的市场机制有待完善，正经历全面的改革过程。例如，目前辅助服务市场主体以发电设施为主（个别地区也包括集中式储能），用户侧资源（如电动汽车）尚不在其列 · 中国电力市场仍以计划属性较强的中长期市场为主，现货市场正在建立的初期；地域间市场改革方向与进程差异较大  |
|   |  针对用户侧资源接入配电网的限制（表后资源分散、难以管理） | 允许电动汽车等用户侧资源并网，但需要经过严格、漫长的项目核准、并网验收与调试过程 | ✎**阻碍有别于国际** · 《分布式发电管理办法》（国家能源局2018）中未明确电动汽车是否属于分布式发电系统范畴。与分布式光伏、热电冷热联供等分布式发电系统不同，电网企业尚未建立关于电动汽车发电接入配电网的运行制度和机制  |
|   |  面向终端电动汽车用户的峰谷电价机制及其他激励措施的缺失 | 针对电动汽车用户制定专门的峰谷电价，且其价差较常规电价更大 | ✎**阻碍有别于国际** · 部分地区没有居民、工商业的峰谷电价，且受充电服务费、转供电加价影响，峰谷电价传导不畅  |

中国电动汽车与电网协同的路线图与政策建议

23

表 8 | 中国与国际在车网协同的制度与技术进展上的差异对比（续）

|   | 主要阻碍 | 国际进展 | 国内进展与差异  |
| --- | --- | --- | --- |
|  技术与标准 | ① 车-桩-网通信协议：不支持有序充电和V2X | · “车-桩”间协议：CCS与CHAdelMo 2.0可有效支持有序充电和V2X · “桩-网”间协议：OpenADR等多个开放协议可提供支持 | ≠阻碍有别于国际 · “车-桩”间协议：现有国家标准对有序充电的支持程度有待改善，尚不支持V2X · “桩-网”间协议：缺乏国家标准，不同的实施主体和技术途径下，支持有序充电和V2X的通信协议仍有待探索  |
|   |  ② 车：多数电动汽车品牌不支持V2X | 日产、三菱等品牌已经开始支持商业化的V2G产品 | =阻碍同国际  |
|   |  ③ 网：配网设备需要改造 | 针对电动汽车提供服务的不同，对计量等设备进行改造 | =阻碍同国际  |
|   |  ④ 电池：V2X可能加速动力电池衰减 | 开展相关动力电池衰减测试；利用电池管理系统进行智能管理 | =阻碍同国际  |

图 9 | 车网协同各保障机制间的关系

![img-16.jpeg](img-16.jpeg)

说明：图中黄色框为需要政府部门提供的保障机制。

本章将从经济可行性、政策保障缺口、技术标准可行性与用户接受度四个方面，分别分析各类车网协同应用在中国的可行性。以上四个方面也是目前在中国推广车网协同亟待完善的领域，彼此相互影响（图9），特别是政府部门提供的保障机制——包括终端电价机制、电力市场与准入制度、充电标准等所发挥的作用较大，能够影响到车网协同的经济可行性与用户接受度。

24

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

## 4.1 经济可行性分析

电动汽车与电网协同不属于公共服务，其成功推广离不开可靠的商业模式。从成本看，实现有序充电或V2X涉及充电桩和配电网的升级改造（图10）。从收益看，车网协同的主体发起并参与车网协同并不是无偿行为，即便不考虑各个投资、参与主体间的收益分成问题，车网协同也需要峰谷电价差或电力市场收益作为经济激励。因而，本节主要分析不同应用场景下、不同车网协同措施对项目发起主体——包括电动汽车用户和负荷集成商（如电网企业、充电运营服务商、物业业主）整体的经济回报水平。

从成本构成看：有序充电和V2X的成本主要来自车端、充电桩和电网端增加智能控制设备、直流-交流逆变器等装置的成本（见图10）：

- ■ 有序充电：利用终端峰谷电价、智能控制两种措施可实现有序充电。如果仅依靠峰谷电价措施，无须任何设备改造投入，但效果有限（且无法参与需求响应或调峰辅助服务）；基于智能控制的有序充电需对本地配电网进行智能化改造，增加负荷监测设备与控制设备的投入。目前，这一改造成本缺乏参考值，较难预估，本研究假设一个有1000个住户的

图 10 | 车网协同项目的收支构成

![img-17.jpeg](img-17.jpeg)

说明：部分车网协同不涉及电动汽车侧改造，成本可忽略不计。黄色框为本研究考虑的收支项，灰色框则非本研究考虑的收支项。其中，建设施工费用和保险等其他费用缺乏数据基础且数值较小，对结果影响不大，充电服务费和现货市场收益不计入成本和收益的原因见后文分析。

中国电动汽车与电网协同的路线图与政策建议

25

住宅小区的有序充电投资为两百万元左右，而平摊至每个充电终端，其2020年成本增幅在2000元/桩左右。

- ■ V2X：实现车网双向协同的成本相对更高，不仅涉及车、桩、网的成本投入，还包括造成动力电池衰减的隐性成本（图11）。在动力电池侧，V2X可能也影响动力电池衰减，消耗电池循环寿命，该部分折旧成本需计入。在桩端，在现有单向充电机基础上，升级双向逆变功能。在网端所需改造与有序充电类似，但需要防止放电过程中配电网潮流变化，从而增加继电保护设备检修成本。以上各环节中，目前V2X电池折旧单价以0.5元/kWh计算——该数值由动力电池系统价格1000元/kWh及磷酸铁锂电池2000次循环寿命计算得出。与有序充电类似，配电网改造成本较难预估，考虑各种附加成本，2020年平摊到每个充电终端的成本以2500元/桩计算。

考虑到这些改造成本可能在推广初期较高，但未来可以通过规模化生产、技术升级，实现成本的下降。所以，本文假设有序充电新增投资从2020年的2000元/桩降低至

2030年的1000元/桩；V2X新增投资从2020年的2500元/桩降低至2030年的1500元/桩；电池充放电折旧从2020年的0.5元/kWh下降至2030年的0.16元/kWh。²

从收益构成看：车网协同不同应用场景的收益来源各不相同，需要逐一分析（见图10与表9）。对电动汽车通过有序充电或者V2X协助本地配网削峰填谷，其收益主要为峰谷电价差套利，或需量电费支出的节约。对电动汽车通过有序充电或V2X参与全网侧服务如调频、需求响应，其收益主要为各市场对不同服务的补偿。

值得注意的是，在国内管制的电力市场环境下，电动汽车参与全网服务的收益（如需求响应或辅助服务收益）是管制市场里的补偿水平，对比国际电力市场的竞争市场定价仍较低，部分地区辅助服务市场的补偿不能覆盖电力辅助服务成本（国家能源局 2019）。由于本文无法对未来的调频或需求响应市场的价格水平做预测，本文假设未来市场价格将延续目前管制市场下的补偿水平。此外，由于现货市场尚未成型，缺乏市场参考，电动汽车参与现货市场交易的经济性不在本文讨论范围。

图 11 | V2X在车端、桩端、网端的成本构成

![img-18.jpeg](img-18.jpeg)

说明：由于直流V2X可行性高于交流V2X，该成本构成着重考虑直流V2X、交流V2X的成本项还应包括升级本载交流充电机、增加逆变模块和保护回路。

表 9 | 不同应用场景下车网协同的收益构成

|  应用场景 |   | 收益构成 | 本研究测算  |
| --- | --- | --- | --- |
|  全网侧应用 | 现货市场电力平衡 | 现货市场收益 | --  |
|   |  需求响应 | 需求响应市场收益 | √  |
|   |  调频 | 辅助服务市场收益 | √  |
|   |  旋转备用 | 辅助服务市场收益 | --  |
|   |  缓解输电线路阻塞 | 现货市场收益 | --  |
|  配网侧应用 | 削峰填谷 | 用电成本节约 | √  |
|   |  分布式光伏充电 | 用电成本节约 | √  |
|   |  备用电源 | 备用电源投入节约 | --  |

26

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

本节将从配电网、全网两个角度，分别分析不同车网协同应用在2020年和2030年的投资回收期和内部收益率（计算方法见附录一）。

#### 4.1.1 配网协同经济潜力分析

##### 负荷侧削峰填谷

电动汽车通过有序充电或V2B，实现本地负荷的削峰填谷，降低用户充电成本，并避免本地配电网增容投资。电动汽车削峰填谷的收益主要体现在两个方面：

- 降低用电成本：针对有序充电，电动汽车可通过在电价低谷阶段充电，降低充电成本。电动汽车V2B可通过在电价低谷充电，在电价峰值放电，实现峰谷差套利，进一步降低电力用户的用电成本。这些用电成本的节约，可视作电力用户或电动汽车负荷集成商的“收益”。
- 降低配电网改造成本：有序充电和V2G可降低负荷高峰时段充电功率，从而降低配电网变压器和线路扩容成本。目前，配电网建设和改造费用由电网企业承担，其成本进而被纳入电网输配电价，从而提高整个社会成本。通过削峰填谷可有效降低电动汽车电网接入成本，最大化本地配电设备的利用率。

本文中削峰填谷的收益仅考虑用电成本节约，未考虑配电网改造成本的节约。峰谷电价机制是激励电动汽车参与削峰填谷的前提，具体收益视峰谷电价差、电动汽车转移电量程度而异。理想情况下，对日均行驶里程40km的电动私家车用户，车辆百公里电耗15kWh，年均充电量约2190kWh，若有序充电，可将用户高峰时段/低谷时段充电电量比从80%:20%转变为20%:80%，则有序充电年度移峰电量为1314kWh。目前中国城市峰谷电价差集中在0.3~0.6元，有序充电年收益为394~788元。V2B的削峰填谷电量潜力取决于车载电池容量。例如，车载电池容量为50kWh，若V2B模式下保持电池SOC始终在30%以上，则电池日放电能力为29kWh，明显高于有序充电转移电量。虽然V2B更高的转移电量可带来更高的峰谷差价套利收益，但也意味着更高的投资与运维成本。

由于住宅小区对削峰填谷、延缓配变增容有切实需要，本文分别计算通过有序充电和V2B的削峰填谷，对住宅小区居民和负荷集成商（如电网企业、充电运营服务商）的经济效益（仅考虑综合收益，不计利益分成）。其中2020年有序充电、V2B的投资和运维成本如表10所示，假设居民峰谷电价差为0.3元。值得注意的是，有序充电还可减少电网企业配电增容的投资。由于本节主要集中于对终端用户的经济激励，因而该部分投资的节约不在本文探讨范畴。

表 10 | 住宅小区：削峰填谷成本收益影响因素（2020年）

|  有序充电 |   | V2B  |   |
| --- | --- | --- | --- |
|  有序充电改造成本 | 2000元/车 | V2B 配网和充电桩改造 | 2500元/车  |
|  有序充电终端运维成本 | 20元/车/年 | V2B电池折旧单价 | 0.5元/kWh  |
|  有序充电转移量 | 60%充电量 | V2B终端运维 | 200元/车/年  |
|  有序充电策略 | 一天一充 | 充放电策略 | 一天一充一放  |
|   |  | 车载电池容量 | 50kWh/车  |
|   |  | 电池备用SOC | 30%  |
|   |  | V2X电损 | 20%  |

中国电动汽车与电网协同的路线图与政策建议

27

具体计算过程如下：

■ 有序充电：

$$CF_{LSC} = P_{TOU} \times E_{shift,SC} - C_{SC}$$
$$E_{shift,SC} = FC \times AM \times 60\%$$

其中：

$CF_{LSC}$：有序充电第t年净现金流，元；

$P_{TOU}$：充电电价峰谷差，元/kWh；

$E_{shift,SC}$：有序充电每年转移电量，kWh；

$C_{SC}$：每年有序充电运维成本，元；

$FC$：车辆单位行驶公里电耗，kWh/km；

$AM$：车辆每年出行里程，km。

■ V2B：

$$CF_{L,VA2} = P_{TOU} \times E_{shift,VA2} - C_{deg} - C_{VA2}$$

$$E_{shift,VA2} = B_{cap} \times \mu \times 365 - FC \times AM \times EF_{VA2} + FC \times AM \times 60\%$$

$$C_{deg} = (B_{cap} \times \mu \times 365 - FC \times AM) \times P_{deg}$$

其中：

$CF_{L,VA2}$：V2G第t年现金流，元；

$E_{shift,VA2}$：V2G每年转移电量，kWh；

$C_{deg}$：每年电池充放电折旧，元/年；

$C_{VA2}$：每年V2G运维成本，元；

$B_{cap}$：车载电池储能容量，kWh；

$\mu$：电池V2G充放电容量上限，%；

$EF_{VA2}$：V2G充放电转换效率，%；

$P_{deg}$：电池单位充放电折旧成本，元/kWh。

表11为有序充电和V2B两种措施的经济性对比。在执行峰谷电价的地区，2020年，有序充电参与削峰填谷的经济性较高，内部收益率达23%，而V2B受于电池衰减折旧影响较大，尚无商业模式。但在2030年，随着电池成本下

降，基于V2B削峰填谷的内部收益率将大幅提升——高达81%，远超有序充电50%的内部收益率。

## 分布式光伏充电

近年来，光伏技术快速成熟，光伏组件成本不断下降，部分地区光伏平准化度电成本已接近甚至低于国内一般工商业目录电价水平。这意味着，在采用工商业目录电价的场所安装分布式光伏设备为电动汽车充电的“光+充”模式，能够为电动汽车用户节约用电成本，具备商业推广的条件。

与国际上居民分布式光伏技术快速发展所不同，中国居民侧屋顶光伏系统的开发潜力有限，仅有在集中式充电站（如公交车充电站、公共充电站等）安装分布式光伏设备具备较大的潜力。在这些场景建设分布式光伏电站，可以降低电动汽车集中充电对电网的冲击，节省用户电费支出，同时利用光伏设备提供的清洁电力。若同处用户侧的电动汽车充电时间灵活可调，通过有序充电或者V2B措施，使电动汽车与分布式光伏电站发电时间匹配，可实现电动汽车与光伏发电在用户侧的直接协同，节省用户侧储能设施投入，提升分布式光伏设备利用率。

“光+充”模式下的现金流收益为：利用分布式光伏充电的用电成本节约。该成本的节约主要来自光伏平准化度电成本与目录电价之差（这里采用工商业目录电价），并去除有序充电或V2B的设备投入。其中，本文假设2020年和2030年分布式光伏平准化度电成本分别为0.38元/kWh（与火电上网电价基本持平）和0.22元/kWh。

电动汽车利用的光伏电量与场地内分布式光伏电站的装机量有关：分布式光伏技术对屋顶面积有较高要求，目前每平方米的装机容量约为100W，因此，分布式光伏发

表 11 | 住宅小区削峰填谷：有序充电和V2B的经济性对比

|   | 有序充电 |   | V2B  |   |
| --- | --- | --- | --- | --- |
|  受益方 | 电动汽车车主及负荷集成商  |   |   |   |
|  年份 | 2020年 | 2030年 | 2020年 | 2030年  |
|  动态投资回收期（年） | 5.0 | 2.2 | >12 | 1.4  |
|  内部收益率 | 23% | 50% | <0 | 81%  |

28

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

电在终端充电量中的比例往往有限，本文假设利用有序充电，场地内光伏的出力占充电站用电负荷的60%；电动汽车充电量中光伏电量比例随着分布式光伏出力曲线实时变化，即第t时段光伏充电量为充电功率与第t时段光伏电量浓度之积。

同样通过内部收益率和投资回收期的方式，测算该应用下的经济性。具体计算过程如下：

■ 有序充电：

$$CF_{t,pv} = (C_{grid} - LCOE_{pv}) \times E_{shift,sc} - C_{sc}$$

$$E_{shift,sc} = 365 \times \frac{I_{max} + \frac{FC \times AM \times 60\%}{EF_{sc} \times P_{EV}}}{\int_{t_{max}} P_{EV} \times G_{PV}(t) dt}$$

其中：

$C_{grid}$：用户侧目录电价，元/kWh；

$LCOE_{pv}$：光伏平准化度电成本，元/kWh（含设备与建设成本，根据10年折算）；

$E_{shift,sc}$：每年有序充电转移电量，kWh；

$P_{EV}$：电动汽车充电或放电功率，kW；

$G_{PV}(t)$：光伏日发电曲线，即第t时段光伏电量浓度；

$EF_{sc}$：充电效率，%；

$t_{max}$：光伏发电高峰起始时间。

■ V2B

$$CF_{t,V2B} = (P_{grid} - LCOE_{pv}) \times E_{shift,v2B} - C_{deg} - C_{v2B}$$

$$E_{shift,v2B} = 365 \times \frac{I_{max} + \frac{B_{me} \times \mu - FC \times AM}{EF_{v2B} \times P_{EV}} + \frac{FC \times AM \times 60\%}{EF_{sc} \times P_{EV}}}{\int_{t_{max}} P_{EV} \times G_{PV}(t) dt}$$

$$C_{deg} = E_{shift,v2B} - FC \times AM \times P_{deg}$$

其中：

$CF_{t,V2B}$：V2B第t年现金流，元；

$E_{shift,v2B}$：V2B每年转移电量，kWh。

表12显示有序充电和V2B与分布式光伏互动的经济性差异。值得指出的是，无论是否采取车网协同措施，“光+充”模式的经济性已开始显现。这里分析车网协同措施是否能在“分布式光伏+无序充电”的基础上，进一步提升经济性。2020年由于有序充电或V2B前期设备投入成本较高，两种车网协同措施对“光+充”模式经济性的改善程度并不明显。2030年有序充电的经济性开始浮现，特别是有序充电能够更好地匹配光伏出力与电动汽车的充电负荷，但V2B（与“光储充”模式相近）受电池衰减和设备投入影响较大，经济性有限。

# 备用电源

电动汽车同样具有备用电源的特点，理论上具有提升用户供电可靠性和供电质量的潜力。2019年中国城乡居民生活用电量为1.02万亿千瓦时（中电联 2020），按照全国14亿人口计算，则每户家庭日均用电量接近6kWh。2019年新售电动乘用车车载电池容量普遍在50kWh以上，即车载电池容量可满足一般家庭近10天用电需求。从放电功率角度看，目前7kW的交流充电机也可保证一般家庭全部用电设备的电力供应。

国外较早开展了电动汽车作为备用电源的探索。例如日产汽车的Vehicle to Home（V2H）系统采用聆风（LEAF）电动汽车作为备用电源（见图12），通过功率转换系统（PCS）将直流电转化为交流电对家庭进行供电。利用CHAdeMO直流充电接口，可从电动汽车输出电力。该系统在分电盘上安装了切换开关，用户可用于选择切换使用电动汽车供电或者电力公司供电。使用电动汽车供电

表 12 | 基于有序充电和V2B的分布式光伏互动经济性对比

|   | 有序充电 |   | V2B  |   |
| --- | --- | --- | --- | --- |
|  受益方 | 电动汽车车队运营商（如公交企业）或充电运营服务商  |   |   |   |
|  时间 | 2020年 | 2030年 | 2020年 | 2030年  |
|  动态投资回收期（年） | >12 | 10.7 | >12 | >12  |
|  内部收益率 | <0 | 9.4% | <0 | <0  |

中国电动汽车与电网协同的路线图与政策建议

29

时，分电盘便可以在物理上将汽车与电力网隔开，这样便不再需要系统连接的单独许可。在早期日本国内销售的4万台聆风电动汽车中，5%的客户购买了这一系统（工业和信息化部 2014）。

虽然电动汽车具备作为备用电源的技术潜力，但其经济性需要结合不同用户的需求具体分析。与日本不同，国内一般居民较少安装备用电源。而对于一些特殊工商业用户，利用电动汽车替代传统备用/应急电源的技术可行性和经济性也有待验证。

图 12 | 日产汽车Vehicle to Home (V2H)系统

![img-19.jpeg](img-19.jpeg)

来源：日产汽车 https://www.nissan-global.com

![img-20.jpeg](img-20.jpeg)

## 4.1.2 全网协同经济潜力分析

### 调频辅助服务

电力辅助服务指为维护电力系统的安全稳定运行，由发电企业、电网经营企业和电力用户提供的服务。在我国，电力辅助服务具体包括一次调频、自动发电控制（AGC）提供的二次调频、调峰、无功调节、备用、黑启动等。虽然一次调频和自动发电控制（AGC）均属于调频服务，但在中国的辅助服务机制下，一次调频为无偿的基本服务，仅AGC服务具有补偿。为鼓励发电企业提供AGC服务，各区域均颁布了《并网发电厂辅助服务管理实施细则》和《发电厂并网运行管理实施细则》（简称“两个细则”），对调频辅助服务的考核与补偿做出了规定。国内不同地区辅助服务定价机制及价格水平各不相同，导致各地电储能参与调频辅助服务的收益水平差异，如目前山西、内蒙古、广东等地电网侧储能参与调频已显现出经济性。

目前，全国调频市场虽整体市场空间有限，但未来增长前景可期。2018年全国参与电力辅助服务的发电企业获得的调频补偿为40亿元，在辅助服务总费用中占比不足30%（国家能源局2018）。但随着可再生能源发电规模日益扩大，为保证电网频率稳定和区域偏差控制的要求，调频等辅助服务市场的规模也将逐渐扩大，这无疑将会提升电池储能在电力市场的应用空间。

#### ■ 有序充电：

$$CF_{t,sc} = p_f \times E_{shift,sc} \times (1 - \alpha) - C_{sc}$$

其中：

每年有序充电转移电量：$E_{shift,sc} = FC \times AM \times 60\%$

单位千瓦时调频服务补偿价格 $p_f$：

$$p_f = p_{fmw} / 1000 \times 3600 / t_f \times 2$$

$p_{fmw}$：单位兆瓦调频服务补偿价格，元/MW；

$t_f$：平均单次调频时长，h。

#### ■ V2G：

$$CF_{t,V2G} = p_f \times E_{f,vaq} - C_{dog} - C_{vaq}$$

其中：

$$E_{f,vaq} = (B_{vaq} \times \mu \times 365 - FE \times AM) \times EF_{vaq}$$

$$C_{dog} = (E_{f,vaq} - FE \times AM) \times P_{dog}$$

单位千瓦时调频服务补偿价格 $p_f$ 为：

$$p_f = p_{fmw} / 1000 \times 3600 / t_{f+2}$$

其中，

$p_{fmw}$：单位兆瓦调频服务补偿价格，元/MW；

$t_f$：平均单次调频时长，h；

$C_{dog}$：每年V2G动力电池折旧，元/年；

$C_{vaq}$：V2G运维成本，元/年；

$P_{dog}$：V2G动力电池折旧，元/kWh。

本文假设单位兆瓦的调频服务补偿价格为5元/MW；由于本文无法对未来的调频或需求响应市场的价格水平做预测，这里假设收益水平将延续目前水平，未来调频收益有可能会比文中预测更高（见表13）。2020年，电动汽车以有序充电方式参与调频已经具备经济性；而到2030年，随着V2G前期投入成本的下降，特别是考虑到调频服务具有单价高、频次多的特点，电动汽车参与调频具有较明显的经济性。

表 13 | V2G方式提供调频服务的经济性分析

|   | 有序充电 |   | V2G  |   |
| --- | --- | --- | --- | --- |
|  受益方 | 电动汽车用户及负荷集成商  |   |   |   |
|  时间 | 2020年 | 2030年 | 2020年 | 2030年  |
|  动态投资回收期（年） | 4.7 | 2.4 | >12 | 0.8  |
|  内部收益率 | 19% | 47% | <0 | 135%  |

中国电动汽车与电网协同的路线图与政策建议

31

## 需求响应

需求响应指电力用户针对价格信息或激励机制做出响应，改变自身用电模式的市场化参与行为（田世明 2014）。电动汽车参与需求响应可对电力系统起到削峰填谷的作用：在供电紧张时，限制部分电动汽车充电，降低部分电动汽车的充电功率，或允许电动汽车向电网反向送电，从而降低负荷高峰时段电网供电压力；在负荷低谷时段，鼓励电动汽车充电，从而提升负荷低谷时段电网利用水平。

电力需求响应的激励水平取决于目前的补偿机制。以江苏省为例，根据《江苏省电力需求响应实施细则（修订版）》的规定（江苏省经济和信息化委员会 2018），对通过需求响应临时性减少（错避峰）的可中断负荷，按其响应类型和响应速度试行可中断负荷电价，其中，实时需求响应调控时间超过 2 小时，电价标准为 15 元/kW；对通过需求响应临时性增加（填谷）的负荷，促进可再生能源电力消纳，执行可再生能源消纳补贴，其中约定响应谷段可再生能源消纳补贴为 5 元/kW，平时段补贴为 8 元/kW。

电动汽车参与需求响应的收益主要基于响应功率和响应频次。其每年净现金流计算过程如下：

■ 有序充电：

$$CF_{t,ac} = R_{dr} - C_{dr}$$
$$R_{DR} = f \times p_{dr} \times P_{EV}$$

其中：

$CF_{t,ac}$：有序充电第 t 年净现金流，元；

$R_{dr}$：每年需求响应收益，元；

$C_{dr}$：每年需求响应运维成本，元；

$f$：每年电动汽车参与需求响应频次，次；

$p_{dr}$：需求响应补偿单价，元/kW/次；

$P_{EV}$：电动汽车充电功率，kW；

■ V2G

$$CF_{t,v2g} = R_{dr} - C_{deg} - C_{v2g}$$
$$C_{deg} = f \times t \times P_{EV} \times P_{deg}$$

其中，

$t$：单次需求响应持续时间，小时/次；

需求响应的发布频次较低，同一用户一般不超过 10 次/年，或响应时间不超过 20 小时/年，且需求响应调度指令更具随机性，调度机构往往在事前较短时间内（如 4 小时内）。本研究假设车辆充电功率为 7 kW，每年参与需求响应为 5 次，单次响应时间为 1 小时，响应补偿价格为 10 元/kW。

投资回收期和内部收益率结果如表 14 所示，随着电池成本的下降，电动汽车以 V2X 方式参与需求响应的收益率将不断提升，在 2030 年将有望超越有序充电。

### 4.1.3 总结

电动汽车与电网协同存在多种应用场景，但这些应用的经济性水平各异。在不考虑现行市场机制不完善、市场准入要求高、技术阻碍多的基础上，本节对比了 2020 年、2030 年电动汽车有序充电和 V2X 在四种应用场景下的内部收益率（图 13）：

对比有序充电和 V2X：由于目前电池成本较高，加之 V2X 对电池寿命可能产生影响，目前 V2X 的经济性普遍偏低。2030 年后，随着电池成本的下降，V2X 的经济性将快速得到改善。特别是 V2X 可能提供的充放电电量比有序充电更多，所以，当克服设备投入成本、电池折旧成本后，V2X 能够提供更多的经济收益。

对比各类应用场景：近期削峰填谷经济性较高，特别是基于有序充电的削峰填谷已具一定经济性；在 2030 年以

表 14 | 电动汽车通过有序充电和 V2X 方式参与需求响应的经济性对比

|   | 有序充电 |   | V2G  |   |
| --- | --- | --- | --- | --- |
|  受益方 | 电动汽车用户及负荷集成商  |   |   |   |
|  时间 | 2020 年 | 2030 年 | 2020 年 | 2030 年  |
|  动态投资回收期（年） | 8.6 | 3.6 | 6 | 2.8  |
|  内部收益率 | 12% | 32% | 19% | 40%  |

32

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

图 13 | 2020年、2030年各应用场景有序充电和V2X经济性对比（纵轴：内部收益率）

![img-21.jpeg](img-21.jpeg)

图 14 | 电池折旧成本和V2X电损对削峰填谷经济性的影响（纵轴：内部收益率）

a. 电池折旧成本变化（2030年）

![img-22.jpeg](img-22.jpeg)

说明：图 2 中，当电池折旧成本达到 0.3 元/kWh 时，基于 V2X 的削峰填谷将不再具备经济性。

b. V2X电损变化（2030年）

![img-23.jpeg](img-23.jpeg)

后，调频开始具有更高的市场价值。受发布频次的影响，需求响应的经济性略低于削峰填谷和调频。以上结果说明，在当前中国电力市场与电价水平下，削峰填谷具有更可观的经济性，这与国际上调频普遍具有更高的经济价值有所区别。值得注意，削峰填谷的经济性是基于终端峰谷电价机制，但国内仍有很多地区尚未采用峰谷电价。

从影响车网协同经济性的因素分析，终端电价与电力市场补偿水平、电池折旧成本和前期设备投入，以及双向充放电电损对车网协同的经济影响较大：

- 终端电价与电力市场补偿水平：作为车网协同最主要的收益来源，加大峰谷电价差、提高调频服务的补偿水平，能有效提高车网协同的经济性。未来，随着全网服务的补偿单价与发布频次大幅提升，其收益可能会超过削峰填谷的收益，成为收益最高的应用
- 电池折旧成本和前期设备投入：虽然对比固定电化学储能，车网协同可以节约前期电池购置成

本，但V2X对电池寿命的影响不可忽略。根据本研究测算，电池折旧成本是影响V2X经济性的最重要因素（图14），其对经济性的影响程度甚至高于V2X设备投入的影响程度（若不计电池折旧成本，基于V2X的车网协同应用在2020年就具备经济可行性）。未来，随着电池技术提升与成本下降，以及车网协同的硬件设备规模化推广，车网协同的经济性也会进一步得到改善。

- 双向充放电电损：V2X过程中的效率损失对车网协同的经济性也有相当影响。当充放电效率损失从20%提升至30%时，削峰填谷的内部收益率将从81%下降到37%（2030年水平）。所以，降低双向充电过程中的电损对改善车网协同的经济性有较大帮助。

值得指出的是，本研究没有计入充电服务费，因为在一些车网协同的目标场所（如办公室、住宅等场所）并不存在充电服务费。但在部分工商业场所如商业综合体及公共充电站，计入充电服务费会影响以上应用的经济性。

中国电动汽车与电网协同的路线图与政策建议

33

## 4.2 政策保障缺口分析

政府部门提供的保障机制（包括终端电价机制、电力市场与准入制度）是影响车网协同经济可行性、建立商业模式的重要前提。

目前，中国终端用户的电价分成市场电价和目录电价。参与中长期电力批发市场的部分电力用户（或售电企业）如大工业用户，其交易电价为市场电价。而未参与电力批发市场的用户，如居民、部分工商业和大工业用户，采用政府制定的目录电价。

现阶段，我国电动汽车用户及其负荷集成商无法直接参与包括中长期在内的各种电力市场交易，所以目录电价机制——特别是峰谷电价机制——决定了电动汽车与电网协同是否存在商业可行性。然而，受部分地区峰谷电价机制缺失、转供电加价等因素影响（表15），电动汽车与电网协同尚缺乏可靠的商业模式。这导致虽然峰谷电价差套利收益潜力最大（见第4.1.1节分析），但目前没有经济激励机制。

展望未来，以国际趋势类推，中国电动汽车用户或负荷集成商参与中长期市场、现货能量市场、辅助服务市场，将成为中国车网协同的大势所趋。然而，中国各类电力市场当前的管制程度仍然较高，正处于市场重塑的阶段。随着改革的不断推进，电力市场的红利将不断得到释放，车网协同的潜力也不断提高。

### 4.2.1 终端用户目录电价机制的挑战

基于峰谷差的目录电价是电动汽车实现峰谷差套利的重要前提。此外，峰谷电价驱动的电动汽车在充电时间上的“错峰”，不仅可以延缓局部配网变压器增容需要，也可以缓解夏季用电高峰地区的负荷峰谷差、减少电源侧和输电侧投资。

为鼓励对电动汽车充电推广峰谷电价，国家发展和改革委员会分别于2014年和2018年出台了《关于电动汽车用电价格政策有关问题的通知》和《关于创新和完善促进绿色发展价格机制的意见》。尽管如此，受部分地区峰谷电价机制缺失、转供电加价等因素影响，峰谷电价机制仍然不能有效发挥作用（见表16）。

**居民电价：**中国城市中，居民峰谷电价覆盖程度有限。本研究针对36个中心城市居民电价的梳理显示，执行居民峰谷电价的仅有10个城市（28%），仍有很多城市（如北京、苏州）对居民电价采用阶梯电价或固定电价，低于执行工商业峰谷电价的城市数量——18个城市（50%）（见表17）。

此外，国内城市居民电价的峰谷差较小。美国圣地亚哥天然气和电力公司（2014）针对电动汽车用户的试验表明，当峰谷电价比为6：1时，接近90%的电动汽车主会主动选择在谷时充电。所以，该公司针对辖区内拥有电动汽车的家庭加大峰谷分时电价差，电动汽车居民用户的夏季峰谷电价比为5.5：1，高于加利福尼亚州普通居民的正常

表 15 | 中国车网协同政策保障机制的缺口

|   | 应用场景 | 政策保障缺口  |
| --- | --- | --- |
|  配网侧应用 | 削峰填谷、延缓变压增容投资 | 终端用户目录电价： ■ 大部分地区没有居民、工商业的峰谷电价机制，导致削峰填谷缺乏经济激励 ■ 受充电服务费、转供电加价影响，公共充电桩的峰谷电价信号传导不畅  |
|  全网侧应用 | 现货市场电力平衡 | 电力市场机制： ■ 电力市场自身的市场机制不完善 ■ 电力市场参与主体有限、准入门槛高 ■ 电动汽车作为用户侧，储能并网运行存在管理的空白  |
|   |  需求响应  |   |
|   |  调频  |   |
|   |  备用（或爬坡）  |   |
|   |  缓解输电线路阻塞  |   |

34

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

表 16 | 中国36个中心城市居民和工商业峰谷电价执行情况与电价信号传导程度

|   | 峰谷电价执行情况 | 电价信号传导程度  |
| --- | --- | --- |
|  居民电价 | 覆盖程度有限 10个中心城市采纳 | 电价信号传导程度强： ■ （一般）无充电服务费 ■ （一般）无停车费 ■ 较少存在转供电加价问题  |
|  工商业电价 | 覆盖程度略高 18个中心城市采纳 | 电价信号传导程度弱： ■ （一般）有充电服务费 ■ （一般）有停车费 ■ 存在转供电加价问题  |

来源：世界资源研究所根据各城市 2018 年居民与工商业目录电价统计，统计中未计入广州市，因为广东省（除深圳外）安装独立电表的充电设施均采用大工业电价。

表 17 | 美国圣地亚哥天然气和电力公司（SDG&E）居民用户电动汽车充电峰谷电价（夏季）与深圳、上海夏季居民峰谷电价的比较

|  加利福尼亚州居民电价 | 峰时 （16:00至21:00） | 超级谷时 （0:00至6:00） | 峰谷电价比  |
| --- | --- | --- | --- |
|  拥有电动汽车家庭的居民电价 （夏季） | 44美分 | 8美分 | 5.5*  |
|  正常居民电价 （夏季，第一阶梯） | 47美分 | 16美分 | 2.9*  |
|  深圳居民电价 | 峰时 （14:00至17:00，19:00至22:00） | 谷时 （0:00至8:00） | 峰谷电价比  |
|  居民峰谷电价 | 1.08元 | 0.33元 | 3.2  |
|  上海居民电价 | 峰时 （6:00至22:00） | 谷时 （22:00至6:00） | 峰谷电价比  |
|  居民峰谷电价 （第二档阶梯） | 0.677元 | 0.337元 | 2.0  |

说明：\*加利福尼亚州的峰谷电价比为峰时电价与超级谷时电价之比。

来源：美国圣地亚哥天然气和电力公司（SDG&E）的EV/TOU 5电价与标准电价、上海市发展和改革委员会2019、中国南方电网2019

中国电动汽车与电网协同的路线图与政策建议

35

图 15 | 典型城市一般工商业与居民峰谷电价比

![img-24.jpeg](img-24.jpeg)

来源：各地相关文件

电价峰谷价格比2.9：1。然而，目前中国城市中，即使是居民峰谷电价比较高的深圳，其峰谷电价比也仅为3.2：1。

**工商业电价：**相对于居民电价，工商业的峰谷电价较为普及；据本研究统计，在36个中心城市中，18个城市已经采纳了工商业的峰谷电价；此外，工商业峰谷电价比也明显大于居民的峰谷电价比（见图16）。尽管如此，在商业综合体、写字楼或公共场所充电时，除峰谷电价外，用户还需负担充电服务费与停车费，甚至一些情况下，办公场所或商业综合体的充电桩还涉及物业部门“转供电”加价问题。这些因素综合影响，导致公共充电桩的峰谷电价信号传导机制不畅。

#### 4.2.2 电力市场的挑战

从国际经验看，电动汽车通过有序充电或V2G参与现货能量市场、辅助服务市场已是主流趋势。这些应用场景不仅可以为用户带来可观的收益，也可以使电力市场参与主体多元化，促进电力市场建设。

然而，与国际电力市场不同，中国电力市场管制程度仍然较高，正处于市场全面改革的背景下。目前，中国的四个电力市场包括中长期电力能量市场、现货能量市场、

辅助服务市场和需求响应市场。这些电力市场成熟情况各异，都需要完善，且电动汽车能否参与，仍需要提上电力市场改革的议程。

鉴于电动汽车在不同市场中参与应用场景的差异以及中国各类电力市场成熟度的区别，以下将分成中长期电能量市场及其他电力市场分别阐述：电动汽车适合参与中长期市场，以较低边际成本购电，且中国的中长期电能量市场发展相对成熟；而在现货电能市场、辅助服务市场或需求响应市场，电动汽车则能够参与更多元的应用场景，如现货购电卖电、提供调频辅助服务等，但中国目前电力市场管制化程度较高，电动汽车作为用户侧，储能的应用潜力将随着电力市场的改革不断拓展（见表18）。

#### ■ 电动汽车参与中长期电能量市场购电

中长期电能量市场的交易是以年、月、周等为周期，以大用户直接交易的电能量合约为基础。自2016年国家发展和改革委员会、国家能源局出台的《电力中长期交易基本规则（暂行）》建立了相对完整的中长期交易规则后，中国电力市场目前以中长期交易为主。2019年1月~10月，中长期电力市场交易的电量占全社会电量比重为28.6%（中国电力企业联合会 2019）。即便电力市场改

36

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

表 18 | 国内外电力市场比较

|   | 电动汽车 参与电力市场的应用场景 | 中国电力市场改革 当前进展  |
| --- | --- | --- |
|  中长期电能量市场 | ■ 低边际成本购电 | ■ 相对完善，但缺乏带电力曲线的交易  |
|  现货电能量市场 | ■ 低边际成本购电 ■ 高边际成本卖电 | ■ 在建设与试点期  |
|  辅助服务市场 | ■ 调频 ■ 备用 ■ 爬坡等支持可再生能源消纳的辅助服务 | ■ 市场机制不完善——采用补偿机制，而非市场机制，且补偿范围有限（如一次调频仍为无偿服务）  |
|  需求响应市场 | ■ 需求响应 （需求响应可能并入现货市场，可能在辅助服务市场中单独开设需求响应市场） | ■ 少数民族地区（如江苏、上海、河南、天津、山东等）有需求响应市场，补偿水平有限，依靠财政补贴，缺乏可持续的资源来源  |

革不断推进，未来中长期电能量市场的份额也将远高于现货市场的份额。

随着电动汽车数量规模与用电量的增加，电动汽车负荷集成商（如充电运营商）参与中长期市场已成为必然趋势：一方面，电动汽车的用电量较大、可预测，为其参与中长期市场提供条件。另一方面，电动汽车负荷集成商可在中长期市场上降低购电成本。以广东为例，2018年度双边协商的电价大约为比非市场化电价低0.00755元/kWh。以规模为一万辆电动汽车的负荷集成商为例，通过中长期交易一年可节约80万~240万元电费。

电动汽车负荷集成商参与中长期市场购电包括直接参与和通过售电企业参与两种方式。无论何种参与方式，均面临如下挑战：

**一是准入门槛的阻碍。**在中长期电力市场中，电动汽车负荷集成商尚无法满足电力用户的门槛（见表19），包括：

- ☐ 资格认定要求。北京电力交易中心要求，电力用户在电网企业独立开户、单独计量，这对很多使用“转供电”的充电桩并不实际。

☐ 用电量要求。目前部分省份（地区）对参与用户的用电量有最低要求，通常要求最小年度用电量需大于100万~1000万千瓦时。一些用户量大的充电服务运营商具备该条件。

☐ 用电量要求。目前部分省份（地区）对参与用户的用电量有最低要求，通常要求最小年度用电量需大于100万~1000万千瓦时。一些用户量大的充电服务运营商具备该条件。

值得注意的是，负荷集成商面对这些准入门槛也可以采取规避措施。例如，部分地区规定达不到电压等级或者达不到用电量要求的用户可以委托售电企业代理——湖南规定，由售电企业代理参与直接交易的电力用户不受电压等级限制，江苏省在《江苏省新能源汽车充电设施建设运营管理办法》（苏工信产业〔2019〕49号）中，甚至允许充电运营商注册成为售电企业，参与中长期电力市场。

**二是偏差考核引起的阻碍。**对于参与到中长期市场的负荷集成商，作为售电企业，也将面临严格的用电偏差考核与违约风险。例如，广东省要求，月度实际使用电量与其交易电量的偏差在±2%以上的情况，按月度竞价统一出清价格绝对值的2倍考核；北京要求，月度实际使用电量与其交易电量的偏差应小于5%，否则将向相应发电企业支付违约金。电动汽车充电负荷受分散私人用户

中国电动汽车与电网协同的路线图与政策建议

37

表 19 | 全国各地电力市场的准入门槛

|  省份（地区） | 准入门槛  |
| --- | --- |
|  广东 | - ■ 珠三角九市的工商业用户门槛为年度用电量1300万千瓦时 - ■ 粤东西北十二市的工商业用户市场准入门槛为年度用电量500万千瓦时 - ■ 广东省高新技术企业市场准入门槛为年度用电量400万千瓦时 - ■ 铜铁、建材行业企业市场准入门槛为年度用电量500万千瓦时  |
|  安徽 | - ■ 年用电量在 100 万千瓦时和 1000 万千瓦时之间的企业，由售电企业代理参与 - ■ 年用电量 1000 万千瓦时及以上的企业，可直接或委托售电企业代理参与  |
|  甘肃 | - ■ 10kV及以上电压等级电力用户，清洁供暖电力用户电压等级可适当放宽  |
|  青海 | - ■ 现阶段电压等级35kV及以上的大工业用户，选择连续稳定运行且用电量大的生产企业参与直接交易，根据市场发展情况，逐步扩大参与直接交易的电力用户范围  |
|  江西 | - ■ 10kV及以上电压等级电力用户，优先放开省级及以上工业园区内、售电侧改革试点园区内10kV及以上电压等级的电力用户参与直接交易 - ■ 10kV以下电力用户参与直接交易，应根据国家有关要求统筹推进  |
|  陕西 | - ■ 用电电压等级35kV及以上的工业企业或10kV及以上的高新技术企业，以及战略性新兴企业。工业园区和独立配售电企业可整体作为用户参与直接交易。环保排放必须达标  |
|  上海 | - ■ 参与直接交易的用户电压等级暂定为35kV及以上，年用电量100万千瓦时及以上，执行大工业或一般工商业电价，在电网企业独立开户，单独计量的企业 - ■ 年用电量在100万千瓦时和1000万千瓦时之间的企业参与直接交易，暂由售电企业代理；年用电量1000万千瓦时及以上的企业，可直接或委托售电企业代理参与  |
|  浙江 | - ■ 现阶段可放开电压等级在110kV（66kV）及以上的工商业用户，根据需要放开用电容量1000kVA及以上的35kV和10kV用户，根据市场发展情况放开用户  |
|  北京、湖南、山西、辽宁、宁夏、新疆、云南、河南、河北、四川、贵州、吉林、黑龙江、广西、海南 | - ■ 10kV及以上电压等级电力用户，鼓励优先购电的企业和电力用户自愿进入市场；（大多要求）拥有自备电源的用户应当按规定承担国家政府性基金及附加、政策性交叉补贴和系统备用费 - ■ （北京、湖南等）在电网企业独立开户、单独计量，执行大工业和一般工商业电价的企业，执行阶梯电价、差别性和惩罚性电价的电力用户不得参加  |

来源：国家发展和改革委员会、国家能源局、2016；各省、自治区和直辖市电力交易中心

随机充电行为影响较大，如果负荷集成商控制负荷偏差的能力有限，将面临偏差考核带来的高昂违约成本。

值得注意的是，各地区的偏差考核方法差别较大。例如，江苏在月内也有滚动修正、月内挂牌交易等措施，可减轻电动汽车负荷集成商在偏差考核方面的压力。另外，偏差考核控制是售电企业的核心运营能力之一，通过售电企业代理回避偏差考核风险也是可行方式之一。电动汽车负荷集成商也可以根据大数据分析，更好地预测与控制充电需求。

**三是缺乏峰谷电价或分时电价引导。**目前国内的中长期市场没有分时段的电价，这可能导致负荷集成商缺乏动力引导电动汽车用户在系统负荷谷时充电、峰时放电。在未来，随着现货市场机制的逐步推进以及可再生能源的广泛应用，带电力（功率）曲线的中长期市场将成为未来必然趋势（即交易标的为负荷，而非电力），分时电价机制也会成为中长期市场的特点，该问题将随着现货电力市场与中长期电力市场的改革得到解决。

38

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

## 专栏 4 | 中国电力市场发展现状

**现货电能量市场**还在逐步推进期。2017年国家发展和改革委员会、国家能源局联合下发了《关于开展电力现货市场建设试点工作的通知》，选择南方（以广东起步）、蒙西、浙江、山西、山东、福建、四川、甘肃等8个地区作为第一批试点，加快组织推动电力现货市场建设工作。截至2019年，大部分试点地区仍然处于“试出清”、不“试结算”的试运行阶段。

**辅助服务市场**在市场机制、参与主体等方面仍有待完善。目前中国的辅助服务市场包括调峰、调频、备用等，并以调峰为主，部分地区辅以调频服务。例如，2018年上半年中国辅助服务市场中，调峰、AGC和备用补偿费用占总补偿费用的90%以上（见专栏图1）。在市场机制上，我国辅助服务的补偿机制和补偿价格仍然是非市场化的，其主要依据2006年原国家电力监管委员会建立的辅助服务补偿机制。该机制中，辅助服务费用设定在发电企业内部循环，即由承担辅助服务量低于平均水平的发电机组支付费用给承担辅助辅助量超过平均水平的发电机组。电力调度机构按照单项辅助服务性能由高到低进行排序，基于系统运行需要调用。该机制属于“补偿机制”而非市场机制。在参与主体上，辅助服务仅限于发电侧机组，虽然部分地区集中式储能设施可参与，但用户侧储能仍未获得准入许可。

专栏图 1 | 2018年上半年电力辅助服务补偿费用构成

![img-25.jpeg](img-25.jpeg)

来源：国家能源局 2019

**需求响应市场**以非市场化的用户管理为主。需求响应（简称“DR”）是指采用价格或激励措施改变用户用电行为，以达到削峰填谷的目的。从2013年起，国家开展电力需求响应城市综合试点建设，北京、上海、江苏，以及广东佛山分别实施了需求响应项目试点工作。在参与主体上，多数试点由政府主导，电网企业支持参与，负荷集成商整合电力用户资源，参与用户以工商业用户为主。在补偿机制上，需求响应理论上需要现货价格的引导，但由于我国现货市场本身仍然在试点中，因此，目前国内需求响应尚未建立起市场化的价格机制。

中国电动汽车与电网协同的路线图与政策建议

39

## ■ 电动汽车参与现货能量市场、辅助服务市场和需求响应市场

目前，中国电力市场仍以计划属性较强的大用户直接交易的中长期交易为主；现货能量市场正在建立的初期；辅助服务市场、需求响应市场仍然以计划性为主，有待完善市场机制（见专栏四）。所以，电动汽车参与现货能量市场、辅助服务市场与需求响应市场，变现电动汽车的全网车网协同价值，遇到的阻碍不仅包括市场准入问题，也包括市场自身改革仍需完善的问题。

当前，电动汽车通过有序充电或者V2G参与辅助服务、需求响应或现货电能市场的主要阻碍在于以下几个方面：

**一是电力市场自身的市场机制不完善，补偿水平有限，资金来源不可持续。**由于现货市场的分时电价、节点电价能够充分反映不同时段、地区的边际发电成本和电力供需情况，所以，现货市场是一个成熟电力市场体系的核心。对全网侧车网协同的应用而言，现货市场中的价格信号能很好地体现电动汽车提供调峰、需求响应的市场价格——特别是在电力市场较成熟的欧美国家，全网侧应用（如调频）的收益水平是最高的。但在中国的当下，现货市场尚处于试点期，各类电力市场的管制水平较高，电动汽车能够参与的全网侧应用种类较少。主要制约包括：一些电动汽车适宜参与的应用场景，如一次调频或辅助可再生能源消纳的“爬坡”服务，仍为无偿服务或尚未推出；此外，当前中国电力辅助服务市场仍是补偿机制，而非市场化竞争机制，其辅助服务总费用在总电费中的占比较欧美等电力市场还存在一定差距。随着近期电力辅助服务市场加大补偿力度（国家能源局 2019），并在未来从补偿机制向竞争机制转型，中国全网侧车网协同应用的经济可行性有望提升。

此外，部分电力市场没有建立受益者付费机制，导致补偿资金来源不可持续。例如，电动汽车针对风电夜间出力大而提供了“填谷”需求响应服务，虽然与电动汽车实际充电需求耦合度很高，但该补偿机制主要依靠财政补贴，缺乏可持续的资金来源。未来，仍需依靠现货电能市场建立的分时电价机制，利用峰时电价收益建立可持续的支付来源。

**二是对电动汽车作为用户侧储能并网运行存在管理的空白。**电动汽车以V2G方式参与调频、调峰辅助服务以及现货市场交易均需要并网运行，但并网所需的技术规范、发电收购制度以及管理办法仍存在较多缺失。虽然国家能源局在2018年版《分布式发电管理办法》中首次将分布式储能设施纳入分布式发电系统，但没有明确电动汽车（及

充电桩）是否属于该范畴；相关政府部门与电网企业也未建立关于电动汽车放电接入电网的运行制度和机制。一方面是电动汽车接入电网的技术标准、工程规范和相关管理办法存在空白，是否能延用分布式光伏并网的管理办法仍是未知。另一方面是电动汽车放电出力是否也能够无障碍地上网，也缺乏相关管理意见。国内根据分布式光伏电站装机规模的差异，有全额上网、全部自用、余电上网三种不同运营模式规定（国家能源局 2018）；加利福尼亚州则鼓励电动汽车放电尽可能地上网——参与辅助服务市场，以降低辅助服务市场发电的边际成本。但电动汽车作为用户侧分布式储能的新兴事物，如何规范上网电量，仍有待研究探讨。

目前，国内所有类型的用户侧储能存在并网的限制，其主要源于：一是电动汽车作为用户侧资源较分散，难以管理，且用户侧资源并网供电可能对配电网电能质量与反向负荷造成负面影响，威胁配网安全；二是部分利益主体认为用户侧储能对电源测的发电进行储存，并参与电力市场交易的操作是“套利行为”。此外，国际上对用户侧资源并网也采取谨慎的监管措施，用户侧资源并网需要经过严格的项目核准、并网验收和调试过程。

**三是电力市场准入门槛较高。**除了物理层面的并网，电动汽车是否能够并网参与电力市场，还取决于电力市场对参与主体与市场准入门槛的界定。国际上，电力市场在准入机制设计上多以消除歧视性条款、开放市场准入为目标，允许各类设施接入电力市场并参与交易。例如，美国联邦能源管理委员会755法令（2011）明确“技术中立”和“基于绩效”的调频服务付款原则，设置调频辅助服务市场的准入门槛。而这一原则的影响范围，也在从调频辅助服务市场向整个电力批发市场延展：2018年，美国联邦能源管理委员会出台的 841法令要求，美国所有地区的批发电力市场（不仅是调频辅助服务）应消除储能准入门槛，允许储能设施参与电力市场交易。

在中国，以辅助服务市场为例，根据两个细则，市场参与主体主要针对大型发电设施。少数地区（如广东）的辅助服务市场也对具有一定规模的集中式电化学储能设施开放（国家能源局南方监管局 2018）。但是，零散的表层用户侧资源如电动汽车（及充电桩），由于所提供的容量与电能量有限、管理复杂，尚未被系统纳入辅助服务市场主体的范畴。尽管如此，2019年年底，华北辅助服务市场在全国首次提出以调峰市场为试点，将参与主体扩展到包括电动汽车（及充电桩）在内的第三方主体（国家能源局华北监管局 2019），以调峰市场为突破口，电动汽车全面参与辅助服务市场或整个电力市场，接受统一调度也有望成为现实。

40

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

表 20 | 辅助服务与需求响应市场（对电储能的）准入门槛以及对电动汽车的负荷集成要求

|   | 准入要求 | 负荷集成要求 | 准入门槛  |
| --- | --- | --- | --- |
|  中国辅助服务市场 | 调峰 华北：调节容量不小于2.5MWh、最大充放电功率不小于5MW，持续时间不小于15分钟 | 250辆车同时充、放电，并持续15分钟以上（充放电功率为20kW） | 高  |
|   |  调频 山西：调频额定容量不小于15MW，持续时间不小于15分钟 | 750辆车同时充、放电，并持续15分钟以上（充放电功率为20kW） | 高  |
|  中国需求响应市场 | 需求响应 河南、江苏：非工业用户容量不小于200kW 江苏：约定响应一天累积时间不超过2小时，实时响应1次不超过30分钟 | 10辆车同时充、放电（充放电功率为20kW） | 中  |
|  美国辅助服务市场 | 调频 PIM：最小容量大于100kW，调频效果打分大于75% CAISO：持续时间不小于15分钟 | 5辆车同时充、放电，并持续15分钟以上（充放电功率为20kW） | 低  |

说明：PIM市场中的调频效果是指将调频资源的出力曲线和指令曲线进行对比，对延时情况、准确度和精确度三个维度进行打分，得到综合分数为“调频效果”。若调频效果大于75%，参与调频主体实际获得的调频收入为调频费用乘以调频结果打分；如调频效果低于75%，将不给予任何调频补偿。

来源：国家能源局华北监管局2019；国家能源局山西监管办公室2017；河南省发展和改革委员会2019；江苏省工业和信息化厅、江苏省发展和改革委员会2018

此外，由于目前中国电力市场主要针对大型发电设施，因而与美国电力市场相比，对参与主体的额定容量、持续时间等指标的准入要求较高（见表20）。即便电动汽车通过负荷集成商参与电力市场交易，但如果市场对所需的车辆数要求过高，可能抑制负荷集成商参与的积极性。

**四是未来电力市场价格波动性与电力市场绩效考核（现货市场偏差考核或辅助服务市场效果考核）风险，对电动汽车负荷集成商的管理水平提出了更高要求。**即便电力市场允许电动汽车负荷集成商参与，负荷集成商能否有效管理电力市场中的价格风险与严格绩效考核风险仍未知。

首先，未来现货市场、辅助服务市场的价格波动可能较强，对电动汽车集成商而言，既是机遇也是挑战。随着电化学储能成本下降与固定储能投资增加，我国调频市场已呈现供大于求的现象，导致近期国内调频市场的补偿价格下降。例如，2018年以前，山西省调频价格为15元/MW，而2018年年底，其报价调整至5~10元/MW。类似

的，根据德国辅助服务市场估算，如果未来德国有一千万辆电动汽车参与辅助服务市场，每辆电动汽车每年获得的收益仅在300元左右，且该收益会随着参与辅助服务市场的电动汽车数量增加而下降（国际可再生能源署2019）。在动态供需平衡的市场中，未来调频市场的供需将受多种因素影响（如可再生能源普及度、电动汽车参与程度，以及固定储能等其他调频资源投入），未来调频市场的价格也将呈现波动趋势。这些价格波动与市场周期性对电动汽车集成商的收益可能造成一定的不确定性，并对其经营管理水平提出了更高的要求。

其次，与中长期市场类似，辅助服务市场与现货市场也执行绩效考核。若电动汽车负荷集成商无法完成考核，其支付的违约金也将影响电动汽车参与全网服务的经济性。现实中，私家电动汽车在出行与充电上的随机性较大，这为负荷集成商准确预测电动汽车在电力市场所能提供的容量与持续时间，并将偏差控制在一定范围提出了新要求。

中国电动汽车与电网协同的路线图与政策建议

41

## 4.3 技术标准可行性分析

目前电动汽车与电网协同在各个技术环节均存在阻碍，未来升级改造的潜力巨大。这些阻碍包括V2X对动力电池侧电池衰减的影响，车辆侧加强车辆对充电标准的执行，充电桩侧支持双向充放电和双向计量，也有配电网侧对智能配电网的软硬件升级改造，更有“车-桩-网”信息交互的通信协议完善。

实现车网协同需要软件、硬件和通信协议全方位的升级（见图16）。这些升级不仅创造商业机会，也离不开一个相互协同的产业生态系统，包括动力电池、车辆、充电桩、配电网企业合作，以及软件平台、硬件设备与通信协议之间的协同兼容。

### 4.3.1 “车-桩-网”电流与信息交换的标准

有序充电或者V2X需要比现有标准更丰富、实时性要求更高的“新”信息，并在车辆、电网、用户等不同主体间进行交互。这些“新”信息包括车辆电池的SOC状态、用户出行需求、配电网实时负荷等，甚至也包含电网调度

中心远程发送的控制指令（见图17）。这些信息传导到充电运营商或配电网运营商的控制平台，后台进行计算与优化（见专栏五），将实时优化控制指令传导到电动汽车侧，进行充放电控制。

这些“新”信息通常不包含在现有“车-桩”和“桩-网”的通信协议标准中。因此，在国内外有序充电和V2X试点中，往往通过建立商业化通信协议，修订已有的通信标准，或鼓励用户通过手机APP直接输入信息等方法进行信息交互。

### 车辆-充电桩间的信息交换

国际车-桩充电标准中不乏对有序充电和双向充放电的支持。例如，日本的CHAdeMO标准不仅支持有序充电，也支持车-桩间直流的双向充放电操作。美欧的CCS标准采用ISO 15118通信协议，能够支持直流、交流的有序充电及双向充放电。

目前，我国国家标准不支持有序充电和双向充放电。其中，在有序充电方面：交流桩通信硬件接口要求（参见国家标准GB/T20234.2—2015《电动汽车传导充电用连接装置第2部分：交流充电接口》）和系统要求（参见国家标准GB/

图 16 | 实现电动汽车与电网协同所需的通信协议、硬件设备与软件系统升级

![img-26.jpeg](img-26.jpeg)

图 17 | 车网协同所需车侧、桩侧、网侧信息

![img-27.jpeg](img-27.jpeg)

42

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

T18487.1—2015《电动汽车传导充电系统 第1部分：通用要求》）不支持有序充电的信息交互；对比交流充电，直流桩硬件上已基本满足要求，只需对部分直流通信协议（参见国家标准GB/T27930—2015《电动汽车非车载传导式充电机与电池管理系统之间的通信协议（直流充电）》）及系统要求（参见国家标准GB/T18487.1—2015《电动汽车传导充电系统 第1部分：通用要求》）进行优化，即可支持有序充电。此外，以上直流与交流标准尚不支持电动汽车的反向放电。

**在有序充电方面**，通信硬件接口与软件协议在支持交、直流有序充电上有所区别，其中，交流充电协议为支持有序充电所需的改动较大：

- ■ 在交流充电协议上，国家标准《电动汽车传导充电系统 第1部分：通用要求》（GB/T 18487.1—2015）定义了基于PWM通信方式的交流充电方式，国家标准《电动汽车传导充电用连接装置 第2部分：交流充电接口》（GB/T 20234.2—2105）定义了交流充电接口标准。依据该标准，交流充电不设置任何物理通信线路，而是通过电源线的PWM信号，传输少量与充电相关的交互信息，而车辆侧的控制装置通过实时判断充电桩发出的PWM信号占空比，确定车载充电机的输出功率。虽然这一充电控制流程操作相对简单，但通过PWM的通信方式传播的信息量有限，交流充电桩无法采集足够的车辆信息（如电池容量、剩余电量等），用以定制有序充电或V2X的优化控制策略。理想情况下，交流有序充电需要对物理通信接口和通信协议均做出较大修改。

虽然现有交流充电方式在交互信息内容上受限，但目前在不改变国家标准的基础上，仍有规避方案。当前开展的有序充电试点中，多是通过充电用户在手机APP端填写必要车辆信息，以制定更完整的有序充电优化策略。在有序充电控制上，这些试点项目也是采用控制PWM信号或充电桩的电流、电压上限，对车辆进行充电启停控制与功率调节。由于交互的信息为手动输入，用户

的充电体验完全取决于人工提供信息的准确性。另外，未来，项目实施方也可通过协调整车生产企业或者国家车端远程监控平台，获取所需的车辆状态信息，以实现交流有序充电。

- ■ 在直流充电协议上，在硬件接口上具备了基于CAN的实时通信方式，满足有序充电和V2X的需求，而在通信协议方面，国家标准《电动汽车非车载传导式充电机与电池管理系统之间的通信协议》（GB/T 27930—2015）目前缺少充电桩主动控制车辆功率的控制命令，需进行适当调整优化。对比交流充电通信接口与协议，直流充电调整幅度更小。随着针对有序充电的需求日益增长，为解决交流充电不支持有序充电的问题，可以对现有交流桩进行小功率直流改造。但其商业模式和住宅小区用户接受程度尚待检验。

**在双向充放电方面：**通信硬件和软件协议接口的调整难度与有序充电类似。另外，特定的V2X应用场景（如调频）对传输频率、时延、响应时间都有较高要求，当前的国家标准《电动汽车非车载传导式充电机与电池管理系统之间的通信协议》（GB/T 27930—2015）能否支持也有待检验。

实现V2X的车网协同还需要“定制”车辆和充电桩（见图18）。对于交流充电方式，支持V2X涉及车端改造。目前车侧的整流器主要负责交流转为直流，为支持电动汽车放电，需在车辆侧加装直流转交流的逆变器。而这一改造面临两大挑战：首先，国际上安装车载逆变器所遵循的标准（SAE J-3072）与国际通用的分布式电源的逆变器标准（UL 1741）并不兼容；其次，在车辆侧加装逆变器也无疑会增加车辆重量与成本。对于直流充电方式，支持V2X只需要把充电桩改为有双向充放电能力的充放电机（PCS）即可，不涉及车辆改造，实现起来较为容易。

交流充电与直流充电比较之下，实现直流的有序充电和V2X相对容易；无论是日本的CHAdeMO充电标准，还是美国加利福尼亚州的电动汽车电网协同战略，均将

图 18 | 支持V2X所需的车辆及充电桩的硬件设备改造

![img-28.jpeg](img-28.jpeg)

中国电动汽车与电网协同的路线图与政策建议

43

直流充放电作为首要突破口。未来，如果中国国家标准与CHAdeMO标准在大功率快充上实现兼容（即“超级”标准），也有望在直流充电上对V2X予以支持。然而，从市场规模看，交流充电桩占比更大，且与有序充电的应用场景高度重合——根据中国电动汽车充电基础设施促进联盟（2019）统计，2019年12月，全国共有公共交流充电桩30万台，占全部公共充电桩数量的58%，而大部分私人充电桩也为交流桩。因此，未来仍有必要解决交流充电协议不支持有序充电的问题。

最后，实现有序充电和V2X的另一个主要阻碍在于车辆侧的不支持。虽然有关部门已经将是否满足充电接口标准，作为新能源汽车产品准入要求之一并进行专项检验（工业和信息化部 2017），但不同车辆品牌对充电标准的执行情况仍然差强人意。例如，一些车辆在交流充电中不执行PWM信号；另一些车辆未能在要求的时间内做出响应。此外，部分车辆安全保护程度较高，特别是对接入电网但一段时间不充电的情况，会进入休眠状态，导致第三方无法唤醒车辆执行有序充电或V2X的操作。充电桩和车辆接口标准化进程，以及后续车桩企业对标准的执行力度，都影响到车网协同的实现。

### 充电桩-充电运营商-电网间的信息交换

仅靠车-桩间通信协议不足以实现车网协同，完整的车网协同仍需要实现充电桩-充电运营商-电网间的信息交换。目前中国没有支持充电桩-充电运营商-电网间信息交互的国家标准，需要对电网运行调度相关的标准进行完善，增加对电动汽车有序充电和双向充放电的支持。

随着控制主体和实施手段的多元化，有序充电在技术路径选择、市场化程度方面均存在差异。无论国内还是国外，充电桩-充电运营商-电网间的信息交换存在两种常见方式：

**方式一，以充电运营商（或负荷集成商）为主的优化控制**（见图19）：配电网运营商实时将本地变压器的负荷等信息传输给充电运营商（或负荷集成商），由负荷运营商制定优化策略，控制、调整充电桩的充电时间和充电功率。该方式由于允许各个有实力的充电运营商或负荷集成商参与，因而更市场化。但其缺陷在于：一是需要配电网运营商分享变压器实时负荷等信息，这可能影响配电网的安全性。二是其信息交互过程较冗长、涉及主体较多。例如，配电网运营商在收到充电运营商发送的充电负荷信息后，实时反馈配电网负荷情况，并由充电运营商进行优化计算，控制充电桩执行优化策略。此过程中任何一个环节的通信不畅，均可能产生较长延时，影响有序充电执行效果。

**方式二，以配电网运营商为主的优化控制**（见图20）：配电网运营商在获得充电运营商的许可后，对充电桩直接进行控制。其中，配电网运营商将实时采集变压器负荷，依据实时负荷、车辆状态信息，在本地计算有序充电优化策略，并通过安装在充电桩侧的能源路由器，根据指定优化后的负荷曲线，对充电桩进行控制。实现该方式需要由配电网运营企业对充电桩加装能源路由器和通信设施，必要时也涉及对充电桩的软硬件改造，允许其接受配电网运营商的直接控制。该方式可避免方式一中的两个缺陷，在国内有序充电试点项目较为普遍。该方式的缺点在于：除配电网运营商外，其他市场主体参与度有限。

针对以上两种方式，由于国家标准在“充电桩-充电运营商-电网”间通信协议的缺失，现实中由不同运营商自定义通信协议（见专栏五）。对于是否有必要开发针对充电桩-充电运营商-（配）电网的物理通信方式与信息交换协议的国家标准，仍有待市场规模与商业模式更清晰后，再做讨论。而为建立更为公平开放的市场环境，有必要鼓励配电网运营商在信息安全的情况下，分享配电网的相关信息。

图 19 | 以充电运营商为主的有序充电优化控制方式

![img-29.jpeg](img-29.jpeg)

44

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

图 20 | 以配电网运营商为主的有序充电优化控制方式

基于通信协议的车-桩间信息交互 基于通信协议的桩-网间信息交互 基于手机APP的车-网间信息交互

![img-30.jpeg](img-30.jpeg)

# 专栏 5 | 电动汽车与电网协同智能优化软件

车网协同的智能优化软件以车-桩-网信息交互为基础，是电动汽车车网协同的控制“中枢”。高端的车网协同智能优化软件可以针对不同应用场景、优化目标，以及车辆并网、离网的动态信息，对电动汽车采取动态、差异化的控制策略。可以说，车网协同智能软件是充电运营商、负荷集成商或电网运营商的核心竞争力。

车网协同智能优化软件的构成因功能和应用场景而异，通常由两个部分组成，包括充电桩实时控制模块和电力调度模块（见专栏图2）。

智能充放电管理模块：该模块是实现有序充电、V2X的必要组成。在功能上，该模块统筹电动汽车出行“刚需”、动力电池SOC状态，以及本地配电网开放容量信息、电网远程调度指令（如调频、需求响应）等，将负荷或电能量分解成对每个充电桩差异化的控制策略。如果参与车网协同的车辆是营运车辆，该模块还需要与其运营计划的排班系统打通。针对有序充电，计算机化控制策略的软件一般连同其他硬件设备，布设在变压器侧。

电网调度模块：该模块主要为电动汽车V2X充放电参与全网的应用场景而设计。结合每辆车当天或第二天的出行需求，确定参与日内/日前（辅助）市场的交易标的（如电能量、功率容量与时间），并向电力市场提交报价。电动汽车出行行为分散、随机性大，针对电动汽车所面临的电力市场偏差考核或辅助服务效果考核的成本风险，需要利用软件建模分析用户出行、充电规律，或事前获得出行行程，以准确预测电动汽车在现货市场或辅助服务市场提供的电能量及容量。

专栏图 2 | 美国V2G试点项目：车-桩-网智能调度系统的组成与相互关系

![img-31.jpeg](img-31.jpeg)

来源：Weasel 等 2017

中国电动汽车与电网协同的路线图与政策建议

45

## 专栏 6 | 国际桩-网间通信协议分类与对比

国际上通行多个支持充电桩-运营商-配电网间信息交互的开放通信协议标准，包括Open Charge Point Protocol (OCPP)、Open Smart Charging Protocol (OCSP)和IEC 61850等。这些充电桩-运营商-配电网之间的信息交互标准，在控制主体、市场化程度上与中国类似，同样存在以市场化的充电运营商为主导的有序充电，以及以配电网运营商为主导的有序充电。因此，支持桩-运营商-配电网的开放通信协议也呈现分化。其中，OCPP协议可以支持以充电运营商为主导的有序充电，ISO 61850支持以配电网运营商为主导的有序充电，而OCSP则介于二者之间（ElaadNL 2016）（见专栏图3）。

专栏图 3 | 车-桩-网双向通信协议概览与分类

![img-32.jpeg](img-32.jpeg)

来源：ElaadNL 2016

46

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

### 4.3.2 配电网侧——智能配电网改造及人工智能应用

车网协同虽然延缓了配电网容量升级的投资，但支持车网协同需要对配电网进行智能化改造投入。这些智能化的硬件改造为大数据收集、人工智能与区块链的应用搭建了平台，为规模化推广车网协同奠定了基础。

虽然不同的技术路径和实施主体对配电网的改造要求不同，但必要的配电网侧改造包括负荷监测、双向电量计量和大数据与人工智能应用（具体见附录二）。

**负荷监测：** 基于智能控制的有序充电场景，必须加强对本地负荷的监测频次，以提高对灵活负荷（如电动汽车充电）控制的时间精度。目前，国内多数配电网对负荷的监测时间间隔较大，无法及时探测到本地负荷峰谷、动态实时的配网开放容量，降低了有序充电的调控能力。加装负荷监测设备可缩短配电网调度的响应时间，并增强有序充电的调控能力，这对未来车辆参与有序充电，甚至整合其他资源如分布式光伏的接入，均提供了必要条件。

**双向电量计量：** 实现电动汽车V2X必须加装双向计量电表。目前，配电网中的电力传输仍以单向为主，即从电网到终端用户，而双向电表普及度不高。安装智能电表后，可在关口电表中对桩端计量数据进行实时核减，为计量电动汽车未来放电平衡本地负荷或上网的电量与计费提供可能。

除了负荷监测和双向电量计量外，有序充电和V2X还需要在配电网侧配套加装通信线路、控制设备等，而这些设备的更新改造也视具体应用场景、技术路线、软件平台和物理通信选择而异。

**大数据与人工智能应用：** 在有序充电和V2G实现与推广过程中，有效收集各类型小区、写字楼、商业区等不同

区域的负荷数据、海量出行与充电需求数据，以及不同车型的充放电数据等，可以满足有序充电的实时分析和精确预测的需要。同时，为满足不同地区差异化的充电及放电需求，需要通过海量数据采集、人工智能技术，自动生成“一用户一策略”，加速有序充电的规模化推广。

负荷监测与智能电表的安装也使得大数据收集分析成为可能，结合基于人工智能、区块链的虚拟电厂智能控制，车网协同策略将更为自动化、精细化。

### 4.3.3 电池侧——动力电池衰减与车辆质保

目前的动力电池主要为日常出行而设计，并未考虑其作为分布式储能设施的情况。V2X工况下，电池频繁充放电不仅增加了使用次数，也可能由于充放电深度、充放电倍率而加剧电池衰减。对电池寿命的担忧以及电池更换带来的额外成本，是影响整车生产企业、用户对V2X接受度的重要阻碍。因此，V2X除了保证车辆出行刚需，也需要增加保护电池寿命作为约束条件。

电池寿命衰减受温度、充放电深度、充放电倍率、电池一致性等因素影响。因此，在车网协同操作中，需要充分考虑充放电深度、充放电倍率变化对动力电池寿命衰减的影响。不同车网协同的应用场景下，动力电池实际充放电工况也有所不同，对衰减的影响也存在差异。例如，美国电力市场中的一次调频、爬坡（协助集中式可再生能源消纳）等辅助服务，作为典型功率型服务，持续时间较短，多在1小时以内，因此，动力电池放电深度相对较浅（国际可再生能源署2018）。相反，需求响应“调峰”服务作为电量型服务，有时会持续较长的时间，如4小时左右。如果参与V2X调度的车辆数有限，会增加电池放电深度，甚至产生过度放电的风险——即便对常规的集中式储能而言，也仅能支撑4小时放电。所以，有必要结合车网协同的应用场景，定制电池控制策略，或选择电动汽车适合参与的应用场景（见表21）。

表 21 | 国际车网协同不同应用场景对响应时间、持续时长的要求

|   | 目的 | 要求  |   |   |
| --- | --- | --- | --- | --- |
|   |   |  响应时间（分钟） | 持续时长（分钟） | 参与频率  |
|  配网 | 局部削峰填谷 | - | 15 ~ 120 | 经常  |
|   |  本地备用电源 | - | 60以上 | 不经常  |
|  全网 | 一次调频 | 0 ~ 0.5 | 0.5 ~ 30 | 经常  |
|   |  二次调频、备用 | 5 ~ 240 | 30 ~ 240 | 经常  |
|   |  需求响应 | 5 ~ 240 | 60 ~ 240 | 经常  |

来源：国际可再生能源署 2018、Cenex 2018

中国电动汽车与电网协同的路线图与政策建议

47

**电池管理系统（BMS）将扮演重要角色：**未来，随着对动力电池性能与衰减情况的更深入了解，电池管理系统可对V2X造成的衰减进行有效控制。研究表明（Uddin et al. 2017 & 2018），在电池管理系统（BMS）的有效控制下，持续浅充浅放不仅不会加速电池衰减，反而可能使电池超过其设计寿命。作为对照，在没有BMS优化的情况下，以最大化削峰填谷收益为目标进行的V2X会加速动力电池衰减。然而，如果利用BMS对削峰填谷服务进行智能管理——即控制车辆日行驶用电21%~38%SOC，此后随即参与V2X放电8%~40%SOC左右，动力电池的寿命会比仅用于日常出行时寿命更长。

除电池寿命管理外，动力电池在V2X模式下的安全策略、热管理也同样需要在车辆研发过程中调整，进行故障防护、自燃事故预防，以实现更高的安全性及经济性。

**未来固态电池技术可能延长电池循环寿命：**随着动力电池技术的演进，电池循环寿命会有所提高，未来V2X频繁充放电对电池衰减的影响可忽略不计。

现阶段，车载动力电池的循环寿命呈下降趋势，可能会影响车辆提供V2X的应用场景与频次。目前，主流的磷酸铁锂电池单体寿命可达4000次，而乘用车主要采用的三元锂电池（NCM523）单体寿命超过2000次，最新的

三元锂电池（NCM811）单体寿命则为1500次左右（见表22）。没有电池管理系统优化时，搭载三元锂电池的纯电动乘用车能够提供的V2X次数有限。

然而，根据《节能与新能源汽车技术路线图》，2030年动力电池系统寿命将从2000次上升到3000次；同时，未来固态锂电池的应用推广也有望大幅提升动力电池的循环寿命（起点研究 2019）。这为纯电动汽车自由参与多种V2X服务提供了技术可行性。

**电池衰减与车辆质保的关联：**V2X对动力电池衰减的潜在影响导致车辆生产企业对车辆成本的担忧，因而大多数汽车生产企业选择不对量产车型提供对V2X的支持。目前，仅有日产聆风（Leaf）等少数量产车型支持V2G，国内吉利、威马的部分纯电动汽车已支持V2G，而丰田、宝马、奔驰等多数车企，则在测试车型上推出允许放电的车型，以适应V2X试点项目的需要。在未来，车辆生产企业对V2X的积极性与市场大众的接受度、商业模式紧密相关（P&GE 2018）。

未来，电动汽车如果支持双向充放电，车辆质保体系也将发生变化。当前主流的车辆质保体系主要与行驶里程或购买年限挂钩，没有与充放电次数、放电深度挂钩（P&GE 2018）。作为少数支持V2X的量产车型，日产

表 22 | 动力电池单体与系统性能发展趋势

|  电池类型 | 单体能量密度（Wh/kg） | 单体循环寿命（次）  |
| --- | --- | --- |
|  锰酸锂电池（LMO） | 140 | 2000  |
|  磷酸铁锂电池（LFP） | 180 | 4000  |
|  三元锂电池（NCM523） | 220 | 2000  |
|  三元锂电池（NCM811） | 270 | 1500  |
|  固态锂电池 | >350 | 未知  |
|  锂空气电池 | >600 | 未知  |

来源：中国汽车技术研究中心调研

说明：固态锂电池和锂空气电池正在研发中，实际的循环寿命和能量密度仍未知。

|   | 2020年 | 2025年 | 2030年  |
| --- | --- | --- | --- |
|  系统比能量（Wh/kg） | 260 | 300 | 350  |
|  系统寿命（次） | 2000 | 2000 | 3000  |
|  系统成本（元/Wh） | 1 | 0.9 | 0.8  |

来源：节能与新能源汽车技术路线图

48

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

聆风的电池质保体系与放电量挂钩，要求车辆每天放电在5kWh内；而国内吉利、威马的部分纯电动汽车要求在每辆车每天放电20kWh内的使用条件下，提供5年质保。未来，如果越来越多的电动汽车品牌开始支持双向充放电，其质保体系也需要调整为与放电频次、放电深度相关。

## 4.4 用户接受度分析

由于整车生产企业、充电运营商、电网企业多以“用户为中心”，所以电动汽车用户对车网协同的便利度、使用成本与收益的接受程度，是影响电动汽车参与电网协同的决定性因素。目前，有序充电和V2X对中国用户仍为新鲜事物。现阶段电动汽车推广还存在里程不足、里程焦虑、充电桩数量有限等挑战，而车网协同对动力电池寿命以及用户出行刚需的更进一步影响，可能会抑制用户接受度。

**有序充电的用户接受度：**调查显示，有序充电的用户接受度整体要高于V2X的接受度（自然资源保护协会2018）。其中，基于峰谷电价的有序充电，用户接受度更高；而当电动汽车用户参与受智能控制的有序充电时，由于缺乏相应的经济激励措施，积极性相对有限（见表23）。因此，未来推广有序充电时，需要采用价格激励与智能控制“双管齐下”的措施。

**双向充放电的用户接受度：**相较之下，双向充放电的整体用户接受度有限，也因用户类型与应用场景而异。日常运时间久的车辆参与V2X的可能性很低，如出租车、网约车、公交车等；出行时间短、出行规律、大部分时间处于停车状态的车辆参与V2X的可行性更高，如校车、公务车、私家车等（见图21）。此外，一些对运营成本、收益敏感的车辆类型，如城市轻型物流车，也具备参与V2X的潜力。若V2X技术和商业模式更清晰，可能会更好地激发负荷集成商如物流企业参与的积极性。

表 23 | 有序充电不同措施效果比较

|   | 智能控制 | 峰谷电价 | 峰谷电价+智能控制  |
| --- | --- | --- | --- |
|  用户参与度 | 偏低 | 高 | 高  |
|  效果1：本地负荷优化程度 | 更优化 | 优化程度有限 | 更优化  |
|  效果2：可再生能源（风能）消纳程度 | 消纳程度更理想 | 消纳程度有限 | 消纳程度更理想  |

说明：可再生能源消纳未讨论太阳能的消纳，是因为目前终端电价的峰谷机制与光伏出力时间耦合度较低，不存在比较的基础。

图 21 | 不同车型一天内出行时间对比及对V2X潜在接受程度差异

![img-33.jpeg](img-33.jpeg)

说明：根据文献总结。

中国电动汽车与电网协同的路线图与政策建议

49

1

第五章

# 未来车网协同路线图
与相关建议

中国推广车网协同需要结合电力市场改革、电池成本下降等外部条件，以及电动汽车自身优势，分步地探索适宜的应用场景。一方面，虽然中国势在必行的电力市场改革将为车网协同释放更多商业“红利”，但电力市场改革过程的未知性与地域间差异也为电动汽车参与电力市场增添了不确定性（见专栏八）。另一方面，不同车网协同应用场景对电动汽车的需求也存在差异，且电动汽车面临的政策保障、技术阻碍也有区别（见表24）。综合考量制度保障、技术标准阻碍，车网协同需要分近期和中远期两步实施（见图22）：

近期（2025年之前）：电动汽车可充分发挥其负荷灵活的优势，在用户侧削峰填谷、分布式光伏充电以及需求响应与调峰辅助市场（填谷）发挥作用：

首先，电动汽车通过有序充电削峰填谷、缓解局部配变扩容具有现实意义，特别是在住宅小区或采用快充的公共场所，存在规模化推广的需求。配套电网建设与改造成本过高，且相关成本会反映到电网输配电价，造成全社会用电成本的上升；而电动汽车有序充电与配电网扩容投入相比，前期投入成本低，是最经济且行之有效的选择。另外，随着光伏组件成本不断下降，在采用工商业目录电价的场所安装分布式光伏设备为电动汽车充电的模式，也能降低电动汽车集中充电对电网的冲击，节省用户电费支出。

其次，电动汽车作为负荷侧灵活资源，有条件参与需求响应市场、特定调峰辅助服务市场和电力现货试点。随着大比例可再生能源接入，电动汽车参与电

力系统“填谷”的需求也不断增加，特别是电动汽车的主要充电时间与风电出力大的夜间（或春节期间）高度重叠，有助于缩小电网峰谷差，促进风力消纳。

- 需求响应市场：市场准入门槛相对较低——一般需要几十辆电动汽车参与即可满足准入要求。针对需求响应的两种响应方式——以人工参与方式（通过手机APP、即时通信软件接收响应邀约）或自动响应方式（通信设备基于通信协议接收响应邀约）参与需求响应，目前，电动汽车负荷集成商以人工方式接受响应邀约的居多，技术门槛不高。未来，随着电力需求响应信息交换规范的推出，电动汽车负荷集成商也能够自动响应邀约，实时地参与需求响应。
- 调峰辅助服务市场：电动汽车还可通过参与调峰辅助市场“填谷”。例如，华北调峰辅助市场明确允许负荷侧电动汽车（及充电桩）作为市场参与主体，辅助可再生能源消纳（国家能源局华北监管局 2019）。与需求响应市场相比，调峰辅助服务市场对车辆数量和持续时长要求较高，仅有大型负荷集成商（如成规模的充电运行商或电网企业）有条件参与。
- 现货市场：在广东现货市场中，大型电动汽车充电站正参与电力现货市场试运行，而广东省也在有意识地培养一批创新的车网互动服务企业。目前中国8个电力现货市场已经启动试运行，在这些现货市场中，电动汽车有条件在市场试运行之初就参与现货市场交易，提供现货平衡。

中国电动汽车与电网协同的路线图与政策建议

51

图 22 | 中国电动汽车与电网协同路线图

■ 电动汽车储能功率 (GW) ■ 电动汽车储能电量 (GWh)

![img-34.jpeg](img-34.jpeg)

■ 存在阻碍

有序充电规模化推广

V2G试点示范

|  应用场景 | 有序充电规模化推广 | 有序充电规模化推广 | 有序充电规模化推广 | 有序充电规模化推广 | 有序充电规模化推广 | 有序充电规模化推广  |
| --- | --- | --- | --- | --- | --- | --- |
|  应用场景 | ·削峰填谷、缓解配网增容 | ·分布式光伏充电 | ·需求响应 ·调峰辅助服务 ·现货市场平衡 | ·调频辅助服务 ·调峰辅助服务 | ·现货市场平衡 ·爬坡辅助服务 ·备用辅助服务 | ·缓解输电线路阻塞  |
|  电力价格与市场机制阻碍 | ·缺乏终端峰谷电价机制或其他经济激励 | - | - | ·调频市场存在参与主体及准入门槛限制 | ·电力现货市场尚未成熟运行和全面推广 ·爬坡辅助服务未推出 | ·电力现货市场节点电价尚未成熟运行和全面推广  |
|  并网限制 | - | - | - | 有限制 | 有限制 | 有限制  |
|  协议标准阻碍 | ·用户自发响应峰谷电价，无技术门槛 ·充电标准稍作优化可支持直流有序充电 | - | ·人工响应，无技术门槛 ·自动响应受标准制约 | ·充电标准不支持V2X | ·充电标准不支持V2X | ·充电标准不支持V2X  |
|  对动力电池的影响 | - | - | - | 可能有影响 | 可能有影响 | 可能有影响  |

来源：电动汽车储能预测来源于国家发展和改革委员会能源研究所与国家可再生能源中心 2017

说明：1. 电动汽车能够提供的储能电量通过电动汽车数量、单车电池容量计算，为电动汽车所能提供的储能电量的上限。

2. 本网协同应用场景中，不同颜色代表不同推广时间阶段，红色（■）代表近期，橙色（■）代表 2025 年左右，绿色（■）代表 2025 年后。

3. 虽然电动汽车能够以 V2B 方式提供削峰填谷、需求响应服务，但对动力电池衰减可能产生影响且用户接受度有限，在近期缺乏推广的基础，因此未予以考虑。

52

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

表 24 | 车网协同应用的适用场所

■ 车网协同适宜场景 ■ 潜在场景 □ 不适宜场景

|   | ■ 削峰填谷、延缓配网扩容 | ■ 分布式光伏充电 | ■ 需求响应 ■ 调峰 | ■ 自动发电控制 | ■ 现货市场电力平衡 ■ 一次调频 ■ 爬坡辅助服务  |
| --- | --- | --- | --- | --- | --- |
|  场所类型1 住宅小区 |  |  |  |  |   |
|  场所类型2 政府、企事业单位办公和商业场所 |  |  |  |  |   |
|  场所类型3 大型工业园区 |  |  |  |  |   |
|  场所类型4 城市公共快充站 |  |  |  |  |   |
|  场所类型5 长时间停留的公共停车场（P+R、机场） |  |  |  |  |   |
|  场所类型6 城市物流或公交场站 |  |  |  |  |   |
|  场所类型7 校车、公务用车、分时租赁车的充电桩 |  |  |  |  |   |

■ 调频辅助服务市场：随着电动汽车在以上领域应用的成熟，可以试点形式允许其以第三方独立辅助商身份加入调频辅助市场，进行技术与经济可行性验证。

以有序充电的方式参与负荷侧削峰填谷、需求响应及调峰等服务，所适用的场所多元。除车辆周转率高的公共交通场站、物流场站外，住宅小区、企事业办公场所、工业园区、公共充电站（桩）等均有条件参与（见表 24）。

**中远期（2025年以后）：**随着电力市场改革释放更多的红利，以及动力电池成本的下降与寿命的提升，电动汽车可进而发挥其储能与分布式电源的作用，结合微电网、虚拟电厂等试点平台，以V2X方式提供调频、现货电力平衡、爬坡服务，争取在2025—2030年形成具有示范意义的项目与模式。

对比传统抽水蓄能等储能设施以及火电机组，电动汽车具有快速功率输出与精准跟踪能力，在一次调频、自动发电控制（也称“二次调频”）、爬坡辅助服务、实时现货电力平衡等应用领域具有独特优势，可以弥补传统火电机组或抽水蓄能的不足。由于这些应用领域对响应时间、响应精度要求高，且频繁充放电也对动力电池寿命有影响，所以，有必要开展V2G试点进行技术验证。然而，电动汽车V2G在缓解输电线路阻塞等应用领域的技术优势不明显，其参与的必要性需再做讨论。

由于目前中国电力现货市场已经进入试运行阶段，而辅助服务市场的改革也将成为必然，电动汽车可以虚拟电厂等方式，通过充放电方式参与现货、辅助电力市场。特别是在公务车、校车、分时租赁车、城市物流车（备用车）等车辆使用强度不高的公共领域（见表 24），可以启动

中国电动汽车与电网协同的路线图与政策建议

53

若干V2G试点，争取在2025—2030年形成具有示范意义的项目与模式。

路线图中规划的有序充电推广与V2G试点示范开展，需要政府部门与行业协会发挥重要的制度“解锁”作用，通过优化政策制度和出台技术标准，提升车网协同的商业潜力与公共接受度。以下将分别对有序充电推广和V2G试点面临的阻碍，提出相关政策建议（见表25）。

表 25 | 推广车网协同的主要阻碍、政策建议与重要程度汇总

|   | 主要阻碍 | 政策建议 | 重要程度  |
| --- | --- | --- | --- |
|  有序充电  |   |   |   |
|  政策与制度 | 终端用户峰谷电价机制： 部分地区没有居民、工商业的峰谷电价，且受充电服务费、转供电加价影响，峰谷电价传导不畅 | 地方发展和改革部门： ·设置电动汽车（充电桩）专用的峰谷电价 ·提供有序充电设施的建设补贴及交流桩的直流改造费用 ·公共充电设施采购中优先要求采购支持灵活智能充电的设施 ·允许充电运营商通过中长期、现货、调峰和需求响应等电力市场购电或提供相关服务 | 高  |
|  技术与标准 | 车-桩-网通信协议： ·“车-桩”间协议：交流充电协议为支持有序充电所需的改动较大，直流充电协议所需的改动较小 ·“桩-网”间协议：缺乏国家标准，仍需探索不同的实施主体和技术途径下，支持有序充电的通信协议 | 标准制定机构： ·优先修订直流充电国家标准《电动汽车非车载传导式充电机与电池管理系统之间的通信协议》（GB/T27930—2015），支持直流有序充电 | 高  |
|   |   |  地方住房和城乡建设部门、发展和改革部门： ·鼓励物业企业与业主委员会积极配合，引导不同主体（电网企业、充电运营服务商）参与有序充电 | 高  |
|   |   |  标准制定机构、整车生产企业、充电设备制造商： ·委托第三方机构对不同品牌车辆、充电桩的接口标准执行情况进行检测验证，作为市场准入前提 ·鼓励整车生产企业或充电设备制造商在生产中提供软件更新接口，通过低成本的软件更新方式，支持有序充电 | 高  |
|   |   |  地方住房和城乡建设部门、发展和改革部门、负荷集成商： ·鼓励推广小功率直流桩替代交流桩，实现直流有序充电 | 中  |
|   |   |  负荷集成商： ·延续目前第三方信息采集的方式（用户手动输入或接入车端远程监控平台），获取必要信息，实现交流有序充电 | 低  |
|   |   |  发展和改革部门、电网企业： ·鼓励配电网运营商分享本地电动汽车充放电负荷上限等处理后、非敏感信息 | 中  |

54

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

表 25 | 推广车网协同的主要阻碍、政策建议与重要程度汇总（续）

|   | 主要阻碍 | 政策建议 | 重要程度  |
| --- | --- | --- | --- |
|  V26  |   |   |   |
|  政策与制度 | 电力市场完善程度与准入门槛： 中国电力市场的市场机制有待完善，正经历全面的改革过程——缺口包括竞争性市场机制、市场参与主体范畴、市场准入门槛 | 国家及地方发展和改革部门、能源部门： ·调频辅助服务：可先以试点形式放宽对电动汽车的限制 ·需求响应、调峰、中长期市场：现阶段，鼓励电动汽车作为负荷，参与需求响应、调峰辅助服务及中长期市场、促进可再生能源消纳 | 低  |
|   |  用户侧资源接入电网的管理要求： 《分布式发电管理办法》（国家能源局 2018）中未明确电动汽车是否属于分布式发电系统范畴。与分布式光伏、热电冷热联供等分布式发电系统不同，政府部门与电网企业尚未建立关于电动汽车发电接入配电网的运行制度和机制 | 国家及地方发展和改革部门、能源部门： ·制定电动汽车（及充电桩）接入电网的技术标准、工程规范和相关流程及管理意见 | 中  |
|  技术与标准 | 车·桩·网通信协议： ·“车·桩”网协议：国家标准不支持V2X ·“桩·网”网协议：缺乏国家标准，仍有待探索不同的实施主体和技术途径下，支持V2X的通信协议 | 国家及地方发展和改革部门、能源部门等： ·提供科研资金或政策支持V2G试点，对技术可行性与经济可行性进行论证 | 中  |
|   |   |  中国电力企业联合会： ·研究基于直流充电的双向充放电通信标准，并验证直流充电标准对调频等高精度服务的支持程度 | 中  |
|   |  电池衰减： V2X可能加速动力电池衰减 | 整车生产企业、电池生产企业、研究机构： ·测试车网协同工况下的动力电池衰减情况，优化电池管理系统及相关充放电策略 | 中  |

中国电动汽车与电网协同的路线图与政策建议

55

## 5.1 关于推广有序充电的建议

有序充电推广遇到的主要阻碍为：一是商业模式缺失，虽然基于有序充电的削峰填谷已具一定经济性（见第4.1.1节），但目前峰谷电价覆盖范围有限、执行不彻底，导致参与有序充电各方无法覆盖投资成本并获利。二是车-桩间充电标准不支持交流有序充电，这与有序充电的部分需求场景（如住宅小区）脱节。化解这些问题需要政府部门与行业协会提供政策保障机制：

首先，为构建有序充电的商业模式，除了有序充电的发起方（电网企业、充电服务运营商）通过技术创新和规模化量产方式，降低相关设备的前期投资成本外，更重要的是保障有序充电的发起方与电动汽车用户能够获得足够的经济激励。具体措施包括终端峰谷电价机制以及其他激励措施：

### （1）终端峰谷电价机制：考虑针对单独报装、电网直供电的充电设施，出台电动汽车专用充电电价：

- ■ 针对电动汽车的峰谷电价机制：目录电价覆盖面广，仅为推动车网协同而推行峰谷电价并不现实。由于电动汽车用户具有单独报装的条件，城市发展和改革部门可针对直供电、单独计量的电动汽车充电桩——如住宅小区私人桩，专门设计一套针对电动汽车的峰谷电价体系。同时，与目录峰谷电价相比，电动汽车充电电价可进一步加大峰谷差。
- ■ 针对公共桩转供电加价、充电服务费影响峰谷电价传导的问题：地方发展和改革部门应要求：一是商业场所、写字楼的公共充电桩终端安装“核减表”，并加强转供电加价的监督举报机制；二是要求充电费与电价分离，引导充电服务费按照峰谷费方式收取。

### （2）除峰谷电价外，其他行之有效的措施还包括政府补贴、公共充电设施采购要求，以及允许充电运营服务商参与现货、调峰和需求响应等电力市场（见专栏七）：

- ■ 通过充电站（桩）的建设补贴引导对有序充电的投资：在推广初期，地方政府可为有序充电的前期建设投入提供补贴。目前，地方补贴正从购置环节向充电站（桩）建设环节转移，这部分补贴可优先补贴特定场景下的有序充电建设投入（如对住宅小区等配变开放容量不足地区的交流桩进行小功率直流改造、公共充电站的柔性有序充电设备投入等）。为创造公平的市场环境，地方补贴应无差别地支持电网企业、充电服务运营商等。

- ■ 公共充电设施采购中要求优先采购支持有序充电的设施：在有序充电推广早期，地方政府还可通过采购政策，率先以政府采购的公共充电桩为试点，逐步在公共充电站（桩）中扩大有序充电的推广范围。

- ■ 允许充电运营商通过在中长期、现货、调峰辅助服务和需求响应等电力市场中购电或提供相关服务：地方发展和改革部门、能源部门可允许充电运营商作为售电企业参与中长期电能量市场交易，并通过放宽需求响应市场或调峰辅助市场的准入门槛，让电动汽车提供“填谷”服务。在现阶段现货市场试运行中，应允许充电运营商参与。

其次，为克服“车-桩”间交流充电标准的缺失问题，以及“桩-网”间标准化通讯协议的空白，提出以下建议（见表26）：

### （1）针对车-桩间充电通信协议：

- ■ 优先修订直流充电国家标准《电动汽车非车载传导式充电机与电池管理系统之间的通信协议》（GB/T27930—2015），支持直流有序充电。
- ■ 对交流充电桩，优先考虑以下两种弥补措施，但若两种方式的用户体验不良或商业模式不佳，则有必要考虑对现有交流充电通信接口与协议进行较大修改：一是允许负荷集成商以手机APP等方式采集必要的车辆状态信息，或允许负荷集成商通过整车生产企业或者国家的车辆远程监控平台获取所需的车辆状态信息，以实现交流有序充电。二是以补贴等形式，鼓励配电开放容量有限的住宅小区业主或有序充电实施单位对既有私人交流桩进行小功率直流桩改造，或新建小功率直流桩。
- ■ 为推广有序充电和双向充放电应用，建议第三方机构对不同品牌车辆、充电桩的接口标准执行情况进行检测验证，以此作为市场准入的标准。鼓励整车生产企业或充电设备制造商在生产中提供软件更新接口，通过低成本的软件更新方式支持有序充电和双向充放电。

### （2）针对桩-网间通信协议：充电运营商为主导与配电网运营商为主导的两种有序充电实施方式对通信协议和通信接口的要求不同，是否有必要制定国家标准，仍有待实施主体、商业模式和市场规模更明确后再讨论。目前可以：

- ■ 以试点形式鼓励物业企业与业主委员会积极配合有序充电试点推广；鼓励不同主体探索多种有序充电技术实现方式，为标准制定做铺垫（见附录二）。

56

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

■ 鼓励配电网运营商在电网运营安全的前提下，分享分析处理后的结论信息，如本地配电网充电负荷上限等，支持多元化实施主体参与创新。

表 26 | 有序充电所涉及的软件、硬件和通信协议升级

|  充电方式 | 车-桩通信协议 现状与改进建议 | 桩-网通信协议 现状与改进建议  |
| --- | --- | --- |
|  交流 | **现状：**国家标准不支持 **建议：** - ■ 负荷集成商：延续目前第三方的信息采集方式（用户手动输入或接入车端远程监控平台），获取必要信息，实现交流有序充电 - ■ 住房和城乡建设部门、发展和改革部门、负荷集成商：鼓励推广小功率直流桩，进行交流桩替代，实现直流有序充电 - ■ 标准制定机构、整车生产企业：建议第三方机构对不同品牌车辆、充电桩的接口标准执行情况进行检测验证；鼓励整车生产企业或充电设备制造商在生产中提供软件更新接口，通过低成本的软件更新方式，支持有序充电和双向充放电 | **现状：**由服务提供商自行定义，尚无标准 **建议：** - ■ 住房和城乡建设部门：鼓励物业企业与业主委员会积极配合，引导不同主体参与有序充电试点，为公平地制定标准奠定基础 - ■ 电网企业：鼓励配电网运营商分享分析处理后的本地配电变压器信息，支持多元化实施主体参与创新  |
|  直流 | **现状：**国家标准有待优化 **建议：** - ■ 标准制定机构：优先修订直流充电国家标准《电动汽车非车载传导式充电桩与电池管理系统之间的通信协议》（GB/T27930—2015），给予负荷集成商对车辆更多的控制权 |   |

## 专栏 7 | 国际推广有序充电的政策经验

虽然有序充电具备规模化推广的现实意义与必要性，但无论在中国还是欧美国家，商业模式与标准的缺失是推广有序充电最主要的障碍。

国际上，为了将有序充电从少数试点项目向规模化应用推广，主要采取的措施包括峰谷电价、政府补贴、政府采购要求与标准强制（加利福尼亚州能源局 2019、Agora Verkehrswende 2019、英国交通运输部 2019）。例如：

- ■ 强制性标准：英国交通运输部正在研究，要求近期所有新增的非公共充电桩支持有序充电。为此，英国计划在其标准化机构（British Standards Institution）制定的标准中，强制所有充电桩设备在生产和出厂认证中安装并确认其具备智能控制设备（Energy Smart Appliance），以支持有序充电。未来，英国计划通过智能电表（Smart Meter）控制充电桩的充电负荷，并通过这一技术路径实现有序充电、V2G及多种应用场景（如负荷侧削峰填谷、需求响应、隔墙售电等）。
- ■ 政府补贴与采购要求：加利福尼亚州能源局正在研究，在电动汽车峰谷电价基础上，对公共事业局和配电网运营商建设的公共充电桩予以更多的建设资金支持，或借助政府采购的方式提高其对有序充电的支持。

中国电动汽车与电网协同的路线图与政策建议

57

## 5.2 关于推广V2G试点示范的建议

由于目前中国电力现货市场已经进入试运行阶段，而辅助服务市场的改革也将成为必然，电动汽车可以V2G方式参与现货、辅助电力市场。特别是在公务车、校车、分时租赁车、城市货运车（备用车）等车辆使用强度不高的公共领域，可以启动若干V2G试点，争取在2025—2030年形成具有示范意义的模式，为后期推广奠定基础。相关建议如下：

首先，应本着“试点先行”的原则，以科研资金或国家示范项目等形式，支持电网企业、电力用户（如楼宇业主或工业园区）、充电运营服务商、整车生产企业与研究机构共同参与V2G试点示范，开展技术可行性与经济可行性的论证，为标准制定和制度设计提供基础：

- 探索多元的V2G技术路径：以直流充放电为突破口，探索不同实施主体下充电桩—充电运营服务商—电网间的通信接口与信息交互内容，研发V2G智能优化软硬件系统。
- 探索V2G项目的经济可行性与利益分成机制：验证电动汽车V2G参与全网服务的商业可行性，探索不同参与方之间合理的利益分成机制。
- 鼓励负荷集成商加强技术储备：面对未来电力市场价格波动性与电力市场的绩效考核，负荷集成商作为V2G的实施主体，需要积累用户出行、充电行为的大数据并进行分析，精确预测V2G转移电量，同时纳入对气象及可再生能源出力的预测机制，让电动汽车能够更主动地参与可再生能源的消纳。

第二，发展和改革部门、经济和信息化部门与电力调度机构应对电动汽车并网、参与电力市场交易做出更明确的管理要求：

- 电力市场准入的放宽：首先，分步放宽对电动汽车的准入限制；现阶段，对电动汽车作为灵活负荷参与现货和辅助服务电力市场，应放开限制。对电动汽车以放电形式参与电力市场，特别是调频辅助服务市场，可先以试点形式参与，在效果得到验证后，再全面允许其参与。其次，以绩效为依据，将电动汽车负荷集成商的准入资质与其绩效考核结果挂钩，建立“有进有出”的准入与退出机制。

- 电动汽车并网的监管：首先，在2018年版《分布式发电管理办法》中，明确电动汽车（及充电桩）作为分布式发电系统的定位。其次，制定电动汽车（及充电桩）接入电网的技术标准、工程规范和相关流程及管理办法，保证电动汽车接入电网在计量、数据传输、电能质量等方面要满足的要求。最后，针对电动汽车能否无障碍、无歧视地上网出台相关管理意见，明确电动汽车放电全额上网、全部自用、余电上网的前提条件。

第三，标准制定机构及时修订或重新制定车-桩-网间的通信接口和协议，以支持电动汽车双向充放电（见表27）：

- 车-桩通信标准：优先修订直流充电国家标准《电动汽车非车载传导式充电机与电池管理系统之间的通信协议》（GB/T27930—2015），支持电动汽车的直流双向充放电，验证该标准支持调频辅助服务的可靠性。
- 桩-网通信接口与标准：有必要探索不同的实施主体和技术途径下，充电桩-充电运营服务商-电网间的通信接口、信息交互内容与流程，并适时制定相关标准；鼓励配电网运营商在电网运营安全的前提下，分享分析处理后的配电变压器信息，如本地配电网允许返送电功率的上限等，支持多元化实施主体参与创新。

表 27 | V2G所涉及的车-桩-网间通信协议升级

|  充电方式 | 车-桩通信协议现状与改进建议 | 桩-网通信协议现状与改进建议  |
| --- | --- | --- |
|  交流 | 现状：国家标准目前不支持 | 现状：尚无相关标准  |
|  直流 | 现状：国家标准目前不支持 建议： 标准制定机构：优先研究基于直流充电的双向充放电通信标准，并验证直流充电标准对调频等高精度服务的支持度 | 建议： 电网企业、充电运营服务商、研究机构等：开展V2G试点，鼓励不同主体参与，探索不同技术途径下充电桩-配电网-电力调度机构之间的通信接口、通信架构、功能规范、信息交互内容与流程 电网企业：鼓励配电网运营商分享分析处理后的本地配电变压器信息  |

58

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

第四，整车生产企业、电池生产企业与研究机构应开展车网协同工况下的动力电池衰减测试，结合动力电池运营监控平台及大数据分析，优化电池管理系统及相关充放电策略。

## 专栏 8 | 中国电力市场未来可能改革方向

随着市场改革推进，中国电力市场将突破目前的管制约束，形成更为合理的市场机制。未来电力市场的格局也将与现在有所不同：随着现货电力市场的形成与市场竞价机制的建立，需求响应市场、调峰辅助服务可能将被并入现货市场，无偿服务如一次调频和基本调峰将有望逐步转成有偿服务。随着可再生能源发电占比的提升，针对实时电力平衡的新型辅助服务，如协助集中式光伏并网的“爬坡”产品，将会推出（见专栏表2）。

然而，不同地区间电力市场改革路线会有所区别。例如，由于现货市场改革进程的地域差异，一些区域电力市场可能选择将电储能和负荷侧资源纳入调峰等辅助服务市场，而一些改革先行地区可能选择将调峰辅助服务直接并入现货市场。这意味着在不同区域电力市场下，车网协同可以参与的应用场景及其经济效益将有所差别，负荷集成商仍需要探索区域化的车网协同路径。

### 专栏 2 | 中国电力市场未来可能改革方向

|   | 中国电力市场改革当前进展 | 中国电力市场未来可能改革方向  |
| --- | --- | --- |
|  中长期电能量市场 | ■ 相对成熟 | ■ 进一步完善：包括增加带电力（功率）曲线的中长期市场交易，与现货电能量市场接轨*  |
|  需求响应市场 | ■ 江苏、上海、河南、天津、山东等已建立需求响应市场 ■ 补偿水平有限，缺乏可持续的付费机制 | ■ 可能根据现货市场价格进行需求响应，或在辅助服务市场中单独开设需求响应市场  |
|  辅助服务市场 | ■ 市场机制不完善 | ■ 一次调频从无偿服务转为有偿服务 ■ 调峰并入现货市场 ■ 新增辅助集中式可再生能源并网与消纳相关的辅助服务（如爬坡服务**）  |
|  现货电能量市场 | ■ 仍在建设与试运行期 | ■ 形成以分时节点电价（或分时分区电价）为基础的交易机制  |

\*说明：带电力（功率）曲线的中长期市场交易以电动车为交易标的，能够支持可再生能源的消纳。目前，中国的中长期市场无法支持可再生能源参与。

\*\*说明：建立类似加利福尼亚州 0400 的爬坡辅助服务，这种对持续时间要求较短，对功率变化率要求较高的辅助服务性会电动汽车的特性。2011 年，0400 在其 0mm 和 5mm 的实时率期引入了一种新的辅助服务产品“灵活爬坡产品”（Fiedler foraging Feeder, FW），灵活爬坡产品和传统的辅助服务产品不同，这种产品的需求和规格不是根据其轨迹一个时期的状态而定，而是依据两个时间点的变化而定。

### 专栏 3 | 中国辅助服务市场未来可能改革方向

|   | 中国辅助服务市场现状 | 未来可能的调整  |
| --- | --- | --- |
|  基本辅助服务 （无补偿） | 一次调频 | 有偿辅助服务  |
|   |  基本调峰：25%至50%额定出力 | 并入现货市场  |
|   |  基本无功调节 | --  |
|  有偿辅助服务 （有补偿） | 二次调频 | --  |
|   |  有偿调峰：深度调峰、启停调峰 | 并入现货市场  |
|   |  旋转备用补偿 | --  |
|   |  有偿无功调节 | --  |
|   |  黑启动 | --  |

中国电动汽车与电网协同的路线图与政策建议

59

BEST COPY

## 附录一

# 内部收益率和投资回收期计算

### 内部收益率

内部收益率代表资金流入现值总额与资金流出现值总额相等，即净现值等于零时的折现率（如下式）。一般情况下，内部收益率大于等于基准收益率（一般项目收益率为8%）时，可认为项目可行。

$$NPV = \sum_{t=1}^T \frac{CF_t}{(1 + IRR)^t} - C_o = o$$

其中：

$NPV$：项目净现值，元；

$CF_t$：项目t年净现金流，元；

$IRR$：项目内部收益率，%；

$C_o$：项目初期投资成本，元；

$T$：项目运行周期，年。

### 投资回收期

除内部收益率外，投资回收期也可直观对比项目经济性水平。投资回收期代表投资项目投产后获得的收益总额达到该投资项目投入的投资总额所需要的时间。虽然有序充电参与峰谷价差调节的能力相比V2G较为有限，但其投资和运维成本都较低，有助于其快速回收成本，即投资回收期短。投资回收期计算公式如下：

$$T_{payback} = \frac{p-n}{p} + n_y$$

其中：

$T_{payback}$：项目投资回收期；

$n_y$：项目现金流为负的最后一年的年份；

$p$：项目累计现金流为正第一年当年现金流，元；

$n$：项目累计现金流为负最后年当年累计现金流，元。

中国电动汽车与电网协同的路线图与政策建议

61

## 附录二

# 车网协同所涉及的软件、硬件升级与改造

无论是实现有序充电，还是实现V2X，均需要对现有电动汽车、充电桩、配电网进行软硬件升级改造。其中，一些改造可通过低成本的软件升级方式实现，如整车生产企业可通过软件更新方式调整车辆充电安全保护，以支持有序充电；而一些改造（如配电网和充电桩的改造）涉及加装硬件设备和通信线路，需要进行硬件改造，见下表。

这些软硬件升级与改造多数与车网协同的实现方式以及通信协议紧密相关，如果能在充电桩、配电网设备的生产中就实现标准化的集成，或鼓励日后以软件升级方式完成更新，就能够最大程度减少后期改造中重复施工等成本。

表 | 车网协同涉及的软件和硬件升级

|  充电方式 | 车辆侧 | 充电桩侧 | 配电网侧  |
| --- | --- | --- | --- |
|  **有序充电**  |   |   |   |
|  交流 | ■ 通过软件升级，加强对充电协议的支持，优化车辆的充电安全保护措施 | ■ 加装设备，接收与处理控制充电负荷的信号 | ■ 配电网侧加装负荷采集器 ■ 部署负荷集成商开发“车-桩-网”智能软件、通信线路和设备，实现对有序充电的智能控制  |
|  直流 | ■ 通过软件升级，加强对充电协议的支持，优化车辆的充电安全保护措施 | ■ 通过加装设备或软件升级，接收与处理控制充电负荷的信号 | ■ 配电网侧加装负荷采集器 ■ 部署充电运营商、负荷集成商或电网运营商开发“车-桩-网”智能软件，配套通信线路和设备，实现对有序充电的智能控制  |
|  **V2X**  |   |   |   |
|  交流 | ■ 安装车载逆变器，并测试车载逆变器是否会对配电网电能质量产生影响 | ■ 加装双向计量设备 ■ 加装设备，接收与处理控制充电负荷的信号 | ■ 加装配电网侧的负荷采集器 ■ 部署充电运营商、负荷集成商或电网运营商开发“车-桩-网”智能软件，配套通信线路和设备，实现对V2X的智能控制  |
|  直流 |  | ■ 加装双向计量设备 ■ 加装变流器 ■ 通过加装设备或软件升级，接收与处理控制充电负荷的信号 | ■ 加装配电网侧的负荷采集器 ■ 部署充电运营商、负荷集成商或电网运营商开发“车-桩-网”智能软件，配套通信线路和设备，实现V2X的智能控制  |

62

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

## 参考文献

1. [1] Agora Verkehrswende 2019. Distribution grid planning for a successful energy transition—focus on electromobility. Conclusions of a study commissioned by Agora Verkehrswende, Agora Energiewende, and Regulatory Assistance Project (RAP).
2. U. S. Department of Energy (美国能源部). Benefits of demand response in electricity markets and recommendations for achieving them: a report to the United State Congress pursuant to section 1252 of the Energy Policy Act of 2005 [R/OL] [2008-02-21]
3. Cenex. 2018, V2G Market Study: answering the preliminary questions for V2G—what, where and how much.
4. PG&E (太平洋煤电公司). 2018. Electric Program Investment Charge—Test Smart Inverter Enhanced Capabilities—Vehicle to Home.
5. Everoze, EVConsult, Innovate UK, UK Power Network. 2018. V2G Global Roadtrip: Around the World In 50 Projects.
6. Brendlinger, J., Campbell, M., Hlivko, J., Kaltenhauser, H., Wechtenhiser, B., Hafer, G., 2017. Environmental quality, energy, and power technology—Task Order 012: Plug-in electric vehicle, vehicle to grid. U.S. air force research laboratory.
7. Wenzel, G., Negrete-Pincetic, M., Olivares, D.E., 2017. Real-time Charging Strategies for an Electric Vehicle Aggregator to Provide Ancillary Services. in IEEE Transactions on Smart Grid. Vol. PP, No. 99, pp. 1-1.
8. California ISO, California Governor’s Office, California Energy Commission, and the CPUC. 2014. California Vehicle-Grid Integration (VGI) Roadmap: enabling vehicle-based grid services.
9. Xu, B., Dvorkin, Y., Kirschen, D.S., Silva-Monroy, C.A., Watson, J.P., 2016. A comparison of policies on the participation of storage in U.S. frequency regulation market. in IEEE Power and Energy Society General Meeting.
10. International Energy Agency (IEA, 国际能源署). 2019. Demand Response: Tracking Clean Energy Progress. https://www.iea.org/icep/energyintegration/demandresponse/
11. California Public Utilities Commission (加利福尼亚州公用事业委员会). 2019. Interconnection Rule-making: working group three final report.
12. California Energy Commission (加利福尼亚州能源局). 2019. California Vehicle Grid Integration Roadmap Update.
13. Department for Transport of U.K. (英国交通运输部). 2019. Electric Vehicle Smart Charging. https://www.gov.uk/government/consultations/electric-vehicle-smart-charging
14. San Diego Gas & Electric (SDG&E). 2014. Final Evaluation for San Diego Gas & Electric’s Plug-in Electric Vehicle TOU Pricing and Technology Study.
15. Uddin K., Jackson T., Widanage W.D., Chouchelamane G., Jennings P.A., Marco J., 2017. On the possibility of extending the lifetime of lithium-ion batteries through optimal V2G facilitated by an integrated vehicle and smart-grid system, Energy, Vol. 133: 710-722
16. Uddin K., Dubarry M., Glick M.K., 2018. The viability of vehicle-to-grid operations from a battery technology and policy perspective, Energy Policy. Vol 113: 342-347
17. 罗卓伟, 胡泽春, 宋永华, 徐智威, 阳岳希, 刘辉. 2012. 大规模电动汽车充放电优化控制及容量效益分析. 电力系统自动化
18. 国网能源研究院. 2018. 电动汽车发展对配电网影响及效益分析. 自然资源保护协会项目报告
19. 国家电网市场营销部. 2013. 电动汽车智能充换电服务网络建设与运营. 北京. 中国电力出版社.
20. 田世明, 王蓓蓓, 张晶. 智能电网条件下的需求响应关键技术 [J]. 中国电机工程学报, 2014, (22): 3576-3589.
21. 国网电动汽车公司. 2019. 全国首例电动汽车参与春节“填谷”电力需求响应试点. https://www.nengapp.com/news/detail/2376108
22. 江苏省经济和信息化委员会, 关于印发《江苏省电力需求响应实施细则 (修订版)》的通知, 苏经信电力 [2018] 477 号
23. 国家发展改革委 国家能源局关于印发《电力中长期交易基本规则 (暂行)》的通知. http://zfxgk.nea.gov.cn/auto81/201908/t20190820_3692.htm
24. 广东省经济和信息化委关于2019年电力市场交易规模安排和市场主体准入的通知. http://www.gdei.gov.cn/ywfl/dlny/201810/t20181004_130572.htm
25. 中国汽车报 2019. 有序充电让电动汽车由“电网负担”变为“电网调控法宝”. https://www.xianjichina.com/news/details_135817.html
26. 薛露露, 夏俊荣, 禹如杰, 任焕焕, 刘勇, 韦围, 刘鹏. 2019. 新能源汽车如何更好地接入电网: 中国新能源车规模化推广对电网的影响分析. 世界资源研究所报告.
27. 中国电力企业联合会. 2019. 2018—2019年度全国电力供需形势分析预测报告.

中国电动汽车与电网协同的路线图与政策建议

63

28. 国家能源局. 2019. 2018年全国可再生能源并网运行情况介绍.
29. 国家能源局. 2019. 2019年第一季度风电并网运行情况
30. 国家能源局. 2018. 关于2018年上半年电力辅助服务有关情况的通报
31. 国家能源局. 2018. 分布式光伏发电项目管理办法（征求意见稿）
32. 国家能源局. 2018年全国电力辅助服务有关情况通报（a）
33. 国家发展和改革委员会. 2017. 关于深入推进供给侧结构性改革做好新形势下电力需求侧管理工作的通知. 发改运行规〔2017〕1690号
34. 国家能源局. 2018. 分布式发电管理办法（征求意见稿）
35. 国电南瑞科技股份有限公司. 2018. 电动汽车有序充电技术及试点应用. 2018年中国电机工程学会年会.
36. 中国电动充电基础设施促进联盟. 2019. 2019年4月全国电动汽车充电基础设施运行情况.
37. 国家发展和改革委员会能源研究所，国家可再生能源中心. 2017. 中国可再生能源展望. 2017.
38. 国家发展和改革委员会能源研究所，国家可再生能源中心，清华大学. 2017. 新能源发电与电动汽车协同发展战略研究. 能源基金会支持项目报告
39. 工业和信息化部. 2014. 日本推出电动汽车家庭供电系统可实现“错峰用电” https://www.dlev.com/news/jishu/35356
40. 国家发展和改革委员会，国家能源局. 2016. 电力中长期交易基本规则(暂行). http://zbxgk.nea.gov.cn/auto81/201908/t20190820_3692.htm
41. 国家能源局山西监管办公室. 2017. 关于鼓励电化学储能参与山西省调峰调频辅助服务有关事项的通知
42. 国家能源局南方监管局. 2018. 电化学储能电站并网运行管理及辅助服务管理实施细则
43. 国家能源局华北监管局. 2019. 第三方独立主体参与华北电力调峰辅助服务市场试点方案（征求意见稿）.
44. 河南省发展和改革委员会. 2019. 关于2019年开展电力需求响应工作的通知
45. 江苏省工业和信息化厅，江苏省发展和改革委员会. 2018. 江苏省电力需求响应实施细则（修订版）
46. 起点研究. 2019. 2019年中国固态锂电池行业研究报告.
47. 中关村储能产业技术联盟. 2019. 中国储能市场发展及预测.
48. 刘坚，金亨美，唐莉，朱肖晶，龚海华. 2018. 电动汽车储能市场及激励机制研究. 自然资源保护协会研究报告
49. 中国电动汽车充电基础设施促进联盟. 2019. 2019年9月全国电动汽车充电基础设施运行情况.

64

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

## 注释

1. 统计中未计入广州市，因为广东省（除深圳外）安装独立电表的充电设施均采用大工业电价。
2. 若计入充电服务费，分布式光伏充电能够节约的充电成本可以更高。
3. 按每户三人计算。

## 致谢

在在本报告的研究与编写过程中，能源和交通领域的众多专家、学者给予了大力支持并提供了宝贵建议，在此，我们向各位专家表示由衷的感谢。

同时，世界资源研究所的各位领导和同事也给予了大力支持和指导。在此特别向世界资源研究所（美国）北京代表处首席代表方莉、副首席代表房伟权、S&R负责人李来来，以及其他各位同事表示诚挚的谢意。

最后，我们要感谢威廉与佛洛拉·休利特基金会（William and Flora Hewlett Foundation）及橡树基金会（Oak Foundation）对本研究提供的资金支持。对本报告做出重要贡献的专家和同事名单如下（排名不分先后）：

|  **刘永东** | 中国电力企业联合会标准化中心  |
| --- | --- |
|  **赵勇强** | 国家发展和改革委员会能源研究所  |
|  **张帆** | 中国电动汽车充电基础设施促进联盟  |
|  **王明才** | 国网电动汽车服务有限公司  |
|  **唐渊** | 中国南方电网广州供电局  |
|  **潘鸣宇** | 国网电力科学研究院  |
|  **周锋** | 全球能源互联网发展合作组织  |
|  **王建斌** | 中国汽车技术研究中心有限公司  |
|  **许晓慧** | 中国电力科学研究院有限公司  |
|  **夏俊荣** | 中国电力科学研究院有限公司  |
|  **龚慧明** | 能源基金会（美国）北京代表处  |
|  **陈健华** | 能源基金会（美国）北京代表处  |
|  **苗红** | 世界资源研究所（美国）北京代表处  |
|  **刘岱宗** | 世界资源研究所（美国）北京代表处  |
|  **袁敏** | 世界资源研究所（美国）北京代表处  |
|  **李相宜** | 世界资源研究所（美国）北京代表处  |
|  **陈晨** | 世界资源研究所能源项目  |

中国电动汽车与电网协同的路线图与政策建议

65

## 作者介绍

**薛露露**是世界资源研究所（美国）北京代表处研究员。

**刘坚**是国家发展和改革委员会能源研究所副研究员

**王颖**是东南大学自动化学院讲师

**刘小诗**是中国电动汽车百人会副秘书长

**熊英**是中国电动汽车百人会研究部副部长

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

Cover 摄图网; pg. i.bj.sgcc.com.cn/国网北京电力公司; pg. vi Flickr/26344495@N05; pg. xiv Unsplash/Dina Lydia; pg. xxii 摄图网; pg. 3 Unsplash/Andreas Dress; pg. 4 Unsplash/Luca Bravo; pg. 13 摄图网; pg. 14 Unsplash/Marc Heckner; pg. 22 Unsplash/American Public Power Association; pg. 30 ifanr/董车会; pg. 50 Flickr/thelastminute; pg. 60 bj.sgcc.com.cn/国网北京电力公司.

66

Action Plans and Policy Recommendations on Vehicle Grid Integration in China

世界资源研究所（WRI）出版物，皆为针对公众关注问题而开展的适时性学术性研究。
世界资源研究所承担筛选研究课题的责任，并负责保证作者及相关人员的研究自由、同时积极征求和回应咨询团队及评审专家的指导意见。若无特别声明，出版物中陈述观点的解释权及研究成果均由其作者专属所有。

Creative Commons

Copyright 2020 World Resources Institute 版权所有
本产品由创用（Creative Commons）4.0许可授权，许可副本参见http://creativecommons.org/licenses/by/4.0/

![img-35.jpeg](img-35.jpeg)

世界资源研究所
WORLD RESOURCES INSTITUTE

世界资源研究所（美国）北京代表处
北京市东城区东中街3号
东环广场写字楼A座7层K-M室
邮编：100027
电话：+86-10 8416 5697
WWW.WRI.ORG.CN

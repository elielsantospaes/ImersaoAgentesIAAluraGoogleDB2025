def generate_get_topics_prompt(article):
    
    TOPICS_PROMPT = f"""
    INSTRUCTION:
    You will receive a text of a scientific paper, that is breaked in some topics and subtopics. Your task is to extract only the name of the topics and subtopics you will be provided in the task:

    EXAMPLES:
    paper_1: '''
    Fishing in the Open Sea: A Comprehensive Investigation
    1. Introduction
    Open sea fishing, also known as deep-sea or offshore fishing, is a practice that involves capturing fish species that dwell far from coastal waters. It plays a crucial role in global food security, economic development, and cultural traditions. Despite its significance, open sea fishing faces numerous challenges, including overfishing, climate change, and regulatory issues. This article explores the complexities of open sea fishing, analyzing current research, investigating ecological impacts, and evaluating fishing techniques used in offshore environments.

    2. Related Work
    Previous research on open sea fishing has predominantly focused on sustainability, technological advancements in fishing gear, and fish population dynamics. For instance, Pauly et al. (2002) emphasized the depletion of fish stocks due to industrial fishing methods, while Watson and Morato (2013) explored the effectiveness of marine protected areas (MPAs) in conserving biodiversity. Several studies have also analyzed the socioeconomic impacts of deep-sea fishing on coastal communities (Béné et al., 2010), and the role of satellite tracking in monitoring illegal fishing practices (Kroodsma et al., 2018).

    3. Investigating the Impact of Fishing Techniques on Marine Ecosystems
    One of the critical areas of concern in open sea fishing is the ecological impact of different fishing methods. Longlining, trawling, and purse seining are widely used, each with distinct consequences on marine habitats and non-target species. This investigation focuses on how these techniques affect bycatch rates, seafloor integrity, and migratory species.

    4. Methodology
    The study employed a mixed-methods approach combining quantitative data analysis and qualitative case studies. Satellite data from the Global Fishing Watch platform were used to map fishing activity across selected regions of the Atlantic and Pacific Oceans. In addition, interviews were conducted with marine biologists, fisheries officers, and local fishermen to gain insight into field practices. Bycatch data and habitat disturbance metrics were collected from published environmental impact assessments and national fisheries reports.

    5. Results
    The analysis revealed that:

    Trawling resulted in the highest level of habitat disruption, with significant damage to benthic ecosystems.

    Longlining showed moderate ecological impact, but high bycatch rates, particularly of seabirds and turtles.

    Purse seining was the most efficient in terms of target catch but contributed to the unintentional capture of juvenile fish and dolphins.
    Regions with strict enforcement of fishing quotas and gear regulations, such as parts of the North Atlantic, showed better ecological outcomes than those with weaker governance.

    6. Discussion
    These findings underscore the need for sustainable fishing practices that balance productivity with ecosystem preservation. While technological improvements in gear design have reduced some impacts, enforcement remains uneven across jurisdictions. Multinational agreements and data-sharing among countries are essential to combat illegal and unreported fishing. Moreover, promoting selective fishing methods and increasing investment in alternative livelihoods can help reduce pressure on open sea resources.

    7. Conclusion
    Open sea fishing is both an opportunity and a challenge. As global demand for seafood continues to rise, the need for ecologically responsible fishing methods becomes increasingly urgent. This article highlights that while significant progress has been made in understanding and managing offshore fishing, coordinated global action and ongoing research are vital to ensure the long-term sustainability of marine ecosystems and the communities that depend on them.'''

    output: [
    "1. Introduction",
    "2. Related Work",
    "3. Investigating the Impact of Fishing Techniques on Marine Ecosystems",
    "4. Methodology",
    "5. Results",
    "6. Discussion",
    "7. Conclusion"
    ]

    paper_2: '''1. Introduction
    Noise suppression in headsets has become a key feature for enhancing audio clarity and user comfort in both professional and personal environments. By reducing or eliminating ambient sound, users can experience improved communication, focused listening, and reduced fatigue in noisy settings. Noise suppression is typically achieved through passive noise isolation, active noise cancellation (ANC), or a combination of both. This study investigates the effectiveness of noise suppression in two primary headset designs: intra-auricular (in-ear) and supra-auricular (over-ear) models, evaluating performance across different acoustic environments.

    2. Approach
    The approach taken in this study involved both objective measurements and subjective user evaluations. A sample of six commercial headset models—three intra-auricular and three supra-auricular—were tested in controlled acoustic environments simulating office noise, traffic, and human speech. Noise suppression efficiency was measured in decibels (dB) using head and torso simulators (HATS). Subjective feedback was collected through a standardized user questionnaire focused on comfort, perceived noise reduction, and audio quality.

    Each headset was tested under two conditions:

    Passive mode: relying only on physical noise isolation.

    Active mode: with ANC turned on where available.

    Data was collected and averaged across multiple sessions for statistical consistency.

    3. Results
    The results indicate varying levels of noise suppression performance based on headset design and use of active technologies.

    3.1 Results for Intra-Auricular Cases
    In-ear (intra-auricular) headsets demonstrated strong performance in the high-frequency range, primarily due to their seal within the ear canal. The average noise suppression was:

    Passive mode: 18 dB

    Active mode: 24 dB

    Users reported effective isolation from office chatter and keyboard noise, but less success against low-frequency sounds such as engine hum. ANC effectiveness was more limited due to the smaller hardware size, but provided noticeable improvements in consistent environments.

    3.2 Results for Supra-Auricular Cases
    Over-ear (supra-auricular) headsets provided broader frequency noise suppression, particularly in the low-to-mid frequency range. Average suppression values were:

    Passive mode: 15 dB

    Active mode: 32 dB

    ANC performance was significantly higher in these models, especially against consistent low-frequency noise like air conditioning or traffic rumble. Users noted higher comfort for long-term wear and better suppression in noisy public or transit environments. However, bulkiness was a reported drawback in mobile contexts.

    4. Limitations
    While the study provides valuable insights into the performance of noise suppression technologies, several limitations were identified.

    4.1 Case Size Limitations
    ANC performance is heavily dependent on component size and battery capacity. In-ear models face physical constraints that limit the quality of microphones and signal processing hardware, resulting in lower overall ANC efficiency. Conversely, over-ear headsets can house more advanced components but may sacrifice portability and comfort in hot or physically active settings.

    Other case-related limitations include:

    Reduced battery life for compact models under ANC mode

    Feedback noise or audio coloration introduced by aggressive ANC in small enclosures

    5. Conclusions
    Noise suppression in headsets is a critical factor for modern audio applications, with each design offering distinct advantages. In-ear headsets provide discreetness and high-frequency isolation, while over-ear models excel at full-spectrum suppression, particularly in low frequencies. The choice between the two should consider use case, environment, and comfort preferences. While ANC technology has advanced significantly, its implementation is still constrained by form factor, especially in compact models. Future improvements in low-power processing and miniaturized components may further enhance ANC performance across all headset types.'''

    output: [
    "1 Introduction",
    "2 Aproach",
    "3 Results",
    "3.1 Results for intra auricular cases",
    "3.2 Results for supra auricular cases",
    "4 Limitations",
    "4.1 Case size lilmitations",
    "5 Conclusions"
    ]   


    paper_3: '''Enhancing English Language Learning: Methods, Insights, and Future Directions
    Motivation
    English is the most widely studied second language in the world, serving as a global medium for business, science, education, and diplomacy. As societies become more interconnected, proficiency in English has become a key asset for personal, academic, and professional advancement. However, learners often face challenges such as lack of motivation, ineffective instruction, limited exposure, and difficulty acquiring pronunciation or fluency. This article aims to explore effective strategies for English learning, evaluate current methodologies, and present results from recent approaches to improve engagement and retention.

    Related Work
    Numerous studies have investigated second language acquisition (SLA), with emphasis on cognitive, social, and technological aspects. Krashen’s Input Hypothesis (1985) emphasized the importance of comprehensible input in language acquisition, while Swain (1985) argued for the importance of output in developing fluency. More recent work has explored the use of blended learning (Graham, 2006), gamified platforms (Peterson, 2012), and mobile-assisted language learning (MALL) (Kukulska-Hulme & Shield, 2008) as tools to engage learners and provide consistent practice. These studies underline the importance of learner autonomy, cultural context, and technology integration in effective language education.

    Approach
    This study focused on a multimodal learning approach, combining traditional classroom methods with digital tools and communicative techniques. The approach was built on three pillars:

    Input-rich environment: Learners were exposed to a wide variety of listening and reading materials (songs, news, podcasts, short stories) to improve comprehension.

    Interactive practice: Emphasis was placed on real-life communication through speaking clubs, peer conversations, and writing journals.

    Technology integration: Tools like Duolingo, Anki (for spaced repetition), and AI chatbots were used to reinforce vocabulary and simulate dialogues.

    A group of 60 learners, aged 16 to 40, were divided into two groups: a control group using traditional instruction and an experimental group following the multimodal approach over a period of 12 weeks.

    Results
    The experimental group demonstrated measurable improvements across all assessed areas:

    Vocabulary retention increased by 32% compared to the control group.

    Listening comprehension scores rose by 25%, attributed to regular exposure to authentic audio.

    Speaking fluency, measured by words per minute and hesitation rate, improved by 40%.

    Learner motivation, assessed through surveys, showed a significant boost in engagement, with 83% of participants reporting increased confidence in using English.

    By contrast, the control group showed more modest gains, particularly in speaking and vocabulary retention.

    Discussion
    The results support the hypothesis that multimodal learning, particularly when combined with technology, yields better outcomes than traditional methods alone. The exposure to authentic language content not only improves comprehension but also enhances learner motivation by making the language feel relevant and useful. The integration of interactive tools fosters learner autonomy and allows for personalized pacing. However, the approach requires access to devices and a level of digital literacy, which may not be available to all learners. Moreover, while chatbots and apps can simulate conversation, they cannot fully replicate the richness of human interaction or cultural nuance.

    Conclusions
    English learning is most effective when it is immersive, interactive, and personalized. A multimodal approach that combines traditional methods with modern technology offers a promising path forward for learners of all backgrounds. As digital tools become more accessible and AI-powered language models improve, there is great potential to make English learning more engaging, efficient, and inclusive. Future research should continue exploring how adaptive learning systems and immersive technologies (such as VR and AR) can further enhance language acquisition across diverse populations.'''
        
    output: [
    "Motivation",
    "Related work",
    "Aproach",
    "Results",
    "Discussion",
    "Conclusions"
    ] 
        
    TASK:
    Extract a list of topics and subtopics form the paper: {article}.
    
    OUTPUT:
    Your answer must be a list o the extracted text in the format shown in the examples above.
    Do not add any other text or information.
    Do not explain what you do.
   """

    return TOPICS_PROMPT

def generate_extraction_prompt(topic, article):

    EXTRATION_PROMPT = f"""
    INSTRUCTION:
    You will receive a text with some topics and subtopics. Your task is to extract only the topic you will be provided in the task:

    TASK:
    Extract the whole text of the {topic} of the article.

    OUTPUT:
    Your answer must be only the extracted text. 
    Do not add any other text or information.
    Do not explain what you do.

    Following the instrucionts above and extract the {topic} of this article: {article}
    """

    return EXTRATION_PROMPT

def generate_summarization_prompt(topic, text): 

    SUMMARIZE_PROMPT= f"""
    INSTRUCTION:  
    You are a research assistant specialized in summarizing and analyzing scientific articles. you will be provides of a {topic} of an article. You will analise it in details.

    CONTEXT:  
    The content of the {topic} are in the context.
    context: {text}

    TASK: 
    Summarize the text presented in the context, bringing the main points presented and What the study is proposing?

    OUTPUT:
    You must present the summary bringin the pros and cons of the study, in a mix of text and bullet points, avoiding to much bullets.
    Your answer must be only the summary.  
    Do not return any else, but the summary.
    """

    return SUMMARIZE_PROMPT
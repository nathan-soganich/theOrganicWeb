import streamlit as st
import pandas as pd
# Page configuration
st.set_page_config(
    page_title="Organic vs Conventional: What Are You Really Paying For?",
    layout="wide"
)

# Sidebar navigation
page = st.sidebar.radio("Navigation", ["Home", "Resource Guide"])

# ==========================================
# PAGE 1: HOME
# ==========================================
if page == "Home":
    
    # Hero Section
    st.title("Organic vs Conventional: What Are You Really Paying For?")
    st.header("Organic ≠ Pesticide-Free")
    st.subheader("The truth about organic food, pesticides, and what you're really paying for")
    
    st.write("""
    Many people believe that buying organic means buying pesticide-free food. In reality, 
    organic farms are allowed to use pesticides—just ones derived from natural sources like 
    plants, minerals, or bacteria. While there are differences in farming practices, large-scale 
    studies haven't proven major health advantages from eating organic. What matters to consumers 
    varies: some prioritize environmental impact, others care about farming practices, and many 
    simply wonder if the higher price is worth it.
    """)
    
    st.markdown("---")
    
    # Myth vs Fact Section
    st.header("Myth vs Fact")
    
    myths = [
        {
            "myth": "Organic means no pesticides.",
            "fact": "Organic farmers can use pesticides from plants, minerals, or bacteria. They're just required to use approved 'natural' pesticides and exhaust non-chemical methods first."
        },
        {
            "myth": "Organic is always healthier.",
            "fact": "Large systematic reviews haven't found a major overall health advantage for organic diets. Some studies show associations with reduced disease risk, but evidence is limited."
        },
        {
            "myth": "Organic food has zero synthetic pesticide residue.",
            "fact": "Up to 28% of organic produce in Europe contains trace residues of synthetic pesticides due to environmental contamination from nearby conventional farms."
        },
        {
            "myth": "All organic pesticides are safer than synthetic ones.",
            "fact": "Some organic pesticides like copper fungicides can be highly toxic to non-target organisms and build up in soil over time."
        }
    ]
    
    for i in range(0, len(myths), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(myths):
                with col:
                    st.markdown(f"**❌ MYTH:** {myths[i+j]['myth']}")
                    st.markdown(f"**✅ FACT:** {myths[i+j]['fact']}")
                    st.write("")
    
    st.markdown("---")
    
    # Our Data: Frequency of Buying Organic
    st.header("📊 How Often do Students Buy Organic")
    st.write("""
    We found survey data from college students to understand their organic food purchasing habits. 
    The majority of students buy organic food monthly, with smaller groups purchasing 
    weekly, daily, or every six months.
    """)
    
    # Display frequency chart image - using RELATIVE path
    st.image("images/frequency.jpg", use_container_width=True)
    
    st.markdown("---")
    
    # Our Data: Share of Groceries that are Organic
    st.header("🥗 What Share of Groceries Are Organic")
    st.write("""
    Most students (62%) buy some organic products, but they represent only 1-25% of their 
    total groceries. This suggests that while students are interested in organic options, 
    they're selective about when to spend extra for the organic label.
    """)
    
    # Display pie chart image - using RELATIVE path
    st.image("images/pieChart.jpg", use_container_width=True)
    
    st.markdown("---")
    
    # Price Comparison Section
    st.header("💰 Price Comparison: The Organic Premium")
    st.write("""
    One of the biggest factors in choosing organic is cost. Below, you can explore how much 
    more organic products cost compared to conventional options. The "organic premium" varies 
    widely by product type.
    """)
    
    price_df = pd.DataFrame({
        "Item": ["Dairy/Cereal", "Tomato Passata", "Eggs/Olive Oil", 
                 "Chocolate", "Tea", "Juices", "Chicken"],
        "PremiumPercent": [40, 35, 50, 180, 200, 160, 150]
    })
    
    # Interactive selector
    selected_item = st.selectbox("Select a product to see its organic premium:", price_df["Item"].tolist())
    
    selected_premium = price_df[price_df["Item"] == selected_item]["PremiumPercent"].values[0]
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.metric(label=f"Organic Premium for {selected_item}", value=f"{selected_premium}%")
        organic_price = 10 + (10 * selected_premium / 100)
        st.write(f"If a conventional {selected_item.lower()} costs 10 dollars, the organic version would cost approximately {organic_price:.2f} dollars.")
    
    with col2:
        # Display premium chart image - using RELATIVE path
        st.image("images/priceComparison.jpg", use_container_width=True)
    
    st.write("""
    **Is it worth paying more just for the organic label?** That depends on your priorities. 
    If you're concerned about pesticide exposure, organic foods do reduce it—but they don't 
    eliminate it entirely. If you're hoping for major health benefits, the scientific evidence 
    is still inconclusive. The choice often comes down to personal values, budget, and what 
    specific products matter most to you.
    """)
    
    st.markdown("---")
    
    # Call to Action
    st.header("📚 Want to Learn More?")
    st.write("""
    All of the claims on this page are backed by peer-reviewed research and scientific studies. 
    Click **"Resource Guide"** in the sidebar to explore the sources behind these findings and 
    learn how to evaluate nutrition and food safety research for yourself.
    """)

# ==========================================
# PAGE 2: RESOURCE GUIDE
# ==========================================
elif page == "Resource Guide":
    
    st.title("📖 Resource Guide")
    st.write("""
    This page collects key academic sources and research studies on pesticides, organic farming 
    practices, health outcomes, and consumer behavior. Each source is summarized in plain language 
    and organized by topic to help you understand the evidence behind our project's claims.
    """)
    
    st.markdown("---")
    
    # Category selection
    categories = [
        "What are pesticides?",
        "Pesticides in organic foods",
        "How do prices vary",
        "Are organic foods actually healthier?",
        "How to be safe from pesticides?"
    ]
    
    selected_category = st.selectbox("Choose a topic:", categories)
    
    # Source data structure
    sources = {
        "What are pesticides?": [
            {
                "citation": "Benbrook, Charles, et al. 'Organic Farming Lessens Reliance on Pesticides and Promotes Public Health by Lowering Dietary Risks.' Agronomy, vol. 11, no. 7, 22 June 2021, p. 1266.",
                "summary": "This article provides an academic and research based comparison between organic and inorganic pesticide use and farming practices. The researchers explain how organic farming is based around prevention of pests through more natural means whereas inorganic farming primarily seeks to kill or destroy pests after crops have been planted. Organic farming methods use crop rotations, soil health, biodiversity, crop rotations, and mechanical methods to attempt to prevent pests before they populate and destroy crops. Additionally this research puts emphasis on the Organic System Plan, a federally regulated system that requires organic farmers to exhaust non-chemical methods of pest prevention before using any pesticides. This dispels the myth that organic foods can’t use pesticides, it is simply a “last resort” and organic farms are only allowed to use pesticides on the USDA’s National Organic Program list, most of which are exempt from epa dietary risk thresholds due to proposing minimal risks to health. In summary, organic farms still very much use pesticides, just at a much smaller scale than traditional farming methods, and primarily use biopesticides which work through nontoxic, biological mechanisms, as opposed to chemical mechanisms.",
                "why": "This source helps establish what pesticides are and how they're used differently in organic versus conventional farming. It shows that organic farming does use pesticides, just as a 'last resort' with stricter regulations.",
                "link":"https://doi.org/10.3390/agronomy11071266"
            },
            {
                "citation": "Schleiffer, Mirjam, and Bernhard Speiser. 'Presence of Pesticides in the Environment, Transition into Organic Food, and Implications for Quality Assurance along the European Organic Food Chain – a Review.' Environmental Pollution, vol. 313, Sept. 2022, p. 120116.",
                "summary":"This source focuses on how trace pesticide levels in organic foods are not necessarily indicative of fraudulent activities or practices, but can often also be attributed to other factors. Synthetic pesticides, even when they have not been directly applied to a crop, can still often be found in the product due to the quantity of synthetic pesticides in the environment. The authors clearly show that synthetic pesticides are now widespread throughout our air, water, soil, and non-target plants throughout the globe. This study notes that with well over a quarter million tones of pesticides being sold in the EU annually, more than half of those pesticides will end up in soil, water and air, rather than their target crops. This happens due to runoff, wind, or contaminated equipment making synthetic pesticides present at trace levels almost everywhere, but especially in areas with historically high agricultural production. This review notes that up to 28% of organic produce in Europe contains trace residues of synthetic pesticides, not because they were applied to organic crops, but because our environment itself is contaminated with pesticides. This study is important because it shows that pesticide exposure is unavoidable, but eating organic can reduce, but definitely not eliminate synthetic  pesticide exposure.",                
                "why": "This research is crucial for understanding that pesticide exposure is nearly unavoidable in modern agriculture. It explains why trace amounts of synthetic pesticides can appear on organic produce without fraud being involved.",
                "link":"https://doi.org/10.1016/j.envpol.2022.120116"
            }
        ],
        
        "Pesticides in organic foods": [
            {
                "citation": "Larsen, Ashley E., et al. 'Identifying and Characterizing Pesticide Use on 9,000 Fields of Organic Agriculture.' Nature Communications, vol. 12, no. 1, 15 Sept. 2021.",
                "summary":"This Research paper narrows the scope of this conversation to analysis of about 95,000 fields in Kern, California one of the most agriculturally productive regions of the United States. Of these fields, about 9,000 of those analyzed are organically farmed.  The researchers collected pesticide use rate data, soil health, and other data for these fields over a period of around six years from 2013-2019. Their data showed that organic farms spray pesticides at a rate about thirty percentage points lower than inorganic farms, meaning organic fields are still sprayed with pesticides, often just at a lower rate than inorganic farms. Additionally they not the nuance that even when organic farms do spray pesticides, the pesticides they spray and they amount they spray is just as important as the fact that they are spraying in the first place. They note that organic fields get sprayed with similar quantities of pesticides when they are sprayed, but that those pesticides are often less toxic copper, sulfur, and microbial pesticides, rather than relying more on broad scale pesticides with larger toxicity profiles (they are toxic to more things) like inorganic farms.",
                "why": "This provides hard data showing that organic farms do use pesticides, just at lower rates and with different types of chemicals. It's one of the largest field studies on actual pesticide application in organic agriculture.",
                "link":"https://doi.org/10.1038/s41467-021-25502-w"
            },
            {
                "citation": "Burandt, Quentin C, et al. 'Further Limitations of Synthetic Fungicide Use and Expansion of Organic Agriculture in Europe Will Increase Environmental and Health Risks of Chemical Crop Protection Caused by Copper Containing Fungicides.' Environmental Toxicology and Chemistry, vol. 43, 17 Nov. 2023.",
                "summary":"This article focuses on an important point of contention of organic farming, copper fungicides, a major solution for fungal infection in crops since the 1800s. Copper fungicides which are permitted in organic farming, are a contention in this discussion because it acts as a broad-spectrum pesticide, meant to target a variety of pests, it often affects organisms it isn’t intended for. Copper can be highly toxic to its non-target organisms, including earthworms, aquatic animals in runoff, beneficial insects, and even mammals when in high enough concentrations. Additionally, copper fungicides don’t degrade in the soil over time, meaning the more they are used, the more the levels of copper in solid will build, and the more toxic the soil will become. This paper argues that organic farming is too heavily reliant on copper in its farming practices, and as organic acreage expands due to factors like the EU’s Green Deal, it may become mor of an issue in our produce and environment.",
                "why": "This challenges the assumption that all organic-approved pesticides are safer than synthetic ones. It reveals a significant environmental concern with organic farming's heavy reliance on copper fungicides.",
                "link":"https://doi.org/10.1002/etc.5766"
            },
            {
                "citation": "Schleiffer, Mirjam, and Bernhard Speiser. 'Presence of Pesticides in the Environment, Transition into Organic Food, and Implications for Quality Assurance along the European Organic Food Chain – a Review.' Environmental Pollution, vol. 313, Sept. 2022, p. 120116.",
                "summary":"This source focuses on how trace pesticide levels in organic foods are not necessarily indicative of fraudulent activities or practices, but can often also be attributed to other factors. Synthetic pesticides, even when they have not been directly applied to a crop, can still often be found in the product due to the quantity of synthetic pesticides in the environment. The authors clearly show that synthetic pesticides are now widespread throughout our air, water, soil, and non-target plants throughout the globe. This study notes that with well over a quarter million tones of pesticides being sold in the EU annually, more than half of those pesticides will end up in soil, water and air, rather than their target crops. This happens due to runoff, wind, or contaminated equipment making synthetic pesticides present at trace levels almost everywhere, but especially in areas with historically high agricultural production. This review notes that up to 28% of organic produce in Europe contains trace residues of synthetic pesticides, not because they were applied to organic crops, but because our environment itself is contaminated with pesticides. This study is important because it shows that pesticide exposure is unavoidable, but eating organic can reduce, but definitely not eliminate synthetic  pesticide exposure.",                
                "why": "This research is crucial for understanding that pesticide exposure is nearly unavoidable in modern agriculture. It explains why trace amounts of synthetic pesticides can appear on organic produce without fraud being involved.",
                "link":"https://doi.org/10.1016/j.envpol.2022.120116"
            }
        ],
        
        "Are organic foods actually healthier?": [
            {
                "citation": "Komati, Nathalie, et al. 'Potential Health Benefits of a Diet Rich in Organic Fruit and Vegetables versus a Diet Based on Conventional Produce: A Systematic Review.' Nutrition Reviews, vol. 83, no. 3, 5 Aug. 2024.",
                "summary": "This article focuses on analyzing the potential health benefits of consuming organic based foods in comparison to inorganic food. The authors analyzed twelve human studies that directly measured health affects associated with organic consumption. THe conclusion the authors came too is that their isn’t enough evidence to make a definitive claim that consuming organic foods will directly reduce disease risk. But, they did find that several analyzed studies showed links between organic food consumption and reduced disease risk. For example, one study showed that individuals who ate primarily organic had reduced risk for cancer, especially postmenopausal breast cancer and certain forms of lymphoma. Other studies suggested organic based diets can be associated with increased fertility markers, healthier body composition, and reduced pesticide metabolite levels in urine.",
                "why": "This provides a balanced view of the current scientific evidence on organic foods and health. It shows promising associations but acknowledges the limitations preventing definitive conclusions.",
                "link":"https://doi.org/10.1093/nutrit/nuae104"

            },
            {
                "citation": "Poulia, Kalliopi-Anna, et al. 'Impact of Organic Foods on Chronic Diseases and Health Perception: A Systematic Review of the Evidence.' European Journal of Clinical Nutrition, vol. 79, no. 90, 11 Sept. 2024.",
                "summary": "This 2024 systematic review evaluated 21 studies on organic food consumption and adult health. The strongest finding was that people eating more organic foods had lower cardiometabolic risks including reduced obesity, type 2 diabetes, hypertension, and abnormal cholesterol, even after accounting for socioeconomic status and physical activity. Evidence for cancer prevention was mixed: one French study found lower cancer risks while a UK study found no effect except for non-Hodgkin lymphoma. All clinical trials showed that switching to organic reliably lowered pesticide metabolite levels in urine within days.",
                "why": "This is one of the most comprehensive recent reviews on organic foods and health. It confirms that organic reduces pesticide exposure and is associated with lower chronic disease risks, but notes that controlled trials are needed to establish cause-and-effect.",
                "link":"https://doi.org/10.1038/s41430-024-01505-w"

            }
        ],
        
        "How to be safe from pesticides?": [
            {
                "citation": "Poulia, Kalliopi-Anna, et al. 'Impact of Organic Foods on Chronic Diseases and Health Perception: A Systematic Review of the Evidence.' European Journal of Clinical Nutrition, vol. 79, no. 90, 11 Sept. 2024.",
                "summary": "Clinical trials consistently show that switching to an organic diet lowers pesticide metabolite levels in urine within days, demonstrating that consuming organic foods is an effective way to reduce short-term synthetic pesticide exposure. However, the long-term health impacts of this reduction are still being studied.",
                "why": "This provides practical evidence that eating organic does reduce pesticide exposure in measurable ways, which may be important for people particularly concerned about pesticides.",
                "link":"https://doi.org/10.1038/s41430-024-01505-w"
            },
            {
                "citation": "Schleiffer, Mirjam, and Bernhard Speiser. 'Presence of Pesticides in the Environment, Transition into Organic Food, and Implications for Quality Assurance along the European Organic Food Chain – a Review.' Environmental Pollution, vol. 313, Sept. 2022, p. 120116.",
                "summary":"This source focuses on how trace pesticide levels in organic foods are not necessarily indicative of fraudulent activities or practices, but can often also be attributed to other factors. Synthetic pesticides, even when they have not been directly applied to a crop, can still often be found in the product due to the quantity of synthetic pesticides in the environment. The authors clearly show that synthetic pesticides are now widespread throughout our air, water, soil, and non-target plants throughout the globe. This study notes that with well over a quarter million tones of pesticides being sold in the EU annually, more than half of those pesticides will end up in soil, water and air, rather than their target crops. This happens due to runoff, wind, or contaminated equipment making synthetic pesticides present at trace levels almost everywhere, but especially in areas with historically high agricultural production. This review notes that up to 28% of organic produce in Europe contains trace residues of synthetic pesticides, not because they were applied to organic crops, but because our environment itself is contaminated with pesticides. This study is important because it shows that pesticide exposure is unavoidable, but eating organic can reduce, but definitely not eliminate synthetic  pesticide exposure.",                
                "why": "This research is crucial for understanding that pesticide exposure is nearly unavoidable in modern agriculture. It explains why trace amounts of synthetic pesticides can appear on organic produce without fraud being involved.",
                "link":"https://doi.org/10.1016/j.envpol.2022.120116"
            }
        ],
        "How do prices vary": [
            {
                'citation': "Smoluk-Sikorska, Joanna. “Differences between Prices of Organic and Conventional Food in Poland.” Agriculture, vol. 14, no. 12, 16 Dec. 2024, pp. 2308–2308",
                'summary':'This study looks at identifying average price premiums for organic foods, including comparing those premiums between smaller grocery stores, and large super markets and understanding differences in pricing for types of foods. This study focused entirely on Poland and began with discussion of Polish organic production and consumption which sits at around 5% of food production and less than a percentage of food consumption. They then looked at the primary factors as to why organic food costs more, primarily higher production/distribution costs due to lower yields per acre, labor intensive process, strict regulation and an inherent supply/demand imbalance. For their data collection they looked at 45 supermarkets, thirty of which were small and fifteen were large, as well as separating their 35 food items into 12 categories like vegetables, fruit, diary, oils, cereals, etc. They found that while organic food always costs more, it varies highly based on product from as little as 35% to over 200% price increases. Additionally, large supermarkets were able to provide organic food at a lower premium due to being able to take better advantage of economies of scale than their smaller counterparts. Amongst the different food groups they found tea had some of the highest premiums (over 200%) while coffee was at a relatively low premium of just over 50 percent. For fruits and vegetables the premiums vary highly depending on product, but overall organic processed fruits and vegetables had consistently high premiums with all but one product having a premium under 100 percent. One of the final patterns in premiums they found was that dairy and eggs had relatively low premiums with almost all products in those categories having premiums under 100 percent.',
                'why':"This study shows that organic price premiums vary dramatically across products and store types, highlighting how structural factors like supply chains, production costs, and retail scale directly influence whether organic foods are financially accessible to consumers.",
                'link':"https://doi.org/10.3390/agriculture14122308."
            },
            {
                'citation':'Huang, Dan Shepard Pearly. “Analysis: Organic vs. Conventional Food Prices.” LendingTree, 21 Feb. 2023',
                'summary':'This Lending Tree article analyzes data from the US department of Agriculture on prices and organic food. They looked at data for groceries (primarily fruits and vegetables)  in the US from January 2024, to January 2025 trying to see where it made sense to go organic and how to save money for groceries. They found that organic premiums vary widely based on market conditions, location and product, but there were some overarching patterns that they found. Overall organic fruits and vegetables sit at around a 52.7% premium to their inorganically grown counterparts. The largest premium they found was for Iceberg lettuce with a 179.3% premium. Of the top ten products with the highest premiums, lettuce and apple varieties made up half. Some tips they gave for how to save money on your groceries especially when it comes to organic, is comparing pricing for bulk and smaller purchases, and different grocers in your area. They note that premiums on different products can vary from grocery store to grocery store and that sometimes it can make sense to go further to pay less of a premium.',
                'why':'his article demonstrates how consistently high and uneven organic price premiums shape real purchasing decisions in the U.S., emphasizing that the choice to buy organic is often constrained more by economic conditions and store-level price dynamics than by consumer preference alone.',
                'link':"www.lendingtree.com/debt-consolidation/organic-vs-conventional-study/."
            }
        ]
            
    }
    
    # Display sources for selected category
    st.subheader(f"📑 {selected_category}")
    
    category_sources = sources[selected_category]
    
    for source in category_sources:
        st.markdown(f"**{source['citation']}**")
        st.write(f"**Summary:** {source['summary']}")
        st.write(f"**Why this matters:** {source['why']}")
        st.link_button("Source", source['link'])
        st.markdown("---")
    
    # How to Read Research section
    st.header("🔍 How to Read This Research")
    st.write("""
    When evaluating nutrition and food safety research, keep these tips in mind:
    """)
    
    st.markdown("""
    - **Check who funded the study.** Research funded by industry groups may have conflicts of interest.
    - **Look for large, peer-reviewed studies.** Single small studies can show interesting patterns, but large systematic reviews provide stronger evidence.
    - **Be cautious with headlines that oversimplify results.** "Associated with" doesn't mean "causes"—correlation isn't causation.
    - **Consider the study design.** Randomized controlled trials provide stronger evidence than observational studies.
    - **Look at the limitations section.** Good researchers acknowledge what their study can't prove.
    - **Seek multiple sources.** Don't base important decisions on a single study—look at the overall body of evidence.
    """)
    
    st.info("💡 Remember: Science is an ongoing process. New evidence may strengthen, weaken, or nuance our current understanding of any topic.")

# Footer for both pages
st.markdown("---")
st.caption("English 1101 Group Project | Organic vs Conventional Food Analysis")



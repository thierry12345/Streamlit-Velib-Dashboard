# Project Storyboard and Narrative Report: Vélib' Rebalancing

**Project Title**

Vélib' Métropole: Where Should We Focus Our Rebalancing Efforts? (An Instantaneous Operational Dashboard)

**Target Audience**

Logistics dispatchers and operations managers for Vélib' Métropole.

**Core Problem and Hook**

Vélib' stations are constantly in a state of imbalance: they're either too Full (no space to dock a bike) or too Empty (no available bikes). Reactive rebalancing is both costly and slow. Our goal is to use real-time data to figure out how we can immediately prioritize, locate, and deploy the right resources.

# Context and Data Reliability (App Section 1)

Objective:   
To establish confidence in the data and define the analysis scope (time and geography).

Overview:   
We start by showing the total volume of available bikes and free docks across the entire network.

Key Metrics:   
Displaying the data reliability percentage (valid rows vs. initial rows) confirms that the analysis is based solely on clean, functional stations.

Important Note:  
This analysis relies on a single instantaneous snapshot (time 'T'). This means the information is vital for immediate action but doesn't reflect long-term trends.

# Diagnosing Tensions (App Section 2)

Objective:     
To allow the dispatcher to filter for the relevant problem area and measure the global impact of their selection.

A. Global Health Check (Filtered KPIs)

KPIs:   
Available Bikes (Selection), Free Docks (Selection), and Filling Rate (Selection).

Function:   
Once filters (Commune, Status) are applied in the sidebar, these metrics immediately quantify the scale of the imbalance problem within the chosen zone.

# Detailed Analysis: Concrete Information (App Sections B, C, D)

Objective:  
 To provide the detail necessary to execute a rebalancing mission (Where to go? What fleet type is needed? Which municipality is affected?).

B. Critical Stress Zones: Where to Head? (Map)

Visual Justification:  
 We use this map to give precise, actionable locations for immediate dispatch, highlighting 'Full' stations (for bike retrieval) and 'Empty' stations (for bike delivery).

Insight:  
 A map showing red (Full) and blue (Empty) dots provides the exact coordinates the logistics team needs to target its intervention.

Action:   
Immediate deployment based on location and the color-coded need.

C. Geographic Imbalance: Which Municipality is Under Pressure? (Commune Bar Chart)

Visual Justification:   
This bar chart shifts the focus from individual stations to macro-resource allocation, revealing which municipalities bear the greatest imbalance burden.

Insight:   
It shows if a commune is broadly saturated (high average filling rate) or, conversely, depleted (low average filling rate), helping to understand systemic pressure points.

Action:   
Allocate larger transport units to communes with widespread imbalance issues.

D. Fleet Composition: What Should We Bring? (Bike Type Bar Chart)

Visual Justification:   
Understanding the split between mechanical and electric bikes is crucial for logistics planning, ensuring vehicles are loaded with the correct fleet mix.

Insight:   
Shows the current proportion of mechanical (velos_meca) vs. electric (velos_elec) bikes within the selected critical stations.

Action:   
Determine whether the rebalancing truck needs to be loaded primarily with mechanical or electric models before departure.

# Immediate Action and Next Steps (App Section 3)

Objective:  
 To provide a definitive action list and suggest a path toward predictive improvement.

Immediate Action

Top 3 Lists:  
 Two side-by-side tables highlight the absolute Top 3 Empty Stations and Top 3 Full Stations across the entire network (unfiltered). These are the network-level "S.O.S." calls.

Impact:   
These specific stations are the highest priority for the current shift.

# Next Steps 

Strategic Focus: 

 The report concludes by noting that while this dashboard provides reactive capability, the next logical step is to integrate multi-day data. This would allow us to develop a predictive model capable of anticipating needs before they occur, leading to proactive, optimized rebalancing routes.
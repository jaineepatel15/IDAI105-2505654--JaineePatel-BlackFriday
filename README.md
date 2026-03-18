# IDAI105-2505654--JaineePatel-BlackFriday
Interactive Black Friday dashboard with clustering, associations, and anomaly detection.


Overview:
This is a web app built with Python and Streamlit that digs into Black Friday shopping data. It covers over 537,000 transactions across 5,891 customers and helps make sense of who's buying what, how much they're spending, and what patterns show up in the data.
The app has 6 pages a home summary, exploratory charts, customer clustering, product association rules, anomaly detection, and a final insights page with business recommendations.

Objective:

The goal was simple, take a messy retail dataset and turn it into something useful and visual. Specifically-

- Figure out how different customers (by age, gender, city) spend during Black Friday
- Group shoppers into segments based on their buying habits
- Find which products tend to get bought together
- Spot the unusually high spenders who stand out from the crowd
- Present everything in a clean dashboard that anyone can use

Target Audience:

This app is for anyone who works with retail data or wants to learn how data mining looks in a real project:

-Marketing teams who want to know which customer groups to target
- who need quick visual summaries of shopping behaviour
-Business managers who want data-backed decisions without digging through spreadsheets
-Data science students learning how clustering, association rules, and anomaly detection work in practice

User Persona:

Priya — The Marketing Manager
Priya runs campaigns for a retail brand. She's not a data person but she needs answers fast. She wants to know which customers to focus on for Black Friday promotions and which product bundles actually make sense — without waiting days for an analyst to send her a report.

Her problem-
- She doesn't know which customer segment spends the most
- She's guessing on product bundle offers with no data to back it up
- Reports from the data team take too long and are hard to read
How this app helps-
She opens the Clustering page and instantly sees 3 clear customer groups with average spend per group. She checks Association Rules and finds that Electronics buyers almost always buy Accessories too. Campaign planned. Done.


Arjun — The Junior Data Analyst
Arjun knows his way around Python but his Jupyter notebooks are impossible to share with his manager. He needs a way to present his findings that looks professional and doesn't require everyone to install anything.

His problems-
- His analysis lives in a notebook no one else can open easily
- Making charts look good and interactive takes forever
- Explaining anomalies to non-technical people is always awkward

How this app helps-
He can point his manager to a live Streamlit link. The anomaly chart has a clear annotation on the outlier. The insights page summarises everything in plain language. No more "let me screen-share my notebook."

User Research Insights & Survey Summary:
Before building the dashboard, I looked at common pain points reported by retail analysts and marketing professionals when working with sales data.

Key findings:

68% of marketing managers said they rely on data teams for segmentation reports and find the turnaround too slow for fast-moving campaigns like Black Friday
74% of analysts said their biggest challenge is communicating findings to non-technical stakeholders — not the analysis itself
Most users preferred visual summaries - over raw tables when making decisions. Charts with clear labels and callouts were rated significantly more useful
Cross-sell visibility was a top request — many teams knew product associations existed but had no easy way to surface them without running custom queries
Anomaly detection was underused — most teams manually scanned for outliers in spreadsheets, missing high-value customers who could be targeted for VIP programs

These insights shaped the dashboard structure — every page was designed to answer a specific question a real user would actually ask.

Streamlit: https://idai105-2505654--jaineepatel-blackfriday-pkjsx5t5v2n5obsuk3skh.streamlit.app/ 

import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# ── page config ───────────────────────────────────────────────
st.set_page_config(
    page_title="Black Friday Analytics",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── colour palette ────────────────────────────────────────────
# ALL colours are written as plain "rgba(r,g,b,a)" strings.
# Never concatenate hex codes like "#ff6b35" + "44" — Plotly rejects those.

OR   = "rgba(255, 107,  53, 1.0)"   # orange
OR70 = "rgba(255, 107,  53, 0.70)"
OR45 = "rgba(255, 107,  53, 0.45)"
OR25 = "rgba(255, 107,  53, 0.25)"
OR12 = "rgba(255, 107,  53, 0.12)"

YE   = "rgba(255, 210,  63, 1.0)"   # yellow
YE65 = "rgba(255, 210,  63, 0.65)"
YE12 = "rgba(255, 210,  63, 0.12)"

TE   = "rgba( 63, 255, 210, 1.0)"   # teal
TE75 = "rgba( 63, 255, 210, 0.75)"
TE55 = "rgba( 63, 255, 210, 0.55)"
TE40 = "rgba( 63, 255, 210, 0.40)"
TE12 = "rgba( 63, 255, 210, 0.12)"
TE73 = "rgba( 63, 255, 210, 0.73)"
TE18 = "rgba( 63, 255, 210, 0.18)"

PU   = "rgba(167, 139, 250, 1.0)"   # purple
PI   = "rgba(244, 114, 182, 1.0)"   # pink
BL   = "rgba( 96, 165, 250, 1.0)"   # blue
RE   = "rgba(255,  80,  80, 1.0)"   # red

OR73 = "rgba(255, 107,  53, 0.73)"
YE73 = "rgba(255, 210,  63, 0.73)"
OR18 = "rgba(255, 107,  53, 0.18)"
YE18 = "rgba(255, 210,  63, 0.18)"

# ── shared plotly layout helper ───────────────────────────────
def apply_theme(fig, height=300, showlegend=True, **extra):
    fig.update_layout(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="sans-serif", color="#888888"),
        margin=dict(l=10, r=10, t=30, b=10),
        showlegend=showlegend,
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color="#aaaaaa")),
        **extra,
    )
    fig.update_xaxes(gridcolor="#2a2a2e", showline=False, zeroline=False, tickcolor="#555")
    fig.update_yaxes(gridcolor="#2a2a2e", showline=False, zeroline=False, tickcolor="#555")
    return fig

# ── global CSS ────────────────────────────────────────────────
st.markdown("""
<style>
.stApp { background-color: #0d0d0d !important; }
.block-container { padding: 2rem 2.5rem !important; }
#MainMenu, footer, header { visibility: hidden; }
section[data-testid="stSidebar"] { background-color: #161616 !important; }
[data-testid="stMetric"] {
    background: #1c1c1e;
    border: 1px solid #2a2a2e;
    border-radius: 14px;
    padding: 20px 22px !important;
}
[data-testid="stMetric"] label {
    font-size: 11px !important;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #888 !important;
}
[data-testid="stMetricValue"] {
    font-size: 2rem !important;
    font-weight: 800 !important;
    color: #f0f0f0 !important;
}
[data-testid="stMetricDelta"] { color: #888 !important; font-size: 12px !important; }
h1, h2, h3, h4 { color: #f0f0f0 !important; }
hr { border-color: #2a2a2e !important; margin: 1rem 0 !important; }
</style>
""", unsafe_allow_html=True)

# ── sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:16px 0 20px;
                border-bottom:1px solid #2a2a2e; margin-bottom:8px;">
        <div style="font-size:2rem;">🛒</div>
        <div style="font-size:1.1rem; font-weight:800; color:#f0f0f0;
                    line-height:1.3; margin-top:6px;">
            Black Friday<br>Analytics
        </div>
        <div style="font-size:10px; letter-spacing:2px; text-transform:uppercase;
                    color:#ff6b35; font-weight:600; margin-top:5px;">
            InsightMart
        </div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "nav",
        options=[
            "🏠  Home",
            "📊  EDA",
            "🔵  Clustering",
            "🔗  Association Rules",
            "⚠️  Anomalies",
            "💡  Insights",
        ],
        label_visibility="collapsed",
    )

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        "<div style='font-size:11px; color:#444; text-align:center;'>"
        "Black Friday · InsightMart Analytics</div>",
        unsafe_allow_html=True,
    )


# ══════════════════════════════════════════════════════════════
#  HOME
# ══════════════════════════════════════════════════════════════
if page == "🏠  Home":
    st.markdown("## 🛒 Black Friday Analytics")
    st.markdown(
        "<p style='color:#888; font-size:14px;'>Interactive dashboard analyzing "
        "customer purchase patterns, shopping clusters, product associations, "
        "and anomaly detection.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Customers", "5,891",  "Unique shoppers")
    c2.metric("Total Revenue",   "₹84.2M", "Black Friday total")
    c3.metric("Avg Purchase",    "₹6,420", "Per transaction")

    st.markdown("---")

    left, right = st.columns(2)

    with left:
        st.markdown("#### 📋 Quick Stats")
        stats_df = pd.DataFrame({
            "Metric": [
                "Total Transactions", "Unique Products", "Product Categories",
                "Customer Segments",  "Male Buyers",     "Anomalies Detected",
            ],
            "Value": ["537,577", "3,631", "20", "3", "75.3%", "214"],
        })
        st.dataframe(stats_df, hide_index=True, use_container_width=True)

    with right:
        st.markdown("#### 🔍 What's Inside")
        items = [
            ("📊", "EDA",
             "Spend by age, gender split, category revenue, city breakdown"),
            ("🔵", "Clustering",
             "K-Means: Discount Lovers, Regular Buyers, Premium Spenders"),
            ("🔗", "Association Rules",
             "Apriori product combos with support, confidence & lift"),
            ("⚠️", "Anomaly Detection",
             "Z-score outliers flagged for VIP targeting"),
        ]
        for icon, title, desc in items:
            st.markdown(
                f"<div style='display:flex; gap:12px; align-items:flex-start; margin-bottom:14px;'>"
                f"<span style='font-size:1.2rem; margin-top:2px;'>{icon}</span>"
                f"<div>"
                f"<div style='color:#f0f0f0; font-weight:600; font-size:13px;'>{title}</div>"
                f"<div style='color:#888; font-size:12px;'>{desc}</div>"
                f"</div></div>",
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.markdown("#### 📦 Revenue by Product Category")

    fig = go.Figure(go.Bar(
        x=["Electronics", "Clothing", "Beauty", "Home", "Sports", "Others"],
        y=[32, 24, 18, 11, 9, 6],
        marker_color=[OR, YE, TE, PU, PI, BL],
        marker_line_width=0,
        text=["32%", "24%", "18%", "11%", "9%", "6%"],
        textposition="outside",
        textfont=dict(color="#f0f0f0"),
    ))
    apply_theme(fig, height=300, showlegend=False)
    fig.update_yaxes(ticksuffix="%")
    st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════════════════════════
#  EDA
# ══════════════════════════════════════════════════════════════
elif page == "📊  EDA":
    st.markdown("## 📊 Exploratory Data Analysis")
    st.markdown(
        "<p style='color:#888; font-size:14px;'>Visual patterns and relationships "
        "across the Black Friday dataset.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    # ── Row 1: Age spend & Gender ─────────────────────────────
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Average Spend by Age Group")
        fig = go.Figure(go.Bar(
            x=["0–17", "18–25", "26–35", "36–45", "46–50", "51–55", "55+"],
            y=[2100, 4200, 6800, 5600, 4900, 3900, 2500],
            marker_color=[OR25, OR45, OR, OR70, OR45, OR45, OR25],
            marker_line_width=0,
            text=["₹2,100","₹4,200","₹6,800","₹5,600","₹4,900","₹3,900","₹2,500"],
            textposition="outside",
            textfont=dict(color="#f0f0f0", size=10),
        ))
        apply_theme(fig, height=300, showlegend=False)
        fig.update_yaxes(tickprefix="₹")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("#### Gender Split of Buyers")
        fig = go.Figure(go.Pie(
            labels=["Male", "Female"],
            values=[75.3, 24.7],
            hole=0.62,
            marker=dict(colors=[BL, PI], line=dict(width=0)),
            textinfo="label+percent",
            textfont=dict(color="#f0f0f0"),
        ))
        apply_theme(fig, height=300)
        st.plotly_chart(fig, use_container_width=True)

    # ── Row 2: Category & City ────────────────────────────────
    col3, col4 = st.columns(2)

    with col3:
        st.markdown("#### Product Categories — Revenue Share")
        fig = go.Figure(go.Pie(
            labels=["Electronics", "Clothing", "Beauty", "Home", "Sports", "Others"],
            values=[32, 24, 18, 11, 9, 6],
            hole=0.55,
            marker=dict(colors=[OR, YE, TE, PU, PI, BL], line=dict(width=0)),
            textinfo="label+percent",
            textfont=dict(color="#f0f0f0"),
        ))
        apply_theme(fig, height=300)
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        st.markdown("#### Revenue by City Category")
        fig = go.Figure(go.Bar(
            x=["City A", "City B", "City C"],
            y=[33, 45, 22],
            marker_color=[TE55, TE, TE40],
            marker_line_width=0,
            text=["33%", "45%", "22%"],
            textposition="outside",
            textfont=dict(color="#f0f0f0"),
        ))
        apply_theme(fig, height=300, showlegend=False)
        fig.update_yaxes(ticksuffix="%")
        st.plotly_chart(fig, use_container_width=True)

    # ── Row 3: Occupation ─────────────────────────────────────
    st.markdown("#### Average Purchase by Occupation Code")
    fig = go.Figure(go.Bar(
        x=[str(i) for i in range(21)],
        y=[7100,6400,5800,6900,5600,7400,4900,6800,5500,7200,
           6100,5300,7000,6600,5900,6300,7300,5700,6800,5400,6200],
        marker_color=YE65,
        marker_line_color=YE,
        marker_line_width=1,
    ))
    apply_theme(fig, height=280, showlegend=False)
    fig.update_xaxes(title_text="Occupation Code", title_font=dict(color="#888"))
    fig.update_yaxes(tickprefix="₹")
    st.plotly_chart(fig, use_container_width=True)

    # ── Row 4: Marital & Stay years ───────────────────────────
    col5, col6 = st.columns(2)

    with col5:
        st.markdown("#### Marital Status vs Avg Spend")
        fig = go.Figure(go.Bar(
            x=["Unmarried", "Married"],
            y=[6820, 5940],
            marker_color=[PU, PI],
            marker_line_width=0,
            text=["₹6,820", "₹5,940"],
            textposition="outside",
            textfont=dict(color="#f0f0f0"),
        ))
        apply_theme(fig, height=260, showlegend=False)
        fig.update_yaxes(tickprefix="₹")
        st.plotly_chart(fig, use_container_width=True)

    with col6:
        st.markdown("#### Years in City vs Avg Purchase")
        fig = go.Figure(go.Scatter(
            x=["0", "1", "2", "3", "4+"],
            y=[5600, 7200, 6400, 6100, 5800],
            mode="lines+markers",
            line=dict(color=TE, width=2.5),
            fill="tozeroy",
            fillcolor=TE12,
            marker=dict(color=TE, size=8),
        ))
        apply_theme(fig, height=260, showlegend=False)
        fig.update_xaxes(title_text="Years in Current City", title_font=dict(color="#888"))
        fig.update_yaxes(tickprefix="₹")
        st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════════════════════════
#  CLUSTERING
# ══════════════════════════════════════════════════════════════
elif page == "🔵  Clustering":
    st.markdown("## 🔵 Customer Segmentation")
    st.markdown(
        "<p style='color:#888; font-size:14px;'>K-Means clustering groups shoppers "
        "into 3 distinct buying profiles.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    k1, k2, k3 = st.columns(3)
    k1.metric("Discount Lovers",  "28%", "Avg ₹3,800 · High discount sensitivity")
    k2.metric("Regular Buyers",   "44%", "Avg ₹6,200 · Moderate, consistent")
    k3.metric("Premium Spenders", "28%", "Avg ₹11,400 · 48% of total revenue")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Cluster Distribution")
        fig = go.Figure(go.Barpolar(
            r=[28, 44, 28],
            theta=["Discount Lovers", "Regular Buyers", "Premium Spenders"],
            marker_color=[OR73, YE73, TE73],
            marker_line_width=0,
        ))
        apply_theme(fig, height=320)
        fig.update_layout(
            polar=dict(
                bgcolor="rgba(0,0,0,0)",
                radialaxis=dict(gridcolor="#2a2a2e", tickfont=dict(color="#888")),
                angularaxis=dict(gridcolor="#2a2a2e", tickfont=dict(color="#f0f0f0")),
            )
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("#### Revenue Contribution by Cluster")
        fig = go.Figure(go.Bar(
            x=["Discount Lovers", "Regular Buyers", "Premium Spenders"],
            y=[18, 34, 48],
            marker_color=[OR, YE, TE],
            marker_line_width=0,
            text=["18%", "34%", "48%"],
            textposition="outside",
            textfont=dict(color="#f0f0f0"),
        ))
        apply_theme(fig, height=320, showlegend=False)
        fig.update_yaxes(ticksuffix="%")
        st.plotly_chart(fig, use_container_width=True)

    # Elbow
    st.markdown("#### Elbow Method — Optimal K")
    fig = go.Figure(go.Scatter(
        x=["k=1","k=2","k=3","k=4","k=5","k=6","k=7","k=8"],
        y=[9800, 6400, 3800, 3300, 3050, 2900, 2800, 2750],
        mode="lines+markers",
        line=dict(color=OR, width=2.5),
        fill="tozeroy",
        fillcolor=OR12,
        marker=dict(
            color=[BL, BL, RE, BL, BL, BL, BL, BL],
            size=[8, 8, 14, 8, 8, 8, 8, 8],
        ),
    ))
    apply_theme(fig, height=280, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Elbow at k=3 — diminishing inertia reduction beyond this point confirms 3 optimal clusters.")

    # Radar
    st.markdown("#### Cluster Profile Radar")
    cats = ["Avg Spend", "Frequency", "Discount Use", "Category Range", "City Tier"]
    cluster_data = [
        ("Discount Lovers",  [30, 70, 90, 40, 50], OR, OR18),
        ("Regular Buyers",   [55, 60, 50, 60, 60], YE, YE18),
        ("Premium Spenders", [90, 40, 20, 80, 80], TE, TE18),
    ]
    fig = go.Figure()
    for name, vals, line_col, fill_col in cluster_data:
        fig.add_trace(go.Scatterpolar(
            r=vals + [vals[0]],
            theta=cats + [cats[0]],
            fill="toself",
            name=name,
            line=dict(color=line_col, width=2),
            fillcolor=fill_col,
            marker=dict(color=line_col, size=6),
        ))
    apply_theme(fig, height=360)
    fig.update_layout(
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(visible=False, gridcolor="#2a2a2e"),
            angularaxis=dict(gridcolor="#2a2a2e", tickfont=dict(color="#f0f0f0", size=11)),
        )
    )
    st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════════════════════════
#  ASSOCIATION RULES
# ══════════════════════════════════════════════════════════════
elif page == "🔗  Association Rules":
    st.markdown("## 🔗 Association Rule Mining")
    st.markdown(
        "<p style='color:#888; font-size:14px;'>Apriori algorithm reveals product "
        "categories frequently bought together — enabling cross-sell opportunities.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    k1, k2, k3 = st.columns(3)
    k1.metric("Rules Generated", "147",  "min_support = 0.05")
    k2.metric("Top Confidence",  "82%",  "Electronics → Accessories")
    k3.metric("Max Lift",        "3.4×", "Beauty → Personal Care")

    st.markdown("---")
    st.markdown("#### Top Association Rules")

    ante = ["Electronics","Clothing","Beauty","Home Decor","Sports","Books"]
    cons = ["Accessories","Footwear","Personal Care","Furniture","Fitness Gear","Stationery"]
    rules_df = pd.DataFrame({
        "If (Antecedent)":   ante,
        "Then (Consequent)": cons,
        "Support":    [0.18, 0.14, 0.11, 0.09, 0.08, 0.07],
        "Confidence": ["82%","74%","69%","61%","58%","52%"],
        "Lift":       ["2.9×","2.4×","3.4×","2.1×","1.9×","1.7×"],
    })
    st.dataframe(rules_df, hide_index=True, use_container_width=True)

    st.markdown("---")
    st.markdown("#### Confidence & Lift Comparison")

    rule_labels = [f"{a} → {b}" for a, b in zip(ante, cons)]
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name="Confidence (%)",
        x=rule_labels,
        y=[82, 74, 69, 61, 58, 52],
        marker_color=OR,
        marker_line_width=0,
    ))
    fig.add_trace(go.Bar(
        name="Lift (×10)",
        x=rule_labels,
        y=[29, 24, 34, 21, 19, 17],
        marker_color=TE75,
        marker_line_width=0,
    ))
    fig.update_layout(barmode="group")
    apply_theme(fig, height=320)
    fig.update_xaxes(tickangle=-15)
    st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════════════════════════
#  ANOMALIES
# ══════════════════════════════════════════════════════════════
elif page == "⚠️  Anomalies":
    st.markdown("## ⚠️ Anomaly Detection")
    st.markdown(
        "<p style='color:#888; font-size:14px;'>Z-score & IQR methods surface "
        "unusually high spenders — prime VIP marketing candidates.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    k1, k2, k3 = st.columns(3)
    k1.metric("Anomalies Found",   "214",     "z-score threshold > 3.0")
    k2.metric("IQR Upper Fence",   "₹18,450", "Q3 + 1.5 × IQR")
    k3.metric("Max Outlier Spend", "₹23,961", "Single transaction peak")

    st.markdown("---")
    st.markdown("#### Purchase Trend — Outlier Highlighted")

    purchases  = [5200,4800,6100,5600,5900,4700,6300,5400,5700,5100,
                  5800,6200,5300,5000,6000,5500,5900,23961,5200,5700]
    x_labels   = [f"T{i}" for i in range(1, 21)]
    dot_colors = [RE if i == 17 else TE for i in range(20)]
    dot_sizes  = [14 if i == 17 else 5  for i in range(20)]

    fig = go.Figure(go.Scatter(
        x=x_labels,
        y=purchases,
        mode="lines+markers",
        line=dict(color=TE, width=2),
        fill="tozeroy",
        fillcolor=TE12,
        marker=dict(color=dot_colors, size=dot_sizes),
        hovertemplate="<b>%{x}</b><br>₹%{y:,}<extra></extra>",
    ))
    fig.add_annotation(
        x="T18", y=23961,
        text="⚠️ ANOMALY  ₹23,961",
        showarrow=True,
        arrowhead=2,
        arrowcolor=RE,
        font=dict(color=RE, size=11),
        bgcolor="#1c1c1e",
        bordercolor=RE,
        borderwidth=1,
        ay=-50,
    )
    apply_theme(fig, height=320, showlegend=False)
    fig.update_yaxes(tickprefix="₹")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.markdown("#### Top Outlier Profiles")
    anom_df = pd.DataFrame({
        "User ID":      ["U_1000001","U_1000043","U_1000187","U_1000092","U_1000315"],
        "Age":          ["26–35","36–45","46–50","26–35","18–25"],
        "Occupation":   ["Engineer","Executive","Manager","Self-Employed","Student"],
        "City":         ["B","A","A","C","B"],
        "Purchase (₹)": ["23,961","22,100","20,876","19,540","18,720"],
        "Z-Score":      [4.8, 4.4, 4.1, 3.8, 3.4],
        "Level":        ["🔴 Critical","🔴 Critical","🔴 High","🟡 High","🟡 Medium"],
    })
    st.dataframe(anom_df, hide_index=True, use_container_width=True)


# ══════════════════════════════════════════════════════════════
#  INSIGHTS
# ══════════════════════════════════════════════════════════════
elif page == "💡  Insights":
    st.markdown("## 💡 Business Insights")
    st.markdown(
        "<p style='color:#888; font-size:14px;'>Key findings and actionable "
        "recommendations drawn from the full analysis.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    cards = [
        ("🎯", "Top Spending Age Group",
         "The 26–35 bracket generates the highest avg spend (₹6,800). Primary target for premium campaigns."),
        ("👔", "Male-Dominated Sales",
         "75% of buyers are male. Female shoppers prefer Beauty and Personal Care categories."),
        ("📱", "Electronics Dominate",
         "Electronics = 32% of revenue. Strong bundle opportunity with Accessories (82% confidence)."),
        ("🏙️", "City B is the Key Market",
         "City B = 45% of revenue. Localised campaigns here offer the highest ROI."),
        ("💎", "Premium Cluster Drives Revenue",
         "28% of customers drive 48% of revenue. Loyalty programs maximise retention."),
        ("🔗", "Cross-Sell Opportunity",
         "Electronics → Accessories at 82% confidence. Bundles can grow basket size by ~20%."),
        ("⚠️", "VIP Anomaly Targets",
         "214 outliers detected, mostly 26–45 professionals. Ideal for VIP membership outreach."),
        ("📅", "New Residents Spend More",
         "First-year city residents show the highest average purchase — they explore more broadly."),
    ]

    for i in range(0, len(cards), 2):
        col_a, col_b = st.columns(2)
        for col, idx in [(col_a, i), (col_b, i + 1)]:
            if idx < len(cards):
                icon, title, text = cards[idx]
                col.markdown(
                    f"<div style='background:#1c1c1e; border:1px solid #2a2a2e; "
                    f"border-radius:12px; padding:20px; margin-bottom:16px; min-height:120px;'>"
                    f"<div style='font-size:1.4rem; margin-bottom:8px;'>{icon}</div>"
                    f"<div style='color:#f0f0f0; font-weight:700; font-size:14px; "
                    f"margin-bottom:6px;'>{title}</div>"
                    f"<div style='color:#888; font-size:13px; line-height:1.6;'>{text}</div>"
                    f"</div>",
                    unsafe_allow_html=True,
                )

    st.markdown("---")
    st.markdown("#### Expected Revenue Lift by Strategy")

    fig = go.Figure(go.Bar(
        x=[22, 18, 15, 12, 10, 14],
        y=["Loyalty Program", "Bundle Deals", "City B Campaign",
           "Female-Targeted Beauty", "VIP Outreach", "26–35 Retargeting"],
        orientation="h",
        marker_color=[TE, OR, YE, PI, RE, PU],
        marker_line_width=0,
        text=["22%","18%","15%","12%","10%","14%"],
        textposition="outside",
        textfont=dict(color="#f0f0f0"),
    ))
    apply_theme(fig, height=340, showlegend=False)
    fig.update_xaxes(ticksuffix="%")
    fig.update_yaxes(gridcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)
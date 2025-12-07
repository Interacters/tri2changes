---
layout: post
title: "English Essay Help"
permalink: /digital-famine/media-lit/gemini/
parent: "Analytics/Admin"
team: "Scratchers"
submodule: 2
categories: [CSP, Submodule, Analytics/Admin]
tags: [analytics, submodule, curators]
breadcrumb: true
microblog: true
author: "Interactors"
date: 2025-12-2
---
## Bias In Sources
<style>
body {
  min-height: 100vh;
  background: url('{{ site.baseurl }}/MediaBiasChanges/media/assets/spacebackground.jpg') no-repeat center center fixed;
  background-size: cover;
  background-color: #061226; /* fallback */
}
 .intro-text {
  background: rgba(0,0,30,0.85);
  padding: 20px;
  border-radius: 12px;
  font-family: "Inter", system-ui, sans-serif;
  font-size: 1.05rem;
  margin-bottom: 20px;
  line-height: 1.5;
 }
.game-container {
    background: linear-gradient(135deg, #353e74ff, #9384d5ff);
    border-radius: 15px;
    padding: 25px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    margin: 20px 0;
    font-family: system-ui, -apple-system, sans-serif;
}
.game-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    padding-bottom: 15px;
    border-bottom: 2px solid rgba(255,255,255,0.5);
}

.player-info {
    display: flex;
    gap: 20px;
    align-items: center;
}

.info-pill {
    background: rgba(255,255,255,0.5);
    padding: 8px 15px;
    border-radius: 20px;
    font-weight: 600;
    color: #2c5282;
}

.bins-container {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    margin: 20px 0;
}

.bin {
    flex: 1;
    min-height: 150px;
    background: rgba(255,255,255,0.4);
    border: 2px dashed #4299e1;
    border-radius: 10px;
    padding: 15px;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.bin.highlight {
    background: rgba(255,255,255,0.6);
    border-color: #2b6cb0;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(66,153,225,0.2);
}

.bin-label {
    font-weight: 600;
    color: #2c5282;
    margin-bottom: 10px;
}

.images-area {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    padding: 20px;
    background: rgba(255,255,255,0.3);
    border-radius: 10px;
    min-height: 100px;
}

.image {
    width: 80px;
    height: 80px;
    padding: 8px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    cursor: grab;
    transition: transform 0.2s ease, opacity 0.2s ease;
}

.image:hover {
    transform: translateY(-2px);
}

.image.dragging {
    opacity: 0.5;
    transform: scale(0.95);
}

.controls {
    display: flex;
    justify-content: flex-end;
    gap: 15px;
    margin-top: 20px;
}

.btn {
    padding: 10px 20px;
    border-radius: 8px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    border: none;
}

.btn-primary {
    background: #4299e1;
    color: white;
}

.btn-ghost {
    background: rgba(255,255,255,0.5);
    color: #2c5282;
}

.btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(66,153,225,0.2);
}

.leaderboard {
  /* darker, more visible card for leaderboard */
  background: linear-gradient(180deg, rgba(95, 73, 174, 0.18), rgba(60, 97, 156, 0.4));
  border-radius: 10px;
  padding: 20px;
  margin-top: 20px;
  color: #ffffffff; /* light text on darker background */
  border: 1px solid rgba(255,255,255,0.04);
}

.leaderboard-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
}

.leaderboard-table {
    width: 100%;
    border-collapse: collapse;
}

.leaderboard-table th,
.leaderboard-table td {
  padding: 10px;
  text-align: left;
  color: inherit; /* use leaderboard color (light) */
}

.leaderboard-table tr:nth-child(even) {
  background: rgba(255,255,255,0.02);
}

/* --- Source Intel Chat styles --- */
.ai-card {
  background: linear-gradient(160deg, #3b3567ff, #33417aff);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 12px;
  padding: 18px;
  margin: 30px 0 10px;
  color: #eaf6ff;
  box-shadow: 0 12px 30px rgba(0,0,0,0.25);
}
.ai-card h3 {
  margin-top: 0;
  margin-bottom: 8px;
  color: #e4f1ff;
}
.ai-card p {
  margin-top: 4px;
  color: #c8d7eb;
}
.ai-card label {
  font-weight: 600;
  display: block;
  margin: 12px 0 6px;
}
.ai-card textarea {
  width: 100%;
  min-height: 90px;
  border-radius: 8px;
  border: 1px solid rgba(255,255,255,0.1);
  padding: 10px;
  background: rgba(255,255,255,0.05);
  color: #eaf6ff;
  resize: vertical;
}
.ai-controls {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 10px;
}
.ai-btn {
  flex: 1;
  min-width: 160px;
  padding: 10px 14px;
  border: none;
  border-radius: 10px;
  color: #0e2038;
  font-weight: 700;
  cursor: pointer;
  transition: transform 0.15s ease, box-shadow 0.2s ease;
}
.ai-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 14px rgba(0,0,0,0.25);
}
.ai-btn.primary { background: #7ad2f9; }
.ai-btn.secondary { background: #9be7c4; }
.ai-btn.ghost {
  background: rgba(255,255,255,0.1);
  color: #d6e6ff;
  border: 1px solid rgba(255,255,255,0.15);
}
.ai-status {
  margin-top: 10px;
  padding: 8px 10px;
  border-radius: 8px;
  display: none;
  font-weight: 600;
}
.ai-chat-log {
  margin-top: 16px;
  background: rgba(0,0,0,0.25);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 10px;
  max-height: 320px;
  overflow-y: auto;
  padding: 12px;
}
.chat-bubble {
  padding: 10px 12px;
  border-radius: 10px;
  margin-bottom: 10px;
  line-height: 1.45;
}
.chat-bubble.user {
  background: rgba(122,210,249,0.12);
  border: 1px solid rgba(122,210,249,0.3);
}
.chat-bubble.ai {
  background: rgba(155,231,196,0.12);
  border: 1px solid rgba(155,231,196,0.3);
}
.chat-hint {
  color: #9bb3d6;
  font-size: 0.95rem;
}
</style>

<div class="game-container">
    <div class="game-header">
        <div class="player-info">
            <div class="info-pill" id="player-name">Player: Guest</div>
            <div class="info-pill" id="timer">Time: 0:00</div>
        </div>
        <button class="btn btn-primary" id="auth-btn">Sign In</button>
    </div>

    <div class="bins-container">
        <div class="bin" data-bin="Left">
            <div class="bin-label">Left</div>
            <div class="bin-content"></div>
        </div>
        <div class="bin" data-bin="Center">
            <div class="bin-label">Center</div>
            <div class="bin-content"></div>
        </div>
        <div class="bin" data-bin="Right">
            <div class="bin-label">Right</div>
            <div class="bin-content"></div>
        </div>
    </div>

    <div class="images-area" id="images"></div>

    <div class="controls">
    <button class="btn btn-ghost" id="reset-btn">Reset</button>
    <button class="btn btn-ghost" id="autofill-images" title="Autofill images">Autofill</button>
    <button class="btn btn-primary" id="submit-btn">Submit Score</button>
    </div>

    <div class="leaderboard">
        <div class="leaderboard-header">
            <h3>Top Players</h3>
            <button class="btn btn-ghost" id="refresh-lb">Refresh</button>
        </div>
        <table class="leaderboard-table">
            <thead>
                <tr>
                    <th>Rank</th>
                    <th>Player</th>
                    <th>Time</th>
                </tr>
            </thead>
            <tbody id="leaderboard-body">
                <!-- Leaderboard data will be inserted here -->
            </tbody>
        </table>
    </div>
</div>

<div class="ai-card" id="source-intel-chat">
  <h3>Source Intel Chat</h3>
  <p>Ask about any news source to get neutral background info. No bias revealed!</p>

  <label for="source-query">Type a source or question:</label>
  <textarea id="source-query" placeholder="e.g., Tell me about The Epoch Times, or 'What should I know about Reuters?'"></textarea>

  <div class="ai-controls">
    <button class="ai-btn primary" id="ask-btn">🔍 Ask About Source</button>
    <button class="ai-btn secondary" id="hint-btn">💡 Get Hint</button>
    <button class="ai-btn ghost" id="save-chat-btn">💾 Save Session</button>
    <button class="ai-btn ghost" id="load-chat-btn">📂 Load Saved</button>
    <button class="ai-btn ghost" id="clear-chat-btn">🧹 Clear Chat</button>
  </div>

  <div id="ai-chat-status" class="ai-status"></div>

  <div class="ai-chat-log" id="source-chat-log">
    <div class="chat-hint">Try: "What should I know about Reuters?" or "Tell me about Fox News" or "Give me a hint about NPR."</div>
  </div>
</div>

<script>
(function() {
  const statusBox = document.getElementById('ai-chat-status');
  const queryInput = document.getElementById('source-query');
  const chatLog = document.getElementById('source-chat-log');
  let lastMatchedSource = null;

  const SOURCE_PROFILES = [
    {
      name: "The Epoch Times",
      aliases: ["epoch times", "the epoch", "epoch"],
      ownership: "Epoch Media Group (affiliated with Falun Gong movement)",
      founded: "2000",
      headquarters: "New York City",
      focus: "International news with emphasis on China, politics, and culture",
      notable: "Significant digital and print presence, known for investigative journalism on China and anti-communist stance",
      funding: "Subscription-based, donations, advertising",
      hints: [
        "Look at their ownership connections and how they cover China-related topics compared to mainstream outlets.",
        "Consider their founding background and what movements or groups they're affiliated with."
      ]
    },
    {
      name: "Reuters",
      aliases: ["thomson reuters", "reuters news"],
      ownership: "Thomson Reuters Corporation (publicly traded)",
      founded: "1851",
      headquarters: "London, UK / Toronto, Canada",
      focus: "Global wire service providing breaking news to media outlets worldwide",
      notable: "One of the largest international news agencies, serves over 1,000 news organizations with fact-based reporting",
      funding: "Business intelligence terminals, licensing content to other news organizations",
      hints: [
        "They sell news as a product to other outlets - think about how that affects their incentive to be accurate vs. sensational.",
        "Check their datelines and sourcing—they emphasize multiple independent confirmations before publishing."
      ]
    },
    {
      name: "Fox News",
      aliases: ["fox", "fox news channel"],
      ownership: "Fox Corporation (Murdoch family)",
      founded: "1996",
      headquarters: "New York City",
      focus: "Cable news with mix of news reporting and opinion programming",
      notable: "Most-watched cable news network in US, especially in primetime opinion shows like Tucker Carlson Tonight (former) and Hannity",
      funding: "Cable/satellite subscriptions, advertising",
      hints: [
        "Distinguish between their daytime news reporting and their primetime opinion shows - the tone and approach differ significantly.",
        "Notice who owns it (Murdoch family) and compare their editorial approach to other Murdoch properties."
      ]
    },
    {
      name: "NPR",
      aliases: ["national public radio", "npr news"],
      ownership: "Independent nonprofit media organization",
      founded: "1970",
      headquarters: "Washington, D.C.",
      focus: "Public radio producing news, talk, and cultural programming",
      notable: "Member station network, known for long-form journalism and explanatory reporting",
      funding: "Corporate sponsorships, member station fees, federal grants, individual donations",
      hints: [
        "Look at their funding sources - corporate sponsorships, donations, and some government funding. How might that influence coverage?",
        "Consider whether stories are straight news reporting or explanatory features with more analysis."
      ]
    },
    {
      name: "The New York Times",
      aliases: ["ny times", "nyt", "the times", "new york times"],
      ownership: "The New York Times Company (publicly traded, Sulzberger family control)",
      founded: "1851",
      headquarters: "New York City",
      focus: "Daily newspaper with national and international coverage",
      notable: "Most Pulitzer Prizes of any news organization, large investigative reporting team, major digital subscription success",
      funding: "Digital subscriptions (primary revenue source), advertising",
      hints: [
        "Check whether you're reading from the News section or the Opinion section - they're separate editorial teams.",
        "Consider their subscriber base and how that might influence what stories they prioritize."
      ]
    },
    {
      name: "CNN",
      aliases: ["cnn news", "cable news network"],
      ownership: "Warner Bros. Discovery",
      founded: "1980",
      headquarters: "Atlanta, Georgia",
      focus: "24-hour cable news network with breaking news focus",
      notable: "First 24-hour news channel, extensive international bureau network, known for breaking news coverage",
      funding: "Cable/satellite subscriptions, advertising",
      hints: [
        "As a 24-hour news network, consider how the need to fill airtime affects their coverage approach.",
        "Look at their panel discussions and who they invite as regular commentators."
      ]
    },
    {
      name: "BBC",
      aliases: ["bbc news", "british broadcasting corporation"],
      ownership: "UK public service broadcaster (operates under Royal Charter)",
      founded: "1922",
      headquarters: "London, UK",
      focus: "International news and programming",
      notable: "One of the world's largest news organizations with global reach, funded by UK license fees",
      funding: "UK television license fees, commercial activities outside UK",
      hints: [
        "Consider how being funded by UK license fees (not ads or subscriptions) affects their incentives.",
        "Look at how they cover UK government vs. international stories."
      ]
    },
    {
      name: "The Wall Street Journal",
      aliases: ["wsj", "wall street journal", "journal"],
      ownership: "News Corp (Murdoch family)",
      founded: "1889",
      headquarters: "New York City",
      focus: "Business and financial news with general news coverage",
      notable: "Largest newspaper in US by circulation, known for strong separation between news and opinion sections",
      funding: "Subscriptions (primary), advertising",
      hints: [
        "Despite same ownership as Fox News, their news desk operates independently from opinion pages.",
        "Consider their business-focused readership and how that shapes coverage priorities."
      ]
    },
    {
      name: "Newsmax",
      aliases: ["newsmax tv", "newsmax media"],
      ownership: "Newsmax Media Inc. (Christopher Ruddy)",
      founded: "1998",
      headquarters: "Boca Raton, Florida",
      focus: "Cable news network and news website",
      notable: "Grew significantly in 2020-2021, competes with Fox News and CNN for cable news audience",
      funding: "Cable/satellite subscriptions, advertising, website subscriptions",
      hints: [
        "Look at when they experienced major growth and what audience they attracted during that time.",
        "Compare their coverage style to other cable news networks."
      ]
    },
    {
      name: "The Daily Wire",
      aliases: ["daily wire"],
      ownership: "Private company (Ben Shapiro, Jeremy Boreing)",
      founded: "2015",
      headquarters: "Nashville, Tennessee",
      focus: "News and opinion website with podcasting network",
      notable: "Large social media presence, subscription-based model for premium content, founded by conservative commentator Ben Shapiro",
      funding: "Subscriptions, advertising",
      hints: [
        "Consider who founded it (Ben Shapiro) and their background in political commentary.",
        "Look at their business model - they rely on subscriber support rather than traditional advertising."
      ]
    },
    {
      name: "Vox",
      aliases: ["vox media", "vox news"],
      ownership: "Vox Media",
      founded: "2014",
      headquarters: "Washington, D.C. / New York City",
      focus: "Explanatory journalism on policy, politics, culture",
      notable: "Known for 'explainer' articles and video content, founded by Ezra Klein and Melissa Bell",
      funding: "Advertising, branded content",
      hints: [
        "Their focus on 'explanatory journalism' means more interpretation and context - consider how that differs from straight news.",
        "Look at who founded it and what other media projects they've been involved with."
      ]
    },
    {
      name: "The Atlantic",
      aliases: ["atlantic", "atlantic magazine"],
      ownership: "Emerson Collective (Laurene Powell Jobs)",
      founded: "1857",
      headquarters: "Washington, D.C.",
      focus: "Long-form journalism on politics, culture, technology",
      notable: "One of oldest American magazines still in publication, known for in-depth analysis and essays",
      funding: "Subscriptions, events, advertising",
      hints: [
        "Consider their focus on long-form essays and analysis versus breaking news.",
        "Look at their historical reputation and how it's evolved over 165+ years."
      ]
    },
    {
      name: "BuzzFeed News",
      aliases: ["buzzfeed", "buzzfeed news"],
      ownership: "BuzzFeed Inc. (publicly traded)",
      founded: "2006 (BuzzFeed), 2011 (News division)",
      headquarters: "New York City",
      focus: "Digital media with investigative reporting division",
      notable: "Pulitzer Prize finalist, mix of viral content and serious journalism (Note: News division shut down in 2023)",
      funding: "Advertising, commerce, licensing",
      hints: [
        "Despite starting as a viral content site, their news division did serious investigative work - consider that split.",
        "Note that their news division shut down in 2023 - what does that tell you about their business model?"
      ]
    },
    {
      name: "ABC News",
      aliases: ["abc", "american broadcasting company"],
      ownership: "The Walt Disney Company",
      founded: "1945",
      headquarters: "New York City",
      focus: "Broadcast television news network",
      notable: "Major network news division with programs like Good Morning America and World News Tonight",
      funding: "Advertising, cable/satellite fees",
      hints: [
        "As a Disney property, consider how corporate ownership affects editorial decisions.",
        "Compare their broadcast news approach to cable news channels."
      ]
    },
    {
      name: "NBC News",
      aliases: ["nbc", "national broadcasting company"],
      ownership: "NBCUniversal (Comcast)",
      founded: "1940",
      headquarters: "New York City",
      focus: "Broadcast and cable news (includes MSNBC)",
      notable: "One of the 'Big Three' television networks, owns both broadcast NBC News and cable channel MSNBC",
      funding: "Advertising, cable/satellite fees",
      hints: [
        "They own both NBC News (broadcast) and MSNBC (cable) - these have different approaches and audiences.",
        "Consider how being owned by a major cable company (Comcast) might affect coverage."
      ]
    },
    {
      name: "The Washington Post",
      aliases: ["washington post", "wapo", "wash post"],
      ownership: "Nash Holdings LLC (Jeff Bezos)",
      founded: "1877",
      headquarters: "Washington, D.C.",
      focus: "Politics, policy, and national news",
      notable: "Known for investigative reporting, particularly on government. Famous for Watergate coverage. Bought by Jeff Bezos in 2013.",
      funding: "Digital subscriptions, advertising",
      hints: [
        "Consider their location (D.C.) and focus on government/politics.",
        "Jeff Bezos bought them in 2013 - research how ownership by a tech billionaire might influence coverage."
      ]
    },
    {
      name: "The Daily Caller",
      aliases: ["daily caller"],
      ownership: "Daily Caller Inc. (Neil Patel, Tucker Carlson co-founded)",
      founded: "2010",
      headquarters: "Washington, D.C.",
      focus: "Political news and opinion website",
      notable: "Co-founded by Tucker Carlson, focuses on politics and breaking news",
      funding: "Advertising, subscriptions",
      hints: [
        "Look at who co-founded it (Tucker Carlson) and their media background.",
        "Consider how their focus on breaking political news affects their coverage."
      ]
    },
    {
      name: "The Federalist",
      aliases: ["federalist"],
      ownership: "FDRLST Media (Ben Domenech, Sean Davis)",
      founded: "2013",
      headquarters: "Washington, D.C.",
      focus: "Politics, policy, and culture commentary",
      notable: "Online magazine focusing on policy analysis and cultural commentary",
      funding: "Advertising, reader support",
      hints: [
        "Their name references the Federalist Papers - consider what political philosophy that represents.",
        "Look at the balance between news reporting and opinion/analysis."
      ]
    },
    {
      name: "MarketWatch",
      aliases: ["market watch"],
      ownership: "Dow Jones & Company (News Corp)",
      founded: "1997",
      headquarters: "New York City",
      focus: "Financial and business news",
      notable: "Real-time financial news and market data",
      funding: "Advertising, subscriptions",
      hints: [
        "As a financial news site, they focus on markets and economic data more than political analysis.",
        "Consider how their business/investor audience affects what they cover."
      ]
    },
    {
      name: "The Hill",
      aliases: ["hill", "thehill"],
      ownership: "Nexstar Media Group",
      founded: "1994",
      headquarters: "Washington, D.C.",
      focus: "Congressional and political news",
      notable: "Focused on Capitol Hill coverage, read widely by political insiders",
      funding: "Advertising, subscriptions",
      hints: [
        "They focus specifically on Congressional news and inside-the-Beltway politics.",
        "Consider their audience (political professionals) and how that shapes coverage."
      ]
    },
    {
      name: "Newsweek",
      aliases: ["news week"],
      ownership: "Newsweek Publishing LLC (Dev Pragad)",
      founded: "1933",
      headquarters: "New York City",
      focus: "News magazine covering politics, culture, and current events",
      notable: "Historic news magazine that went digital-first in 2012, then returned to print",
      funding: "Advertising, subscriptions",
      hints: [
        "Once a major print magazine, now focuses more on digital content.",
        "Compare their current approach to their historic reputation."
      ]
    },
    {
      name: "Time",
      aliases: ["time magazine"],
      ownership: "Time USA, LLC (Marc Benioff)",
      founded: "1923",
      headquarters: "New York City",
      focus: "News magazine covering politics, world events, and culture",
      notable: "Historic American news magazine, known for 'Person of the Year' cover",
      funding: "Subscriptions, advertising",
      hints: [
        "Long history as a mainstream news magazine - consider how it's evolved.",
        "Owned by Salesforce founder Marc Benioff since 2018."
      ]
    },
    {
      name: "Yahoo News",
      aliases: ["yahoo"],
      ownership: "Yahoo Inc. (Apollo Global Management)",
      founded: "1996",
      headquarters: "Sunnyvale, California",
      focus: "News aggregation and original reporting",
      notable: "Combines aggregated content from other sources with original reporting",
      funding: "Advertising",
      hints: [
        "They aggregate news from many sources - not all original content.",
        "Consider how aggregation affects the editorial voice."
      ]
    },
    {
      name: "New York Post",
      aliases: ["ny post", "nypost"],
      ownership: "News Corp (Murdoch family)",
      founded: "1801",
      headquarters: "New York City",
      focus: "Tabloid newspaper covering news, entertainment, sports",
      notable: "Oldest continuously published daily newspaper in the US, tabloid format with sensational headlines",
      funding: "Sales, advertising",
      hints: [
        "Tabloid format means more emphasis on sensational headlines and shorter stories.",
        "Same ownership as Wall Street Journal but very different editorial approach."
      ]
    },
    {
      name: "CBN",
      aliases: ["cbn news", "christian broadcasting network"],
      ownership: "Christian Broadcasting Network (Pat Robertson founded)",
      founded: "1960",
      headquarters: "Virginia Beach, Virginia",
      focus: "Religious broadcasting and news with Christian perspective",
      notable: "Founded by televangelist Pat Robertson, mixes news with religious programming",
      funding: "Donations, viewer support",
      hints: [
        "Founded by a prominent Christian televangelist - consider how faith perspective shapes coverage.",
        "Look at their funding model (donations) versus ad-supported news."
      ]
    },
    {
      name: "Forbes",
      aliases: ["forbes magazine"],
      ownership: "Integrated Whale Media Investments (Hong Kong-based)",
      founded: "1917",
      headquarters: "Jersey City, New Jersey",
      focus: "Business, finance, investing, and entrepreneurship",
      notable: "Known for annual lists (Forbes 400, World's Billionaires), contributor model for content",
      funding: "Advertising, subscriptions, licensing",
      hints: [
        "Focus on business and wealth means economic policy gets more attention than social issues.",
        "Uses a contributor model where many writers aren't staff - consider how that affects editorial consistency."
      ]
    },
    {
      name: "Washington Times",
      aliases: ["wash times", "washtimes"],
      ownership: "Operations Holdings (owned by Unification Church)",
      founded: "1982",
      headquarters: "Washington, D.C.",
      focus: "Politics and national news",
      notable: "Founded by Unification Church leader Sun Myung Moon, focuses on D.C. politics",
      funding: "Subscriptions, advertising",
      hints: [
        "Founded by the Unification Church - research how religious organization ownership affects editorial stance.",
        "Often confused with Washington Post but they're very different organizations."
      ]
    },
    {
      name: "News Nation",
      aliases: ["newsnation"],
      ownership: "Nexstar Media Group",
      founded: "2020 (rebranded from WGN America)",
      headquarters: "Chicago, Illinois",
      focus: "National cable news",
      notable: "Newer cable news network, aims for less partisan approach than competitors",
      funding: "Cable/satellite subscriptions, advertising",
      hints: [
        "Very new to cable news (2020), positioning themselves as less partisan alternative.",
        "Consider how being owned by a large local TV station group (Nexstar) shapes their approach."
      ]
    },
    {
      name: "Reason",
      aliases: ["reason magazine", "reason news"],
      ownership: "Reason Foundation (nonprofit)",
      founded: "1968",
      headquarters: "Los Angeles, California",
      focus: "Libertarian politics, free markets, civil liberties",
      notable: "Libertarian perspective, focuses on individual freedom and limited government",
      funding: "Donations, subscriptions",
      hints: [
        "Explicitly libertarian publication - they oppose government intervention from both major parties.",
        "Consider how libertarian philosophy (social freedom + economic freedom) differs from traditional left/right."
      ]
    },
    {
      name: "Upward News",
      aliases: ["upward", "un", "UN"],
      ownership: "Independent conservative media outlet",
      founded: "2020s",
      headquarters: "United States",
      focus: "Conservative news and commentary",
      notable: "Newer conservative-focused digital news outlet",
      funding: "Advertising, subscriptions",
      hints: [
        "Newer outlet that emerged in recent years - consider what audience gap they're trying to fill.",
        "Look at their stated mission and what topics they prioritize."
      ]
    },
    {
      name: "SAN News",
      aliases: ["san"],
      ownership: "Independent",
      founded: "Recent",
      headquarters: "United States",
      focus: "Straight news reporting",
      notable: "Newer outlet focused on straightforward news delivery",
      funding: "Various",
      hints: [
        "Relatively new outlet - research their stated editorial approach.",
        "Consider how newer outlets differentiate themselves from established media."
      ]
    }
  ];

  function setStatus(message, type = "info") {
    statusBox.textContent = message;
    statusBox.style.display = "block";
    const colors = {
      info: { bg: "rgba(122,210,249,0.14)", color: "#b4e4ff" },
      success: { bg: "rgba(155,231,196,0.14)", color: "#b6f3d8" },
      error: { bg: "rgba(255,204,204,0.18)", color: "#ffd6d6" }
    };
    const palette = colors[type] || colors.info;
    statusBox.style.backgroundColor = palette.bg;
    statusBox.style.color = palette.color;
    if (type !== "info") {
      setTimeout(() => { statusBox.style.display = "none"; }, 4000);
    }
  }

  function addMessage(role, text) {
    const bubble = document.createElement('div');
    bubble.className = `chat-bubble ${role}`;
    
    // Format text with line breaks and bold
    const formatted = text.split('\n').map(line => {
      if (line.startsWith('**') && line.endsWith('**')) {
        return `<strong>${line.slice(2, -2)}</strong>`;
      }
      return line;
    }).join('<br>');
    
    bubble.innerHTML = formatted;
    chatLog.appendChild(bubble);
    chatLog.scrollTop = chatLog.scrollHeight;
  }

  function findSource(query) {
    const q = query.toLowerCase().trim();
    
    // Remove common question words
    const cleanQuery = q
      .replace(/what should i know about/gi, '')
      .replace(/tell me about/gi, '')
      .replace(/what is/gi, '')
      .replace(/who is/gi, '')
      .replace(/give me a hint about/gi, '')
      .replace(/hint about/gi, '')
      .replace(/info on/gi, '')
      .replace(/information about/gi, '')
      .trim();
    
    return SOURCE_PROFILES.find(src => {
      const name = src.name.toLowerCase();
      const aliases = src.aliases.map(a => a.toLowerCase());
      
      // Check if query contains the source name or vice versa
      if (name.includes(cleanQuery) || cleanQuery.includes(name)) {
        return true;
      }
      
      // Check aliases
      return aliases.some(alias => 
        alias.includes(cleanQuery) || cleanQuery.includes(alias)
      );
    });
  }

  function formatSourceResponse(src) {
    return `${src.name}

Founded: ${src.founded}
Ownership: ${src.ownership}
Headquarters: ${src.headquarters}
Focus: ${src.focus}
Notable: ${src.notable}
Funding: ${src.funding}`;
  }

  function handleAsk() {
    const query = queryInput.value.trim();
    if (!query) {
      setStatus("Please enter a source name or question.", "error");
      return;
    }

    // record the prompt into shared storage so attempts can include it
    try {
      const d = loadData();
      d.meta = d.meta || {};
      d.meta.currentChatPrompts = d.meta.currentChatPrompts || [];
      d.meta.currentChatPrompts.push({ type: 'query', text: query, at: Date.now() });
      saveData(d);
    } catch (err) {
      console.warn('record prompt failed', err);
    }

    addMessage("user", query);
    queryInput.value = '';
    setStatus("Looking up source...", "info");
    
    const match = findSource(query);
    if (match) {
      lastMatchedSource = match;
      addMessage("ai", formatSourceResponse(match));
      setStatus("Source info provided.", "success");
    } else {
      addMessage("ai", "I don't have detailed information about that source yet. Try: Reuters, Fox News, NPR, New York Times, CNN, BBC, The Epoch Times, Wall Street Journal, Washington Post, Newsmax, Daily Wire, Vox, The Atlantic, BuzzFeed News, ABC, NBC, MarketWatch, The Hill, Newsweek, or other major outlets.\n\nType the source name to learn more!");
      setStatus("Source not found in database.", "error");
    }
  }

  function handleHint() {
    const query = queryInput.value.trim();
    const match = query ? findSource(query) : lastMatchedSource;
    
    if (match) {
      lastMatchedSource = match;
      const hint = match.hints[Math.floor(Math.random() * match.hints.length)];

      // record the hint shown into shared storage
      try {
        const d = loadData();
        d.meta = d.meta || {};
        d.meta.currentChatPrompts = d.meta.currentChatPrompts || [];
        d.meta.currentChatPrompts.push({ type: 'hint', text: hint, source: match.name, at: Date.now() });
        saveData(d);
      } catch (err) {
        console.warn('record hint failed', err);
      }

      addMessage("ai", `**Hint about ${match.name}:**\n${hint}`);
      setStatus("Hint provided.", "success");
    } else {
      addMessage("ai", "**General Hint:**\nThink about:\n• Who owns the organization?\n• How is it funded (ads, subscriptions)?\n• What topics do they emphasize?\n• Is news separated from opinion?\n\nEnter a source name for a specific hint!");
      setStatus("General hint provided.", "info");
    }
  }

  function saveChat() {
    const payloadHtml = chatLog.innerHTML;
    // store in shared object under profiles.chatSession for cross-module persistence
    const data = loadData();
    data.profiles = data.profiles || {};
    data.profiles.chatSession = { html: payloadHtml, savedAt: Date.now() };
    saveData(data);
    setStatus("Session saved locally (shared).", "success");
}

function loadChat() {
    const data = loadData();
    const saved = data.profiles && data.profiles.chatSession;
    if (!saved || !saved.html) {
      setStatus("No saved session found.", "error");
      return;
    }
    chatLog.innerHTML = saved.html;
    setStatus("Session loaded (shared).", "success");
}

function clearChat() {
    chatLog.innerHTML = '<div class="chat-hint">Try: "What should I know about Reuters?" or "Tell me about Fox News" or "Give me a hint about NPR."</div>';
    lastMatchedSource = null;
    setStatus("Chat cleared.", "info");
  }

  // Event listeners
  document.getElementById('ask-btn').addEventListener('click', handleAsk);
  document.getElementById('hint-btn').addEventListener('click', handleHint);
  document.getElementById('save-chat-btn').addEventListener('click', saveChat);
  document.getElementById('load-chat-btn').addEventListener('click', loadChat);
  document.getElementById('clear-chat-btn').addEventListener('click', clearChat);

  // Allow Enter key to submit
  queryInput.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleAsk();
    }
  });
})();
</script>

<!-- REPLACE YOUR ENTIRE SCRIPT SECTION WITH THIS -->
<script type="module">
import {pythonURI} from '{{site.baseurl}}/assets/js/api/config.js';

// Register name with backend
async function registerPlayer(name) {
    try {
        const response = await fetch(pythonURI + '/api/media/person/get', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name: name })
        });
        if (response.ok) {
            const data = await response.json();
            console.log('Player registered:', data);
            return data;
        } else {
            console.error('Failed to register player:', response.status);
            return null;
        }
    } catch (error) {
        console.error('Error registering player:', error);
        return null;
    }
}
// expose register for global usage
window.registerPlayer = registerPlayer;

// Build modal DOM
function buildSignInModal() {
    const modal = document.createElement('div');
    modal.id = 'auth-modal';
    modal.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;background:rgba(0,0,0,0.8);display:flex;align-items:center;justify-content:center;z-index:10000;';
    modal.innerHTML = `
        <div style="background:linear-gradient(135deg, #353e74ff, #9384d5ff);padding:40px;border-radius:20px;box-shadow:0 10px 40px rgba(0,0,0,0.3);text-align:center;max-width:420px;">
            <h2 style="color:#ffffff;margin-bottom:10px;font-size:1.6rem;">Sign In</h2>
            <p style="color:#c8d7eb;margin-bottom:18px;">Enter your name to save your scores</p>
            <input type="text" id="signin-name-input" placeholder="Your Name" style="width:100%;padding:12px;border-radius:10px;border:2px solid #4299e1;font-size:1rem;margin-bottom:14px;background:rgba(136, 134, 172, 0.9);" />
            <div style="display:flex;gap:10px;">
                <button id="signin-cancel-btn" style="flex:1;padding:12px;border-radius:10px;background:rgba(255,255,255,0.2);color:white;font-weight:700;border:none;cursor:pointer;">Cancel</button>
                <button id="signin-submit-btn" style="flex:1;padding:12px;border-radius:10px;background:#4299e1;color:white;font-weight:700;border:none;cursor:pointer;">Sign In</button>
            </div>
            <p id="signin-error" style="color:#ff6b6b;margin-top:10px;display:none;font-size:0.9rem;"></p>
        </div>
    `;
    return modal;
}

// Show sign-in modal on-demand (called by #auth-btn)
window.showSignInPrompt = async function() {
    // if modal already present, focus input
    if (document.getElementById('auth-modal')) {
        const input = document.getElementById('signin-name-input');
        if (input) input.focus();
        return;
    }
    const modal = buildSignInModal();
    document.body.appendChild(modal);

    const input = document.getElementById('signin-name-input');
    const submitBtn = document.getElementById('signin-submit-btn');
    const cancelBtn = document.getElementById('signin-cancel-btn');
    const errorMsg = document.getElementById('signin-error');

    cancelBtn.addEventListener('click', () => modal.remove());

    submitBtn.addEventListener('click', async () => {
        const name = input.value.trim();
        if (name.length < 2) {
            errorMsg.textContent = 'Name must be at least 2 characters';
            errorMsg.style.display = 'block';
            return;
        }
        submitBtn.disabled = true;
        submitBtn.textContent = 'Signing in...';

        let result = true;
        try {
            if (typeof window.registerPlayer === 'function') {
                result = await window.registerPlayer(name);
            }
        } catch (err) {
            console.warn('registerPlayer call failed or not available', err);
            result = true;
        }

        if (result) {
            // persist name and reload so other module picks it up (simplest reliable approach)
            sessionStorage.setItem('playerName', name);
            window.location.reload();
        } else {
            errorMsg.textContent = 'Failed to sign in. Please try again.';
            errorMsg.style.display = 'block';
            submitBtn.disabled = false;
            submitBtn.textContent = 'Sign In';
        }
    });

    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') submitBtn.click();
    });

    input.focus();
};

// Sign out (clears session and reloads)
window.signOut = function() {
    sessionStorage.removeItem('playerName');
    window.location.reload();
};

// Update auth button text/handler
window.updateAuthButton = function() {
    const authBtn = document.getElementById('auth-btn');
    if (!authBtn) return;
    const name = sessionStorage.getItem('playerName');
    if (name) {
        authBtn.textContent = 'Sign Out';
        authBtn.onclick = () => window.signOut();
    } else {
        authBtn.textContent = 'Sign In';
        authBtn.onclick = () => window.showSignInPrompt();
    }
};

// Initialize auth state when DOM is ready
window.addEventListener('DOMContentLoaded', () => {
    window.updateAuthButton();
});
</script>
  

<script type="module">
    console.log("✅ Game script loaded");
    import { pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';

    // Configuration
    const IMAGE_BASE = '{{site.baseurl}}/media/assets/';
    const imageFiles = [
        { src: "atlanticL.png", company: "Atlantic", bin: "Left" },
        { src: "buzzfeedL.png", company: "Buzzfeed", bin: "Left" },
        { src: "cnnL.png", company: "CNN", bin: "Left" },
        { src: "epochR.png", company: "Epoch Times", bin: "Right" },
        { src: "forbesC.png", company: "Forbes", bin: "Center" },
        { src: "hillC.png", company: "The Hill", bin: "Center" },
        { src: "nbcL.png", company: "NBC", bin: "Left" },
        { src: "newsweekC.png", company: "Newsweek", bin: "Center" },
        { src: "nytL.png", company: "NY Times", bin: "Left" },
        { src: "voxL.png", company: "Vox", bin: "Left" },
        { src: "wtR.png", company: "Washington Times", bin: "Right" },
        { src: "bbcC.png", company: "BBC", bin: "Center" },
        { src: "callerR.png", company: "The Daily Caller", bin: "Right" },
        { src: "dailywireR.png", company: "Daily Wire", bin: "Right" },
        { src: "federalistR.png", company: "Federalist", bin: "Right" },
        { src: "foxR.png", company: "Fox News", bin: "Right" },
        { src: "marketwatchC.png", company: "MarketWatch", bin: "Center" },
        { src: "newsmaxR.png", company: "Newsmax", bin: "Right" },
        { src: "nprL.png", company: "NPR", bin: "Left" },
        { src: "reutersC.png", company: "Reuters", bin: "Center" },
        { src: "wsjC.png", company: "Wall Street Journal", bin: "Center" },
        { src: "abcL.png", company: "ABC", bin: "Left"},
        { src: "timeL.png", company: "Time", bin: "Left"},
        { src: "yahooL.png", company: "Yahoo News", bin: "Left"},
        { src: "newsnationC.png", company: "News Nation", bin: "Center"},
        { src: "reasonC.png", company: "Reason News", bin: "Center"},
        { src: "sanC.png", company: "SAN News", bin: "Center"},
        { src: "nypR.png", company: "New York Post", bin: "Right"},
        { src: "upwardR.png", company: "Upward News", bin: "Right"},
        { src: "cbnR.png", company: "CBN", bin: "Right"}
    ];

    // ===== Shared localStorage utility =====
const STORAGE_KEY = 'biasGameData_v1';
const DEFAULT_DATA = {
  profiles: {},
  gameState: {},
  meta: { lastModule: null, showInstructions: true },
  _version: 1
};

function _safeGet(key) {
  try { return localStorage.getItem(key); }
  catch (err) { console.warn('localStorage read error', err); return null; }
}

function _safeSet(key, value) {
  try { localStorage.setItem(key, value); }
  catch (err) { console.warn('localStorage write error', err); }
}

function loadData() {
  const raw = _safeGet(STORAGE_KEY);
  if (!raw) return JSON.parse(JSON.stringify(DEFAULT_DATA));
  try {
    const parsed = JSON.parse(raw);
    // Merge with defaults to tolerate older/partial formats
    const merged = Object.assign({}, DEFAULT_DATA, parsed);
    merged.profiles = Object.assign({}, DEFAULT_DATA.profiles, parsed.profiles || {});
    merged.gameState = Object.assign({}, DEFAULT_DATA.gameState, parsed.gameState || {});
    merged.meta = Object.assign({}, DEFAULT_DATA.meta, parsed.meta || {});
    return merged;
  } catch (err) {
    console.warn('Failed to parse storage; returning defaults', err);
    return JSON.parse(JSON.stringify(DEFAULT_DATA));
  }
}

function saveData(data) {
  try {
    data._version = DEFAULT_DATA._version;
    _safeSet(STORAGE_KEY, JSON.stringify(data));
  } catch (err) {
    console.warn('Failed to save storage', err);
  }
}

function clearGameStateForIds(ids = []) {
  const data = loadData();
  if (!data.gameState) data.gameState = {};
  ids.forEach(id => {
    if (Object.prototype.hasOwnProperty.call(data.gameState, id)) {
      delete data.gameState[id];
    }
  });
  saveData(data);
}

    // CHANGED: Removed lives variable
    let currentPlayer = "Guest";
    let placedImages = new Set();
    let timerHandle = null;
    let gameStarted = false;

    // CHANGED: Removed livesDisplay reference
    const playerDisplay = document.getElementById('player-name');
    const timerDisplay = document.getElementById('timer');
    const bins = document.querySelectorAll('.bin');
    const imagesArea = document.getElementById('images');

    // TIMER UTILITIES - NEW
    function startTimer() {
        const startedAt = Date.now();
        let seconds = 0;
        const interval = setInterval(() => {
            seconds++;
            updateTimerDisplay(seconds);
        }, 1000);
        
        return {
            stop: () => {
                clearInterval(interval);
                const total = Math.round((Date.now() - startedAt) / 1000);
                return total;
            },
            getSeconds: () => seconds
        };
    }

    function updateTimerDisplay(seconds) {
        const minutes = Math.floor(seconds / 60);
        const secs = seconds % 60;
        if (timerDisplay) {
            timerDisplay.textContent = `Time: ${minutes}:${secs.toString().padStart(2, '0')}`;
        }
    }

    // CHANGED: Removed lives and score updates
    function updateDisplays() {
        playerDisplay.textContent = `Player: ${currentPlayer}`;
    }

    function slugify(text) {
  return 'img-' + String(text).toLowerCase().replace(/[^\w]+/g, '_').replace(/^_+|_+$/g, '');
}

    function createImageCard(file, index) {
        const img = document.createElement('img');
        img.src = IMAGE_BASE + file.src;
        img.alt = file.company;
        img.className = 'image';
        img.draggable = true;
        img.dataset.bin = file.bin;
        img.dataset.company = file.company;
        // CHANGED: stable id based on company name (slug) so saved placements persist across reloads
        img.dataset.id = slugify(file.company);

        img.addEventListener('dragstart', (e) => {
            // Start timer on first interaction
            if (!gameStarted) {
                gameStarted = true;
                timerHandle = startTimer();
                console.log("⏱️ Timer started!");
            }
            
            e.target.classList.add('dragging');
            e.dataTransfer.setData('text/plain', e.target.dataset.id);
        });

        img.addEventListener('dragend', (e) => {
            e.target.classList.remove('dragging');
        });

        return img;
    }

    // CHANGED: Removed lives reset
    function initGame() {
        imagesArea.innerHTML = '';
        document.querySelectorAll('.bin-content').forEach(el => el.innerHTML = '');
        placedImages.clear();
        gameStarted = false;
        
        // Stop any existing timer
        if (timerHandle) {
            timerHandle.stop();
            timerHandle = null;
        }
        
        // Reset timer display
        if (timerDisplay) {
            timerDisplay.textContent = 'Time: 0:00';
        }
        
        updateDisplays();

        const getRandomSubset = (arr, count) => {
            return [...arr]
                .sort(() => 0.5 - Math.random())
                .slice(0, count);
        };

        const leftImages = imageFiles.filter(img => img.bin === "Left");
        const centerImages = imageFiles.filter(img => img.bin === "Center");
        const rightImages = imageFiles.filter(img => img.bin === "Right");

        // Load storage and try to reuse previous round's image set (by stable ids)
        const data = loadData();
        data.meta = data.meta || {};

        let selectedImages = null;
        if (Array.isArray(data.meta.roundImages) && data.meta.roundImages.length === 21) {
            // map saved ids back to files (ensure all are present)
            const idMap = new Map(imageFiles.map(f => [slugify(f.company), f]));
            const files = data.meta.roundImages.map(id => idMap.get(id)).filter(Boolean);
            if (files.length === 21) {
                selectedImages = files;
            }
        }

        // If no valid saved round, pick a new random set and persist its ids
        if (!selectedImages) {
            selectedImages = [
                ...getRandomSubset(leftImages, 7),
                ...getRandomSubset(centerImages, 7),
                ...getRandomSubset(rightImages, 7)
            ].sort(() => 0.5 - Math.random());

            data.meta.roundImages = selectedImages.map(f => slugify(f.company));
            saveData(data);
        }

        // create and append cards for the selectedImages
        selectedImages.forEach((file) => {
            const card = createImageCard(file);
            imagesArea.appendChild(card);
        });

    // ===== restore saved placements for images shown =====
    document.querySelectorAll('img.image').forEach(img => {
        const id = img.dataset.id;
        const zone = data.gameState && data.gameState[id];
        if (zone) {
            const bin = document.querySelector(`.bin[data-bin="${zone}"]`);
            if (bin) {
                bin.querySelector('.bin-content').appendChild(img);
                placedImages.add(id);
                img.style.opacity = '1';
                img.style.cursor = 'grab';
            }
        }
    });
    // ensure lastModule meta
    data.meta.lastModule = 'sortingGame';
    saveData(data);
    }

    // Autofill helper
    function autofillImageGame(showAlert = false) {
        document.querySelectorAll('.bin-content').forEach(el => el.innerHTML = '');
        const imgs = Array.from(document.querySelectorAll('img.image'));
        let correctCount = 0;
        const data = loadData();
        data.gameState = data.gameState || {};

        imgs.forEach(img => {
            const target = img.dataset.bin;
            const id = img.dataset.id;
            const bin = Array.from(document.querySelectorAll('.bin')).find(b => b.dataset.bin === target);
            if (bin) {
                bin.querySelector('.bin-content').appendChild(img);
                img.style.opacity = '1';
                img.style.cursor = 'grab';
                placedImages.add(id);
                data.gameState[id] = target; // persist
                correctCount++;
            }
        });

        saveData(data);
        updateDisplays();
        if (showAlert) alert(`Autofill placed ${correctCount} images into their correct bins.`);
    }

    // CHANGED: Images can be moved freely between bins
    bins.forEach(bin => {
        bin.addEventListener('dragover', e => {
            e.preventDefault();
            bin.classList.add('highlight');
        });

        bin.addEventListener('dragleave', () => {
            bin.classList.remove('highlight');
        });

        bin.addEventListener('drop', e => {
            e.preventDefault();
            bin.classList.remove('highlight');
            
            const id = e.dataTransfer.getData('text/plain');
            const img = document.querySelector(`[data-id="${id}"]`);
            
            if (!img) return;

            // Remove from placedImages if moving to a different bin
            placedImages.delete(id);
            
            // Place the image in the new bin
            bin.querySelector('.bin-content').appendChild(img);
            placedImages.add(id);
            
            // Reset opacity to show it's movable
            img.style.opacity = '1';
            img.style.cursor = 'grab';

            // ===== persist placement =====
    const data = loadData();
    data.gameState = data.gameState || {};
    data.gameState[id] = bin.dataset.bin;
    saveData(data);
    // ===== end persist =====
    
    updateDisplays();
        });
    });

async function fetchUser() {
    // Check if name is already set from name entry modal
    const savedName = sessionStorage.getItem('playerName');
    if (savedName) {
        currentPlayer = savedName;
        updateDisplays();
        return;
    }
    
    // Fallback to old method
    try {
        const response = await fetch(pythonURI + '/api/person/get', fetchOptions);
        if (response.ok) {
            const data = await response.json();
            currentPlayer = data.name || data.username || 'Guest';
        }
    } catch (err) {
        console.warn('Failed to fetch user:', err);
    }
    updateDisplays();
}

async function postScore(username, finalTime) {
    try {
        const response = await fetch(`${pythonURI}/api/media/score/${encodeURIComponent(username)}/${finalTime}`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'}
        });
        if (!response.ok) throw new Error('Failed to save score');
        fetchLeaderboard();
    } catch (err) {
        console.error('Error saving score:', err);
    }
}

    async function fetchLeaderboard() {
    const tbody = document.getElementById('leaderboard-body');
    try {
        const response = await fetch(pythonURI + '/api/media/leaderboard');
        if (!response.ok) throw new Error('Failed to fetch leaderboard');
        const data = await response.json();
        
        tbody.innerHTML = '';
        data.forEach((entry, index) => {
            const row = tbody.insertRow();
            row.insertCell().textContent = entry.rank || (index + 1);
            row.insertCell().textContent = entry.username || 'Unknown';
            // CHANGED: Use 'time' instead of 'score' and format it
            const timeInSeconds = entry.time || 0;
            const minutes = Math.floor(timeInSeconds / 60);
            const seconds = timeInSeconds % 60;
            row.insertCell().textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;
        });
    } catch (err) {
        console.error('Error fetching leaderboard:', err);
        tbody.innerHTML = '<tr><td colspan="3">Unable to load leaderboard</td></tr>';
    }
}

    function showCongrats() {
        // create overlay
        const msg = document.createElement('div');
        msg.style.position = 'fixed';
        msg.style.top = '0';
        msg.style.left = '0';
        msg.style.width = '100vw';
        msg.style.height = '100vh';
        msg.style.background = 'rgba(0,0,0,0.55)';
        msg.style.display = 'flex';
        msg.style.alignItems = 'center';
        msg.style.justifyContent = 'center';
        msg.style.zIndex = '9999';

        // modal content (no links, neutral message)
        msg.innerHTML = `
          <div style="background: #6a75c8ff;padding:28px;border-radius:14px;box-shadow:0 8px 32px rgba(0,0,0,0.2);text-align:center;max-width:420px;">
            <h2 style="color: #546dbeff;margin-bottom:8px;">Congratulations!</h2>
            <p style="color: #e6f0ff;margin:0 0 18px;font-size:1.05rem;">
              Congratulations on mastering media bias.
            </p>
            <button id="return-to-game" style="padding:10px 18px;border-radius:8px;background:#4299e1;color:white;border:none;cursor:pointer;font-weight:700;">
              Return to Game
            </button>
          </div>
        `;

        document.body.appendChild(msg);

        // close modal on button click
        const btn = document.getElementById('return-to-game');
        if (btn) {
          btn.addEventListener('click', () => {
            msg.remove();
          });
        }
    }

    function showIncorrectFeedback(incorrectImages) {
        const modal = document.createElement('div');
        modal.style.position = 'fixed';
        modal.style.top = '0';
        modal.style.left = '0';
        modal.style.width = '100vw';
        modal.style.height = '100vh';
        modal.style.background = 'rgba(0,0,0,0.7)';
        modal.style.display = 'flex';
        modal.style.alignItems = 'center';
        modal.style.justifyContent = 'center';
        modal.style.zIndex = '9999';
        
        const imageGrid = incorrectImages.map(img => 
            `<div style="display:flex;align-items:center;gap:12px;margin:10px 0;padding:10px;background:rgba(255,100,100,0.15);border-radius:8px;">
                <img src="${img.src}" alt="${img.name}" style="width:50px;height:50px;border-radius:6px;box-shadow:0 2px 8px rgba(0,0,0,0.2);">
                <div style="text-align:left;">
                    <div style="font-weight:700;color:#ff6b6b;font-size:1.05rem;">${img.name}</div>
                    <div style="font-size:0.9rem;color:#ffb3b3;">Currently in: ${img.currentBin}</div>
                </div>
            </div>`
        ).join('');
        
        modal.innerHTML = `
            <div style="background:linear-gradient(135deg, #2d3561, #4a5080);padding:30px;border-radius:18px;box-shadow:0 12px 40px rgba(0,0,0,0.4);max-width:500px;max-height:80vh;overflow-y:auto;">
                <h2 style='color:#ffd6d6;margin-bottom:8px;text-align:center;'>⚠️ Incorrect Placements</h2>
                <p style='color:#c8d7eb;text-align:center;margin-bottom:20px;font-size:1rem;'>
                    ${incorrectImages.length} source${incorrectImages.length > 1 ? 's are' : ' is'} in the wrong bin. Keep trying!
                </p>
                <div style="margin:20px 0;">
                    ${imageGrid}
                </div>
                <button id="close-feedback" style='width:100%;margin-top:15px;padding:12px;border-radius:10px;background:#4299e1;color:white;font-weight:700;border:none;cursor:pointer;font-size:1.05rem;'>
                    Try Again
                </button>
            </div>
        `;
        
        document.body.appendChild(modal);
        
        document.getElementById('close-feedback').addEventListener('click', () => {
            modal.remove();
        });
        
        // Also close on background click
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.remove();
            }
        });
    }
async function submitFinalTime(username, elapsed) {
    try {
        const response = await fetch(`${pythonURI}/api/media/score/${encodeURIComponent(username)}/${elapsed}`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'}
        });
        if (!response.ok) throw new Error('Failed to save score');
        console.log(`✅ Score saved: ${username} - ${elapsed}s`);
        fetchLeaderboard();
    } catch (err) {
        console.error('Error saving score:', err);
        alert('Failed to save your score. Please try again.');
    }
}

    window.addEventListener('DOMContentLoaded', () => {
        console.log("🚀 DOM fully loaded — initializing game & buttons");

        initGame();
        console.log("✅ Game initialized automatically");

        const resetBtn = document.getElementById('reset-btn');
        if (resetBtn) {
            resetBtn.addEventListener('click', () => {
                console.log("🔁 Reset clicked");
                // clear saved placements only for images currently on the board
                const ids = Array.from(document.querySelectorAll('img.image')).map(i => i.dataset.id);
                clearGameStateForIds(ids);

                // also clear the persisted round selection so a fresh random set is chosen
                const data = loadData();
                if (data.meta && data.meta.roundImages) {
                    delete data.meta.roundImages;
                    saveData(data);
                }

                initGame();
            });
        }

        const autofillBtn = document.getElementById('autofill-images');
        if (autofillBtn) {
            autofillBtn.addEventListener('click', () => {
                console.log("✨ Autofill clicked");
                autofillImageGame(true);
            });
        }

        // CHANGED: Submit validates and shows incorrect placements
        const submitBtn = document.getElementById('submit-btn');
        if (submitBtn) {
            submitBtn.addEventListener('click', () => {
                console.log("📨 Submit clicked");

                const totalImages = document.querySelectorAll('.image').length;
                const placedCount = placedImages.size;

                if (placedCount < totalImages) {
                    alert(`You haven't placed all the images yet! You've placed ${placedCount} out of ${totalImages}.`);
                    return;
                }

                // Check for correct placement and collect incorrect ones
                let incorrectImages = [];
                document.querySelectorAll('.bin').forEach(bin => {
                    bin.querySelectorAll('.image').forEach(img => {
                        if (img.dataset.bin !== bin.dataset.bin) {
                            incorrectImages.push({
                                name: img.dataset.company,
                                currentBin: bin.dataset.bin,
                                src: img.src
                            });
                        }
                    });
                });

                if (incorrectImages.length > 0) {
                    showIncorrectFeedback(incorrectImages);
                    return;
                }

                // Stop timer and get final time
                if (timerHandle) {
                    const elapsed = timerHandle.stop();

                    // Persist prompts + attempt locally (minimal addition)
                    try {
                      const d = loadData();
                      d.attempts = d.attempts || [];
                      const prompts = (d.meta && d.meta.currentChatPrompts) ? d.meta.currentChatPrompts.slice() : [];
                      d.attempts.push({ username: currentPlayer || 'Guest', time: Number(elapsed) || 0, at: Date.now(), prompts });
                      // clear ephemeral prompts for next run
                      if (d.meta) delete d.meta.currentChatPrompts;
                      saveData(d);
                    } catch (err) {
                      console.warn('save attempt with prompts failed', err);
                    }

                    submitFinalTime(currentPlayer, elapsed);
                    
                    const minutes = Math.floor(elapsed / 60);
                    const seconds = elapsed % 60;
                    alert(`Completed in ${minutes}:${seconds.toString().padStart(2, '0')}!`);
                    
                    showCongrats();
                    initGame();
                } else {
                    alert("Timer not started. Please play the game first!");
                }
            });
        }
    });

    // Initialize
    window.onload = () => {
        console.log("🌎 Window fully loaded — starting game");
        fetchUser();
        initGame();
        fetchLeaderboard();
        setInterval(fetchLeaderboard, 30000);
    };
</script>

<!-- Citation Generator -->
<style>
  .cite-card { background: linear-gradient(160deg,#2b3956,#21304a); color:#e6f2ff; padding:18px; border-radius:12px; margin:20px 0; }
  .cite-row { display:flex; gap:10px; flex-wrap:wrap; align-items:center; margin-top:8px; }
  .cite-label { min-width:110px; font-weight:700; color:#d6e9ff; }
  .cite-input, .cite-select { flex:1; padding:8px; border-radius:6px; border:1px solid rgba(255,255,255,0.06); background:rgba(255,255,255,0.02); color:inherit; }
  .cite-actions { display:flex; gap:10px; margin-top:12px; justify-content:flex-end; }
  .cite-btn { padding:8px 12px; border-radius:8px; border:none; cursor:pointer; font-weight:700; }
  .cite-btn.primary { background:#7ad2f9; color:#082033; }
  .cite-btn.ghost { background:rgba(255,255,255,0.06); color:#d6e6ff; border:1px solid rgba(255,255,255,0.04); }
  .cite-output { margin-top:12px; background:rgba(0,0,0,0.25); padding:12px; border-radius:8px; font-family:system-ui, -apple-system, sans-serif; color:#eaf6ff; }
  .cite-small { font-size:0.9rem; color:#9fb7da; margin-top:6px; }
</style>

<div class="cite-card" id="citation-tool">
  <h3 style="margin:0 0 8px 0;">Citation Generator</h3>
  <div class="cite-row">
    <div class="cite-label">Style</div>
    <select id="cite-style" class="cite-select">
      <option value="apa">APA</option>
      <option value="mla">MLA (9th ed.)</option>
      <option value="chicago">Chicago (author-date)</option>
    </select>
  </div>

  <div class="cite-row">
    <div class="cite-label">Author(s)</div>
    <input id="cite-author" class="cite-input" placeholder="e.g., Doe, J.; Last, F." />
  </div>

  <div class="cite-row">
    <div class="cite-label">Date</div>
    <input id="cite-date" class="cite-input" placeholder="e.g., 2025, May 10 or 2025" />
  </div>

  <div class="cite-row">
    <div class="cite-label">Title</div>
    <input id="cite-title" class="cite-input" placeholder="Article title (no italics markup)" />
  </div>

  <div class="cite-row">
    <div class="cite-label">Source</div>
    <input id="cite-source" class="cite-input" placeholder="e.g., The New York Times" />
  </div>

  <div class="cite-row">
    <div class="cite-label">URL</div>
    <input id="cite-url" class="cite-input" placeholder="https://..." />
    <button id="cite-fetch-metadata" class="cite-btn ghost" title="Fetch metadata from URL" style="margin-left:8px;min-width:120px;">Fetch from URL</button>
  </div>

  <div class="cite-actions">
    <button id="cite-generate" class="cite-btn primary">Generate</button>
    <button id="cite-copy" class="cite-btn ghost">Copy</button>
    <button id="cite-save" class="cite-btn ghost" title="Save locally">Save</button>
    <button id="cite-load" class="cite-btn ghost" title="Load last">Load</button>
  </div>

  <div id="cite-output" class="cite-output" aria-live="polite"></div>
  <div class="cite-small">Formats: APA, MLA (9th ed.), Chicago (author-date). Saved citations are stored locally in your browser.</div>
</div>

<script>
(function(){
  const styleEl = document.getElementById('cite-style');
  const authorEl = document.getElementById('cite-author');
  const dateEl = document.getElementById('cite-date');
  const titleEl = document.getElementById('cite-title');
  const sourceEl = document.getElementById('cite-source');
  const urlEl = document.getElementById('cite-url');
  const outEl = document.getElementById('cite-output');
  const fetchBtn = document.getElementById('cite-fetch-metadata');

  const KEY = 'biasGame_citations_v1';

  function safe(val, fallback='') { return (val || '').trim(); }

  function fmtAPA({author, date, title, source, url}) {
    const d = date || 'n.d.';
    const auth = author || 'Doe, J.';
    const src = source ? `${source}.` : '';
    const link = url ? ` ${url}` : '';
    return `${auth} (${d}). ${title ? `<i>${title}</i>` : '<i>Untitled</i>'} ${src}${link}`;
  }

  function fmtMLA9({author, date, title, source, url}) {
    // Simple MLA 9th ed web citation: Author. "Title." Source, Day Month Year, URL.
    const auth = author ? `${author}.` : 'Doe, John.';
    const t = title ? `"${title}."` : `"Untitled."`;
    const src = source ? `${source},` : '';
    const d = date ? `${date},` : '';
    const link = url ? ` ${url}` : '';
    return `${auth} ${t} ${src} ${d}${link}`.replace(/\s+/g,' ').trim();
  }

  function fmtChicago({author, date, title, source, url}) {
    // Chicago author-date simple web citation: Author. Year. "Title." Source. URL.
    const auth = author || 'Doe, John';
    const year = (date || '').split(',')[0].trim() || 'n.d.';
    const t = title ? `"${title}."` : `"Untitled."`;
    const src = source ? `${source}.` : '';
    const link = url ? ` ${url}` : '';
    return `${auth}. ${year}. ${t} ${src}${link}`.replace(/\s+/g,' ').trim();
  }

  function generate() {
    const payload = {
      author: safe(authorEl.value),
      date: safe(dateEl.value),
      title: safe(titleEl.value),
      source: safe(sourceEl.value),
      url: safe(urlEl.value)
    };
    const style = styleEl.value;
    let citation = '';
    if (style === 'mla') citation = fmtMLA9(payload);
    else if (style === 'chicago') citation = fmtChicago(payload);
    else citation = fmtAPA(payload);

    outEl.innerHTML = citation;
    return citation;
  }

  function copyToClipboard(text) {
    if (!navigator.clipboard) {
      const ta = document.createElement('textarea');
      ta.value = text;
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand('copy'); } catch (e) {}
      ta.remove();
      alert('Citation copied (fallback).');
      return;
    }
    navigator.clipboard.writeText(text).catch(() => { alert('Copy failed.'); });
  }

  function save() {
    const citation = generate();
    const saved = JSON.parse(localStorage.getItem(KEY) || '[]');
    saved.push({ citation, at: Date.now() });
    localStorage.setItem(KEY, JSON.stringify(saved.slice(-50)));
    alert('Citation saved locally.');
  }

  function loadLast() {
    const saved = JSON.parse(localStorage.getItem(KEY) || '[]');
    if (!saved.length) { alert('No saved citations.'); return; }
    const last = saved[saved.length - 1];
    outEl.innerHTML = last.citation;
  }

  async function tryFetchHtml(url) {
    // Try direct fetch first (may fail due to CORS)
    try {
      const r = await fetch(url, { method: 'GET', mode: 'cors' });
      if (r.ok) return await r.text();
    } catch (err) {
      console.warn('Direct fetch failed (CORS?), will try proxy', err);
    }
    // Fallback to AllOrigins public proxy (rate-limited). Replace with your own proxy for production.
    try {
      const proxy = 'https://api.allorigins.win/raw?url=' + encodeURIComponent(url);
      const r2 = await fetch(proxy);
      if (r2.ok) return await r2.text();
    } catch (err) {
      console.warn('Proxy fetch failed', err);
    }
    return null;
  }

  function parseMetadataFromHtml(html, url) {
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    const getMeta = (name, prop) => {
      const byName = doc.querySelector(`meta[name="${name}"]`);
      if (byName && byName.content) return byName.content;
      const byProp = doc.querySelector(`meta[property="${prop}"]`);
      if (byProp && byProp.content) return byProp.content;
      const byLink = doc.querySelector(`link[rel="canonical"]`);
      if (name === 'url' && byLink && byLink.href) return byLink.href;
      return null;
    };

    const title = getMeta('title','og:title') || doc.querySelector('title')?.textContent || getMeta('twitter:title','twitter:title');
    const site = getMeta('site_name','og:site_name') || (new URL(url)).hostname.replace(/^www\./,'');
    const author = getMeta('author','article:author') || getMeta('author','og:author') || getMeta('byline','byline');
    const published = getMeta('date','article:published_time') || getMeta('publication_date','publication_date') || getMeta('date','og:updated_time') || getMeta('pubdate','pubdate');

    return { title, site, author, published, url };
  }

  // Format published timestamps into user-friendly strings for each citation style.
  function formatPublishedDate(raw) {
    if (!raw) return null;
    // try parse ISO / common date strings
    const ms = Date.parse(raw);
    if (isNaN(ms)) {
      return { apa: raw, mla: raw, chicago: raw };
    }
    const d = new Date(ms);
    // use UTC parts to avoid timezone shifts from ISO Z strings
    const year = d.getUTCFullYear();
    const monthIdx = d.getUTCMonth();
    const day = d.getUTCDate();
    const months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    const monthName = months[monthIdx];
    return {
      apa: `${year}, ${monthName} ${day}`,      // e.g. "2025, December 4"
      mla: `${day} ${monthName} ${year}`,       // e.g. "4 December 2025"
      chicago: `${year}`                        // Chicago author-date often uses just year for in-text
    };
  }
  
  async function fetchAndFill() {
    const url = (urlEl.value || '').trim();
    if (!url) { alert('Enter a URL first.'); return; }
    fetchBtn.textContent = 'Fetching…';
    fetchBtn.disabled = true;
    try {
      const html = await tryFetchHtml(url);
      if (!html) {
        alert('Failed to fetch page. CORS or proxy error. Consider using a server-side proxy.');
        return;
      }
      const meta = parseMetadataFromHtml(html, url);
      if (meta.author) authorEl.value = meta.author;
      if (meta.published) {
        const fmt = formatPublishedDate(meta.published);
        // choose default format based on selected style
        const style = (styleEl && styleEl.value) ? styleEl.value : 'apa';
        dateEl.value = (fmt && fmt[style]) ? fmt[style] : meta.published;
      }
      if (meta.title) titleEl.value = meta.title;
      if (meta.site) sourceEl.value = meta.site;
      urlEl.value = meta.url || url;
      generate();
      setTimeout(()=>{ fetchBtn.textContent = 'Fetch from URL'; fetchBtn.disabled = false; }, 250);
    } catch (err) {
      console.warn(err);
      alert('Error fetching metadata.');
      fetchBtn.textContent = 'Fetch from URL';
      fetchBtn.disabled = false;
    }
  }

  fetchBtn.addEventListener('click', fetchAndFill);

  // show a default sample on load
  authorEl.value = 'Doe, J.';
  dateEl.value = '2025, May 10';
  titleEl.value = 'Harvard revokes tenure of Francesca Gino after misconduct findings.';
  sourceEl.value = 'The New York Times';
  urlEl.value = 'https://www.nytimes.com/article-link';
  generate();
})();
</script>

---
layout: post 
title: Portfolio Home 
hide: true
show_reading_time: false
---

Hi! My name is [Your Full Name]

### Development Environment

> Coding starts with tools, explore these tools and procedures with a click.

<div style="display: flex; flex-wrap: wrap; gap: 10px;">
    <a href="https://github.com/Open-Coding-Society/student">
        <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
    </a>
    <a href="https://open-coding-society.github.io/student">
        <img src="https://img.shields.io/badge/GitHub%20Pages-327FC7?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Pages">
    </a>
    <a href="https://kasm.opencodingsociety.com/">
        <img src="https://img.shields.io/badge/KASM-0078D4?style=for-the-badge&logo=kasm&logoColor=white" alt="KASM">
    </a>
    <a href="https://vscode.dev/">
        <img src="https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="VSCode">
    </a>
</div>

<br>

### Class Progress

> Here is my progress through coding, click to see these online

<div style="display: flex; flex-wrap: wrap; gap: 10px;">
    <a href="{{site.baseurl}}/snake" style="text-decoration: none;">
        <div style="background-color: #00FF00; color: black; padding: 10px 20px; border-radius: 5px; font-weight: bold;">
            Snake Game
        </div>
    </a>
    <a href="{{site.baseurl}}/turtle" style="text-decoration: none;">
        <div style="background-color: #FF0000; color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold;">
            Turtle
        </div>
    </a>
</div>

<br>

<!-- Contact Section -->
### Get in Touch

> Feel free to reach out if you'd like to collaborate or learn more about our work.

<p style="color: #2A7DB1;">Open Coding Society: <a href="https://opencodingsociety.com" style="color: #2A7DB1; text-decoration: underline;">Socials</a></p>

<!DOCTYPE html>
<html>
<head>
    <title>Mood Checker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }

        h1 {
            margin-bottom: 20px;
        }

        button {
            margin: 5px;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }

        #mood-list {
            margin-top: 20px;
            padding: 10px;
            background: #f3f3f3;
            border-radius: 8px;
        }

        .mood-entry {
            margin-bottom: 8px;
        }
    </style>
</head>
<body>
    <h1>Mood Checker</h1>

    <button onclick="sendMood('Happy')">😀 Happy</button>
    <button onclick="sendMood('Sad')">😢 Sad</button>
    <button onclick="sendMood('Angry')">😡 Angry</button>
    <button onclick="sendMood('Excited')">🤩 Excited</button>

    <h2>All Mood Logs:</h2>
    <div id="mood-list"></div>

    <script src="/static/script.js"></script>
</body>
</html>

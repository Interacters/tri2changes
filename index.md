---
layout: post 
title: Portfolio Home 
hide: true
show_reading_time: false
---

<style>
    :root {
        --primary: #2563eb;
        --primary-dark: #1e40af;
        --success: #059669;
        --gray-50: #f9fafb;
        --gray-100: #f3f4f6;
        --gray-200: #e5e7eb;
        --gray-600: #4b5563;
        --gray-700: #374151;
        --gray-900: #111827;
    }

    body {
        background: linear-gradient(to bottom, #0f172a, #1e293b);
        min-height: 100vh;
    }

    .home-container {
        padding: 2.5rem;
        max-width: 1400px;
        margin: 0 auto;
    }

    .hero-section {
        background: #8787cd;
        border-radius: 12px;
        padding: 3rem 2.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        text-align: center;
    }

    .hero-section h1 {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--gray-900);
        margin: 0 0 1rem 0;
        letter-spacing: -0.025em;
    }

    .hero-section p {
        font-size: 1.1rem;
        color: var(--gray-700);
        margin: 0 0 2rem 0;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
    }

    .tools-section {
        background: #8787cd;
        border-radius: 12px;
        padding: 2rem 2.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }

    .tools-section h2 {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--gray-900);
        margin: 0 0 1.5rem 0;
    }

    .btn-primary {
        background: var(--primary);
        color: white;
        padding: 1rem 2rem;
        border-radius: 8px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        transition: all 0.2s ease;
    }

    .btn-primary:hover {
        background: var(--primary-dark);
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(37, 99, 235, 0.3);
        color: white;
        text-decoration: none;
    }

    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 1.5rem;
        margin-bottom: 2rem;
    }

    .feature-card {
        background: #c9c9f5;
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        transition: all 0.2s ease;
        text-decoration: none;
        display: block;
    }

    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        text-decoration: none;
    }

    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        display: block;
    }

    .feature-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: var(--gray-900);
        margin: 0 0 0.75rem 0;
    }

    .feature-description {
        color: var(--gray-700);
        line-height: 1.6;
        font-size: 0.95rem;
        margin: 0;
    }

    .cta-section {
        background: linear-gradient(135deg, var(--primary), var(--primary-dark));
        border-radius: 12px;
        padding: 2.5rem;
        text-align: center;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    }

    .cta-section h2 {
        font-size: 1.75rem;
        font-weight: 700;
        color: white;
        margin: 0 0 1rem 0;
    }

    .cta-section p {
        color: rgba(255, 255, 255, 0.9);
        margin: 0 0 1.5rem 0;
        font-size: 1.05rem;
    }

    .btn-white {
        background: white;
        color: var(--primary);
        padding: 0.875rem 2rem;
        border-radius: 8px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        transition: all 0.2s ease;
        border: none;
        cursor: pointer;
    }

    .btn-white:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
        color: var(--primary-dark);
        text-decoration: none;
    }

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin-top: 2rem;
    }

    .stat-card {
        background: rgba(255, 255, 255, 0.1);
        padding: 1.5rem;
        border-radius: 8px;
        text-align: center;
        backdrop-filter: blur(10px);
    }

    .stat-number {
        font-size: 2rem;
        font-weight: 700;
        color: white;
        display: block;
        margin-bottom: 0.5rem;
    }

    .stat-label {
        color: rgba(255, 255, 255, 0.8);
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
</style>

<div class="home-container">
    <!-- Hero Section -->
    <div class="hero-section">
        <h1>Welcome to EssayLab</h1>
        <p>Master media literacy, develop critical thinking skills, and become a confident researcher with our comprehensive suite of educational tools.</p>
    </div>

    <!-- Quick Access -->
    <div class="tools-section">
        <h2> Quick Access</h2>
        <p style="color: var(--gray-700); margin-bottom: 1.5rem;">Jump straight to the English Help resources</p>
        <a href="https://interacters.github.io/tri2changes/english_help/" class="btn-primary" style="display: inline-block; background: var(--primary); padding: 1rem 2rem; border-radius: 8px; color: white; text-decoration: none; font-weight: 600; transition: all 0.2s ease;">
            Go to English Help →
        </a>
    </div>




</div>


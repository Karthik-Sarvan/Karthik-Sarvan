\documentclass[10pt,a4paper]{article}

% --- PACKAGES ---
\usepackage[utf8]{inputenc}
\usepackage[margin=0.55in, top=0.55in, bottom=0.55in]{geometry} 
\usepackage{xcolor}
\usepackage{fontawesome5}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{parskip}

% --- FONT SETUP ---
\usepackage[sfdefault]{roboto}
\usepackage[T1]{fontenc}

% --- COLOR PALETTE ---
\definecolor{textblack}{HTML}{2B2B2B}
\definecolor{textgray}{HTML}{666666}
\definecolor{linkblue}{HTML}{1A5276} 
\definecolor{lightgray}{HTML}{F2F2F2}
\definecolor{linegray}{HTML}{D1D1D1}

\color{textblack}
\pagestyle{empty} 

% --- CUSTOM COMMANDS ---

% Section Title with Right-Side Accent Text
\newcommand{\cvsection}[2]{
    \vspace{1.5em}
    \noindent
    \textbf{\uppercase{#1}} \hspace{0.8em} {\color{linegray}\hrulefill} \hspace{0.8em} \textcolor{textblack}{#2}
    \vspace{0.8em}
}

% Standard Section Title
\newcommand{\cvsectionstandard}[1]{
    \vspace{1.5em}
    \noindent
    \textbf{\uppercase{#1}} \hspace{0.8em} {\color{linegray}\hrulefill}
    \vspace{0.8em}
}

% Split Layout for Experience/Projects
\newcommand{\cventry}[6]{
    \noindent
    \begin{minipage}[t]{0.22\textwidth}
        \raggedright
        \textbf{#1} \\[0.4em]
        \textcolor{textgray}{\scriptsize #2} \\[0.2em]
        \textcolor{textgray}{\scriptsize #3}
    \end{minipage}%
    \begin{minipage}[t]{0.04\textwidth}
        \centering \vspace{0.2em} \textcolor{linegray}{\textbullet}
    \end{minipage}%
    \begin{minipage}[t]{0.74\textwidth}
        \raggedright
        \textbf{#4} #5 \\[0.4em]
        \small #6
    \end{minipage}
    \par\vspace{1.2em}
}

% Reusable Footer Command for multi-page consistency
\newcommand{\cvfooter}{
    \vfill
    \begin{center}
        \colorbox{lightgray}{
            \makebox[\dimexpr\textwidth-2\fboxsep\relax]{
                \vspace{0.4em}
                \small \textcolor{textblack}{
                    \faPhone \hspace{0.3em} +91 6281858488 \quad \textbar \quad 
                    \faEnvelope \hspace{0.3em} karthiks1mail@gmail.com
                }
                \vspace{0.4em}
            }
        }
    \end{center}
}

\begin{document}

% ==========================================
% PAGE 1: HEADER & CORE EXPERIENCE
% ==========================================
\noindent
\begin{minipage}[c]{0.55\textwidth}
    \raggedright
    {\fontsize{28}{32}\selectfont \textbf{\uppercase{Karthik Sarvan}}} \\ \vspace{0.4em}
    {\Large \textcolor{textgray}{Embedded Engineer}}
\end{minipage}%
\textcolor{linegray}{\vrule width 1.2pt height 1.6cm}%
\hspace{0.04\textwidth}%
\begin{minipage}[c]{0.40\textwidth}
    \raggedleft \small
    \textcolor{textgray}{\faGithub} \hspace{0.3em} \href{https://github.com/Karthik-Sarvan}{github.com/Karthik-Sarvan} \\[0.4em]
    \textcolor{textgray}{\faLinkedin} \hspace{0.3em} \href{https://linkedin.com/in/Karthik-Sarvan}{linkedin.com/in/Karthik-Sarvan} \\[0.4em]
    \textcolor{textgray}{\faGlobe} \hspace{0.3em} \href{https://pratibim.tech/karthik}{pratibim.tech/karthik}
\end{minipage}

% ==========================================
% ABOUT ME
% ==========================================
\cvsection{About Me}{Hardware \textbar{} Firmware \textbar{} Systems}

\noindent \small
I’m an Electronics and Communication engineering student who loves building things from the ground up—whether that’s writing bare-metal firmware, designing custom hardware, or bridging the gap between physical sensors and modern web architectures. I thrive on solving complex problems, writing safe and concurrent systems in Rust, and diving deep into low-level micro-controller operations.

% ==========================================
% WORK EXPERIENCE
% ==========================================
\cvsectionstandard{Work Experience}

\cventry{Aegion Dynamic Solutions}{Dec 2025 -- Present}{Visakhapatnam, India}{Embedded Intern}{}{
    Gaining hands-on experience designing and optimizing embedded systems. I focus on microcontroller-based designs, real-time hardware-software integration, and writing highly efficient low-level firmware in C and Rust to keep hardware running reliably.
}

\cventry{Reaidy.io}{Sept 2024 -- Apr 2025}{Visakhapatnam, India}{MERN Stack Developer}{}{
    Worked on REAIDY, a platform built to help users practice for specialized interviews. I developed the core AI features, guided my team through technical roadblocks, and actively contributed to the product's overall software architecture.
}

\cventry{Spotmies LLP}{June 2023 -- Dec 2023}{Visakhapatnam, India}{React Intern}{}{
    Interned as a web developer where I learned the ropes of production-level MERN stack development. I collaborated closely with cross-functional teams and clients to ship solid, responsive web applications.
}

% ==========================================
% EDUCATION & SKILLS 
% ==========================================
\vspace{0.5em}
\noindent
\begin{minipage}[t]{0.46\textwidth}
    \textbf{\uppercase{Education}} \hspace{0.5em} {\color{linegray}\hrulefill}
    \vspace{1.2em}
    
    \textbf{Chaitanya Engineering College} \\
    \textcolor{textgray}{\small 2023 -- Present} \\
    \small Pursuing B.Tech in Electronics \& Communication
    \vspace{1.5em}
    
    \textbf{Gov. Polytechnic Pendurti} \\
    \textcolor{textgray}{\small Completed} \\
    \small Diploma in Electronics \& Communication
\end{minipage}
\hfill
\begin{minipage}[t]{0.48\textwidth}
    \textbf{\uppercase{Skills}} \hspace{0.5em} {\color{linegray}\hrulefill}
    \vspace{1.2em}
    
    \textbf{Languages:} \\
    \textcolor{textgray}{\small Rust, C/C++, JavaScript, Python}
    \vspace{0.8em}
    
    \textbf{Frameworks \& Web:} \\
    \textcolor{textgray}{\small MERN Stack, React, Node.js}
    \vspace{0.8em}
    
    \textbf{Hardware \& Systems:} \\
    \textcolor{textgray}{\small Embedded Firmware, Microcontrollers (STM32), PCB Design, Linux Kernel, Control Systems (PID), Git}
\end{minipage}
\vspace{0.5em}

% ==========================================
% FEATURED PROJECTS (Start Page 1)
% ==========================================
\cvsectionstandard{Projects}

\cventry{Pratibim}{\href{https://pratibim.tech}{\textcolor{linkblue}{\faExternalLinkAlt \hspace{0.1em} pratibim.tech}}}{EDA Tool \textbar{} Rust, AI}{Core Developer}{}{
    An AI-driven Electronic Design Automation (EDA) tool that acts as a co-pilot for hardware engineers. It autonomously designs circuit schematics by analyzing component datasheets. I built the memory-safe core engine in Rust to make the complex backend highly scalable and fast.
}

\cventry{Mimic}{\href{https://mimic.aegiondynamic.com}{\textcolor{linkblue}{\faExternalLinkAlt \hspace{0.1em} mimic.aegion...}}}{Firmware \textbar{} STM32}{Firmware Engineer}{\textbar{} Proxy Framework}{
    A hardware emulation framework that acts as a proxy for physical sensors. It helps firmware engineers test I2C, SPI, and UART protocols using an STM32 board when they lack the actual hardware. I built the bare-metal C firmware and the Python bridge that connects it to the host computer.
}

% Print Footer and trigger page break
\cvfooter
\newpage

% ==========================================
% PAGE 2: PROJECTS CONTINUED
% ==========================================
\vspace*{0.5em} % Small buffer at the top of the new page
\cvsectionstandard{Projects (Continued)}

\cventry{Relay Test System}{\href{https://github.com/Karthik-Sarvan}{\textcolor{linkblue}{\faExternalLinkAlt \hspace{0.1em} view project}}}{Diagnostics \textbar{} PCB}{Embedded Engineer}{}{
    Built a portable, automated diagnostic unit to validate relays in the field. I wrote the firmware to run precise, automated test sequences for contact resistance, relay bounce, and exact pickup/drop voltage thresholds.
}

\cventry{Defense Project}{\textcolor{textgray}{\faLock \hspace{0.1em} Confidential}}{Control Systems}{Firmware Engineer}{\textbar{} Multi-Axis Actuation}{
    Architected highly reliable firmware and tuned strict Proportional-Integral-Derivative (PID) controllers for precise multi-axis motor actuation within a secure, closed-loop defense application.
}

\cventry{PID Balancer}{\href{https://github.com/Karthik-Sarvan}{\textcolor{linkblue}{\faExternalLinkAlt \hspace{0.1em} view demo}}}{Hardware Lab}{Embedded Engineer}{\textbar{} Closed-Loop Logic}{
    Built a real-time hardware control system utilizing custom PID algorithms to dynamically adjust platform tilt and continuously balance a freely moving object using fast-response spatial sensor feedback mapping.
}

\cventry{Next Project}{\href{https://github.com/Karthik-Sarvan}{\textcolor{linkblue}{\faExternalLinkAlt \hspace{0.1em} view project}}}{Tech Stack}{Your Role}{}{
    Replace this text with the description of another project. You can copy/paste this block to add as many projects as you need. Keep the descriptions to 2-3 lines to maintain the clean editorial formatting of the document.
}

% Print Footer at the bottom of Page 2
\cvfooter

\end{document}

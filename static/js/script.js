// Global variables
let currentProblem = null;
let currentLanguage = 'Python';
let allProblems = {};

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    loadProblems();
    setupEventListeners();
    initializeSearch();
}

function setupEventListeners() {
    // Language selection
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            currentLanguage = this.dataset.language;
        });
    });

    // Filter buttons
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            filterProblems(this.dataset.difficulty);
        });
    });

    // Keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        if (e.ctrlKey && e.key === 'k') {
            e.preventDefault();
            document.getElementById('search-input').focus();
        }
        if (e.key === 'Escape') {
            if (document.getElementById('problem-details').style.display !== 'none') {
                hideProblemDetails();
            }
        }
    });
}

function loadProblems() {
    // Try to fetch from backend first
    fetch('/get_problem_categories')
        .then(response => response.json())
        .then(data => {
            allProblems = data;
            displayProblems();
        })
        .catch(error => {
            console.log('Using fallback problems data');
            // Fallback to hardcoded data if backend is not available
            allProblems = {
                "Two Sum": {
                    "statement": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
                    "difficulty": "Easy",
                    "category": "Array, Hash Table",
                    "tags": ["array", "hash-table", "two-pointers"]
                },
                "Valid Parentheses": {
                    "statement": "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
                    "difficulty": "Easy",
                    "category": "String, Stack",
                    "tags": ["string", "stack", "matching"]
                },
                "Reverse Linked List": {
                    "statement": "Given the head of a singly linked list, reverse the list, and return the reversed list.",
                    "difficulty": "Easy",
                    "category": "Linked List, Recursion",
                    "tags": ["linked-list", "recursion", "two-pointers"]
                },
                "Binary Tree Inorder Traversal": {
                    "statement": "Given the root of a binary tree, return the inorder traversal of its nodes' values.",
                    "difficulty": "Easy",
                    "category": "Tree, Depth-First Search",
                    "tags": ["tree", "dfs", "inorder", "recursion"]
                },
                "Climbing Stairs": {
                    "statement": "You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?",
                    "difficulty": "Easy",
                    "category": "Dynamic Programming, Math",
                    "tags": ["dynamic-programming", "math", "fibonacci"]
                },
                "Maximum Subarray": {
                    "statement": "Given an integer array nums, find the subarray with the largest sum, and return its sum.",
                    "difficulty": "Medium",
                    "category": "Array, Dynamic Programming",
                    "tags": ["array", "dynamic-programming", "divide-and-conquer"]
                },
                "Longest Substring Without Repeating Characters": {
                    "statement": "Given a string s, find the length of the longest substring without repeating characters.",
                    "difficulty": "Medium",
                    "category": "String, Sliding Window",
                    "tags": ["string", "sliding-window", "hash-table"]
                },
                "Container With Most Water": {
                    "statement": "Given n non-negative integers height where each represents a point at coordinate (i, height[i]). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.",
                    "difficulty": "Medium",
                    "category": "Array, Two Pointers",
                    "tags": ["array", "two-pointers", "greedy"]
                },
                "Trapping Rain Water": {
                    "statement": "Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.",
                    "difficulty": "Hard",
                    "category": "Array, Two Pointers",
                    "tags": ["array", "two-pointers", "dynamic-programming", "stack"]
                },
                "Binary Tree Maximum Path Sum": {
                    "statement": "A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root. The path sum of a path is the sum of the node's values in the path. Given the root of a binary tree, return the maximum path sum of any non-empty path.",
                    "difficulty": "Hard",
                    "category": "Tree, Dynamic Programming",
                    "tags": ["tree", "dynamic-programming", "dfs", "path-sum"]
                }
            };
            displayProblems();
        });
}

function displayProblems() {
    const grid = document.getElementById('problems-grid');
    grid.innerHTML = '';

    // Count problems by difficulty
    let easyCount = 0, mediumCount = 0, hardCount = 0;
    
    Object.entries(allProblems).forEach(([problemName, problemDetails]) => {
        // Count by difficulty
        if (problemDetails.difficulty === 'Easy') easyCount++;
        else if (problemDetails.difficulty === 'Medium') mediumCount++;
        else if (problemDetails.difficulty === 'Hard') hardCount++;
        
        const card = document.createElement('div');
        card.className = 'problem-card';
        card.onclick = () => showProblemDetails(problemName);
        
        // Create difficulty badge with appropriate color
        const difficultyClass = problemDetails.difficulty.toLowerCase();
        
        card.innerHTML = `
            <h3>${problemName}</h3>
            <div class="problem-meta">
                <span class="difficulty-badge ${difficultyClass}">${problemDetails.difficulty}</span>
                <span class="category-badge">${problemDetails.category}</span>
            </div>
            <div class="problem-tags">
                ${problemDetails.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
            </div>
        `;
        
        grid.appendChild(card);
    });
    
    // Update statistics
    document.getElementById('total-problems').textContent = Object.keys(allProblems).length;
    document.getElementById('easy-problems').textContent = easyCount;
    document.getElementById('medium-problems').textContent = mediumCount;
    document.getElementById('hard-problems').textContent = hardCount;
}

function showProblemDetails(problemName) {
    currentProblem = problemName;
    
    // Fetch problem details
    fetch(`/get_problem?name=${encodeURIComponent(problemName)}`)
        .then(response => response.json())
        .then(problem => {
            if (problem.error) {
                showToast('Problem not found', 'error');
                return;
            }

            // Update UI
            document.getElementById('problem-title').textContent = problemName;
            document.getElementById('problem-statement-text').textContent = problem.statement;
            document.getElementById('problem-difficulty').textContent = problem.difficulty;
            document.getElementById('problem-category').textContent = problem.category;
            
            // Show problem details, hide problem selection
            document.getElementById('problem-selection').style.display = 'none';
            document.getElementById('problem-details').style.display = 'block';
            document.getElementById('solution-container').style.display = 'none';
            
            // Reset language selection
            document.querySelectorAll('.lang-btn').forEach(btn => btn.classList.remove('active'));
            document.querySelector('.lang-btn[data-language="Python"]').classList.add('active');
            currentLanguage = 'Python';
            
            // Smooth scroll to top
            window.scrollTo({ top: 0, behavior: 'smooth' });
        })
        .catch(error => {
            console.error('Error fetching problem:', error);
            showToast('Error loading problem details', 'error');
        });
}

function hideProblemDetails() {
    document.getElementById('problem-selection').style.display = 'block';
    document.getElementById('problem-details').style.display = 'none';
    document.getElementById('solution-container').style.display = 'none';
    currentProblem = null;
    
    // Smooth scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function solveProblem() {
    if (!currentProblem) {
        showToast('No problem selected', 'error');
        return;
    }

    if (!currentLanguage) {
        showToast('Please select a programming language', 'error');
        return;
    }

    // Show solution container and loading state
    document.getElementById('solution-container').style.display = 'block';
    document.getElementById('loading-spinner').style.display = 'block';
    document.getElementById('solution-sections').style.display = 'none';
    document.getElementById('error-message').style.display = 'none';
    
    // Update solution header
    document.getElementById('solution-problem-name').textContent = currentProblem;
    document.getElementById('solution-language-display').textContent = currentLanguage;
    
    // Smooth scroll to solution
    document.getElementById('solution-container').scrollIntoView({ behavior: 'smooth' });

    // Prepare request data
    const requestData = {
        problem_name: currentProblem,
        problem_statement: document.getElementById('problem-statement-text').textContent,
        language: currentLanguage
    };

    // Call backend API
    fetch('/solve_problem', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('loading-spinner').style.display = 'none';
        
        if (data.success) {
            displaySolution(data.solution);
        } else {
            document.getElementById('error-message').style.display = 'block';
            showToast('Error: ' + data.error, 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('loading-spinner').style.display = 'none';
        document.getElementById('error-message').style.display = 'block';
        showToast('Network error. Please try again.', 'error');
    });
}

function displaySolution(solutionText) {
    // Parse the solution text into sections
    const sections = parseSolutionText(solutionText);
    
    // Display explanation
    document.getElementById('solution-explanation').innerHTML = sections.explanation || '<p>No explanation provided.</p>';
    
    // Display code with syntax highlighting
    const codeElement = document.getElementById('solution-code');
    codeElement.textContent = sections.code || '// No code provided';
    codeElement.className = `language-${getLanguageClass(currentLanguage)}`;
    
    // Re-highlight the code
    if (window.Prism) {
        Prism.highlightElement(codeElement);
    }
    
    // Display complexity analysis
    document.getElementById('complexity-analysis').innerHTML = sections.complexity || '<p>No complexity analysis provided.</p>';
    
    // Display dry run examples
    document.getElementById('dry-run-examples').innerHTML = sections.dryRun || '<p>No dry run examples provided.</p>';
    
    // Display alternative approaches
    document.getElementById('alternative-approaches').innerHTML = sections.alternatives || '<p>No alternative approaches provided.</p>';
    
    // Show solution sections
    document.getElementById('solution-sections').style.display = 'block';
}

function parseSolutionText(text) {
    const sections = {
        explanation: '',
        code: '',
        complexity: '',
        dryRun: '',
        alternatives: ''
    };
    
    // Split text into sections based on the structured format
    const explanationMatch = text.match(/EXPLANATION:(.*?)(?=CODE:|$)/s);
    const codeMatch = text.match(/CODE:(.*?)(?=COMPLEXITY ANALYSIS:|$)/s);
    const complexityMatch = text.match(/COMPLEXITY ANALYSIS:(.*?)(?=DRY RUN EXAMPLES:|$)/s);
    const dryRunMatch = text.match(/DRY RUN EXAMPLES:(.*?)(?=ALTERNATIVE APPROACHES:|$)/s);
    const alternativesMatch = text.match(/ALTERNATIVE APPROACHES:(.*?)$/s);
    
    if (explanationMatch) {
        sections.explanation = explanationMatch[1].trim();
    }
    
    if (codeMatch) {
        sections.code = codeMatch[1].trim();
    }
    
    if (complexityMatch) {
        sections.complexity = complexityMatch[1].trim();
    }
    
    if (dryRunMatch) {
        sections.dryRun = dryRunMatch[1].trim();
    }
    
    if (alternativesMatch) {
        sections.alternatives = alternativesMatch[1].trim();
    }
    
    // If structured parsing fails, fall back to keyword-based parsing
    if (!sections.explanation && !sections.code) {
        return fallbackParseSolutionText(text);
    }
    
    return sections;
}

function fallbackParseSolutionText(text) {
    const sections = {
        explanation: '',
        code: '',
        complexity: '',
        dryRun: '',
        alternatives: ''
    };
    
    // Split text into lines
    const lines = text.split('\n');
    let currentSection = 'explanation';
    let sectionContent = [];
    
    for (let line of lines) {
        const trimmedLine = line.trim();
        
        // Detect section headers
        if (trimmedLine.toLowerCase().includes('explanation') || 
            trimmedLine.toLowerCase().includes('approach') ||
            trimmedLine.toLowerCase().includes('solution')) {
            if (sectionContent.length > 0) {
                sections[currentSection] = sectionContent.join('\n').trim();
            }
            currentSection = 'explanation';
            sectionContent = [];
            continue;
        }
        
        if (trimmedLine.toLowerCase().includes('code') || 
            trimmedLine.toLowerCase().includes('implementation')) {
            if (sectionContent.length > 0) {
                sections[currentSection] = sectionContent.join('\n').trim();
            }
            currentSection = 'code';
            sectionContent = [];
            continue;
        }
        
        if (trimmedLine.toLowerCase().includes('complexity') || 
            trimmedLine.toLowerCase().includes('time') ||
            trimmedLine.toLowerCase().includes('space')) {
            if (sectionContent.length > 0) {
                sections[currentSection] = sectionContent.join('\n').trim();
            }
            currentSection = 'complexity';
            sectionContent = [];
            continue;
        }
        
        if (trimmedLine.toLowerCase().includes('dry run') || 
            trimmedLine.toLowerCase().includes('example') ||
            trimmedLine.toLowerCase().includes('test case')) {
            if (sectionContent.length > 0) {
                sections[currentSection] = sectionContent.join('\n').trim();
            }
            currentSection = 'dryRun';
            sectionContent = [];
            continue;
        }
        
        if (trimmedLine.toLowerCase().includes('alternative') || 
            trimmedLine.toLowerCase().includes('other') ||
            trimmedLine.toLowerCase().includes('different')) {
            if (sectionContent.length > 0) {
                sections[currentSection] = sectionContent.join('\n').trim();
            }
            currentSection = 'alternatives';
            sectionContent = [];
            continue;
        }
        
        // Add line to current section
        sectionContent.push(line);
    }
    
    // Add the last section
    if (sectionContent.length > 0) {
        sections[currentSection] = sectionContent.join('\n').trim();
    }
    
    return sections;
}

function getLanguageClass(language) {
    const languageMap = {
        'Python': 'python',
        'Java': 'java',
        'C++': 'cpp'
    };
    return languageMap[language] || 'python';
}

function copyCode() {
    const codeElement = document.getElementById('solution-code');
    const copyBtn = document.querySelector('.copy-btn');
    
    // Modern clipboard API
    if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(codeElement.textContent).then(() => {
            copyBtn.classList.add('copied');
            copyBtn.textContent = '✅ Copied!';
            showToast('Code copied to clipboard!', 'success');
            
            setTimeout(() => {
                copyBtn.classList.remove('copied');
                copyBtn.textContent = '📋 Copy Code';
            }, 2000);
        }).catch(err => {
            console.error('Failed to copy: ', err);
            fallbackCopy();
        });
    } else {
        fallbackCopy();
    }
}

function fallbackCopy() {
    const codeElement = document.getElementById('solution-code');
    const copyBtn = document.querySelector('.copy-btn');
    
    const textArea = document.createElement('textarea');
    textArea.value = codeElement.textContent;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand('copy');
    document.body.removeChild(textArea);
    
    copyBtn.classList.add('copied');
    copyBtn.textContent = '✅ Copied!';
    showToast('Code copied to clipboard!', 'success');
    
    setTimeout(() => {
        copyBtn.classList.remove('copied');
        copyBtn.textContent = '📋 Copy Code';
    }, 2000);
}

function filterProblems(difficulty) {
    const grid = document.getElementById('problems-grid');
    grid.innerHTML = '';
    
    let easyCount = 0, mediumCount = 0, hardCount = 0;
    
    Object.entries(allProblems).forEach(([problemName, problemDetails]) => {
        // Count problems by difficulty
        if (problemDetails.difficulty === 'Easy') easyCount++;
        else if (problemDetails.difficulty === 'Medium') mediumCount++;
        else if (problemDetails.difficulty === 'Hard') hardCount++;
        
        // Filter by difficulty
        if (difficulty === 'all' || problemDetails.difficulty === difficulty) {
            const card = document.createElement('div');
            card.className = 'problem-card';
            card.onclick = () => showProblemDetails(problemName);
            
            // Create difficulty badge with appropriate color
            const difficultyClass = problemDetails.difficulty.toLowerCase();
            
            card.innerHTML = `
                <h3>${problemName}</h3>
                <div class="problem-meta">
                    <span class="difficulty-badge ${difficultyClass}">${problemDetails.difficulty}</span>
                    <span class="category-badge">${problemDetails.category}</span>
                </div>
                <div class="problem-tags">
                    ${problemDetails.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
                </div>
            `;
            
            grid.appendChild(card);
        }
    });
    
    // Update statistics based on filtered results
    if (difficulty === 'all') {
        document.getElementById('easy-problems').textContent = easyCount;
        document.getElementById('medium-problems').textContent = mediumCount;
        document.getElementById('hard-problems').textContent = hardCount;
    } else {
        // Show only the filtered difficulty count
        const filteredCount = difficulty === 'Easy' ? easyCount : 
                             difficulty === 'Medium' ? mediumCount : 
                             difficulty === 'Hard' ? hardCount : 0;
        document.getElementById('easy-problems').textContent = difficulty === 'Easy' ? filteredCount : 0;
        document.getElementById('medium-problems').textContent = difficulty === 'Medium' ? filteredCount : 0;
        document.getElementById('hard-problems').textContent = difficulty === 'Hard' ? filteredCount : 0;
    }
}

function initializeSearch() {
    const searchInput = document.getElementById('search-input');
    let searchTimeout;
    
    searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            const query = this.value.toLowerCase();
            searchProblems(query);
        }, 300);
    });
}

function searchProblems(query) {
    if (!query.trim()) {
        displayProblems();
        return;
    }
    
    const grid = document.getElementById('problems-grid');
    grid.innerHTML = '';
    
    Object.entries(allProblems).forEach(([problemName, problemDetails]) => {
        if (problemName.toLowerCase().includes(query) || 
            problemDetails.category.toLowerCase().includes(query) ||
            problemDetails.difficulty.toLowerCase().includes(query) ||
            (problemDetails.tags && problemDetails.tags.some(tag => tag.toLowerCase().includes(query)))) {
            const card = document.createElement('div');
            card.className = 'problem-card';
            card.onclick = () => showProblemDetails(problemName);
            
            // Create difficulty badge with appropriate color
            const difficultyClass = problemDetails.difficulty.toLowerCase();
            
            card.innerHTML = `
                <h3>${problemName}</h3>
                <div class="problem-meta">
                    <span class="difficulty-badge ${difficultyClass}">${problemDetails.difficulty}</span>
                    <span class="category-badge">${problemDetails.category}</span>
                </div>
                <div class="problem-tags">
                    ${problemDetails.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
                </div>
            `;
            
            grid.appendChild(card);
        }
    });
}

function showToast(message, type = 'info') {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.className = `toast show ${type}`;
    
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// Utility functions
function smoothScrollTo(element) {
    element.scrollIntoView({ behavior: 'smooth' });
}

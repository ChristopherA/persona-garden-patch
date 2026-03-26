import os
import re
import sys

garden = sys.argv[1]

# Directories that need index pages (only ones with content, not forms/)
dirs_to_index = {
    'glosses': ('Glosses', 'Interpretive definitions that frame concepts through a broader lens.'),
    'models': ('Models', 'Structural representations showing how elements relate to each other.'),
    'convictions': ('Convictions', 'Claims about how the world works, grounded in experience.'),
    'decisions': ('Decisions', 'Recorded choices with reasoning and alternatives considered.'),
    'patterns': ('Patterns', 'Recurring solutions that resolve specific tensions.'),
    'principles': ('Principles', 'Standing constraints on what we must always or never do.'),
    'inquiries': ('Inquiries', 'Open questions worth investigating, with possible directions.'),
    'boundaries': ('Boundaries', 'Declarations of where authority ends and who may decide what.'),
    'citations': ('Citations', 'Structured dossiers on published works with analysis and insights.'),
    'domains': ('Knowledge Domains', 'Active indexes for knowledge areas that cross-cut form types.'),
    'protocols': ('Protocols', 'Specifications for multi-party coordination across trust boundaries.'),
    'scenarios': ('Scenarios', 'Possible futures that test assumptions and reveal implications.'),
    'values': ('Values', 'Orientations toward what matters — abstract commitments that shape principles.'),
    'personas': ('Personas', 'Design documents for agent identities — behavioral scope, blind spots, and operational architecture.'),
    'forms': ('Form Type Definitions', 'Structural contracts defining what each form type answers and how it is organized.'),
}

for dirname, (title, description) in dirs_to_index.items():
    dirpath = os.path.join(garden, dirname)
    if not os.path.isdir(dirpath):
        continue
    
    # Collect all .md files (not index.md, not analysis.md/insights.md)
    entries = []
    for root, dirs, files in os.walk(dirpath):
        # Only top-level files or compound lead files
        rel = os.path.relpath(root, dirpath)
        depth = 0 if rel == '.' else rel.count(os.sep) + 1
        
        for f in files:
            if not f.endswith('.md') or f == 'index.md':
                continue
            if f in ('analysis.md', 'insights.md'):
                continue
            
            filepath = os.path.join(root, f)
            stem = f[:-3]
            
            # Read brief_summary from YAML
            with open(filepath) as fh:
                content = fh.read()
            
            brief = ''
            tagline = ''
            fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if fm_match:
                fm = fm_match.group(1)
                bm = re.search(r'brief_summary:\s*"([^"]*)"', fm)
                if bm: brief = bm.group(1)
                tm = re.search(r'tagline:\s*"([^"]*)"', fm)
                if tm: tagline = tm.group(1)
            
            # Compute relative link from index.md in this dir
            rel_path = os.path.relpath(filepath, dirpath)
            html_path = rel_path[:-3] + '.html'
            html_path = html_path.replace(' ', '%20').replace('(', '%28').replace(')', '%29')
            
            summary = tagline or brief or ''
            # Truncate brief if too long for index
            if len(summary) > 200:
                summary = summary[:197] + '...'
            
            entries.append((stem, html_path, summary))
    
    entries.sort(key=lambda x: x[0])
    
    # Generate index
    lines = [f'# {title}', '', description, '']
    
    for stem, path, summary in entries:
        if summary:
            lines.append(f'**[{stem}]({path})** — {summary}')
        else:
            lines.append(f'**[{stem}]({path})**')
        lines.append('')
    
    lines.append(f'*{len(entries)} nodes in this section.*')
    lines.append('')
    
    index_path = os.path.join(dirpath, 'index.md')
    with open(index_path, 'w') as fh:
        fh.write('\n'.join(lines))
    print(f"  {dirname}/index.md: {len(entries)} entries")


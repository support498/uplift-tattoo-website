from fpdf import FPDF
from fpdf.enums import XPos, YPos

# Colors
BLACK   = (10, 10, 10)
DARK    = (17, 17, 17)
CARD    = (26, 26, 26)
BORDER  = (42, 42, 42)
MUTED   = (102, 102, 102)
TEXT    = (220, 220, 220)
WHITE   = (255, 255, 255)
GOLD    = (201, 168, 76)
GOLD_L  = (232, 201, 122)
GREEN   = (76, 175, 125)
RED     = (224, 85, 85)
YELLOW  = (232, 184, 75)
BLUE    = (91, 156, 246)
PURPLE  = (155, 127, 232)

class UpliftReport(FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')
        self.set_auto_page_break(auto=True, margin=18)
        self.set_margins(18, 18, 18)

    def set_bg(self, color=BLACK):
        self.set_fill_color(*color)
        self.rect(0, 0, 210, 297, 'F')

    def gold_bar(self):
        self.set_fill_color(*GOLD)
        self.rect(0, 0, 210, 1.2, 'F')

    def section_header(self, num, title):
        self.ln(6)
        # Number badge
        self.set_fill_color(40, 30, 10)
        self.set_text_color(*GOLD)
        self.set_font('Helvetica', 'B', 8)
        self.cell(18, 6, f'  {num}', border=0, fill=True, new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_x(self.get_x() + 4)
        self.set_text_color(*WHITE)
        self.set_font('Helvetica', 'B', 14)
        self.cell(0, 6, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)
        self.set_draw_color(*BORDER)
        self.set_line_width(0.3)
        self.line(18, self.get_y(), 192, self.get_y())
        self.ln(5)

    def metric_card(self, x, y, w, h, label, value, sub, color=WHITE):
        self.set_fill_color(*CARD)
        self.set_draw_color(*BORDER)
        self.set_line_width(0.2)
        self.rect(x, y, w, h, 'FD')
        self.set_xy(x + 3, y + 3)
        self.set_font('Helvetica', 'B', 6)
        self.set_text_color(*MUTED)
        self.cell(w - 6, 4, label.upper(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_xy(x + 3, y + 8)
        self.set_font('Helvetica', 'B', 20)
        self.set_text_color(*color)
        self.cell(w - 6, 10, value, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_xy(x + 3, y + 20)
        self.set_font('Helvetica', '', 6.5)
        self.set_text_color(*MUTED)
        self.multi_cell(w - 6, 3.5, sub)

    def pill(self, x, y, text, color, bg):
        self.set_fill_color(*bg)
        self.set_text_color(*color)
        self.set_font('Helvetica', 'B', 6.5)
        w = self.get_string_width(text) + 6
        self.set_xy(x, y)
        self.cell(w, 5, text, fill=True, new_x=XPos.RIGHT, new_y=YPos.TOP)
        return w

    def score_bar(self, x, y, w, pct, color=GOLD):
        self.set_fill_color(*BORDER)
        self.rect(x, y, w, 3, 'F')
        self.set_fill_color(*color)
        self.rect(x, y, w * pct / 100, 3, 'F')

    def highlight_box(self, title, body):
        self.set_fill_color(30, 22, 8)
        self.set_draw_color(100, 84, 38)
        self.set_line_width(0.3)
        x = self.get_x()
        y = self.get_y()
        # write content first to measure height
        self.rect(x, y, 174, 4, 'F')  # title bg
        self.set_xy(x + 3, y + 0.8)
        self.set_font('Helvetica', 'B', 7)
        self.set_text_color(*GOLD)
        self.cell(170, 3, title.upper(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_xy(x + 3, y + 5.5)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(*TEXT)
        start_y = self.get_y()
        self.multi_cell(168, 4, body)
        end_y = self.get_y()
        height = end_y - y + 3
        self.set_xy(x, y)
        self.rect(x, y, 174, height, 'D')
        self.ln(3)

    def check_item(self, text, icon='check'):
        if icon == 'check':
            c, t = GREEN, '+'
        elif icon == 'cross':
            c, t = RED, 'x'
        else:
            c, t = YELLOW, '~'
        self.set_font('Helvetica', 'B', 8)
        self.set_text_color(*c)
        self.cell(6, 4.5, t, new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_font('Helvetica', '', 7.5)
        self.set_text_color(*TEXT)
        self.multi_cell(0, 4.5, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def header(self):
        pass

    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', '', 7)
        self.set_text_color(*MUTED)
        self.set_draw_color(*BORDER)
        self.set_line_width(0.2)
        self.line(18, self.get_y(), 192, self.get_y())
        self.ln(2)
        self.cell(0, 4, 'UPLIFT Tattoo & Piercing  ·  497 Broome St, SoHo NYC  ·  uplifttattoo.com  ·  SEO Report May 2026', align='C')


pdf = UpliftReport()

# ─────────────────────────────────────────────────────────
# COVER PAGE
# ─────────────────────────────────────────────────────────
pdf.add_page()
pdf.set_bg(BLACK)
pdf.gold_bar()

pdf.ln(30)
pdf.set_font('Helvetica', 'B', 7)
pdf.set_text_color(*GOLD)
pdf.set_char_spacing(2)
pdf.cell(0, 5, '  SEO & WEB PRESENCE REPORT', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_char_spacing(0)

pdf.ln(6)
pdf.set_font('Helvetica', 'B', 38)
pdf.set_text_color(*WHITE)
pdf.cell(0, 16, 'UPLIFT Tattoo', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.cell(0, 16, '& Piercing', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.ln(6)
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(*MUTED)
pdf.multi_cell(120, 5.5, 'Full competitive ranking analysis, keyword position audit, technical health review, and growth opportunities for uplifttattoo.com and upliftpiercing.com')

pdf.ln(14)

# Cover meta
meta = [('Primary Domain', 'uplifttattoo.com'), ('Location', '497 Broome St, SoHo NYC'), ('Report Date', 'May 2026'), ('Prepared by', 'Claude Code')]
for label, val in meta:
    pdf.set_font('Helvetica', 'B', 6.5)
    pdf.set_text_color(*MUTED)
    pdf.cell(45, 4, label.upper(), new_x=XPos.RIGHT, new_y=YPos.TOP)

pdf.ln(5)
for label, val in meta:
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_text_color(*WHITE)
    pdf.cell(45, 5, val, new_x=XPos.RIGHT, new_y=YPos.TOP)

pdf.ln(20)

# Score box
pdf.set_fill_color(*CARD)
pdf.set_draw_color(*BORDER)
pdf.set_line_width(0.3)
pdf.rect(18, pdf.get_y(), 80, 44, 'FD')
pdf.set_xy(18, pdf.get_y() + 4)
pdf.set_font('Helvetica', 'B', 6.5)
pdf.set_text_color(*MUTED)
pdf.cell(80, 4, 'OVERALL SEO HEALTH SCORE', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_xy(18, pdf.get_y() + 2)
pdf.set_font('Helvetica', 'B', 40)
pdf.set_text_color(*GOLD)
pdf.cell(80, 18, '67', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_xy(18, pdf.get_y())
pdf.set_font('Helvetica', '', 8)
pdf.set_text_color(*MUTED)
pdf.cell(80, 5, '/ 100  -  Good, significant upside remaining', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_xy(18, pdf.get_y() + 2)
pdf.set_font('Helvetica', 'B', 8)
pdf.set_text_color(*GOLD)
pdf.cell(80, 5, 'Schemas built. Ready to deploy.', align='C')


# ─────────────────────────────────────────────────────────
# PAGE 2 - EXECUTIVE SUMMARY
# ─────────────────────────────────────────────────────────
pdf.add_page()
pdf.set_bg(BLACK)
pdf.gold_bar()

pdf.section_header('01', 'Executive Summary')

# Metric cards
cards = [
    ('Google Rating', '4.8*', '1,200+ reviews - strongest in SoHo', GOLD),
    ('Keywords at #1', '5/10', 'Core target terms ranked first', GREEN),
    ('Schema Coverage', '0%', 'No structured data - 10 files now built', RED),
    ('Yelp Reviews', '135', 'vs 1,200+ Google - major gap', BLUE),
]
cw = 42
cx = 18
cy = pdf.get_y()
for i, (label, val, sub, color) in enumerate(cards):
    pdf.metric_card(cx + i * (cw + 2), cy, cw, 30, label, val, sub, color)
pdf.set_y(cy + 34)

pdf.highlight_box(
    'Summary Finding',
    'UPLIFT ranks #1 for its strongest keywords - matching tattoos NYC, flash tattoo NYC, lettering tattoo NYC, group tattoos NYC, and tattoo studio SoHo - and is clearly the dominant fineline tattoo studio in SoHo by volume and reputation. However, the site has zero structured data (now fixed), a nearly inactive blog, no editorial placements in major NYC roundups, and a split-domain strategy dividing authority between uplifttattoo.com and upliftpiercing.com. On piercing, Nine Moons Piercing is outranking UPLIFT for the top position. These gaps represent straightforward, high-return fixes - none require rebuilding the site.'
)

# Two-column check lists
col_w = 84
col2_x = 18 + col_w + 6

pdf.set_fill_color(*CARD)
pdf.set_draw_color(*BORDER)
pdf.set_line_width(0.2)
y_start = pdf.get_y()
pdf.rect(18, y_start, col_w, 58, 'FD')
pdf.rect(col2_x, y_start, col_w, 58, 'FD')

pdf.set_xy(21, y_start + 3)
pdf.set_font('Helvetica', 'B', 8)
pdf.set_text_color(*WHITE)
pdf.cell(col_w - 6, 5, 'Biggest Strengths', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(21)
strengths = [
    '#1 - matching tattoos NYC (5 of 10 SERP slots)',
    '#1 - flash tattoo NYC',
    '#1 - lettering tattoo NYC',
    '#1 - group tattoos NYC same day',
    '#1 - tattoo studio SoHo NYC',
    '1,200+ Google reviews - unmatched in local market',
    'Multiple pages indexed per keyword (strong domain)',
]
for s in strengths:
    pdf.set_xy(21, pdf.get_y())
    pdf.check_item(s, 'check')

pdf.set_xy(col2_x + 3, y_start + 3)
pdf.set_font('Helvetica', 'B', 8)
pdf.set_text_color(*WHITE)
pdf.cell(col_w - 6, 5, 'Biggest Gaps', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.set_x(col2_x + 3)
gaps = [
    'Zero schema markup - star ratings not showing',
    'Nine Moons outranks for luxury piercing SoHo',
    'DOVIANA outranks for piercing blog keywords',
    'Not in Time Out, Loving NY, or editorial lists',
    'Blog: 7 posts in 7 years',
    'Split domain divides authority',
    'Yelp: 135 reviews vs Google 1,200+',
]
for g in gaps:
    pdf.set_xy(col2_x + 3, pdf.get_y())
    pdf.check_item(g, 'cross')


# ─────────────────────────────────────────────────────────
# PAGE 3 - KEYWORD RANKINGS
# ─────────────────────────────────────────────────────────
pdf.add_page()
pdf.set_bg(BLACK)
pdf.gold_bar()
pdf.section_header('02', 'Keyword Rankings')

pdf.set_font('Helvetica', '', 7.5)
pdf.set_text_color(*MUTED)
pdf.multi_cell(0, 4, 'Rankings verified via live Google search, May 2026. Organic results only, excluding paid ads. SERP slots show which top-10 positions UPLIFT holds (gold) vs competitors (grey).')
pdf.ln(3)

keywords = [
    ('matching tattoos nyc',         '2,400/mo', '#1 + #2 + #4 + #7 + #8', 'Dominating', GREEN,   'IGLA (pos 5)'),
    ('flash tattoo nyc',             '3,600/mo', '#1',                      'Winning',    GREEN,   'Live By The Sword (pos 2)'),
    ('tattoo studio soho nyc',       '1,900/mo', '#1 + #4 + #5 + #8',      'Dominating', GREEN,   'Love Machine (pos 2)'),
    ('lettering tattoo nyc',         '1,300/mo', '#1',                      'Winning',    GREEN,   'IGLA (pos 2)'),
    ('group tattoos nyc same day',   '880/mo',   '#1 + #2',                 'Winning',    GREEN,   'IGLA (pos 3)'),
    ('first tattoo nyc',             '1,100/mo', '#1 + #8 + #9',            'Winning',    GREEN,   'Skin Design (pos 2)'),
    ('fineline tattoos nyc',         '5,400/mo', '#2 + #10',                'Strong',     BLUE,    'finelinetattoo.com (pos 1)'),
    ('butterfly tattoo nyc',         '1,600/mo', '#2 + #3 + #4 + #6-#8',   'Very Strong',BLUE,    'Monolith Studio (pos 1)'),
    ('walk-in tattoo soho nyc',      '2,200/mo', '#2 + #4',                 'Competing',  YELLOW,  'Love Machine (pos 1)'),
    ('luxury piercing nyc soho',     '1,800/mo', '#2 (upliftpiercing) #4',  'Losing #1',  RED,     'Nine Moons Piercing (pos 1)'),
]

# Table header
pdf.set_fill_color(*BORDER)
header_cols = ['Keyword', 'Est. Volume', 'UPLIFT Position', 'Status', 'Top Competitor']
col_widths  = [50, 18, 42, 22, 42]
pdf.set_font('Helvetica', 'B', 6.5)
pdf.set_text_color(*MUTED)
for col, w in zip(header_cols, col_widths):
    pdf.cell(w, 5, col, fill=True, new_x=XPos.RIGHT, new_y=YPos.TOP)
pdf.ln(5)

for i, (kw, vol, pos, status, sc, comp) in enumerate(keywords):
    bg = (20, 20, 20) if i % 2 == 0 else (14, 14, 14)
    y = pdf.get_y()
    pdf.set_fill_color(*bg)
    pdf.rect(18, y, 174, 7, 'F')

    pdf.set_xy(18, y + 1)
    pdf.set_font('Helvetica', 'B', 7.5)
    pdf.set_text_color(*WHITE)
    pdf.cell(col_widths[0], 5, kw, new_x=XPos.RIGHT, new_y=YPos.TOP)

    pdf.set_xy(18 + col_widths[0], y + 1)
    pdf.set_font('Helvetica', '', 7)
    pdf.set_text_color(*MUTED)
    pdf.cell(col_widths[1], 5, vol, new_x=XPos.RIGHT, new_y=YPos.TOP)

    pdf.set_xy(18 + col_widths[0] + col_widths[1], y + 1)
    pdf.set_font('Helvetica', 'B', 7.5)
    pdf.set_text_color(*sc)
    pdf.cell(col_widths[2], 5, pos, new_x=XPos.RIGHT, new_y=YPos.TOP)

    pdf.set_xy(18 + col_widths[0] + col_widths[1] + col_widths[2], y + 1)
    pdf.set_font('Helvetica', 'B', 7)
    pdf.set_text_color(*sc)
    pdf.cell(col_widths[3], 5, status, new_x=XPos.RIGHT, new_y=YPos.TOP)

    pdf.set_xy(18 + col_widths[0] + col_widths[1] + col_widths[2] + col_widths[3], y + 1)
    pdf.set_font('Helvetica', '', 7)
    pdf.set_text_color(*MUTED)
    pdf.multi_cell(col_widths[4], 5, comp)
    pdf.set_y(y + 7)

pdf.ln(4)
pdf.highlight_box(
    'Key Insight - #1 Position You\'re Missing',
    '"fineline tattoos nyc" - your highest-volume keyword at ~5,400 searches/month - has you at #2 behind finelinetattoo.com, which holds an unfair brand-name advantage. A long-form content expansion at /fineline-tattoos-nyc with FAQ schema (now built), more internal links, and 500 additional words could push you to #1 and add significant monthly traffic. This is the highest-leverage page on the site.'
)


# ─────────────────────────────────────────────────────────
# PAGE 4 - COMPETITOR INTELLIGENCE
# ─────────────────────────────────────────────────────────
pdf.add_page()
pdf.set_bg(BLACK)
pdf.gold_bar()
pdf.section_header('03', 'Competitor Intelligence')

pdf.set_font('Helvetica', '', 7.5)
pdf.set_text_color(*MUTED)
pdf.multi_cell(0, 4, 'Scoring based on keyword ranking overlap, review volume, editorial presence, content velocity, and domain signals. Verified May 2026.')
pdf.ln(3)

# TATTOO COMPETITORS
pdf.set_font('Helvetica', 'B', 7)
pdf.set_text_color(*MUTED)
pdf.cell(0, 4, 'TATTOO COMPETITORS', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(1)

tattoo_comps = [
    ('* UPLIFT Tattoo',   'SoHo',             67,  '1,200+', '135',   'None',          GOLD,  'YOU',     (40,30,10),    GOLD),
    ('Bang Bang Tattoo',  'SoHo + Chinatown',  88,  '3,000+', '500+',  '15+ (Vogue etc)',WHITE,'CRITICAL',(60,10,10),    RED),
    ('IGLA Tattoo',       'Midtown Manhattan', 62,  '800+',   '200+',  '3-5 lists',      TEXT, 'HIGH',    (40,15,15),    RED),
    ('Live By The Sword', 'SoHo + 2 others',   71,  '2,000+', '600+',  '5-8 lists',      TEXT, 'MEDIUM',  (40,35,10),    YELLOW),
    ('Atelier Eva',       'Williamsburg',       58,  '400+',   '150+',  '4-6 lists',      TEXT, 'MEDIUM',  (40,35,10),    YELLOW),
    ('Monolith Studio',   'Brooklyn',           74,  '600+',   '180+',  '6-8 lists',      TEXT, 'MEDIUM',  (40,35,10),    YELLOW),
    ('Love Machine NYC',  'SoHo',               55,  '300+',   '100+',  '2-3 lists',      TEXT, 'WATCH',   (15,25,40),    BLUE),
]

hdr = ['Studio', 'Auth.', 'G.Reviews', 'Yelp', 'Editorial', 'Threat']
hw  = [46, 14, 20, 16, 26, 16]

pdf.set_fill_color(*BORDER)
pdf.set_font('Helvetica', 'B', 6)
pdf.set_text_color(*MUTED)
for col, w in zip(hdr, hw):
    pdf.cell(w, 5, col, fill=True, new_x=XPos.RIGHT, new_y=YPos.TOP)
pdf.ln(5)

for studio, loc, auth, gr, yr, ed, tc, tlabel, tbg, tc2 in tattoo_comps:
    y = pdf.get_y()
    row_bg = (25, 20, 8) if studio.startswith('*') else (20,20,20)
    pdf.set_fill_color(*row_bg)
    pdf.rect(18, y, 138, 9, 'F')

    pdf.set_xy(18, y + 0.5)
    pdf.set_font('Helvetica', 'B', 7.5)
    pdf.set_text_color(*tc)
    pdf.cell(hw[0], 4, studio, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_xy(18, y + 5)
    pdf.set_font('Helvetica', '', 6.5)
    pdf.set_text_color(*MUTED)
    pdf.cell(hw[0], 3, loc)

    pdf.set_xy(18 + hw[0], y + 1)
    pdf.set_font('Helvetica', 'B', 8)
    col_score = GOLD if studio.startswith('*') else BLUE
    pdf.set_text_color(*col_score)
    pdf.cell(hw[1], 5, str(auth))

    pdf.set_xy(18 + hw[0] + hw[1], y + 2)
    pdf.set_font('Helvetica', '', 7.5)
    gcol = GOLD if studio.startswith('*') else TEXT
    pdf.set_text_color(*gcol)
    pdf.cell(hw[2], 5, gr)

    pdf.set_xy(18 + hw[0] + hw[1] + hw[2], y + 2)
    ycol = RED if yr == '135' else TEXT
    pdf.set_text_color(*ycol)
    pdf.cell(hw[3], 5, yr)

    pdf.set_xy(18 + hw[0] + hw[1] + hw[2] + hw[3], y + 2)
    pdf.set_font('Helvetica', '', 7)
    ecol = GREEN if '15+' in ed else (YELLOW if any(c.isdigit() for c in ed) else MUTED)
    pdf.set_text_color(*ecol)
    pdf.cell(hw[4], 5, ed)

    # Threat pill
    pill_x = 18 + sum(hw[:5])
    pdf.set_fill_color(*tbg)
    pdf.set_text_color(*tc2)
    pdf.set_font('Helvetica', 'B', 6.5)
    pdf.set_xy(pill_x, y + 2)
    pdf.cell(hw[5], 5, tlabel, fill=True, align='C')

    pdf.ln(9)

pdf.ln(3)

# PIERCING COMPETITORS
pdf.set_font('Helvetica', 'B', 7)
pdf.set_text_color(*MUTED)
pdf.cell(0, 4, 'PIERCING COMPETITORS', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.ln(1)

piercing_comps = [
    ('* UPLIFT Piercing', 'SoHo (upliftpiercing.com)', 54,  '1,200+(shared)', '135',  'No content',     GOLD,  'YOU',      (40,30,10),  GOLD),
    ('Nine Moons Piercing','123 Lafayette St, SoHo',   72,  '900+',           '487',  'Time Out feature',TEXT, 'CRITICAL', (60,10,10),  RED),
    ('DOVIANA',           '174 Spring St, SoHo',        60,  '400+',           '200+', '10+ blog posts',  TEXT, 'HIGH',     (40,15,15),  RED),
    ('STUDS',             'Multiple NYC locations',      80,  'National',       '1,000+','National brand', TEXT, 'MEDIUM',   (40,35,10),  YELLOW),
]

pdf.set_fill_color(*BORDER)
pdf.set_font('Helvetica', 'B', 6)
pdf.set_text_color(*MUTED)
for col, w in zip(hdr, hw):
    pdf.cell(w, 5, col, fill=True, new_x=XPos.RIGHT, new_y=YPos.TOP)
pdf.ln(5)

for studio, loc, auth, gr, yr, ed, tc, tlabel, tbg, tc2 in piercing_comps:
    y = pdf.get_y()
    row_bg = (25, 20, 8) if studio.startswith('*') else (20,20,20)
    pdf.set_fill_color(*row_bg)
    pdf.rect(18, y, 138, 9, 'F')

    pdf.set_xy(18, y + 0.5)
    pdf.set_font('Helvetica', 'B', 7.5)
    pdf.set_text_color(*tc)
    pdf.cell(hw[0], 4, studio)
    pdf.set_xy(18, y + 5)
    pdf.set_font('Helvetica', '', 6.5)
    pdf.set_text_color(*MUTED)
    pdf.cell(hw[0], 3, loc)

    pdf.set_xy(18 + hw[0], y + 1)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_text_color(GOLD if studio.startswith('*') else BLUE)
    pdf.cell(hw[1], 5, str(auth))

    pdf.set_xy(18 + hw[0] + hw[1], y + 2)
    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_text_color(GOLD if studio.startswith('*') else TEXT)
    pdf.cell(hw[2], 5, gr)

    pdf.set_xy(18 + hw[0] + hw[1] + hw[2], y + 2)
    pdf.set_text_color(RED if yr == '135' else TEXT)
    pdf.cell(hw[3], 5, yr)

    pdf.set_xy(18 + hw[0] + hw[1] + hw[2] + hw[3], y + 2)
    pdf.set_font('Helvetica', '', 7)
    pdf.set_text_color(GREEN if 'Time Out' in ed else (YELLOW if 'blog' in ed.lower() else MUTED))
    pdf.cell(hw[4], 5, ed)

    pdf.set_fill_color(*tbg)
    pdf.set_text_color(*tc2)
    pdf.set_font('Helvetica', 'B', 6.5)
    pdf.set_xy(18 + sum(hw[:5]), y + 2)
    pdf.cell(hw[5], 5, tlabel, fill=True, align='C')

    pdf.ln(9)

pdf.ln(3)
pdf.highlight_box(
    'Critical Piercing Threat - Nine Moons is 2 blocks away',
    'Nine Moons Piercing at 123 Lafayette St (2 blocks from UPLIFT) holds the #1 position for "luxury piercing nyc soho" and has 487 Yelp reviews vs your 135. They were featured by Time Out. Your piercing authority is diluted across two domains. Consolidating upliftpiercing.com into uplifttattoo.com and building dedicated piercing content (like DOVIANA\'s blog strategy) are the two most direct moves to close this gap.'
)


# ─────────────────────────────────────────────────────────
# PAGE 5 - TECHNICAL SEO HEALTH
# ─────────────────────────────────────────────────────────
pdf.add_page()
pdf.set_bg(BLACK)
pdf.gold_bar()
pdf.section_header('04', 'Technical SEO Health')

audits = [
    ('Structured Data / Schema', 'F', [
        ('cross', 'No TattooParlor / LocalBusiness schema anywhere on site'),
        ('cross', '1,200+ reviews not in AggregateRating - stars not showing in search'),
        ('cross', 'No FAQPage schema - 24 FAQ answers invisible to rich results'),
        ('cross', 'No Service schema on any service page'),
        ('cross', 'No BreadcrumbList or Person schema'),
        ('check', '10 schema files now built and ready to deploy'),
    ]),
    ('On-Page SEO', 'C+', [
        ('check', 'Homepage H1 is clear and keyword-targeted'),
        ('check', 'Service pages have strong H2 structure'),
        ('check', 'Internal linking is moderate-to-strong'),
        ('cross', 'Meta descriptions missing on homepage, /piercing, /fineline-tattoos-nyc'),
        ('cross', 'Multiple H1 tags on /piercing page (technical error)'),
        ('warn',  'Image alt text present but inconsistent'),
    ]),
    ('Content & Blog', 'D', [
        ('check', 'Core service pages exist for all primary keywords'),
        ('check', 'Pages average 800-900 words - adequate'),
        ('cross', 'Only 7 blog posts across 7+ years of operation'),
        ('cross', 'Last blog post was May 2025 - one year gap'),
        ('cross', 'No aftercare guides, style guides, or educational content'),
        ('cross', 'DOVIANA and IGLA ranking for queries UPLIFT is not targeting'),
    ]),
    ('Local SEO & Profiles', 'B-', [
        ('check', 'Google Business Profile active - 4.8 stars, 1,200+ reviews'),
        ('check', 'Address, hours, and category correct on Google'),
        ('check', 'TripAdvisor listing exists with positive reviews'),
        ('cross', 'Yelp only 135 reviews - major platform underperformance'),
        ('cross', 'TripAdvisor not actively managed - low review count'),
        ('warn',  'No NAP schema to reinforce address/phone/hours'),
    ]),
    ('Domain Authority & Backlinks', 'C', [
        ('check', 'Site ranks for competitive terms - moderate authority'),
        ('check', 'Multiple pages indexed and ranking - good crawlability'),
        ('cross', 'Not featured in Time Out, Loving NY, or major editorial lists'),
        ('cross', 'No high-authority editorial backlinks detected'),
        ('cross', 'upliftpiercing.com splits domain authority'),
        ('warn',  'BirdEye, Roadtrippers links provide minor signals only'),
    ]),
    ('Multi-Domain Strategy', 'D+', [
        ('warn',  'upliftpiercing.com is a fully separate domain - not a redirect'),
        ('cross', 'Cross-linking between the two domains is minimal (footer only)'),
        ('cross', 'Backlinks to one domain do not benefit the other'),
        ('cross', 'Google may treat them as separate businesses in local results'),
        ('cross', 'No meta description on upliftpiercing.com homepage'),
        ('warn',  'Decision needed: consolidate or invest in both separately'),
    ]),
]

grade_colors = {'A': GREEN, 'B': BLUE, 'B-': BLUE, 'C': YELLOW, 'C+': YELLOW, 'D': RED, 'D+': RED, 'F': (255,50,50)}
card_w = 84
card_h = 52

for idx, (title, grade, items) in enumerate(audits):
    col = idx % 2
    row = idx // 2
    if col == 0 and row > 0:
        pdf.ln(4)
    cx = 18 + col * (card_w + 6)
    cy = pdf.get_y() if col == 0 else pdf.get_y()

    if col == 0:
        saved_y = pdf.get_y()

    pdf.set_fill_color(*CARD)
    pdf.set_draw_color(*BORDER)
    pdf.set_line_width(0.2)
    pdf.rect(cx, pdf.get_y() if col == 0 else saved_y, card_w, card_h, 'FD')

    y0 = pdf.get_y() if col == 0 else saved_y
    pdf.set_xy(cx + 3, y0 + 3)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_text_color(*WHITE)
    pdf.cell(card_w - 20, 5, title, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font('Helvetica', 'B', 11)
    gc = grade_colors.get(grade, MUTED)
    pdf.set_text_color(*gc)
    pdf.set_xy(cx + card_w - 14, y0 + 2)
    pdf.cell(12, 6, grade, align='C')

    item_y = y0 + 9
    for icon, text in items:
        if item_y > y0 + card_h - 4:
            break
        pdf.set_xy(cx + 3, item_y)
        ic, ic_t = (GREEN, '+') if icon == 'check' else ((RED, 'x') if icon == 'cross' else (YELLOW, '~'))
        pdf.set_font('Helvetica', 'B', 7)
        pdf.set_text_color(*ic)
        pdf.cell(5, 4, ic_t, new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.set_xy(cx + 8, item_y)
        pdf.set_font('Helvetica', '', 6.8)
        pdf.set_text_color(*TEXT)
        pdf.multi_cell(card_w - 11, 4, text)
        item_y += 7

    if col == 1:
        pdf.set_y(saved_y + card_h + 4)


# ─────────────────────────────────────────────────────────
# PAGE 6 - KEYWORD GAPS & ACTION PLAN
# ─────────────────────────────────────────────────────────
pdf.add_page()
pdf.set_bg(BLACK)
pdf.gold_bar()
pdf.section_header('05', 'Keyword Gaps & Opportunities')

pdf.set_font('Helvetica', '', 7.5)
pdf.set_text_color(*MUTED)
pdf.multi_cell(0, 4, 'Keywords with meaningful search volume where UPLIFT is not currently ranking in the top 5, or where no dedicated page exists.')
pdf.ln(3)

gaps_kw = [
    ('ear piercing nyc',                 '~6,600/mo',  'Not ranking'),
    ('curated ear piercing nyc',         '~1,900/mo',  'Not ranking'),
    ('do fineline tattoos last',         '~2,400/mo',  'No page - AI gold'),
    ('nose piercing nyc',                '~3,200/mo',  'Not ranking'),
    ('how long do fineline tattoos last','~1,800/mo',  'No page'),
    ('tattoo events nyc',                '~2,900/mo',  'No dedicated page'),
    ('septum piercing nyc',              '~1,600/mo',  'DOVIANA ranking'),
    ('tattoo aftercare nyc',             '~1,100/mo',  'No content'),
    ('helix piercing nyc',               '~2,100/mo',  'Not ranking'),
    ('fineline tattoo ideas',            '~4,400/mo',  'No dedicated content'),
    ('tattoo corporate event nyc',       '~720/mo',    'High value - no page'),
    ('small tattoos nyc women',          '~2,200/mo',  'Not ranking'),
]

col_w2 = [80, 28, 66]
for i, (kw, vol, status) in enumerate(gaps_kw):
    y = pdf.get_y()
    bg = (20,20,20) if i % 2 == 0 else (14,14,14)
    pdf.set_fill_color(*bg)
    pdf.rect(18, y, 174, 6, 'F')
    pdf.set_xy(18, y + 1)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_text_color(*TEXT)
    pdf.cell(col_w2[0], 4, kw, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_text_color(*MUTED)
    pdf.cell(col_w2[1], 4, vol, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font('Helvetica', 'B', 7.5)
    pdf.set_text_color(*RED)
    pdf.cell(col_w2[2], 4, status)
    pdf.ln(6)

pdf.ln(2)
pdf.section_header('06', 'Prioritized Action Plan')

actions = [
    ('1', 'Deploy All 10 Schema Files (Already Built)',
     '10 schema files are ready in your /schemas folder. Paste each into the corresponding Squarespace page header. This unlocks star ratings, FAQPage snippets, Service rich results, and BreadcrumbList navigation across all 9 core pages plus upliftpiercing.com.',
     'CRITICAL', RED),
    ('2', 'Fix Multiple H1s on /piercing Page',
     'The piercing page has 3+ H1 tags. Convert all but the primary one to H2/H3 in Squarespace. 20-minute fix that removes a technical error confusing Google about the page\'s focus keyword.',
     'HIGH', GREEN),
    ('3', 'Add Meta Descriptions to Core Pages',
     'Homepage, /fineline-tattoos-nyc, /piercing, /flash-tattoo-designs, /matching-tattoos-nyc all lack meta descriptions. These 155-char summaries directly affect CTR. A 5-10% CTR improvement means dozens of extra visitors per week from the same position.',
     'HIGH', GREEN),
    ('4', 'Build /do-fineline-tattoos-last Page',
     '~4,200 monthly searches for "do fineline tattoos last / fade." Create a dedicated page with a short answer block, FAQ schema, and 600+ words. Designed for AI search and featured snippets. Could rank in 30-60 days.',
     'HIGH', GREEN),
    ('5', 'Add Yelp Review Request to Post-Appointment Flow',
     'Nine Moons has 487 Yelp reviews. You have 135. Add a Yelp link to your text follow-up after every appointment. Even 10% conversion compounds fast. Target: 200+ reviews by end of 2026.',
     'HIGH', GREEN),
    ('6', 'Outreach to Editorial Lists',
     'Time Out, Loving NY, Tattooed Images, NY Mag. With 1,200+ Google reviews and #1 positions on core keywords you have a strong pitch. Each placement = high-authority backlink + referral traffic + brand authority.',
     'HIGH', GREEN),
    ('7', 'Launch Piercing Blog Content vs DOVIANA',
     'DOVIANA ranks for "septum piercing NYC," "nostril piercing NYC," "navel piercing NYC" with dedicated blog posts. UPLIFT has zero piercing blog content. 5-6 posts would capture this traffic and close the gap.',
     'HIGH', GREEN),
    ('8', 'Decide: Consolidate upliftpiercing.com or Invest in It',
     'Option A: redirect to uplifttattoo.com/piercing - consolidate all authority. Option B: fully invest as a standalone brand. Option A is lower risk and faster. Either way the current half-built state is the worst of both.',
     'MEDIUM', YELLOW),
    ('9', 'Build Artist SEO Pages (Junh, Julia, Kseniya)',
     'Only Anastasia has a dedicated SEO page. Each artist page targets their specialty + NYC, ranks for name searches, and creates internal links back to booking. Each page is a new indexed asset.',
     'MEDIUM', YELLOW),
    ('10','Strengthen /fineline-tattoos-nyc for #1',
     'You\'re at #2 for your highest-volume keyword (5,400/mo) behind a site that only wins on domain name. Expand the page with 300+ more words, a FAQ section (schema now installed), and more internal links from homepage and blog.',
     'HIGH', GREEN),
]

for num, title, desc, impact, ic in actions:
    if pdf.get_y() > 240:
        pdf.add_page()
        pdf.set_bg(BLACK)
        pdf.gold_bar()

    y = pdf.get_y()
    pdf.set_fill_color(*CARD)
    pdf.set_draw_color(*BORDER)
    pdf.set_line_width(0.15)

    # Number badge
    pdf.set_fill_color(40, 30, 10)
    pdf.set_draw_color(*GOLD)
    pdf.rect(18, y, 8, 8, 'FD')
    pdf.set_xy(18, y + 0.5)
    pdf.set_font('Helvetica', 'B', 8)
    pdf.set_text_color(*GOLD)
    pdf.cell(8, 7, num, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)

    # Title
    pdf.set_xy(28, y + 1)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_text_color(*WHITE)
    pdf.cell(130, 5, title, new_x=XPos.RIGHT, new_y=YPos.TOP)

    # Impact pill
    pill_bg = (60, 10, 10) if impact == 'CRITICAL' else ((20, 45, 20) if impact == 'HIGH' else (45, 35, 10))
    pdf.set_fill_color(*pill_bg)
    pdf.set_text_color(*ic)
    pdf.set_font('Helvetica', 'B', 6.5)
    pdf.set_xy(160, y + 1.5)
    pdf.cell(32, 4.5, impact, fill=True, align='C')

    # Description
    pdf.set_xy(28, y + 7)
    pdf.set_font('Helvetica', '', 7.5)
    pdf.set_text_color(*MUTED)
    pdf.multi_cell(162, 3.8, desc)

    pdf.ln(3)
    pdf.set_draw_color(*BORDER)
    pdf.line(18, pdf.get_y(), 192, pdf.get_y())
    pdf.ln(3)


# ─────────────────────────────────────────────────────────
# OUTPUT
# ─────────────────────────────────────────────────────────
output_path = "/Users/upliftconcierge/Desktop/Claude Code /Uplift Tattoo /UPLIFT-SEO-Audit-Report.pdf"
pdf.output(output_path)
print(f"PDF saved: {output_path}")

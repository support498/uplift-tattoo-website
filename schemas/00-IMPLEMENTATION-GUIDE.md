# UPLIFT Tattoo & Piercing — Schema Implementation Guide

All schema files are ready to paste into Squarespace. Follow the steps below for each page.

---

## How to Add Schema in Squarespace

### Page-Level (Recommended - Most Pages)
1. Go to **Pages** in Squarespace
2. Hover over the page and click the **gear icon** (Page Settings)
3. Click **Advanced**
4. Paste the schema HTML into **Page Header Code Injection**
5. Save

### Site-Wide (For Homepage Schema Only - Optional)
1. Go to **Settings > Advanced > Code Injection**
2. Paste into the **Header** field
3. Save
- Note: Only use site-wide for the homepage schema. All other schemas are page-specific.

---

## Schema Files - Where Each One Goes

| File | Page | URL |
|------|------|-----|
| `01-homepage-schema.html` | Homepage | uplifttattoo.com/ |
| `02-fineline-tattoos-nyc-schema.html` | Fineline Tattoos NYC | uplifttattoo.com/fineline-tattoos-nyc |
| `03-piercing-schema.html` | Piercing | uplifttattoo.com/piercing |
| `04-flash-tattoo-designs-schema.html` | Flash Tattoo Designs | uplifttattoo.com/flash-tattoo-designs |
| `05-matching-tattoos-nyc-schema.html` | Matching Tattoos NYC | uplifttattoo.com/matching-tattoos-nyc |
| `06-lettering-tattoos-nyc-schema.html` | Lettering Tattoos NYC | uplifttattoo.com/lettering-tattoos-nyc |
| `07-butterfly-tattoo-schema.html` | Butterfly Flash Tattoo | uplifttattoo.com/butterfly-flash-tattoo |
| `08-faq-page-schema.html` | FAQ Page | uplifttattoo.com/faq |
| `09-our-team-schema.html` | Our Team | uplifttattoo.com/our-team |
| `10-upliftpiercing-com-schema.html` | upliftpiercing.com Homepage | upliftpiercing.com/ |

---

## What Each Schema Does

### 01 - Homepage
- **TattooParlor** - tells Google exactly what the business is, where it is, when it's open, and how to contact it
- **AggregateRating** - enables star ratings (4.8/1200+ reviews) to appear in Google search results
- **FAQPage** - top 6 questions for AI search and featured snippets
- **WebSite** - sitelinks search box signal
- **OfferCatalog** - flash tattoos ($199+), custom tattoos ($299+), luxury piercing

### 02 - Fineline Tattoos NYC
- **Service** - defines fineline tattooing as a named service with pricing and provider
- **FAQPage** - 7 fineline-specific questions targeting "do fineline tattoos fade," "how long to heal," etc.
- **BreadcrumbList** - page hierarchy signal

### 03 - Piercing
- **Service** - defines all piercing service types with jewelry pricing
- **FAQPage** - 7 piercing questions including jewelry policy, safety, and pricing
- **BreadcrumbList**

### 04 - Flash Tattoo Designs
- **Service** - flash tattoo as a defined service with collection breakdown
- **FAQPage** - 6 flash tattoo questions targeting walk-in and same-day searches
- **BreadcrumbList**

### 05 - Matching Tattoos NYC
- **Service** - matching tattoos for couples, friends, groups with group deposit info
- **FAQPage** - 7 matching tattoo questions including group process and pricing
- **BreadcrumbList**

### 06 - Lettering Tattoos NYC
- **Service** - lettering, script, numbers, custom typography
- **FAQPage** - 4 lettering-specific questions
- **BreadcrumbList**

### 07 - Butterfly Tattoo
- **Service** - butterfly flash and custom designs with pricing
- **FAQPage** - 4 butterfly tattoo questions including placement
- **BreadcrumbList**

### 08 - FAQ Page
- **FAQPage** - full 24-question schema covering every FAQ on the site
- This is the most powerful schema for featured snippets and AI search answers
- **BreadcrumbList**

### 09 - Our Team
- **ItemList** of all 16 artists and specialists as **Person** schema with specialties
- Helps Google understand who works at the studio and for artist-name searches
- **BreadcrumbList**

### 10 - upliftpiercing.com
- **HealthAndBeautyBusiness** - full business schema for the separate domain
- **FAQPage** - 5 key piercing questions
- Note: Consider redirecting upliftpiercing.com to uplifttattoo.com/piercing long-term

---

## After You Install

1. **Test each page** at [Google Rich Results Test](https://search.google.com/test/rich-results)
   - Paste the page URL and click Test URL
   - Should show: LocalBusiness, FAQPage, Service, BreadcrumbList results
2. **Submit updated sitemaps** in Google Search Console after all schemas are live
3. **Monitor Rich Results** in Google Search Console under Enhancements
4. Star ratings in search results typically appear within 2-6 weeks after implementation

---

## Important Notes

- Update **image URLs** in homepage and piercing schemas to real image paths once confirmed
- Update **reviewCount** in AggregateRating as your Google review count grows
- Do NOT add the same FAQPage schema to multiple pages for the same questions - keep them unique per page
- Squarespace may strip some special characters - if schema breaks, use the Rich Results Test to debug

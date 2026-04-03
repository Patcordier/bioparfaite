# BioParfaite.com — Roadmap & Suivi

## FAIT
- [x] Landing page (index.html) — design dark/neon, responsive, mobile-first
- [x] Formulaire diagnostic (formulaire.html) — 5 questions, navigation étape par étape
- [x] Branding "BioParfaite.com" appliqué partout
- [x] Toutes mentions "IA" supprimées, remplacées par "nos experts" / "notre méthode"
- [x] 6 apps de rencontre intégrées : Tinder, Bumble, Hinge, Happn, Fruitz, Badoo
- [x] Géolocalisation IP : prix en $ CAD (Canada) ou € (Europe/Afrique) automatique
- [x] Pricing psychologique : 9,97$ CAD / 9,97€
- [x] Image Stripe générée (assets/bioparfaite-stripe-product.png)
- [x] Favicon + icône 512px (favicon.png, icon-512.png) ajoutés sur toutes les pages
- [x] Compression images : 6 Mo → 320 Ko (PNG → JPG optimisé 85%)
- [x] Image OG "0 match ?" percutante + balises OG mises à jour (généraliste, pas d'appli spécifique)
- [x] Produits Stripe créés (BioParfaite CAD + BioParfaite EUR)
- [x] SEO : title + meta description optimisés à chaque modification
- [x] Ordre du formulaire optimisé pour la conversion (facile → difficile → email)
- [x] Brancher les 2 liens Stripe dans le site
- [x] Acheter le domaine bioparfaite.com (OVH)
- [x] DNS configuré : 4x A records GitHub + CNAME www → patcordier.github.io
- [x] Héberger le site sur GitHub Pages
- [x] Brancher le formulaire au webhook N8N
- [x] S'inscrire sur Anthropic + récupérer clé API
- [x] Configurer le noeud N8N "Message a model" : Anthropic, claude-opus-4-6, prompt HTML
- [x] Prompt Claude rédigé et sauvegardé (voir PROMPT_CLAUDE.md v3)
- [x] Configurer le noeud N8N "Send email" : template HTML aux couleurs du site
- [x] Tester le parcours complet : formulaire → N8N → Claude → email client (~0,04$ par génération)
- [x] Token secret webhook N8N (Header Auth X-BP-Token)
- [x] Rate limiting sur le formulaire (1 soumission/minute)
- [x] Honeypot anti-bot sur le formulaire
- [x] Ignore Bots activé dans N8N
- [x] Page mentions légales + CGV + politique confidentialité + cookies (mentions-legales.html)
- [x] Liens footer sur index.html et formulaire.html
- [x] DNSSEC activé sur OVH
- [x] HTTPS activé sur GitHub Pages (Enforce HTTPS coché)
- [x] Email pro : "BioParfaite <contact.bioparfaite@gmail.com>" configuré dans N8N (SMTP Gmail, port 587, STARTTLS)
- [x] Limite de dépenses mensuelle sur Anthropic (20$)
- [x] Chatbot FAQ interactive (10 questions, widget flottant)
- [x] Immatriculation NEQ : Patrix Digital (2281999708)
- [x] Mentions légales mises à jour avec NEQ
- [x] Google Search Console : propriété vérifiée + sitemap soumis (4 pages indexées)
- [x] SEO avancé : sitemap.xml, robots.txt, Schema.org JSON-LD, Open Graph, canonical, hreflang
- [x] Article blog #1 : "Bio Tinder Homme : 30 Exemples" (avec images, blur paywall, CTA)
- [x] Section Blog ajoutée sur page d'accueil (3 cartes dont 2 "Bientôt")
- [x] Fichier comptabilité Excel (Comptabilite_Patrix_Digital.xlsx)

## A FAIRE — Priorité moyenne
- [x] Branding Stripe : logo BioParfaite + couleur #0a0a0f / #ff2d78 configurés
- [ ] Articles blog #2 à #4 (voir calendrier de publication ci-dessous)
- [ ] Version anglophone du site (dupliquer et traduire)
- [ ] Nom de domaine anglophone (à choisir)
- [x] Page de remerciement post-paiement Stripe (redirect après paiement) — `merci.html` créé
- [x] Google Analytics GA4 (G-07K92SE02C) installé sur toutes les pages

## CONCURRENTS ANALYSÉS
- [x] **Roast.dating** — Leader, traduit de l'anglais, CTA agressif, 84k+ clients
- [x] **Texting Academy** — Bon contenu long-form, ton "coach séduction"
- [x] **stat-rencontres.fr** — Générateur bio gratuit basique, site brouillon
- [x] **DatingZest** — Vend des numéros de téléphone pour vérification d'apps. Analysé : pas pertinent pour nous, mais mots-clés SEO exploitables (articles blog)

## PHASE 2 — Offre Premium "Analyse de Profil"
- [ ] Concept : le client upload un screenshot du profil qui l'intéresse → IA analyse photo+bio → phrases d'accroche ultra-personnalisées
- [ ] Pack 3 profils : 14,97$ CAD / 14,97€
- [ ] Pack 10 profils : 29,97$ CAD / 29,97€
- [ ] Nouveau formulaire avec upload d'image
- [ ] Nouveau workflow N8N avec Claude Vision
- [ ] Nouveaux produits Stripe
- [ ] Coût API estimé : ~0,08-0,10$ par analyse (vision)

## A FAIRE — Priorité basse / idées futures
- [ ] Créer des codes promo Stripe pour campagnes marketing
- [ ] Témoignages réels (remplacer les fictifs quand tu auras de vrais clients)
- [ ] Tester d'autres prix (A/B testing)
- [ ] Version premium (plus de bios, coaching profil complet)

---

## DECISIONS PRISES
| Sujet | Décision | Raison |
|-------|----------|--------|
| Nom de domaine FR | bioparfaite.com | SEO optimal, francophonie entière |
| Extension | .com uniquement | Universel, pas besoin de .fr et .ca |
| Prix | 9,97$ / 9,97€ | Pricing psychologique (fin en 7) |
| Mentions IA | Supprimées | Eviter que les clients aillent sur ChatGPT |
| Hébergement | GitHub Pages (gratuit) | patcordier.github.io/bioparfaite → bioparfaite.com |
| Registrar domaine | OVH (.com) | WHOIS anonymisé par RGPD |
| Entreprise | Patrix Digital (NEQ 2281999708) | Entreprise individuelle, Québec |
| Back-office | Pas nécessaire | Stripe + N8N suffisent, modifications dans le HTML |
| Ordre formulaire | Facile → clics → texte → email | Maximise le taux de complétion |
| Taxes Stripe | Pas activées pour l'instant | A activer quand inscrit aux taxes |

---

## RECHERCHE DE MOTS-CLÉS — Analyse SEO avril 2026

### Mots-clés principaux (FR) — Volume élevé
| Mot-clé | Volume estimé | Concurrence | Intention |
|---------|--------------|-------------|-----------|
| bio tinder | Très élevé | Forte | Informationnelle → conversion |
| phrase d'accroche tinder | Très élevé | Forte | Informationnelle → conversion |
| site de rencontre | Extrêmement élevé | Très forte | Navigation / comparaison |
| profil tinder | Élevé | Moyenne | Informationnelle |
| comment draguer sur tinder | Élevé | Moyenne | Informationnelle |
| phrase d'accroche bumble | Moyen | Faible-moyenne | Informationnelle → conversion |
| bio bumble | Moyen | Faible-moyenne | Informationnelle → conversion |
| phrase d'accroche hinge | Moyen (croissant) | Faible | Informationnelle → conversion |
| plan cul / rencontre sexe | Très élevé | Forte | Transactionnelle (pas notre cible directe) |
| trouver l'amour en ligne | Moyen | Moyenne | Informationnelle |
| rencontre en ligne | Très élevé | Très forte | Navigation |

### Mots-clés longue traîne (FR) — Faible concurrence, haute conversion
| Mot-clé longue traîne | Potentiel | Priorité |
|------------------------|-----------|----------|
| bio tinder homme 2026 | Fort | ★★★★★ |
| bio tinder femme 2026 | Fort | ★★★★★ |
| exemple bio tinder drôle | Fort | ★★★★★ |
| meilleure bio tinder 2026 | Fort | ★★★★★ |
| que mettre dans sa bio tinder | Fort | ★★★★ |
| comment avoir plus de matchs tinder | Fort | ★★★★ |
| phrase d'accroche tinder qui marche | Fort | ★★★★ |
| profil tinder qui attire | Moyen | ★★★★ |
| phrase d'accroche drôle site de rencontre | Moyen | ★★★★ |
| comment se démarquer sur bumble | Moyen | ★★★ |
| bio hinge en français | Faible-moyen | ★★★ |
| comment briser la glace sur happn | Faible | ★★★ |
| generateur bio tinder | Moyen | ★★★★★ (direct competitor) |
| créer un profil de rencontre attractif | Moyen | ★★★★ |
| comment draguer une fille sur internet | Élevé | ★★★ |
| premier message site de rencontre | Élevé | ★★★★ |
| phrases pour draguer sur tinder | Moyen | ★★★★ |
| bio badoo originale | Faible-moyen | ★★★ |
| bio fruitz exemple | Faible | ★★ |
| pick up line en français | Moyen | ★★★★ |
| rencontre sérieuse en ligne | Moyen | ★★★ |
| comment aborder quelqu'un en ligne | Moyen | ★★★★ |

### Mots-clés anglais (pour futur site EN)
| Keyword | Volume (global) | Competition |
|---------|----------------|-------------|
| tinder bio | 60 500+/mois | Forte |
| pick up lines | Très élevé | Forte |
| best tinder bio | Élevé | Moyenne |
| bumble bio ideas | Moyen | Moyenne |
| hinge prompts answers | Moyen-élevé | Moyenne |
| dating profile tips | Moyen | Moyenne |
| tinder opening lines | Élevé | Forte |
| funny dating bio | Moyen | Faible-moyenne |

### Concurrents directs qui se positionnent sur ces mots-clés
| Site | Mots-clés couverts | Force |
|------|-------------------|-------|
| texting-academy.com | bio tinder, phrase d'accroche tinder | Contenu long-form, bien structuré |
| roast.dating/fr | phrases accroche tinder, bio tinder | Leader, 84k+ clients, version FR |
| seductionbykamal.com | tinder phrases accroche | Blog SEO agressif |
| stat-rencontres.fr | generateur bio tinder | Outil gratuit concurrent direct |
| mariages.net | bio tinder | Autorité de domaine très élevée |
| dragueurdeparis.com | phrase accroche tinder | Contenu orienté hommes |

---

## BLOG — Plan de contenu SEO (mis à jour avec recherche mots-clés)
Objectif : attirer du trafic Google gratuit avec des articles optimisés sur les mots-clés à forte conversion.

### PRIORITÉ 1 — Articles à fort volume + forte intention d'achat
1. "Bio Tinder : 30 exemples pour homme qui font matcher en 2026"
   → Mots-clés : bio tinder, bio tinder homme 2026, meilleure bio tinder
2. "Bio Tinder pour femme : 25 exemples irrésistibles (2026)"
   → Mots-clés : bio tinder femme, exemple bio tinder femme
3. "50 phrases d'accroche Tinder qui marchent vraiment (testées en 2026)"
   → Mots-clés : phrase d'accroche tinder, phrases pour draguer sur tinder
4. "Générateur de bio pour Tinder, Bumble et Hinge — Comment ça marche"
   → Mots-clés : generateur bio tinder, créer un profil de rencontre

### PRIORITÉ 2 — Articles par application (couvrir chaque niche)
5. "Phrases d'accroche Bumble : 30 exemples pour qu'elle te réponde"
   → Mots-clés : phrase d'accroche bumble, bio bumble
6. "Bio Hinge en français : comment remplir tes prompts pour matcher"
   → Mots-clés : bio hinge, hinge prompts français
7. "Bio Badoo : comment se démarquer des milliers de profils"
   → Mots-clés : bio badoo, bio badoo originale
8. "Happn : 10 astuces pour un profil qui attire les gens autour de toi"
   → Mots-clés : profil happn, happn astuces

### PRIORITÉ 3 — Articles à intention informationnelle large (trafic volume)
9. "Pourquoi tu n'as pas de matchs sur Tinder (et comment corriger ça)"
   → Mots-clés : pas de match tinder, comment avoir plus de matchs
10. "Comment aborder quelqu'un sur une app de rencontre sans être bizarre"
    → Mots-clés : comment aborder, premier message site de rencontre
11. "Comment draguer sur Internet : le guide complet 2026"
    → Mots-clés : comment draguer sur internet, draguer en ligne
12. "Bio Tinder drôle : 25 exemples qui font rire (et matcher)"
    → Mots-clés : bio tinder drôle, exemple bio tinder drôle
13. "Pick-up lines en français : 40 phrases d'accroche originales"
    → Mots-clés : pick up line français, phrases drague originales
14. "Rencontre sérieuse en ligne : comment créer un profil qui attire les bonnes personnes"
    → Mots-clés : rencontre sérieuse en ligne, profil rencontre sérieuse
15. "Premier message sur un site de rencontre : 20 exemples qui donnent envie de répondre"
    → Mots-clés : premier message site de rencontre, comment envoyer un premier message

### Calendrier de publication (1 article / semaine)
| Semaine | Date cible | Article | Statut |
|---------|-----------|---------|--------|
| S1 | 2 avril 2026 | Bio Tinder Homme : 30 exemples | ✅ Publié |
| S2 | 9 avril 2026 | Bio Tinder Femme : 25 exemples irrésistibles | Prêt à publier |
| S3 | 16 avril 2026 | 50 phrases d'accroche Tinder qui marchent | À écrire |
| S4 | 23 avril 2026 | Générateur de bio : comment ça marche | À écrire |
| S5 | 30 avril 2026 | Phrases d'accroche Bumble : 30 exemples | À écrire |
| S6 | 7 mai 2026 | Bio Hinge en français | À écrire |
| S7 | 14 mai 2026 | Pourquoi tu n'as pas de matchs sur Tinder | À écrire |
| S8 | 21 mai 2026 | Comment aborder quelqu'un en ligne | À écrire |

Rythme recommandé : **1 article par semaine** = Google voit que le site est actif, sans surcharger.

### Format recommandé :
- 1000 à 2000 mots par article (Google favorise le contenu long et complet en 2026)
- Exemples concrets de bios et phrases (contenu original, pas du copié-collé)
- Structure H2/H3 claire pour les featured snippets et AI Overviews
- CTA vers BioParfaite intégré naturellement (milieu + fin de chaque article)
- 3 exemples gratuits par style + blur sur le reste (conversion)
- Données chiffrées quand possible (taux de réponse, statistiques)
- PAS de commentaires publics (risque d'avis négatifs)

---

## TÂCHES EN ATTENTE

### Priorité haute
- [ ] Configurer DNS FixMyBio.com (A + AAAA + CNAME www)
- [ ] Créer le site anglais FixMyBio.com (dupliquer et adapter BioParfaite)
- [ ] Nouveaux liens Stripe USD / GBP / AUD
- [ ] Adapter le prompt Claude pour générer en anglais
- [ ] Articles blog anglais (SEO)

### Priorité moyenne
- [x] Rédiger les posts promo prêts à copier-coller → dossier `promo/`
  - [x] 3 posts Reddit FR (r/france, r/AskFrance, r/Quebec) → `promo/posts-reddit-fr.md`
  - [x] 3 posts Reddit EN (r/Tinder, r/dating_advice, r/Bumble) → `promo/posts-reddit-en.md`
  - [x] 1 article Medium FR (~1200 mots, valeur + CTA discret) → `promo/article-medium-fr.md`
  - [x] 1 article Medium EN (~1200 mots, valeur + CTA discret) → `promo/article-medium-en.md`
  - [x] Calendrier de publication (3 semaines, horaires optimaux) → `promo/calendrier-publication.md`
- [ ] S'affilier à TinderProfile.ai (30% commission, via tinderprofile.ai/affiliate/)
- [ ] Intégrer les liens d'affiliation dans les articles FR et EN
- [ ] Créer notre propre programme d'affiliation
- [x] Branding Stripe : logo + couleurs configurés
- [x] Page de remerciement post-paiement Stripe — `merci.html` créé
- [x] Google Analytics GA4 (BioParfaite = G-07K92SE02C)
- [ ] Version espagnole (futur)

### Priorité basse
- [ ] Phase 2 — Offre Premium "Analyse de Profil" (screenshot → phrases personnalisées)
- [ ] Système de build Tailwind (remplacer CDN par CSS compilé)
- [ ] Témoignages réels (remplacer les fictifs quand vrais clients)
- [ ] A/B testing prix
- [ ] Codes promo Stripe

---

## PLAN DE PROMOTION — Organique + Payant

### Organique GRATUIT (par ordre de priorité)

#### 1. SEO — Blog (déjà en cours) ★★★★★
- 1 article/semaine par site (FR + EN) = 24 articles/an/site
- Résultats visibles : 2-3 mois, plein effet 6-12 mois
- Chaque article ramène du trafic indéfiniment (effet cumulé)
- Cibler les mots-clés longue traîne KD < 25 (voir SEO_BIBLE.md)

#### 2. TikTok / Instagram Reels ★★★★★
- Format : "Je réécris ta bio Tinder en 30 secondes" (avant/après)
- Vidéos 15-60 secondes, face caméra ou texte animé
- 3-5 vidéos/semaine minimum
- Lien en bio vers BioParfaite.com / FixMyBio.com (via Linktree)
- MEILLEUR canal gratuit en 2026 : 1 vidéo virale = des milliers de visiteurs
- Hashtags : #tinder #datingtips #tinderprofile #biotinder #matchs

#### 3. Reddit ★★★★☆
- Subreddits EN : r/Tinder (1.3M), r/Bumble, r/dating_advice, r/hingeapp, r/OnlineDating
- Subreddits FR : r/france, r/AskFrance, r/Quebec
- Stratégie : 2 semaines de karma building (répondre, aider) → partager articles naturellement
- NE JAMAIS faire de pub directe = ban immédiat
- Reddit est cité par Google et par les IA (ChatGPT, Gemini) → visibilité SEO indirecte

#### 4. Pinterest ★★★☆☆
- Infographies : "50 idées de bio Tinder", "Phrases d'accroche qui marchent"
- Trafic stable et long terme (comme le SEO)
- Public majoritairement féminin → articles "bio femme"
- Chaque pin = lien vers article de blog

#### 5. Quora / Forums ★★☆☆☆
- Répondre aux questions avec un lien vers l'article
- Peu d'effort, trafic régulier mais faible

### Publicité PAYANTE (si budget disponible)

| Plateforme | Budget min./mois | ROI attendu | Avantage | Inconvénient |
|---|---|---|---|---|
| **Google Ads** | 150-300€ | Élevé | Intent d'achat direct ("générateur bio tinder") | CPC potentiellement élevé |
| **TikTok Ads** | 50-200€ | Moyen-Élevé | CPM très bas, ciblage 18-35 ans | Conversion moins directe |
| **Meta Ads (FB/IG)** | 100-300€ | Moyen | Ciblage précis (intérêts dating) | Restrictions contenu dating |
| **Reddit Ads** | 50-150€ | Moyen | Audience ciblée par subreddit | Volume limité |

> Recommandation : commencer par Google Ads (mots-clés à forte intention) quand les premières ventes organiques sont confirmées.

---

## PROGRESSION SEO — Comment le site prend de la valeur

### Mois par mois (Domain Authority & trafic)
| Période | Domain Authority (DA) | Trafic organique estimé | Ce qui se passe |
|---|---|---|---|
| **Mois 0-1** (maintenant) | DA 1-5 | 0-50/mois | Google indexe les pages, "sandbox" |
| **Mois 2-3** | DA 5-10 | 50-500/mois | Premiers articles référencés en page 3-5 |
| **Mois 4-6** | DA 10-15 | 500-2 000/mois | Articles longue traîne atteignent page 1-2 |
| **Mois 7-12** | DA 15-25 | 2 000-8 000/mois | Mots-clés moyens en page 1, effet cumulé |
| **Année 2** | DA 25-40 | 8 000-30 000/mois | Autorité établie, concurrence avec les moyens |
| **Année 3+** | DA 40+ | 30 000+/mois | Trafic stable, mots-clés compétitifs accessibles |

### Ce qui fait monter le DA (Domain Authority)
1. **Âge du domaine** — Google fait davantage confiance aux domaines anciens (patience)
2. **Backlinks** — Chaque site qui pointe vers toi = un "vote" (les articles Reddit/forums comptent)
3. **Contenu régulier** — 1 article/semaine montre que le site est actif et sérieux
4. **Trafic utilisateur** — Plus de visiteurs = signaux positifs (temps passé, pages vues)
5. **Maillage interne** — Plus d'articles = plus de liens internes = meilleur référencement global

### Effet composé du SEO (exponentiel, pas linéaire)
- Article 1 seul → trafic limité
- 10 articles → chacun pousse les autres (maillage interne)
- 25 articles → Google considère le site comme "expert du sujet" (Topical Authority)
- 50+ articles → le site se positionne même sur des mots-clés non ciblés directement

---

## PROJECTIONS FINANCIÈRES — Année 1

### Hypothèses
- Prix : 9,97€/CAD par vente | Coût API : ~0,05$ | Marge nette : ~95%
- Coûts fixes : ~30$/an (2 domaines) | Hébergement : 0$ (GitHub Pages)

### Scénario Réaliste Moyen (SEO + contenu social, 2 sites FR/EN)
| Période | Trafic/mois (2 sites) | Taux conversion | Ventes/mois | CA mensuel |
|---|---|---|---|---|
| Mois 1-3 | 200-1 000 | 1.5% | 3-15 | 30-150€ |
| Mois 4-6 | 1 000-5 000 | 2% | 20-100 | 200-1 000€ |
| Mois 7-12 | 5 000-15 000 | 2.5% | 125-375 | 1 250-3 740€ |
| **Total Année 1** | | | **~700-2 500 ventes** | **~7 000-25 000€ net** |

> Ces projections supposent : publication régulière (1 article/semaine), présence sur TikTok/Reddit, 2 sites actifs. Sans promotion sociale, diviser par 2-3.

---

## PHASE 3 — PROJET ASTROLOGIE IA (après FixMyBio + version ES)

> Ne pas démarrer avant que les sites rencontre FR + EN tournent et génèrent des ventes (minimum 3-6 mois).
> Infrastructure identique : site statique + formulaire + N8N + Claude + Stripe + GitHub Pages.

### Le marché
- Marché mondial astrologie 2026 : **17.7 milliards $** (croissance 20%/an)
- 80% des millennials/Gen Z consultent l'astrologie régulièrement
- Prix moyen d'une consultation astrologue : **100-300$**
- Concurrents IA (Arcanavana, AstroChart.ai, XORD) → surtout des abonnements mensuels
- **Très peu de concurrence IA en français** → même avantage que BioParfaite

### Positionnement — NE PAS juste vendre de l'astrologie

Le problème des concurrents : ils vendent un "thème astral" = un produit générique.
Les gens n'achètent pas un thème astral, ils achètent une **réponse à un problème**.

#### Angles de positionnement possibles (à valider)

| Angle | Problème résolu | Cible | Prix potentiel | Potentiel |
|---|---|---|---|---|
| **"Guide de vie astral"** | "Je suis perdu(e), je ne sais pas quoi faire" | 25-40 ans en transition de vie | 29.97-49.97$ | ★★★★★ |
| **Compatibilité amoureuse** | "Est-ce que cette personne est faite pour moi ?" | Couples, célibataires | 19.97-29.97$ | ★★★★★ |
| **Astro-carrière** | "Quel métier me correspond vraiment ?" | Étudiants, reconversion pro | 24.97-39.97$ | ★★★★☆ |
| **Thème astral bébé/enfant** | "Comment élever mon enfant selon sa personnalité ?" | Parents (marché émotionnel) | 29.97-39.97$ | ★★★★☆ |
| **Prévisions annuelles** | "À quoi ressemble mon année 2027 ?" | Tout le monde (récurrence annuelle) | 14.97-24.97$ | ★★★★☆ |
| **Astro-séduction** | "Comment séduire selon mon signe ?" → pont avec BioParfaite | Célibataires | 14.97$ | ★★★☆☆ |

#### Idées de différenciation
- **Pack multi-lecture** : thème natal + compatibilité + prévisions = 49.97-69.97$ (up-sell)
- **Format visuel** : PDF premium illustré avec carte du ciel personnalisée (pas juste du texte email)
- **Pont avec BioParfaite** : après le thème astral → "Découvre aussi ta bio idéale selon ton signe" (cross-sell)
- **Contenu blog SEO** : "Compatibilité Bélier-Scorpion", "Horoscope 2027 Gémeaux" → mots-clés longue traîne infinis (12 signes × 12 combinaisons = 144 articles de compatibilité)
- **Saisonnalité** : pics de ventes au Nouvel An (bonnes résolutions), Saint-Valentin (compatibilité), rentrée (carrière)
- **Langue** : FR d'abord (quasi aucun concurrent IA), puis EN + ES

#### APIs astronomiques — Données planétaires en temps réel
Les positions planétaires sont des données astronomiques réelles (pas inventées). Des APIs fournissent ces calculs :

| API | Données fournies | Prix |
|---|---|---|
| **Swiss Ephemeris** | Positions planétaires ultra-précises (référence NASA) | Open source / gratuit |
| **AstrologyAPI.com** | Thème natal, transits, compatibilité, prédictions | ~20$/mois |
| **Prokerala Astrology API** | Thème natal, horoscope, compatibilité | Gratuit (limité) puis payant |
| **Aztro API** | Horoscope quotidien par signe (basique) | Gratuit |

**Workflow avec données réelles :**
```
Swiss Ephemeris (positions planétaires du jour/semaine)
         ↓
Thème natal du client (date + heure + lieu de naissance → stocké)
         ↓
Claude reçoit les transits de la semaine + thème natal
         ↓
Interprétation personnalisée unique (différente chaque semaine)
         ↓
Email automatique (N8N) ou PDF
```

#### Modèle de revenus — Abonnement récurrent (game changer)
Contrairement à BioParfaite (achat unique), l'astrologie permet un modèle **par abonnement** :

| Offre | Prix | Livrable | Récurrence |
|---|---|---|---|
| Thème natal complet | 29.97-49.97$ | PDF 15-20 pages illustré | One-shot |
| Compatibilité détaillée | 29.97$ | PDF 2 personnes, thèmes croisés | One-shot |
| Horoscope perso hebdo | 4.97$/mois | Email chaque lundi, transits réels | Abonnement |
| Pack Premium | 9.97$/mois | Hebdo + alertes transits majeurs + conseils | Abonnement |
| Prévisions annuelles | 19.97$ | PDF année complète | Annuel (récurrent) |

**Projections abonnement :**
- 100 abonnés × 9.97$/mois = 997$/mois
- 500 abonnés × 9.97$/mois = **4 985$/mois** (~60 000$/an)
- 1 000 abonnés × 9.97$/mois = **9 970$/mois** (~120 000$/an)
- Coût API + Claude par abonné : ~0.10-0.20$/semaine → marge ~95%

#### Concurrents analysés (astrologie)

| Site | Modèle | Points forts | Points faibles |
|---|---|---|---|
| **ShivShakti.fr** | Contenu astro SEO → vend des bracelets (39-49€) | Contenu long, Google Ads actif | Design basique, contenu recyclé, pas personnalisé |
| **Astrologie.fr** | Portail classique → consultation téléphonique (3.5-9.5€/min) | Gros DA, thème natal gratuit | Design daté, pas de produit digital, modèle ancien |
| **Arcanavana** | App IA multi-traditions | 4 systèmes (Western, Vedic, BaZi, Chinese) | 24.99$/mois cher, pas de contenu SEO |
| **AstroChart.ai** | App IA multilingue | Multi-langues, interface propre | Pas de blog SEO, pas de PDF |
| **Co-Star** (app) | App mobile gratuite + premium | Millions d'utilisateurs, beau design | App seulement, pas de site web SEO |
| **The Pattern** (app) | App mobile IA | UX moderne, social features | App seulement, anglais uniquement |

**Avantage clé** : aucun de ces concurrents ne combine contenu SEO massif (144+ articles) + produit personnalisé par données planétaires réelles + design moderne + prix accessible. En français, le marché est quasi vide.

#### SEO Astrologie — La mine d'or de contenu
| Type de contenu | Nombre d'articles | Exemple | Volume recherche |
|---|---|---|---|
| Compatibilité signe×signe | **144 articles** | "Compatibilité Bélier Scorpion" | 1 000-10 000/mois chacun |
| Horoscope mensuel par signe | **144/an** (12×12 mois) | "Horoscope Gémeaux juin 2027" | 5 000-20 000/mois |
| Personnalité par signe | **12 articles** | "Personnalité Balance" | 3 000-8 000/mois |
| Ascendant par signe | **12 articles** | "Ascendant Vierge signification" | 2 000-5 000/mois |
| Signe lunaire | **12 articles** | "Lune en Scorpion" | 1 000-3 000/mois |
| **Total potentiel** | **300+ articles** la première année | | |

> Avec 300 articles ciblant chacun un mot-clé à 1 000-10 000 recherches/mois, le trafic total pourrait atteindre **50 000-200 000 visiteurs/mois** à maturité. Même avec 1% de conversion en abonnement, ça donne 500-2 000 abonnés.

#### Ce qu'il faudra produire
- [ ] Recherche de noms de domaine (.com) — idées : AstroGuide, MonCielAstral, etc.
- [ ] Recherche mots-clés astrologie FR + EN (voir format SEO_BIBLE.md)
- [ ] Analyse concurrents approfondie (Co-Star, The Pattern, apps)
- [ ] Tester Swiss Ephemeris / AstrologyAPI → vérifier les données
- [ ] Prompt Claude spécialisé astrologie (données astronomiques + interprétation créative)
- [ ] Landing page + formulaire (date/heure/lieu de naissance) — design dark/neon comme BioParfaite
- [ ] Système de génération PDF illustré (carte du ciel + rapport)
- [ ] Produits Stripe (one-shot + abonnement mensuel)
- [ ] Workflow N8N (one-shot + cron hebdomadaire pour abonnés)
- [ ] 12 articles de base (1 par signe)
- [ ] 144 articles de compatibilité (production semi-automatisée avec Claude)
- [ ] Pages légales
- [ ] Configuration Stripe pour paiements récurrents (abonnements)

#### Autres idées de business IA (même modèle, pour plus tard)
| Idée | Cible | Prix | Potentiel |
|---|---|---|---|
| Lettre de motivation IA | Chercheurs d'emploi | 9.97-14.97$ | ★★★★☆ |
| Bio LinkedIn IA | Professionnels | 14.97$ | ★★★★☆ |
| Discours de mariage IA | Mariés/témoins | 14.97-24.97$ | ★★★☆☆ |
| Description Airbnb IA | Propriétaires | 14.97-29.97$ | ★★★☆☆ |

---

## NOTES IMPORTANTES
- Repo GitHub : https://github.com/Patcordier/bioparfaite
- Site live : https://patcordier.github.io/bioparfaite/
- Clés_privées.txt est protégé par .gitignore (jamais publié sur GitHub)
- Pour modifier une question du formulaire : ouvrir formulaire.html, changer le texte
- Pour modifier un prix : changer dans la section PRICING du script (index.html fin de fichier)
- Pour mettre à jour le site : modifier les fichiers puis git add, commit, push

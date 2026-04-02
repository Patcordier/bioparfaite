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
- [ ] Branding Stripe : ajouter logo BioParfaite + couleur accent (Paramètres > Profil Stripe > Branding)
- [ ] Articles blog #2 à #4 (voir calendrier de publication ci-dessous)
- [ ] Version anglophone du site (dupliquer et traduire)
- [ ] Nom de domaine anglophone (à choisir)
- [ ] Page de remerciement post-paiement Stripe (redirect après paiement)
- [ ] Google Analytics pour suivre les visites

## CONCURRENTS ANALYSÉS
- [x] **Roast.dating** — Leader, traduit de l'anglais, CTA agressif, 84k+ clients
- [x] **Texting Academy** — Bon contenu long-form, ton "coach séduction"
- [x] **stat-rencontres.fr** — Générateur bio gratuit basique, site brouillon
- [ ] **DatingZest** — Vend des numéros de téléphone pour vérification d'apps

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

## NOTES IMPORTANTES
- Repo GitHub : https://github.com/Patcordier/bioparfaite
- Site live : https://patcordier.github.io/bioparfaite/
- Clés_privées.txt est protégé par .gitignore (jamais publié sur GitHub)
- Pour modifier une question du formulaire : ouvrir formulaire.html, changer le texte
- Pour modifier un prix : changer dans la section PRICING du script (index.html fin de fichier)
- Pour mettre à jour le site : modifier les fichiers puis git add, commit, push

# BioParfaite.com — Roadmap & Suivi

## FAIT
- [x] Landing page (index.html) — design dark/neon, responsive, mobile-first
- [x] Formulaire diagnostic (formulaire.html) — 7 questions, navigation étape par étape
- [x] Branding "BioParfaite.com" appliqué partout
- [x] Toutes mentions "IA" supprimées, remplacées par "nos experts" / "notre méthode"
- [x] 6 apps de rencontre intégrées : Tinder, Bumble, Hinge, Happn, Fruitz, Badoo
- [x] Géolocalisation IP : prix en $ CAD (Canada) ou € (Europe/Afrique) automatique
- [x] Pricing psychologique : 9,97$ CAD / 9,97€
- [x] Image Stripe générée (assets/bioparfaite-stripe-product.png)
- [x] Produits Stripe créés (BioParfaite CAD + BioParfaite EUR)
- [x] SEO : title + meta description optimisés à chaque modification
- [x] Ordre du formulaire optimisé pour la conversion (facile → difficile → email)

## A FAIRE — Priorité haute
- [x] Brancher les 2 liens Stripe dans le site
- [ ] Acheter le domaine bioparfaite.com
- [ ] Héberger le site (GitHub Pages gratuit ou autre)
- [x] Brancher le formulaire au webhook N8N
- [x] S'inscrire sur Anthropic + mettre 10$ + récupérer clé API
- [x] Configurer le noeud N8N "Message a model" : Anthropic, claude-opus-4-6, prompt HTML
- [x] Prompt Claude rédigé et sauvegardé (voir PROMPT_CLAUDE.md v3)
- [x] Configurer le noeud N8N "Send email" : template HTML aux couleurs du site
- [x] Tester le parcours complet : formulaire → N8N → Claude → email client (~0,04$ par génération)

## A FAIRE — Priorité moyenne
- [ ] Branding Stripe : ajouter logo BioParfaite + couleur accent #ff2d78 (Paramètres > Profil Stripe > Branding)
- [ ] Blog / articles SEO (voir section "Blog" ci-dessous)
- [ ] Version anglophone du site (dupliquer et traduire)
- [ ] Nom de domaine anglophone (à choisir)
- [ ] Page de remerciement post-paiement Stripe (redirect après paiement)

## A FAIRE — Priorité basse / idées futures
- [ ] Ajouter Google Analytics pour suivre les visites
- [ ] Créer des codes promo Stripe pour campagnes marketing
- [ ] Témoignages réels (remplacer les fictifs quand tu auras de vrais clients)
- [ ] Tester d'autres prix (A/B testing)
- [ ] Ajouter un chatbot ou FAQ interactive
- [ ] Version premium (plus de bios, coaching profil complet)

---

## DECISIONS PRISES
| Sujet | Décision | Raison |
|-------|----------|--------|
| Nom de domaine FR | bioparfaite.com | SEO optimal, francophonie entière |
| Extension | .com uniquement | Universel, pas besoin de .fr et .ca |
| Prix | 9,97$ / 9,97€ | Pricing psychologique (fin en 7) |
| Mentions IA | Supprimées | Eviter que les clients aillent sur ChatGPT |
| Back-office | Pas nécessaire | Stripe + N8N suffisent, modifications dans le HTML |
| Ordre formulaire | Facile → clics → texte → email | Maximise le taux de complétion |
| Taxes Stripe | Pas activées pour l'instant | A activer quand inscrit aux taxes |

---

## BLOG — Plan de contenu SEO
Objectif : attirer du trafic Google gratuit avec des articles que les célibataires recherchent.

### Articles à écrire (par priorité SEO) :
1. "Les 20 meilleures bios Tinder pour homme en 2026"
2. "Les 15 meilleures bios Tinder pour femme en 2026"
3. "30 phrases d'accroche Bumble qui marchent vraiment"
4. "Comment écrire une bio Hinge qui donne envie de matcher"
5. "Bio Tinder drôle : 25 exemples qui font rire (et matcher)"
6. "Premières phrases sur Fruitz : comment briser la glace"
7. "Bio Badoo : comment se démarquer des autres profils"
8. "Comment aborder quelqu'un sur une app de rencontre sans être bizarre"
9. "Happn : 10 astuces pour un profil qui attire"
10. "Pourquoi tu n'as pas de matchs sur Tinder (et comment corriger ça)"

### Format recommandé :
- 800 à 1500 mots par article
- Exemples concrets de bios et phrases
- CTA vers BioParfaite à la fin de chaque article
- PAS de commentaires publics (voir ci-dessous)

---

## NOTES IMPORTANTES
- Le formulaire est prêt à être branché sur N8N (webhook commenté dans le code)
- Les liens Stripe placeholder sont dans index.html lignes ~430-431
- Pour modifier une question du formulaire : ouvrir formulaire.html, changer le texte
- Pour modifier un prix : changer dans la section PRICING du script (index.html fin de fichier)

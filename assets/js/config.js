/* =====================================================================
   SITE SETTINGS - edit here once, every page updates (header, top bar, footer,
   floating WhatsApp/Call buttons, booking slots).
   Rendered by assets/js/layout.js and assets/js/main.js.
   ===================================================================== */
window.SITE = {
  /* Brand */
  name: "DISHA Advanced Surgical & Laser Piles Clinic",  // full clinic name (alt text, aria labels, copyright)
  short: "DISHA",  // logo main word
  subtitle: "Advanced Surgical & Laser Piles Clinic",  // logo small line
  about: "Journey towards better life. Advanced laser piles and laparoscopic surgery in Pune by Dr. Abhijeet Suresh Shinde.",  // footer intro text

  /* Contact */
  phone: "+919766815782",  // used in tel: links
  phoneDisplay: "+91 97668 15782",  // shown on screen
  whatsapp: "919766815782",  // country code + number, no + sign
  waText: "Hello, I would like to enquire",  // pre-filled WhatsApp message
  email: "info@dishaclinic.example",
  address: "1st Floor, OPD No. 2, Survey No. 22/2, Ganga Altus, F Building, Cherry Life, Near Manipal Hospital, Thite Nagar, Kharadi, Pune, Maharashtra 411014",
  hours: "Daily: 10:00 AM – 9:00 PM",
  callAhead: "Call ahead for appointments",
  year: 2026,  // copyright year in footer

  /* Social links (replace '#' with the real page URL) */
  social: [
    {"label": "Instagram", "letter": "I", "url": "#"},
    {"label": "Facebook", "letter": "F", "url": "#"},
    {"label": "LinkedIn", "letter": "L", "url": "#"},
    {"label": "YouTube", "letter": "Y", "url": "#"},
  ],

  /* Booking form */
  slots: ["10:00 AM", "11:00 AM", "12:00 PM", "01:00 PM", "02:00 PM", "03:00 PM", "04:00 PM", "05:00 PM", "06:00 PM", "07:00 PM", "08:00 PM"],  // appointment time slots
  closedDays: [],  // weekday numbers 0=Sun ... 6=Sat that are closed

  /* Header "Services" dropdown (7 core services). Footer labels still come from serviceGroups below. */
  menuServices: [
    { slug: "piles-haemorrhoid-surgery", label: "Piles (Haemorrhoids)" },
    { slug: "fissure-treatment", label: "Fissure in Ano" },
    { slug: "fistula-treatment", label: "Fistula in Ano" },
    { slug: "pilonidal-sinus-surgery", label: "Pilonidal Sinus" },
    { slug: "hernia-repair-surgery", label: "Hernia" },
    { slug: "appendix-surgery", label: "Appendix" },
    { slug: "gallbladder-stone-surgery", label: "Gallbladder" },
  ],

  /* Services menu (header dropdown). To add a service: copy a services/<folder>/, then add one line here. */
  serviceGroups: [
    { title: "Anorectal Surgeries", items: [
      { slug: "laser-piles-treatment", label: "Laser Piles Treatment" },
      { slug: "piles-haemorrhoid-surgery", label: "Piles (Haemorrhoid) Treatment" },
      { slug: "fissure-treatment", label: "Anal Fissure Treatment" },
      { slug: "fistula-treatment", label: "Anal Fistula Treatment" },
      { slug: "pilonidal-sinus-surgery", label: "Pilonidal Sinus Treatment" },
      { slug: "perianal-abscess-drainage", label: "Perianal Abscess Treatment" },
    ] },
    { title: "Laparoscopic & Abdominal Surgeries", items: [
      { slug: "laparoscopic-surgery", label: "Laparoscopic (Keyhole) Surgery" },
      { slug: "gallbladder-stone-surgery", label: "Gallbladder Stone Surgery" },
      { slug: "hernia-repair-surgery", label: "Hernia Repair Surgery" },
      { slug: "appendix-surgery", label: "Appendix Surgery" },
      { slug: "diagnostic-laparoscopy", label: "Diagnostic Laparoscopy" },
      { slug: "bowel-surgery", label: "Small & Large Bowel Surgery" },
    ] },
    { title: "Urological Surgeries", items: [
      { slug: "kidney-stone-treatment", label: "Kidney Stone Treatment" },
      { slug: "ureteric-stone-removal", label: "Ureteric Stone Removal (URS)" },
      { slug: "prostate-surgery", label: "Prostate Surgery (TURP)" },
      { slug: "stricture-urethra", label: "Stricture Urethra Treatment" },
      { slug: "hydrocele-surgery", label: "Hydrocele Surgery" },
      { slug: "circumcision-surgery", label: "Circumcision (Adult & Child)" },
    ] },
    { title: "General & Day-care Surgeries", items: [
      { slug: "lipoma-cyst-removal", label: "Lipoma, Cyst & Swelling Removal" },
      { slug: "breast-lump-removal", label: "Breast Lump Removal" },
      { slug: "thyroid-surgery", label: "Thyroid Surgery" },
      { slug: "abscess-surgery", label: "Abscess Surgery" },
      { slug: "corn-surgery", label: "Foot Corn Treatment" },
      { slug: "ingrown-toenail-surgery", label: "Ingrown Toenail Surgery" },
    ] },
    { title: "Endoscopy, Emergency & Foot Care", items: [
      { slug: "upper-gi-endoscopy", label: "Upper GI Endoscopy" },
      { slug: "lower-gi-endoscopy", label: "Lower GI Endoscopy (Colonoscopy)" },
      { slug: "emergency-gi-surgery", label: "Emergency G.I. Surgery" },
      { slug: "diabetic-foot-surgery", label: "Diabetic Foot Care & Surgery" },
    ] },
  ],

  /* Services shown in the footer (slugs from the list above) */
  footerServices: [
    "laser-piles-treatment",
    "piles-haemorrhoid-surgery",
    "fissure-treatment",
    "fistula-treatment",
    "gallbladder-stone-surgery",
    "hernia-repair-surgery",
    "appendix-surgery",
    "kidney-stone-treatment",
  ]
};

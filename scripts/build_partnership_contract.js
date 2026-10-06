// Builds templates/RS_Links_Partnership_Agreement.docx
//
// Usage: node scripts/build_partnership_contract.js
//
// Logos: drop PNG files at templates/assets/rs-links-logo.png (and,
// optionally, templates/assets/partner-logo.png) and re-run. Until a logo
// file exists, a placeholder box is printed in the header instead.

const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ImageRun,
  Header, Footer, AlignmentType, WidthType, BorderStyle, ShadingType,
  LevelFormat, PageNumber, TabStopType, VerticalAlign, PageBreak,
} = require("docx");

const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "templates", "RS_Links_Partnership_Agreement.docx");
const OUR_LOGO = path.join(ROOT, "templates", "assets", "rs-links-logo.png");
const PARTNER_LOGO = path.join(ROOT, "templates", "assets", "partner-logo.png");

const BRAND = "0B4A35";  // RS Links green
const NAVY = "12222F";
const ACCENT = "EFB547"; // RS Links gold
const FONT = "Calibri";
const PAGE_W = 11906; // A4
const MARGIN = 1134;  // 2 cm
const CONTENT_W = PAGE_W - 2 * MARGIN;

const BLANK = "______________________________";
const SHORT = "______________";

// ---------- helpers ----------
const t = (text, o = {}) => new TextRun({ text, font: FONT, size: 21, ...o });
const b = (text, o = {}) => t(text, { bold: true, ...o });
// Fields RS Links must fill before sending (highlighted so they're easy to spot).
const ours = (text) => t(`[${text}]`, { highlight: "yellow" });

const p = (runs, o = {}) =>
  new Paragraph({
    children: Array.isArray(runs) ? runs : [t(runs)],
    spacing: { after: 120, line: 276 },
    alignment: AlignmentType.JUSTIFIED,
    ...o,
  });

const heading = (num, text) =>
  new Paragraph({
    children: [t(`${num}.  ${text.toUpperCase()}`, { bold: true, color: BRAND, size: 23 })],
    spacing: { before: 280, after: 120 },
    keepNext: true,
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "D0D7E1", space: 2 } },
  });

let clauseRef = 0;
const clause = (sec, runs) => {
  clauseRef += 1;
  return new Paragraph({
    children: [b(`${sec}.${clauseRef}  `), ...(Array.isArray(runs) ? runs : [t(runs)])],
    spacing: { after: 110, line: 276 },
    alignment: AlignmentType.JUSTIFIED,
    indent: { left: 567, hanging: 567 },
  });
};
const section = (num, title, items) => {
  clauseRef = 0;
  return [heading(num, title), ...items.map((r) => clause(num, r))];
};

const bullet = (runs) =>
  new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    children: Array.isArray(runs) ? runs : [t(runs)],
    spacing: { after: 80 },
    alignment: AlignmentType.JUSTIFIED,
  });

const border = { style: BorderStyle.SINGLE, size: 4, color: "B8C2D0" };
const borders = { top: border, bottom: border, left: border, right: border };
const noBorder = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };

const cell = (children, width, o = {}) =>
  new TableCell({
    children: (Array.isArray(children) ? children : [children]).map((c) =>
      typeof c === "string" ? new Paragraph({ children: [t(c)], spacing: { after: 40 } }) : c
    ),
    width: { size: width, type: WidthType.DXA },
    borders,
    margins: { top: 50, bottom: 50, left: 110, right: 110 },
    verticalAlign: VerticalAlign.CENTER,
    ...o,
  });

const shaded = (fill) => ({ fill, type: ShadingType.CLEAR, color: "auto" });

const table = (widths, rows) =>
  new Table({
    width: { size: widths.reduce((a, c) => a + c, 0), type: WidthType.DXA },
    columnWidths: widths,
    rows,
  });

// Two-column "label | value" table.
const fieldTable = (title, fields, labelW = 3400) => {
  const valueW = CONTENT_W - labelW;
  return table([labelW, valueW], [
    new TableRow({
      children: [
        cell(new Paragraph({ children: [b(title, { color: "FFFFFF" })] }), CONTENT_W, {
          columnSpan: 2, shading: shaded(BRAND),
        }),
      ],
    }),
    ...fields.map(([label, value]) =>
      new TableRow({
        children: [
          cell(new Paragraph({ children: [b(label)] }), labelW, { shading: shaded("F2F5F9") }),
          cell(new Paragraph({ children: Array.isArray(value) ? value : typeof value === "string" ? [t(value)] : [value] }), valueW),
        ],
      })
    ),
  ]);
};

const spacer = (after = 120) => new Paragraph({ children: [], spacing: { after } });

// ---------- header / logos ----------
const logoBlock = (file, placeholder, align) => {
  if (fs.existsSync(file)) {
    return new Paragraph({
      alignment: align,
      children: [new ImageRun({ type: "png", data: fs.readFileSync(file), transformation: { width: 165, height: 57 } })],
    });
  }
  return new Paragraph({
    alignment: align,
    children: [t(placeholder, { size: 16, color: "8A94A6", italics: true })],
  });
};

const headerTable = table([CONTENT_W / 2, CONTENT_W / 2], [
  new TableRow({
    children: [
      new TableCell({
        width: { size: CONTENT_W / 2, type: WidthType.DXA },
        borders: noBorders,
        verticalAlign: VerticalAlign.CENTER,
        children: fs.existsSync(OUR_LOGO)
          ? [logoBlock(OUR_LOGO, "", AlignmentType.LEFT)]
          : [
              new Paragraph({ children: [t("RS ", { bold: true, size: 40, color: BRAND }), t("Links", { bold: true, size: 40, color: NAVY })] }),
              new Paragraph({ children: [t("CONSULTANTS PVT. LTD.", { size: 15, color: BRAND, characterSpacing: 60 })] }),
            ],
      }),
      new TableCell({
        width: { size: CONTENT_W / 2, type: WidthType.DXA },
        borders: noBorders,
        verticalAlign: VerticalAlign.CENTER,
        children: [logoBlock(PARTNER_LOGO, "[ Party B logo (optional) ]", AlignmentType.RIGHT)],
      }),
    ],
  }),
]);

const header = new Header({
  children: [
    headerTable,
    new Paragraph({
      children: [],
      spacing: { after: 0 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: ACCENT, space: 4 } },
    }),
  ],
});

const footer = new Footer({
  children: [
    new Paragraph({
      border: { top: { style: BorderStyle.SINGLE, size: 4, color: "D0D7E1", space: 4 } },
      tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }],
      children: [
        t("RS Links Consultants Pvt. Ltd. — Partnership Agreement  |  Confidential", { size: 16, color: "6B7280" }),
        t("\tInitials:  Party A ______   Party B ______     Page ", { size: 16, color: "6B7280" }),
        new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 16, color: "6B7280" }),
        t(" of ", { size: 16, color: "6B7280" }),
        new TextRun({ children: [PageNumber.TOTAL_PAGES], font: FONT, size: 16, color: "6B7280" }),
      ],
    }),
  ],
});

// ---------- body ----------
const body = [];

body.push(
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 120, after: 60 },
    children: [t("PARTNERSHIP & RECRUITMENT COLLABORATION AGREEMENT", { bold: true, size: 32, color: BRAND })],
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 240 },
    children: [t("For Individuals, Overseas Employment Promoters (OEPs) and Recruitment Agencies", { italics: true, size: 21, color: "4B5563" })],
  }),
  table([CONTENT_W / 2, CONTENT_W / 2], [
    new TableRow({
      children: [
        cell(new Paragraph({ children: [b("Agreement Ref. No.:  "), t(SHORT)] }), CONTENT_W / 2),
        cell(new Paragraph({ children: [b("Effective Date:  "), t(SHORT)] }), CONTENT_W / 2),
      ],
    }),
    new TableRow({
      children: [
        cell(new Paragraph({ children: [b("Place of Execution:  "), t(SHORT)] }), CONTENT_W / 2),
        cell(new Paragraph({ children: [b("Term:  "), t("12 months, auto-renewing (Clause 15)")] }), CONTENT_W / 2),
      ],
    }),
  ]),
  spacer(140),
  p([t("This Partnership & Recruitment Collaboration Agreement (the "), b("“Agreement”"), t(") is entered into on the Effective Date stated above by and between:")]),
  spacer(60),
  fieldTable("PARTY A — RS LINKS CONSULTANTS PVT. LTD.", [
    ["Registered Name", "RS Links Consultants (Private) Limited"],
    ["SECP Incorporation No.", ours("Incorporation no.")],
    ["OEP Licence No. (if applicable)", ours("Licence no. & expiry")],
    ["NTN / Tax No.", ours("NTN")],
    ["Registered Address", ours("Registered office address")],
    ["Authorised Signatory", ours("Name & designation")],
    ["Email / Phone", ours("Official email / phone")],
  ]),
  p([t("(hereinafter "), b("“Party A”"), t(" or "), b("“RS Links”"), t(", which expression includes its successors and permitted assigns)")], {
    spacing: { before: 80, after: 160 },
  }),
  p([b("AND")], { alignment: AlignmentType.CENTER }),
  fieldTable("PARTY B — PARTNER", [
    ["Partner Type (tick one)", "☐ Individual     ☐ OEP     ☐ Recruitment Agency     ☐ Other: __________"],
    ["Full Name / Company Name", ""],
    ["CNIC / Passport No. (Individual)", ""],
    ["Company Registration No.", ""],
    ["OEP / Recruitment Licence No. & Expiry", ""],
    ["NTN / Tax No.", ""],
    ["Registered / Residential Address", ""],
    ["City & Country", ""],
    ["Authorised Representative & Designation", ""],
    ["Email", ""],
    ["Phone / WhatsApp", ""],
    ["Website / LinkedIn", ""],
  ]),
  p([t("(hereinafter "), b("“Party B”"), t(" or the "), b("“Partner”"), t(", which expression includes its successors and permitted assigns)")], {
    spacing: { before: 80, after: 160 },
  }),
  p([t("Party A and Party B are each referred to as a "), b("“Party”"), t(" and together as the "), b("“Parties”"), t(".")]),
);

body.push(new Paragraph({
  children: [t("BACKGROUND", { bold: true, color: BRAND, size: 23 })],
  spacing: { before: 240, after: 100 },
  keepNext: true,
  pageBreakBefore: true,
  border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: "D0D7E1", space: 2 } },
}));
body.push(
  p("A.  Party A is a company incorporated in Pakistan engaged in recruitment, manpower sourcing and HR consultancy services for employers and clients in Pakistan and internationally."),
  p("B.  Party B is an individual, Overseas Employment Promoter or recruitment agency with access to employer demands and/or qualified candidates."),
  p("C.  The Parties wish to collaborate on a non-exclusive basis, sharing demands and candidates for mutual benefit, on the terms and conditions set out below."),
);

body.push(
  ...section(1, "Definitions", [
    [b("“Demand” "), t("means any job order, vacancy, manpower requirement or business requirement received from an employer or client and shared by one Party with the other.")],
    [b("“Candidate” "), t("means any individual whose profile, CV or details are introduced by one Party to the other or to a Client under this Agreement.")],
    [b("“Client” "), t("means any employer, company or end-user to whom Candidates are presented or from whom a Demand originates.")],
    [b("“Placement” "), t("means a Candidate accepting an offer of employment or engagement from a Client, or as otherwise defined in the relevant Case Agreement.")],
    [b("“Case Agreement” "), t("means the written terms agreed for a specific Demand or Candidate in the form of Annexure A (or by email expressly confirmed by both Parties), forming part of this Agreement.")],
    [b("“Confidential Information” "), t("means all non-public information disclosed by either Party, including Client and Candidate details, Demands, pricing, fees, business methods and contacts.")],
  ]),

  ...section(2, "Purpose and Scope", [
    "The purpose of this Agreement is to set out the general framework under which the Parties will share Demands and Candidates and work together to fulfil them.",
    "This Agreement is a framework agreement. It does not by itself oblige either Party to provide any minimum number of Demands or Candidates, or to make any payment. Specific commercial obligations arise only under a Case Agreement.",
    "The scope of collaboration may include local and overseas recruitment, candidate sourcing and screening, document processing support, and referral of business opportunities, as agreed between the Parties from time to time.",
  ]),

  ...section(3, "Nature of Relationship", [
    "This Agreement is non-exclusive. Each Party remains free to work with other partners, agencies and clients, subject to Clauses 8 (Non-Circumvention) and 9 (Confidentiality).",
    "The Parties are independent contractors. Nothing in this Agreement creates a partnership in law, joint venture, employment or agency relationship. Neither Party may bind the other, make commitments, or represent itself as the other’s agent, without prior written consent.",
    "Each Party bears its own costs, staff, taxes and overheads unless otherwise agreed in a Case Agreement.",
  ]),

  ...section(4, "Obligations of Party A (RS Links)", [
    "Share Demands and/or Candidate requirements with Party B with reasonably accurate information on role, location, qualifications and timelines, to the extent known.",
    "Review Candidates and submissions from Party B in good faith and give feedback within a reasonable time.",
    "Keep Party B informed of the status of Candidates introduced by Party B, including interview outcomes and Placements.",
    "Make payments due to Party B strictly in accordance with the applicable Case Agreement.",
  ]),

  ...section(5, "Obligations of Party B (Partner)", [
    "Provide only genuine Demands and genuine Candidates, with true, accurate and verifiable information and documents. Party B shall not submit forged, altered or misleading documents.",
    "Obtain each Candidate’s informed consent before sharing his or her CV or personal data with Party A or any Client.",
    "Where Party B is an OEP or licensed agency, maintain a valid licence at all times, comply with all applicable emigration, labour and recruitment laws and regulations, and immediately inform Party A of any suspension, cancellation or expiry of its licence.",
    "Not charge any Candidate any fee, deposit or cost, except where expressly permitted by applicable law, and never in Party A’s name.",
    "Not make any promise, guarantee or representation to a Candidate or Client on behalf of Party A regarding jobs, visas, salaries or timelines without Party A’s written approval.",
    "Respond to Party A’s requests, and inform Party A promptly of any change in a Candidate’s availability or a Demand’s status.",
  ]),

  ...section(6, "Demand and Candidate Submission Process", [
    "Every Demand and Candidate shall be shared in writing (email or other agreed written channel) so that a clear record of the date and source of introduction exists.",
    [t("A Candidate shall be deemed introduced by the Party that first submits that Candidate’s complete profile in writing for a specific Demand. Such ownership remains valid for "), b("______ months"), t(" from the date of submission, unless otherwise stated in the Case Agreement.")],
    "Where the same Candidate is received from more than one source, the earliest complete written submission prevails. Party A’s records shall be used as the reference in case of conflict, subject to reasonable evidence from Party B.",
    "No work on a Demand or Candidate shall be treated as chargeable until a Case Agreement has been agreed for that Demand or Candidate in accordance with Clause 7.",
  ]),

  ...section(7, "Commercial Terms and Payment", [
    [b("Case-by-case basis. "), t("The Parties expressly agree that the fee, commission, service charge or any other payment for every Demand or Candidate provided by Party B will be decided separately on a case-to-case basis. No fixed rate, commission or percentage applies under this Agreement.")],
    "For each Demand or Candidate, the agreed commercial terms — including the amount, currency, payment trigger (e.g. selection, visa, deployment, joining or completion of a probation period), payment schedule, replacement or refund conditions, and any taxes — shall be recorded in a Case Agreement substantially in the form of Annexure A, or confirmed in writing by email by authorised representatives of both Parties, before work on that case begins.",
    "No payment shall be due or payable by either Party in respect of any Demand or Candidate for which a Case Agreement has not been agreed in writing. Verbal promises or understandings shall not create any payment obligation.",
    "Unless the Case Agreement states otherwise, payment becomes due only after Party A has itself received the corresponding payment from the Client, and within ______ days of such receipt against a valid invoice from Party B.",
    "Each Party is responsible for its own taxes. Any withholding tax required by law shall be deducted at source and the relevant certificate provided.",
    "Payments shall be made by bank transfer to the account given by Party B in Annexure B. Party A shall not make cash payments or payments to third-party accounts.",
    "If a Placement fails, is cancelled or a Client claims a refund or replacement, the consequences for Party B’s fee (refund, adjustment or replacement Candidate) shall be as set out in the relevant Case Agreement.",
  ]),

  ...section(8, "Non-Circumvention and Non-Solicitation", [
    "Neither Party shall, directly or indirectly, bypass the other Party to deal with any Client, Demand or Candidate introduced by the other Party, without the prior written consent of the introducing Party.",
    [t("This obligation continues during the term of this Agreement and for "), b("______ months"), t(" after its termination or expiry.")],
    "If a Party breaches this Clause, it shall pay the other Party the fee the other Party would reasonably have earned on that business, in addition to any other remedies available under law.",
    "Neither Party shall solicit or hire the other Party’s employees or staff during the term of this Agreement and for twelve (12) months thereafter without written consent.",
  ]),

  ...section(9, "Confidentiality", [
    "Each Party shall keep the other’s Confidential Information strictly confidential, use it only for the purposes of this Agreement, and disclose it only to staff who need to know it and are bound by similar obligations.",
    "Confidentiality obligations do not apply to information that is publicly available (other than through breach), already lawfully known to the receiving Party, or required to be disclosed by law or by a competent authority.",
    "These obligations survive for three (3) years after termination or expiry of this Agreement.",
  ]),

  ...section(10, "Data Protection", [
    "Each Party shall process Candidate and Client personal data lawfully, fairly and securely, only for recruitment purposes, and in compliance with applicable data-protection laws (including, where applicable, the laws of the Candidate’s or Client’s country).",
    "Personal data shall not be sold, shared with unauthorised third parties or retained longer than necessary. Each Party shall promptly notify the other of any data breach affecting shared data.",
  ]),

  ...section(11, "Ethical Recruitment, Compliance and Anti-Bribery", [
    "Both Parties shall comply with all applicable laws, including emigration, labour, anti-money-laundering, anti-bribery and anti-corruption laws.",
    "Neither Party shall engage in human trafficking, forced labour, withholding of Candidates’ passports or documents, misleading advertising, or any discriminatory practice.",
    "Neither Party shall offer, pay, request or accept any bribe, kickback or improper payment in connection with this Agreement.",
  ]),

  ...section(12, "Branding and Intellectual Property", [
    "Each Party retains ownership of its name, logo, trademarks, materials and know-how. Neither Party may use the other’s name or logo in advertising, social media, job postings or proposals without prior written approval.",
    "Party B shall not advertise any Demand received from Party A under Party A’s name, or post such Demand publicly, without Party A’s written approval.",
  ]),

  ...section(13, "Representations and Warranties", [
    "Each Party represents that it has full authority to enter into this Agreement, that the signatory is duly authorised, and that entering into this Agreement does not breach any other agreement or law binding on it.",
    "Party B represents that all information provided in this Agreement and its Annexures is true and complete, and undertakes to notify Party A of any change.",
  ]),

  ...section(14, "Indemnity and Limitation of Liability", [
    "Each Party shall indemnify the other against losses, claims, penalties and reasonable legal costs arising from its own breach of this Agreement, negligence, fraud, or breach of law, including any false Candidate document or unlawful fee charged to a Candidate.",
    "Neither Party shall be liable for indirect, consequential or loss-of-profit damages, except in cases of fraud, wilful misconduct, breach of confidentiality or breach of Clause 8.",
    "Party A does not guarantee that any Candidate will be selected or placed, or that any Demand will result in a Placement.",
  ]),

  ...section(15, "Term and Termination", [
    "This Agreement starts on the Effective Date and continues for twelve (12) months. It renews automatically for further twelve-month periods unless either Party gives written notice of non-renewal at least thirty (30) days before expiry.",
    "Either Party may terminate this Agreement for convenience by giving thirty (30) days’ written notice.",
    "Either Party may terminate immediately by written notice if the other Party commits a material breach (including fraud, forged documents, unlawful fees or loss of licence) and, where curable, fails to remedy it within seven (7) days of notice.",
    "Termination does not affect fees already earned under an agreed Case Agreement, or Clauses 8, 9, 10, 14 and 17, which survive termination.",
  ]),

  ...section(16, "Force Majeure", [
    "Neither Party is liable for delay or failure to perform caused by events beyond its reasonable control, including natural disasters, epidemics, war, government action, changes in immigration or visa policy, or embassy closures. The affected Party shall notify the other promptly and use reasonable efforts to resume performance.",
  ]),

  ...section(17, "Governing Law and Dispute Resolution", [
    [t("This Agreement is governed by the laws of "), ours("jurisdiction, e.g. the Islamic Republic of Pakistan"), t(".")],
    "The Parties shall first attempt to resolve any dispute amicably through good-faith negotiation between senior representatives within thirty (30) days of written notice of the dispute.",
    [t("Failing amicable settlement, the dispute shall be referred to arbitration by a sole arbitrator in "), ours("city"), t(" under applicable arbitration law. The award shall be final and binding. Courts at "), ours("city"), t(" shall have exclusive jurisdiction for any interim relief.")],
  ]),

  ...section(18, "Notices", [
    "All notices under this Agreement shall be in writing and sent to the addresses or email addresses stated above (or as later updated in writing). Email notices are effective when sent, unless a delivery failure message is received.",
  ]),

  ...section(19, "General", [
    "This Agreement, together with its Annexures and all Case Agreements, constitutes the entire agreement between the Parties on its subject matter and supersedes prior discussions.",
    "Any amendment must be in writing and signed (or confirmed by email) by authorised representatives of both Parties.",
    "Party B may not assign or subcontract this Agreement without Party A’s prior written consent.",
    "If any provision is held invalid, the remaining provisions remain in full force.",
    "No failure or delay in exercising a right is a waiver of that right.",
    "This Agreement may be signed in counterparts and by electronic or scanned signatures, each of which is deemed an original.",
  ]),
);

// ---------- signatures ----------
const sigCol = (title, name) => [
  new Paragraph({ children: [b(title, { color: BRAND })], spacing: { after: 120 } }),
  new Paragraph({ children: [b("For: "), name], spacing: { after: 240 } }),
  new Paragraph({ children: [t("Signature: _______________________")], spacing: { after: 140 } }),
  new Paragraph({ children: [t("Name: ___________________________")], spacing: { after: 140 } }),
  new Paragraph({ children: [t("Designation: _____________________")], spacing: { after: 140 } }),
  new Paragraph({ children: [t("CNIC / ID No.: ___________________")], spacing: { after: 140 } }),
  new Paragraph({ children: [t("Date: ____________________________")], spacing: { after: 140 } }),
  new Paragraph({ children: [t("Company stamp:")], spacing: { after: 400 } }),
];
const half = CONTENT_W / 2;

body.push(
  new Paragraph({
    keepNext: true,
    spacing: { before: 280, after: 160 },
    children: [t("IN WITNESS WHEREOF, ", { bold: true }), t("the Parties have executed this Agreement on the Effective Date by their duly authorised representatives.")],
  }),
  table([half, half], [
    new TableRow({
      cantSplit: true,
      children: [
        cell(sigCol("PARTY A", t("RS Links Consultants Pvt. Ltd.")), half),
        cell(sigCol("PARTY B", t("______________________")), half),
      ],
    }),
  ]),
  spacer(160),
  table([half, half], [
    new TableRow({
      cantSplit: true,
      children: [1, 2].map((n) =>
        cell([
          new Paragraph({ children: [b(`WITNESS ${n}`, { color: BRAND })], spacing: { after: 160 } }),
          new Paragraph({ children: [t("Signature: _______________________")], spacing: { after: 160 } }),
          new Paragraph({ children: [t("Name: ___________________________")], spacing: { after: 160 } }),
          new Paragraph({ children: [t("CNIC / ID No.: ___________________")], spacing: { after: 160 } }),
        ], half)
      ),
    }),
  ]),
);

// ---------- Annexure A: Case Agreement ----------
const annexTitle = (title, sub) => [
  new Paragraph({ children: [new PageBreak()] }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 60 },
    children: [t(title, { bold: true, size: 28, color: BRAND })],
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 240 },
    children: [t(sub, { italics: true, color: "4B5563" })],
  }),
];

body.push(
  ...annexTitle("ANNEXURE A — CASE AGREEMENT", "One form per Demand or Candidate. Payment terms are decided case by case (Clause 7)."),
  fieldTable("CASE DETAILS", [
    ["Case Ref. No.", ""],
    ["Master Agreement Ref. No.", ""],
    ["Date", ""],
    ["Case Type", "☐ Demand provided by Party B     ☐ Candidate(s) provided by Party B     ☐ Other"],
    ["Client / Employer (if disclosed)", ""],
    ["Position(s) / Trade", ""],
    ["Country / Location", ""],
    ["No. of Positions / Candidates", ""],
    ["Candidate Name(s) & Passport/CNIC No.", ""],
  ], 3600),
  spacer(140),
  fieldTable("COMMERCIAL TERMS AGREED FOR THIS CASE", [
    ["Fee / Commission Amount", ""],
    ["Currency", ""],
    ["Basis", "☐ Fixed per candidate   ☐ Fixed per demand   ☐ % of salary   ☐ Other: ________"],
    ["Paid By", "☐ Party A to Party B     ☐ Party B to Party A"],
    ["Payment Trigger", "☐ Selection   ☐ Visa issued   ☐ Deployment / joining   ☐ After probation   ☐ Other: ________"],
    ["Payment Schedule / Instalments", ""],
    ["Payment Due Within", "______ days of trigger / receipt of Client payment"],
    ["Replacement / Guarantee Period", ""],
    ["Refund Conditions", ""],
    ["Expenses (who bears which costs)", ""],
    ["Taxes", ""],
    ["Special Conditions", ""],
  ], 3600),
  spacer(140),
  p("This Case Agreement forms part of, and is governed by, the Partnership & Recruitment Collaboration Agreement between the Parties. In case of conflict on commercial terms for this case, this Case Agreement prevails."),
  table([half, half], [
    new TableRow({
      cantSplit: true,
      children: ["PARTY A — RS Links Consultants", "PARTY B"].map((title) =>
        cell([
          new Paragraph({ children: [b(title, { color: BRAND })], spacing: { after: 240 } }),
          new Paragraph({ children: [t("Signature: _______________________")], spacing: { after: 160 } }),
          new Paragraph({ children: [t("Name: ___________________________")], spacing: { after: 160 } }),
          new Paragraph({ children: [t("Date: ____________________________")], spacing: { after: 160 } }),
        ], half)
      ),
    }),
  ]),
);

// ---------- Annexure B: Partner details & documents ----------
body.push(
  ...annexTitle("ANNEXURE B — PARTY B BANK DETAILS & DOCUMENTS", "To be completed by Party B and returned with the signed Agreement."),
  fieldTable("BANK DETAILS (for payments under Clause 7)", [
    ["Account Title", ""],
    ["Bank Name & Branch", ""],
    ["Account No. / IBAN", ""],
    ["SWIFT Code (if international)", ""],
  ], 3600),
  spacer(140),
  new Paragraph({ children: [b("Documents to be attached by Party B (tick as provided):", { color: BRAND })], spacing: { after: 120 } }),
  ...[
    "☐  Copy of CNIC / Passport of Party B or its authorised representative",
    "☐  Company registration certificate (Agencies / OEPs)",
    "☐  Valid OEP / recruitment licence with expiry date (OEPs / licensed agencies)",
    "☐  NTN / tax registration certificate",
    "☐  Board resolution or authority letter for the signatory (companies)",
    "☐  Company profile and logo (optional, for joint materials — subject to Clause 12)",
  ].map((s) => new Paragraph({ children: [t(s)], spacing: { after: 100 }, indent: { left: 360 } })),
  spacer(140),
  p([t("Party B confirms that the above details are true and correct.     Signature: ____________________     Date: ______________")]),
);

const doc = new Document({
  creator: "RS Links Consultants Pvt. Ltd.",
  title: "Partnership & Recruitment Collaboration Agreement",
  styles: { default: { document: { run: { font: FONT, size: 21 } } } },
  numbering: {
    config: [{
      reference: "bullets",
      levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } }],
    }],
  },
  sections: [{
    properties: {
      page: {
        size: { width: PAGE_W, height: 16838 },
        margin: { top: 1700, bottom: 1134, left: MARGIN, right: MARGIN, header: 500, footer: 500 },
      },
    },
    headers: { default: header },
    footers: { default: footer },
    children: body.filter(Boolean),
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  fs.writeFileSync(OUT, buf);
  console.log(`Wrote ${OUT}`);
});

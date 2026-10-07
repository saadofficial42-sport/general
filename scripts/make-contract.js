// Generates an employment contract (.docx) on RS Links Consultants letterhead.
// Usage: node scripts/make-contract.js contracts/<employee>.json [out.docx]
// The letterhead (templates/letterhead/) is placed as a full-page background:
// first.jpg on page 1 (with REF/DATE lines), cont.jpg on later pages.

const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Header, Footer, ImageRun, Table,
  TableRow, TableCell, WidthType, BorderStyle, AlignmentType, PageNumber,
  LevelFormat, ShadingType, HorizontalPositionRelativeFrom, VerticalPositionRelativeFrom,
} = require("docx");

const COMPANY = "RS Links Consultants (Pvt.) Ltd.";
const BRAND = "0E6143";
const COMPANY_ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi, Pakistan";
const FONT = "Calibri";

const inFile = process.argv[2];
if (!inFile) {
  console.error("Usage: node scripts/make-contract.js <employee.json> [out.docx]");
  process.exit(1);
}
const e = JSON.parse(fs.readFileSync(inFile, "utf8"));
const outFile = process.argv[3] || inFile.replace(/\.json$/, ".docx");
const LETTERHEAD_DIR = path.join(__dirname, "..", "templates", "letterhead");
const salary = e.salaryPkr ? `PKR ${e.salaryPkr.toLocaleString("en-US")}/-` : "PKR ______________/-";

const r = (text, opts = {}) => new TextRun({ text, font: FONT, size: 22, ...opts });
const b = (text, opts = {}) => r(text, { bold: true, ...opts });
const p = (children, opts = {}) =>
  new Paragraph({ children: Array.isArray(children) ? children : [r(children)],
    spacing: { after: 120, line: 276 }, alignment: AlignmentType.JUSTIFIED, ...opts });

let clauseNo = 0;
const clause = (title) => {
  clauseNo += 1;
  return new Paragraph({
    children: [b(`${clauseNo}. ${title.toUpperCase()}`, { color: BRAND })],
    spacing: { before: 200, after: 100 }, keepNext: true,
  });
};
const sub = (children, opts = {}) => new Paragraph({
  children: (Array.isArray(children) ? children : [children]).map((c) => (typeof c === "string" ? r(c) : c)),
  numbering: { reference: "sub", level: 0, instance: clauseNo },
  spacing: { after: 80, line: 276 }, alignment: AlignmentType.JUSTIFIED, ...opts,
});

// A4 page in EMU-free pixel units docx-js expects (96 dpi): 595.92 x 842.88 pt
const PAGE_PX = { width: 795, height: 1124 };
const background = (file) => new Header({ children: [new Paragraph({ children: [
  new ImageRun({ type: "jpg", data: fs.readFileSync(path.join(LETTERHEAD_DIR, file)),
    transformation: PAGE_PX,
    floating: {
      horizontalPosition: { relative: HorizontalPositionRelativeFrom.PAGE, offset: 0 },
      verticalPosition: { relative: VerticalPositionRelativeFrom.PAGE, offset: 0 },
      behindDocument: true, allowOverlap: true,
    } }),
] })] });

// Small page counter sitting just above the letterhead's tagline band.
const footer = new Footer({ children: [
  new Paragraph({
    alignment: AlignmentType.RIGHT,
    children: [
      r(`Employment Agreement — ${e.name}  |  Page `, { size: 16, color: "6B7C75" }),
      new TextRun({ children: [PageNumber.CURRENT], size: 16, color: "6B7C75", font: FONT }),
      r(" of ", { size: 16, color: "6B7C75" }),
      new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 16, color: "6B7C75", font: FONT }),
    ],
  }),
] });

// Key-terms summary table
const MARGIN_X = 1000;
const W = 11906 - 2 * MARGIN_X; // A4 text width (DXA)
const COLS = [2800, W - 2800];
const cellBorder = { style: BorderStyle.SINGLE, size: 4, color: "B8D4C7" };
const borders = { top: cellBorder, bottom: cellBorder, left: cellBorder, right: cellBorder };
const row = (k, v) => new TableRow({ children: [
  new TableCell({ width: { size: COLS[0], type: WidthType.DXA }, borders,
    shading: { type: ShadingType.CLEAR, fill: "E8F3EE", color: "auto" },
    margins: { top: 60, bottom: 60, left: 120, right: 120 },
    children: [new Paragraph({ children: [b(k)] })] }),
  new TableCell({ width: { size: COLS[1], type: WidthType.DXA }, borders,
    margins: { top: 60, bottom: 60, left: 120, right: 120 },
    children: [new Paragraph({ children: [r(v)] })] }),
] });
const terms = new Table({
  width: { size: W, type: WidthType.DXA }, columnWidths: COLS,
  rows: [
    row("Employee Name", e.name),
    row("Father's Name", e.fatherName),
    row("CNIC No.", e.cnic),
    row("Designation", e.position),
    row("Mode of Work", e.workMode),
    row("Monthly Salary", `${salary} (${e.salaryWords} only)`),
    row("Salary Disbursement", `Paid ${e.payDay}`),
    row("Date of Joining", e.startDate),
  ],
});

const sigBlock = (left, right) => {
  const half = W / 2;
  const none = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
  const nb = { top: none, bottom: none, left: none, right: none };
  const col = (lines) => new TableCell({ width: { size: half, type: WidthType.DXA }, borders: nb,
    children: lines.map((l, i) => new Paragraph({ spacing: { after: 60 }, keepNext: true,
      children: [i === 0 ? b(l, { color: BRAND }) : r(l)] })) });
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [half, half],
    rows: [new TableRow({ cantSplit: true, children: [col(left), col(right)] })] });
};

function modeOfWork() {
  const mode = (e.workMode || "").toLowerCase();
  if (mode === "remote") return [
    sub(["The Employee shall work on a ", b("remote"), " basis and is not required to attend the Company's office on a regular basis, unless specifically requested by the Company with reasonable notice."]),
    sub("The Employee shall be available and reachable through the Company's agreed communication channels during working hours, attend scheduled online meetings, and maintain a reliable internet connection and suitable workspace at their own cost."),
    sub(`Working hours shall be as communicated by the Company from time to time.${e.workHoursNote ? " " + e.workHoursNote : ""}`),
  ];
  if (mode === "on-site" || mode === "in office") return [
    sub(["The Employee shall work ", b("in office"), `, from the Company's office at ${COMPANY_ADDRESS}, or at such other location as the Company may reasonably direct.`]),
    sub(`Working days and hours shall be as communicated by the Company from time to time.${e.workHoursNote ? " " + e.workHoursNote : ""}`),
  ];
  return [
    sub("The Employee shall work from the Company's office or remotely, as directed by the Company in writing from time to time."),
    sub(`Working days and hours shall be as communicated by the Company from time to time.${e.workHoursNote ? " " + e.workHoursNote : ""}`),
  ];
}

// Optional per-case commission: e.commission = { rates: [[region, amountPkr]], terms: [..] }
function commissionClause() {
  if (!e.commission) return [];
  const C = [W - 720 - 3000, 3000];
  const cell = (child, w, shade) => new TableCell({ width: { size: w, type: WidthType.DXA }, borders,
    ...(shade ? { shading: { type: ShadingType.CLEAR, fill: "E8F3EE", color: "auto" } } : {}),
    margins: { top: 60, bottom: 60, left: 120, right: 120 }, children: [new Paragraph({ keepNext: true, children: [child] })] });
  const table = new Table({ width: { size: W - 720, type: WidthType.DXA }, columnWidths: C,
    indent: { size: 720, type: WidthType.DXA },
    rows: [
      new TableRow({ tableHeader: true, children: [cell(b("Destination"), C[0], true), cell(b("Commission per approved case"), C[1], true)] }),
      ...e.commission.rates.map(([region, amt]) => new TableRow({ cantSplit: true, children: [
        cell(r(region), C[0]), cell(b(`PKR ${amt.toLocaleString("en-US")}/-`), C[1])] })),
    ] });
  return [
    clause("Commission"),
    sub("In addition to the salary, the Employee shall be entitled to a commission for every approved case submitted by the Employee, at the following rates:", { keepNext: true }),
    table,
    new Paragraph({ spacing: { after: 80 }, children: [] }),
    ...e.commission.terms.map(sub),
  ];
}

const body = [
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 },
    children: [b("EMPLOYMENT AGREEMENT", { size: 32, color: BRAND })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 240 },
    children: [r(e.position, { size: 24, italics: true })] }),

  p([r("This Employment Agreement (the "), b("“Agreement”"), r(") is made and entered into on the date stated above by and between:")]),
  p([b(COMPANY), r(`, a private limited company incorporated under the laws of Pakistan, having its office at ${COMPANY_ADDRESS} (hereinafter the `), b("“Company”"), r(", which expression shall include its successors and assigns);")]),
  p([b("AND", { color: BRAND })], { alignment: AlignmentType.CENTER }),
  p([b(`${e.salutation} ${e.name}`), r(`, ${e.relation} ${e.fatherName}, holding CNIC No. `), b(e.cnic), r(" (hereinafter the "), b("“Employee”"), r(").")]),
  p("The Company and the Employee are each referred to as a “Party” and together as the “Parties”. The Parties agree to the following terms and conditions."),

  new Paragraph({ spacing: { before: 120, after: 100 }, children: [b("KEY TERMS", { color: BRAND })] }),
  terms,

  clause("Appointment and Position"),
  sub(["The Company appoints the Employee to the position of ", b(e.position), " with effect from the Date of Joining stated above, and the Employee accepts this appointment on the terms of this Agreement."]),
  sub("The Employee shall report to the Company's management or to such person as the Company may designate from time to time."),

  clause("Duties and Responsibilities"),
  ...e.duties.map(sub),
  sub("The Employee shall perform such other related duties as may reasonably be assigned by the Company, and shall carry out all duties diligently, honestly and to the best of their ability."),

  clause("Mode of Work"),
  ...modeOfWork(),

  clause("Remuneration"),
  sub(["The Employee shall be paid a fixed monthly salary of ", b(salary), ` (${e.salaryWords} only).`]),
  sub(["The salary shall be disbursed ", b(e.payDay), " for the preceding month of service, by bank transfer or any other mode agreed between the Parties."]),
  sub("Salary for any incomplete month of service shall be calculated on a pro-rata basis. Any applicable taxes shall be deducted in accordance with the laws of Pakistan."),

  ...commissionClause(),

  clause("Probation"),
  sub("The first three (3) months of employment shall be a probationary period. During probation, either Party may terminate this Agreement by giving seven (7) days' written notice. On successful completion, the Employee's appointment shall be confirmed in writing."),

  clause("Working Hours and Attendance"),
  sub("The Employee shall observe the working days, hours and attendance procedures communicated by the Company, and shall inform the Company in advance of any absence or delay."),
  sub("Unauthorised absence for three (3) or more consecutive working days without a reasonable explanation may be treated as abandonment of employment."),

  clause("Leave"),
  sub("The Employee shall be entitled to leave in accordance with the Company's leave policy and applicable law. All leave must be requested in advance and approved by the Company, except in case of genuine emergency or illness, which must be reported as soon as possible."),

  clause("Confidentiality and Company Secrets"),
  sub(["“Confidential Information” means all information about the Company and its business that is not publicly available, whether written, electronic or verbal, including in particular: (i) client, employer and partner lists and their contact details; (ii) job orders, demand letters, visa quotas and recruitment requirements; (iii) overseas partners, agents, OEPs and other business relationships; (iv) fees, pricing, cost structures, margins, commission rates and all financial information; (v) the candidate database and candidates' personal data and documents; (vi) business methods, processes, templates, strategies and plans; and (vii) any other information marked or reasonably understood to be confidential."]),
  sub("The Employee shall not, during or after employment, disclose any Confidential Information to any person — including other recruitment agencies, OEPs, agents, candidates, competitors, friends or family members — or use it for their own benefit or for the benefit of anyone other than the Company."),
  sub("The Employee shall not copy, download, photograph, forward to a personal email, phone or messaging account, or remove from the Company's systems or premises any Confidential Information, except as strictly necessary to perform their duties and as authorised by the Company."),
  sub("These restrictions shall not apply to disclosure required by law or by order of a competent authority, provided the Employee first informs the Company where lawfully permitted."),
  sub("The obligations in this clause shall continue during employment and indefinitely after this Agreement ends, for any reason. Any breach of this clause shall be treated as gross misconduct."),

  clause(e.propertyClause.title),
  ...e.propertyClause.items.map(sub),

  clause("Non-Solicitation and Non-Circumvention"),
  sub("During employment and for a period of twelve (12) months after it ends, the Employee shall not, directly or indirectly, solicit, approach or deal with any client, employer, overseas partner, agent or candidate of the Company with whom the Employee dealt, or about whom the Employee received Confidential Information, during their employment, for the purpose of providing services that compete with the Company."),
  sub("The Employee shall not bypass the Company to deal directly, or through any other person or agency, with any client, partner or candidate introduced to the Employee through the Company."),
  sub("During the same period, the Employee shall not induce or encourage any employee of the Company to leave the Company."),

  clause("Integrity and Handling of Payments"),
  sub("The Employee shall not demand, accept or receive any money, fee, gift, commission or other benefit from any candidate, client, partner, vendor or other person in connection with the Company's business, other than the remuneration paid by the Company under this Agreement."),
  sub("All payments from candidates and clients shall be made only to the Company's official bank account or against an official Company receipt. The Employee shall not collect any payment in their personal name or account."),
  sub("The Employee shall not make any false or misleading promise or statement to any candidate or client regarding jobs, visas, salaries, timelines or costs, and shall not prepare, alter or submit any forged, false or misleading document."),
  sub("Any breach of this clause shall be treated as gross misconduct, and the Company may also take legal action and report the matter to the relevant authorities."),

  clause("Conflict of Interest and Exclusivity"),
  sub("The Employee shall devote their working time and attention to the Company's business and shall promptly disclose to the Company any personal or financial interest that conflicts, or may conflict, with the interests of the Company."),
  sub("During employment, the Employee shall not, without the Company's prior written consent, work for, advise or hold any interest in any other recruitment agency, OEP, travel or visa consultancy, or any other business that competes with the Company."),

  clause("Conduct and Public Statements"),
  sub("The Employee shall act professionally and honestly, comply with the Company's policies and lawful instructions, and shall not engage in any activity that harms the Company's interests or reputation."),
  sub("The Employee shall not make any public statement or social media post about the Company, its clients, partners or candidates, and shall not use the Company's name, logo or materials for personal purposes, without the Company's prior approval."),

  clause("Compliance with Laws"),
  sub("The Employee shall comply with all applicable laws of Pakistan, including the Emigration Ordinance, 1979 and the rules made under it, and with the requirements of destination countries as instructed by the Company, in the course of their duties."),
  sub("The Employee shall handle all personal data of candidates, clients and staff lawfully, securely and only for the Company's legitimate business purposes."),

  clause("Company Systems and Equipment"),
  sub("All Company email accounts, phone numbers, messaging accounts, software, devices and equipment provided to or used by the Employee for work are the property of the Company and shall be used only for the Company's business."),
  sub("The Company may access and review its accounts, systems and records, including work communications, for legitimate business purposes."),

  clause("Termination"),
  sub("After confirmation, either Party may terminate this Agreement by giving one (1) month's written notice, or salary in lieu of notice."),
  sub("The Company may terminate this Agreement immediately and without notice in case of gross misconduct, including breach of the Confidentiality and Company Secrets or Integrity and Handling of Payments clauses, dishonesty, fraud, gross negligence, unauthorised absence, or any other material breach of this Agreement."),
  sub("Upon termination, the Employee shall immediately return all Company property, documents, files, data and equipment, hand over all account credentials, and shall not retain any copies. Final dues shall be settled after a complete handover."),

  clause("Consequences of Breach"),
  sub("The Employee shall be liable for any loss or damage suffered by the Company as a result of the Employee's breach of this Agreement, wilful misconduct or negligence, and the Company may recover such amounts as permitted by law."),
  sub("Because a breach of the confidentiality, non-solicitation or integrity obligations may cause the Company harm that cannot be adequately compensated by money, the Company shall be entitled to seek injunctive relief from a competent court, in addition to any other remedy."),

  clause("General"),
  sub("Notices under this Agreement shall be given in writing and delivered by hand, courier or email to the address or email of the receiving Party on the Company's records."),
  sub("If any provision of this Agreement is found invalid or unenforceable, it shall be enforced to the maximum extent permitted, and the remaining provisions shall continue in full force."),
  sub("The Employee may not assign or transfer any rights or obligations under this Agreement. No failure or delay by the Company in enforcing any provision shall be treated as a waiver of it."),

  clause("Governing Law and Disputes"),
  sub("This Agreement shall be governed by the laws of the Islamic Republic of Pakistan. The Parties shall first attempt to resolve any dispute amicably; failing which, it shall be referred to the competent courts at Rawalpindi."),

  clause("Entire Agreement"),
  sub("This Agreement constitutes the entire agreement between the Parties regarding the employment and supersedes any prior understanding. Any amendment shall be valid only if made in writing and signed by both Parties. The Employee confirms that they have read and understood this Agreement and sign it voluntarily."),

  new Paragraph({ spacing: { before: 280, after: 200 }, keepNext: true,
    children: [r("IN WITNESS WHEREOF, the Parties have signed this Agreement on the date first written above.")] }),
  sigBlock(
    ["For and on behalf of the Company", COMPANY, "", "Signature: ______________________", "Name: __________________________", "Designation: ____________________", "Company Stamp:"],
    ["Employee", `${e.name}`, "", "Signature: ______________________", `CNIC: ${e.cnic}`, "Date: ___________________________"],
  ),
  new Paragraph({ spacing: { before: 280, after: 80 }, keepNext: true, children: [b("Witnesses", { color: BRAND })] }),
  sigBlock(
    ["Witness 1", "Name: __________________________", "CNIC: __________________________", "Signature: ______________________"],
    ["Witness 2", "Name: __________________________", "CNIC: __________________________", "Signature: ______________________"],
  ),
];

const doc = new Document({
  creator: COMPANY,
  title: `Employment Agreement - ${e.name}`,
  styles: { default: { document: { run: { font: FONT, size: 22 } } } },
  numbering: { config: [{ reference: "sub", levels: [{ level: 0, format: LevelFormat.LOWER_LETTER,
    text: "(%1)", alignment: AlignmentType.LEFT,
    style: { paragraph: { indent: { left: 720, hanging: 400 } } } }] }] },
  sections: [{
    properties: {
      titlePage: true,
      // Body sits between the letterhead's REF/DATE line and its tagline band.
      page: { margin: { top: 3500, bottom: 2400, left: MARGIN_X, right: MARGIN_X, header: 0, footer: 1750 } },
    },
    headers: { first: background("first.jpg"), default: background("cont.jpg") },
    footers: { first: footer, default: footer },
    children: body,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(outFile, buf);
  console.log(`Wrote ${outFile}`);
});

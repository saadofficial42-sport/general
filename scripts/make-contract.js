// Generates an employment contract (.docx) on RS Links Consultants letterhead.
// Usage: node scripts/make-contract.js contracts/<employee>.json [out.docx]
// If contracts/letterhead.png exists it is used as the page header image;
// otherwise a text letterhead is rendered.

const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Header, Footer, ImageRun, Table,
  TableRow, TableCell, WidthType, BorderStyle, AlignmentType, PageNumber,
  LevelFormat, ShadingType,
} = require("docx");

const COMPANY = "RS Links Consultants (Pvt.) Ltd.";
const BRAND = "1F3A5F";
const FONT = "Calibri";

const inFile = process.argv[2];
if (!inFile) {
  console.error("Usage: node scripts/make-contract.js <employee.json> [out.docx]");
  process.exit(1);
}
const e = JSON.parse(fs.readFileSync(inFile, "utf8"));
const outFile = process.argv[3] || inFile.replace(/\.json$/, ".docx");
const letterheadPath = path.join(path.dirname(inFile), "letterhead.png");
const salary = `PKR ${e.salaryPkr.toLocaleString("en-US")}/-`;

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
const sub = (children) => new Paragraph({
  children: (Array.isArray(children) ? children : [children]).map((c) => (typeof c === "string" ? r(c) : c)),
  numbering: { reference: "sub", level: 0, instance: clauseNo },
  spacing: { after: 80, line: 276 }, alignment: AlignmentType.JUSTIFIED,
});

function letterhead() {
  if (fs.existsSync(letterheadPath)) {
    return [new Paragraph({ alignment: AlignmentType.CENTER, children: [
      new ImageRun({ type: "png", data: fs.readFileSync(letterheadPath),
        transformation: { width: 600, height: 90 } }),
    ] })];
  }
  return [
    new Paragraph({ alignment: AlignmentType.LEFT, spacing: { after: 0 }, children: [
      b("RS LINKS CONSULTANTS", { size: 34, color: BRAND, characterSpacing: 20 }),
      r("  (PVT.) LTD.", { size: 20, color: BRAND, bold: true }),
    ] }),
    new Paragraph({
      spacing: { after: 0 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: BRAND, space: 4 } },
      children: [],
    }),
  ];
}

const footer = new Footer({ children: [
  new Paragraph({
    alignment: AlignmentType.CENTER,
    border: { top: { style: BorderStyle.SINGLE, size: 6, color: BRAND, space: 4 } },
    children: [
      r(`${COMPANY}  |  Employment Agreement — ${e.name}  |  Page `, { size: 16, color: "666666" }),
      new TextRun({ children: [PageNumber.CURRENT], size: 16, color: "666666", font: FONT }),
      r(" of ", { size: 16, color: "666666" }),
      new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 16, color: "666666", font: FONT }),
    ],
  }),
] });

// Key-terms summary table
const W = 9026; // A4 text width at 1" margins (DXA)
const COLS = [2800, W - 2800];
const cellBorder = { style: BorderStyle.SINGLE, size: 4, color: "BFC8D6" };
const borders = { top: cellBorder, bottom: cellBorder, left: cellBorder, right: cellBorder };
const row = (k, v) => new TableRow({ children: [
  new TableCell({ width: { size: COLS[0], type: WidthType.DXA }, borders,
    shading: { type: ShadingType.CLEAR, fill: "EAF0F7", color: "auto" },
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
    children: lines.map((l, i) => new Paragraph({ spacing: { after: 60 },
      children: [i === 0 ? b(l, { color: BRAND }) : r(l)] })) });
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [half, half],
    rows: [new TableRow({ children: [col(left), col(right)] })] });
};

const body = [
  new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { after: 200 },
    children: [r(`Date: ${e.contractDate}`)] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 },
    children: [b("EMPLOYMENT AGREEMENT", { size: 32, color: BRAND })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 240 },
    children: [r(e.position, { size: 24, italics: true })] }),

  p([r("This Employment Agreement (the "), b("“Agreement”"), r(") is made and entered into on the date stated above by and between:")]),
  p([b(COMPANY), r(", a private limited company incorporated under the laws of Pakistan (hereinafter the "), b("“Company”"), r(", which expression shall include its successors and assigns);")]),
  p([b("AND", { color: BRAND })], { alignment: AlignmentType.CENTER }),
  p([b(`${e.salutation} ${e.name}`), r(`, ${e.relation} ${e.fatherName}, holding CNIC No. `), b(e.cnic), r(" (hereinafter the "), b("“Employee”"), r(").")]),
  p("The Company and the Employee are each referred to as a “Party” and together as the “Parties”. The Parties agree to the following terms and conditions."),

  new Paragraph({ spacing: { before: 120, after: 100 }, children: [b("KEY TERMS", { color: BRAND })] }),
  terms,

  clause("Appointment and Position"),
  sub(["The Company appoints the Employee to the position of ", b(e.position), " with effect from the Date of Joining stated above, and the Employee accepts this appointment on the terms of this Agreement."]),
  sub("The Employee shall report to the Company's management or to such person as the Company may designate from time to time."),

  clause("Duties and Responsibilities"),
  sub("The Employee shall be responsible for planning, creating and publishing content across the Company's social media channels; managing posting calendars; engaging with followers and responding to messages and comments in a timely and professional manner; running and monitoring campaigns; and reporting on reach, engagement and performance."),
  sub("The Employee shall perform such other related duties as may reasonably be assigned by the Company, and shall carry out all duties diligently, honestly and to the best of their ability."),
  sub("The Employee shall not publish any content on behalf of the Company that has not been approved in line with the Company's instructions, and shall comply with the policies of each social media platform."),

  clause("Mode of Work"),
  sub(["The Employee shall work on a ", b("remote"), " basis and is not required to attend the Company's office on a regular basis, unless specifically requested by the Company with reasonable notice."]),
  sub("The Employee shall be available and reachable through the Company's agreed communication channels during working hours, attend scheduled online meetings, and maintain a reliable internet connection and suitable workspace at their own cost."),
  sub("Working hours shall be as communicated by the Company from time to time. Social media duties may occasionally require reasonable availability outside normal hours."),

  clause("Remuneration"),
  sub(["The Employee shall be paid a fixed monthly salary of ", b(salary), ` (${e.salaryWords} only).`]),
  sub(["The salary shall be disbursed ", b(e.payDay), " for the preceding month of service, by bank transfer or any other mode agreed between the Parties."]),
  sub("Salary for any incomplete month of service shall be calculated on a pro-rata basis. Any applicable taxes shall be deducted in accordance with the laws of Pakistan."),

  clause("Probation"),
  sub("The first three (3) months of employment shall be a probationary period. During probation, either Party may terminate this Agreement by giving seven (7) days' written notice. On successful completion, the Employee's appointment shall be confirmed in writing."),

  clause("Leave"),
  sub("The Employee shall be entitled to leave in accordance with the Company's leave policy and applicable law. All leave must be requested in advance and approved by the Company, except in case of genuine emergency or illness, which must be reported as soon as possible."),

  clause("Confidentiality"),
  sub("The Employee shall keep strictly confidential all information relating to the Company, its clients, candidates, partners, pricing, business plans and operations, and shall not disclose or use such information except for the performance of their duties."),
  sub("This obligation shall continue during employment and after this Agreement ends, for any reason."),

  clause("Company Accounts and Intellectual Property"),
  sub("All content, designs, graphics, videos, captions and other material created by the Employee in the course of employment shall be the sole property of the Company."),
  sub("All login credentials and access to the Company's social media accounts, tools and pages are the property of the Company. The Employee shall not change passwords, remove administrators or transfer ownership without written approval, and shall hand over all credentials and access on the termination of employment."),

  clause("Conduct and Exclusivity"),
  sub("The Employee shall act professionally, comply with the Company's policies and lawful instructions, and shall not engage in any activity that conflicts with the interests of the Company or harms its reputation."),
  sub("The Employee shall not, without prior written consent of the Company, undertake similar work for any competing business during the term of employment."),

  clause("Termination"),
  sub("After confirmation, either Party may terminate this Agreement by giving one (1) month's written notice, or salary in lieu of notice."),
  sub("The Company may terminate this Agreement immediately and without notice in case of misconduct, breach of confidentiality, dishonesty, gross negligence, or a material breach of this Agreement."),
  sub("Upon termination, the Employee shall return all Company property, files and data, and hand over all account credentials. Final dues shall be settled after a complete handover."),

  clause("Governing Law and Disputes"),
  sub("This Agreement shall be governed by the laws of the Islamic Republic of Pakistan. The Parties shall first attempt to resolve any dispute amicably; failing which, it shall be referred to the competent courts of Pakistan."),

  clause("Entire Agreement"),
  sub("This Agreement constitutes the entire agreement between the Parties regarding the employment and supersedes any prior understanding. Any amendment shall be valid only if made in writing and signed by both Parties."),

  new Paragraph({ spacing: { before: 280, after: 200 }, keepNext: true,
    children: [r("IN WITNESS WHEREOF, the Parties have signed this Agreement on the date first written above.")] }),
  sigBlock(
    ["For and on behalf of the Company", COMPANY, "", "Signature: ______________________", "Name: __________________________", "Designation: ____________________", "Company Stamp:"],
    ["Employee", `${e.name}`, "", "Signature: ______________________", `CNIC: ${e.cnic}`, "Date: ___________________________"],
  ),
  new Paragraph({ spacing: { before: 280, after: 80 }, children: [b("Witnesses", { color: BRAND })] }),
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
    properties: { page: { margin: { top: 1700, bottom: 1300, left: 1440, right: 1440, header: 500, footer: 500 } } },
    headers: { default: new Header({ children: letterhead() }) },
    footers: { default: footer },
    children: body,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(outFile, buf);
  console.log(`Wrote ${outFile}`);
});
